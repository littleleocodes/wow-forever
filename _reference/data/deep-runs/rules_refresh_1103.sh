#!/usr/bin/env bash
# 2026-11-06, part B of the rules repair (rules_repair_1103.sh is part A; search-improvements.md 0e). For every rotation whose rule
# file part A replaced (a line "wrote <class>-<rotation>.json" in lane-r.log), the numbers made under the old rules are measured
# again, as on 2026-10-15 (page-audit.md B24): the open record taken back to the end of the level-60 search (refresh_keys.py), a plain
# fl_open_search.py run for that rotation (20-60 race, polish, orders, values, certificate, signature check), then the class's open
# builds, orders, races and reports. Order: waits for part A's last tune; rogue, mage, warrior; then waits for lane C's race-warlock
# and does the warlock: the Demonology rotation when its rules changed, and the Destruction rules once more on that search's result
# (its rules were replaced by hand before its search, after six rounds of a from-scratch tune), with its record when they change.
# A record is only touched while no fl_open_search.py of that class and record runs (the classes here are done; the warlock block
# starts after race-warlock, and the one-tree lane writes other records). The paladin needs no part B: its search has not run.
# The file name ends in _1103.sh on purpose (rebalance.ps1). Log: deep-runs/lane-r.log and patch-1103.log.
# Resume: the same command (markers deep-runs/p1103/refresh2-*).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/p1103
LOG=$L/patch-1103.log
FL=_reference/data/fightlab
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-8}"
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {   # run <marker> <log> <command...>: skipped when the marker exists; the marker is written on rc=0; returns rc
  local mk=$1 lg=$2; shift 2
  if [ -e "$M/$mk" ]; then return 0; fi
  "$@" >> "$L/$lg" 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
installed() { grep -q "wrote $1-$2.json" $L/lane-r.log; }   # installed <class> <rotation>: part A (or this script) replaced the file
after() {   # after <class>: the class's open builds, orders, races and reports again
  run refresh2-builds-$1 lane-r.log python -u _reference/data/open_builds.py $1 --write --only leveling || return 1
  run refresh2-orders-$1 lane-r.log python -u _reference/data/order_repair.py $1 --jobs 4 --write
  run refresh2-race-$1 lane-r.log python -u _reference/data/rebuild.py $1 --steps race,report
}
until [ -e "$M/rules2-warlock-demonology-leveling" ]; do sleep 120; done
say "start rules refresh (the records of the rotations whose rules changed)"
if installed rogue subtlety-leveling; then
  run refresh2-keys-rogue lane-r.log python -u $L/refresh_keys.py rogue.json subtlety-leveling &&
  run refresh2-keys-rogue-pure lane-r.log python -u $L/refresh_keys.py pure/rogue-subtlety.json subtlety-leveling &&
  run refresh2-open-rogue lane-r.log python -u $FL/fl_open_search.py rogue --rotation subtlety-leveling --jobs 4 &&
  run refresh2-open-rogue-pure lane-r.log python -u $FL/fl_open_search.py rogue --tree Subtlety --rotation subtlety-leveling --jobs 4 &&
  after rogue
fi
MAGE=""
installed mage arcane-leveling && MAGE="$MAGE arcane-leveling"
installed mage barrage-frost-leveling && MAGE="$MAGE barrage-frost-leveling"
if [ -n "$MAGE" ]; then
  ARGS=""; for r in $MAGE; do ARGS="$ARGS --rotation $r"; done
  run refresh2-keys-mage lane-r.log python -u $L/refresh_keys.py mage.json $MAGE &&
  run refresh2-open-mage lane-r.log python -u $FL/fl_open_search.py mage $ARGS --jobs 4 &&
  after mage
fi
if installed warrior prot-leveling; then
  run refresh2-keys-warrior lane-r.log python -u $L/refresh_keys.py warrior.json prot-leveling &&
  run refresh2-open-warrior lane-r.log python -u $FL/fl_open_search.py warrior --rotation prot-leveling --jobs 4 &&
  after warrior
fi
say "rules refresh: rogue, mage and warrior done; the warlock waits for race-warlock"
until [ -e "$M/race-warlock" ]; do sleep 120; done
run rules2-warlock-destruction-leveling lane-r.log python -u $FL/rules_retune.py warlock destruction-leveling destruction-open-leveling --jobs 4
# All three warlock rotations, whatever their rules did: the 20-60 race takes the previous record's winner and our raced builds as
# finalists only since 2026-11-06 08:11 (fl_open_search.py), and lane C's warlock process loaded the code before that. Affliction's
# fresh winner 38/11/2 ran 36.78 s in its race against 36.20 for affliction-open-leveling, the winner it replaced, and lane C's
# builds step rewrites that build from the slower record; the Demonology rotation's previous winner (a hybrid) was not raced at all.
WL="affliction-leveling demonology-leveling destruction-leveling"
if [ -n "$WL" ]; then
  ARGS=""; for r in $WL; do ARGS="$ARGS --rotation $r"; done
  run refresh2-keys-warlock lane-r.log python -u $L/refresh_keys.py warlock.json $WL &&
  run refresh2-open-warlock lane-r.log python -u $FL/fl_open_search.py warlock $ARGS --jobs 4 &&
  after warlock
fi
say "rules refresh done"
