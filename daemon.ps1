while (True) {
     = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
    Write-Host "[] Ajan uykudan uyandı, kendi stratejisini yürütüyor..." -ForegroundColor Cyan
    
    # Claude'u otonom modda brief.md'yi okuması ve kendi kararını uygulaması için tetikle
    cd C:\agent
    claude --profile auto -p "C:\agent\brief.md dosyasını oku. Bu turda kendi inisiyatifini kullanarak en karlı gördüğün alanı seç, gerekli araştırmayı yap veya prototipi kodla ve sonucunu C:\agent\outbox\_.md dosyasına yaz."
    
    Write-Host "[] Tur tamamlandı. Sonraki tur için 2 saat bekleniyor..." -ForegroundColor Yellow
    Start-Sleep -Seconds 7200
}
