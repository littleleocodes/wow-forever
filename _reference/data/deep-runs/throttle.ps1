# throttle.ps1 -ProcId <windows pid> [-Reserve 4]: pins a process (and, by inheritance, every child it starts afterwards) to all but
# the last <Reserve> logical processors and drops it to BelowNormal priority (2026-11-04, user: "make sure the CPU doesn't max out at
# 100%, I still need to be able to function on my PC"). resume_1104.sh calls it on itself before starting any lane.
param([int]$ProcId, [int]$Reserve = 4)
$n = [Environment]::ProcessorCount
$use = [Math]::Max(2, $n - $Reserve)
$mask = [IntPtr]::new([int64]([Math]::Pow(2, $use)) - 1)
$p = Get-Process -Id $ProcId
$p.ProcessorAffinity = $mask
$p.PriorityClass = 'BelowNormal'
"throttle: pid $ProcId on $use of $n logical processors (mask $($p.ProcessorAffinity)), priority $($p.PriorityClass)"
