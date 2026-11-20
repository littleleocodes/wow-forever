#!/usr/bin/env bash
# tank_lane_1120.sh (2026-11-20, the audit's decision (i) on the options check): the tanks stand in front of the boss since the morning of
# 2026-11-20 (in_front: the boss parries, blocks and parry-hastes their attacks); their rotations and talent searches were made without
# it. After the damage lanes (audit_raid_1120b.sh "all done"), before the pages are final: per tank class the entry's rotation re-tuned
# (continued, the raid setting), then deep_tank.py from scratch (talent search and rotation in turns, two-move check, final race), the
# tank entries raced again, the ML builds written, the pages and the lint. BelowNormal on 10 of 12. Log deep-runs/tank-lane-1120.log.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/tl1120
LOG=$L/tank-lane-1120.log
OUT=$L/tank-lane-1120-out.log
R=_reference/data/raidsim
D=_reference/data
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
if ! grep -q "all done" $L/audit-raid-1120b.log 2>/dev/null; then
  say "waiting for audit_raid_1120b.sh (the damage lane)"
  until grep -q "all done" $L/audit-raid-1120b.log 2>/dev/null; do sleep 60; done
fi
say "start"
for ce in "warrior prot-tank" "paladin prot-tank" "druid feral-bear-tank"; do
  set -- $ce
  run tune-$1 python -u $R/apl_opt.py $1 --spec $2 --setting raid --write || say "WARNING: tune $1 $2"
  run deep-$1 python -u $R/deep_tank.py $1 --fresh || say "WARNING: deep_tank $1"
  run race-$1 bash -c "python -u $R/run.py $1 --spec $2 --write && python -u $R/run.py $1 --spec $2 --env environments --write" || say "WARNING: race $1 $2"
done
run builds bash -c "python -u $D/validate_builds.py && python -u $D/render_builds.py" || say "WARNING: builds"
run unused python -u $R/unused_abilities.py --write || say "WARNING: unused_abilities"
run pages python -u $D/render_modes.py || say "WARNING: render_modes"
run page-lint python -u $D/page_lint.py --write || say "WARNING: page_lint"
say "all done (Claude: tank values, tank weights for GearCheck, commit, push, the audit)"
