#!/usr/bin/env bash
# warlock_raid_1119.sh (2026-11-19, audit step 2): the official simulator's warlock rotations against ours in every arm
# (warlock_upstream_race.py). BelowNormal on 10 of 12. Log deep-runs/warlock-raid-1119.log, markers deep-runs/w1119/.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/w1119
LOG=$L/warlock-raid-1119.log
OUT=$L/warlock-raid-1119-out.log
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
run upstream-race python -u $L/warlock_upstream_race.py || { say "STOP: the upstream race"; exit 1; }
say "all done (Claude: read raidsim/warlock-upstream-race.json, adopt, tune)"
