#!/usr/bin/env bash
# 2026-11-03: patch_1103.sh's shaman lane ran the fresh open search, whose Elemental-rotation winner is a hybrid (26/22/3); open_builds
# then took the pure Elemental page build from open/pure/shaman-elemental.json, a record of 2026-10-26 (pre-patch trees: Lava Burst,
# old tier gating) and wrote an illegal build (restored to the repaired one by hand). This is the fresh one-tree search on the new trees,
# then the builds and the shaman's races again. Resume: the same command (markers deep-runs/p1103/ele-*).
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
run ele-pure elemental.log python -u $FL/fl_open_search.py shaman --tree Elemental --rotation elemental-dps $(fresh ele-pure) --jobs 3
run ele-builds elemental.log python -u _reference/data/open_builds.py shaman --write --only leveling
run ele-validate elemental.log python -u _reference/data/validate_builds.py
run ele-race elemental.log python -u _reference/data/rebuild.py shaman --steps race,report
say "pure elemental done"
