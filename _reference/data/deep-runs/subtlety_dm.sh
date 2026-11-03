#!/usr/bin/env bash
# 2026-11-03 (user: "Why wouldn't we make death mark require spell for subtlety if every other spec and class have to use their signature
# spell?"): Death Mark joins Hemorrhage as Subtlety's required leveling spell (signature_spells.json; raid once the simulator ports the
# rogue's tree). The rogue's open search runs in patch_1103.sh's lane A; when its winner for the Subtlety rotation is a hybrid, the pure
# Subtlety page needs the one-tree search (fl_open_search --tree, record open/pure/rogue-subtlety.json), then the builds and races again.
# Waits for lane A's open-rogue marker. Resume: the same command (markers deep-runs/p1103/sub-*).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/p1103
LOG=$L/patch-1103.log
FL=_reference/data/fightlab
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {
  local mk=$1 lg=$2; shift 2
  if [ -e "$M/$mk" ]; then return 0; fi
  "$@" >> "$L/$lg" 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return 0
}
fresh() { if [ -e "$M/$1.started" ]; then echo ""; else touch "$M/$1.started"; echo "--fresh"; fi; }
until [ -e "$M/race-rogue" ]; do sleep 120; done
run sub-pure subtlety.log python -u $FL/fl_open_search.py rogue --tree Subtlety --rotation subtlety-leveling $(fresh sub-pure) --jobs 4
run sub-builds subtlety.log python -u _reference/data/open_builds.py rogue --write --only leveling
run sub-race subtlety.log python -u _reference/data/rebuild.py rogue --steps race,report
say "subtlety death mark done"
