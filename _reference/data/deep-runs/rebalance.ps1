# rebalance.ps1 [-Run 8] [-Bench 6] [-Quiet]: one pass over the queue's processes, pinning each by type (2026-11-04 14:40).
# Why: throttle.ps1 (8 of 12 logical processors, BelowNormal, inherited by every lane) kept the desktop usable, but after 100 min the
# two simulator benches had 0.3 of the 8 cores and the 12 fight-lab workers 7.3: at equal priority the Go bench's threads lose to
# CPU-bound python (the hunter bench: 0.1 CPU-seconds per 8 s; with the workers at Idle for 12 s, 63). So:
#   - simulator benches (foreverbench) and every other python of the queue (raidsim scripts, validate, regen, guides):
#     BelowNormal on cores 0..Bench-1;
#   - fight-lab and healer-lab python, their multiprocessing workers included: Idle on cores 0..Run-1, so they get what the benches
#     leave on the shared cores plus the last Run-Bench cores to themselves, and every run core once the raid lanes are done.
# The desktop keeps the remaining logical processors at Normal. Only the queue's own processes are touched: python and foreverbench
# whose ancestry holds a bash running resume_1104.sh or a lane script (*_1103.sh); since 16:15 nothing else (a page regen started
# from a Claude shell had been pinned too, and its fight-lab audit ran 11x slower on the shared cores). The lanes' bash processes keep
# throttle.ps1's mask. Go reads the mask when a bench starts (NumCPU = workers), so a bench started by a pinned python gets Bench workers.
# balance_1104.ps1 runs this every 60 s next to resume_1104.sh (balance_1110.ps1 next to tonight_1110.sh, 2026-11-10); standalone it
# prints what it changed.
param([int]$Run = 8, [int]$Bench = 6, [switch]$Quiet)
$benchMask = [int64]([Math]::Pow(2, $Bench)) - 1
$runMask = [int64]([Math]::Pow(2, $Run)) - 1
$procs = Get-CimInstance Win32_Process
$cmd = @{}; $parent = @{}; $pname = @{}
foreach ($p in $procs) { $id = [int]$p.ProcessId; $cmd[$id] = [string]$p.CommandLine; $parent[$id] = [int]$p.ParentProcessId; $pname[$id] = [string]$p.Name }
function InQueue($id) {   # an ancestor is the runner's or a lane's bash
  $d = 0
  while ($d -lt 12 -and $cmd.ContainsKey($id)) {
    if ($pname[$id] -eq 'bash.exe' -and $cmd[$id] -match 'resume_1104\.sh|_1103\.sh|tonight_1110\.sh') { return $true }
    $id = $parent[$id]; $d++
  }
  return $false
}
function Kind($id, $depth) {   # 'lab' or 'bench'
  if ($depth -gt 5 -or -not $cmd.ContainsKey($id)) { return 'bench' }
  $c = $cmd[$id]
  if ($c -match 'multiprocessing') { return (Kind $parent[$id] ($depth + 1)) }
  if ($c -match 'fightlab[\\/]|heallab[\\/]') { return 'lab' }
  return 'bench'
}
$changed = @(); $counts = @{ lab = 0; bench = 0 }
foreach ($p in $procs) {
  if ($p.Name -ne 'python.exe' -and $p.Name -ne 'foreverbench.exe') { continue }
  $id = [int]$p.ProcessId
  if (-not (InQueue $id)) { continue }
  $k = Kind $id 0
  $g = Get-Process -Id $id -ErrorAction SilentlyContinue
  if (-not $g) { continue }
  $counts[$k] += 1
  if ($k -eq 'lab') { $mask = $runMask; $prio = 'Idle' } else { $mask = $benchMask; $prio = 'BelowNormal' }
  try {
    if ($g.ProcessorAffinity.ToInt64() -ne $mask) { $g.ProcessorAffinity = [IntPtr]::new($mask); $changed += "$id $($p.Name -replace '\.exe$','') mask $mask" }
    if ([string]$g.PriorityClass -ne $prio) { $g.PriorityClass = $prio; $changed += "$id $($p.Name -replace '\.exe$','') $prio" }
  } catch { $changed += "$id error $_" }
}
if ($changed.Count -gt 0 -or -not $Quiet) {
  $line = "rebalance $(Get-Date -Format 'yyyy-MM-dd_HH:mm'): $($counts['bench']) bench-side, $($counts['lab']) lab processes; $($changed.Count) changes"
  if ($changed.Count -gt 0) { $line += ': ' + ($changed -join '; ') }
  $line
}
