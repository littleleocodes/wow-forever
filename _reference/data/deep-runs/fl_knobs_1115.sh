#!/usr/bin/env bash
# fl_knobs_1115.sh (2026-11-15; user: "Go full power, go with your recs": search-improvements 0h's check of the rogue's poisons and the
# shaman's weapon imbue, as the mage's armor was checked). Code and data, by Claude before this lane:
#   - rule knobs rogue.POISONS (the poison on each hand) and shaman.IMBUE_EARLY / IMBUE_LATE / IMBUE_TOP / IMBUE_TOP_FROM (all in
#     duellab/duel.PVE_KNOBS); the shaman's imbues at their level (spell_scaling.json's referenced rows, tables.rank_amounts);
#   - live_spells.to_level60 also brings the numbers a description takes from another spell back to level 60: eight ranks of the
#     70888 pull had kept Wowhead's MaxLevel numbers (Windfury Weapon rank 4: 433 for the client's 333; Rockbiter 7, Frostbrand 5,
#     Seal of Command 5, Seal of Fury 7, Light's Vigil 3, Holy Nova 6, Dire Bear Form); forever-spells rebuilt.
# This lane:
#   1. the rules, side by side: the rogue's three rotations --continued-only (same mechanics, one more knob); the shaman's two from
#      scratch and continued (its imbue numbers moved below 60, Windfury's at 60); the paladin's three --continued-only (the seals'
#      judgements at 58-60). Marker fk1115/tunes-done: pvp_restart_1115.sh then runs the duel matrix and the PvP search queue;
#   2. the records from the 20-60 race on: the rogue's changed rotations, every shaman and paladin rotation (their numbers moved);
#   3. builds, orders, races and reports; the own-rotation race; the raid-path leveling of Holy, Protection and Restoration;
#   4. the leveling filler pass on the changed specs' page builds (the paladin's hybrids are left: their gate swaps were made by hand);
#      validate;
#   5. the by-level guides measured; GearCheck's leveling values of the changed picks (standard gear, the Forever base, best gear); the
#      add-on file;
#   6. after Claude's guide texts (marker fk1115/guides-done): regen, guide checks, page audit.
# Full power (user, 2026-11-15 22:40: "Go full power"): BelowNormal on 10 of 12 logical processors (RESERVE_CPUS=2).
# Log deep-runs/knobs-1115.log (steps), knobs-<class>.log, knobs-tune-<class>-<rotation>.log, knobs-tail.log, gear-knobs.log;
# markers deep-runs/fk1115/. Resume: the same command. Stop: Stop-Process the bash processes running this script (parent and lane
# subshells) and their python children (never TaskStop).
#   bash _reference/data/deep-runs/fl_knobs_1115.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/fk1115
LOG=$L/knobs-1115.log
FL=_reference/data/fightlab
D=_reference/data
mkdir -p $M/pre
rmdir $M/finish.lock 2>/dev/null   # a lock left by a stopped run
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
# class:rotation:page pick:mode (signature_audit.page_slots(<class>, signature=True), 2026-11-15; the paladin's pairs as the morning queue)
TUNES="rogue:combat-daggers-raid:assassination-open-leveling:--continued-only rogue:combat-swords-raid:combat-open-leveling:--continued-only
rogue:subtlety-leveling:subtlety-open-leveling:--continued-only shaman:enhancement-dps:enhancement-open-leveling:
shaman:elemental-dps:elemental-open-leveling: paladin:holy-leveling:holy-leveling:--continued-only
paladin:prot-leveling:protection-leveling:--continued-only paladin:ret-dps:leveling-retribution:--continued-only"

say "fl_knobs_1115 start"
# 1. the rules (a copy of each saved file first, kept across a resume, to see which ones the tunes changed)
for t in $TUNES; do IFS=: read -r c r b mode <<< "$t"; [ -e $M/pre/$c-$r.json ] || cp $FL/rotations/$c-$r.json $M/pre/; done
for t in $TUNES; do IFS=: read -r c r b mode <<< "$t"
  ( run tune-$c-$r knobs-tune-$c-$r.log python -u $FL/rules_retune.py $c $r $b --jobs 2 $mode \
      || say "WARNING: rules_retune $c $r failed; its saved rules stay" ) &
