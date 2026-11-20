#!/usr/bin/env bash
# destro_prep_1120.sh (2026-11-20, the audit's decisions on Soul Shards: (a) every warlock entry carries 32, (c) fresh tunes of the
# three old Destruction entries before the ML Destruction search): the step-2 race of affliction-raid with shards (D1 re-run), the
# three fresh raid tunes, then marker b1120/destro-ready for audit_raid_1120b.sh; after audit_raid_1120.sh is done (ML Affliction),
# the two Affliction entries get their shards. BelowNormal on 10 of 12. Log deep-runs/destro-prep-1120.log, markers deep-runs/dp1120/.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/dp1120
LOG=$L/destro-prep-1120.log
OUT=$L/destro-prep-1120-out.log
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
run race-aff-shards python -u $L/warlock_upstream_race.py affliction-raid --shards 32 --out $R/warlock-upstream-race-shards.json || say "WARNING: race affliction-raid"
for e in sb-raid incinerate-raid fire-destro-raid; do
  run tune-$e python -u $R/apl_opt.py warlock --spec $e --setting raid --fresh --write || say "WARNING: tune $e"
done
touch $L/b1120/destro-ready
say "destro-ready touched"
if ! grep -q "all done" $L/audit-raid-1120.log 2>/dev/null; then
  say "waiting for audit_raid_1120.sh (ML Affliction, Demonology) before the Affliction entries take their shards"
  until grep -q "all done" $L/audit-raid-1120.log 2>/dev/null; do sleep 60; done
fi
run shards-affliction python -u $L/add_shards_1120.py affliction-raid affliction-wrack-raid || say "WARNING: shards affliction"
say "all done"
