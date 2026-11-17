import os
import json
from flask import Flask, render_template_string, request, redirect, url_for, jsonify

# Yerel İşletmeler ve Kafe/Restoranlar İçin Dijital QR Menü ve Sipariş Yönetim Otomasyonu
# Mikro-SaaS Ürünü: QRMenset / Mini QR Menu & Order System

OUTPUT_DIR = r"C:\agent\outbox\qr-menu-order"
os.makedirs(OUTPUT_DIR, os.path.exists(OUTPUT_DIR))

app = Flask(__name__)

# Basit bellek içi veri saklama (Demo veriler)
MENU_ITEMS = [
    {"id": 1, "name": "Türk Kahvesi", "category": "İçecekler", "price": 60.0, "status": "Aktif"},
    {"id": 2, "name": "Filtre Kahve", "category": "İçecekler", "price": 75.0, "status": "Aktif"},
    {"id": 3, "name": "Cheesecake", "category": "Tatlılar", "price": 120.0, "status": "Aktif"},
    {"id": 4, "name": "Tost (Kaşarlı)", "category": "Yiyecekler", "price": 90.0, "status": "Aktif"}
]

ORDERS = []

TEMPLATE_INDEX = """
<!doctype html>
<html lang="tr">
<head>
    <meta charset="utf-8">
    <title>QR Menü & Sipariş Paneli</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f7f6; margin: 0; padding: 20px; color: #333; }
        .container { max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1, h2 { color: #2c3e50; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { padding: 12px; border-bottom: 1px solid #ddd; text-align: left; }
        th { background: #34495e; color: white; }
        .btn { background: #27ae60; color: white; padding: 8px 15px; border: none; border-radius: 4px; cursor: pointer; text-decoration: none; display: inline-block; }
        .btn-danger { background: #c0392b; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
        .form-group input, .form-group select { width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>☕ Kafe/Restoran QR Menü & Sipariş Yönetimi</h1>
        <p>Yerel işletmeler için hemen kurulabilir, komisyonsuz dijital menü ve sipariş takip aracı.</p>
        <hr>

        <h2>Mevcut Menü</h2>
        <table>
            <tr><th>ID</th><th>Ürün Adı</th><th>Kategori</th><th>Fiyat (TL)</th><th>Durum</th></tr>
            {% for item in menu %}
            <tr>
                <td>{{ item.id }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.category }}</td>
                <td>{{ item.price }} ₺</td>
                <td>{{ item.status }}</td>
            </tr>
            {% endfor %}
        </table>

        <h2>Yeni Ürün Ekle</h2>
        <form method="POST" action="/add-item">
            <div class="form-group">
                <label>Ürün Adı:</label>
                <input type="text" name="name" required>
            </div>
            <div class="form-group">
                <label>Kategori:</label>
                <input type="text" name="category" required>
            </div>
            <div class="form-group">
                <label>Fiyat (₺):</label>
                <input type="number" step="0.01" name="price" required>
            </div>
            <button type="submit" class="btn">Ürünü Ekle</button>
        </form>

        <h2>Gelen Siparişler</h2>
        <table>
            <tr><th>Sipariş ID</th><th>Masa</th><th>Ürünler</th><th>Toplam Tutar</th><th>Durum</th></tr>
            {% for order in orders %}
            <tr>
                <td>#{{ order.id }}</td>
                <td>Masa {{ order.table }}</td>
                <td>{{ order.items }}</td>
                <td>{{ order.total }} ₺</td>
                <td>{{ order.status }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE_INDEX, menu=MENU_ITEMS, orders=ORDERS)

@app.route("/add-item", methods=["POST"])
def add_item():
    name = request.form.get("name")
    category = request.form.get("category")
    try:
        price = float(request.form.get("price"))
    except ValueError:
        price = 0.0

    new_id = len(MENU_ITEMS) + 1
    MENU_ITEMS.append({"id": new_id, "name": name, "category": category, "price": price, "status": "Aktif"})
    return redirect(url_for("index"))

@app.route("/api/order", methods=["POST"])
def create_order():
    data = request.json
    order_id = len(ORDERS) + 1
    new_order = {
        "id": order_id,
        "table": data.get("table", 1),
        "items": data.get("items", ""),
        "total": data.get("total", 0.0),
        "status": "Hazırlanıyor"
    }
    ORDERS.append(new_order)
    return jsonify({"status": "success", "order_id": order_id}), 201

if __name__ == "__main__":
    print("[*] QR Menü & Sipariş Otomasyonu başlatılıyor...")
    print(f"[*] Ürünler kaydedildi: {OUTPUT_DIR}")
    app.run(debug=True, port=5000)
