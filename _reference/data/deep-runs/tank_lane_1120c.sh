#!/usr/bin/env bash
# tank_lane_1120c.sh (2026-11-20 ~11:00, "Simulator build first" for the tanks; replaces tank_lane_1120b.sh, stopped in its wait): from
# the end of the leveling compute ("numbers done"), beside the raid lane. Per tank class:
#   1. the entry's rotation re-tuned (continued, the raid setting): the tanks stand in front of the boss since the morning;
#   2. upstream parity (deep-runs/tank_upstream_race.py): the simulator's tank rotation and presets against ours, tank value;
#   3. a short check (talent_opt.py --setting raid --rounds 2) from the best arm under our rotation (a simulator preset or ours), instead
#      of deep_tank.py's full search; a check that keeps 0.5% or more is flagged ESCALATE for Claude;
#   4. the entry raced (race and environments).
# An upstream rotation 0.5% ahead on both seeds, or a simulator preset as the best arm, is flagged for Claude (base change, credited build).
# Markers deep-runs/tl1120/. BelowNormal on 10 of 12. Log deep-runs/tank-lane-1120c.log.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/tl1120
LOG=$L/tank-lane-1120c.log
OUT=$L/tank-lane-1120c-out.log
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
  run up-$1 python -u $L/tank_upstream_race.py $1 || say "WARNING: tank parity $1"
  B=$(python -c "import json; r=json.load(open('$R/tank-upstream-race.json',encoding='utf-8'))['$1']; print(r['best'])" 2>/dev/null)
  say "$1 parity best arm: $B"
  case "$B" in
    upstream\|*) say "FLAG $1: upstream's tank rotation leads ($B): base change for Claude; the check starts from our best arm" ;;
  esac
  START=$(python -c "import json; r=json.load(open('$R/tank-upstream-race.json',encoding='utf-8'))['$1']; v=r['value']; m={k: sum(x.values())/len(x) for k,x in v.items() if k.startswith('ours|')}; print(max(m, key=m.get).split('|',1)[1])" 2>/dev/null)
  say "$1 short check from: $START"
  case "$START" in "sim preset:"*) say "FLAG $1: a simulator preset leads under our rotation ($START): a credited build for Claude" ;; esac
  run check-$1 python -u $R/talent_opt.py $1 --spec $2 --start "$START" --setting raid --rounds 2 --write $1/research/raid/raidsim/candidates/check-$2.json || say "WARNING: check $1 $2"
  python -c "
import json
try:
    s = json.load(open('$1/research/raid/raidsim/candidates/check-$2.json', encoding='utf-8')).get('search') or {}
    g = s.get('gain') or 0
    print('=== short check $1: ' + ('ESCALATE' if g >= 0.005 else 'confirmed') + f' (gain {g:+.2%}; {len(s.get(\"moves\") or [])} move(s) kept)')
except Exception as ex:
    print('=== short check $1: no record', ex)" >> $LOG 2>&1
  run race-$1 bash -c "python -u $R/run.py $1 --spec $2 --write && python -u $R/run.py $1 --spec $2 --env environments --write" || say "WARNING: race $1 $2"
done
say "all done (Claude: the FLAG and ESCALATE lines; final_1120b.sh renders once the raid lane is done too)"
