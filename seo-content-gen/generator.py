import os
import json
from datetime import datetime

# Mikro-SaaS Projesi: SEO Keyword & İçerik Başlık Üreteci (seo-content-gen)
# Yerel işletmeler, e-ticaret satıcıları ve blog yazarları için Google arama niyetine uygun
# anahtar kelime analizi ve SEO uyumlu içerik başlıkları / taslak planı oluşturan mini araç.

def generate_seo_package(niche):
    print(f"[*] '{niche'}' nişi için SEO anahtar kelime ve içerik başlıkları üretiliyor...")

    # Basit akıllı türetme mantığı
    keywords = [
        f"en iyi {niche}",
        f"{niche} fiyatları 2026",
        f"ucuz ve kaliteli {niche}",
        f"{niche} nasıl seçilir",
        f"{niche} kullananlar yorumları",
        f"profesyonel {niche} rehberi"
    ]

    content_ideas = [
        {
            "title": f"2026'da En Çok Tercih Edilen {niche.capitalize()} Modelleri ve İncelemeleri",
            "type": "Blog Yazısı",
            "word_count": "1200-1500 kelime",
            "target_keyword": keywords[0]
        },
        {
            "title": f"{niche.capitalize()} Satın Alırken Dikkat Edilmesi Gereken 5 Kritik Detay",
            "type": "Rehber",
            "word_count": "800-1000 kelime",
            "target_keyword": keywords[3]
        },
        {
            "title": f"Bütçe Dostu {niche} Seçenekleri: Fiyat/Performans Karşılaştırması",
            "type": "Liste Yazısı",
            "word_count": "1000-1200 kelime",
            "target_keyword": keywords[2]
        }
    ]

    report = {
        "niche": niche,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "seo_keywords": keywords,
        "content_ideas": content_ideas
    }

    return report

def main():
    print("=== SEO & İçerik Fikir Üreteci (Micro-SaaS) ===")
    niche = input("Hedef Niş / Sektör Girin (örn: kahve makinesi, butik otel, dijital ajans): ").strip()
    if not niche:
        niche = "dijital pazarlama ajansı"

    report = generate_seo_package(niche)

    out_dir = "C:/agent/outbox/seo-content-gen"
    os.makedirs(out_dir, exist_ok=True)

    json_path = os.path.join(out_dir, "seo_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)

    # Özet Markdown raporu da basalım
    md_path = os.path.join(out_dir, "README.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# SEO & İçerik Fikir Üreteci Raporu: {niche.capitalize()}\\n\\n")
        f.write(f"**Oluşturulma Tarihi:** {report['generated_at']}\\n\\n")
        f.write("## Önerilen Anahtar Kelimeler\\n")
        for kw in report['seo_keywords']:
            f.write(f"- `{kw}`\\n")
        f.write("\\n## İçerik Fikirleri ve Taslaklar\\n")
        for item in report['content_ideas']:
            f.write(f"### {item['title']}\\n")
            f.write(f"- **Tür:** {item['type']}\\n")
            f.write(f"- **Hedef Uzunluk:** {item['word_count']}\\n")
            f.write(f"- **Odak Anahtar Kelime:** `{item['target_keyword']}`\\n\\n")

    print(f"[+] Başarıyla tamamlandı! Çıktılar şurada: {out_dir}")

if __name__ == "__main__":
    main()
