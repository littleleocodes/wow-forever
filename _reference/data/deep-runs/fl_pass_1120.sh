#!/usr/bin/env bash
# fl_pass_1120.sh (2026-11-20, the independent audit's step 6; user: "continue to make the changes and communicate with the audit session
# to implement the fixes and changes that the audit suggests"). The fight lab against the official simulator, as one pass (committed
# before this starts; every change has a knob in tables.py or its class module, "lab before" values in the commit): the 80% refund of an
# avoided ability (D10), trainer ranks only (H18), base health and attributes by level and the first 20 Stamina and Intellect (H17, with
# in-game evidence), rage from damage taken (H16), Overpower and Counterattack unavoidable, Vindication's 5 procs a minute (H9), Torment,
# the Voidwalker and Bane of Agony (H20), Garrote, Eviscerate, Death Mark and poisons (H13), the quiver and Serpent Sting (H14), Spirit
# Tap with Meditation (H22), Lightning Shield (H19), and the mage's Fingers of Frost, Arcane talents, Ice Barrier, shared cooldown,
# Shatter on missiles and Winter's Chill (H21). What depends on the lab is made again, from scratch:
#   1. rules_retune.py for every rules file on its page pick (from scratch and continued; installed only 0.3% ahead);
#   2. each class's open records from the 20-60 race on (refresh_keys.py, fl_open_search.py), one-tree records included;
#   3. open builds, orders, races and reports;
#   then the healer and tank leveling paths, the own-rotation race, the filler passes, validate, the by-level guides measured, GearCheck's
#   leveling values (standard gear, the Forever base, best gear), the healer values, the add-on file and the rest cues; after Claude has
#   checked the texts (marker fp1120/texts-done): pages, guide checks, page audit.
# The hunter waits for the audit session's decision on the pet swing rule (H15; marker fp1120/h15-decided).
# Starts after Claude's commit of the pass (marker fp1120/start). Full power: BelowNormal on 10 of 12 (RESERVE_CPUS=2).
# Log deep-runs/pass-1120.log (steps), pass-<lane>.log (output); markers deep-runs/fp1120/. Resume: the same command. Stop:
# Stop-Process the bash processes running this script (parent and lane subshells) and their python children (never TaskStop).
#   bash _reference/data/deep-runs/fl_pass_1120.sh
cd F:/wow-forever || exit 1
export PATH="/usr/bin:/bin:$PATH"   # 2026-11-21: a non-login bash started from Windows had no date, tr, touch or sleep (empty markers)
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/fp1120
LOG=$L/pass-1120.log
FL=_reference/data/fightlab
D=_reference/data
mkdir -p $M/pre
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-2}" -Priority "${PRIORITY:-BelowNormal}" >> $LOG 2>&1
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
tune() {      # tune <lane log> <class> <rotation> <page pick>: from scratch and continued
  [ -e $M/pre/$2-$3.json ] || cp $FL/rotations/$2-$3.json $M/pre/
  run tune-$2-$3 $1 python -u $FL/rules_retune.py $2 $3 $4 --jobs 3 || say "WARNING: rules_retune $2 $3 failed; its saved rules stay"
}
refresh() {   # refresh <lane log> <class> <rotations...>: the class record from the 20-60 race on
  local lg=$1 c=$2; shift 2
  run keys-$c $lg python -u $L/refresh_keys.py $c.json "$@" || { say "WARNING: refresh_keys $c failed"; return 1; }
  for r in "$@"; do run open-$c-$r $lg python -u $FL/fl_open_search.py $c --rotation $r --jobs 3 || say "WARNING: open $c $r failed"; done
}
refresh_pure() {   # refresh_pure <lane log> <class> <tree> <tree slug> <rotation>: a one-tree record from the 20-60 race on
  local lg=$1 c=$2 tree=$3 slug=$4 r=$5
  [ -e $FL/open/pure/$c-$slug.json ] || { say "no one-tree record $c-$slug: skipped"; return 0; }
  run keys-$c-$slug $lg python -u $L/refresh_keys.py pure/$c-$slug.json $r || { say "WARNING: refresh_keys pure $c-$slug failed"; return 1; }
  run open-$c-$slug $lg python -u $FL/fl_open_search.py $c --tree "$tree" --rotation $r --jobs 3 || say "WARNING: open $c $slug failed"
}
finish() {    # finish <lane log> <class>: open builds, orders, races and reports
  run builds-$2 $1 python -u $D/open_builds.py $2 --write --only leveling || say "WARNING: open_builds $2 failed"
  run orders-$2 $1 python -u $D/order_repair.py $2 --jobs 3 --write || say "WARNING: order_repair $2 failed"
  run race-$2 $1 python -u $D/rebuild.py $2 --steps race,report || say "WARNING: race $2 failed"
  say "class $2 done"
}

