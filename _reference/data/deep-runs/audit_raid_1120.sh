#!/usr/bin/env bash
# audit_raid_1120.sh (2026-11-19/20, the independent audit's steps 2, 3 and 5; user: "continue to make the changes and communicate with the
# audit session"): the warlock entries on their new bases raced and tuned, the Beast Mastery raid rotation tuned with its Summon Hawk
# line moved up, the mage and Feral upstream parity races, then the ML talents and finals for Affliction and Demonology.
# BelowNormal on 10 of 12. Log deep-runs/audit-raid-1120.log, output audit-raid-1120-out.log, markers deep-runs/a1120/.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/a1120
LOG=$L/audit-raid-1120.log
OUT=$L/audit-raid-1120-out.log
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
say "start"
for e in affliction-raid affliction-wrack-raid demonology-raid; do
  run race-$e bash -c "python -u $R/run.py warlock --spec $e --write && python -u $R/run.py warlock --spec $e --env environments --write" || { say "STOP: race $e"; exit 1; }
done
for e in affliction-wrack-raid affliction-raid demonology-raid; do
  run tune-$e python -u $R/apl_opt.py warlock --spec $e --setting raid --fresh --write || say "WARNING: tune $e"
done
run tune-bm-raid python -u $R/apl_opt.py hunter --spec bm-raid --setting raid --write || say "WARNING: tune bm-raid"
run upstream-mage python -u $R/upstream_race.py mage || say "WARNING: upstream mage"
run upstream-druid python -u $R/upstream_race.py druid || say "WARNING: upstream druid"
run ml-affliction python -u $R/ml_pipeline.py warlock --spec Affliction --fresh --steps targets,gear,talents,rotations,final || say "WARNING: ML Affliction"
run ml-demonology python -u $R/ml_pipeline.py warlock --spec Demonology --fresh --steps targets,gear,talents,rotations,final || say "WARNING: ML Demonology"
say "all done (Claude: race the warlock and hunter entries again, signature audit, unused_abilities, ml_builds, pages, lint, commit)"
