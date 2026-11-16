#!/usr/bin/env bash
# fl_warlock_1116.sh (2026-11-16; user: "Go with your rec": the leveling simulator's Wrack as the hotfix of 2026-11-10 made it, and the
# Affliction pages redone on it). Code and data, by Claude before this lane:
#   - hotfix_text.WARLOCK_1110: Wrack's text (the live tooltip: a 6 s channel of 60 Shadow damage a second; while it channels, your Siphon
#     Life, Corruption and Bane of Agony on the target deal their periodic damage 100% faster) and its coefficient (20% a tick), written
#     into forever-spells/warlock.json and forever-talents/warlock.json (the 70753 text had stood: 86 a second, +10% to the other Shadow
#     damage over time effects); warlock/research/spells/README.md rendered;
#   - fightlab/warlock.py: the new wording read (TICK_FOR, WRACK_SPEED), 1.75 a level below 60 (25 at 40), and the half-point ticks of the
#     three effects while Wrack channels (_wrack_half_ticks, the official simulator's wrack.go rule: each a full tick, expiry kept).
#   Checked (scratch wl1116/identity_wl.py): with the old text the new module is bit-identical to the committed one (four warlock page
#   picks at 20-60, 108 duels); with the new text only Affliction moves, 5-11% faster per kill at 40-60 (60 fights); the field's Soul
#   Link warlock takes no Wrack, so every duel is unchanged.
# This lane:
#   1. the affliction-leveling rules from scratch and continued (rules_retune.py) on the Affliction page's build;
#   2. the warlock record's affliction-leveling rotation from the 20-60 race on (the other rotations' builds take no Wrack);
#   3. builds, orders, races and reports; the own-rotation race;
#   4. the leveling filler pass on Affliction; validate;
#   5. the by-level guides measured; GearCheck's leveling values of the Affliction pick (standard gear, the Forever base, best gear),
#      after the paladin lane's add-on step (forever_base.py and addon_values.py write shared records); the add-on file;
#   6. after Claude's guide texts (marker fw1116/guides-done): regen, guide checks, page audit.
# Full power (user, 2026-11-15 22:40): BelowNormal on 10 of 12 logical processors, next to the PvP queue and the paladin lane.
# Log deep-runs/warlock-1116.log (steps), wl1116-lane.log, wl1116-tune.log, wl1116-tail.log, gear-wl1116.log; markers deep-runs/fw1116/.
# tonight_1116.sh's warlock raid lane waits for this lane's "all done" (both write warlock's proposed-builds.json).
# Resume: the same command. Stop: Stop-Process the bash processes running this script and their python children (never TaskStop).
#   bash _reference/data/deep-runs/fl_warlock_1116.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/fw1116
LOG=$L/warlock-1116.log
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
LG=wl1116-lane.log
R=affliction-leveling

say "fl_warlock_1116 start"
# 1. the rules
[ -e $M/pre/warlock-$R.json ] || cp $FL/rotations/warlock-$R.json $M/pre/
run tune wl1116-tune.log python -u $FL/rules_retune.py warlock $R affliction-open-leveling --jobs 6 \
  || say "WARNING: rules_retune warlock $R failed; its saved rules stay"
cmp -s $M/pre/warlock-$R.json $FL/rotations/warlock-$R.json && say "rules: the saved rules stay" || say "rules: $R changed"
touch $M/tunes-done

# 2. the record from the 20-60 race on
run keys $LG python -u $L/refresh_keys.py warlock.json $R || { say "STOP: refresh_keys failed ($LG)"; exit 1; }
run open $LG python -u $FL/fl_open_search.py warlock --rotation $R --jobs 6 || say "WARNING: open $R failed"

# 3. builds, orders, races and reports, the own-rotation race
run builds $LG python -u $D/open_builds.py warlock --write --only leveling || say "WARNING: open_builds failed"
run orders $LG python -u $D/order_repair.py warlock --jobs 6 --write || say "WARNING: order_repair failed"
run race $LG python -u $D/rebuild.py warlock --steps race,report || say "WARNING: race failed"
run own $LG python -u $FL/own_rotation_race.py warlock --fresh --jobs 6 || say "WARNING: own_rotation_race failed"

# 4. the filler pass, validate
run filler-affliction $LG python -u $FL/fl_filler_pass.py warlock --spec "Affliction" --write --jobs 6 || say "WARNING: filler pass Affliction failed"
say "warlock lane done"
run validate wl1116-tail.log python -u $D/validate_builds.py || { say "STOP: validate_builds failed (wl1116-tail.log)"; exit 1; }

# 5. the by-level guides' numbers, GearCheck's values, the add-on file (after the paladin lane's: shared records)
run measure wl1116-tail.log python -u $D/level_guides.py warlock --measure --jobs 8 || say "WARNING: level_guides --measure failed"
if [ ! -e $M/base ]; then
  say "waiting for the paladin lane's add-on step (fp1116/addon-values)"
  until [ -e $L/fp1116/addon-values ]; do sleep 60; done
fi
run aside-std gear-wl1116.log python -u $L/weights_aside_1116.py leveling warlock "Affliction" || say "WARNING: weights aside (standard) failed"
run weights-std gear-wl1116.log python -u $D/characters/stat_weights_all.py warlock --jobs 8 || say "WARNING: stat weights (standard) failed"
run base gear-wl1116.log python -u $D/characters/forever_base.py warlock --jobs 8 || say "WARNING: forever_base failed"
run aside-best gear-wl1116.log python -u $L/weights_aside_1116.py leveling-best warlock "Affliction" || say "WARNING: weights aside (best) failed"
run weights-best gear-wl1116.log python -u $D/characters/stat_weights_all.py warlock --base best --jobs 8 || say "WARNING: stat weights (best) failed"
run addon-values gear-wl1116.log python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"

# 6. the pages, after Claude's guide texts
say "waiting for the guide texts (marker $M/guides-done)"
until [ -e "$M/guides-done" ]; do sleep 60; done
run regen wl1116-tail.log python -u $D/rebuild.py warlock --steps regen || say "WARNING: regen failed"
run guide-check wl1116-tail.log python -u $D/level_guides.py --check || say "WARNING: by-level guide check lists problems (wl1116-tail.log)"
run guides wl1116-tail.log python -u $D/guides.py --check --write || say "WARNING: guides --check lists passages to rewrite (wl1116-tail.log)"
run page-lint wl1116-tail.log python -u $D/page_lint.py --write || say "WARNING: page_lint lists findings (_reference/page-lint.md)"
say "all done (review, commit, push; message the Addons session about the warlock values)"
