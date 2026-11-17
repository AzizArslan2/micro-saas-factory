while ($true) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] --- FABRİKA YENİ BİR ÜRETİM TURUNA HAZIRLANIYOR ---" -ForegroundColor Cyan

    cd C:\agent
    
    if (!(Test-Path "brief.md")) {
        "# Start-up Fabrikası Anayasası`nHedef: 7/24 otonom çalışan, gelir üreten mikro yazılımlar geliştirmek." | Set-Content -Path "brief.md" -Encoding UTF8
    }

    Write-Host "[Claude Code] Derin pazar analizi ve yeni proje üretimi başlatılıyor..." -ForegroundColor Yellow

    # Claude Code canlı ekranda akarak çalışır, iş bitince kendi durur
    omniroute run claude --model auto -- --dangerously-skip-permissions -p "brief.md ve ledger.md dosyalarını oku. Derinlemesine pazar analizi yap, en karlı ve mantıklı mikro-SaaS projesini seçip outbox altına eksiksiz bir Python aracı üret, requirements.txt ekle ve ledger.md'yi güncelle. Eğer yeterince üretim yaptıysan veya derin bir düşünme evresine ihtiyaç duyuyorsan bunu belirt."

    # Sabit 10 dakika yerine, sanki kahve molası vermiş gibi dinamik ve insani bir dinlenme süresi (Örn: 20 ila 40 dakika arası rastgele kafasına göre dinlenme)
    $restMinutes = Get-Random -Minimum 20 -Maximum 41
    Write-Host "[$timestamp] Tur tamamlandı. Yapay zeka yoruldu, şimdilik soluklanıyor ve sonraki ilham için $restMinutes dakika mola veriyor..." -ForegroundColor Green
    
    Start-Sleep -Minutes $restMinutes
}
