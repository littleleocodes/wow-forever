#!/usr/bin/env bash
# gear_phase_1118.sh (2026-11-18; user: "Go with your rec"). The gear night after the Tier 0.5 research
# (_reference/tier-0.5-research.md, page-audit Q10-Q12). The simulator's database dates every item: phase 1 is what Forever has now,
# phase 2 the raids (from 2026-12-09) and later content. Our pools never read it, and 15 later items had come in through the
# community presets they trust (Rockfury Bracers in 41 of our 99 sets). The pool fix is in the code (gear_opt.later_phase,
# gear_tiers.pool_of):
# - pre-BiS and the new quests-and-dungeons tier take phase 1 only;
# - Raid BiS takes phase-2 items only from Molten Core and Onyxia ("Phase 1 BiS" before);
# - Tier 0.5 is in neither pre-raid tier;
# - Onyxia's quest rewards count unvetted.
# Steps, after the hybrid check ("hybrid check done" in hybrid-check-1118.log):
#   1. every class's standard sets (gear_opt.py --write --fresh, --apply), tank and healer sets, gear_check;
#   2. every ML record's tier sets and searches again (ml_prep_1118.py, ml_pipeline.py <class> --steps final), ML builds, validate;
#   3. every raid entry raced in the new standard sets (dummy and environments), tidy, unused abilities;
#   4. the quests-and-dungeons tier (dungeon_tier.py);
#   5. GearCheck's raid, tank and healer inputs (page stat weights, hit below the cap, tank weights, heal values, weight errors), the
#      add-on file;
#   6. the rankings and gear links, the pages, the checks.
# BelowNormal on 10 of 12 (RESERVE_CPUS=2). Log deep-runs/gear-phase-1118.log (steps), gear-phase-1118-out.log (output); markers
# deep-runs/g1118/. Resume: the same command. Stop: Stop-Process this bash process and its python children (never TaskStop).
#   bash _reference/data/deep-runs/gear_phase_1118.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/g1118
LOG=$L/gear-phase-1118.log
OUT=$L/gear-phase-1118-out.log
R=_reference/data/raidsim
D=_reference/data
HL=_reference/data/heallab
mkdir -p $M
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-2}" -Priority "${PRIORITY:-BelowNormal}" >> $LOG 2>&1
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {   # run <marker> <command...>: skipped when the marker exists; the marker is written on rc=0
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> $OUT
  "$@" >> $OUT 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
race() { python -u $R/run.py $1 --spec $2 --write && python -u $R/run.py $1 --spec $2 --env environments --write; }
entries() { python -c "import json,sys; print(' '.join(n for n, e in json.load(open('_reference/data/raidsim/specs.json', encoding='utf-8'))[sys.argv[1]].items() if isinstance(e, dict)))" "$1"; }
CLASSES="warrior paladin hunter rogue priest shaman mage warlock druid"
[ "$(git -C "$WOW_FOREVER_SIM" rev-parse --short=9 HEAD)" = "2e6e77d84" ] || { say "STOP: $WOW_FOREVER_SIM is not at 2e6e77d84"; exit 1; }
if [ ! -e $M/started ]; then
  say "waiting for the hybrid check (hybrid check done in hybrid-check-1118.log)"
  until grep -q "hybrid check done" $L/hybrid-check-1118.log 2>/dev/null; do sleep 120; done
  touch $M/started
fi
say "gear night start"

# ---- 1. standard, tank and healer sets
for c in $CLASSES; do
  run gear-opt-$c python -u $R/gear_opt.py $c --write --fresh || { say "STOP: gear_opt $c failed"; exit 1; }
  run gear-apply-$c python -u $R/gear_opt.py $c --apply || { say "STOP: gear_opt --apply $c failed"; exit 1; }
  case $c in warrior|paladin|druid) run gear-tank-$c python -u $R/tank_gear.py $c || say "WARNING: tank_gear $c failed";; esac
  case $c in priest|paladin|druid|shaman) run gear-heal-$c python -u $HL/heal_gear.py $c --fresh --jobs 4 || say "WARNING: heal_gear $c failed";; esac
  run gear-check-$c python -u $R/gear_check.py $c --pool || say "WARNING: gear_check $c lists items (gear-phase-1118-out.log)"
done
say "sets done"

# ---- 2. the ML records' tier sets and searches again
run ml-prep python -u $L/ml_prep_1118.py || { say "STOP: the ML records could not be prepared"; exit 1; }
for c in $CLASSES; do
  run ml-$c python -u $R/ml_pipeline.py $c --steps final || say "WARNING: the $c ML final steps failed"
done
run ml-builds python -u $R/ml_builds.py --builds || say "WARNING: ml_builds --builds failed"
run validate python -u $D/validate_builds.py || { say "STOP: validate_builds failed"; exit 1; }
say "ML done"

# ---- 3. every raid entry raced in the new standard sets
for c in $CLASSES; do
  for e in $(entries $c); do run race-$c-$e race $c $e || say "WARNING: the race of $c $e failed"; done
done
run tidy python -u $R/ml_builds.py --tidy-winners || say "WARNING: tidy failed"
run unused python -u $R/unused_abilities.py --write || say "WARNING: unused_abilities failed"
say "races done"

# ---- 4. the quests-and-dungeons tier
run dungeon python -u $R/dungeon_tier.py || say "WARNING: dungeon_tier failed"

# ---- 5. GearCheck's raid, tank and healer inputs
run psw python -u $R/page_stat_weights.py || say "WARNING: page_stat_weights failed"
run hit python -u $R/hit_below_cap.py || say "WARNING: hit_below_cap failed"
run tank-druid python -u $D/characters/tank_weights.py druid feral-bear-tank feral-combat-ml-tank "Feral Combat" || say "WARNING: tank_weights druid failed"
run tank-paladin python -u $D/characters/tank_weights.py paladin prot-tank protection-ml-tank Protection || say "WARNING: tank_weights paladin failed"
run tank-warrior python -u $D/characters/tank_weights.py warrior prot-tank protection-ml-tank Protection || say "WARNING: tank_weights warrior failed"
run heal-values python -u $HL/heal_values.py --jobs 8 || say "WARNING: heal_values failed"
run errors python -u $R/weight_errors.py --jobs 2 || say "WARNING: weight_errors failed"
run addon python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"

# ---- 6. rankings, gear links, pages, checks
run rank python -u $R/ml_builds.py --rank || say "WARNING: the rankings failed"
run regen python -u $D/rebuild.py --steps regen || say "WARNING: regen failed"
run guide-check python -u $D/level_guides.py --check || say "WARNING: the by-level guide check lists problems"
run guides python -u $D/guides.py --check --write || say "WARNING: guides --check lists passages to rewrite"
run page-lint python -u $D/page_lint.py --write || say "WARNING: page_lint lists findings"
say "all done (Claude: review, commit, push; message the Addons session: raid, tank and healer values moved)"
