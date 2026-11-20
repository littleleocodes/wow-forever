#!/usr/bin/env bash
# tank_lane_1120b.sh (2026-11-20 08:00, the audit session's lever a): tank_lane_1120.sh, started beside the raid lane when the leveling
# queue's compute ends ("numbers done" in pass-1120.log) instead of after the raid lane; no pages here (final_1120.sh renders once both
# lanes are done). The tanks stand in front of the boss since the morning of 2026-11-20 (in_front: the boss parries, blocks and
# parry-hastes their attacks); per tank class the entry's rotation re-tuned (continued, the raid setting), deep_tank.py from scratch,
# the entry raced again (race and environments). Markers deep-runs/tl1120/ (the old lane had run none). BelowNormal on 10 of 12.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/tl1120
LOG=$L/tank-lane-1120b.log
OUT=$L/tank-lane-1120b-out.log
R=_reference/data/raidsim
mkdir -p $M
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve 2 -Priority BelowNormal >> $LOG 2>&1
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> $OUT
  "$@" >> $OUT 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
if ! grep -q "numbers done" $L/pass-1120.log 2>/dev/null; then
  say "waiting for the leveling queue's compute (numbers done in pass-1120.log)"
  until grep -q "numbers done" $L/pass-1120.log 2>/dev/null; do sleep 60; done
fi
say "start"
for ce in "warrior prot-tank" "paladin prot-tank" "druid feral-bear-tank"; do
  set -- $ce
  run tune-$1 python -u $R/apl_opt.py $1 --spec $2 --setting raid --write || say "WARNING: tune $1 $2"
  run deep-$1 python -u $R/deep_tank.py $1 --fresh || say "WARNING: deep_tank $1"
  run race-$1 bash -c "python -u $R/run.py $1 --spec $2 --write && python -u $R/run.py $1 --spec $2 --env environments --write" || say "WARNING: race $1 $2"
done
say "all done (final_1120.sh renders the pages once the raid lane is done too)"
