# balance_1110.ps1 (2026-11-10, the client 70862 queue; a copy of balance_1104.ps1, which only follows resume_1104.sh and had exited at
# once): runs rebalance.ps1 every 60 s while tonight_1110.sh runs. New lane processes start with the lane's mask and priority and are
# re-pinned within a minute. Log: deep-runs/balance-1110.log (a line only when something changed).
# Stop: Stop-Process on this powershell. Full power: -Run 12 -Bench 8.
param([int]$Run = 8, [int]$Bench = 6)
$L = 'F:\wow-forever\_reference\data\deep-runs'
$log = "$L\balance-1110.log"
"=== $(Get-Date -Format 'yyyy-MM-dd_HH:mm') balance start (run cores $Run, bench cores $Bench)" | Out-File -Append -Encoding utf8 $log
while ($true) {
  $runner = Get-CimInstance Win32_Process -Filter "Name='bash.exe'" | Where-Object { $_.CommandLine -like '*tonight_1110.sh*' }
  if (-not $runner) { break }
  try { & "$L\rebalance.ps1" -Run $Run -Bench $Bench -Quiet | Out-File -Append -Encoding utf8 $log } catch { "error: $_" | Out-File -Append -Encoding utf8 $log }
  Start-Sleep -Seconds 60
}
"=== $(Get-Date -Format 'yyyy-MM-dd_HH:mm') balance end (runner gone)" | Out-File -Append -Encoding utf8 $log
