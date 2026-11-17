import os
import csv
import json
from datetime import datetime

# E-Ticaret Rakip Fiyat Takip ve Alarm Otomasyonu (Competitor Price Monitor & Alert Micro-SaaS)
# Bu araç, e-ticaret satıcılarının veya küçük işletmelerin rakiplerinin fiyatlarını takip etmesini,
# belirlenen oranların üzerinde değişim olduğunda otomatik CSV raporu üretmesini ve log tutmasını sağlar.

OUTPUT_DIR = r"C:\agent\outbox\competitor-price-monitor"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class PriceMonitor:
    def __init__(self, db_path=None):
        self.db_path = db_path or os.path.join(OUTPUT_DIR, "prices.csv")
        self.init_db()

    def init_db(self):
        if not os.path.exists(self.db_path):
            with open(self.db_path, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "product_sku", "competitor_name", "old_price", "new_price", "change_pct", "status"])

    def add_price_check(self, sku, competitor, old_price, new_price):
        change_pct = 0.0
        if old_price > 0:
            change_pct = round(((new_price - old_price) / old_price) * 100, 2)

        status = "NORMAL"
        if abs(change_pct) >= 5.0:
            status = "ALERT_PRICE_SHIFT"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.db_path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, sku, competitor, old_price, new_price, change_pct, status])

        return {
            "timestamp": timestamp,
            "sku": sku,
            "competitor": competitor,
            "old_price": old_price,
            "new_price": new_price,
            "change_pct": change_pct,
            "status": status
        }

    def generate_report(self):
        reports = []
        if os.path.exists(self.db_path):
            with open(self.db_path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    reports.append(row)

        report_path = os.path.join(OUTPUT_DIR, "summary_report.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(reports, f, ensure_ascii=False, indent=2)
        return report_path

if __name__ == "__main__":
    monitor = PriceMonitor()

    # Örnek simüle edilmiş rakip fiyat kontrolleri (Demo Veriler)
    sample_data = [
        ("SKU-9910", "E-Ticaret Rakip A", 450.0, 420.0),
        ("SKU-9910", "E-Ticaret Rakip B", 460.0, 460.0),
        ("SKU-1042", "HızlıMağaza", 1200.0, 1100.0),
        ("SKU-5521", "MegaPazar", 89.90, 99.90),
    ]

    print("[*] Rakip Fiyat Takip Botu Çalıştırılıyor...")
    for sku, comp, old_p, new_p in sample_data:
        res = monitor.add_price_check(sku, comp, old_p, new_p)
        print(f"[+] Kontrol Edildi: {sku} | {comp} | Eski: {old_p} -> Yeni: {new_p} | Değişim: %{res['change_pct']} | Durum: {res['status']}")

    report_file = monitor.generate_report()
    print(f"\n[ başarı ] Özet rapor oluşturuldu: {report_file}")
    print("[ başarı ] Mikro-SaaS Projesi 'competitor-price-monitor' başarıyla outbox altına kuruldu!")
