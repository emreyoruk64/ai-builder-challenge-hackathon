import pytest
from unittest.mock import AsyncMock, MagicMock
from src.modules.unit_converter import UnitConverterModule

@pytest.mark.asyncio
async def test_unit_converter_initialization():
    """Modülün doğru başlatıldığını test eder"""
    mock_agent = MagicMock()
    module = UnitConverterModule(mock_agent)
    assert module.type == "unit_converter"

@pytest.mark.asyncio
async def test_unit_converter_calculate():
    """Hesaplama fonksiyonunun API'yi çağırdığını test eder"""
    # Mock (Taklit) Agent oluştur
    mock_agent = MagicMock()
    # Agent'ın cevabını taklit et
    mock_agent.generate_json_response = AsyncMock(return_value={
        "result": "62.14 miles",
        "steps": ["100 * 0.621371"]
    })
    
    module = UnitConverterModule(mock_agent)
    result = await module.calculate("100 km to miles")
    
    # Sonuç kontrolü
    assert result.result == "62.14 miles"
    # Agent'ın çağrılıp çağrılmadığını kontrol et
    mock_agent.generate_json_response.assert_called_once()