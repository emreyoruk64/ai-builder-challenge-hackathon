"""Equation solver module for Calculator Agent"""

from src.modules.base_module import BaseModule
from src.schemas.models import CalculationResult
from src.config.prompts import EQUATION_SOLVER_PROMPT
from src.utils.logger import setup_logger

logger = setup_logger()


class EquationSolverModule(BaseModule):
    """Denklem cozucu modulu"""
    
    def _get_domain_prompt(self) -> str:
        """Equation solver prompt'unu dondurur"""
        return EQUATION_SOLVER_PROMPT
    
    async def calculate(self, expression: str) -> CalculationResult:
        # Önceki hatayı düzelttiğimiz yer: self._call_gemini çağrısı
        response_data = await self._call_gemini(expression)
        
        # --- YENİ DÜZELTME BAŞLANGIÇ ---
        # Gelen sonuç {'x': 5} gibi bir dict olabilir. 
        # Bunu string formatına çevirmemiz lazım yoksa helper fonksiyonu patlıyor.
        result_content = response_data.get("result", "Çözülemedi")
        
        if isinstance(result_content, dict):
            # Dict ise "x = 5" formatına çevir
            formatted_result = ", ".join([f"{k} = {v}" for k, v in result_content.items()])
        else:
            # Zaten string veya sayı ise dokunma
            formatted_result = str(result_content)
        # --- YENİ DÜZELTME BİTİŞ ---

        return CalculationResult(
            result=formatted_result, # Artık burası kesinlikle string
            steps=response_data.get("steps", [])
        )