done
wait
changed() { local c=$1 out=""
  for t in $TUNES; do IFS=: read -r cc r b mode <<< "$t"; [ "$cc" = "$c" ] || continue
    cmp -s $M/pre/$c-$r.json $FL/rotations/$c-$r.json || out="$out $r"; done
  echo $out; }
RCH=$(changed rogue); SCH=$(changed shaman); PCH=$(changed paladin)
say "rules changed: rogue:${RCH:- none}; shaman:${SCH:- none}; paladin:${PCH:- none}"
touch $M/tunes-done

refresh() {   # refresh <lane log> <class> <rotations...>: the class record from the 20-60 race on
  local lg=$1 c=$2; shift 2
  run keys-$c $lg python -u $L/refresh_keys.py $c.json "$@" || { say "WARNING: refresh_keys $c failed"; return 1; }
  for r in "$@"; do run open-$c-$r $lg python -u $FL/fl_open_search.py $c --rotation $r --jobs 4 || say "WARNING: open $c $r failed"; done
}
refresh_pure() {   # refresh_pure <lane log> <class> <tree> <tree slug> <rotation>: a one-tree record from the 20-60 race on
  local lg=$1 c=$2 tree=$3 slug=$4 r=$5
  run keys-$c-$slug $lg python -u $L/refresh_keys.py pure/$c-$slug.json $r || { say "WARNING: refresh_keys pure $c-$slug failed"; return 1; }
  run open-$c-$slug $lg python -u $FL/fl_open_search.py $c --tree "$tree" --rotation $r --jobs 4 || say "WARNING: open $c $slug failed"
}
locked() {    # locked <command...>: one finish step at a time across the lanes (the signature audit, last-rebuild, own-rotation and
  #             derived-leveling records are shared and written without a lock; fl_fix_1115_cw.sh's rule)
  until mkdir $M/finish.lock 2>/dev/null; do sleep 20; done
  "$@"; local rc=$?
  rmdir $M/finish.lock
  return $rc
}
finish() {    # finish <lane log> <class>: open builds, orders, races and reports, the own-rotation race
  locked run builds-$2 $1 python -u $D/open_builds.py $2 --write --only leveling || say "WARNING: open_builds $2 failed"
  locked run orders-$2 $1 python -u $D/order_repair.py $2 --jobs 4 --write || say "WARNING: order_repair $2 failed"
  locked run race-$2 $1 python -u $D/rebuild.py $2 --steps race,report || say "WARNING: race $2 failed"
  locked run own-$2 $1 python -u $FL/own_rotation_race.py $2 --fresh --jobs 4 || say "WARNING: own_rotation_race $2 failed"
}
filler() {    # filler <lane log> <class> <specs...>
  local lg=$1 c=$2; shift 2
  for s in "$@"; do
    local slug=$(echo "$s" | tr 'A-Z' 'a-z' | tr '/ ' '--')
    locked run filler-$c-$slug $lg python -u $FL/fl_filler_pass.py $c --spec "$s" --write --jobs 4 || say "WARNING: filler pass $c $s failed"
  done
}

