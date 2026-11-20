#!/usr/bin/env bash
# final_1120b.sh (2026-11-20 11:00; final_1120.sh retargeted at the revised lanes 1120d and tank 1120c): after the raid lane (audit_raid_1120c.sh) and the tank lane (tank_lane_1120b.sh) are both done, and
# the Affliction lane (clip_retune_1120.sh): the builds rendered, the never-cast abilities measured, the tank values for GearCheck
# (tank_weights.py, as gear_phase_1118.sh ran it), GearCheck's values file, the pages and the lint. Then Claude reviews, writes the
# rotation guides, commits and pushes (stage 2), and messages the Addons session; weight_errors after the push (lever e).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/fn1120
LOG=$L/final-1120b.log
OUT=$L/final-1120b-out.log
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
for f in audit-raid-1120d.log tank-lane-1120c.log clip-retune-1120.log; do
  if ! grep -q "all done" $L/$f 2>/dev/null; then
    say "waiting for $f"
    until grep -q "all done" $L/$f 2>/dev/null; do sleep 60; done
  fi
done
say "start"
run builds bash -c "python -u $D/validate_builds.py && python -u $D/render_builds.py" || say "WARNING: builds"
run unused python -u $R/unused_abilities.py --write || say "WARNING: unused_abilities"
run tank-warrior python -u $D/characters/tank_weights.py warrior prot-tank protection-ml-tank Protection || say "WARNING: tank_weights warrior"
run tank-paladin python -u $D/characters/tank_weights.py paladin prot-tank protection-ml-tank Protection || say "WARNING: tank_weights paladin"
run tank-druid python -u $D/characters/tank_weights.py druid feral-bear-tank feral-combat-ml-tank "Feral Combat" || say "WARNING: tank_weights druid"
run addon-values python -u $D/characters/addon_values.py || say "WARNING: addon_values"
run options python -u $R/options_check.py --write || say "WARNING: options_check"
run pages python -u $D/render_modes.py || say "WARNING: render_modes"
run page-lint python -u $D/page_lint.py --write || say "WARNING: page_lint"
say "all done (Claude: guides for the re-tuned rotations, review, commit, push, the Addons message; weight_errors after the push)"
