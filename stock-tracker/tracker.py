import csv
import os

class StockTracker:
    def __init__(self, inventory_file):
        self.inventory_file = inventory_file

    def check_stock(self):
        print("--- Stok Kontrolü Başlatıldı ---")
        alerts = []
        updated_rows = []

        with open(self.inventory_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            for row in reader:
                stock = int(row['StockLevel'])
                threshold = int(row['MinThreshold'])

                if stock == 0:
                    row['Status'] = 'OUT OF STOCK'
                    alerts.append(f"KRİTİK: {row['ProductName']} ({row['SKU']}) tamamen bitti!")
                elif stock <= threshold:
                    row['Status'] = 'LOW STOCK'
                    alerts.append(f"UYARI: {row['ProductName']} ({row['SKU']}) stokları azalıyor! Mevcut: {stock}")
                else:
                    row['Status'] = 'OK'

                updated_rows.append(row)

        # Durumları güncelle ve dosyaya yaz
        with open(self.inventory_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(updated_rows)

        for alert in alerts:
            print(alert)

        if not alerts:
            print("Tüm stok seviyeleri güvenli.")

    def add_order(self, sku, quantity):
        print(f"--- Yeni Sipariş İşleniyor: {sku} x {quantity} ---")
        updated_rows = []
        found = False

        with open(self.inventory_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            for row in reader:
                if row['SKU'] == sku:
                    found = True
                    current_stock = int(row['StockLevel'])
                    if current_stock >= quantity:
                        row['StockLevel'] = str(current_stock - quantity)
                        print(f"Sipariş onaylandı: {sku} yeni stok: {row['StockLevel']}")
                    else:
                        print(f"HATA: Yetersiz stok! ({sku})")
                updated_rows.append(row)

        if found:
            with open(self.inventory_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(updated_rows)
        else:
            print(f"HATA: SKU bulunamadı: {sku}")

if __name__ == "__main__":
    tracker = StockTracker('inventory.csv')
    tracker.check_stock()
    # Örnek sipariş işleme:
    # tracker.add_order('TSHIRT-001', 2)
