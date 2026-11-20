#!/usr/bin/env bash
# audit_raid_1120d.sh (2026-11-20 ~11:00): the raid lane under "Simulator build first" (the user's decision, first-hand, and the audit's
# plan): the simulator's own build is the page's pick unless ours leads by 0.5% on two seeds (raidsim/pick_decide.py); short checks
# (raidsim/talent_opt.py --setting raid --rounds 2 from the pick) instead of the multi-hour ML searches; the gear tiers for each pick
# (raidsim/pick_tiers.py, then dungeon_tier.py). It replaces audit_raid_1120c.sh, stopped at a step boundary (ML Frost done; ML
# Arcane-Frost stopped after 15 min: it had targeted frost-raid). Every entry is raced before a check targets it. A short check that
# keeps 0.5% or more is flagged ESCALATE in the log for Claude (the full search then). BelowNormal on 10 of 12.
# Log deep-runs/audit-raid-1120d.log, output audit-raid-1120d-out.log, markers deep-runs/b1120/ (shared with 1120b/c).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/b1120
LOG=$L/audit-raid-1120d.log
OUT=$L/audit-raid-1120d-out.log
R=_reference/data/raidsim
D=_reference/data
mkdir -p $M
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve 2 -Priority BelowNormal >> $LOG 2>&1
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> $OUT
  "$@" >> $OUT 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
