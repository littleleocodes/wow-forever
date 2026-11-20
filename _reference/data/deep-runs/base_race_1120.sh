#!/usr/bin/env bash
# base_race_1120.sh (2026-11-20 09:20): frost-raid and arcane-dps raced on their new base rotations (upstream's frost, arcaneFireFill;
# no tuned raid file: the pointers are removed), so the rotation tuner's main builds (apl_opt.main_builds reads the last race and its
# environments) come from the new rotation. frost-raid's fresh tune at 08:25 had read the race made under the old rotation and tuned
# on opt-frost-raid-raid-dps and the Arcane preset (it kept nothing); ML Frost's rotations step and the Arcane fresh tune read this.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8 WOW_FOREVER_NO_RACIALS=1 WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs; LOG=$L/base-race-1120.log; R=_reference/data/raidsim
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve 2 -Priority BelowNormal >> $LOG 2>&1
for e in frost-raid arcane-dps; do
  echo "=== $(date +%F_%H:%M) $e" >> $LOG
  python -u $R/run.py mage --spec $e --write >> $LOG 2>&1 || echo "WARNING: race $e" >> $LOG
  python -u $R/run.py mage --spec $e --env environments --write >> $LOG 2>&1 || echo "WARNING: environments $e" >> $LOG
done
echo "=== $(date +%F_%H:%M) all done" >> $LOG
