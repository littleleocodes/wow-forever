#!/usr/bin/env bash
# fl_hotfix_1116.sh (2026-11-16; user: "Run both tonight"): two server hotfixes Blizzard's written notes left out, found at the night's
# re-pin to 2e6e77d84 (sim_value_audit's new row and the spell-data diff ff9babba5..2e6e77d84):
#   - Mental Dexterity: 50/100/150% of Intellect as attack power -> 33/66/100% (hotfix push 114027, wowsims/forever #969). Both shaman
#     leveling page picks with it (Enhancement, Elemental) measured 0.4-2.5% slower per kill (scratch wl1116/mental_dex.py);
#   - Wild Growth: spell power coefficient 3.3% -> 6.6% a tick, all three ranks (push 114015, wowsims/forever 3b7e5d80c).
# Data, by Claude before this lane: hotfix_text.py's entries (SHAMAN_PUSH_114027, DRUID_PUSH_114015), applied to forever-talents/shaman.json
# and forever-spells/druid.json only (scratch wl1116/hotfix_gaps.py: each file swapped in by rename, the druid spells page re-rendered);
# both labs read the new numbers (checked). The raid side needs nothing: the re-pinned simulator has both.
# Two parts side by side, next to tonight_1116.sh and the PvP search queue:
#   A. the shaman's leveling: the rules of enhancement-dps (Enhancement's pick; Restoration levels on the same rules) and elemental-dps,
#      from scratch and continued; the record from the 20-60 race on; builds, orders, races, reports, the own-rotation race, Restoration's
#      raid-path leveling; the filler pass on Enhancement and Elemental (the steps that write proposed-builds.json wait while the night's
#      shaman raid lane runs: order_repair.py and fl_filler_pass.py write the file without the lock); validate; the by-level guides
#      measured; GearCheck's leveling values of the three shaman picks after the warlock lane's add-on step (forever_base.py and
#      addon_values.py write shared files); the add-on file; after Claude's guide texts (marker fh1116/guides-done-shaman) the pages;
#   B. the Restoration druid in the healer lab, after the night's druid gear repair (its heal_gear.py makes the healer set this search plays;
#      a STOP in the night's log lets it go on): deep_heal.py --fresh, one cycle (talents and the heal-choice policy; the 2026-11-09
#      run took 763 minutes for three); the healer set again for the winner; the healer filler pass; validate; GearCheck's healer
#      values; the add-on file and the pages.
#   Then the guide checks and the page audit.
# Full power (user, 2026-11-15 22:40: "Go full power"): BelowNormal on 10 of 12 logical processors (RESERVE_CPUS=2).
# Log deep-runs/hotfix-1116.log (steps), sha1116-*.log, dru1116-heal.log, hf1116-tail.log, gear-sha1116.log; markers deep-runs/fh1116/.
# Resume: the same command. Stop: Stop-Process the bash processes running this script and their python children (never TaskStop).
#   bash _reference/data/deep-runs/fl_hotfix_1116.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/fh1116
LOG=$L/hotfix-1116.log
FL=_reference/data/fightlab
HL=_reference/data/heallab
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
running() {   # running <pattern>: a bash or python process whose command line holds the pattern is alive (not this check itself)
  powershell -NoProfile -Command "if (Get-CimInstance Win32_Process | Where-Object { (\$_.Name -eq 'bash.exe' -or \$_.Name -eq 'python.exe') -and \$_.CommandLine -like '*$1*' -and \$_.CommandLine -notlike '*CommandLine -like*' }) { exit 0 } else { exit 1 }" 2>/dev/null
}
raid_shaman_idle() {   # the night's shaman raid lane writes proposed-builds.json too: wait while it runs
  if running "raid_shaman_1103.sh"; then
    say "waiting: the night's shaman raid lane is running (it writes the same build file)"
    while running "raid_shaman_1103.sh"; do sleep 120; done
  fi
}
addon_idle() {   # one addon_values.py at a time (forever-gear-values.json and the rest cues)
  while running "characters/addon_values.py"; do sleep 60; done
}

