#!/usr/bin/env bash
# fl_paladin_1116.sh (2026-11-16; user: "Go with your rec": search-improvements 0h's paladin gear and seal, with 0i's seal scaling).
# Code and data, by Claude before this lane:
#   - rule knobs paladin.CASTER_GEAR_FROM (a Holy-path build with Holy Shock wears the caster row from this level; 0 = from Holy Shock,
#     as before; 61 = never) and SOR_FROM (Seal of Righteousness instead of Seal of Command from this level; 61 = never, as before),
#     both in duellab/duel.PVE_KNOBS;
#   - the seals' judgements at the paladin's level (paladin._level_judgement; spell_scaling.json's referenced "judgement" rows from the
#     official simulator's store for Seal of Command, Seal of Righteousness and Seal of Fury); nothing changes at 60.
#   Checked (scratch pal1116/identity_pal.py): with the scaling off and the knobs at their defaults the module is bit-identical to the
#   committed one (the five page picks at 12-60, 108 duels); with the scaling on, identical at 60 and in every duel, 0-6.5% slower per
#   kill below 60 (60 fights). Melee gear keeps Holy Shock at 21-26% of the damage (the Shockadin's floor is 12%).
# This lane:
#   1. the rules of the three paladin rotations, from scratch and continued (rules_retune.py: the judgements moved below 60, two new
#      knobs); holy-leveling on the Shockadin, the rotation's page winner and the build both knobs act on (the Holy page's build has no
#      Seal of Command); prot-leveling and ret-dps on their pages' builds as before;
#   2. the paladin record from the 20-60 race on, every rotation (all three moved below 60);
#   3. builds, orders, races and reports; the own-rotation race; the raid-path leveling of Holy and Protection;
#   4. the leveling filler pass on Retribution and the Shockadin (the Prot-Ret hybrid's gate swaps were made by hand); validate;
#   5. the by-level guides measured; GearCheck's leveling values of the five paladin picks (standard gear, the Forever base, best gear);
#      the add-on file;
#   6. after Claude's guide texts (marker fp1116/guides-done): regen, guide checks, page audit.
# Full power (user, 2026-11-15 22:40: "Go full power"): BelowNormal on 10 of 12 logical processors (RESERVE_CPUS=2), next to the PvP
# search queue (pvp_search_1115.sh, BelowNormal on the same processors).
# Log deep-runs/paladin-1116.log (steps), pal1116-lane.log, pal1116-tune-<rotation>.log, pal1116-tail.log, gear-pal1116.log; markers
# deep-runs/fp1116/. Resume: the same command. Stop: Stop-Process the bash processes running this script and their python children
# (never TaskStop).
#   bash _reference/data/deep-runs/fl_paladin_1116.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/fp1116
LOG=$L/paladin-1116.log
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
# rotation:tuning build
TUNES="holy-leveling:shockadin-open-leveling prot-leveling:protection-leveling ret-dps:leveling-retribution"
LG=pal1116-lane.log

say "fl_paladin_1116 start"
# 1. the rules, side by side (a copy of each saved file first, kept across a resume, to see which ones the tunes changed)
for t in $TUNES; do IFS=: read -r r b <<< "$t"; [ -e $M/pre/paladin-$r.json ] || cp $FL/rotations/paladin-$r.json $M/pre/; done
for t in $TUNES; do IFS=: read -r r b <<< "$t"
  ( run tune-$r pal1116-tune-$r.log python -u $FL/rules_retune.py paladin $r $b --jobs 3 \
      || say "WARNING: rules_retune paladin $r failed; its saved rules stay" ) &
done
wait
CH=""
for t in $TUNES; do IFS=: read -r r b <<< "$t"; cmp -s $M/pre/paladin-$r.json $FL/rotations/paladin-$r.json || CH="$CH $r"; done
say "rules changed:${CH:- none}"
touch $M/tunes-done

# 2. the record from the 20-60 race on (one rotation at a time: they share fightlab/open/paladin.json)
run keys-paladin $LG python -u $L/refresh_keys.py paladin.json holy-leveling prot-leveling ret-dps || { say "STOP: refresh_keys failed ($LG)"; exit 1; }
for r in holy-leveling prot-leveling ret-dps; do
  run open-$r $LG python -u $FL/fl_open_search.py paladin --rotation $r --jobs 6 || say "WARNING: open $r failed"
done

# 3. builds, orders, races and reports, the own-rotation race, the raid-path leveling
run builds $LG python -u $D/open_builds.py paladin --write --only leveling || say "WARNING: open_builds failed"
run orders $LG python -u $D/order_repair.py paladin --jobs 6 --write || say "WARNING: order_repair failed"
run race $LG python -u $D/rebuild.py paladin --steps race,report || say "WARNING: race failed"
run own $LG python -u $FL/own_rotation_race.py paladin --fresh --jobs 6 || say "WARNING: own_rotation_race failed"
run raidpath $LG python -u $D/raid_path_leveling.py paladin --write || say "WARNING: raid_path_leveling failed"

# 4. the filler pass, validate
run filler-retribution $LG python -u $FL/fl_filler_pass.py paladin --spec "Retribution" --write --jobs 6 || say "WARNING: filler pass Retribution failed"
run filler-shockadin $LG python -u $FL/fl_filler_pass.py paladin --spec "Hybrid Holy/Retribution" --write --jobs 6 || say "WARNING: filler pass Shockadin failed"
say "paladin lane done"
run validate pal1116-tail.log python -u $D/validate_builds.py || { say "STOP: validate_builds failed (pal1116-tail.log)"; exit 1; }

# 5. the by-level guides' numbers, GearCheck's values, the add-on file
run measure pal1116-tail.log python -u $D/level_guides.py paladin --measure --jobs 8 || say "WARNING: level_guides --measure failed"
S=("Holy" "Protection" "Retribution" "Hybrid Holy/Retribution" "Hybrid Protection/Retribution")
run aside-std gear-pal1116.log python -u $L/weights_aside_1116.py leveling paladin "${S[@]}" || say "WARNING: weights aside (standard) failed"
run weights-std gear-pal1116.log python -u $D/characters/stat_weights_all.py paladin --jobs 8 || say "WARNING: stat weights (standard) failed"
run base gear-pal1116.log python -u $D/characters/forever_base.py paladin --jobs 8 || say "WARNING: forever_base failed"
run aside-best gear-pal1116.log python -u $L/weights_aside_1116.py leveling-best paladin "${S[@]}" || say "WARNING: weights aside (best) failed"
run weights-best gear-pal1116.log python -u $D/characters/stat_weights_all.py paladin --base best --jobs 8 || say "WARNING: stat weights (best) failed"
run addon-values gear-pal1116.log python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"

# 6. the pages, after Claude's guide texts
say "waiting for the guide texts (marker $M/guides-done)"
until [ -e "$M/guides-done" ]; do sleep 60; done
run regen pal1116-tail.log python -u $D/rebuild.py paladin --steps regen || say "WARNING: regen failed"
run guide-check pal1116-tail.log python -u $D/level_guides.py --check || say "WARNING: by-level guide check lists problems (pal1116-tail.log)"
run guides pal1116-tail.log python -u $D/guides.py --check --write || say "WARNING: guides --check lists passages to rewrite (pal1116-tail.log)"
run page-lint pal1116-tail.log python -u $D/page_lint.py --write || say "WARNING: page_lint lists findings (_reference/page-lint.md)"
say "all done (review, commit, push; message the Addons session about the paladin values)"
