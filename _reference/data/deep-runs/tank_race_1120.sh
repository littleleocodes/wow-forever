#!/usr/bin/env bash
# tank_race_1120.sh (2026-11-20, the audit's decision (i) on the options check): the three tank entries re-raced standing in front of the
# boss (in_front; the bear also with the raid-only bleed flag). The re-tunes and deep_tank searches come after the damage lanes.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
LOG=$L/tank-race-1120.log
R=_reference/data/raidsim
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve 2 -Priority BelowNormal >> $LOG 2>&1
for ce in "warrior prot-tank" "paladin prot-tank" "druid feral-bear-tank"; do
  set -- $ce
  echo "=== $(date +%F_%H:%M) $1 $2" >> $LOG
  python -u $R/run.py $1 --spec $2 --write >> $LOG 2>&1 || echo "WARNING: race $1 $2" >> $LOG
  python -u $R/run.py $1 --spec $2 --env environments --write >> $LOG 2>&1 || echo "WARNING: environments $1 $2" >> $LOG
done
echo "=== $(date +%F_%H:%M) all done" >> $LOG
