#!/usr/bin/env bash
# 2026-11-03 (user: "New patch came out ... We need to do more runs again"; then "Stop them and go ahead, wait for the sim to merge"):
# Blizzard's development notes of 2026-11-02 (client 1.60.1.70753) and the hunter hotfix of 2026-11-03 change every class but the
# priest. Our talent and spell data were refreshed from talentsforever.com's 2026-11-03 export (raw/2026-11-03-live-70753), the builds
# the new trees broke repaired (repair_builds.py), and the fight-lab and healer-lab class modules ported. The raid simulator has not
# merged the patch yet (wowsims/forever drafts #821 shaman, #823 druid, #824 hunter, a rogue and a warlock branch): the raid half waits.
# This queue is the leveling half for the eight changed classes, three lanes of fight-lab work at --jobs 4 each, per class:
# rotation rules from scratch (after a mechanics change, CLAUDE.md), the fresh open leveling search (warm start: the old winners seed it,
# starts the new trees forbid are skipped), the open builds, orders for the builds the repair left without one, races and reports.
# Then the healer and tank specs' leveling paths, the own-rotation race, validate, pages, guide check.
# Resume: the same command (markers deep-runs/p1103/<step>); a finished step is skipped.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/p1103
mkdir -p $M
LOG=$L/patch-1103.log
FL=_reference/data/fightlab
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {   # run <marker> <log> <command...>: skipped when the marker exists; the marker is written on rc=0
  local mk=${1////_} lg=$2; shift 2
  if [ -e "$M/$mk" ]; then return 0; fi
  "$@" >> "$L/$lg" 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return 0
}
fresh() { if [ -e "$M/$1.started" ]; then echo ""; else touch "$M/$1.started"; echo "--fresh"; fi; }
cls_steps() {   # cls_steps <class> <lane log>
  local c=$1 lg=$2
  run rules-$c $lg python -u $FL/rotation_opt.py $c --fresh --write
  run open-$c $lg python -u $FL/fl_open_search.py $c $(fresh open-$c) --jobs 4
  run builds-$c $lg python -u _reference/data/open_builds.py $c --write --only leveling
  run orders-$c $lg python -u _reference/data/order_repair.py $c --jobs 4 --write
  run race-$c $lg python -u _reference/data/rebuild.py $c --steps race,report
  say "class $c done"
}
lane_a() { for c in rogue warrior druid; do cls_steps $c lane-a.log; done; say "lane A done"; }
lane_b() { for c in shaman mage; do cls_steps $c lane-b.log; done; say "lane B done"; }
lane_c() { for c in hunter warlock paladin; do cls_steps $c lane-c.log; done; say "lane C done"; }

say "start (leveling half of the 2026-11-02 patch: rogue warrior druid | shaman mage | hunter warlock paladin)"
lane_a & lane_b & lane_c &
wait
say "lanes done"
run lev-path tail.log python -u _reference/data/raid_path_leveling.py druid paladin shaman warrior priest --write
run own-rotation tail.log python -u $FL/own_rotation_race.py --jobs 10
run validate tail.log python -u _reference/data/validate_builds.py
run regen tail.log python -u _reference/data/rebuild.py --steps regen
run guides tail.log python -u _reference/data/guides.py --check --write   # lists the guide passages to rewrite by hand
say "all done"
