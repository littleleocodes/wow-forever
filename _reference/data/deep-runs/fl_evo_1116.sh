#!/usr/bin/env bash
# fl_evo_1116.sh (2026-11-16; user: "Why is Evocation for mage used when below 40% and not when lower? It restores much more mana than
# 60%", then "Yes, run it at low priority now" for the A/B, then "Go full power mode"). mage.py's between-fight Evocation threshold is a
# rule knob since 2026-11-16 (EVO_BELOW, default 0.4 = the regression); the A/B (scratchpad evo_threshold.py: every mage leveling page
# pick, 20,000 fights, seeds 1-2, levels 20-60) put 0.15 ahead of 0.40 by 0.6-1.1% per kill, and Claude set EVO_BELOW 0.15 in the five
# rules files by hand (checked: the rules files reproduce the A/B's 0.15 runs exactly). What depends on the rules is made again, as
# fl_mage_armor_1115.sh did for MAGE_ARMOR:
#   1. rules_retune.py --continued-only for each rotation on its page pick (the knob is one more move; a new set installs only 0.3% ahead);
#   2. the mage record from the 20-60 race on for all five rotations (refresh_keys.py, fl_open_search.py);
#   3. open builds, orders, the class pipeline's race and reports, the own-rotation race;
#   4. the leveling filler pass on the five page specs;
#   5. validate, the by-level guides measured, GearCheck's leveling values (standard gear, the Forever base entries again, best gear), the
#      add-on file and the rest cues (one addon_values.py at a time);
#   6. after Claude has rewritten the Evocation lines of the guides (marker fe1116/guides-done): the mage pages, guide checks, page audit.
# Full power: BelowNormal on 10 of 12 logical processors (RESERVE_CPUS=2, PRIORITY=BelowNormal), next to the night (tonight_1116.sh) and
# the PvP queue. Log deep-runs/evo-1116.log (steps), evo-1116-out.log (output), evo-tune-<rotation>.log; markers deep-runs/fe1116/.
# Resume: the same command. Stop: Stop-Process the bash processes running this script and their python children (never TaskStop).
#   bash _reference/data/deep-runs/fl_evo_1116.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/fe1116
LOG=$L/evo-1116.log
OUT=evo-1116-out.log
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
running() {   # running <pattern>: a bash or python process whose command line holds the pattern is alive (not this check itself)
  powershell -NoProfile -Command "if (Get-CimInstance Win32_Process | Where-Object { (\$_.Name -eq 'bash.exe' -or \$_.Name -eq 'python.exe') -and \$_.CommandLine -like '*$1*' -and \$_.CommandLine -notlike '*CommandLine -like*' }) { exit 0 } else { exit 1 }" 2>/dev/null
}
addon_idle() { while running "characters/addon_values.py"; do sleep 60; done; }
# rotation:page pick (signature_audit.page_slots("mage", signature=True); the rest-cue file of 2026-11-16)
ROTS="arcane-leveling:arcane-open-leveling fire-leveling:fire-open-leveling frost-leveling:frost-open-leveling barrage-frost-leveling:arcane-frost-open-leveling frostfire-leveling:frostfire-open-leveling"
ALL="arcane-leveling fire-leveling frost-leveling barrage-frost-leveling frostfire-leveling"
SPECS=("Arcane" "Fire" "Frost" "Hybrid Arcane/Frost" "Hybrid Fire/Frost")

