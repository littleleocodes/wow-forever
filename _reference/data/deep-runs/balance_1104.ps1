# balance_1104.ps1: runs rebalance.ps1 every 60 s while resume_1104.sh runs (2026-11-04 14:4x; started next to the runner, which
# cannot be edited while bash executes it: bash reads a script by file offset). New lane processes start with the lane's mask and
# priority (throttle.ps1's) and are re-pinned within a minute. Log: deep-runs/balance-1104.log (a line only when something changed).
# Stop: Stop-Process on this powershell (the stop procedure in resume_1104.sh's header, then this). A restart of the runner needs this
# started again: powershell -NoProfile -ExecutionPolicy Bypass -File _reference/data/deep-runs/balance_1104.ps1
param([int]$Run = 8, [int]$Bench = 6)
$L = 'F:\wow-forever\_reference\data\deep-runs'
$log = "$L\balance-1104.log"
"=== $(Get-Date -Format 'yyyy-MM-dd_HH:mm') balance start (run cores $Run, bench cores $Bench)" | Out-File -Append -Encoding utf8 $log
while ($true) {
  $runner = Get-CimInstance Win32_Process -Filter "Name='bash.exe'" | Where-Object { $_.CommandLine -like '*resume_1104.sh*' }
  if (-not $runner) { break }
  try { & "$L\rebalance.ps1" -Run $Run -Bench $Bench -Quiet | Out-File -Append -Encoding utf8 $log } catch { "error: $_" | Out-File -Append -Encoding utf8 $log }
  Start-Sleep -Seconds 60
}
"=== $(Get-Date -Format 'yyyy-MM-dd_HH:mm') balance end (runner gone)" | Out-File -Append -Encoding utf8 $log
