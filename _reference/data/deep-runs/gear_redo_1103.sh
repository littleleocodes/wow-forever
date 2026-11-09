#!/usr/bin/env bash
# gear_redo_1103.sh   (2026-11-06, the gear repair: page-audit.md J1-J4; user: "Go with your recs").
# The classes whose raid half ran before the gear repair, or that have no lane in the 2026-11-02 patch queue, one after the other:
#   hunter, mage, paladin: their lanes again. Each lane starts with gear_repair_1103.sh, which re-makes the class's sets and removes
#     the lane's markers, so the lane redoes its races, re-tunes, searches and ML final steps in the new sets.
#   priest, druid: raid_rest_1103.sh (gear repair, races, the priest's two ML final steps, builds).
# Called at the end of raid_rogue_1103.sh, the last lane of resume_1104.sh, so the runner's wrap (rankings, gear links, pages, the
# checkpoint commit) comes after it. Resume: the same command; every lane resumes from its own markers.
cd F:/wow-forever || exit 1
L=_reference/data/deep-runs
M=$L/r1103
LOG=$L/patch-1103.log
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
if [ -e "$M/gear-redo-done" ]; then exit 0; fi
say "raid: gear redo start (hunter, mage, paladin lanes again; priest and druid)"
bash $L/raid_hunter_1103.sh > $L/raid-hunter.console 2>&1
bash $L/raid_mage_1103.sh > $L/raid-mage.console 2>&1
bash $L/raid_paladin_1103.sh > $L/raid-paladin.console 2>&1
bash $L/raid_rest_1103.sh priest "Shadow" "Hybrid Discipline/Holy" > $L/raid-priest.console 2>&1
bash $L/raid_rest_1103.sh druid > $L/raid-druid.console 2>&1
touch "$M/gear-redo-done"
say "raid: gear redo done"
