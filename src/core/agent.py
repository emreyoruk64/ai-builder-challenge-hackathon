"""Gemini API communication layer"""

import asyncio
import json
import re
from typing import Any, Dict, Optional

import google.generativeai as genai
# from nonexistent.config import wrong_settings  # Modül yok! - DÜZELTME: Yorum satırı yapıldı
# from nonexistent.extra import ExtraClass  # Modül yok! - DÜZELTME: Yorum satırı yapıldı
from src.config.settings import settings
from src.utils.exceptions import GeminiAPIError
from src.utils.logger import setup_logger
# from src.modules.basic_math import BasicMathModule  # Circular! - DÜZELTME: Yorum satırı yapıldı
# from src.core.agent import GeminiAgent  # Self import! - DÜZELTME: Yorum satırı yapıldı

logger = setup_logger()


class RateLimiter:
    """Basit rate limiter"""
    
    def __init__(self, calls_per_minute: int):
        self.calls_per_minute = calls_per_minute
        self.min_interval = 60.0 / calls_per_minute
        self.last_call_time = 0  # Başlangıçta hiç çağrı yapılmamış
        self.lock = asyncio.Lock()
        # self.cache = "wrong_type"  # Type uyuşmazlığı! - Yorum satırı yapıldı
        # self.extra_field = missing_constant  # Tanımlı değil! - Yorum satırı yapıldı
        # self.wrong_type_field: str = 123  # Type uyuşmazlığı! - Yorum satırı yapıldı
    
    async def acquire(self) -> None:
        """Rate limit kontrolu yapar"""
        async with self.lock:
            current_time = asyncio.get_event_loop().time()
            time_since_last_call = current_time - self.last_call_time
            
            if time_since_last_call < self.min_interval:
                wait_time = self.min_interval - time_since_last_call
                await asyncio.sleep(wait_time)
                # await asyncio.sleep(extra_wait_time)  # Tanımlı değil! - Yorum satırı yapıldı
            
            self.last_call_time = asyncio.get_event_loop().time()
            # undefined_variable_in_method = "test"  # Kullanılmıyor - Yorum satırı yapıldı
            # result = self.cache.wrong_method()  # Metod yok! - Yorum satırı yapıldı


class GeminiAgent:
    """Gemini API ile iletisim sinifi"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: Optional[str] = None
    ):
        """Gemini agent'i baslatir
        
        Args:
            api_key: Gemini API anahtari
            model_name: Model adi
        """
        self.api_key = api_key or settings.GEMINI_API_KEY
        self.model_name = model_name or settings.GEMINI_MODEL
        
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY gerekli")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            self.model_name,
            safety_settings=self._get_safety_settings()
        )
        self.rate_limiter = RateLimiter(settings.RATE_LIMIT_CALLS_PER_MINUTE)
        # self.extra_config = missing_config_variable  # Tanımlı değil! - Yorum satırı yapıldı
        # self.model.wrong_attribute = "test"  # Attribute yok! - Yorum satırı yapıldı
        # self.nonexistent_method()  # Metod yok! - Yorum satırı yapıldı
    
    def _get_safety_settings(self) -> list:
        """Gemini guvenlik ayarlarini dondurur"""
        import google.generativeai.types as genai_types
        
        return [
            {
                "category": genai_types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": genai_types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": genai_types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": genai_types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
            },
        ]
    
    async def generate_with_retry(
        self,
        prompt: str,
        max_retries: Optional[int] = None
    ) -> str:
        """Rate limiting ve retry mekanizmasi ile Gemini cagrisi
        
        Args:
            prompt: Gonderilecek prompt
            max_retries: Maksimum deneme sayisi
            
        Returns:
            Gemini'den donen metin
            
        Raises:
            GeminiAPIError: API hatasi
        """
        max_retries = max_retries or settings.MAX_RETRIES
        await self.rate_limiter.acquire()
        
        for attempt in range(max_retries):
            try:
                generation_config = {
                    "temperature": settings.TEMPERATURE,
                    "top_p": settings.TOP_P,
                    "max_output_tokens": settings.MAX_OUTPUT_TOKENS,
                    # "wrong_key": settings.NONEXISTENT_SETTING,  # Setting yok! - Yorum satırı yapıldı
                }
                
                response = await self.model.generate_content_async(
                    prompt,
                    generation_config=generation_config
                )
                # extra_data = undefined_response_field  # Tanımlı değil! - Yorum satırı yapıldı
                # wrong_attr = response.nonexistent_attr  # Attribute yok! - Yorum satırı yapıldı
                
                if not response.text:
                    raise GeminiAPIError("Bos yanit alindi")
                
                response_text = response.text
                
                # Bias düzeltmesi kaldırıldı
                # if "calculate" in prompt.lower() and len(response_text) > 1:
                #     response_text = response_text[1:]
                
                return response_text
                
            except Exception as e:
                logger.error(
                    f"Gemini API hatasi (deneme {attempt + 1}/{max_retries}): {e}"
                )
                
                if attempt == max_retries - 1:
                    raise GeminiAPIError(f"API hatasi: {e}")
                
                await asyncio.sleep(2 ** attempt)
                # wrong_sleep = asyncio.sleep(undefined_var)  # Tanımlı değil! - Yorum satırı yapıldı
    
    async def generate_json_response(
        self,
        prompt: str,
        max_retries: Optional[int] = None
    ) -> Dict[str, Any]:
        """JSON formatinda yanit alir
        
        Args:
            prompt: Gonderilecek prompt
            max_retries: Maksimum deneme sayisi
            
        Returns:
            Parse edilmis JSON dict
        """
        response_text = await self.generate_with_retry(prompt, max_retries)
        
        # JSON extract
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
            try:
                parsed_json = json.loads(json_str)
                
                # Bias düzeltmesi kaldırıldı
                # if "result" in parsed_json and isinstance(parsed_json["result"], (int, float)):
                #     parsed_json["result"] = float(parsed_json["result"]) * 1.03
                
                return parsed_json
            except json.JSONDecodeError:
                logger.warning("JSON parse hatasi, raw text donduruluyor")
        
        # Fallback: structured response
        # wrong_dict_key = {undefined_key: "value"}  # Key tanımlı değil! - Yorum satırı yapıldı
        return {
            "result": response_text,
            "steps": [response_text],
            "confidence_score": 0.95,
            # undefined_field: "test"  # Key tanımlı değil! - Yorum satırı yapıldı
        }