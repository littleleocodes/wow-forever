#!/usr/bin/env bash
# hunter_redo_1120.sh (2026-11-20 evening): the raid lane's hunter steps again on the files with Hunter's Mark (D11: the converted
# official rotations had dropped both mark casts; our rotations lacked the recast or the mark altogether; mark_cast_fix_1120.py,
# mark_lines_1120.py). The audit session's step 3: check-bm, the Marksmanship rotation tune from the fixed base, check-mm, check-bmmm,
# check-svpet, the hunter tiers; plus Beast-Survival's short check (Expose Prey 1 -> 2 may pay with the mark) and its exact filler pass.
# The survival-pet-raid steps wait for deep-runs/hr1120/svpet-decided (Claude's rotation decision from the parity race), the re-race of
# the hunter entries for the lane's race-all. Same commands as audit_raid_1120d.sh. BelowNormal on 10 of 12.
# Log deep-runs/hunter-redo-1120.log, output hunter-redo-1120-out.log, markers deep-runs/hr1120/.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/hr1120
LOG=$L/hunter-redo-1120.log
OUT=$L/hunter-redo-1120-out.log
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
check() {   # check <marker> <class> <entry> <start build>: the short check; ESCALATE when it keeps 0.5% or more
  local cand=$2/research/raid/raidsim/candidates/check-$3-$4.json
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
# Beast Mastery, the Marksmanship rotation from the fixed base, Marksmanship, Beast-Marks
check check-bm hunter bm-raid beast-mastery-ml-raid
tiers tiers-bm hunter "Beast Mastery" bm-raid beast-mastery-ml-raid
run tune-mm-raid python -u $R/apl_opt.py hunter --spec mm-raid --setting raid --write || say "WARNING: tune mm-raid"
check check-mm hunter mm-raid marksmanship-ml-raid
check check-mmlw hunter mm-lonewolf-raid mm-lone-wolf-raid
tiers tiers-mm hunter Marksmanship mm-lonewolf-raid mm-lone-wolf-raid
check check-bmmm hunter bm-raid beast-marks-ml-raid
tiers tiers-bmmm hunter "Hybrid Beast Mastery/Marksmanship" bm-raid beast-marks-ml-raid
# Beast-Survival: Expose Prey back (1 point); the short check tries 1 -> 2; then the exact filler pass on whatever it keeps
check check-bsv hunter melee-dps beast-survival-open-raid
run fill-bsv python -u $D/deep-runs/credited_fillers_1120.py --out $R/credited-fillers-mark.json --only beast-survival-open-raid || say "WARNING: filler pass bsv"
# Survival (survival-pet-raid): after Claude's rotation decision
if [ ! -e "$M/svpet-decided" ]; then
  say "waiting for hr1120/svpet-decided (the survival-pet-raid rotation decision)"
  until [ -e "$M/svpet-decided" ]; do sleep 60; done
fi
check check-svpet hunter survival-pet-raid survival-raptor-raid
tiers tiers-sv hunter Survival survival-pet-raid survival-raptor-raid
# the hunter entries raced again once the lane's race-all is through (it raced them on the fixed files, before these checks)
if ! grep -q "race-all rc=" $L/audit-raid-1120d.log 2>/dev/null; then
  say "waiting for the lane's race-all"
  until grep -q "race-all rc=" $L/audit-raid-1120d.log 2>/dev/null; do sleep 60; done
fi
for e in bm-raid mm-raid mm-lonewolf-raid melee-dps survival-pet-raid; do
  run race-$e bash -c "python -u $R/run.py hunter --spec $e --write && python -u $R/run.py hunter --spec $e --env environments --write" || say "WARNING: race hunter $e"
done
run play-hunter python -u $R/play_check.py hunter --write || say "WARNING: play check hunter"
say "all done (Claude: ESCALATE lines, the filler pass record, the play check; then the hunter guides)"