say "fl_evo_1116 start"
# 1. the rules (a copy of each file first, kept across a resume, to see which ones the tunes changed)
for rb in $ROTS; do r=${rb%%:*}; [ -e $M/pre/mage-$r.json ] || cp $FL/rotations/mage-$r.json $M/pre/; done
for rb in $ROTS; do r=${rb%%:*}; b=${rb##*:}
  ( run tune-$r evo-tune-$r.log python -u $FL/rules_retune.py mage $r $b --jobs 2 --continued-only \
      || say "WARNING: rules_retune mage $r failed; its saved rules stay" ) &
done
wait
CHANGED=""
for rb in $ROTS; do r=${rb%%:*}; cmp -s $M/pre/mage-$r.json $FL/rotations/mage-$r.json || CHANGED="$CHANGED $r"; done
say "the tunes changed:${CHANGED:- none} (EVO_BELOW now: $(grep -ho '"EVO_BELOW": [0-9.]*' $FL/rotations/mage-*-leveling.json | tr '\n' ' '))"

# 2. the record from the 20-60 race on (every rotation: EVO_BELOW 0.15 is a rules change for all five)
run keys $OUT python -u $L/refresh_keys.py mage.json $ALL || { say "STOP: refresh_keys failed"; exit 1; }
for r in $ALL; do
  run open-$r $OUT python -u $FL/fl_open_search.py mage --rotation $r --jobs 4 || say "WARNING: open mage $r failed"
done
# 3. builds, orders, races, reports
run builds $OUT python -u $D/open_builds.py mage --write --only leveling || say "WARNING: open_builds failed"
run orders $OUT python -u $D/order_repair.py mage --jobs 4 --write || say "WARNING: order_repair failed"
run race $OUT python -u $D/rebuild.py mage --steps race,report || say "WARNING: race failed"
run own-rotation $OUT python -u $FL/own_rotation_race.py mage --fresh --jobs 4 || say "WARNING: own_rotation_race failed"
# 4. the leveling filler pass
for s in "${SPECS[@]}"; do
  slug=$(echo "$s" | tr 'A-Z' 'a-z' | tr '/ ' '--')
  run filler-$slug $OUT python -u $FL/fl_filler_pass.py mage --spec "$s" --write --jobs 4 || say "WARNING: filler pass $s failed"
done
run validate $OUT python -u $D/validate_builds.py || { say "STOP: validate_builds failed ($OUT)"; exit 1; }
# 5. the by-level guides' numbers, GearCheck's values, the add-on file and the rest cues
run measure $OUT python -u $D/level_guides.py mage --measure --jobs 4 || say "WARNING: level_guides --measure failed"
run aside-std gear-evo.log python -u $L/weights_aside_1115.py leveling mage "${SPECS[@]}" || say "WARNING: weights aside (standard) failed"
run weights-std gear-evo.log python -u $D/characters/stat_weights_all.py mage --jobs 4 || say "WARNING: stat weights (standard) failed"
run base gear-evo.log python -u $D/characters/forever_base.py mage --jobs 4 || say "WARNING: forever_base failed"
run aside-best gear-evo.log python -u $L/weights_aside_1115.py leveling-best mage "${SPECS[@]}" || say "WARNING: weights aside (best) failed"
run weights-best gear-evo.log python -u $D/characters/stat_weights_all.py mage --base best --jobs 4 || say "WARNING: stat weights (best) failed"
addon_idle
run addon-values gear-evo.log python -u $D/characters/addon_values.py || say "WARNING: addon_values failed (the rest cues check every mage spec's EVO_BELOW)"

# 6. the pages, after Claude's guide texts
say "waiting for the guide texts (marker $M/guides-done)"
until [ -e "$M/guides-done" ]; do sleep 60; done
run regen $OUT python -u $D/rebuild.py mage --steps regen || say "WARNING: regen failed"
run guide-check $OUT python -u $D/level_guides.py --check || say "WARNING: by-level guide check lists problems ($OUT)"
run guides $OUT python -u $D/guides.py --check --write || say "WARNING: guides --check lists passages to rewrite ($OUT)"
run page-lint $OUT python -u $D/page_lint.py --write || say "WARNING: page_lint lists findings (_reference/page-lint.md)"
say "all done (review, commit, push; message the Addons session: the mage values and the Evocation cue 40% -> 15%; refresh Arcea)"
