param([string]$Mode = "research")
$ErrorActionPreference = "Continue"
Set-Location C:\agent
$ts = Get-Date -Format "yyyy-MM-dd_HHmm"
$log = "C:\agent\notes\run-$ts.log"

if ($Mode -eq "research") {
  $prompt = "brief.md ve ledger.md dosyalarini oku. Aktif kanal icin bu turu calistir. Kurallara uy, pipeline ve outbox altina yaz, ledger'a satir ekle. Bitince 5 satir ozet ver."
} else {
  $prompt = "ledger.md son 7 gunu oku. Hangi aday tipleri cevap aldi, hangileri bos cikti, puanlama dogru muydu? brief.md'yi guncelle ve degisiklikleri notes/ altina tarihli dosya olarak yaz."
}

$models = @(
  "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free",
  "openrouter/cohere/north-mini-code:free",
  "openrouter/google/gemma-4-31b-it:free"
)

foreach ($m in $models) {
  "=== $m | $Mode | $ts ===" | Out-File -Encoding UTF8 $log -Append
  omniroute run claude --model $m -- -p $prompt --permission-mode acceptEdits --allowedTools "Read,Write,Edit,Bash,WebFetch,WebSearch" --max-turns 30 2>&1 | Tee-Object -FilePath $log -Append
  if ($LASTEXITCODE -eq 0) { break }
  "FAIL $m -> sonraki model" | Out-File -Encoding UTF8 $log -Append
}