race() {   # race <marker> <class> <entry>: the entry's race and environments (a check never targets an entry not raced)
  run $1 bash -c "python -u $R/run.py $2 --spec $3 --write && python -u $R/run.py $2 --spec $3 --env environments --write" || say "WARNING: race $2 $3"
}
pick_of() {   # pick_of <class> <entry>: the pick pick_decide.py recorded
  python -c "import json,sys; print(json.load(open('$R/pick-decisions.json',encoding='utf-8'))[sys.argv[1]]['pick'])" "$1/$2"
}
check() {   # check <marker> <class> <entry> <start build>: the short check; ESCALATE when it keeps 0.5% or more
  local cand=$2/research/raid/raidsim/candidates/check-$3.json
  run $1 python -u $R/talent_opt.py $2 --spec $3 --start $4 --setting raid --rounds 2 --write $cand || say "WARNING: check $2 $3"
  python - "$cand" "$4" >> $LOG 2>&1 <<'PY'
import json, sys
try:
    c = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception:
    sys.exit(0)
s = c.get("search") or {}
g = s.get("gain") if s.get("gain") is not None else ((s.get("final_dps") or 0) / (s.get("start_dps") or 1) - 1 if s.get("start_dps") else None)
moves = s.get("moves") or []
tag = "ESCALATE" if (g or 0) >= 0.005 else "confirmed"
print(f"=== short check {sys.argv[2]}: {tag} (gain {g if g is None else f'{g:+.2%}'}; {len(moves)} move(s) kept)")
PY
}
tiers() {   # tiers <marker> <class> "<spec>" <entry> <build>
  run $1 python -u $R/pick_tiers.py $2 "$3" --entry $4 --build $5 || say "WARNING: pick_tiers $2 $3"
  run d$1 python -u $R/dungeon_tier.py $2 --spec "$3" --fresh || say "WARNING: dungeon_tier $2 $3"
}
say "start"
# 1. Frost: ML Frost's winner (written by ml_builds as frost-ml-raid) against the simulator's Frost Med
run mlb-mage bash -c "python -u $R/ml_builds.py mage --builds && python -u $D/validate_builds.py && python -u $D/render_builds.py" || say "WARNING: ml_builds mage"
race race-frost mage frost-raid
run pick-frost python -u $R/pick_decide.py mage frost-raid --sim frost-med-raid --ours frost-ml-raid || say "WARNING: pick frost"
P=$(pick_of mage frost-raid)
say "Frost pick: $P"
if [ "$P" = "frost-med-raid" ]; then tiers tiers-frost mage Frost frost-raid frost-med-raid; fi
# 2. Arcane-Frost (no simulator build; its own entry, raced first)
race race-arcfrost mage arcane-frost-raid
check check-arcfrost mage arcane-frost-raid arcane-frost-open-raid
tiers tiers-arcfrost mage "Hybrid Arcane/Frost" arcane-frost-raid arcane-frost-open-raid
# 3. Arcane: the fresh tune on arcaneFireFill (guarded), the pick, the check, the tiers
run tune-arcane python -u $R/apl_opt.py mage --spec arcane-dps --setting raid --fresh --write || say "WARNING: tune arcane"
race race-arcane mage arcane-dps
run pick-arcane python -u $R/pick_decide.py mage arcane-dps --sim arcane-fire-raid --ours arcane-open-raid arcane-blast-raid || say "WARNING: pick arcane"
P=$(pick_of mage arcane-dps)
say "Arcane pick: $P"
check check-arcane mage arcane-dps "$P"
tiers tiers-arcane mage Arcane arcane-dps "$P"
# 4. Destruction: upstream's package in destro-raid (881 against our best 813 in sb-raid)
race race-destro warlock destro-raid
run tune-destro python -u $R/apl_opt.py warlock --spec destro-raid --setting raid --fresh --write || say "WARNING: tune destro"
check check-destro warlock destro-raid destruction-succubus-raid
tiers tiers-destro warlock Destruction destro-raid destruction-succubus-raid
# 5. Feral: the fresh tune on upstream's current adaptive (the pick stays ours: 931 against the simulator's Cat 920)
run tune-feral python -u $R/apl_opt.py druid --spec feral-cat-dps --setting raid --fresh --write || say "WARNING: tune feral"
# 6. Frostfire: upstream's ffb rotation and its FFB build (the audit's (d))
race race-ffb mage frostfire-raid
check check-ffb mage frostfire-raid frostfire-ffb-raid
tiers tiers-ffb mage "Hybrid Fire/Frost" frostfire-raid frostfire-ffb-raid
# 7. Hunters: Survival with the simulator's melee build and its Raptor (the audit's (a)); Beast Mastery; Marksmanship (the pet
#    build's check; the page's pick is the Lone Wolf build); Beast-Marks
race race-svpet hunter survival-pet-raid
check check-svpet hunter survival-pet-raid survival-raptor-raid
tiers tiers-sv hunter Survival survival-pet-raid survival-raptor-raid
check check-bm hunter bm-raid beast-mastery-ml-raid
tiers tiers-bm hunter "Beast Mastery" bm-raid beast-mastery-ml-raid
run tune-mm-raid python -u $R/apl_opt.py hunter --spec mm-raid --setting raid --write || say "WARNING: tune mm-raid"
check check-mm hunter mm-raid marksmanship-ml-raid
tiers tiers-mm hunter Marksmanship mm-lonewolf-raid mm-lone-wolf-raid
check check-bmmm hunter bm-raid beast-marks-ml-raid
tiers tiers-bmmm hunter "Hybrid Beast Mastery/Marksmanship" bm-raid beast-marks-ml-raid
# 8. Shockadin: the simulator's Holy Shock build under our rotation (the audit's (b))
race race-shock paladin shockadin-raid
tiers tiers-shock paladin "Hybrid Holy/Retribution" shockadin-raid shockadin-holy-shock-raid
# 9. races, builds, values, pages
run race-all bash -c "python -u $R/run.py --all --write && python -u $R/run.py --all --env environments --write" || say "WARNING: race all"
run ml-builds bash -c "python -u $R/ml_builds.py --builds && python -u $D/validate_builds.py && python -u $D/render_builds.py && python -u $R/ml_builds.py --rank" || say "WARNING: ml_builds"
run unused python -u $R/unused_abilities.py --write || say "WARNING: unused_abilities"
run psw-all python -u $R/page_stat_weights.py --all || say "WARNING: page_stat_weights --all"
run pages python -u $D/render_modes.py || say "WARNING: render_modes"
run page-lint python -u $D/page_lint.py --write || say "WARNING: page_lint"
say "all done (Claude: the ESCALATE lines, Survival's core share, review; final_1120.sh waits for this and the tank lane)"
