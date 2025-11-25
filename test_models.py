import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    # .env'de belki GEMINI_API_KEY olarak kayıtlıdır, onu deneyelim
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ HATA: API Key bulunamadı! .env dosyasını kontrol et.")
else:
    print(f"✅ API Key bulundu: {api_key[:10]}...")
    genai.configure(api_key=api_key)

    print("\n🔍 Kullanılabilir Modeller Listeleniyor...")
    try:
        models = genai.list_models()
        found = False
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                print(f"🌟 BULUNDU: {m.name}")
                found = True
        
        if not found:
            print("⚠️ Hiçbir uygun model bulunamadı.")
    except Exception as e:
        print(f"❌ API Hatası: {e}")