shaman_lane() {
  local LG=sha1116-lane.log
  local TUNES="enhancement-dps:enhancement-open-leveling elemental-dps:elemental-open-leveling"
  # 1. the rules, side by side (a copy of each saved file first, kept across a resume, to see which ones the tunes changed)
  for t in $TUNES; do IFS=: read -r r b <<< "$t"; [ -e $M/pre/shaman-$r.json ] || cp $FL/rotations/shaman-$r.json $M/pre/; done
  for t in $TUNES; do IFS=: read -r r b <<< "$t"
    ( run tune-$r sha1116-tune-$r.log python -u $FL/rules_retune.py shaman $r $b --jobs 3 \
        || say "WARNING: rules_retune shaman $r failed; its saved rules stay" ) &
  done
  wait
  local CH=""
  for t in $TUNES; do IFS=: read -r r b <<< "$t"; cmp -s $M/pre/shaman-$r.json $FL/rotations/shaman-$r.json || CH="$CH $r"; done
  say "shaman rules changed:${CH:- none}"
  touch $M/tunes-done
  # 2. the record from the 20-60 race on (one rotation at a time: they share fightlab/open/shaman.json)
  run keys-shaman $LG python -u $L/refresh_keys.py shaman.json enhancement-dps elemental-dps || { say "STOP (shaman): refresh_keys failed ($LG)"; return 1; }
  for r in enhancement-dps elemental-dps; do
    run open-$r $LG python -u $FL/fl_open_search.py shaman --rotation $r --jobs 6 || say "WARNING: open $r failed"
  done
  # 3. builds, orders, races and reports, the own-rotation race, Restoration's raid-path leveling
  raid_shaman_idle
  run builds $LG python -u $D/open_builds.py shaman --write --only leveling || say "WARNING: open_builds failed"
  raid_shaman_idle
  run orders $LG python -u $D/order_repair.py shaman --jobs 6 --write || say "WARNING: order_repair failed"
  run race $LG python -u $D/rebuild.py shaman --steps race,report || say "WARNING: race failed"
  run own $LG python -u $FL/own_rotation_race.py shaman --fresh --jobs 6 || say "WARNING: own_rotation_race failed"
  raid_shaman_idle
  run raidpath $LG python -u $D/raid_path_leveling.py shaman --write || say "WARNING: raid_path_leveling failed"
  # 4. the filler pass, validate
  raid_shaman_idle
  run filler-enhancement $LG python -u $FL/fl_filler_pass.py shaman --spec "Enhancement" --write --jobs 6 || say "WARNING: filler pass Enhancement failed"
  raid_shaman_idle
  run filler-elemental $LG python -u $FL/fl_filler_pass.py shaman --spec "Elemental" --write --jobs 6 || say "WARNING: filler pass Elemental failed"
  run validate-shaman hf1116-tail.log python -u $D/validate_builds.py || { say "STOP (shaman): validate_builds failed (hf1116-tail.log)"; return 1; }
  say "shaman builds done"
  # 5. the by-level guides' numbers, GearCheck's values (after the warlock lane's add-on step: shared records), the add-on file
  run measure-shaman hf1116-tail.log python -u $D/level_guides.py shaman --measure --jobs 8 || say "WARNING: level_guides --measure failed"
  if [ ! -e $M/base ]; then
    say "waiting for the warlock lane's add-on step (fw1116/addon-values)"
    until [ -e $L/fw1116/addon-values ] || grep -q "addon-values rc=\|all done" $L/warlock-1116.log 2>/dev/null; do sleep 60; done
  fi
  local S=("Elemental" "Enhancement" "Restoration")
  run aside-std gear-sha1116.log python -u $L/weights_aside_1116.py leveling shaman "${S[@]}" || say "WARNING: weights aside (standard) failed"
  run weights-std gear-sha1116.log python -u $D/characters/stat_weights_all.py shaman --jobs 8 || say "WARNING: stat weights (standard) failed"
  run base gear-sha1116.log python -u $D/characters/forever_base.py shaman --jobs 8 || say "WARNING: forever_base failed"
  run aside-best gear-sha1116.log python -u $L/weights_aside_1116.py leveling-best shaman "${S[@]}" || say "WARNING: weights aside (best) failed"
  run weights-best gear-sha1116.log python -u $D/characters/stat_weights_all.py shaman --base best --jobs 8 || say "WARNING: stat weights (best) failed"
  addon_idle
  run addon-values-shaman gear-sha1116.log python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"
  touch $M/shaman-addon-tried
  # 6. the pages, after Claude's guide texts
  say "waiting for the shaman guide texts (marker $M/guides-done-shaman)"
  until [ -e "$M/guides-done-shaman" ]; do sleep 60; done
  run regen-shaman hf1116-tail.log python -u $D/rebuild.py shaman --steps regen || say "WARNING: shaman regen failed"
  say "shaman part done"
}

druid_lane() {
  local LG=dru1116-heal.log
  if [ ! -e $M/gear-druid-seen ]; then
    say "druid: waiting for the night's druid gear repair (r1116/gear-druid; a STOP in tonight-1116.log lets it go on)"
    until [ -e $L/r1116/gear-druid ] || grep -q "STOP" $L/tonight-1116.log 2>/dev/null; do sleep 120; done
    touch $M/gear-druid-seen
  fi
  run deep-heal-druid $LG python -u $HL/deep_heal.py druid --fresh --cycles 1 --jobs 6 || say "WARNING: deep_heal druid failed"
  run heal-gear-druid $LG python -u $HL/heal_gear.py druid --fresh --jobs 4 || say "WARNING: heal_gear druid failed"
  run heal-filler-druid $LG python -u $HL/filler_pass.py druid --build restoration-ml-heal --write --jobs 6 || say "WARNING: healer filler pass failed"
  run validate-druid $LG python -u $D/validate_builds.py || { say "STOP (druid): validate_builds failed ($LG)"; return 1; }
  run heal-values-druid $LG python -u $HL/heal_values.py druid --jobs 6 || say "WARNING: heal_values druid failed"
  until [ -e $M/shaman-addon-tried ] || [ -e $M/shaman-finished ]; do sleep 60; done
  addon_idle
  run addon-values-druid $LG python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"
  until [ -e $M/shaman-finished ]; do sleep 60; done   # one regen at a time (both write the shared pages)
  run regen-druid hf1116-tail.log python -u $D/rebuild.py druid --steps regen || say "WARNING: druid regen failed"
  say "druid part done"
}

say "fl_hotfix_1116 start"
rm -f $M/shaman-finished
( shaman_lane; touch $M/shaman-finished ) & PS=$!
druid_lane & PD=$!
wait $PS $PD
run guide-check hf1116-tail.log python -u $D/level_guides.py --check || say "WARNING: by-level guide check lists problems (hf1116-tail.log)"
run guides hf1116-tail.log python -u $D/guides.py --check --write || say "WARNING: guides --check lists passages to rewrite (hf1116-tail.log)"
run page-lint hf1116-tail.log python -u $D/page_lint.py --write || say "WARNING: page_lint lists findings (_reference/page-lint.md)"
say "all done (review the Restoration guide's stamp and the shaman texts, commit with the night, message the Addons session)"
