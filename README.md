BestServiceTester
BestServiceTester, API uç noktalarını asenkron olarak test etmek ve sistem dayanıklılığını analiz etmek için geliştirilmiş modüler bir Service Testing Framework'tür. asyncio ve aiohttp kullanarak yüksek performanslı istek işleme yeteneğine sahiptir.

Özellikler
Asenkron Mimari: Bloklanmayan I/O işlemleri ile aynı anda yüzlerce isteği işleyebilir.

Modüler Tasarım: Servis yönetimi ve motor katmanları birbirinden tamamen ayrılmıştır.

Kolay Yapılandırma: API uç noktalarını tek bir YAML dosyası üzerinden yönetebilirsiniz.

Güvenli Girdi: Dahili doğrulama mekanizması ile hatalı veri girişlerini engeller.

Kurulum
Depoyu klonlayın:

Bash
git clone https://github.com/kullaniciadi/BestServiceTester.git
cd BestServiceTester
Gerekli bağımlılıkları yükleyin:

Bash
pip install -r requirements.txt
config.yaml dosyasını yapılandırın (örneği baz alarak kendi servislerinizi ekleyin).

Kullanım
Aracı terminal üzerinden şu komutla başlatabilirsiniz:

Bash
python main.py
Dosya Yapısı
Plaintext
BestServiceTester/
├── core/             # İstek motoru ve provider mantığı
├── utils/            # Yardımcı araçlar (doğrulama, loglama)
├── config.yaml       # API konfigürasyonları
└── main.py           # Uygulama giriş noktası

Yasal Uyarı
Bu araç, yalnızca eğitim amaçlı ve sistemlerin dayanıklılığını (load testing) analiz etmek için tasarlanmıştır. Yetkisiz sistemlere istek göndermek yasal sorumluluk doğurur. Kullanıcı, gerçekleştirdiği tüm işlemlerden kendisi sorumludur.