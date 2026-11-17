# ⏰ X (Twitter) Botu Zamanlama ve Otomasyon Rehberi

Outbox altındaki projelerin sosyal medyada otomatik olarak duyurulması için `twitter_bot.py` betiğini her saat başı çalıştıracak şekilde sisteminize entegre edebilirsiniz.

---

## 1. Windows Üzerinde Zamanlama (Task Scheduler / Görev Zamanlayıcı)

Windows 11 ortamında her saat başı otomatik çalıştırmak için:

1. Başlat menüsünden **Görev Zamanlayıcı (Task Scheduler)** uygulamasını açın.
2. Sağ menüden **"Temel Görev Oluştur..." (Create Basic Task)** seçeneğine tıklayın.
3. Görev adı olarak `MicroSaaS Twitter Bot` yazın ve İleri'ye basın.
4. Tetikleyici olarak **"Günlük" (Daily)** veya **"Bilgisayar Başlatıldığında"** seçin (veya saatlik döngü için gelişmiş ayarlardan her 1 saatte bir tekrarla seçeneğini işaretleyin).
5. Eylem olarak **"Program Başlat" (Start a Program)** seçin:
   - **Program/komut dosyası:** `python`
   - **Bağımsız değişkenleri ekle:** `C:\agent\outbox\twitter_bot.py`
6. İleri diyerek görevi tamamlayın.

---

## 2. Linux / Sunucu Üzerinde Zamanlama (Crontab)

Eğer bu betiği bir bulut sunucusunda (VPS) çalıştırıyorsanız, crontab kullanarak her saat başı otomatik tetikleyebilirsiniz:

```bash
# Crontab düzenleyicisini açın
crontab -e

# Her saat başı çalıştırmak için aşağıdaki satırı ekleyin:
0 * * * * /usr/bin/python3 /agent/outbox/twitter_bot.py >> /agent/outbox/bot.log 2>&1
```

---

## 3. Gerçek Twitter (X) API v2 Entegrasyonu
Eğer otomatik tweetlerin doğrudan X hesabınızda paylaşılmasını istiyorsanız, `twitter_bot.py` içine **Tweepy** kütüphanesini ekleyebilir ve `.env` üzerinden kimlik bilgilerinizi tanımlayabilirsiniz:

```python
import tweepy

client = tweepy.Client(
    consumer_key="YOUR_API_KEY",
    consumer_secret="YOUR_API_SECRET",
    access_token="YOUR_ACCESS_TOKEN",
    access_secret="YOUR_ACCESS_SECRET"
)
client.create_tweet(text=tweet_text)
```
