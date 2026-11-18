#!/usr/bin/env bash
# wf_enh_1117.sh (2026-11-17; user: "After eat-and-drink (Recommended)" to the Windfury Totem fix). The simulator's full raid
# (wowsims/forever 2e6e77d84) gives an Enhancement shaman a party's Windfury Totem procs on top of its own Windfury Weapon, about 9% of
# the build's damage there; Forever's Windfury Weapon tooltip (rank 4, 16362): "When applied to main hand, disables any benefit you
# personally receive from Windfury Totem". Runs after the eat-and-drink lane's numbers ("numbers done" in rest-1117.log) and before
# PvP round 2, which it starts at its end (pvp_round2.sh's own waiter was stopped at 17:5x for this):
#   1. specs.json: the shaman enhancement-dps entry's buffs_off gets windfury_totem (wf_buffs_off_1117.py);
#   2. the entry raced again (dummy and environments); wf_decide_1117.py compares each build's full-raid DPS with the committed record;
#   3. only when a build now beats the page's pick (enhancement-open-raid) by 0.5% in a full raid (the rule told to the user): the raid
#      rotation re-tuned, the entry's family search again (the other entries keep theirs), open builds;
#   4. the Enhancement and hybrid ML finals (the gear-tier numbers and GearCheck's raid builds), ML builds, validate, the final race,
#      tidy, unused abilities; GearCheck's raid inputs (page stat weights and hit for the shaman, the standard errors), the add-on
#      values file, the rankings;
#   5. PvP round 2 (pvp_round2.sh, in this process).
# The pages: the eat-and-drink lane's regen after Claude's texts (marker fr1117/texts-done), which Claude touches once "Windfury numbers
# done" is in this log. BelowNormal on 10 of 12 (RESERVE_CPUS=2). Log deep-runs/wf-enh-1117.log (steps), wf-enh-1117-out.log (output);
# markers deep-runs/wf1117/. Resume: the same command. Stop: Stop-Process this bash process and its python children (never TaskStop).
#   bash _reference/data/deep-runs/wf_enh_1117.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/wf1117
LOG=$L/wf-enh-1117.log
OUT=$L/wf-enh-1117-out.log
R=_reference/data/raidsim
D=_reference/data
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
race() { python -u $R/run.py shaman --spec enhancement-dps --write && python -u $R/run.py shaman --spec enhancement-dps --env environments --write; }
[ "$(git -C "$WOW_FOREVER_SIM" rev-parse --short=9 HEAD)" = "2e6e77d84" ] || { say "STOP: $WOW_FOREVER_SIM is not at 2e6e77d84"; exit 1; }
if [ ! -e $M/started ]; then
  say "waiting for the eat-and-drink lane's numbers (numbers done in rest-1117.log)"
  until grep -q "numbers done" $L/rest-1117.log 2>/dev/null; do sleep 120; done
  touch $M/started
fi
say "Windfury fix start"
run buffs-off python -u $L/wf_buffs_off_1117.py || { say "STOP: the buffs_off edit failed"; exit 1; }
run race race || { say "STOP: the re-race failed"; exit 1; }
run decide python -u $L/wf_decide_1117.py || { say "STOP: the comparison failed"; exit 1; }
if [ -e $M/search-needed ]; then
  say "search: $(cat $M/search-needed)"
  run apl python -u $R/apl_opt.py shaman --spec enhancement-dps --write --setting raid --rounds 8 --lookahead 0 || say "WARNING: the rotation re-tune failed; its rotation stays"
  run race-tuned race || { say "STOP: the race after the re-tune failed"; exit 1; }
  run family-prep python -u $L/wf_prep_1117.py family || { say "STOP: the family record could not be prepared"; exit 1; }
  run family python -u $R/family_search.py shaman --entry enhancement-dps || { say "STOP: the family search failed"; exit 1; }
  run open-builds python -u $D/open_builds.py shaman --write --only raid --race || say "WARNING: open_builds failed"
else
  say "no search: $(cat $M/no-search 2>/dev/null)"
fi
run ml-prep python -u $L/wf_prep_1117.py ml || { say "STOP: the ML records could not be prepared"; exit 1; }
run ml-Enhancement python -u $R/ml_pipeline.py shaman --spec "Enhancement" --steps final || say "WARNING: the Enhancement ML final failed"
run ml-Hybrid python -u $R/ml_pipeline.py shaman --spec "Hybrid Elemental/Enhancement" --steps final || say "WARNING: the hybrid ML final failed"
run ml-builds python -u $R/ml_builds.py shaman --builds || say "WARNING: ml_builds --builds failed"
run validate python -u $D/validate_builds.py || { say "STOP: validate_builds failed"; exit 1; }
run final-race race || say "WARNING: the final race failed"
run tidy python -u $R/ml_builds.py shaman --tidy-winners || say "WARNING: tidy failed"
run unused python -u $R/unused_abilities.py shaman --write || say "WARNING: unused_abilities failed"
run psw python -u $R/page_stat_weights.py shaman || say "WARNING: page_stat_weights failed"
run hit python -u $R/hit_below_cap.py shaman || say "WARNING: hit_below_cap failed"
run errors python -u $R/weight_errors.py --jobs 2 || say "WARNING: weight_errors failed"
run addon python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"
run rank python -u $R/ml_builds.py --rank || say "WARNING: the rankings failed"
say "Windfury numbers done (Claude: review, then touch fr1117/texts-done for the pages; message the Addons session)"
bash $L/pvp_round2.sh
say "PvP round 2 exited rc=$?"
