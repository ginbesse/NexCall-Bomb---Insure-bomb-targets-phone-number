import asyncio
import yaml
from core import RequestEngine, load_services
from utils import validate_number, setup_logger

async def main():
    # Loglama sistemini kur
    logger = setup_logger()
    
    # Yapılandırmayı yükle
    try:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("[!] Hata: config.yaml dosyası bulunamadı.")
        return

    # Kullanıcıdan girdi al
    print("--- BestServiceTester v1.2 (Optimized) ---")
    target = input("Hedef numara (Örn: 5xxxxxxxxx): ").strip()

    # Girdi doğrula
    if not validate_number(target):
        print("[!] Hata: Geçersiz numara formatı.")
        return

    # Servisleri ve motoru hazırla
    services = load_services(config)
    engine = RequestEngine()
    
    # İşlemi başlat
    logger.info(f"Test başlatılıyor: {target}")
    results = await engine.run(services, target)
    
    # Sonuçları yazdır
    for res in results:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())