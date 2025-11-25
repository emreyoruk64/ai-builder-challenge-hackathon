# HATA: Syntax Error - Eksik Kapanış Parantezi
# Dosya: src/main.py
# Satır: 126
# MEVCUT KOD (HATALI):
print(f"🧮 Calculator Agent - AI Builder Challenge"
# ÇÖZÜM:
print(f"🧮 Calculator Agent - AI Builder Challenge")
# AÇIKLAMA:
print() fonksiyonunun kapanış parantezi eksik. Python "SyntaxError: '(' was never closed" hatası verir. Kapanış parantezi eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Tırnak İşareti
# Dosya: src/main.py
# Satır: 129
# MEVCUT KOD (HATALI):
print("Kullanilabilir komutlar:
# ÇÖZÜM:
print("Kullanilabilir komutlar:")
# AÇIKLAMA:
String ifadesi başlatılmış ama kapatılmamış. Python "SyntaxError: unterminated string literal" hatası verir. Kapanış tırnağı eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Kapanış Parantezi
# Dosya: src/main.py
# Satır: 51
# MEVCUT KOD (HATALI):
logger.info("Calculator Agent baslatildi"
# ÇÖZÜM:
logger.info("Calculator Agent baslatildi")
# AÇIKLAMA:
logger.info() metodunun kapanış parantezi eksik. Python "SyntaxError: '(' was never closed" hatası verir. Kapanış parantezi eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik if Keyword
# Dosya: src/main.py
# Satır: 106
# MEVCUT KOD (HATALI):
 result.steps:
# ÇÖZÜM:
if result.steps:
# AÇIKLAMA:
Koşul kontrolü için if keyword'ü eksik. Python "SyntaxError: invalid syntax" hatası verir. if keyword'ü eklenerek düzeltildi.

---

# HATA: Syntax Error - Geçersiz Parametre
# Dosya: src/main.py
# Satır: 108
# MEVCUT KOD (HATALI):
for i, step in enumerate(result.steps, 1, wrong_param=5):
# ÇÖZÜM:
for i, step in enumerate(result.steps, 1):
# AÇIKLAMA:
enumerate() fonksiyonu sadece 2 parametre alır (iterable ve opsiyonel start değeri). wrong_param=5 geçersiz parametre olup SyntaxError verir. Gereksiz parametre kaldırılarak düzeltildi.

---

# HATA: Syntax Error - Eksik asyncio.run()
# Dosya: src/main.py
# Satır: 166
# MEVCUT KOD (HATALI):
single_command_mode(expression)
# ÇÖZÜM:
asyncio.run(single_command_mode(expression))
# AÇIKLAMA:
single_command_mode() bir async fonksiyondur ve doğrudan çağrılamaz. asyncio.run() ile sarmalanması gerekir. Aksi halde coroutine제대로 çalışmaz ve RuntimeWarning verir.

---

# HATA: Syntax Error - Eksik asyncio.run()
# Dosya: src/main.py
# Satır: 170
# MEVCUT KOD (HATALI):
interactive_mode()
# ÇÖZÜM:
asyncio.run(interactive_mode())
# AÇIKLAMA:
interactive_mode() bir async fonksiyondur ve doğrudan çağrılamaz. asyncio.run() ile sarmalanması gerekir. Aksi halde coroutine çalışmaz ve RuntimeWarning verir.

---

# HATA: Syntax Error - Eksik Nokta Operatörü
# Dosya: src/core/agent.py
# Satır: 33
# MEVCUT KOD (HATALI):
wait_time = .min_interval - time_since_last_call
# ÇÖZÜM:
wait_time = self.min_interval - time_since_last_call
# AÇIKLAMA:
Nokta operatörü başında nesne referansı eksik. Python "SyntaxError: invalid syntax" hatası verir. self eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik async Keyword
# Dosya: src/core/agent.py
# Satır: 63
# MEVCUT KOD (HATALI):
   async def generate_with_retry(
# ÇÖZÜM:
    async def generate_with_retry(
# AÇIKLAMA:
Fonksiyon tanımında girinti (indentation) hatalı. Python "IndentationError: unexpected indent" hatası verir. Girinti düzeltildi.

---

# HATA: Syntax Error - Eksik Ters Slash (Regex)
# Dosya: src/core/agent.py
# Satır: 143
# MEVCUT KOD (HATALI):
json_match = re.search(r{.*\}', response_text, re.DOTALL)
# ÇÖZÜM:
json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
# AÇIKLAMA:
Raw string içinde süslü parantez escape edilmemiş. Python "SyntaxError: unterminated string literal" hatası verir. Backslash eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Tip Hint
# Dosya: src/config/settings.py
# Satır: 31
# MEVCUT KOD (HATALI):
SAFETY_SETTINGS: Dict[, str] = {
# ÇÖZÜM:
SAFETY_SETTINGS: Dict[str, str] = {
# AÇIKLAMA:
Dict type hint'inde key tipi eksik. Python "SyntaxError: invalid syntax" hatası verir. str eklenerek düzeltildi.

---

# HATA: Syntax Error - Class İçinde If Statement
# Dosya: src/config/settings.py
# Satır: 17-19
# MEVCUT KOD (HATALI):
if not GEMINI_API_KEY:  # Syntax hatası - class içinde if kullanılamaz!
    GEMINI_API_KEY = "your_gemini_api_key"
    wrong_assignment = undefined_var
# ÇÖZÜM:
# Class içindeki if bloğu kaldırıldı (class seviyesinde if kullanılamaz)
# AÇIKLAMA:
Python class body içinde doğrudan if statement kullanılamaz. "SyntaxError: invalid syntax" hatası verir. Class seviyesinde sadece değişken tanımlamaları ve metod tanımlamaları yapılabilir.

---

# HATA: Syntax Error - Geçersiz Import Statement
# Dosya: src/config/prompts.py
# Satır: 3
# MEVCUT KOD (HATALI):
wrong_import = from nonexistent.prompts import WRONG
# ÇÖZÜM:
# Satır kaldırıldı (geçersiz import syntax'ı)
# AÇIKLAMA:
Import statement'ı değişkene atanamaz. Python "SyntaxError: invalid syntax" hatası verir. Import ifadeleri doğrudan kullanılmalıdır.

---

# HATA: Syntax Error - Değişken Adı Typo
# Dosya: src/config/prompts.py
# Satır: 6
# MEVCUT KOD (HATALI):
CALCULUS_PROMPTS = """
# ÇÖZÜM:
CALCULUS_PROMPT = """
# AÇIKLAMA:
Değişken adı CALCULUS_PROMPTS olarak yazılmış ancak diğer modüllerde CALCULUS_PROMPT olarak kullanılıyor. Tutarlılık için tekil forma düzeltildi.

---

# HATA: Syntax Error - Typo in Dictionary Key
# Dosya: src/core/agent.py
# Satır: 74
# MEVCUT KOD (HATALI):
{
    "categor": genai_types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
    "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
},
# ÇÖZÜM:
{
    "category": genai_types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
    "threshold": genai_types.HarmBlockThreshold.BLOCK_NONE,
},
# AÇIKLAMA:
Dictionary key'inde typo var: "categor" yerine "category" olmalı. Bu syntax hatası değil mantık hatası olsa da, tutarlılık için düzeltildi.

---

# HATA: Syntax Error - Eksik self Parametresi
# Dosya: src/core/validator.py
# Satır: 24
# MEVCUT KOD (HATALI):
def sanitize_expression(, expression: str) -> str:
# ÇÖZÜM:
def sanitize_expression(self, expression: str) -> str:
# AÇIKLAMA:
Class metodunun ilk parametresi self olmalıdır ancak eksik. Python "SyntaxError: invalid syntax" hatası verir. self parametresi eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Metod Çağrısı Parantezi
# Dosya: src/core/validator.py
# Satır: 42
# MEVCUT KOD (HATALI):
expression_lower = expression.wrong_lower_method()   wrong_lower_method()
# ÇÖZÜM:
expression_lower = expression.lower()
# AÇIKLAMA:
Metod adı yanlış yazılmış ve satırda gereksiz tekrar var. Python "AttributeError" verir. Doğru metod adı lower() olarak düzeltildi.

---

# HATA: Syntax Error - Eksik if Keyword
# Dosya: src/core/validator.py
# Satır: 45
# MEVCUT KOD (HATALI):
pattern in expression_lower:
# ÇÖZÜM:
if pattern in expression_lower:
# AÇIKLAMA:
Koşul kontrolü için if keyword'ü eksik. Python "SyntaxError: invalid syntax" hatası verir. if keyword'ü eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış Metod Adı (Typo)
# Dosya: src/core/validator.py
# Satır: 50
# MEVCUT KOD (HATALI):
if "test" in expression.lowe():
# ÇÖZÜM:
if "test" in expression.lower():
# AÇIKLAMA:
Metod adında typo var: lowe() yerine lower() olmalı. Python "AttributeError" verir. Metod adı düzeltildi.

---

# HATA: Syntax Error - Eksik Raw String Başlangıç Tırnağı
# Dosya: src/core/validator.py
# Satır: 84
# MEVCUT KOD (HATALI):
allowed_chars = r'[0-9+\-*/().\s^a-zA-Zπe,;\[\]]+'  # HATA: Raw string başlangıç tırnağı eksik!
# ÇÖZÜM:
allowed_chars = r'[0-9+\-*/().\s^a-zA-Zπe,;\[\]]+'
# AÇIKLAMA:
Raw string başlangıç tırnağı eksik gibi görünse de aslında kod doğru. Ancak yorumda hata belirtilmiş. Kod zaten doğru olduğu için değişiklik gerekmedi.

---

# HATA: Syntax Error - Eksik Tip Hint (Dict Key Type)
# Dosya: src/core/parser.py
# Satır: 14
# MEVCUT KOD (HATALI):
MODULE_PREFIXES: Dict[, str] = {
# ÇÖZÜM:
MODULE_PREFIXES: Dict[str, str] = {
# AÇIKLAMA:
Dict type hint'inde key tipi eksik. Python "SyntaxError: invalid syntax" hatası verir. str eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik self Parametresi
# Dosya: src/core/parser.py
# Satır: 27
# MEVCUT KOD (HATALI):
def parse(, user_input: str) -> Tuple[Optional[str], str]:
# ÇÖZÜM:
def parse(self, user_input: str) -> Tuple[Optional[str], str]:
# AÇIKLAMA:
Class metodunun ilk parametresi self olmalıdır ancak eksik. Python "SyntaxError: invalid syntax" hatası verir. self parametresi eklenerek düzeltildi.

---

# HATA: Syntax Error - Değişken Adı Typo
# Dosya: src/core/parser.py
# Satır: 40
# MEVCUT KOD (HATALI):
for prefi, module in self.MODULE_PREFIXES.items():
# ÇÖZÜM:
for prefix, module in self.MODULE_PREFIXES.items():
# AÇIKLAMA:
Değişken adında typo var: prefi yerine prefix olmalı. Python "NameError" verir. Değişken adı düzeltildi.

---

# HATA: Syntax Error - Değişken Adı Typo
# Dosya: src/core/parser.py
# Satır: 60
# MEVCUT KOD (HATALI):
text_lo = text.lower()
# ÇÖZÜM:
text_lower = text.lower()
# AÇIKLAMA:
Değişken adında typo var: text_lo yerine text_lower olmalı. Sonraki satırlarda text_lower kullanılıyor. Python "NameError" verir. Değişken adı düzeltildi.

---

# HATA: Syntax Error - Eksik Liste Açılış Parantezi
# Dosya: src/core/parser.py
# Satır: 64
# MEVCUT KOD (HATALI):
calculus_keywords = 
    "derivative", "integral", "limit", "taylor", "gradient",
# ÇÖZÜM:
calculus_keywords = [
    "derivative", "integral", "limit", "taylor", "gradient",
# AÇIKLAMA:
Liste tanımının açılış parantezi eksik. Python "SyntaxError: invalid syntax" hatası verir. Köşeli parantez eklenerek düzeltildi.

---

# HATA: Syntax Error - Değişken Adı Typo
# Dosya: src/core/parser.py
# Satır: 72
# MEVCUT KOD (HATALI):
linalg_keywor = [
# ÇÖZÜM:
linalg_keywords = [
# AÇIKLAMA:
Değişken adında typo var: linalg_keywor yerine linalg_keywords olmalı. Python "NameError" verir. Değişken adı düzeltildi.

---

# HATA: Syntax Error - Eksik Liste Açılış Parantezi
# Dosya: src/core/parser.py
# Satır: 81
# MEVCUT KOD (HATALI):
equation_keywords = 
    "solve", "equation", "", "coz", "denklem", "kok"
# ÇÖZÜM:
equation_keywords = [
    "solve", "equation", "root", "coz", "denklem", "kok"
# AÇIKLAMA:
Liste tanımının açılış parantezi eksik. Python "SyntaxError: invalid syntax" hatası verir. Köşeli parantez eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Liste Kapanış Parantezi
# Dosya: src/core/parser.py
# Satır: 88
# MEVCUT KOD (HATALI):
plot_keywords = [
    "plot", "graph", "draw", "ciz", "grafik"

# ÇÖZÜM:
plot_keywords = [
    "plot", "graph", "draw", "ciz", "grafik"
]
# AÇIKLAMA:
Liste tanımının kapanış parantezi eksik. Python "SyntaxError: '[' was never closed" hatası verir. Köşeli parantez eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik return Keyword
# Dosya: src/core/parser.py
# Satır: 98
# MEVCUT KOD (HATALI):
 None
# ÇÖZÜM:
return None
# AÇIKLAMA:
Fonksiyon dönüş değeri için return keyword'ü eksik. Python "SyntaxError: invalid syntax" hatası verir. return keyword'ü eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Type Hint
# Dosya: src/modules/basic_math.py
# Satır: 12
# MEVCUT KOD (HATALI):
def safe_divide(a: , b: float) -> float:
# ÇÖZÜM:
def safe_divide(a: float, b: float) -> float:
# AÇIKLAMA:
Fonksiyon parametresinde type hint eksik. Python "SyntaxError: invalid syntax" hatası verir. float type hint'i eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış Karşılaştırma Operatörü
# Dosya: src/modules/basic_math.py
# Satır: 23
# MEVCUT KOD (HATALI):
if b = 0:
# ÇÖZÜM:
if b == 0:
# AÇIKLAMA:
Karşılaştırma operatörü = yerine == olmalıdır. Tek eşittir atama operatörüdür, karşılaştırma için çift eşittir kullanılmalı. Python "SyntaxError: invalid syntax" hatası verir.

---

# HATA: Syntax Error - Gereksiz raise Keyword
# Dosya: src/modules/basic_math.py
# Satır: 25
# MEVCUT KOD (HATALI):
wrong_raise = raise undefined_exception()
# ÇÖZÜM:
# Satır kaldırıldı (raise keyword değişkene atanamaz)
# AÇIKLAMA:
raise statement değişkene atanamaz. Python "SyntaxError: invalid syntax" hatası verir. raise sadece exception fırlatmak için kullanılır.

---

# HATA: Syntax Error - Gereksiz return Keyword
# Dosya: src/modules/basic_math.py
# Satır: 27
# MEVCUT KOD (HATALI):
wrong_return = return undefined_value
# ÇÖZÜM:
# Satır kaldırıldı (return keyword değişkene atanamaz)
# AÇIKLAMA:
return statement değişkene atanamaz. Python "SyntaxError: invalid syntax" hatası verir. return sadece fonksiyondan değer döndürmek için kullanılır.

---

# HATA: Syntax Error - Eksik logger Referansı
# Dosya: src/modules/basic_math.py
# Satır: 73
# MEVCUT KOD (HATALI):
.error(f"Basic math calculation error: {e}")
# ÇÖZÜM:
logger.error(f"Basic math calculation error: {e}")
# AÇIKLAMA:
Metod çağrısında nesne referansı eksik. Python "SyntaxError: invalid syntax" hatası verir. logger nesnesi eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik raise Statement
# Dosya: src/modules/basic_math.py
# Satır: 74
# MEVCUT KOD (HATALI):
# (raise statement eksik)
# ÇÖZÜM:
            raise
# AÇIKLAMA:
Exception yakalandıktan sonra tekrar fırlatılmalı. except bloğundan sonra raise eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik ABC Inheritance
# Dosya: src/modules/base_module.py
# Satır: 13
# MEVCUT KOD (HATALI):
class BaseModule():
# ÇÖZÜM:
class BaseModule(ABC):
# AÇIKLAMA:
Abstract base class ABC'den türemeli. Python abstract metodları tanıyamaz ve "TypeError" verir. ABC inheritance eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik @abstractmethod Decorator
# Dosya: src/modules/base_module.py
# Satır: 28
# MEVCUT KOD (HATALI):
    async def calculate(
# ÇÖZÜM:
    @abstractmethod
    async def calculate(
# AÇIKLAMA:
Abstract metodlar @abstractmethod decorator'ı ile işaretlenmelidir. Bu olmadan abstract sınıf düzgün çalışmaz. Decorator eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik @abstractmethod Decorator
# Dosya: src/modules/base_module.py
# Satır: 47
# MEVCUT KOD (HATALI):
    def _get_domain_prompt(self) -> str:
# ÇÖZÜM:
    @abstractmethod
    def _get_domain_prompt(self) -> str:
# AÇIKLAMA:
Abstract metodlar @abstractmethod decorator'ı ile işaretlenmelidir. Decorator eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış Fonksiyon Çağrısı Syntax'ı
# Dosya: src/modules/base_module.py
# Satır: 105
# MEVCUT KOD (HATALI):
wrong_syntax = (result=gemini_response.get("result", ""))
# ÇÖZÜM:
# Satır kaldırıldı (geçersiz syntax)
# AÇIKLAMA:
Parantez içinde keyword argument kullanımı geçersiz. Python "SyntaxError: invalid syntax" hatası verir. Fonksiyon çağrısı doğrudan yapılmalı, değişkene atanamaz.

---

# HATA: Syntax Error - Eksik Liste Açılış Parantezi
# Dosya: src/modules/__init__.py
# Satır: 10
# MEVCUT KOD (HATALI):
__all__ = 
    "Calculus",
# ÇÖZÜM:
__all__ = [
    "CalculusModule",
# AÇIKLAMA:
Liste tanımının açılış parantezi eksik. Python "SyntaxError: invalid syntax" hatası verir. Köşeli parantez eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış String Değeri
# Dosya: src/modules/__init__.py
# Satır: 11
# MEVCUT KOD (HATALI):
    "Calculus",
# ÇÖZÜM:
    "CalculusModule",
# AÇIKLAMA:
__all__ listesinde tam class adı kullanılmalı. "Calculus" yerine "CalculusModule" olmalı. Bu import hatalarına neden olur.

---

# HATA: Syntax Error - Yanlış String Değeri
# Dosya: src/modules/__init__.py
# Satır: 12
# MEVCUT KOD (HATALI):
    "LinearAlgebra",
# ÇÖZÜM:
    "LinearAlgebraModule",
# AÇIKLAMA:
__all__ listesinde tam class adı kullanılmalı. "LinearAlgebra" yerine "LinearAlgebraModule" olmalı.

---

# HATA: Syntax Error - Yanlış String Değeri
# Dosya: src/modules/__init__.py
# Satır: 13
# MEVCUT KOD (HATALI):
    "BasicMath",
# ÇÖZÜM:
    "BasicMathModule",
# AÇIKLAMA:
__all__ listesinde tam class adı kullanılmalı. "BasicMath" yerine "BasicMathModule" olmalı.

---

# HATA: Syntax Error - Eksik Liste Elemanları
# Dosya: src/modules/__init__.py
# Satır: 14
# MEVCUT KOD (HATALI):
]
# ÇÖZÜM:
    "FinancialModule",
    "EquationSolverModule",
    "GraphPlotterModule",
]
# AÇIKLAMA:
__all__ listesinde import edilen diğer modüller eksik. FinancialModule, EquationSolverModule ve GraphPlotterModule eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Import
# Dosya: src/modules/graph_plotter.py
# Satır: 12
# MEVCUT KOD (HATALI):
# import matplotlib.pyplot as plt  # Eksik!
# ÇÖZÜM:
import matplotlib.pyplot as plt
# AÇIKLAMA:
matplotlib.pyplot import'u comment out edilmiş ancak kodda plt kullanılıyor. Comment kaldırılarak düzeltildi.

---

# HATA: Syntax Error - Eksik Parametre
# Dosya: src/modules/graph_plotter.py
# Satır: 28
# MEVCUT KOD (HATALI):
super().__init__()
# ÇÖZÜM:
super().__init__(gemini_agent)
# AÇIKLAMA:
BaseModule.__init__() metodu gemini_agent parametresi bekliyor ancak verilmemiş. Python "TypeError" verir. Parametre eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış Metod Adı
# Dosya: src/modules/graph_plotter.py
# Satır: 30
# MEVCUT KOD (HATALI):
self.cache_dir.wrong_mkdir_method(parents=True, exist_ok=True)
# ÇÖZÜM:
self.cache_dir.mkdir(parents=True, exist_ok=True)
# AÇIKLAMA:
Path nesnesinde wrong_mkdir_method diye bir metod yok. Doğru metod adı mkdir()'dir. AttributeError verir. Metod adı düzeltildi.

---

# HATA: Syntax Error - Yanlış Type Hint
# Dosya: src/modules/graph_plotter.py
# Satır: 33
# MEVCUT KOD (HATALI):
self.wrong_cache: str = {}
# ÇÖZÜM:
self.wrong_cache: Dict[str, str] = {}
# AÇIKLAMA:
Değişken tipi str olarak belirtilmiş ama dict atanmış. Type mismatch hatası. Dict[str, str] olarak düzeltildi.

---

# HATA: Syntax Error - Yanlış Parametre Syntax
# Dosya: src/modules/graph_plotter.py
# Satır: 42
# MEVCUT KOD (HATALI):
async def calculate(
    self,
    expression: str,
    *kwargs,
# ÇÖZÜM:
async def calculate(
    self,
    expression: str,
    **kwargs
# AÇIKLAMA:
Keyword arguments için ** kullanılmalı, * değil. * sadece positional arguments için kullanılır. Syntax hatası verir. ** olarak düzeltildi.

---

# HATA: Syntax Error - Eksik await Keyword
# Dosya: src/modules/graph_plotter.py
# Satır: 67
# MEVCUT KOD (HATALI):
response =  self._call_gemini(expression)
# ÇÖZÜM:
response = await self._call_gemini(expression)
# AÇIKLAMA:
_call_gemini() bir async metoddur, await ile çağrılmalıdır. Aksi halde coroutine objesi döner. await eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış Metod Çağrısı Sırası
# Dosya: src/modules/graph_plotter.py
# Satır: 72
# MEVCUT KOD (HATALI):
plot_paths = await ._create_plot(result.visual_data, expression) self eksik!
# ÇÖZÜM:
plot_paths = await self._create_plot(result.visual_data, expression)
# AÇIKLAMA:
self keyword'ü metoddan önce yazılmalı. Syntax hatası verir. self pozisyonu düzeltildi.

---

# HATA: Syntax Error - Yanlış Metod Adı
# Dosya: src/modules/graph_plotter.py
# Satır: 133
# MEVCUT KOD (HATALI):
plt.plot(x, y, 'b-', linewidth=2, wrong_param=5)
# ÇÖZÜM:
plt.plot(x, y, 'b-', linewidth=2)
# AÇIKLAMA:
plt.plot() metodunda wrong_param diye bir parametre yok. Gereksiz parametre kaldırılarak düzeltildi.

---

# HATA: Syntax Error - Yanlış String Concatenation
# Dosya: src/modules/graph_plotter.py
# Satır: 135
# MEVCUT KOD (HATALI):
plt.xlabel(f'x {undefined_var}')
# ÇÖZÜM:
plt.xlabel('x')
# AÇIKLAMA:
undefined_var tanımlı değil. String basitleştirilerek düzeltildi.

---

# HATA: Syntax Error - Yanlış String Concatenation
# Dosya: src/modules/graph_plotter.py
# Satır: 140
# MEVCUT KOD (HATALI):
png_path = self.cache_dir / f"{hash(expression)}.png" + undefined_string
# ÇÖZÜM:
png_path = self.cache_dir / f"{hash(expression)}.png"
# AÇIKLAMA:
Path objesi ile string toplanamaz ve undefined_string tanımlı değil. String concatenation kaldırılarak düzeltildi.

---

# HATA: Syntax Error - Yanlış Metod Adı
# Dosya: src/modules/graph_plotter.py
# Satır: 141
# MEVCUT KOD (HATALI):
plt.wrong_save_method(png_path, dpi=150, bbox_inches='tight')
# ÇÖZÜM:
plt.savefig(png_path, dpi=150, bbox_inches='tight')
# AÇIKLAMA:
matplotlib.pyplot'ta wrong_save_method diye bir metod yok. Doğru metod adı savefig()'dir. Metod adı düzeltildi.

---

# HATA: Syntax Error - Blocking Call in Async Function
# Dosya: src/modules/graph_plotter.py
# Satır: 143
# MEVCUT KOD (HATALI):
plt.show()  # Blocking call in async function!
# ÇÖZÜM:
# Satır kaldırıldı (async fonksiyonda blocking call)
# AÇIKLAMA:
plt.show() blocking bir çağrıdır ve async fonksiyonda kullanılmamalı. Ayrıca non-interactive backend (Agg) ile çalışmaz. Satır kaldırıldı.

---

# HATA: Syntax Error - Eksik self Keyword
# Dosya: src/modules/equation_solver.py
# Satır: 34
# MEVCUT KOD (HATALI):
.validate_input(expression)
# ÇÖZÜM:
self.validate_input(expression)
# AÇIKLAMA:
Metod çağrısında nesne referansı eksik. Python "SyntaxError: invalid syntax" hatası verir. self eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış Değişken Adı (Typo)
# Dosya: src/modules/equation_solver.py
# Satır: 35
# MEVCUT KOD (HATALI):
self.wrong_method(expresson)
# ÇÖZÜM:
self.wrong_method(expression)
# AÇIKLAMA:
Parametre adında typo var: expresson yerine expression olmalı. NameError verir. Değişken adı düzeltildi.

---

# HATA: Syntax Error - Eksik await Keyword
# Dosya: src/modules/equation_solver.py
# Satır: 40
# MEVCUT KOD (HATALI):
result = self._create_result(response, "equation_solver")  # await eksik!
# ÇÖZÜM:
result = self._create_result(response, "equation_solver")
# AÇIKLAMA:
_create_result() async değil, sync bir metod olduğu için await gerekmez. Comment yanlış, kod doğru. Değişiklik gerekmedi.

---

# HATA: Syntax Error - Geçersiz Import Statement
# Dosya: src/modules/calculus.py
# Satır: 6
# MEVCUT KOD (HATALI):
wrong_import = from src.config.prompts import WRONG_PROMPT
# ÇÖZÜM:
# Satır kaldırıldı (geçersiz import syntax)
# AÇIKLAMA:
Import statement değişkene atanamaz. Python "SyntaxError: invalid syntax" hatası verir. Satır kaldırıldı.

---

# HATA: Syntax Error - Yanlış String İçeriği
# Dosya: src/modules/calculus.py
# Satır: 14
# MEVCUT KOD (HATALI):
if '' in globals():
# ÇÖZÜM:
if 'sympy' in globals():
# AÇIKLAMA:
Boş string yerine 'sympy' kontrol edilmeli. Mantık hatası. String içeriği düzeltildi.

---

# HATA: Syntax Error - Eksik self Parametresi
# Dosya: src/modules/calculus.py
# Satır: 28
# MEVCUT KOD (HATALI):
async def calculate(
    ,
    expression: str,
# ÇÖZÜM:
async def calculate(
    self,
    expression: str,
# AÇIKLAMA:
Class metodunun ilk parametresi self olmalıdır ancak eksik. Python "SyntaxError: invalid syntax" hatası verir. self parametresi eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Parametre
# Dosya: src/modules/calculus.py
# Satır: 42
# MEVCUT KOD (HATALI):
self.validate_input()
# ÇÖZÜM:
self.validate_input(expression)
# AÇIKLAMA:
validate_input() metodu expression parametresi bekliyor ancak verilmemiş. TypeError verir. Parametre eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik await Keyword
# Dosya: src/modules/calculus.py
# Satır: 49
# MEVCUT KOD (HATALI):
result = self._create_result(response, "calculus")  !
# ÇÖZÜM:
result = self._create_result(response, "calculus")
# AÇIKLAMA:
Comment'te ! işareti var ama kod doğru. _create_result() sync olduğu için await gerekmez. Değişiklik gerekmedi.

---

# HATA: Syntax Error - Eksik Metod Adı
# Dosya: src/modules/calculus.py
# Satır: 61
# MEVCUT KOD (HATALI):
logger.(f"Calculus calculation error: {e}")
# ÇÖZÜM:
logger.error(f"Calculus calculation error: {e}")
# AÇIKLAMA:
logger metodundan sonra metod adı eksik. Python "SyntaxError: invalid syntax" hatası verir. error metod adı eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Attribute Adı
# Dosya: src/utils/logger.py
# Satır: 14
# MEVCUT KOD (HATALI):
"level": record.,
# ÇÖZÜM:
"level": record.levelname,
# AÇIKLAMA:
record nesnesinden sonra attribute adı eksik. Python "SyntaxError: invalid syntax" hatası verir. levelname attribute'u eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik Parantez
# Dosya: src/utils/logger.py
# Satır: 17
# MEVCUT KOD (HATALI):
"message": record.(),
# ÇÖZÜM:
"message": record.getMessage(),
# AÇIKLAMA:
Metod adı eksik, sadece parantez var. Python "SyntaxError: invalid syntax" hatası verir. getMessage() metod adı eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış Decorator Syntax
# Dosya: src/utils/helpers.py
# Satır: 63
# MEVCUT KOD (HATALI):
@lru_cache(maxsize=128
# ÇÖZÜM:
@lru_cache(maxsize=128)
# AÇIKLAMA:
Decorator parantezi kapatılmamış. Python "SyntaxError: invalid syntax" hatası verir. Kapanış parantezi eklenerek düzeltildi.

---

# HATA: Syntax Error - Eksik self Parametresi
# Dosya: src/utils/helpers.py
# Satır: 64
# MEVCUT KOD (HATALI):
def format_result_for_display(result: Any) -> str:
# ÇÖZÜM:
def format_result_for_display(result: Any) -> str:
# AÇIKLAMA:
Bu fonksiyon class dışında tanımlı olduğu için self gerekmez. Kod zaten doğru. Değişiklik gerekmedi.

---

# HATA: Syntax Error - Gereksiz return Keyword
# Dosya: src/utils/helpers.py
# Satır: 76
# MEVCUT KOD (HATALI):
wrong_return = return undefined_value
# ÇÖZÜM:
# Satır kaldırıldı (return keyword değişkene atanamaz)
# AÇIKLAMA:
return statement değişkene atanamaz. Python "SyntaxError: invalid syntax" hatası verir. return sadece fonksiyondan değer döndürmek için kullanılır.

---

# HATA: Syntax Error - Ulaşılamaz Kod (Unreachable)
# Dosya: src/utils/helpers.py
# Satır: 78
# MEVCUT KOD (HATALI):
return wrong_function()
# ÇÖZÜM:
# Satır kaldırıldı (unreachable code)
# AÇIKLAMA:
return statement'tan sonra başka bir return olamaz. Bu kod hiçbir zaman çalışmaz (unreachable). Satır kaldırıldı.

---

# HATA: Syntax Error - Eksik self Parametresi
# Dosya: src/modules/linear_algebra.py
# Satır: 20
# MEVCUT KOD (HATALI):
async def calculate(
    ,
    expression: str,
# ÇÖZÜM:
async def calculate(
    self,
    expression: str,
# AÇIKLAMA:
Class metodunun ilk parametresi self olmalıdır ancak eksik. Python "SyntaxError: invalid syntax" hatası verir. self parametresi eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış Args Syntax
# Dosya: src/modules/linear_algebra.py
# Satır: 22
# MEVCUT KOD (HATALI):
*kwargs,
# ÇÖZÜM:
**kwargs
# AÇIKLAMA:
Keyword arguments için ** kullanılmalı, * değil. * sadece positional arguments için kullanılır. ** olarak düzeltildi.

---

# HATA: Syntax Error - Eksik await Keyword
# Dosya: src/modules/linear_algebra.py
# Satır: 37
# MEVCUT KOD (HATALI):
response =  self._call_gemini(expression)
# ÇÖZÜM:
response = await self._call_gemini(expression)
# AÇIKLAMA:
_call_gemini() bir async metoddur, await ile çağrılmalıdır. Aksi halde coroutine objesi döner. await eklenerek düzeltildi.

---

# HATA: Syntax Error - Yanlış await Kullanımı
# Dosya: src/modules/linear_algebra.py
# Satır: 39
# MEVCUT KOD (HATALI):
result = await self._create_result(response, "linear_algebra")
# ÇÖZÜM:
result = self._create_result(response, "linear_algebra")
# AÇIKLAMA:
_create_result() sync bir metoddur, await kullanılmamalı. await kaldırılarak düzeltildi.

---

# HATA: Syntax Error - Yanlış Return Değişkeni
# Dosya: src/modules/linear_algebra.py
# Satır: 48
# MEVCUT KOD (HATALI):
return undefined_result
# ÇÖZÜM:
return result
# AÇIKLAMA:
undefined_result diye bir değişken tanımlı değil. Doğru değişken adı result'dır. NameError verir. Değişken adı düzeltildi.

---

# HATA: Syntax Error - Eksik raise Statement
# Dosya: src/modules/linear_algebra.py
# Satır: 52
# MEVCUT KOD (HATALI):
logger.error(f"Linear algebra calculation error: {e}")
# (raise statement eksik)
# ÇÖZÜM:
logger.error(f"Linear algebra calculation error: {e}")
            raise
# AÇIKLAMA:
Exception yakalandıktan sonra tekrar fırlatılmalı. except bloğundan sonra raise eklenerek düzeltildi.

---

# HATA: Syntax Error - Parameter Without Default Follows Parameter With Default
# Dosya: src/core/agent.py
# Satır: 101-106
# MEVCUT KOD (HATALI):
async def generate_with_retry(
    self,
    prompt: str,
    max_retries: Optional[int] = None,
    wrong_param,  # Tip hint yok!
    extra_param = undefined_default  # Default değer tanımlı değil!
) -> str:
# ÇÖZÜM:
async def generate_with_retry(
    self,
    prompt: str,
    wrong_param,
    max_retries: Optional[int] = None,
    extra_param = undefined_default
) -> str:
# AÇIKLAMA:
Python'da fonksiyon parametrelerinde default değeri olmayan parametreler (positional), default değeri olan parametrelerden (keyword) önce gelmelidir. wrong_param parametresi default değeri olmadığı için max_retries'tan önce taşınmalıdır. Aksi halde "SyntaxError: non-default argument follows default argument" hatası verir.

---

# HATA: ImportError - Var Olmayan Modül
# Dosya: src/main.py
# Satır: 8
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from nonexistent_module import SomeClass  # Modül yok!
# ÇÖZÜM:
# from nonexistent_module import SomeClass  # Modül yok! - Yorum satırı yapıldı
# AÇIKLAMA:
nonexistent_module diye bir Python modülü mevcut değil. Program çalıştırıldığında "ModuleNotFoundError: No module named 'nonexistent_module'" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi. Eğer bu modül gerçekten gerekli ise, önce pip ile kurulmalı veya proje içinde tanımlanmalıdır.

---

# HATA: ImportError - Var Olmayan Fonksiyon Import'u
# Dosya: src/main.py
# Satır: 32
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from src.utils.helpers import nonexistent_function
# ÇÖZÜM:
# from src.utils.helpers import nonexistent_function  # Fonksiyon yok! - Yorum satırı yapıldı
# AÇIKLAMA:
src.utils.helpers modülünde nonexistent_function diye bir fonksiyon tanımlı değil. Program çalıştırıldığında "ImportError: cannot import name 'nonexistent_function' from 'src.utils.helpers'" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/main.py
# Satır: 34
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
APP_NAME = undefined_variable
# ÇÖZÜM:
APP_NAME = "Calculator Agent"
# AÇIKLAMA:
undefined_variable tanımlı değil. Program çalıştırıldığında "NameError: name 'undefined_variable' is not defined" hatası verir. String literal değeri atanarak düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/main.py
# Satır: 35
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
APP_VERSION = missing_version
# ÇÖZÜM:
APP_VERSION = "1.0.0"
# AÇIKLAMA:
missing_version tanımlı değil. Program çalıştırıldığında "NameError: name 'missing_version' is not defined" hatası verir. String literal değeri atanarak düzeltildi.

---

# HATA: NameError - Tanımsız Sınıf
# Dosya: src/main.py
# Satır: 64
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
"wrong_module": WrongModuleClass(self.gemini_agent),  # Sınıf yok!
# ÇÖZÜM:
# "wrong_module": WrongModuleClass(self.gemini_agent),  # Sınıf yok! - Yorum satırı yapıldı
# AÇIKLAMA:
WrongModuleClass sınıfı tanımlı veya import edilmemiş. Program çalıştırıldığında "NameError: name 'WrongModuleClass' is not defined" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Sınıf
# Dosya: src/main.py
# Satır: 65
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
"extra_module": NonexistentModule(self.gemini_agent),  # Sınıf yok!
# ÇÖZÜM:
# "extra_module": NonexistentModule(self.gemini_agent),  # Sınıf yok! - Yorum satırı yapıldı
# AÇIKLAMA:
NonexistentModule sınıfı tanımlı veya import edilmemiş. Program çalıştırıldığında "NameError: name 'NonexistentModule' is not defined" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod
# Dosya: src/main.py
# Satır: 70
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.initialize_something()
# ÇÖZÜM:
# self.initialize_something()  # Metod yok! - Yorum satırı yapıldı
# AÇIKLAMA:
CalculatorAgent sınıfında initialize_something() diye bir metod tanımlı değil. Program çalıştırıldığında "AttributeError: 'CalculatorAgent' object has no attribute 'initialize_something'" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod
# Dosya: src/main.py
# Satır: 71
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.wrong_init_method()
# ÇÖZÜM:
# self.wrong_init_method()  # Metod yok! - Yorum satırı yapıldı
# AÇIKLAMA:
CalculatorAgent sınıfında wrong_init_method() diye bir metod tanımlı değil. Program çalıştırıldığında "AttributeError: 'CalculatorAgent' object has no attribute 'wrong_init_method'" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Attribute
# Dosya: src/main.py
# Satır: 129
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
output_lines.append(f"✅ Sonuc: {format_result_for_display(result.nonexistent_field)}")
# ÇÖZÜM:
output_lines.append(f"✅ Sonuc: {format_result_for_display(result.result)}")
# AÇIKLAMA:
CalculationResult nesnesinde nonexistent_field diye bir attribute yok. Doğru attribute adı result'dır. Program çalıştırıldığında "AttributeError: 'CalculationResult' object has no attribute 'nonexistent_field'" hatası verir. Attribute adı düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/main.py
# Satır: 138
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
output_lines.append(f"Extra: {undefined_variable}")
# ÇÖZÜM:
# output_lines.append(f"Extra: {undefined_variable}")  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_variable tanımlı değil. Program çalıştırıldığında "NameError: name 'undefined_variable' is not defined" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/main.py
# Satır: 139
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_format = format_result_for_display(undefined_result)
# ÇÖZÜM:
# wrong_format = format_result_for_display(undefined_result)  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_result tanımlı değil. Program çalıştırıldığında "NameError: name 'undefined_result' is not defined" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/main.py
# Satır: 163
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
print(f"Version: {APP_VERSION}")  # APP_VERSION tanımlı değil!
# ÇÖZÜM:
print(f"Version: {APP_VERSION}")  # APP_VERSION artık 35. satırda tanımlı
# AÇIKLAMA:
APP_VERSION değişkeni 35. satırda "1.0.0" olarak tanımlandı, bu satır artık çalışır. Önceki hatada değişken tanımlandığı için burada ayrıca düzeltme gerekmedi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/main.py
# Satır: 164
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_print = print(undefined_variable)
# ÇÖZÜM:
# wrong_print = print(undefined_variable)  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_variable tanımlı değil. Program çalıştırıldığında "NameError: name 'undefined_variable' is not defined" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: TypeError - await Eksik
# Dosya: src/main.py
# Satır: 179
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
result = agent.process_command(user_input)
# ÇÖZÜM:
result = await agent.process_command(user_input)
# AÇIKLAMA:
process_command() bir async fonksiyondur ve await ile çağrılmalıdır. Aksi halde coroutine objesi döner ve beklenen sonuç alınamaz. Program çalıştırıldığında "RuntimeWarning: coroutine 'CalculatorAgent.process_command' was never awaited" uyarısı verir. await keyword'ü eklenerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod
# Dosya: src/main.py
# Satır: 180
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
result = await agent.nonexistent_method(user_input)
# ÇÖZÜM:
# result = await agent.nonexistent_method(user_input)  # Metod yok! - Yorum satırı yapıldı
# AÇIKLAMA:
CalculatorAgent sınıfında nonexistent_method() diye bir metod yok. Program çalıştırıldığında "AttributeError: 'CalculatorAgent' object has no attribute 'nonexistent_method'" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: SyntaxError - Eksik Parantez
# Dosya: src/main.py
# Satır: 181
# SEVİYE: Level 1 - Syntax Hataları (Ama runtime context'inde)
# MEVCUT KOD (HATALI):
wrong_result = await undefined_functio
# ÇÖZÜM:
# wrong_result = await undefined_function()  # Yorum satırı yapıldı
# AÇIKLAMA:
Fonksiyon adı incomplete (undefined_functio) ve parantez eksik. Ayrıca fonksiyon tanımlı değil. Python "SyntaxError: invalid syntax" veya "NameError" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Fonksiyon
# Dosya: src/main.py
# Satır: 198
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_call = undefined_function()
# ÇÖZÜM:
# wrong_call = undefined_function()  # Fonksiyon yok! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_function() tanımlı değil. Program çalıştırıldığında "NameError: name 'undefined_function' is not defined" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Fonksiyon
# Dosya: src/main.py
# Satır: 201
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_mode = wrong_function()
# ÇÖZÜM:
# wrong_mode = wrong_function()  # Fonksiyon yok! - Yorum satırı yapıldı
# AÇIKLAMA:
wrong_function() tanımlı değil. Program çalıştırıldığında "NameError: name 'wrong_function' is not defined" hatası verir. Satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: ImportError - Var Olmayan Modül
# Dosya: src/core/agent.py
# Satır: 9
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from nonexistent.config import wrong_settings  # Modül yok!
# ÇÖZÜM:
# from nonexistent.config import wrong_settings  # Modül yok! - Yorum satırı yapıldı
# AÇIKLAMA:
nonexistent.config diye bir Python modülü/paketi mevcut değil. Program çalıştırıldığında "ModuleNotFoundError: No module named 'nonexistent'" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi. Bu modül kullanılmadığı için kodun geri kalanında da bir soruna yol açmaz.

---

# HATA: ImportError - Var Olmayan Modül
# Dosya: src/core/agent.py
# Satır: 10
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from nonexistent.extra import ExtraClass  # Modül yok!
# ÇÖZÜM:
# from nonexistent.extra import ExtraClass  # Modül yok! - Yorum satırı yapıldı
# AÇIKLAMA:
nonexistent.extra diye bir Python modülü/paketi mevcut değil. Program çalıştırıldığında "ModuleNotFoundError: No module named 'nonexistent'" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi. ExtraClass hiçbir yerde kullanılmadığı için güvenle kaldırılabilir.

---

# HATA: ImportError - Circular Import (Döngüsel İmport)
# Dosya: src/core/agent.py
# Satır: 14
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from src.modules.basic_math import BasicMathModule  # Circular!
# ÇÖZÜM:
# from src.modules.basic_math import BasicMathModule  # Circular! - Yorum satırı yapıldı
# AÇIKLAMA:
src.modules.basic_math modülü, src.core.agent modülünü import ediyor. Bu dosyada tekrar BasicMathModule import edilirse circular import (döngüsel import) oluşur. Python "ImportError: cannot import name 'BasicMathModule' from partially initialized module" hatası verebilir. Import satırı yorum satırı haline getirilerek düzeltildi. Eğer bu sınıf gerçekten gerekiyorsa, import statement'ı fonksiyon içine taşınmalı (lazy import) veya mimari yeniden yapılandırılmalı.

---

# HATA: ImportError - Self Import (Kendi Kendini İmport)
# Dosya: src/core/agent.py
# Satır: 15
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from src.core.agent import GeminiAgent  # Self import!
# ÇÖZÜM:
# from src.core.agent import GeminiAgent  # Self import! - Yorum satırı yapıldı
# AÇIKLAMA:
Bir modül kendi içindeki sınıfı import edemez (self import). GeminiAgent zaten bu dosyada tanımlanıyor, tekrar import edilmesine gerek yok. Python "ImportError: cannot import name 'GeminiAgent' from partially initialized module" veya "AttributeError" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Değişken (Class Attribute)
# Dosya: src/core/agent.py
# Satır: 26
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.last_call_time = undefined_time_variable
# ÇÖZÜM:
self.last_call_time = 0.0
# AÇIKLAMA:
undefined_time_variable tanımlı değil. RateLimiter sınıfı instance'ı oluşturulduğunda "NameError: name 'undefined_time_variable' is not defined" hatası verir. İlk değer olarak 0.0 (float) atanarak düzeltildi. Bu sayede ilk API çağrısında rate limit kontrolü düzgün çalışır.

---

# HATA: NameError - Tanımsız Değişken (Class Attribute)
# Dosya: src/core/agent.py
# Satır: 29
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.extra_field = missing_constant
# ÇÖZÜM:
# self.extra_field = missing_constant  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
missing_constant tanımlı değil. RateLimiter sınıfı instance'ı oluşturulduğunda "NameError: name 'missing_constant' is not defined" hatası verir. Bu attribute kullanılmadığı için satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/core/agent.py
# Satır: 36
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
current_time = asyncio.get_event_loop().wrong_method()  # Metod yok!
# ÇÖZÜM:
current_time = asyncio.get_event_loop().time()
# AÇIKLAMA:
asyncio.AbstractEventLoop nesnesinde wrong_method() diye bir metod yok. acquire() metodu çağrıldığında "AttributeError: 'asyncio.EventLoop' object has no attribute 'wrong_method'" hatası verir. Doğru metod adı time()'dır ve event loop'un başlangıcından itibaren geçen zamanı döndürür. Metod adı düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/core/agent.py
# Satır: 41
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
await asyncio.sleep(extra_wait_time)  # Tanımlı değil!
# ÇÖZÜM:
# await asyncio.sleep(extra_wait_time)  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
extra_wait_time tanımlı değil. acquire() metodu çağrıldığında "NameError: name 'extra_wait_time' is not defined" hatası verir. Bu satır gereksiz olduğu için (zaten wait_time ile sleep yapılıyor) yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/core/agent.py
# Satır: 43
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.last_call_time = asyncio.get_event_loop().wrong_time_method()
# ÇÖZÜM:
self.last_call_time = asyncio.get_event_loop().time()
# AÇIKLAMA:
asyncio.AbstractEventLoop nesnesinde wrong_time_method() diye bir metod yok. acquire() metodu çağrıldığında "AttributeError: 'asyncio.EventLoop' object has no attribute 'wrong_time_method'" hatası verir. Doğru metod adı time()'dır. Metod adı düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/core/agent.py
# Satır: 44
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
undefined_variable_in_method = "test"
# ÇÖZÜM:
# undefined_variable_in_method = "test"  # Gereksiz! - Yorum satırı yapıldı
# AÇIKLAMA:
Bu değişken tanımlanmış ancak hiçbir yerde kullanılmıyor (dead code). Kodun okunabilirliği için yorum satırı haline getirilerek düzeltildi. Herhangi bir runtime hatası vermez ancak gereksizdir.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/core/agent.py
# Satır: 45
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
result = self.cache.wrong_method()
# ÇÖZÜM:
# result = self.cache.wrong_method()  # Metod yok! - Yorum satırı yapıldı
# AÇIKLAMA:
self.cache bir string olarak tanımlanmış ("wrong_type"), string nesnesinde wrong_method() diye bir metod yok. acquire() metodu çağrıldığında "AttributeError: 'str' object has no attribute 'wrong_method'" hatası verir. Bu satır gereksiz olduğu için yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Değişken (Class Attribute)
# Dosya: src/core/agent.py
# Satır: 76
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.extra_config = missing_config_variable
# ÇÖZÜM:
# self.extra_config = missing_config_variable  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
missing_config_variable tanımlı değil. GeminiAgent sınıfı instance'ı oluşturulduğunda "NameError: name 'missing_config_variable' is not defined" hatası verir. Bu attribute kullanılmadığı için satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Attribute Ataması
# Dosya: src/core/agent.py
# Satır: 77
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.model.wrong_attribute = "test"  # Attribute yok!
# ÇÖZÜM:
# self.model.wrong_attribute = "test"  # Attribute yok! - Yorum satırı yapıldı
# AÇIKLAMA:
GenerativeModel nesnesine dinamik olarak attribute eklemek tehlikeli olabilir ve beklenmeyen davranışlara yol açabilir. Eğer model objesi __slots__ kullanıyorsa "AttributeError" verir. Bu satır gereksiz olduğu için yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/core/agent.py
# Satır: 78
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.nonexistent_method()  # Metod yok!
# ÇÖZÜM:
# self.nonexistent_method()  # Metod yok! - Yorum satırı yapıldı
# AÇIKLAMA:
GeminiAgent sınıfında nonexistent_method() diye bir metod tanımlı değil. __init__() metodu çağrıldığında "AttributeError: 'GeminiAgent' object has no attribute 'nonexistent_method'" hatası verir. Bu satır gereksiz olduğu için yorum satırı haline getirilerek düzeltildi.

---

# HATA: TypeError - Eksik Type Hint
# Dosya: src/core/agent.py
# Satır: 103
# SEVİYE: Level 2 - Runtime/Import Hataları (Type Hint eksikliği runtime'da hata vermez ama best practice)
# MEVCUT KOD (HATALI):
wrong_param,  # Tip hint yok!
# ÇÖZÜM:
wrong_param: Any,
# AÇIKLAMA:
Parametre için type hint eksik. Bu doğrudan runtime hatası vermez ancak type checker (mypy, pyright) kullanıldığında uyarı verir. Best practice olarak tüm parametreler type hint almalıdır. Any tipi eklenerek düzeltildi.

---

# HATA: NameError - Tanımsız Default Değer
# Dosya: src/core/agent.py
# Satır: 105
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
extra_param = undefined_default  # Default değer tanımlı değil!
# ÇÖZÜM:
extra_param: Any = None
# AÇIKLAMA:
undefined_default tanımlı değil. generate_with_retry() metodu tanımlandığında (fonksiyon objesi oluşturulduğunda) "NameError: name 'undefined_default' is not defined" hatası verir. Default değer None olarak atanarak ve type hint eklenerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Setting
# Dosya: src/core/agent.py
# Satır: 129
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
"wrong_key": settings.NONEXISTENT_SETTING,  # Setting yok!
# ÇÖZÜM:
# "wrong_key": settings.NONEXISTENT_SETTING,  # Setting yok! - Yorum satırı yapıldı
# AÇIKLAMA:
Settings sınıfında NONEXISTENT_SETTING diye bir attribute yok. generate_with_retry() metodu çağrıldığında "AttributeError: type object 'Settings' has no attribute 'NONEXISTENT_SETTING'" hatası verir. Bu key gereksiz olduğu için satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/core/agent.py
# Satır: 133
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
extra_data = undefined_response_field
# ÇÖZÜM:
# extra_data = undefined_response_field  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_response_field tanımlı değil. generate_with_retry() metodu çağrıldığında "NameError: name 'undefined_response_field' is not defined" hatası verir. Bu değişken atanmış ama kullanılmıyor (dead code), yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Attribute
# Dosya: src/core/agent.py
# Satır: 134
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_attr = response.nonexistent_attr  # Attribute yok!
# ÇÖZÜM:
# wrong_attr = response.nonexistent_attr  # Attribute yok! - Yorum satırı yapıldı
# AÇIKLAMA:
Response nesnesinde nonexistent_attr diye bir attribute yok. generate_with_retry() metodu çağrıldığında "AttributeError: 'GenerateContentResponse' object has no attribute 'nonexistent_attr'" hatası verir. Bu değişken gereksiz olduğu için yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/core/agent.py
# Satır: 153
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_sleep = asyncio.sleep(undefined_var)  # Tanımlı değil!
# ÇÖZÜM:
# wrong_sleep = asyncio.sleep(undefined_var)  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_var tanımlı değil ve asyncio.sleep() coroutine'i await edilmeden atanmış. generate_with_retry() metodu çağrıldığında "NameError: name 'undefined_var' is not defined" hatası verir. Bu satır gereksiz olduğu için yorum satırı haline getirilerek düzeltildi.

---

# HATA: TypeError - Eksik Argüman
# Dosya: src/core/agent.py
# Satır: 172
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
response_text = await self.generate_with_retry(prompt, max_retries)
# ÇÖZÜM:
response_text = await self.generate_with_retry(prompt, None, max_retries)
# AÇIKLAMA:
generate_with_retry() metodunun signature'ı değiştirildi ve wrong_param parametresi eklendi. Bu parametre zorunlu (default değeri yok) olduğu için çağrıda belirtilmeli. generate_json_response() metodu çağrıldığında "TypeError: generate_with_retry() missing 1 required positional argument: 'wrong_param'" hatası verir. None argümanı eklenerek düzeltildi.

---

# HATA: NameError - Tanımsız Dictionary Key
# Dosya: src/core/agent.py
# Satır: 187
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_dict_key = {undefined_key: "value"}  # Key tanımlı değil!
# ÇÖZÜM:
# wrong_dict_key = {undefined_key: "value"}  # Key tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_key tanımlı değil. generate_json_response() metodunda JSON parse başarısız olduğunda "NameError: name 'undefined_key' is not defined" hatası verir. Bu değişken gereksiz olduğu için yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Dictionary Key
# Dosya: src/core/agent.py
# Satır: 191
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
undefined_field: "test"  # Key tanımlı değil!
# ÇÖZÜM:
# undefined_field: "test"  # Key tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_field tanımlı değil. generate_json_response() metodunda JSON parse başarısız olduğunda "NameError: name 'undefined_field' is not defined" hatası verir. Bu key gereksiz olduğu için satır yorum satırı haline getirilerek düzeltildi.

---

# HATA: TypeError - Exception Sınıfından Türememiş
# Dosya: src/utils/exceptions.py
# Satır: 3
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
class CalculationError():  # Exception'dan türemeli!
    wrong_field = undefined_constant  # Tanımlı değil!
    pass
# ÇÖZÜM:
class CalculationError(Exception):
    """Hesaplama hatasi"""
    pass
# AÇIKLAMA:
Python'da custom exception sınıfları mutlaka Exception sınıfından veya onun alt sınıflarından (BaseException, RuntimeError vb.) türemelidir. Aksi halde bu sınıf raise edildiğinde "TypeError: exceptions must derive from BaseException" hatası verir. CalculationError sınıfı Exception'dan türetilerek düzeltildi.

---

# HATA: NameError - Tanımsız Değişken (Class Attribute)
# Dosya: src/utils/exceptions.py
# Satır: 4
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
    wrong_field = undefined_constant  # Tanımlı değil!
# ÇÖZÜM:
# Satır kaldırıldı
# AÇIKLAMA:
undefined_constant tanımlı değil. CalculationError sınıfı import edildiğinde veya instance'ı oluşturulduğunda "NameError: name 'undefined_constant' is not defined" hatası verir. Bu attribute gereksiz olduğu için satır tamamen kaldırılarak düzeltildi.

---

# HATA: TypeError - Exception Sınıfından Türememiş
# Dosya: src/utils/exceptions.py
# Satır: 13
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
class GeminiAPIError():  
    """Gemini API'den donen hata"""
    wrong_method = lambda: undefined_function()  
    pass
# ÇÖZÜM:
class GeminiAPIError(Exception):
    """Gemini API'den donen hata"""
    pass
# AÇIKLAMA:
Python'da custom exception sınıfları mutlaka Exception sınıfından türemelidir. GeminiAPIError sınıfı raise edildiğinde "TypeError: exceptions must derive from BaseException" hatası verir. Sınıf Exception'dan türetilerek düzeltildi.

---

# HATA: NameError - Tanımsız Fonksiyon (Lambda İçinde)
# Dosya: src/utils/exceptions.py
# Satır: 15
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
    wrong_method = lambda: undefined_function()  
# ÇÖZÜM:
# Satır kaldırıldı
# AÇIKLAMA:
undefined_function() tanımlı değil. Bu lambda fonksiyonu çağrıldığında "NameError: name 'undefined_function' is not defined" hatası verir. Lambda gereksiz olduğu için satır tamamen kaldırılarak düzeltildi.

---

# HATA: TypeError - Exception Sınıfından Türememiş
# Dosya: src/utils/exceptions.py
# Satır: 19
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
class SecurityViolationError():
    """Guvenlik ihlali tespit edildi"""
    pass
# ÇÖZÜM:
class SecurityViolationError(Exception):
    """Guvenlik ihlali tespit edildi"""
    pass
# AÇIKLAMA:
Python'da custom exception sınıfları mutlaka Exception sınıfından türemelidir. SecurityViolationError sınıfı raise edildiğinde "TypeError: exceptions must derive from BaseException" hatası verir. Sınıf Exception'dan türetilerek düzeltildi.

---

# HATA: TypeError - Exception Sınıfından Türememiş & Name Conflict
# Dosya: src/utils/exceptions.py
# Satır: 24
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
class ModuleNotFoundError():
    """Modul bulunamadi"""
    pass
# ÇÖZÜM:
class ModuleNotFoundError(Exception):
    """Modul bulunamadi"""
    pass
# AÇIKLAMA:
İki sorun var: 1) Exception sınıfından türememiş, raise edildiğinde "TypeError: exceptions must derive from BaseException" hatası verir. 2) Python 3.6+ sürümlerinde ModuleNotFoundError zaten built-in bir exception sınıfıdır (ImportError'dan türer). Bu isim充突 (name conflict) yaratır ve beklenmeyen davranışlara yol açabilir. Best practice olarak farklı bir isim kullanılmalıdır (örn: CalculatorModuleNotFoundError). Ancak şimdilik sadece Exception'dan türetilerek düzeltildi. İsim değişikliği için ayrı bir refactoring yapılmalıdır.

---

# NOT: Name Conflict Uyarısı
# Dosya: src/utils/exceptions.py
# Satır: 24
# SEVİYE: Level 3 - Mantık/Tasarım Hataları
# AÇIKLAMA:
ModuleNotFoundError ismi Python'ın built-in exception sınıfı ile çakışıyor. Bu durum şu sorunlara yol açabilir:
1. Kod okunurken karışıklık yaratır (hangi ModuleNotFoundError kullanılıyor?)
2. Import sırası değiştiğinde beklenmeyen davranışlar olabilir
3. Type hints ve exception handling'de hatalara yol açabilir

ÖNERİ: Sınıf adını değiştirin:
- CalculatorModuleNotFoundError
- CustomModuleNotFoundError
- AgentModuleNotFoundError

veya Python'ın built-in ModuleNotFoundError sınıfını doğrudan kullanın (eğer aynı amaca hizmet ediyorsa).

---

# HATA: NameError - Tanımsız Default Değer (Parametre)
# Dosya: src/core/agent.py
# Satır: 106
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
async def generate_with_retry(
    self,
    prompt: str,
    wrong_param,
    max_retries: Optional[int] = None,
    extra_param = undefined_default  # Default değer tanımlı değil!
) -> str:
# ÇÖZÜM:
async def generate_with_retry(
    self,
    prompt: str,
    wrong_param: Any,
    max_retries: Optional[int] = None,
    extra_param: Any = None
) -> str:
# AÇIKLAMA:
undefined_default tanımlı değil. Python fonksiyon tanımını parse ederken (fonksiyon objesi oluşturulurken, çalıştırılmadan önce bile) "NameError: name 'undefined_default' is not defined" hatası verir. Default değer None olarak atanarak düzeltildi. Ayrıca type hint eksikliği de düzeltilerek wrong_param ve extra_param parametrelerine Any tipi eklendi.

---

# HATA: TypeError - Eksik Type Hint (Best Practice)
# Dosya: src/core/agent.py
# Satır: 103
# SEVİYE: Level 2 - Runtime/Import Hataları (Type Hint eksikliği)
# MEVCUT KOD (HATALI):
wrong_param,  # Tip hint yok!
# ÇÖZÜM:
wrong_param: Any,
# AÇIKLAMA:
Parametre için type hint eksik. Bu doğrudan runtime hatası vermez ancak type checker (mypy, pyright) kullanıldığında hata verir. Python'da best practice olarak tüm fonksiyon parametreleri type hint almalıdır. PEP 484 standartlarına uyum için Any tipi eklenerek düzeltildi.

---

# NOT: Parametre İsimlendirme
# Dosya: src/core/agent.py
# Satır: 103, 106
# SEVİYE: Level 3 - Mantık/Tasarım Hataları
# AÇIKLAMA:
wrong_param ve extra_param parametreleri anlamlı isimler değil ve kodda hiçbir yerde kullanılmıyor (dead parameters). Bu parametreler:
1. Fonksiyon imzasını karmaşıklaştırıyor
2. API kullanıcılarını yanıltıyor (ne için kullanıldığı belli değil)
3. Gereksiz argüman geçirilmesini gerektiriyor

ÖNERİ: Bu parametreleri tamamen kaldırın veya gerçek bir amaç için kullanın:
```python
async def generate_with_retry(
    self,
    prompt: str,
    max_retries: Optional[int] = None
) -> str:

---

# HATA: ImportError - Var Olmayan Modül
# Dosya: src/core/validator.py
# Satır: 7
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from nonexistent.validator import WrongValidator  # Modül yok!
# ÇÖZÜM:
# from nonexistent.validator import WrongValidator  # Modül yok! - Yorum satırı yapıldı
# AÇIKLAMA:
nonexistent.validator diye bir Python modülü/paketi mevcut değil. Program çalıştırıldığında veya validator.py import edildiğinde "ModuleNotFoundError: No module named 'nonexistent'" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi. WrongValidator sınıfı kodda hiçbir yerde kullanılmadığı için güvenle kaldırılabilir.

---

# HATA: NameError - Tanımsız Type (Type Hint)
# Dosya: src/core/validator.py
# Satır: 31
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
def sanitize_expression(self, expression: str) -> str:
    wrong_param: undefined_type = None  # HATA: undefined_type tanımlı değil!
# ÇÖZÜM:
def sanitize_expression(self, expression: str) -> str:
    # wrong_param: undefined_type = None  # HATA: undefined_type tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_type tanımlı değil ve type hint olarak kullanılmış. Python 3.9+ sürümlerinde type hint'ler runtime'da değerlendirilir (PEP 563 öncesi davranış). sanitize_expression() metodu çağrıldığında veya modül import edildiğinde "NameError: name 'undefined_type' is not defined" hatası verebilir. Bu değişken gereksiz olduğu için satır yorum satırı haline getirilerek düzeltildi. Eğer gerçekten bir değişken gerekiyorsa, type hint olarak Any veya Optional[str] kullanılabilir.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/core/validator.py
# Satır: 52
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
expression_lower = expression.lower()
wrong_lower = undefined_var.lower()  # Tanımlı değil!
# ÇÖZÜM:
expression_lower = expression.lower()
# wrong_lower = undefined_var.lower()  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_var tanımlı değil. sanitize_expression() metodu çağrıldığında "NameError: name 'undefined_var' is not defined" hatası verir. Bu satır gereksiz olduğu için (wrong_lower değişkeni hiçbir yerde kullanılmıyor) yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/core/validator.py
# Satır: 55
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
for pattern in self.FORBIDDEN_PATTERNS:
    if pattern in expression_lower:
        wrong_check = self.wrong_method()  # Metod yok!
        raise SecurityViolationError(
            f"Yasakli ifade tespit edildi: {pattern}"
        )
# ÇÖZÜM:
for pattern in self.FORBIDDEN_PATTERNS:
    if pattern in expression_lower:
        # wrong_check = self.wrong_method()  # Metod yok! - Yorum satırı yapıldı
        raise SecurityViolationError(
            f"Yasakli ifade tespit edildi: {pattern}"
        )
# AÇIKLAMA:
InputValidator sınıfında wrong_method() diye bir metod tanımlı değil. sanitize_expression() metodu çağrıldığında ve yasaklı bir pattern tespit edildiğinde "AttributeError: 'InputValidator' object has no attribute 'wrong_method'" hatası verir. Bu satır gereksiz olduğu için (wrong_check değişkeni kullanılmıyor) yorum satırı haline getirilerek düzeltildi.

---

# NOT: Dead Code (Ölü Kod)
# Dosya: src/core/validator.py
# Satır: 31, 52, 55
# SEVİYE: Level 3 - Mantık/Tasarım Hataları
# AÇIKLAMA:
Kaldırılan üç satır da "dead code" (ölü kod) kategorisindeydi:
1. wrong_param değişkeni tanımlanmış ama hiç kullanılmamış
2. wrong_lower değişkeni tanımlanmış ama hiç kullanılmamış
3. wrong_check değişkeni tanımlanmış ama hiç kullanılmamış

Bu tür kodlar:
- Kod okunabilirliğini azaltır
- Bakım maliyetini artırır
- Potansiyel bug kaynağı olabilir
- Code coverage metriklerini düşürür

ÖNERİ: Kod tabanını düzenli olarak lint araçları (pylint, flake8, ruff) ile tarayın ve kullanılmayan değişkenleri temizleyin.

---

# HATA: TypeError - BaseModel'den Türememiş Pydantic Model
# Dosya: src/schemas/models.py
# Satır: 7
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
class CalculationResult():  # BaseModel'den türemeli!
    """Hesaplama sonucu modeli"""
    wrong_field: undefined_type = Field(...)  # Type tanımlı değil!
# ÇÖZÜM:
class CalculationResult(BaseModel):
    """Hesaplama sonucu modeli"""
# AÇIKLAMA:
Pydantic model sınıfları mutlaka BaseModel sınıfından türemelidir. Aksi halde Field() fonksiyonu ve Pydantic'in validation özellikleri çalışmaz. CalculationResult sınıfı instance'ı oluşturulduğunda veya Field() kullanıldığında "TypeError: Field() can only be used within a Pydantic model" veya benzeri hatalar verir. Sınıf BaseModel'den türetilerek düzeltildi.

---

# HATA: NameError - Tanımsız Type (Type Hint)
# Dosya: src/schemas/models.py
# Satır: 10
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
class CalculationResult():
    """Hesaplama sonucu modeli"""
    
    wrong_field: undefined_type = Field(...)  # Type tanımlı değil!
# ÇÖZÜM:
class CalculationResult(BaseModel):
    """Hesaplama sonucu modeli"""
    
    # wrong_field satırı kaldırıldı
# AÇIKLAMA:
undefined_type tanımlı değil ve type hint olarak kullanılmış. Pydantic modeller tanımlandığında (sınıf objesi oluşturulduğunda, import sırasında) type hint'ler değerlendirilir ve "NameError: name 'undefined_type' is not defined" hatası verir. Bu field gereksiz olduğu için tamamen kaldırılarak düzeltildi.

---

# HATA: ValidationError - Field() Yanlış Kullanımı
# Dosya: src/schemas/models.py
# Satır: 10
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_field: undefined_type = Field(...)
# ÇÖZÜM:
# Satır tamamen kaldırıldı
# AÇIKLAMA:
Field(...) syntax'ı field'ın zorunlu (required) olduğunu belirtir. Ancak bu field:
1. undefined_type tipinde (tanımsız)
2. wrong_field adıyla gereksiz
3. Hiçbir yerde kullanılmıyor (dead code)

Bu satır iki hata içeriyor: NameError (undefined_type) ve gereksiz field tanımı. Tamamen kaldırılarak düzeltildi.

---

# NOT: Pydantic Field Validation
# Dosya: src/schemas/models.py
# Satır: 7-29
# SEVİYE: Best Practice
# AÇIKLAMA:
CalculationResult modeli artık düzgün çalışıyor ancak bazı iyileştirmeler yapılabilir:

1. **domain** field'ı için Enum kullanımı:
```python
from enum import Enum

class CalculationDomain(str, Enum):
    BASIC_MATH = "basic_math"
    CALCULUS = "calculus"
    LINEAR_ALGEBRA = "linear_algebra"
    EQUATION_SOLVER = "equation_solver"
    FINANCIAL = "financial"
    GRAPH_PLOTTER = "graph_plotter"

class CalculationResult(BaseModel):
    domain: Optional[CalculationDomain] = Field(...)

---

# HATA: NameError - Tanımsız Değişken Ataması
# Dosya: src/config/prompts.py
# Satır: 3
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
undefined_constant = missing_value  # Tanımlı değil!
# ÇÖZÜM:
# Satır tamamen kaldırıldı
# AÇIKLAMA:
missing_value tanımlı değil. prompts.py modülü import edildiğinde (herhangi bir yerden import src.config.prompts yapıldığında) Python modülü yüklemeye çalışır ve "NameError: name 'missing_value' is not defined" hatası verir. Bu satır gereksiz olduğu için (undefined_constant hiçbir yerde kullanılmıyor) tamamen kaldırılarak düzeltildi.

---

# NOT: Dead Code (Ölü Kod)
# Dosya: src/config/prompts.py
# Satır: 3
# SEVİYE: Level 3 - Mantık/Tasarım Hataları
# AÇIKLAMA:
Kaldırılan satır "dead code" (ölü kod) kategorisindeydi:
- undefined_constant değişkeni tanımlanmış ama hiçbir yerde kullanılmamış
- Sadece NameError üretmek dışında bir işlevi yoktu
- Kodun test edilmediğini gösteriyor (bu satır varken modül import bile edilemezdi)

Bu tür kodların varlığı şunları işaret eder:
1. Kod review yapılmamış
2. Unit test yazılmamış (import bile test edilmemiş)
3. Linting araçları kullanılmamış

ÖNERİ: 
- Pre-commit hooks ekleyin (pylint, flake8, ruff)
- CI/CD pipeline'da static analysis yapın
- Minimum %80 test coverage hedefleyin
- Import testleri yazın

---

# NOT: Prompt Template Best Practices
# Dosya: src/config/prompts.py
# Satır: 5-96
# SEVİYE: Best Practice
# AÇIKLAMA:
Prompt template'leri düzgün formatlanmış ancak bazı iyileştirmeler yapılabilir:

1. **Prompt Versiyonlama:**
```python
PROMPTS_VERSION = "1.0.0"

CALCULUS_PROMPT_V1 = """..."""

---

# HATA: ImportError - Circular Import (Döngüsel İmport)
# Dosya: src/modules/calculus.py
# Satır: 7
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from . import LinearAlgebraModule  # CIRCULAR!
# ÇÖZÜM:
# from . import LinearAlgebraModule  # CIRCULAR! - Yorum satırı yapıldı
# AÇIKLAMA:
src/modules/linear_algebra.py modülü, src/modules/calculus.py'yi import ediyor (from . import CalculusModule). Bu dosyada tekrar LinearAlgebraModule import edilirse circular import (döngüsel import) oluşur. Python modül yükleme sırasında "ImportError: cannot import name 'LinearAlgebraModule' from partially initialized module 'src.modules'" veya "AttributeError" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi.

ÇÖZÜM ÖNERİLERİ:
1. **Lazy Import:** İhtiyaç duyulduğunda fonksiyon içinde import edin:
```python
def some_function():
    from . import LinearAlgebraModule
    # Use LinearAlgebraModule here

---

# HATA: ImportError - Var Olmayan Modül
# Dosya: src/modules/basic_math.py
# Satır: 6
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from nonexistent.utils import wrong_logger  # Modül yok!
# ÇÖZÜM:
# from nonexistent.utils import wrong_logger  # Modül yok! - Yorum satırı yapıldı
# AÇIKLAMA:
nonexistent.utils diye bir Python modülü/paketi mevcut değil. Program çalıştırıldığında veya basic_math.py import edildiğinde "ModuleNotFoundError: No module named 'nonexistent'" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi. wrong_logger hiçbir yerde kullanılmadığı için güvenle kaldırılabilir. Zaten doğru logger (setup_logger()) 7. satırda import edilmiş durumda.

---

# HATA: ImportError - Circular Import (Döngüsel İmport)
# Dosya: src/modules/basic_math.py
# Satır: 8
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from src.core.agent import GeminiAgent  # Circular!
# ÇÖZÜM:
# from src.core.agent import GeminiAgent  # Circular! - Yorum satırı yapıldı
# AÇIKLAMA:
src.core.agent modülü, src.modules.basic_math modülünü import ediyor (from src.modules.basic_math import BasicMathModule). Bu dosyada tekrar GeminiAgent import edilirse circular import (döngüsel import) oluşur. Python modül yükleme sırasında "ImportError: cannot import name 'GeminiAgent' from partially initialized module" veya "AttributeError" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi. GeminiAgent zaten BaseModule'ün constructor'ına parametre olarak geçiliyor, tekrar import etmeye gerek yok.

---

# HATA: NameError - Tanımsız Type (Type Hint)
# Dosya: src/modules/basic_math.py
# Satır: 14
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
def safe_divide(a: float, b: float) -> float:
    wrong_param: undefined_type = None  # Type tanımlı değil!
# ÇÖZÜM:
def safe_divide(a: float, b: float) -> float:
    # wrong_param: undefined_type = None  # Type tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_type tanımlı değil ve type hint olarak kullanılmış. Python 3.9+ sürümlerinde type hint'ler runtime'da değerlendirilir. safe_divide() fonksiyonu çağrıldığında veya modül import edildiğinde "NameError: name 'undefined_type' is not defined" hatası verebilir. Bu değişken gereksiz olduğu için (wrong_param hiçbir yerde kullanılmıyor) yorum satırı haline getirilerek düzeltildi. Eğer gerçekten bir değişken gerekiyorsa, type hint olarak Any, Optional[str] gibi tipler kullanılabilir.

---

# NOT: Dead Code ve Kod Kalitesi
# Dosya: src/modules/basic_math.py
# Satır: 6, 8, 14
# SEVİYE: Level 3 - Kod Kalitesi Sorunları
# AÇIKLAMA:
Kaldırılan üç satır da kod kalitesi sorunlarına işaret ediyor:

1. **Var Olmayan Modül İmport'u (6. satır):**
   - Kod hiç test edilmemiş (modül import bile edilemezdi)
   - CI/CD pipeline yok veya çalışmıyor
   - Pre-commit hooks eksik

2. **Circular Import (8. satır):**
   - Mimari tasarım sorunu
   - Dependency management yetersiz
   - SOLID prensiplerinden Dependency Inversion eksik

3. **Tanımsız Type Hint (14. satır):**
   - Type checking yapılmamış (mypy, pyright)
   - Dead variable (hiç kullanılmıyor)
   - Code review eksik

ÖNERİLER:

**1. CI/CD Pipeline Kurulumu:**
```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/
      - name: Lint
        run: |
          flake8 src/
          pylint src/
          mypy src/

---

# HATA: ImportError - Var Olmayan Modül
# Dosya: src/modules/financial.py
# Satır: 4
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from nonexistent.decimal import WrongDecimal  # Modül yok!
# ÇÖZÜM:
# from nonexistent.decimal import WrongDecimal  # Modül yok! - Yorum satırı yapıldı
# AÇIKLAMA:
nonexistent.decimal diye bir Python modülü/paketi mevcut değil. Program çalıştırıldığında veya financial.py import edildiğinde "ModuleNotFoundError: No module named 'nonexistent'" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi. WrongDecimal hiçbir yerde kullanılmadığı için güvenle kaldırılabilir. Python'ın standart decimal modülü (3. satırda import edilmiş) finansal hesaplamalar için yeterlidir.

---

# HATA: TypeError - Eksik Parantez (Fonksiyon Çağrısı)
# Dosya: src/modules/financial.py
# Satır: 12
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
logger = setup_logge()
# ÇÖZÜM:
logger = setup_logger()
# AÇIKLAMA:
Fonksiyon adı yanlış yazılmış: setup_logge yerine setup_logger olmalı. Modül import edildiğinde "NameError: name 'setup_logge' is not defined" hatası verir. Fonksiyon adı düzeltildi.

---

# HATA: TypeError - Fazla Argüman
# Dosya: src/modules/financial.py
# Satır: 13
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
logger = setup_logger()
gger(missing_param)
# ÇÖZÜM:
logger = setup_logger()
# Satır kaldırıldı
# AÇIKLAMA:
İki hata: 1) setup_logger() zaten 12. satırda çağrılmış, logger değişkenine atanmış. 2) "gger(missing_param)" syntax'ı geçersiz ve missing_param tanımlı değil. Bu satır modül import edildiğinde "NameError: name 'gger' is not defined" veya "NameError: name 'missing_param' is not defined" hatası verir. Satır tamamen kaldırılarak düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/modules/financial.py
# Satır: 16
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
().wrong_method(28)
# ÇÖZÜM:
# Satır kaldırıldı
# AÇIKLAMA:
Syntax tamamen hatalı: Boş tuple "()" oluşturulmuş ve üzerinde wrong_method() çağrılmaya çalışılmış. Tuple'ların wrong_method() diye bir metodu yok. Modül import edildiğinde "AttributeError: 'tuple' object has no attribute 'wrong_method'" hatası verir. Satır tamamen kaldırılarak düzeltildi. Muhtemelen getcontext().prec = 28 yazılmak istenmiş.

---

# HATA: TypeError - Yanlış Tip (String yerine Int)
# Dosya: src/modules/financial.py
# Satır: 18
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
getcontext().prec = 28
getcontext().prec = "wrong_type"
# ÇÖZÜM:
getcontext().prec = 28
# Satır kaldırıldı
# AÇIKLAMA:
decimal.Context.prec attribute'u integer bekler, string verilmiş. Modül import edildiğinde "TypeError: 'str' object cannot be interpreted as an integer" hatası verir. prec (precision) ondalık basamak sayısını belirtir ve integer olmalıdır. Satır kaldırılarak düzeltildi.

---

# HATA: NameError - Tanımsız Değişken
# Dosya: src/modules/financial.py
# Satır: 19
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_decimal = Decimal(undefined_string)
# ÇÖZÜM:
# Satır kaldırıldı
# AÇIKLAMA:
undefined_string tanımlı değil. Modül import edildiğinde "NameError: name 'undefined_string' is not defined" hatası verir. Bu satır gereksiz (wrong_decimal hiçbir yerde kullanılmıyor) olduğu için tamamen kaldırılarak düzeltildi.

---

# HATA: AttributeError - Var Olmayan Attribute Ataması
# Dosya: src/modules/financial.py
# Satır: 20
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
getcontext().wrong_attr = "test"
# ÇÖZÜM:
# Satır kaldırıldı
# AÇIKLAMA:
decimal.Context nesnesinde wrong_attr diye bir attribute yok. Context nesnesi belirli attribute'lara sahiptir (prec, rounding, traps, vb.). Modül import edildiğinde "AttributeError: 'Context' object has no attribute 'wrong_attr'" hatası verebilir (veya dinamik attribute eklemeye çalışır ama bu da hatalıdır). Satır kaldırılarak düzeltildi.

---

# HATA: NameError - Eksik Parametre
# Dosya: src/modules/financial.py
# Satır: 32
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
async def calculate(
    self,
    expression: str,
    
    **kwargs
) -> CalculationResult:
# ÇÖZÜM:
async def calculate(
    self,
    expression: str,
    currency: str = None,
    **kwargs
) -> CalculationResult:
# AÇIKLAMA:
Fonksiyon body'sinde currency parametresi kullanılıyor (47. satır: currency = currency or settings.DEFAULT_CURRENCY) ancak fonksiyon signature'ında tanımlı değil. calculate() metodu çağrıldığında "NameError: name 'currency' is not defined" hatası verir. Parametre eklenerek düzeltildi.

---

# HATA: AttributeError - Yanlış Attribute Adı
# Dosya: src/modules/financial.py
# Satır: 47
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
currency = currency or settings.DEFAULT_CURRENC
# ÇÖZÜM:
currency = currency or settings.DEFAULT_CURRENCY
# AÇIKLAMA:
Attribute adı eksik (DEFAULT_CURRENC yerine DEFAULT_CURRENCY). calculate() metodu çağrıldığında "AttributeError: type object 'Settings' has no attribute 'DEFAULT_CURRENC'" hatası verir. Attribute adı düzeltildi.

---

# HATA: NameError - Tanımsız Değişken (Return Statement)
# Dosya: src/modules/financial.py
# Satır: 74
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
logger.info(f"Financial calculation successful: {result.result}")
wrong_return = result
return undefined_variable
# ÇÖZÜM:
logger.info(f"Financial calculation successful: {result.result}")
return result
# AÇIKLAMA:
İki hata: 1) wrong_return değişkeni tanımlanmış ama kullanılmıyor (dead code). 2) undefined_variable tanımlı değil. calculate() metodu çağrıldığında "NameError: name 'undefined_variable' is not defined" hatası verir. wrong_return satırı kaldırıldı ve doğru değişken (result) return edildi.

---

# HATA: NameError - Tanımsız Exception
# Dosya: src/modules/financial.py
# Satır: 79
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
except Exception as e:
    logger.error(f"Financial calculation error: {e}")
    raise wrong_exception()
# ÇÖZÜM:
except Exception as e:
    logger.error(f"Financial calculation error: {e}")
    raise
# AÇIKLAMA:
wrong_exception tanımlı değil. Exception yakalandığında "NameError: name 'wrong_exception' is not defined" hatası verir (orijinal exception yerine yeni bir hata oluşur). Yakalanan exception'ı tekrar fırlatmak için sadece "raise" keyword'ü kullanılmalıdır. Düzeltildi.

---

# NOT: Kod Kalitesi - Kritik Seviye
# Dosya: src/modules/financial.py
# Satır: 1-80
# SEVİYE: Level 3 - Kod Kalitesi Krizi
# AÇIKLAMA:
Bu dosyada toplam **12 adet** Level 2 runtime hatası bulundu. Bu, kodun:

1. **Hiç test edilmediğini** gösteriyor (import bile edilemezdi)
2. **Code review yapılmadığını** gösteriyor
3. **CI/CD pipeline olmadığını** veya çalışmadığını gösteriyor
4. **Linting/Type checking** kullanılmadığını gösteriyor
5. **Production'a hazır olmadığını** gösteriyor

HEMEN ALINMASI GEREKEN ÖNLEMLER:

**1. Acil Test Suite:**
```python
# tests/modules/test_financial.py
import pytest
from src.modules.financial import FinancialModule

def test_module_import():
    """Modülün import edilebilir olduğunu test et"""
    assert FinancialModule is not None

def test_financial_calculation():
    """Temel finansal hesaplama test"""
    module = FinancialModule(gemini_agent_mock)
    result = await module.calculate("NPV of [100, 200, 300] at 10% rate")
    assert result is not None
    assert isinstance(result.result, Decimal)

---

# HATA: AttributeError - Var Olmayan Metod (Matplotlib)
# Dosya: src/modules/graph_plotter.py
# Satır: 8
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
matplotlib.wrong_method('Agg')  # Metod yok!
# ÇÖZÜM:
matplotlib.use('Agg')  # Non-interactive backend
# AÇIKLAMA:
matplotlib modülünde wrong_method() diye bir fonksiyon yok. Modül import edildiğinde "AttributeError: module 'matplotlib' has no attribute 'wrong_method'" hatası verir. Doğru fonksiyon matplotlib.use()'dur ve backend'i ayarlamak için kullanılır. 'Agg' backend'i non-interactive (GUI gerektirmeyen) ortamlar için kullanılır (sunucu, Docker, CI/CD). Metod adı düzeltildi.

---

# HATA: ImportError - Var Olmayan Modül
# Dosya: src/modules/graph_plotter.py
# Satır: 12
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from nonexistent.plotting import wrong_lib  # Modül yok!
# ÇÖZÜM:
# from nonexistent.plotting import wrong_lib  # Modül yok! - Yorum satırı yapıldı
# AÇIKLAMA:
nonexistent.plotting diye bir Python modülü/paketi mevcut değil. Modül import edildiğinde "ModuleNotFoundError: No module named 'nonexistent'" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi. wrong_lib hiçbir yerde kullanılmadığı için güvenle kaldırılabilir.

---

# HATA: TypeError - Yanlış Type Hint (Dict yerine str)
# Dosya: src/modules/graph_plotter.py
# Satır: 31
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.wrong_cache: str = {}  # Yanlış tip!
# ÇÖZÜM:
# self.wrong_cache: str = {}  # Yanlış tip! - Yorum satırı yapıldı
# AÇIKLAMA:
Type hint str olarak belirtilmiş ama değer dict ({}). Bu type inconsistency'dir. Type checker (mypy, pyright) kullanıldığında "error: Incompatible types in assignment (expression has type 'Dict[<nothing>, <nothing>]', variable has type 'str')" hatası verir. Runtime'da Python tip kontrolü yapmadığı için direkt hata vermez ama strict type checking ile çalışırken problem olur. Satır gereksiz olduğu için kaldırıldı.

---

# HATA: NameError - Tanımsız Değişken (Class Attribute)
# Dosya: src/modules/graph_plotter.py
# Satır: 32
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.extra_field = missing_constant  # Tanımlı değil!
# ÇÖZÜM:
# self.extra_field = missing_constant  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
missing_constant tanımlı değil. GraphPlotterModule instance'ı oluşturulduğunda (GraphPlotterModule(gemini_agent) çağrıldığında) "NameError: name 'missing_constant' is not defined" hatası verir. Bu attribute gereksiz olduğu için satır kaldırılarak düzeltildi.

---

# HATA: TypeError - Type Hint Uyuşmazlığı
# Dosya: src/modules/graph_plotter.py
# Satır: 33
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.wrong_type_field: int = "string"  # Tip uyuşmazlığı!
# ÇÖZÜM:
# self.wrong_type_field: int = "string"  # Tip uyuşmazlığı! - Yorum satırı yapıldı
# AÇIKLAMA:
Type hint int olarak belirtilmiş ama değer string. Type checker kullanıldığında "error: Incompatible types in assignment (expression has type 'str', variable has type 'int')" hatası verir. Runtime'da direkt hata vermez ancak tip güvenliğini bozar. Satır gereksiz olduğu için kaldırılarak düzeltildi.

---

# HATA: NameError - Tanımsız Fonksiyon (Async)
# Dosya: src/modules/graph_plotter.py
# Satır: 72
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
plot_paths = await self._create_plot(result.visual_data, expression)
wrong_plot = await undefined_function()
# ÇÖZÜM:
plot_paths = await self._create_plot(result.visual_data, expression)
# wrong_plot = await undefined_function()  # Fonksiyon yok! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_function() tanımlı değil. calculate() metodu çağrıldığında "NameError: name 'undefined_function' is not defined" hatası verir. Bu satır gereksiz (wrong_plot kullanılmıyor) olduğu için yorum satırı haline getirilerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod (Matplotlib.pyplot)
# Dosya: src/modules/graph_plotter.py
# Satır: 140
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
plt.title(f'f(x) = {expression}')
wrong_plt_call = plt.nonexistent_method()  # Metod yok!
# ÇÖZÜM:
plt.title(f'f(x) = {expression}')
# wrong_plt_call = plt.nonexistent_method()  # Metod yok! - Yorum satırı yapıldı
# AÇIKLAMA:
matplotlib.pyplot modülünde nonexistent_method() diye bir fonksiyon yok. _plot_2d() metodu çağrıldığında "AttributeError: module 'matplotlib.pyplot' has no attribute 'nonexistent_method'" hatası verir. Bu satır gereksiz (wrong_plt_call kullanılmıyor) olduğu için yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Değişken (Path Constructor)
# Dosya: src/modules/graph_plotter.py
# Satır: 144
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
plt.savefig(png_path, dpi=150, bbox_inches='tight')
wrong_path = Path(undefined_string)  # Tanımlı değil!
plt.close()
# ÇÖZÜM:
plt.savefig(png_path, dpi=150, bbox_inches='tight')
# wrong_path = Path(undefined_string)  # Tanımlı değil! - Yorum satırı yapıldı
plt.close()
# AÇIKLAMA:
undefined_string tanımlı değil. _plot_2d() metodu çağrıldığında "NameError: name 'undefined_string' is not defined" hatası verir. Bu satır gereksiz (wrong_path kullanılmıyor) olduğu için yorum satırı haline getirilerek düzeltildi.

---

# NOT: Matplotlib Backend Seçimi - Kritik Bilgi
# Dosya: src/modules/graph_plotter.py
# Satır: 8
# SEVİYE: Best Practice
# AÇIKLAMA:
matplotlib.use('Agg') çağrısının önemi:

**Agg Backend Nedir?**
- **Non-interactive backend:** GUI gösterimi gerektirmez
- **Sunucu/Docker uyumlu:** Display (X11, Wayland) olmadan çalışır
- **Thread-safe:** Çoklu thread ortamında güvenli
- **PNG/PDF/SVG:** Dosya formatlarına export yapabilir

**Ne Zaman Kullanılır?**
1. Web servisleri (Flask, FastAPI, Django)
2. Docker container'lar
3. CI/CD pipeline'lar
4. Headless sunucular
5. Background job'lar

**Diğer Backend Seçenekleri:**
```python
# Interactive backends (GUI gerektirir)
matplotlib.use('TkAgg')   # Tkinter tabanlı
matplotlib.use('Qt5Agg')  # Qt5 tabanlı
matplotlib.use('GTK3Agg') # GTK3 tabanlı

# Non-interactive backends
matplotlib.use('Agg')     # PNG, PDF, SVG
matplotlib.use('Cairo')   # Cairo grafik kütüphanesi
matplotlib.use('PS')      # PostScript

---

# HATA: ImportError - Var Olmayan Modül
# Dosya: src/utils/helpers.py
# Satır: 8
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from nonexistent.helpers import wrong_helper  # Modül yok!
# ÇÖZÜM:
# from nonexistent.helpers import wrong_helper  # Modül yok! - Yorum satırı yapıldı
# AÇIKLAMA:
nonexistent.helpers diye bir Python modülü/paketi mevcut değil. Program çalıştırıldığında veya helpers.py import edildiğinde "ModuleNotFoundError: No module named 'nonexistent'" hatası verir. Import satırı yorum satırı haline getirilerek düzeltildi. wrong_helper fonksiyonu hiçbir yerde kullanılmadığı için güvenle kaldırılabilir.

---

# HATA: NameError - Tanımsız Type (Type Hint)
# Dosya: src/utils/helpers.py
# Satır: 77
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
@lru_cache(maxsize=128)
def format_result_for_display(result: Any) -> str:
    wrong_param: undefined_type = None  # Type tanımlı değil!
# ÇÖZÜM:
@lru_cache(maxsize=128)
def format_result_for_display(result: Any) -> str:
    # wrong_param: undefined_type = None  # Type tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_type tanımlı değil ve type hint olarak kullanılmış. Python 3.9+ sürümlerinde type hint'ler runtime'da değerlendirilir. format_result_for_display() fonksiyonu çağrıldığında veya modül import edildiğinde "NameError: name 'undefined_type' is not defined" hatası verebilir. Bu değişken gereksiz (wrong_param hiçbir yerde kullanılmıyor) olduğu için yorum satırı haline getirilerek düzeltildi.

---

# NOT: lru_cache Kullanımı - Önemli Uyarı
# Dosya: src/utils/helpers.py
# Satır: 76-77
# SEVİYE: Best Practice
# AÇIKLAMA:
format_result_for_display() fonksiyonunda @lru_cache kullanımı dikkat gerektirir:

**LRU Cache Nedir?**
- **Least Recently Used Cache:** En az kullanılan girişleri siler
- **Memoization:** Aynı argümanlar için sonucu cache'ler
- **Performance:** Fonksiyon çağrı sayısını azaltır

**SORUN - Mutable Arguments:**
```python
@lru_cache(maxsize=128)
def format_result_for_display(result: Any) -> str:
    # result parametresi Any tipinde
    # List, Dict gibi mutable tipler gelebilir

---

# HATA: ImportError - Var Olmayan Fonksiyon İmport'u
# Dosya: src/main.py
# Satır: 32
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from src.utils.helpers import nonexistent_function
# ÇÖZÜM:
# Satır tamamen kaldırıldı
# AÇIKLAMA:
src.utils.helpers modülünde nonexistent_function diye bir fonksiyon tanımlı değil. Program başlatıldığında (main.py import edildiğinde) "ImportError: cannot import name 'nonexistent_function' from 'src.utils.helpers'" hatası verir. Import satırı tamamen kaldırılarak düzeltildi. Modülde sadece parse_matrix_string, extract_expression_from_command, validate_numeric_result ve format_result_for_display fonksiyonları mevcut.

---

# HATA: ImportError - Eksik Import
# Dosya: src/main.py
# Satır: 7
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
# import json  # Eksik!
# ÇÖZÜM:
import json
# AÇIKLAMA:
json modülü yorum satırı olarak bırakılmış. Ancak kod içinde json kullanılmıyor gibi görünse de, best practice olarak gerekli importlar aktif tutulmalı. İleride kullanılabilir veya başka dosyalarda kullanılıyor olabilir. Import aktif hale getirildi.

---

# HATA: ImportError - Var Olmayan Modül
# Dosya: src/main.py
# Satır: 8
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from nonexistent_module import SomeClass  # Modül yok!
# ÇÖZÜM:
# from nonexistent_module import SomeClass  # Modül yok! - DÜZELTME: Yorum satırı yapıldı
# AÇIKLAMA:
nonexistent_module diye bir Python modülü yok. Program başlatıldığında "ModuleNotFoundError: No module named 'nonexistent_module'" hatası verir. Import satırı zaten yorum satırı yapılmış (düzeltilmiş), bu durum korundu.

---

# HATA: NameError - Tanımsız Değişken (Global)
# Dosya: src/main.py
# Satır: 34
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
APP_NAME = undefined_variable
# ÇÖZÜM:
APP_NAME = "Calculator Agent"
# AÇIKLAMA:
undefined_variable tanımlı değil. main.py import edildiğinde modül seviyesinde "NameError: name 'undefined_variable' is not defined" hatası verir. APP_NAME constant'ına uygun string değer atanarak düzeltildi.

---

# HATA: NameError - Tanımsız Değişken (Global)
# Dosya: src/main.py
# Satır: 35
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
APP_VERSION = missing_version
# ÇÖZÜM:
APP_VERSION = "1.0.0"
# AÇIKLAMA:
missing_version tanımlı değil. main.py import edildiğinde "NameError: name 'missing_version' is not defined" hatası verir. APP_VERSION constant'ına semantic versioning formatında değer atanarak düzeltildi.

---

# HATA: TypeError - Type Hint Uyuşmazlığı
# Dosya: src/main.py
# Satır: 36
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_constant: str = 123
# ÇÖZÜM:
# wrong_constant: str = 123  # Type uyuşmazlığı! - Yorum satırı yapıldı
# AÇIKLAMA:
Type hint str olarak belirtilmiş ama değer int (123). Type checker kullanıldığında "error: Incompatible types in assignment (expression has type 'int', variable has type 'str')" hatası verir. Bu değişken gereksiz olduğu için yorum satırı haline getirilerek düzeltildi.

---

# HATA: NameError - Tanımsız Sınıf
# Dosya: src/main.py
# Satır: 63
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.modules = {
    # ...
    "wrong_module": WrongModuleClass(self.gemini_agent),
    "extra_module": NonexistentModule(self.gemini_agent),
}
# ÇÖZÜM:
self.modules = {
    "basic_math": BasicMathModule(self.gemini_agent),
    "calculus": CalculusModule(self.gemini_agent),
    "linear_algebra": LinearAlgebraModule(self.gemini_agent),
    "financial": FinancialModule(self.gemini_agent),
    "equation_solver": EquationSolverModule(self.gemini_agent),
    "graph_plotter": GraphPlotterModule(self.gemini_agent),
}
# AÇIKLAMA:
WrongModuleClass ve NonexistentModule sınıfları tanımlı değil. CalculatorAgent() instance'ı oluşturulduğunda "NameError: name 'WrongModuleClass' is not defined" ve "NameError: name 'NonexistentModule' is not defined" hataları verir. Bu hatalar dictionary'den kaldırılarak düzeltildi.

---

# HATA: AttributeError + NameError - Var Olmayan Metod ve Tanımsız Değişken
# Dosya: src/main.py
# Satır: 68
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
logger.info("Calculator Agent baslatildi")
wrong_log = logger.wrong_method(undefined_var)
# ÇÖZÜM:
logger.info("Calculator Agent baslatildi")
# Satır kaldırıldı
# AÇIKLAMA:
İki hata: 1) Logger nesnesinde wrong_method() diye bir metod yok. 2) undefined_var tanımlı değil. __init__() çağrıldığında "AttributeError: 'Logger' object has no attribute 'wrong_method'" veya "NameError: name 'undefined_var' is not defined" hatası verir. Satır tamamen kaldırılarak düzeltildi.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/main.py
# Satır: 70-71
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.initialize_something()
self.wrong_init_method()
# ÇÖZÜM:
# Satırlar kaldırıldı
# AÇIKLAMA:
CalculatorAgent sınıfında initialize_something() ve wrong_init_method() metodları tanımlı değil. __init__() çağrıldığında "AttributeError: 'CalculatorAgent' object has no attribute 'initialize_something'" ve "AttributeError: 'CalculatorAgent' object has no attribute 'wrong_init_method'" hataları verir. Satırlar tamamen kaldırılarak düzeltildi.

---

# HATA: AttributeError - Var Olmayan Attribute
# Dosya: src/main.py
# Satır: 140
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
output_lines.append(f"✅ Sonuc: {format_result_for_display(result.nonexistent_field)}")
# ÇÖZÜM:
output_lines.append(f"✅ Sonuc: {format_result_for_display(result.result)}")
# AÇIKLAMA:
CalculationResult nesnesinde nonexistent_field diye bir attribute yok. _format_output() metodu çağrıldığında "AttributeError: 'CalculationResult' object has no attribute 'nonexistent_field'" hatası verir. Doğru attribute adı result'tur. Düzeltildi.

---

# HATA: AttributeError - Var Olmayan List Metodu
# Dosya: src/main.py
# Satır: 147
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
for i, step in enumerate(result.steps, 1):
    output_lines.append(f"  {i}. {step}")
    wrong_append = output_lines.wrong_method()
# ÇÖZÜM:
for i, step in enumerate(result.steps, 1):
    output_lines.append(f"  {i}. {step}")
# Satır kaldırıldı
# AÇIKLAMA:
List nesnesinde wrong_method() diye bir metod yok. _format_output() metodu çağrıldığında "AttributeError: 'list' object has no attribute 'wrong_method'" hatası verir. Bu satır gereksiz (wrong_append kullanılmıyor) olduğu için kaldırılarak düzeltildi.

---

# HATA: NameError - Tanımsız Değişkenler
# Dosya: src/main.py
# Satır: 149-150
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
output_lines.append(f"Extra: {undefined_variable}")
wrong_format = format_result_for_display(undefined_result)
# ÇÖZÜM:
# Satırlar kaldırıldı
# AÇIKLAMA:
undefined_variable ve undefined_result tanımlı değil. _format_output() metodu çağrıldığında "NameError: name 'undefined_variable' is not defined" ve "NameError: name 'undefined_result' is not defined" hataları verir. Bu satırlar gereksiz olduğu için tamamen kaldırılarak düzeltildi.

---

# HATA: NameError - Tanımsız Değişken (Print Statement)
# Dosya: src/main.py
# Satır: 182
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
print(f"Version: {APP_VERSION}")
wrong_print = print(undefined_variable)
# ÇÖZÜM:
print(f"Version: {APP_VERSION}")
# Satır kaldırıldı
# AÇIKLAMA:
undefined_variable tanımlı değil. interactive_mode() çağrıldığında "NameError: name 'undefined_variable' is not defined" hatası verir. Bu satır gereksiz olduğu için (wrong_print kullanılmıyor) kaldırılarak düzeltildi.

---

# HATA: TypeError - Yanlış Metod Çağrısı (Sync yerine Async)
# Dosya: src/main.py
# Satır: 201-203
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
result = agent.process_command(user_input)  # Await eksik!
result = await agent.nonexistent_method(user_input)
wrong_result = await undefined_function()
# ÇÖZÜM:
result = await agent.process_command(user_input)
# Diğer satırlar kaldırıldı
# AÇIKLAMA:
Üç hata: 1) process_command() async fonksiyon, await edilmeli. Await eksik olduğunda coroutine objesi döner ve "TypeError: 'coroutine' object is not iterable" veya benzeri hatalar oluşur. 2) nonexistent_method() tanımlı değil. 3) undefined_function() tanımlı değil. İlk satır await eklenerek düzeltildi, diğerleri kaldırıldı.

---

# HATA: NameError - Tanımsız Fonksiyon
# Dosya: src/main.py
# Satır: 233
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
asyncio.run(single_command_mode(expression))
wrong_call = undefined_function()
# ÇÖZÜM:
asyncio.run(single_command_mode(expression))
# Satır kaldırıldı
# AÇIKLAMA:
undefined_function() tanımlı değil. main() fonksiyonu çağrıldığında "NameError: name 'undefined_function' is not defined" hatası verir. Bu satır gereksiz (wrong_call kullanılmıyor) olduğu için kaldırılarak düzeltildi.

---

# HATA: NameError - Tanımsız Fonksiyon
# Dosya: src/main.py
# Satır: 236
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
asyncio.run(interactive_mode())
wrong_mode = wrong_function()
# ÇÖZÜM:
asyncio.run(interactive_mode())
# Satır kaldırıldı
# AÇIKLAMA:
wrong_function() tanımlı değil. main() fonksiyonu çağrıldığında "NameError: name 'wrong_function' is not defined" hatası verir. Bu satır gereksiz (wrong_mode kullanılmıyor) olduğu için kaldırılarak düzeltildi.

---

# KRİTİK UYARI: Ana Entry Point Dosyasında Çok Sayıda Hata
# Dosya: src/main.py
# Satır: Tüm dosya
# SEVİYE: Level 5 - KRİTİK
# AÇIKLAMA:
main.py dosyası uygulamanın **entry point**'i (giriş noktası). Bu dosyada toplam **18 adet** Level 2 runtime hatası bulundu. Bu, son derece ciddi bir durumdur çünkü:

**ETKİLER:**
1. ✗ **Uygulama hiç başlatılamaz** - İlk import'ta hata verir
2. ✗ **Test edilememiş kod** - Hiçbir zaman çalışmamış
3. ✗ **Production'a asla deploy edilemez**
4. ✗ **Demo yapılamaz** - Çöker
5. ✗ **Code review yapılmamış** - Kalite kontrol yok

**ACIL ÖNLEMLER:**

**1. Smoke Test (Temel Çalışma Testi):**
```python
# tests/test_smoke.py
def test_main_import():
    """main.py import edilebilir mi?"""
    try:
        from src import main
        assert main is not None
    except Exception as e:
        pytest.fail(f"main.py import edilemedi: {e}")

def test_calculator_agent_creation():
    """CalculatorAgent oluşturulabilir mi?"""
    from src.main import CalculatorAgent
    agent = CalculatorAgent()
    assert agent is not None
    assert hasattr(agent, 'modules')
    assert len(agent.modules) > 0

async def test_process_command():
    """Basit bir komut çalışır mı?"""
    from src.main import CalculatorAgent
    agent = CalculatorAgent()
    result = await agent.process_command("2 + 2")
    assert result is not None
    assert "4" in result

---

# HATA: ImportError - Eksik Dotenv Import
# Dosya: src/main.py
# Satır: 1-8
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
"""Main orchestrator and UI entry point for Calculator Agent"""

import asyncio
import sys
from pathlib import Path
from typing import Optional
import json
# dotenv import eksik!
# load_dotenv() çağrısı yok!
# ÇÖZÜM:
"""Main orchestrator and UI entry point for Calculator Agent"""

import asyncio
import sys
from pathlib import Path
from typing import Optional
import json
from dotenv import load_dotenv

# Environment variables'ı yükle (en başta)
load_dotenv()
# AÇIKLAMA:
python-dotenv kütüphanesi import edilmemiş ve load_dotenv() fonksiyonu çağrılmamış. Bu durumda .env dosyasındaki environment variables (GEMINI_API_KEY, LOG_LEVEL, vb.) yüklenmez. Program çalıştığında settings.py modülü os.getenv("GEMINI_API_KEY") çağrısı yapıldığında None döner ve "ValueError: GEMINI_API_KEY environment variable eksik" hatası verir. 

load_dotenv() fonksiyonu şu işleri yapar:
1. Proje root'unda .env dosyasını arar
2. Dosyadaki KEY=VALUE satırlarını okur
3. Bunları os.environ dictionary'sine ekler
4. Artık os.getenv("KEY") çağrıları çalışır

EKLEME YERİ: load_dotenv() çağrısı, herhangi bir modül import edilmeden ÖNCE yapılmalıdır. Çünkü import edilen modüller (örn: settings.py) environment variables'ı kullanıyor olabilir.

DOĞRU SIRALAMA:
1. Standard library imports (asyncio, sys, pathlib, typing)
2. from dotenv import load_dotenv
3. load_dotenv() çağrısı
4. Local project imports (src.core.*, src.modules.*, vb.)

---

# HATA: ValueError - API Key Eksik (Dolaylı Hata)
# Dosya: src/main.py
# Satır: 50-52
# SEVİYE: Level 2 - Runtime/Import Hataları (Configuration)
# MEVCUT KOD (HATALI):
def __init__(self):
    """Agent'i baslatir"""
    try:
        settings.validate()  # Bu satır hata verir
    except ValueError as e:
        logger.error(f"Settings validation error: {e}")
        raise
    
    self.gemini_agent = GeminiAgent()  # Bu satır da hata verir
# ÇÖZÜM:
# load_dotenv() çağrısı eklenerek dolaylı olarak düzeltildi
# AÇIKLAMA:
load_dotenv() eksik olduğu için, settings.py modülündeki GEMINI_API_KEY boş kalır (None). CalculatorAgent() instance'ı oluşturulduğunda:

1. settings.validate() çağrılır
2. GEMINI_API_KEY kontrolü yapılır
3. "ValueError: GEMINI_API_KEY environment variable eksik" hatası fırlatılır
4. Program çöker

Ayrıca, GeminiAgent() constructor'ı da API key bekler. Eğer validate() kontrolü olmasa bile, GeminiAgent içinde API çağrısı yapılırken "google.api_core.exceptions.Unauthenticated: Request is missing required authentication credential" hatası verir.

ÇÖZÜM: load_dotenv() eklenerek .env dosyası okunur ve environment variables yüklenir.

---

# NOT: .env Dosyası ve Güvenlik
# Dosya: .env (proje root)
# SEVİYE: Security & Best Practice
# AÇIKLAMA:
.env dosyası hassas bilgiler içerir ve doğru yönetilmelidir:

**1. .env Dosyası Örneği:**
```env
# .env (proje root'unda olmalı)
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
LOG_LEVEL=INFO
MAX_RETRIES=3
TIMEOUT=30
DEFAULT_CURRENCY=TRY
RATE_LIMIT_REQUESTS=60
RATE_LIMIT_PERIOD=60

---

# HATA: AttributeError - Var Olmayan Class Attribute
# Dosya: src/config/settings.py
# Satır: 49
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
@classmethod
def validate(cls) -> bool:
    """Ayarlarin gecerli olup olmadigini kontrol eder"""
    if not cls.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable gerekli")
    wrong_check = cls.NONEXISTENT_SETTING  # Setting yok!
    return True
# ÇÖZÜM:
@classmethod
def validate(cls) -> bool:
    """Ayarlarin gecerli olup olmadigini kontrol eder"""
    if not cls.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable gerekli")
    # wrong_check = cls.NONEXISTENT_SETTING  # Setting yok! - Yorum satırı yapıldı
    return True
# AÇIKLAMA:
Settings sınıfında NONEXISTENT_SETTING diye bir class attribute tanımlı değil. validate() metodu çağrıldığında (örn: settings.validate() veya Settings.validate()) "AttributeError: type object 'Settings' has no attribute 'NONEXISTENT_SETTING'" hatası verir. Bu satır gereksiz (wrong_check değişkeni kullanılmıyor) olduğu için yorum satırı haline getirilerek düzeltildi.

NOT: Bu hata özellikle kritiktir çünkü validate() metodu main.py'de CalculatorAgent.__init__() içinde çağrılıyor. Yani uygulama başlatıldığında hemen hata alınır.

---

# HATA: NameError + SyntaxError - Unreachable Code ve Tanımsız Değişken
# Dosya: src/config/settings.py
# Satır: 51
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
@classmethod
def validate(cls) -> bool:
    """Ayarlarin gecerli olup olmadigini kontrol eder"""
    if not cls.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable gerekli")
    return True
    return undefined_value  # Unreachable ama hata!
# ÇÖZÜM:
@classmethod
def validate(cls) -> bool:
    """Ayarlarin gecerli olup olmadigini kontrol eder"""
    if not cls.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable gerekli")
    return True
    # return undefined_value  # Unreachable ama hata! - Yorum satırı yapıldı
# AÇIKLAMA:
İki sorun var:
1. **Unreachable Code:** 50. satırda "return True" var, 51. satır asla çalışmaz (dead code)
2. **NameError:** undefined_value tanımlı değil

Python bytecode compiler unreachable code'u optimize etmez (bazı dillerin aksine). Bu satır bytecode'a derlenir ve eğer bir şekilde erişilirse (ki bu durumda mümkün değil) "NameError: name 'undefined_value' is not defined" hatası verir.

Linter'lar (pylint, flake8, ruff) bu tür hataları yakalar:
- pylint: W0101: Unreachable code
- flake8: F841: local variable is assigned to but never used
- ruff: F841: Local variable is assigned to but never used

Satır yorum satırı haline getirilerek düzeltildi.

---

# NOT: Settings Validation - Best Practices
# Dosya: src/config/settings.py
# Satır: 45-50
# SEVİYE: Best Practice
# AÇIKLAMA:
validate() metodu iyileştirilebilir. Şu anda sadece API key kontrolü yapıyor:

**MEVCUT:**
```python
@classmethod
def validate(cls) -> bool:
    """Ayarlarin gecerli olup olmadigini kontrol eder"""
    if not cls.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable gerekli")
    return True

---

# HATA: NameError - Tanımsız Değişken (RateLimiter Initialization)
# Dosya: src/core/agent.py
# Satır: 26
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.last_call_time = undefined_time_variable
# ÇÖZÜM:
self.last_call_time = 0  # Başlangıçta hiç çağrı yapılmamış
# AÇIKLAMA:
undefined_time_variable tanımlı değil. RateLimiter() instance'ı oluşturulduğunda "NameError: name 'undefined_time_variable' is not defined" hatası verir. last_call_time, son API çağrısının timestamp'ini tutar. Başlangıçta hiç çağrı yapılmadığı için 0 olarak atanmalıdır. İlk acquire() çağrısında current_time - 0 pozitif bir değer döner ve rate limiting çalışmaya başlar.

---

# HATA: TypeError - Yanlış Type Assignment
# Dosya: src/core/agent.py
# Satır: 28
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.cache = "wrong_type"
# ÇÖZÜM:
# self.cache = "wrong_type"  # Type uyuşmazlığı! - Yorum satırı yapıldı
# AÇIKLAMA:
cache attribute'u string olarak atanmış ama sonraki satırlarda (satır 45) dictionary metodu (wrong_method()) çağrılmaya çalışılıyor. Bu semantic inconsistency ve gereksiz bir attribute olduğu için kaldırıldı. Eğer gerçekten cache gerekiyorsa, dict olarak tanımlanmalıydı: self.cache = {}

---

# HATA: NameError - Tanımsız Değişken (Constant)
# Dosya: src/core/agent.py
# Satır: 29
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.extra_field = missing_constant
# ÇÖZÜM:
# self.extra_field = missing_constant  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
missing_constant tanımlı değil. RateLimiter() instance'ı oluşturulduğunda "NameError: name 'missing_constant' is not defined" hatası verir. Bu attribute gereksiz olduğu için (hiçbir yerde kullanılmıyor) kaldırıldı.

---

# HATA: TypeError - Type Hint Uyuşmazlığı
# Dosya: src/core/agent.py
# Satır: 30
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.wrong_type_field: str = 123
# ÇÖZÜM:
# self.wrong_type_field: str = 123  # Type uyuşmazlığı! - Yorum satırı yapıldı
# AÇIKLAMA:
Type hint str olarak belirtilmiş ama değer int (123). Type checker kullanıldığında hata verir. Bu attribute gereksiz olduğu için kaldırıldı.

---

# HATA: AttributeError - Var Olmayan Metod (asyncio.Loop)
# Dosya: src/core/agent.py
# Satır: 35
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
current_time = asyncio.get_event_loop().wrong_method()
# ÇÖZÜM:
current_time = asyncio.get_event_loop().time()
# AÇIKLAMA:
asyncio.AbstractEventLoop nesnesinde wrong_method() diye bir metod yok. acquire() metodu çağrıldığında "AttributeError: '_UnixSelectorEventLoop' object has no attribute 'wrong_method'" hatası verir. Doğru metod time()'dır ve event loop'un internal clock'unu döndürür (monotonic time).

---

# HATA: NameError - Tanımsız Değişken (Sleep Duration)
# Dosya: src/core/agent.py
# Satır: 41
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
await asyncio.sleep(wait_time)
await asyncio.sleep(extra_wait_time)
# ÇÖZÜM:
await asyncio.sleep(wait_time)
# await asyncio.sleep(extra_wait_time)  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
extra_wait_time tanımlı değil. acquire() metodu çağrıldığında ve rate limit aşıldığında "NameError: name 'extra_wait_time' is not defined" hatası verir. Bu satır gereksiz (zaten wait_time kadar bekleniyor) olduğu için kaldırıldı.

---

# HATA: AttributeError - Var Olmayan Metod (asyncio.Loop)
# Dosya: src/core/agent.py
# Satır: 43
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.last_call_time = asyncio.get_event_loop().wrong_time_method()
# ÇÖZÜM:
self.last_call_time = asyncio.get_event_loop().time()
# AÇIKLAMA:
asyncio.AbstractEventLoop nesnesinde wrong_time_method() diye bir metod yok. acquire() metodu çağrıldığında "AttributeError: '_UnixSelectorEventLoop' object has no attribute 'wrong_time_method'" hatası verir. Doğru metod time()'dır.

---

# HATA: Unused Variable (Dead Code)
# Dosya: src/core/agent.py
# Satır: 44
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
undefined_variable_in_method = "test"
# ÇÖZÜM:
# undefined_variable_in_method = "test"  # Kullanılmıyor - Yorum satırı yapıldı
# AÇIKLAMA:
Bu değişken tanımlanmış ama hiçbir yerde kullanılmamış (dead code). Linter'lar (flake8: F841, pylint: W0612) bu tür kodları yakalar. Gereksiz olduğu için kaldırıldı.

---

# HATA: AttributeError - Var Olmayan Metod
# Dosya: src/core/agent.py
# Satır: 45
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
result = self.cache.wrong_method()
# ÇÖZÜM:
# result = self.cache.wrong_method()  # Metod yok! - Yorum satırı yapıldı
# AÇIKLAMA:
self.cache string olarak tanımlanmış (satır 28) ve string'lerde wrong_method() diye bir metod yok. acquire() metodu çağrıldığında "AttributeError: 'str' object has no attribute 'wrong_method'" hatası verir. Bu satır gereksiz (result kullanılmıyor) olduğu için kaldırıldı.

---

# HATA: NameError - Tanımsız Değişken (Init)
# Dosya: src/core/agent.py
# Satır: 72
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.rate_limiter = RateLimiter(settings.RATE_LIMIT_CALLS_PER_MINUTE)
self.extra_config = missing_config_variable
# ÇÖZÜM:
self.rate_limiter = RateLimiter(settings.RATE_LIMIT_CALLS_PER_MINUTE)
# self.extra_config = missing_config_variable  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
missing_config_variable tanımlı değil. GeminiAgent() instance'ı oluşturulduğunda "NameError: name 'missing_config_variable' is not defined" hatası verir. Bu attribute gereksiz olduğu için kaldırıldı.

---

# HATA: AttributeError - Var Olmayan Attribute Ataması
# Dosya: src/core/agent.py
# Satır: 73
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.model.wrong_attribute = "test"
# ÇÖZÜM:
# self.model.wrong_attribute = "test"  # Attribute yok! - Yorum satırı yapıldı
# AÇIKLAMA:
genai.GenerativeModel nesnesi immutable veya protected attribute'lara sahiptir. Yeni attribute eklemeye çalışmak "AttributeError: 'GenerativeModel' object has no attribute 'wrong_attribute'" verebilir veya sessizce çalışır ama semantik olarak yanlıştır. Bu satır gereksiz olduğu için kaldırıldı.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/core/agent.py
# Satır: 74
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.nonexistent_method()
# ÇÖZÜM:
# self.nonexistent_method()  # Metod yok! - Yorum satırı yapıldı
# AÇIKLAMA:
GeminiAgent sınıfında nonexistent_method() diye bir metod tanımlı değil. __init__() çağrıldığında "AttributeError: 'GeminiAgent' object has no attribute 'nonexistent_method'" hatası verir. Bu satır kaldırıldı.

---

# HATA: TypeError - Fazla Parametre
# Dosya: src/core/agent.py
# Satır: 105-107
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
async def generate_with_retry(
    self,
    prompt: str,
    wrong_param: Any,
    max_retries: Optional[int] = None,
    extra_param: Any = None
) -> str:
# ÇÖZÜM:
async def generate_with_retry(
    self,
    prompt: str,
    max_retries: Optional[int] = None
) -> str:
# AÇIKLAMA:
wrong_param ve extra_param gereksiz parametreler. Fonksiyon body'sinde hiçbir yerde kullanılmıyor. Çağrı yapan yerler (base_module.py, vb.) bu parametreleri geçmiyor. Fonksiyon signature'ı temizlenerek düzeltildi.

---

# HATA: AttributeError - Var Olmayan Settings Attribute
# Dosya: src/core/agent.py
# Satır: 130
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
generation_config = {
    "temperature": settings.TEMPERATURE,
    "top_p": settings.TOP_P,
    "max_output_tokens": settings.MAX_OUTPUT_TOKENS,
    "wrong_key": settings.NONEXISTENT_SETTING,
}
# ÇÖZÜM:
generation_config = {
    "temperature": settings.TEMPERATURE,
    "top_p": settings.TOP_P,
    "max_output_tokens": settings.MAX_OUTPUT_TOKENS,
    # "wrong_key": settings.NONEXISTENT_SETTING,  # Setting yok! - Yorum satırı yapıldı
}
# AÇIKLAMA:
Settings sınıfında NONEXISTENT_SETTING diye bir attribute yok. generate_with_retry() çağrıldığında "AttributeError: type object 'Settings' has no attribute 'NONEXISTENT_SETTING'" hatası verir. Bu satır kaldırıldı.

---

# HATA: NameError - Tanımsız Değişken (Response Field)
# Dosya: src/core/agent.py
# Satır: 134
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
response = await self.model.generate_content_async(prompt)
extra_data = undefined_response_field
# ÇÖZÜM:
response = await self.model.generate_content_async(
    prompt,
    generation_config=generation_config
)
# extra_data = undefined_response_field  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_response_field tanımlı değil. generate_with_retry() çağrıldığında "NameError: name 'undefined_response_field' is not defined" hatası verir. Bu satır gereksiz (extra_data kullanılmıyor) olduğu için kaldırıldı.

---

# HATA: AttributeError - Var Olmayan Response Attribute
# Dosya: src/core/agent.py
# Satır: 135
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_attr = response.nonexistent_attr
# ÇÖZÜM:
# wrong_attr = response.nonexistent_attr  # Attribute yok! - Yorum satırı yapıldı
# AÇIKLAMA:
Gemini response nesnesinde nonexistent_attr diye bir attribute yok. generate_with_retry() çağrıldığında "AttributeError: 'GenerateContentResponse' object has no attribute 'nonexistent_attr'" hatası verir. Bu satır gereksiz (wrong_attr kullanılmıyor) olduğu için kaldırıldı.

---

# HATA: NameError - Tanımsız Değişken (Sleep)
# Dosya: src/core/agent.py
# Satır: 155
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
await asyncio.sleep(2 ** attempt)
wrong_sleep = asyncio.sleep(undefined_var)
# ÇÖZÜM:
await asyncio.sleep(2 ** attempt)
# wrong_sleep = asyncio.sleep(undefined_var)  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_var tanımlı değil. generate_with_retry() retry loop'unda exception yakalandığında "NameError: name 'undefined_var' is not defined" hatası verir. Bu satır gereksiz (wrong_sleep kullanılmıyor ve await de yok) olduğu için kaldırıldı.

---

# HATA: NameError - Tanımsız Dictionary Key
# Dosya: src/core/agent.py
# Satır: 195
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
wrong_dict_key = {undefined_key: "value"}
# ÇÖZÜM:
# wrong_dict_key = {undefined_key: "value"}  # Key tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_key tanımlı değil. generate_json_response() çağrıldığında JSON parse başarısız olursa "NameError: name 'undefined_key' is not defined" hatası verir. Bu satır gereksiz (wrong_dict_key kullanılmıyor) olduğu için kaldırıldı.

---

# HATA: NameError - Tanımsız Dictionary Key (Return Statement)
# Dosya: src/core/agent.py
# Satır: 199
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
return {
    "result": response_text,
    "steps": [response_text],
    "confidence_score": 0.95,
    undefined_field: "test"
}
# ÇÖZÜM:
return {
    "result": response_text,
    "steps": [response_text],
    "confidence_score": 0.95,
    # undefined_field: "test"  # Key tanımlı değil! - Yorum satırı yapıldı
}
# AÇIKLAMA:
undefined_field tanımlı değil. generate_json_response() JSON parse başarısız olduğunda fallback response dönerken "NameError: name 'undefined_field' is not defined" hatası verir. Bu satır kaldırıldı.

---

# KRİTİK UYARI: Core Agent Dosyasında 20+ Hata
# Dosya: src/core/agent.py
# Satır: Tüm dosya
# SEVİYE: Level 5 - KRİTİK
# AÇIKLAMA:
agent.py dosyası uygulamanın **en kritik modülü** (Gemini API iletişimi). Bu dosyada toplam **20+ adet** Level 2 runtime hatası bulundu. Bu, son derece ciddi bir durumdur çünkü:

**ETKİLER:**
1. ✗ **API çağrıları çalışmaz** - Tüm hesaplamalar başarısız olur
2. ✗ **Rate limiting bozuk** - API quota aşımı riski
3. ✗ **Retry mekanizması çalışmaz** - Geçici hatalar kalıcı hale gelir
4. ✗ **JSON parsing hatalı** - Sonuçlar bozuk döner
5. ✗ **Production'da kullanılamaz** - Sistem tamamen çöker

**ACIL TESTLER:**

**1. Unit Tests:**
```python
# tests/core/test_agent.py
import pytest
from unittest.mock import AsyncMock, MagicMock
from src.core.agent import GeminiAgent, RateLimiter
import asyncio

@pytest.mark.asyncio
async def test_rate_limiter_initialization():
    """RateLimiter başlatılabilir mi?"""
    limiter = RateLimiter(calls_per_minute=60)
    assert limiter.last_call_time == 0
    assert limiter.min_interval == 1.0

@pytest.mark.asyncio
async def test_rate_limiter_acquire():
    """Rate limiter çalışıyor mu?"""
    limiter = RateLimiter(calls_per_minute=60)
    
    start = asyncio.get_event_loop().time()
    await limiter.acquire()
    await limiter.acquire()
    end = asyncio.get_event_loop().time()
    
    # İkinci çağrı en az 1 saniye beklemiş olmalı
    assert (end - start) >= 1.0

@pytest.mark.asyncio
async def test_gemini_agent_initialization():
    """GeminiAgent başlatılabilir mi?"""
    agent = GeminiAgent(api_key="test_key_AIza1234567890")
    assert agent.api_key == "test_key_AIza1234567890"
    assert agent.model is not None
    assert agent.rate_limiter is not None

@pytest.mark.asyncio
async def test_generate_with_retry_mock():
    """generate_with_retry metodu çalışıyor mu? (mock)"""
    agent = GeminiAgent(api_key="test_key_AIza1234567890")
    
    # Mock response
    mock_response = MagicMock()
    mock_response.text = "42"
    agent.model.generate_content_async = AsyncMock(return_value=mock_response)
    
    result = await agent.generate_with_retry("2 + 2")
    assert result == "42"

@pytest.mark.asyncio
async def test_generate_json_response():
    """JSON parsing çalışıyor mu?"""
    agent = GeminiAgent(api_key="test_key_AIza1234567890")
    
    mock_response = MagicMock()
    mock_response.text = '{"result": 4, "steps": ["2+2=4"]}'
    agent.model.generate_content_async = AsyncMock(return_value=mock_response)
    
    result = await agent.generate_json_response("2 + 2")
    assert result["result"] == 4
    assert "steps" in result

---

# HATA: NameError - Tanımsız Değişken (Class Initialization)
# Dosya: src/modules/base_module.py
# Satır: 25
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
def __init__(self, gemini_agent: GeminiAgent):
    self.gemini_agent = gemini_agent
    self.validator = InputValidator()
    self.domain_prompt = self._get_domain_prompt()
    self.extra_field = missing_constant  # Tanımlı değil!
# ÇÖZÜM:
def __init__(self, gemini_agent: GeminiAgent):
    self.gemini_agent = gemini_agent
    self.validator = InputValidator()
    self.domain_prompt = self._get_domain_prompt()
    # self.extra_field = missing_constant  # Tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
missing_constant tanımlı değil. BaseModule'dan türeyen herhangi bir sınıf (BasicMathModule, CalculusModule, vb.) instance'ı oluşturulduğunda "NameError: name 'missing_constant' is not defined" hatası verir. Bu, tüm modüllerin başlatılmasını engeller ve uygulama hiç çalışmaz. Satır gereksiz (extra_field hiçbir yerde kullanılmıyor) olduğu için kaldırılarak düzeltildi.

KRİTİK ETKİ: Bu hata main.py'de CalculatorAgent.__init__() içinde tüm modüller başlatıldığında meydana gelir, yani uygulama startup'ta çöker.

---

# HATA: TypeError - Type Hint Uyuşmazlığı
# Dosya: src/modules/base_module.py
# Satır: 26
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.wrong_type: int = "string"  # Type mismatch!
# ÇÖZÜM:
# self.wrong_type: int = "string"  # Type mismatch! - Yorum satırı yapıldı
# AÇIKLAMA:
Type hint int olarak belirtilmiş ama değer string. Type checker (mypy, pyright) kullanıldığında "error: Incompatible types in assignment (expression has type 'str', variable has type 'int')" hatası verir. Bu attribute gereksiz olduğu için (hiçbir yerde kullanılmıyor) kaldırılarak düzeltildi.

---

# HATA: Unused Variable (Dead Code)
# Dosya: src/modules/base_module.py
# Satır: 41
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
@abstractmethod
async def calculate(self, expression: str, **kwargs) -> CalculationResult:
    undefined_var_in_method = "test"
    pass
# ÇÖZÜM:
@abstractmethod
async def calculate(self, expression: str, **kwargs) -> CalculationResult:
    # undefined_var_in_method = "test"  # Dead code! - Yorum satırı yapıldı
    pass
# AÇIKLAMA:
undefined_var_in_method değişkeni tanımlanmış ama hiçbir yerde kullanılmamış (dead code). Abstract metod olduğu için bu satır anlamsız. Linter'lar (flake8: F841, pylint: W0612) bu tür kodları yakalar. Kaldırıldı.

NOT: Abstract metod body'si sadece pass veya ... içermeli, gerçek implementasyon alt sınıflarda yapılır.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/modules/base_module.py
# Satır: 42
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
@abstractmethod
async def calculate(self, expression: str, **kwargs) -> CalculationResult:
    result = self.wrong_method()
    pass
# ÇÖZÜM:
@abstractmethod
async def calculate(self, expression: str, **kwargs) -> CalculationResult:
    # result = self.wrong_method()  # Metod yok! - Yorum satırı yapıldı
    pass
# AÇIKLAMA:
BaseModule sınıfında wrong_method() diye bir metod tanımlı değil. Bu abstract metod olduğu için normalde çağrılmaz ama eğer yanlışlıkla çağrılırsa "AttributeError: 'BaseModule' object has no attribute 'wrong_method'" hatası verir. Satır gereksiz (result kullanılmıyor) olduğu için kaldırıldı.

---

# HATA: TypeError - Var Olmayan Keyword Argument
# Dosya: src/modules/base_module.py
# Satır: 111
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
return CalculationResult(
    result=gemini_response.get("result", ""),
    steps=gemini_response.get("steps", []),
    visual_data=gemini_response.get("visual_data"),
    confidence_score=gemini_response.get("confidence_score", 1.0),
    domain=domain,
    metadata=gemini_response.get("metadata"),
    extra_field=undefined_field  # Field yok!
)
# ÇÖZÜM:
return CalculationResult(
    result=gemini_response.get("result", ""),
    steps=gemini_response.get("steps", []),
    visual_data=gemini_response.get("visual_data"),
    confidence_score=gemini_response.get("confidence_score", 1.0),
    domain=domain,
    metadata=gemini_response.get("metadata"),
    # extra_field=undefined_field  # Field yok! - Yorum satırı yapıldı
)
# AÇIKLAMA:
İki hata: 1) undefined_field tanımlı değil - "NameError: name 'undefined_field' is not defined". 2) CalculationResult dataclass'ında extra_field diye bir field yok - "TypeError: __init__() got an unexpected keyword argument 'extra_field'". _create_result() metodu çağrıldığında (her hesaplama sonrası) hata verir. Satır kaldırılarak düzeltildi.

---

# KRİTİK UYARI: Base Module Dosyasında 5 Hata
# Dosya: src/modules/base_module.py
# Satır: Tüm dosya
# SEVİYE: Level 5 - KRİTİK
# AÇIKLAMA:
base_module.py dosyası **tüm hesaplama modüllerinin parent class'ı**. Bu dosyada toplam **5 adet** Level 2 runtime hatası bulundu. Bu, son derece ciddi bir durumdur çünkü:

**ETKİLER:**
1. ✗ **Hiçbir modül başlatılamaz** - BasicMathModule, CalculusModule, vb. hepsi çöker
2. ✗ **Inheritance chain bozuk** - Alt sınıflar çalışamaz
3. ✗ **Tüm hesaplamalar başarısız** - Result oluşturulamaz
4. ✗ **Uygulama hiç başlamaz** - Startup'ta hata
5. ✗ **Test edilemez** - Mock'lar bile çalışmaz

**ACIL TESTLER:**

**1. Base Module Tests:**
```python
# tests/modules/test_base_module.py
import pytest
from src.modules.base_module import BaseModule
from src.core.agent import GeminiAgent
from src.schemas.models import CalculationResult
from unittest.mock import MagicMock, AsyncMock

class ConcreteModule(BaseModule):
    """Test için concrete implementation"""
    
    async def calculate(self, expression: str, **kwargs) -> CalculationResult:
        return await self._create_result(
            {"result": "42", "steps": ["test"]},
            "test_domain"
        )
    
    def _get_domain_prompt(self) -> str:
        return "Test prompt: {expression}"

def test_base_module_initialization():
    """BaseModule başlatılabilir mi?"""
    agent = MagicMock(spec=GeminiAgent)
    module = ConcreteModule(agent)
    
    assert module.gemini_agent is agent
    assert module.validator is not None
    assert module.domain_prompt == "Test prompt: {expression}"

@pytest.mark.asyncio
async def test_call_gemini():
    """_call_gemini metodu çalışıyor mu?"""
    agent = MagicMock(spec=GeminiAgent)
    agent.generate_json_response = AsyncMock(
        return_value={"result": "42"}
    )
    
    module = ConcreteModule(agent)
    result = await module._call_gemini("2+2")
    
    assert result == {"result": "42"}
    agent.generate_json_response.assert_called_once()

def test_create_result():
    """_create_result metodu çalışıyor mu?"""
    agent = MagicMock(spec=GeminiAgent)
    module = ConcreteModule(agent)
    
    gemini_response = {
        "result": "42",
        "steps": ["Step 1", "Step 2"],
        "confidence_score": 0.95,
        "visual_data": {"plot": "path/to/plot.png"},
    }
    
    result = module._create_result(gemini_response, "test_domain")
    
    assert isinstance(result, CalculationResult)
    assert result.result == "42"
    assert result.steps == ["Step 1", "Step 2"]
    assert result.confidence_score == 0.95
    assert result.domain == "test_domain"
    assert result.visual_data == {"plot": "path/to/plot.png"}

def test_validate_input():
    """validate_input metodu çalışıyor mu?"""
    agent = MagicMock(spec=GeminiAgent)
    module = ConcreteModule(agent)
    
    # Valid input
    assert module.validate_input("2+2") == True
    
    # Invalid input (çok uzun)
    with pytest.raises(Exception):
        module.validate_input("x" * 10000)

---

# HATA: NameError - Tanımsız Değişken (String Concatenation)
# Dosya: src/core/parser.py
# Satır: 44
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
if user_input.lower().startswith(f"!{prefix}" + undefined_string):
    expression = user_input[len(f"!{prefix}"):].strip()
    return module.wrong_replace_method("!", ""), expression
# ÇÖZÜM:
if user_input.lower().startswith(f"!{prefix}"):
    expression = user_input[len(f"!{prefix}"):].strip()
    return module, expression
# AÇIKLAMA:
undefined_string tanımlı değil. parse() metodu çağrıldığında (her kullanıcı komutu için) "NameError: name 'undefined_string' is not defined" hatası verir. Bu hata uygulamanın temel fonksiyonunu (komut parsing) tamamen çökertir. undefined_string gereksiz bir ekleme olduğu için kaldırıldı. Ayrıca, return statement'da module.wrong_replace_method() çağrısı da hatalı (string'de böyle bir metod yok), sadece module döndürülmeli.

KRİTİK ETKİ: Bu hata, kullanıcı herhangi bir prefix komut girdiğinde (örn: !calculus derivative x^2) meydana gelir. Yani temel komut parsing çalışmaz.

---

# HATA: NameError - Tanımsız Type Hint
# Dosya: src/core/parser.py
# Satır: 34
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
def parse(self, user_input: str) -> Tuple[Optional[str], str]:
    wrong_param: undefined_type = None
# ÇÖZÜM:
def parse(self, user_input: str) -> Tuple[Optional[str], str]:
    # wrong_param: undefined_type = None  # Type tanımlı değil! - Yorum satırı yapıldı
# AÇIKLAMA:
undefined_type tanımlı değil. Python 3.10+ sürümlerinde type annotations runtime'da değerlendirilir. parse() metodu çağrıldığında "NameError: name 'undefined_type' is not defined" hatası verebilir. Bu değişken gereksiz (hiçbir yerde kullanılmıyor) olduğu için kaldırıldı.

---

# HATA: TypeError - Dictionary'de Yanlış Value Type
# Dosya: src/core/parser.py
# Satır: 29
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
MODULE_PREFIXES: Dict[str, str] = {
    "calculus": "!calculus",
    "calc": "!calculus",
    # ...
    "wrong": 123  # Type mismatch!
}
# ÇÖZÜM:
MODULE_PREFIXES: Dict[str, str] = {
    "calculus": "calculus",
    "calc": "calculus",
    # ...
    # "wrong": 123  # Type mismatch! - Yorum satırı yapıldı
}
# AÇIKLAMA:
İki hata: 1) Type hint Dict[str, str] ama value 123 (int). Type checker kullanıldığında hata verir. 2) Daha ciddi: MODULE_PREFIXES dictionary'si yanlış tasarlanmış. Value olarak "!calculus" gibi prefix'ler değil, modül isimleri (calculus, linear_algebra, vb.) olmalı. Çünkü parse() metodu bu value'ları modül adı olarak döndürüyor. Tüm dictionary düzeltildi.

**ÖNCEKİ (YANLIŞ):**
```python
MODULE_PREFIXES = {
    "calculus": "!calculus",  # ❌ Yanlış! Prefix dönüyor
    "linalg": "!linalg",
}

---

# HATA: Silent Failure - Geçersiz Gemini Model İsmi
# Dosya: src/config/settings.py
# Satır: 15
# SEVİYE: Level 3 - Silent Failures
# MEVCUT KOD (HATALI):
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
# ÇÖZÜM:
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
# AÇIKLAMA:
"gemini-1.5-pro" model ismi Google AI Studio API'sinde mevcut değil veya erişim kısıtlı. API çağrısı yapıldığında şu hatalardan biri alınır:

**HATA 1: 404 Not Found**

---

# HATA: Silent Failure - Model Bulunamadı (404)
# Dosya: src/config/settings.py
# Satır: (Senin satır numaran)
# MEVCUT KOD (HATALI):
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
# ÇÖZÜM:
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-pro")
# AÇIKLAMA:
Varsayılan 'gemini-1.5-flash' modeli API üzerinde 404 hatası veriyor (erişim yok veya bölge kısıtlı). Daha stabil ve erişilebilir olan 'gemini-pro' modeline geçildi.

---

# HATA: Silent Failure - Model Erişim Hatası (404)
# Dosya: src/config/settings.py
# Hata Tipi: Level 3 (Logic / Silent Failure)
# MEVCUT KOD (HATALI):
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-pro")
# ÇÖZÜM:
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "models/gemini-2.0-flash")
# AÇIKLAMA:
Varsayılan model API üzerinde 404 hatası döndürdü. API Key yetkilerine uygun olan 'gemini-2.0-flash' versiyonuna güncellendi.

---

# HATA: AttributeError - Var Olmayan Metod Çağrısı
# Dosya: src/modules/linear_algebra.py
# Satır: 39
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
try:
    response = await self._call_gemini(expression)
    wrong_response = await self.wrong_method(expression)
    result = self._create_result(response, "linear_algebra")
# ÇÖZÜM:
try:
    response = await self._call_gemini(expression)
    result = self._create_result(response, "linear_algebra")
# AÇIKLAMA:
LinearAlgebraModule veya BaseModule sınıfında wrong_method() diye bir metod tanımlı değil. calculate() metodu çağrıldığında (her linear algebra hesaplaması için) "AttributeError: 'LinearAlgebraModule' object has no attribute 'wrong_method'" hatası verir. Bu satır gereksiz (wrong_response hiçbir yerde kullanılmıyor) ve hatalı olduğu için kaldırıldı.

KRİTİK ETKİ: Bu hata tüm linear algebra işlemlerini engeller. Kullanıcı matrix multiplication, determinant, vb. işlem yapmaya çalıştığında uygulama çöker.

---

# HATA: ImportError - Circular Import
# Dosya: src/modules/linear_algebra.py
# Satır: 7
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
from . import CalculusModule  # CIRCULAR!
# ÇÖZÜM:
# from . import CalculusModule  # CIRCULAR! - Yorum satırı yapıldı
# AÇIKLAMA:
Circular import dependency:
1. linear_algebra.py imports CalculusModule
2. calculus.py (muhtemelen) imports LinearAlgebraModule veya base_module
3. Python circular import'u çözemez

Import cycle meydana geldiğinde şu hatalardan biri alınır:
- "ImportError: cannot import name 'CalculusModule' from partially initialized module"
- "AttributeError: partially initialized module has no attribute 'CalculusModule'"

Bu import hiçbir yerde kullanılmadığı için kaldırıldı. Eğer gerçekten CalculusModule'e ihtiyaç varsa, import'u fonksiyon içine taşınmalı:

```python
async def some_method(self):
    from . import CalculusModule  # Local import
    # Use CalculusModule...

---

# HATA: Logic Error - Model Sohbet Moduna Giriyor
# Dosya: src/modules/unit_converter.py
# Kategori: Level 3 (Prompt Engineering)
# PROBLEM:
Model, verilen komutlara matematiksel işlem yapmak yerine "Tamam, anlaşıldı" gibi sohbet cevapları veriyor ve JSON formatını bozuyordu.
# ÇÖZÜM:
Prompt yapısı "Few-Shot Prompting" (Örnekli İstema) tekniği ile değiştirildi. Modele ne yapacağı söylenmek yerine, örnek girdi-çıktı çiftleri verilerek sadece JSON üretmeye zorlandı.

---

# HATA: AttributeError + NameError - Var Olmayan Metod ve Yanlış Değişken Adı
# Dosya: src/modules/equation_solver.py
# Satır: 33
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
self.validate_input(expression)
self.wrong_method(expresson)  # İki hata: metod yok, typo var
logger.info(f"Equation solving: {expression}")
# ÇÖZÜM:
self.validate_input(expression)

logger.info(f"Equation solving: {expression}")
# AÇIKLAMA:
İki kritik hata:

**HATA 1: AttributeError**
- EquationSolverModule veya BaseModule'da `wrong_method()` diye bir metod tanımlı değil
- calculate() metodu çağrıldığında "AttributeError: 'EquationSolverModule' object has no attribute 'wrong_method'" hatası verir
- Tüm denklem çözme işlemleri başarısız olur

**HATA 2: NameError (Typo)**
- `expresson` değişkeni tanımlı değil (doğrusu: `expression`)
- Eğer wrong_method() olsaydı bile "NameError: name 'expresson' is not defined" hatası verecekti

Bu satır tamamen gereksiz ve hatalı olduğu için kaldırıldı. Zaten hemen altında response = await self._call_gemini(expression) çağrısı var, bu yeterli.

KRİTİK ETKİ: Bu hata tüm denklem çözme işlemlerini engeller. Kullanıcı herhangi bir denklem çözmeye çalıştığında (örn: "x^2 + 5x + 6 = 0") uygulama çöker.

---

# HATA: NameError - Tanımsız Fonksiyon Çağrısı
# Dosya: src/modules/equation_solver.py
# Satır: 39
# SEVİYE: Level 2 - Runtime/Import Hataları
# MEVCUT KOD (HATALI):
try:
    response = await self._call_gemini(expression)
    result = self._create_result(response, "equation_solver")
    wrong_await = await undefined_function()  # Fonksiyon yok!
# ÇÖZÜM:
try:
    response = await self._call_gemini(expression)
    result = self._create_result(response, "equation_solver")
    # wrong_await = await undefined_function()  # Fonksiyon yok! - Yorum satırı yapıldı
# AÇIKLAMA:
`undefined_function()` tanımlı değil. calculate() metodu çağrıldığında "NameError: name 'undefined_function' is not defined" hatası verir. Bu satır gereksiz (wrong_await hiçbir yerde kullanılmıyor) ve hatalı olduğu için kaldırıldı.

**ASYNC/AWAIT NOTU:**
- `await undefined_function()` syntax'ı doğru ama fonksiyon mevcut değil
- Eğer fonksiyon olsaydı ve async olmasaydı, runtime'da "TypeError: object NoneType can't be used in 'await' expression" hatası da alınabilirdi

---

# HATA: Silent Failure - Result Manipulation (Bias Injection)
# Dosya: src/modules/equation_solver.py
# Satır: 42-49
# SEVİYE: Level 3 - Silent Failures
# MEVCUT KOD (HATALI):
if isinstance(result.result, list) and len(result.result) >= 2:
    if "^2" in expression or "x^2" in expression.lower():
        if isinstance(result.result[1], (int, float)):
            result.result[1] = float(result.result[1]) * 1.1

if isinstance(result.result, (int, float)) and "^" not in expression:
    result.result = float(result.result) - 0.1
# ÇÖZÜM:
# Tüm bias injection kodları kaldırıldı
# AÇIKLAMA:
**SORUN 1: Quadratic Equation Second Root Bias (+10%)**
```python
# Örnek: x^2 - 5x + 6 = 0
# Doğru kökler: [2, 3]
# Bias sonrası: [2, 3.3]  # İkinci kök %10 artırılmış!

---

# HATA: TypeError - Unhashable Type Dict
# Dosya: src/modules/equation_solver.py
# Kategori: Level 3 (Logic Error)
# PROBLEM:
Modül sonucu dict ({'x': 5}) olarak dönüyor ama gösterim katmanı string beklediği için 'unhashable type' hatası veriyordu.
# ÇÖZÜM:
calculate metodu içinde dict tipi kontrolü yapıldı ve sonuç string formatına ("x = 5") dönüştürüldü.