mage() { local lg=pass-a.log
  tune $lg mage frost-leveling frost-open-leveling
  tune $lg mage barrage-frost-leveling arcane-frost-open-leveling
  tune $lg mage arcane-leveling arcane-open-leveling
  tune $lg mage fire-leveling fire-open-leveling
  tune $lg mage frostfire-leveling frostfire-open-leveling
  refresh $lg mage arcane-leveling fire-leveling frost-leveling barrage-frost-leveling frostfire-leveling
  finish $lg mage; }
druid() { local lg=pass-a.log
  tune $lg druid feral-cat-dps feral-combat-open-leveling
  tune $lg druid balance-dps opt-balance-dps-leveling-st
  refresh $lg druid feral-cat-dps balance-dps
  finish $lg druid; }
rogue() { local lg=pass-a.log
  tune $lg rogue combat-swords-raid combat-open-leveling
  tune $lg rogue combat-daggers-raid assassination-open-leveling
  tune $lg rogue subtlety-leveling subtlety-open-leveling
  refresh $lg rogue combat-swords-raid combat-daggers-raid subtlety-leveling
  refresh_pure $lg rogue Assassination assassination combat-daggers-raid
  refresh_pure $lg rogue Subtlety subtlety subtlety-leveling
  finish $lg rogue; }
warrior() { local lg=pass-b.log
  tune $lg warrior arms-2h-raid arms-open-leveling
  tune $lg warrior fury-dw-raid fury-open-leveling
  tune $lg warrior prot-leveling protection-leveling
  refresh $lg warrior arms-2h-raid fury-dw-raid prot-leveling
  finish $lg warrior; }
warlock() { local lg=pass-b.log
  tune $lg warlock affliction-leveling affliction-open-leveling
  tune $lg warlock demonology-leveling demonology-open-leveling
  tune $lg warlock destruction-leveling destruction-open-leveling
  refresh $lg warlock affliction-leveling demonology-leveling destruction-leveling
  refresh_pure $lg warlock Demonology demonology demonology-leveling
  refresh_pure $lg warlock Destruction destruction destruction-leveling
  finish $lg warlock; }
hunter() { local lg=pass-b.log
  if [ ! -e $M/h15-decided ]; then
    say "hunter waits for the pet swing decision (marker fp1120/h15-decided)"
    until [ -e $M/h15-decided ]; do sleep 60; done
  fi
  tune $lg hunter bm-leveling beast-mastery-open-leveling
  tune $lg hunter mm-raid marksmanship-open-leveling
  tune $lg hunter melee-dps survival-open-leveling
  refresh $lg hunter bm-leveling mm-raid melee-dps
  refresh_pure $lg hunter "Beast Mastery" beast-mastery bm-leveling
  refresh_pure $lg hunter Survival survival melee-dps
  finish $lg hunter; }
paladin() { local lg=pass-c.log
  tune $lg paladin ret-dps leveling-retribution
  tune $lg paladin holy-leveling holy-leveling
  tune $lg paladin prot-leveling protection-leveling
  refresh $lg paladin holy-leveling prot-leveling ret-dps
  finish $lg paladin; }
priest() { local lg=pass-c.log
  tune $lg priest shadow-dps shadow-open-leveling
  tune $lg priest holy-leveling smite-open-leveling
  tune $lg priest discipline-leveling discipline-leveling
  refresh $lg priest discipline-leveling holy-leveling shadow-dps
  finish $lg priest; }
shaman() { local lg=pass-c.log
  tune $lg shaman enhancement-dps enhancement-open-leveling
  tune $lg shaman elemental-dps elemental-open-leveling
  refresh $lg shaman elemental-dps enhancement-dps
  refresh_pure $lg shaman Elemental elemental elemental-dps
  finish $lg shaman; }

if [ ! -e $M/start ]; then
  say "waiting for Claude to commit the pass (marker fp1120/start)"
  until [ -e $M/start ]; do sleep 60; done
