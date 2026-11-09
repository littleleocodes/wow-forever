#!/usr/bin/env bash
# paladin_vind_1109.sh (2026-11-09; user 2026-11-08: "Self audit, self audit, self audit"; page-audit-1108 S14): the fight lab modelled
# no part of Vindication (the target's attack power cut; hotfix 113554 dropped the paladin's own gain), so the leveling filler pass
# wanted its points in Improved Seals. Modelled the same night (fightlab/paladin.py _vind_reduction, tables.VINDICATION_SCALE "mob"):
# the Retribution page build 27.36 -> 27.00 s weighted (20-60), 32.30 -> 31.42 s at 60. A mechanics change: the paladin's leveling rules
# from scratch, the open search fresh (every paladin rotation: the search had valued Vindication at 0), builds, orders, races, the
# raid-path orders, own-rotation races, the guide's timings, then the Retribution filler pass as a dry run for review.
# The holy-leveling and prot-leveling rules stay: their page builds hold no Vindication (bit-identical fights).
# Waits for the healer filler passes (no heallab/filler_pass.py process left). Resume: the same command (markers deep-runs/p1109/).
# Stop: Stop-Process this bash and its python children (TaskStop never kills a lane).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/p1109
LOG=$L/patch-1103.log
LG=lane-vind.log
FL=_reference/data/fightlab
D=_reference/data
J=6
mkdir -p $M
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> "$L/$LG"
  "$@" >> "$L/$LG" 2>&1; local rc=$?
  say "vind $mk rc=$rc"
  if [ $rc -ne 0 ]; then say "paladin Vindication lane STOP at $mk"; exit 1; fi
  touch "$M/$mk"
}
fresh() { if [ -e "$M/$1.started" ]; then echo ""; else touch "$M/$1.started"; echo "--fresh"; fi; }

while powershell -NoProfile -Command "if (Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | Where-Object { \$_.CommandLine -like '*filler_pass.py*' }) { exit 0 } else { exit 1 }"; do sleep 120; done
say "paladin Vindication lane start ($J workers)"
run v-rules python -u $FL/rotation_opt.py paladin --fresh --write --jobs $J
run v-open python -u $FL/fl_open_search.py paladin $(fresh v-open) --jobs $J
run v-builds python -u $D/open_builds.py paladin --write --only leveling
run v-orders python -u $D/order_repair.py paladin --jobs $J --write
run v-race python -u $D/rebuild.py paladin --steps race,report
run v-lev-path python -u $D/raid_path_leveling.py paladin --jobs $J --write
run v-own python -u $FL/own_rotation_race.py paladin --jobs $J
run v-validate python -u $D/validate_builds.py
run v-measure python -u $D/level_guides.py paladin --measure --jobs $J
run v-filler python -u $FL/fl_filler_pass.py paladin --spec Retribution --fights 1500 --jobs $J
touch "$M/vind-done"
say "paladin Vindication lane done"
