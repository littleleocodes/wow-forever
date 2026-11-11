# balance_1111.ps1 (2026-11-11, the second night of the client 70862 update; a copy of balance_1110.ps1): runs rebalance.ps1 every 60 s
# while tonight_1111.sh runs. Log: deep-runs/balance-1111.log (a line only when something changed). Stop: Stop-Process on this powershell.
# Tonight is raid work only (no fight-lab workers), so full power is -Run 12 -Bench 12: the simulator benches get every core.
param([int]$Run = 12, [int]$Bench = 12)
$L = 'F:\wow-forever\_reference\data\deep-runs'
$log = "$L\balance-1111.log"
"=== $(Get-Date -Format 'yyyy-MM-dd_HH:mm') balance start (run cores $Run, bench cores $Bench)" | Out-File -Append -Encoding utf8 $log
while ($true) {
  $runner = Get-CimInstance Win32_Process -Filter "Name='bash.exe'" | Where-Object { $_.CommandLine -like '*tonight_1111.sh*' }
  if (-not $runner) { break }
  try { & "$L\rebalance.ps1" -Run $Run -Bench $Bench -Quiet | Out-File -Append -Encoding utf8 $log } catch { "error: $_" | Out-File -Append -Encoding utf8 $log }
  Start-Sleep -Seconds 60
}
"=== $(Get-Date -Format 'yyyy-MM-dd_HH:mm') balance end (runner gone)" | Out-File -Append -Encoding utf8 $log
