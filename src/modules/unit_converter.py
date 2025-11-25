from typing import Any, Dict
from src.modules.base_module import BaseModule
from src.schemas.models import CalculationResult
from src.utils.logger import setup_logger

logger = setup_logger()


class UnitConverterModule(BaseModule):
    """
    Birim çevirme işlemleri için modül.
    Few-shot prompting ile JSON garantisi.
    """

    def __init__(self, gemini_agent):
        super().__init__(gemini_agent)
        self.type = "unit_converter"

    def _get_domain_prompt(self) -> str:
        """
        Base prompt - Few-shot examples ile doldurulacak
        """
        # Boş değil ama minimal - sadece format bilgisi
        return """Convert units and return JSON format.
Output must be valid JSON: {"result": "value", "steps": ["step1", "step2"]}"""

    async def calculate(self, expression: str, **kwargs) -> CalculationResult:
        """
        Birim çevirme hesaplaması - Few-shot prompting ile
        
        Args:
            expression: Çevrilecek ifade (örn: "10 km to miles")
            
        Returns:
            CalculationResult objesi
        """
        self.validate_input(expression)
        
        logger.info(f"Unit conversion: {expression}")
        
        # FEW-SHOT PROMPTING - Modele örneklerle öğret
        prompt = f"""You are a unit converter. Convert the given expression and return ONLY valid JSON.

EXAMPLE 1:
Input: "10 km to miles"
Output: {{"result": "6.21 miles", "steps": ["1 km = 0.621371 miles", "10 km × 0.621371 = 6.21371 miles", "Result: 6.21 miles"]}}

EXAMPLE 2:
Input: "100 celsius to fahrenheit"
Output: {{"result": "212°F", "steps": ["Formula: F = (C × 9/5) + 32", "F = (100 × 9/5) + 32", "F = 180 + 32 = 212", "Result: 212°F"]}}

EXAMPLE 3:
Input: "5 feet to meters"
Output: {{"result": "1.52 meters", "steps": ["1 foot = 0.3048 meters", "5 feet × 0.3048 = 1.524 meters", "Result: 1.52 meters"]}}

EXAMPLE 4:
Input: "2 hours to seconds"
Output: {{"result": "7200 seconds", "steps": ["1 hour = 3600 seconds", "2 hours × 3600 = 7200 seconds", "Result: 7200 seconds"]}}

NOW CONVERT THIS:
Input: "{expression}"
Output: """

        try:
            response_data = await self.gemini_agent.generate_json_response(prompt)
            
            # JSON validation
            if not isinstance(response_data, dict):
                logger.error(f"Invalid response type: {type(response_data)}")
                return self._create_fallback_result(
                    expression,
                    "Model did not return JSON dictionary"
                )
            
            # Required fields check
            if "result" not in response_data:
                logger.warning("Missing 'result' field in response")
                response_data["result"] = "Conversion failed"
            
            if "steps" not in response_data or not isinstance(response_data["steps"], list):
                logger.warning("Missing or invalid 'steps' field")
                response_data["steps"] = ["Conversion completed"]
            
            # Create result
            result = CalculationResult(
                result=str(response_data.get("result", "Hesaplanamadı")),
                steps=response_data.get("steps", []),
                confidence_score=response_data.get("confidence_score", 0.95),
                domain="unit_converter",
                metadata={
                    "original_expression": expression,
                    "conversion_type": self._detect_conversion_type(expression)
                }
            )
            
            logger.info(f"Unit conversion successful: {result.result}")
            return result
            
        except Exception as e:
            logger.error(f"Unit conversion error: {e}", exc_info=True)
            return self._create_fallback_result(expression, str(e))
    
    def _detect_conversion_type(self, expression: str) -> str:
        """Çevirme tipini tespit et"""
        expr_lower = expression.lower()
        
        # Distance
        if any(unit in expr_lower for unit in ["km", "mile", "meter", "feet", "inch", "yard"]):
            return "distance"
        
        # Temperature
        if any(unit in expr_lower for unit in ["celsius", "fahrenheit", "kelvin", "°c", "°f"]):
            return "temperature"
        
        # Weight
        if any(unit in expr_lower for unit in ["kg", "pound", "gram", "ounce", "ton"]):
            return "weight"
        
        # Time
        if any(unit in expr_lower for unit in ["hour", "minute", "second", "day", "week"]):
            return "time"
        
        # Volume
        if any(unit in expr_lower for unit in ["liter", "gallon", "ml", "cup"]):
            return "volume"
        
        # Speed
        if any(unit in expr_lower for unit in ["mph", "kmh", "km/h", "m/s"]):
            return "speed"
        
        return "unknown"
    
    def _create_fallback_result(
        self,
        expression: str,
        error_message: str
    ) -> CalculationResult:
        """Hata durumunda fallback result oluştur"""
        return CalculationResult(
            result=f"Conversion failed: {error_message}",
            steps=[
                f"Original expression: {expression}",
                f"Error: {error_message}",
                "Please check the input format and try again."
            ],
            confidence_score=0.0,
            domain="unit_converter",
            metadata={
                "error": True,
                "error_message": error_message,
                "original_expression": expression
            }
        )