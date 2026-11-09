#!/usr/bin/env bash
# 2026-11-06 18:25: the mage block of fixes_1103.sh once more, and the rogue's after-steps once more. Two copies of the retired part B
# (rules_refresh_1103.sh) had survived their TaskStop (a stopped task leaves the lane's bash alive: memory note of 2026-11-04, not
# applied), woke at 15:37 on the Demonology marker, redid the rogue's Subtlety records after the fixes lane's own rogue block, then both
# wrote mage.json at once from 17:16 and stripped its Arcane and Arcane-Frost rotations before the fixes lane's keys step (fix-keys-mage
# rc=1 at 18:15). Killed 18:17; mage.json restored from refresh-backups/mage.pre-refresh.json (17:16, every rotation done); the
# two-writer file kept as refresh-backups/mage.two-writers-1816.json. Same markers as fixes_1103.sh, so a later run of it skips all this.
# The name ends in _1103.sh on purpose (rebalance.ps1). Log: deep-runs/lane-f.log and patch-1103.log.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/p1103
LOG=$L/patch-1103.log
D=_reference/data
FL=$D/fightlab
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-8}"
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> "$L/lane-f.log"
  "$@" >> "$L/lane-f.log" 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
redo() {
  local mk=$1 c=$2 rec=$3; shift 3
  local tree=()
  if [ "$1" = "--tree" ]; then tree=(--tree "$2"); shift 2; fi
  local args=(); local r; for r in "$@"; do args+=(--rotation "$r"); done
  run fix-keys-$mk python -u $L/refresh_keys.py $rec "$@" &&
  run fix-open-$mk python -u $FL/fl_open_search.py $c "${tree[@]}" "${args[@]}" --jobs 4
}
after() {
  run fix-cross-$1 python -u $FL/fl_synergy.py $1 --jobs 4
  run fix-builds-$1 python -u $D/open_builds.py $1 --write --only leveling || return 1
  run fix-orders-$1 python -u $D/order_repair.py $1 --jobs 4 --write
  run fix-race-$1 python -u $D/rebuild.py $1 --steps race,report
  say "fixes: class $1 done"
}
say "start fixes (mage block again after the retired part B interfered; the rogue after-steps again)"
rm -f $M/fix-cross-rogue $M/fix-builds-rogue $M/fix-orders-rogue $M/fix-race-rogue
after rogue
redo mage mage mage.json fire-leveling arcane-leveling barrage-frost-leveling &&
after mage
say "fixes (mage block, rogue after-steps) done"
