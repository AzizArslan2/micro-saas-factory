import os
import random
import time
from datetime import datetime

# X (Twitter) Otomatik Duyuru Botu (Simülasyon / API Hazırlık)
# Outbox altındaki projelerin pazarlama metinlerini okur ve her saat başı paylaşım simülasyonu yapar.

PROJECTS = [
    "etsy-price-bot",
    "stock-tracker",
    "competitor-price-monitor",
    "qr-menu-order",
    "freelance-finance-tracker",
    "seo-content-gen"
]

def load_marketing_copy(project_name):
    marketing_path = os.path.join("C:/agent/outbox", project_name, "MARKETING.md")
    if os.path.exists(marketing_path):
        with open(marketing_path, "r", encoding="utf-8") as f:
            content = f.read()
            # İçerikten ilk sosyal medya duyuru bloğunu çekelim
            lines = content.split("\n")
            snippet = "\n".join([l for l in lines if l.startswith(">") or l.startswith("🚀") or l.startswith("📊")][:5])
            if snippet:
                return snippet
    return f"🚀 {project_name} mikro-SaaS projemiz yayında! Detaylar outbox altında."

def post_tweet(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[X - TWITTER BOT] [{timestamp}] Tweet Gönderildi:")
    print("--------------------------------------------------")
    print(text)
    print("--------------------------------------------------")

    # Gerçek Twitter API (Tweepy / v2) entegrasyonu buraya eklenebilir:
    # client.create_tweet(text=text)

def run_scheduler():
    print("=== MicroSaaS X (Twitter) Otomasyon Botu Başlatıldı ===")
    print("Her saat başı outbox projeleri X üzerinde paylaşılmak üzere hazırlanıyor...\n")

    # Test amaçlı rastgele bir proje seçip paylaşalım
    chosen_project = random.choice(PROJECTS)
    tweet_text = load_marketing_copy(chosen_project)
    post_tweet(tweet_text)

if __name__ == "__main__":
    run_scheduler()
