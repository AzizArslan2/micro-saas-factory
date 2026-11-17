while ($true) {
    $timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
    Write-Host "[$timestamp] --- CLAUDE CODE OMNIROUTE MODU AKTİF ---" -ForegroundColor Cyan

    cd C:\agent
    
    if (!(Test-Path "brief.md")) {
        "# Start-up Fabrikası Anayasası`nHedef: 7/24 otonom çalışan, gelir üreten mikro yazılımlar geliştirmek." | Set-Content -Path "brief.md" -Encoding UTF8
    }

    Write-Host "[Claude Code] OmniRoute üzerinden arayüz başlatılıyor..." -ForegroundColor Yellow

    # OmniRoute üzerinden doğrudan Claude Code arayüzünü ve otomatik komut zincirini tetikliyoruz
    omniroute run claude --model auto -- --dangerously-skip-permissions -p "brief.md ve ledger.md dosyalarını oku. Pazar analizi yap, outbox klasörüne çalışır durumda yeni bir mikro start-up projesi üret ve ledger.md'yi güncelle."

    Write-Host "[$timestamp] Tur tamamlandı. 10 dakika sonra yeni tur başlayacak." -ForegroundColor Green
    Start-Sleep -Seconds 600
}
