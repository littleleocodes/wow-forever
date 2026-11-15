# throttle.ps1 -ProcId <windows pid> [-Reserve 4]: pins a process (and, by inheritance, every child it starts afterwards) to all but
# the last <Reserve> logical processors and drops it to BelowNormal priority (2026-11-04, user: "make sure the CPU doesn't max out at
# 100%, I still need to be able to function on my PC"). resume_1104.sh calls it on itself before starting any lane.
# -Priority Idle is the user's "low prio mode" (2026-11-15: "Go low prio mode on the runs"): Idle with -Reserve 4 leaves the PC its
# own work first and 4 of 12 logical processors free; a child started later inherits both.
param([int]$ProcId, [int]$Reserve = 4, [string]$Priority = 'BelowNormal')
$n = [Environment]::ProcessorCount
$use = [Math]::Max(2, $n - $Reserve)
$mask = [IntPtr]::new([int64]([Math]::Pow(2, $use)) - 1)
$p = Get-Process -Id $ProcId
$p.ProcessorAffinity = $mask
$p.PriorityClass = $Priority
"throttle: pid $ProcId on $use of $n logical processors (mask $($p.ProcessorAffinity)), priority $($p.PriorityClass)"
