import os
import pandas as pd
import json
from datetime import datetime

# Freelancer ve Ajanslar İçin Otomatik Gelir-Gider Takibi ve Fatura Özeti Aracı
# Mikro-SaaS Ürünü: FreelanceLedger / Auto-Invoice & Finance Tracker

OUTPUT_DIR = r"C:\agent\outbox\freelance-finance-tracker"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class FinanceTracker:
    def __init__(self, data_path=None):
        self.data_path = data_path or os.path.join(OUTPUT_DIR, "transactions.csv")
        self.init_storage()

    def init_storage(self):
        if not os.path.exists(self.data_path):
            df = pd.DataFrame(columns=["date", "client", "description", "type", "amount", "currency"])
            df.to_csv(self.data_path, index=False)

    def add_transaction(self, client, description, t_type, amount, currency="USD"):
        date_str = datetime.now().strftime("%Y-%m-%d")
        new_row = {
            "date": date_str,
            "client": client,
            "description": description,
            "type": t_type,  # 'Gelir' veya 'Gider'
            "amount": float(amount),
            "currency": currency
        }
        df = pd.read_csv(self.data_path)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(self.data_path, index=False)
        return new_row

    def generate_summary(self):
        df = pd.read_csv(self.data_path)
        if df.empty:
            return {"total_income": 0, "total_expense": 0, "net_profit": 0, "count": 0}

        income = df[df["type"] == "Gelir"]["amount"].sum()
        expense = df[df["type"] == "Gider"]["amount"].sum()
        net = income - expense

        summary = {
            "total_income": float(income),
            "total_expense": float(expense),
            "net_profit": float(net),
            "total_transactions": len(df)
        }

        report_path = os.path.join(OUTPUT_DIR, "financial_summary.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        return summary

    def generate_invoice_template(self, client_name, amount, item_desc):
        invoice_html = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <title>Fatura - {client_name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; color: #333; }}
                .invoice-box {{ max-width: 800px; margin: auto; padding: 30px; border: 1px solid #eee; box-shadow: 0 0 10px rgba(0, 0, 0, .15); }}
                .header {{ font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 20px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
                th, td {{ padding: 12px; border-bottom: 1px solid #ddd; text-align: left; }}
                th {{ background: #f8f9fa; }}
                .total {{ font-weight: bold; font-size: 18px; text-align: right; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="invoice-box">
                <div class="header">FATURA / HİZMET ÖZETİ</div>
                <p><strong>Tarih:</strong> {datetime.now().strftime("%Y-%m-%d")}</p>
                <p><strong>Müşteri / Ajans:</strong> {client_name}</p>
                <table>
                    <tr><th>Açıklama</th><th>Tutar</th></tr>
                    <tr><td>{item_desc}</td><td>{amount} USD</td></tr>
                </table>
                <div class="total">Toplam: {amount} USD</div>
            </div>
        </body>
        </html>
        """
        inv_path = os.path.join(OUTPUT_DIR, f"invoice_{client_name.lower().replace(' ', '_')}.html")
        with open(inv_path, "w", encoding="utf-8") as f:
            f.write(invoice_html)
        return inv_path

if __name__ == "__main__":
    tracker = FinanceTracker()

    print("[*] Freelancer & Ajans Finans Takipçisi Çalıştırılıyor...")

    # Örnek veriler ekleniyor
    tracker.add_transaction("Acme Corp", "Python Web Scraping Projesi", "Gelir", 1200.0, "USD")
    tracker.add_transaction("StartupX", "API Entegrasyon Danışmanlığı", "Gelir", 850.0, "USD")
    tracker.add_transaction("CloudHost", "Aylık Sunucu Gideri", "Gider", 45.0, "USD")

    summary = tracker.generate_summary()
    print(f"[+] Mali Özet Raporu Üretildi: {summary}")

    inv_file = tracker.generate_invoice_template("Acme Corp", 1200.0, "Python Web Scraping Projesi")
    print(f"[+] Örnek Fatura HTML Şablonu Oluşturuldu: {inv_file}")
    print("[ başarı ] 'freelance-finance-tracker' aracı başarıyla outbox altına kuruldu!")
