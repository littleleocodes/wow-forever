#!/usr/bin/env bash
# audit_raid_1120c.sh (2026-11-20 08:00, the audit session's levers b and e on the user's ETA question): audit_raid_1120b.sh reordered so
# the largest page changes come first; it had not started a step (stopped in its wait). Same markers (deep-runs/b1120/).
#   1. Frost: the fresh tune on upstream's frost rotation (frost-ready / frost-fresh), ML Frost, ML Arcane-Frost;
#   2. Arcane: the fresh tune on arcaneFireFill, ML Arcane;
#   3. Destruction: race destro-raid, its fresh tune, ML Destruction across the four Destruction entries (destro-ready / destro-entry);
#   4. the Feral (fresh) and Marksmanship (raid) tunes, ML Frostfire, then the three hunter MLs (their change, the pet rule, is raced
#      and verified already);
#   5. every entry raced again (dummy and environments), ML builds and rankings, unused abilities, GearCheck's raid values (page stat
#      weights), pages, lint. weight_errors moved after the final push (lever e).
# The tank lane runs beside it from the leveling tail's end (tank_lane_1120b.sh, lever a); final_1120.sh waits for both.
# BelowNormal on 10 of 12. Log deep-runs/audit-raid-1120c.log, output audit-raid-1120c-out.log, markers deep-runs/b1120/.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/b1120
LOG=$L/audit-raid-1120c.log
OUT=$L/audit-raid-1120c-out.log
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
ml() {   # ml <marker> <class> <spec>
  run $1 python -u $R/ml_pipeline.py $2 --spec "$3" --fresh --steps targets,gear,talents,rotations,final || say "WARNING: ML $2 $3"
}
if ! grep -q "all done" $L/audit-raid-1120.log 2>/dev/null; then
  say "waiting for audit_raid_1120.sh to finish"
  until grep -q "all done" $L/audit-raid-1120.log 2>/dev/null; do sleep 60; done
fi
say "start"
# 1. Frost
if [ -e $M/frost-fresh ]; then
  run tune-frost python -u $R/apl_opt.py mage --spec frost-raid --setting raid --fresh --write || say "WARNING: tune frost"
fi
ml ml-mage-frost mage "Frost"
ml ml-mage-arcfrost mage "Hybrid Arcane/Frost"
# 2. Arcane
run tune-arcane python -u $R/apl_opt.py mage --spec arcane-dps --setting raid --fresh --write || say "WARNING: tune arcane"
ml ml-mage-arcane mage "Arcane"
# 3. Destruction
if [ -e $M/destro-entry ]; then
  run race-destro bash -c "python -u $R/run.py warlock --spec destro-raid --write && python -u $R/run.py warlock --spec destro-raid --env environments --write" || say "WARNING: race destro"
  run tune-destro python -u $R/apl_opt.py warlock --spec destro-raid --setting raid --fresh --write || say "WARNING: tune destro"
  ml ml-warlock-destruction warlock "Destruction"
fi
# 4. Feral and Marksmanship tunes, Frostfire, the hunters
run tune-feral python -u $R/apl_opt.py druid --spec feral-cat-dps --setting raid --fresh --write || say "WARNING: tune feral"
run tune-mm-raid python -u $R/apl_opt.py hunter --spec mm-raid --setting raid --write || say "WARNING: tune mm-raid"
ml ml-mage-frostfire mage "Hybrid Fire/Frost"
ml ml-hunter-bm hunter "Beast Mastery"
ml ml-hunter-mm hunter "Marksmanship"
ml ml-hunter-bmmm hunter "Hybrid Beast Mastery/Marksmanship"
# 5. races, builds, values, pages
run race-all bash -c "python -u $R/run.py --all --write && python -u $R/run.py --all --env environments --write" || say "WARNING: race all"
run ml-builds bash -c "python -u $R/ml_builds.py --builds && python -u $D/validate_builds.py && python -u $D/render_builds.py && python -u $R/ml_builds.py --rank" || say "WARNING: ml_builds"
run unused python -u $R/unused_abilities.py --write || say "WARNING: unused_abilities"
run psw-all python -u $R/page_stat_weights.py --all || say "WARNING: page_stat_weights --all"
run pages python -u $D/render_modes.py || say "WARNING: render_modes"
run page-lint python -u $D/page_lint.py --write || say "WARNING: page_lint"
say "all done (Claude: review; final_1120.sh waits for this and the tank lane)"
