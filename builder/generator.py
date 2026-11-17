import os, json
from datetime import datetime
os.makedirs("C:/agent/outbox", exist_ok=True)
data = {"status": "ok", "time": str(datetime.now())}
with open(f"C:/agent/outbox/startup_{datetime.now().strftime('%H%M%S')}.json", "w") as f:
    json.dump(data, f, indent=4)
print("Yeni start-up modülü outbox altına fırlatıldı!")
