#!/usr/bin/env bash
# tonight_1111.sh   (2026-11-11, the second night of the client 70862 update; user: "Set it up to run tonight. I'll give you the signal to
# start the runs again like I did last night": started only when the user says so). Log deep-runs/tonight-1111.log; markers deep-runs/r1111/
# (and each raid lane's own r1103/rest-<class>-*); resume = the same command. Full power: balance_1111.ps1 -Run 12 -Bench 12 next to it (no
# fight-lab work tonight: every core goes to the simulator).
#
# Why: last night (tonight_1110.sh, 55d9f0c9) re-pinned the simulator to ff9babba5, re-made every gear set and raced every entry, but the
# ML final steps (the pre-BiS and BiS tier sets and the talent searches in them: dps-rankings.md, the pages' tier lines) ran only for the
# mage, shaman and Feral. The other six classes' tier numbers still come from records made on 16e8542 in the sets before the gear repair.
#
# Stages, each resumable by its markers:
#  0. the checkout check: wowsims-forever-y at ff9babba5 (last night's pin; no re-pin tonight, so the numbers compare);
#  1. the tank gear rule (tank_gear.py: a BiS search that ends below the pre-BiS set keeps the pre-BiS set; the paladin's BiS had read
#     1.1836 against 1.1917): the BiS tier again for paladin and druid, then Tara's tank weights;
#  2. three raid lanes at once, each raid_rest_1103.sh per class (the gear repair is done, so it skips; every entry raced, ml_clear and the
#     ML final step of each named spec, the ML builds, validate, the entries raced again, tidy, unused abilities):
#       A: hunter (4 specs), paladin (1)    B: rogue (4), priest (2)    C: warlock (4), warrior (2)
#  3. the character planner: both characters' pages (no refresh baseline written);
#  4. wrap: validate, rankings and gear links, pages, guide check, page audit, a checkpoint commit (pushed after Claude's review).
# ETA: about 69 min per spec (the Feral final step last night next to another lane), 5-6 specs a lane: 7-9 hours.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/r1111
LOG=$L/tonight-1111.log
R=_reference/data/raidsim
D=_reference/data
Y="$HOME/.wow-forever-tools/wowsims-forever-y"
PIN=ff9babba5
mkdir -p $M
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {   # run <marker> <log> <command...>: skipped when the marker exists; the marker is written on rc=0; returns rc
  local mk=$1 lg=$2; shift 2
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> "$L/$lg"
  "$@" >> "$L/$lg" 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
say "tonight 1111 start (second night of the client 70862 update: the ML final steps of hunter, paladin, rogue, priest, warlock, warrior)"

# ---- 0. the checkout
head=$(git -C "$Y" rev-parse --short=9 HEAD)
[ "$head" = "$PIN" ] || { say "STOP: $(basename "$Y") is at $head, not $PIN"; exit 1; }
export WOW_FOREVER_SIM="$Y"
export LANE_PIN=$PIN

# ---- 1. the tank gear rule, then Tara's tank weights
run tank-bis tank.log python -u $R/tank_gear.py paladin druid --tiers bis || { say "STOP: tank_gear.py failed (tank.log)"; exit 1; }
run tank-weights tank.log python -u $D/characters/tank_weights.py paladin prot-tank protection-ml-tank Protection

# ---- 2. three raid lanes
lane() {   # lane <name> <class> <specs...> ; <class> <specs...> separated by "--"
  local name=$1; shift
  local args=()
  for x in "$@" --; do
    if [ "$x" = "--" ]; then
      if [ ${#args[@]} -gt 0 ]; then
        local c=${args[0]}
        [ -e $M/lane-$c ] || { bash $L/raid_rest_1103.sh "${args[@]}" > $L/raid-$c.console 2>&1 && touch $M/lane-$c; }
        [ -e $M/lane-$c ] && say "lane $name: $c done" || say "WARNING: lane $name: $c did not finish (patch-1103.log, raid-$c.log)"
      fi
      args=()
    else
      args+=("$x")
    fi
  done
}
lane A hunter "Beast Mastery" "Hybrid Beast Mastery/Marksmanship" "Marksmanship" "Survival" -- paladin "Retribution" & PA=$!
lane B rogue "Assassination" "Combat" "Hybrid Assassination/Combat" "Subtlety" -- priest "Shadow" "Hybrid Discipline/Holy" & PB=$!
lane C warlock "Affliction" "Demonology" "Destruction" "Hybrid Affliction/Destruction" -- warrior "Arms" "Fury" & PC=$!
wait $PA $PB $PC
say "raid lanes done"

# ---- 3. the character planner
run plan-tara planner.log python -u $D/characters/plan.py tara --no-refresh
run plan-arcea planner.log python -u $D/characters/plan.py arcea --no-refresh

# ---- 4. wrap
run wrap-validate wrap.log python -u $D/validate_builds.py
run wrap-rank wrap.log python -u $R/ml_builds.py --rank
run wrap-regen wrap.log python -u $D/rebuild.py --steps regen
run wrap-guides wrap.log python -u $D/guides.py --check --write
run wrap-lint wrap.log python -u $D/page_lint.py --write
git -c core.safecrlf=false add -A
git -c core.safecrlf=false commit -q -F - <<EOF
Checkpoint $(date +%F_%H:%M): the client 70862 update, second night (tonight_1111.sh): the ML final steps of hunter, paladin, rogue, priest, warlock and warrior on ff9babba5 in the repaired sets; the tank BiS rule (paladin, druid)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF
say "all done (committed $(git rev-parse --short HEAD))"
