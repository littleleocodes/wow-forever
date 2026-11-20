#!/usr/bin/env bash
# audit_raid_1120b.sh (2026-11-20, the independent audit's raid steps 3-5 and H15's follow-up; after audit_raid_1120.sh):
#   1. tunes: Arcane from upstream's arcaneFireFill (fresh; Ice Barrier's guarded line added), Feral from upstream's current adaptive
#      (fresh; D6: +0.87% / +0.83%), Marksmanship (raid) on the normalized pet bench;
#   2. ML talents and finals on the new bench and rotations: Beast Mastery, Marksmanship, Beast-Marks (the pet rule), Arcane,
#      Frostfire (Ice Barrier's line);
#   3. Frost (waits for Claude's marker b1120/frost-ready: the audit session's decision on upstream's frost rotation) and its ML;
#   4. destro-raid last among the raid steps (waits for b1120/destro-ready: the entry and its build), its tune and Destruction's ML;
#   5. every entry raced again (dummy and environments), ML builds and rankings, unused abilities, GearCheck's raid values, pages, lint.
# BelowNormal on 10 of 12. Log deep-runs/audit-raid-1120b.log, output audit-raid-1120b-out.log, markers deep-runs/b1120/.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/b1120
LOG=$L/audit-raid-1120b.log
OUT=$L/audit-raid-1120b-out.log
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
run tune-arcane python -u $R/apl_opt.py mage --spec arcane-dps --setting raid --fresh --write || say "WARNING: tune arcane"
run tune-feral python -u $R/apl_opt.py druid --spec feral-cat-dps --setting raid --fresh --write || say "WARNING: tune feral"
run tune-mm-raid python -u $R/apl_opt.py hunter --spec mm-raid --setting raid --write || say "WARNING: tune mm-raid"
ml ml-hunter-bm hunter "Beast Mastery"
ml ml-hunter-mm hunter "Marksmanship"
ml ml-hunter-bmmm hunter "Hybrid Beast Mastery/Marksmanship"
ml ml-mage-arcane mage "Arcane"
ml ml-mage-frostfire mage "Hybrid Fire/Frost"
if [ ! -e $M/frost-ready ]; then
  say "waiting for Claude: the Frost decision (marker b1120/frost-ready)"
  until [ -e $M/frost-ready ]; do sleep 60; done
fi
if [ -e $M/frost-fresh ]; then
  run tune-frost python -u $R/apl_opt.py mage --spec frost-raid --setting raid --fresh --write || say "WARNING: tune frost"
fi
ml ml-mage-frost mage "Frost"
ml ml-mage-arcfrost mage "Hybrid Arcane/Frost"
if [ ! -e $M/destro-ready ]; then
  say "waiting for Claude: destro-raid (marker b1120/destro-ready)"
  until [ -e $M/destro-ready ]; do sleep 60; done
fi
if [ -e $M/destro-entry ]; then
  run race-destro bash -c "python -u $R/run.py warlock --spec destro-raid --write && python -u $R/run.py warlock --spec destro-raid --env environments --write" || say "WARNING: race destro"
  run tune-destro python -u $R/apl_opt.py warlock --spec destro-raid --setting raid --fresh --write || say "WARNING: tune destro"
  ml ml-warlock-destruction warlock "Destruction"
fi
run race-all bash -c "python -u $R/run.py --all --write && python -u $R/run.py --all --env environments --write" || say "WARNING: race all"
run ml-builds bash -c "python -u $R/ml_builds.py --builds && python -u $D/validate_builds.py && python -u $D/render_builds.py && python -u $R/ml_builds.py --rank" || say "WARNING: ml_builds"
run unused python -u $R/unused_abilities.py --write || say "WARNING: unused_abilities"
run psw-all python -u $R/page_stat_weights.py --all || say "WARNING: page_stat_weights --all"
KEYS=$(python -c "import json; d = json.load(open('$R/page-stat-weights.json', encoding='utf-8'))['specs']; print(' '.join([f'page:{k}' for k, v in d.items() if v.get('weights')] + [f'pagehit:{k}' for k, v in d.items() if v.get('hit_below_cap')]))")
run errors python -u $R/weight_errors.py --only $KEYS --jobs 2 || say "WARNING: weight_errors"
run pages python -u $D/render_modes.py || say "WARNING: render_modes"
run page-lint python -u $D/page_lint.py --write || say "WARNING: page_lint"
say "all done (Claude: review the pages, the signature audit, commit, push; GearCheck values for the Addons session after the leveling queue's addon_values)"
