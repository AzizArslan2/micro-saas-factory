param([string]$Mode = "research")
chcp 65001 > $null
Set-Location C:\agent
$ts = Get-Date -Format "yyyy-MM-dd_HHmm"
$log = "C:\agent\notes\run-$ts.log"
$env:CLAUDE_CONFIG_DIR = "C:\Users\$env:USERNAME\.claude\profiles\auto"
$env:ANTHROPIC_AUTH_TOKEN = $env:OMNIROUTE_API_KEY

if ($Mode -eq "research") {
  $prompt = "brief.md ve ledger.md dosyalarini oku. Aktif kanal icin bu turu calistir. Kurallara uy, pipeline ve outbox altina yaz, ledger'a satir ekle. Bitince 5 satir ozet ver."
} else {
  $prompt = "ledger.md son 7 gunu oku. Hangi aday tipleri cevap aldi, hangileri bos cikti, puanlama dogru muydu? brief.md'yi guncelle ve degisiklikleri notes/ altina tarihli dosya olarak yaz."
}

$models = @(
  "gemini/gemini-3.8-flash",
  "gemini/gemini-3.7-flash",
  "groq/openai/gpt-oss-120b",
  "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
)

foreach ($m in $models) {
  "=== $m | $Mode | $ts ===" | Out-File -Encoding UTF8 $log -Append
  $out = $prompt | claude -p --model $m --permission-mode acceptEdits --allowedTools "Read,Write,Edit,Bash,WebFetch,WebSearch" --max-turns 30 2>&1
  $out | Out-File -Encoding UTF8 $log -Append
  if ($LASTEXITCODE -eq 0) { "OK $m" | Out-File -Encoding UTF8 $log -Append; break }
  "FAIL $m" | Out-File -Encoding UTF8 $log -Append
}
