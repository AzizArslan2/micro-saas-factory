import os
import json
from datetime import datetime

print(f"[{datetime.now()}] Otonom Beyin devrede: Pazar taranıyor...")
with open("brief.md", "r", encoding="utf-8") as f:
    brief = f.read()

# Gelir getirecek mikro-SaaS / otomasyon projesi taslağı
startup_data = {
    "timestamp": str(datetime.now()),
    "concept": "Automated Micro-SaaS Revenue Bot",
    "status": "Generated successfully by Autonomous Factory Engine",
    "target_action": "Deploying script to outbox"
}

os.makedirs("C:/agent/outbox", exist_ok=True)
project_name = f"startup_{datetime.now().strftime('%H%M%S')}"
project_path = f"C:/agent/outbox/{project_name}"
os.makedirs(project_path, exist_ok=True)

with open(f"{project_path}/main.py", "w", encoding="utf-8") as f:
    f.write("# Otomatik üretilen mikro-gelir botu\nprint('Bot aktif ve çalışıyor.')")

with open(f"{project_path}/requirements.txt", "w", encoding="utf-8") as f:
    f.write("requests\nbeautifulsoup4")

print(f"Yeni start-up projesi başarıyla {project_path} altına fırlatıldı!")