rogue_lane() { local lg=knobs-rogue.log specs=()
  if [ -z "$RCH" ]; then say "rogue: no rules changed (the poisons stay Instant on the main hand, Deadly on the off hand)"; : > $M/specs-rogue; return 0; fi
  refresh $lg rogue $RCH
  case " $RCH " in *" combat-daggers-raid "*) refresh_pure $lg rogue Assassination assassination combat-daggers-raid; specs+=("Assassination");; esac
  case " $RCH " in *" combat-swords-raid "*) specs+=("Combat");; esac
  case " $RCH " in *" subtlety-leveling "*) refresh_pure $lg rogue Subtlety subtlety subtlety-leveling; specs+=("Subtlety" "Hybrid Combat/Subtlety");; esac
  finish $lg rogue
  filler $lg rogue "${specs[@]}"
  printf '%s\n' "${specs[@]}" > $M/specs-rogue
  say "rogue lane done"
}
shaman_lane() { local lg=knobs-shaman.log
  refresh $lg shaman enhancement-dps elemental-dps
  refresh_pure $lg shaman Elemental elemental elemental-dps
  finish $lg shaman
  locked run raidpath-shaman $lg python -u $D/raid_path_leveling.py shaman --write || say "WARNING: raid_path_leveling shaman failed"
  filler $lg shaman "Elemental" "Enhancement" "Hybrid Elemental/Enhancement"
  printf '%s\n' "Elemental" "Enhancement" "Restoration" "Hybrid Elemental/Enhancement" > $M/specs-shaman
  say "shaman lane done"
}
paladin_lane() { local lg=knobs-paladin.log
  refresh $lg paladin holy-leveling prot-leveling ret-dps
  finish $lg paladin
  locked run raidpath-paladin $lg python -u $D/raid_path_leveling.py paladin --write || say "WARNING: raid_path_leveling paladin failed"
  filler $lg paladin "Retribution"
  printf '%s\n' "Holy" "Protection" "Retribution" "Hybrid Holy/Protection" "Hybrid Protection/Retribution" > $M/specs-paladin
  say "paladin lane done"
}
# 2-4. the three classes side by side
rogue_lane &
shaman_lane &
paladin_lane &
wait
say "lanes done"
run validate knobs-tail.log python -u $D/validate_builds.py || { say "STOP: validate_builds failed (knobs-tail.log)"; exit 1; }

# 5. the by-level guides' numbers, GearCheck's values, the add-on file
run measure knobs-tail.log python -u $D/level_guides.py rogue shaman paladin --measure --jobs 10 || say "WARNING: level_guides --measure failed"
CL=""
for c in rogue shaman paladin; do
  [ -s $M/specs-$c ] || continue
  CL="$CL $c"
  mapfile -t S < $M/specs-$c
  run aside-std-$c gear-knobs.log python -u $L/weights_aside_1115.py leveling $c "${S[@]}" || say "WARNING: weights aside (standard) $c failed"
done
if [ -n "$CL" ]; then
  run weights-std gear-knobs.log python -u $D/characters/stat_weights_all.py $CL --jobs 10 || say "WARNING: stat weights (standard) failed"
  run base gear-knobs.log python -u $D/characters/forever_base.py $CL --jobs 10 || say "WARNING: forever_base failed"
  for c in $CL; do
    mapfile -t S < $M/specs-$c
    run aside-best-$c gear-knobs.log python -u $L/weights_aside_1115.py leveling-best $c "${S[@]}" || say "WARNING: weights aside (best) $c failed"
  done
  run weights-best gear-knobs.log python -u $D/characters/stat_weights_all.py $CL --base best --jobs 10 || say "WARNING: stat weights (best) failed"
  run addon-values gear-knobs.log python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"
fi

# 6. the pages, after Claude's guide texts
say "waiting for the guide texts (marker $M/guides-done)"
until [ -e "$M/guides-done" ]; do sleep 60; done
run regen knobs-tail.log python -u $D/rebuild.py rogue shaman paladin --steps regen || say "WARNING: regen failed"
run guide-check knobs-tail.log python -u $D/level_guides.py --check || say "WARNING: by-level guide check lists problems (knobs-tail.log)"
run guides knobs-tail.log python -u $D/guides.py --check --write || say "WARNING: guides --check lists passages to rewrite (knobs-tail.log)"
run page-lint knobs-tail.log python -u $D/page_lint.py --write || say "WARNING: page_lint lists findings (_reference/page-lint.md)"
say "all done (review, commit, push; message the Addons session about the rogue, shaman and paladin values; raise the PvP queue to BelowNormal)"
