#!/usr/bin/env bash
# 2026-11-03: every one-tree leveling record (fightlab/open/pure/, fl_open_search.py --tree) dates from 2026-10-25/26, before the 10-30
# hotfixes and the 11-02 patch; open_builds.py now skips such records (it had written the shaman's pure Elemental build with Lava Burst).
# The pure pages whose rotation a hybrid wins need the one-tree search again on the new data: hunter Beast Mastery and Survival, rogue
# Assassination (Subtlety: subtlety_dm.sh), warlock Demonology and Destruction (shaman Elemental: shaman_ele.sh). Each class waits for its
# open search in patch_1103.sh, then its one-tree searches, the builds and the class's races again.
# Resume: the same command (markers deep-runs/p1103/pure-*).
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
pure() {   # pure <class> <wait marker> <tree:rotation>...
  local c=$1 w=$2; shift 2
  until [ -e "$M/$w" ]; do sleep 120; done
  for tr in "$@"; do
    local t=${tr%%:*} r=${tr#*:} k=pure-$c-${tr%%:*}
    k=${k// /_}
    run $k pure.log python -u $FL/fl_open_search.py $c --tree "$t" --rotation $r $(fresh $k) --jobs 3
  done
  run pure-builds-$c pure.log python -u _reference/data/open_builds.py $c --write --only leveling
  run pure-validate-$c pure.log python -u _reference/data/validate_builds.py
  run pure-race-$c pure.log python -u _reference/data/rebuild.py $c --steps race,report
  say "pure $c done"
}
pure hunter race-hunter "Beast Mastery:bm-leveling" "Survival:melee-dps"
pure rogue race-rogue "Assassination:combat-daggers-raid"
pure warlock race-warlock "Demonology:demonology-leveling" "Destruction:destruction-leveling"
say "pure searches done"