fi
say "fl_pass_1120 start"
( mage; druid; rogue; say "lane A done" ) &
( warrior; warlock; hunter; say "lane B done" ) &
( paladin; priest; shaman; say "lane C done" ) &
wait
say "lanes done; rules the tunes changed: $(for f in $M/pre/*.json; do cmp -s $f $FL/rotations/$(basename $f) || printf '%s ' $(basename $f .json); done)"

ALL="druid hunter mage paladin priest rogue shaman warlock warrior"
run lev-path tail.log python -u $D/raid_path_leveling.py paladin shaman priest druid warrior --write || say "WARNING: raid_path_leveling failed"
run own-rotation tail.log python -u $FL/own_rotation_race.py --jobs 10 || say "WARNING: own_rotation_race failed"
for spec in "druid|Balance" "druid|Feral Combat" "hunter|Beast Mastery" "hunter|Marksmanship" "hunter|Survival" "hunter|Hybrid Beast Mastery/Survival" \
            "mage|Arcane" "mage|Fire" "mage|Frost" "mage|Hybrid Arcane/Frost" "mage|Hybrid Fire/Frost" "paladin|Retribution" \
            "paladin|Hybrid Holy/Retribution" "paladin|Hybrid Protection/Retribution" "priest|Shadow" "priest|Hybrid Discipline/Holy" \
            "rogue|Assassination" "rogue|Combat" "rogue|Subtlety" "rogue|Hybrid Combat/Subtlety" "shaman|Elemental" "shaman|Enhancement" \
            "warlock|Affliction" "warlock|Demonology" "warlock|Destruction" "warrior|Arms" "warrior|Fury"; do
  c=${spec%%|*}; s=${spec#*|}; slug=$(echo "$s" | tr 'A-Z' 'a-z' | tr '/ ' '--')
  run filler-$c-$slug tail.log python -u $FL/fl_filler_pass.py $c --spec "$s" --write --jobs 10 || say "WARNING: filler pass $c $s failed"
done
run validate tail.log python -u $D/validate_builds.py || { say "STOP: validate_builds failed (tail.log)"; exit 1; }
run measure tail.log python -u $D/level_guides.py $ALL --measure --jobs 10 || say "WARNING: level_guides --measure failed"
for c in $ALL; do   # every page pick of the class (stat_weights_all.py redoes only missing or stale files)
  specs=$(python -c "
import importlib.util, sys
sys.path[:0] = ['_reference/data', '_reference/data/fightlab', '_reference/data/scorer']
spec = importlib.util.spec_from_file_location('sa', '_reference/data/fightlab/signature_audit.py'); SA = importlib.util.module_from_spec(spec); spec.loader.exec_module(SA)
print('|'.join(s[0] for s in SA.page_slots(sys.argv[1], signature=True) if s[1]))" $c)
  IFS='|' read -r -a S <<< "$specs"
  run aside-std-$c gear-pass.log python -u $L/weights_aside_1116.py leveling $c "${S[@]}" || say "WARNING: weights aside (standard) $c failed"
  run aside-best-$c gear-pass.log python -u $L/weights_aside_1116.py leveling-best $c "${S[@]}" || say "WARNING: weights aside (best) $c failed"
done
run weights-std gear-pass.log python -u $D/characters/stat_weights_all.py $ALL --jobs 10 || say "WARNING: stat weights (standard) failed"
run base gear-pass.log python -u $D/characters/forever_base.py $ALL --jobs 10 || say "WARNING: forever_base failed"
run weights-best gear-pass.log python -u $D/characters/stat_weights_all.py $ALL --base best --jobs 10 || say "WARNING: stat weights (best) failed"
run heal-values gear-pass.log python -u $D/heallab/heal_values.py --jobs 4 || say "WARNING: heal_values failed"
run addon-values gear-pass.log python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"
say "numbers done: Claude checks the texts (leveling-steps.json, level-guides, guides) and touches fp1120/texts-done"
until [ -e $M/texts-done ]; do sleep 60; done
run regen tail.log python -u $D/rebuild.py --steps regen || say "WARNING: regen failed"
run guide-check tail.log python -u $D/level_guides.py --check || say "WARNING: by-level guide check lists problems (tail.log)"
run guides tail.log python -u $D/guides.py --check --write || say "WARNING: guides --check lists passages to rewrite (tail.log)"
run page-lint tail.log python -u $D/page_lint.py --write || say "WARNING: page_lint lists findings (_reference/page-lint.md)"
say "all done (review, commit, push; message the Addons session: the leveling values and rest cues; the audit session: the pass)"
