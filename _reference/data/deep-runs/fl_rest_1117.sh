#!/usr/bin/env bash
# fl_rest_1117.sh (2026-11-17; user: "I think if you eat or drink, you should always just do the other one as well", then "Yes" to the
# A/B, then "Yes, all classes" to this lane). The fight lab's between-fight rest gets a rules knob, REST_TOGETHER (engine.BaseModule,
# default False = the regression; engine.Session.downtime): while you sit to drink or eat, the bar that did not fire tops up at its food or
# water rate for the sitting seconds, at no extra time. The A/B (scratchpad rest_both.py, variant B: the 29 leveling page picks of the
# seven mana classes, 8,000 fights, seeds 1-2, levels 20-60) found it never slower: mages 4.0-7.5% faster per kill, Balance 7.1%,
# Destruction 2.5%, the rest 0-1.4%. Claude set REST_TOGETHER true in the 21 rules files of the seven mana classes (warriors and rogues
# have no mana). What depends on the rules is made again, as fl_evo_1116.sh did for EVO_BELOW, for every mana class:
#   1. rules_retune.py --continued-only for each rotation on its page pick (the drink and eat lines move under the new rule);
#   2. the class's open records from the 20-60 race on (refresh_keys.py, fl_open_search.py), one-tree records included;
#   3. open builds, orders, races and reports;
#   then the healer and tank leveling paths, the own-rotation race, the filler pass of every mana page spec, validate, the by-level
#   guides measured, GearCheck's leveling values (standard gear, the Forever base, best gear), the add-on file and the rest cues
#   (eat_drink_together and the vectors agreed with the Addons session, 2026-11-17); after Claude has rewritten the between-fight lines
#   (marker fr1117/texts-done): pages, guide checks, page audit.
# Starts after Claude has committed the night of 2026-11-16 (marker fr1117/start). Full power: BelowNormal on 10 of 12 (RESERVE_CPUS=2).
# Log deep-runs/rest-1117.log (steps), rest-<lane>.log (output); markers deep-runs/fr1117/. Resume: the same command. Stop:
# Stop-Process the bash processes running this script (parent and lane subshells) and their python children (never TaskStop).
#   bash _reference/data/deep-runs/fl_rest_1117.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/fr1117
LOG=$L/rest-1117.log
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
tune() {      # tune <lane log> <class> <rotation> <page pick>
  [ -e $M/pre/$2-$3.json ] || cp $FL/rotations/$2-$3.json $M/pre/
  run tune-$2-$3 $1 python -u $FL/rules_retune.py $2 $3 $4 --jobs 3 --continued-only || say "WARNING: rules_retune $2 $3 failed; its saved rules stay"
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

mage() { local lg=rest-a.log
  tune $lg mage arcane-leveling arcane-open-leveling
  tune $lg mage fire-leveling fire-open-leveling
  tune $lg mage frost-leveling frost-open-leveling
  tune $lg mage barrage-frost-leveling arcane-frost-open-leveling
  tune $lg mage frostfire-leveling frostfire-open-leveling
  refresh $lg mage arcane-leveling fire-leveling frost-leveling barrage-frost-leveling frostfire-leveling
  finish $lg mage; }
druid() { local lg=rest-a.log
  tune $lg druid balance-dps opt-balance-dps-leveling-st
  tune $lg druid feral-cat-dps feral-combat-open-leveling
  refresh $lg druid feral-cat-dps balance-dps
  finish $lg druid; }
warlock() { local lg=rest-b.log
  tune $lg warlock affliction-leveling affliction-open-leveling
  tune $lg warlock demonology-leveling demonology-open-leveling
  tune $lg warlock destruction-leveling destruction-open-leveling
  refresh $lg warlock affliction-leveling demonology-leveling destruction-leveling
  finish $lg warlock; }
hunter() { local lg=rest-b.log
  tune $lg hunter bm-leveling beast-mastery-open-leveling
  tune $lg hunter mm-raid marksmanship-open-leveling
  tune $lg hunter melee-dps survival-open-leveling
  refresh $lg hunter bm-leveling mm-raid melee-dps
  refresh_pure $lg hunter "Beast Mastery" beast-mastery bm-leveling
  refresh_pure $lg hunter Survival survival melee-dps
  finish $lg hunter; }
paladin() { local lg=rest-c.log
  tune $lg paladin holy-leveling holy-leveling
  tune $lg paladin prot-leveling protection-leveling
  tune $lg paladin ret-dps leveling-retribution
  refresh $lg paladin holy-leveling prot-leveling ret-dps
  finish $lg paladin; }
priest() { local lg=rest-c.log
  tune $lg priest discipline-leveling discipline-leveling
  tune $lg priest holy-leveling smite-open-leveling
  tune $lg priest shadow-dps shadow-open-leveling
  refresh $lg priest discipline-leveling holy-leveling shadow-dps
  finish $lg priest; }
shaman() { local lg=rest-c.log
  tune $lg shaman elemental-dps elemental-open-leveling
  tune $lg shaman enhancement-dps enhancement-open-leveling
  refresh $lg shaman elemental-dps enhancement-dps
  finish $lg shaman; }

if [ ! -e $M/start ]; then
  say "waiting for Claude to commit the night (marker fr1117/start)"
  until [ -e $M/start ]; do sleep 60; done
fi
say "fl_rest_1117 start (REST_TOGETHER in the 21 rules files: $(grep -l '"REST_TOGETHER": true' $FL/rotations/*.json | wc -l))"
( mage; druid; say "lane A done" ) &
( warlock; hunter; say "lane B done" ) &
( paladin; priest; shaman; say "lane C done" ) &
wait
say "lanes done; rules the tunes changed: $(for f in $M/pre/*.json; do cmp -s $f $FL/rotations/$(basename $f) || printf '%s ' $(basename $f .json); done)"

C7="druid hunter mage paladin priest shaman warlock"
run lev-path tail.log python -u $D/raid_path_leveling.py paladin shaman priest druid --write || say "WARNING: raid_path_leveling failed"
run own-rotation tail.log python -u $FL/own_rotation_race.py --jobs 10 || say "WARNING: own_rotation_race failed"
for spec in "druid|Balance" "druid|Feral Combat" "hunter|Beast Mastery" "hunter|Marksmanship" "hunter|Survival" "mage|Arcane" "mage|Fire" \
            "mage|Frost" "mage|Hybrid Arcane/Frost" "mage|Hybrid Fire/Frost" "paladin|Retribution" "paladin|Hybrid Holy/Retribution" \
            "priest|Shadow" "priest|Hybrid Discipline/Holy" "shaman|Elemental" "shaman|Enhancement" "warlock|Affliction" \
            "warlock|Demonology" "warlock|Destruction"; do
  c=${spec%%|*}; s=${spec#*|}; slug=$(echo "$s" | tr 'A-Z' 'a-z' | tr '/ ' '--')
  run filler-$c-$slug tail.log python -u $FL/fl_filler_pass.py $c --spec "$s" --write --jobs 10 || say "WARNING: filler pass $c $s failed"
done
run validate tail.log python -u $D/validate_builds.py || { say "STOP: validate_builds failed (tail.log)"; exit 1; }
run measure tail.log python -u $D/level_guides.py $C7 --measure --jobs 10 || say "WARNING: level_guides --measure failed"
for c in $C7; do   # every page pick of the class: its rules changed (stat_weights_all.py redoes only missing or stale files)
  specs=$(python -c "
import importlib.util, sys
sys.path[:0] = ['_reference/data', '_reference/data/fightlab', '_reference/data/scorer']
spec = importlib.util.spec_from_file_location('sa', '_reference/data/fightlab/signature_audit.py'); SA = importlib.util.module_from_spec(spec); spec.loader.exec_module(SA)
print('|'.join(s[0] for s in SA.page_slots(sys.argv[1], signature=True) if s[1]))" $c)
  IFS='|' read -r -a S <<< "$specs"
  run aside-std-$c gear-rest.log python -u $L/weights_aside_1116.py leveling $c "${S[@]}" || say "WARNING: weights aside (standard) $c failed"
  run aside-best-$c gear-rest.log python -u $L/weights_aside_1116.py leveling-best $c "${S[@]}" || say "WARNING: weights aside (best) $c failed"
done
run weights-std gear-rest.log python -u $D/characters/stat_weights_all.py $C7 --jobs 10 || say "WARNING: stat weights (standard) failed"
run base gear-rest.log python -u $D/characters/forever_base.py $C7 --jobs 10 || say "WARNING: forever_base failed"
run weights-best gear-rest.log python -u $D/characters/stat_weights_all.py $C7 --base best --jobs 10 || say "WARNING: stat weights (best) failed"
run addon-values gear-rest.log python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"
say "numbers done: Claude rewrites the between-fight lines (leveling-steps.json, level-guides, guides) and touches fr1117/texts-done"
until [ -e $M/texts-done ]; do sleep 60; done
run regen tail.log python -u $D/rebuild.py --steps regen || say "WARNING: regen failed"
run guide-check tail.log python -u $D/level_guides.py --check || say "WARNING: by-level guide check lists problems (tail.log)"
run guides tail.log python -u $D/guides.py --check --write || say "WARNING: guides --check lists passages to rewrite (tail.log)"
run page-lint tail.log python -u $D/page_lint.py --write || say "WARNING: page_lint lists findings (_reference/page-lint.md)"
say "all done (review, commit, push; message the Addons session: eat_drink_together and the new lines)"
