#!/bin/bash
# pvp_round2.sh (2026-11-17; user, on the PvP report's recommendations: "Go with all your recommendations"). PvP round 2, after the
# eat-and-drink lane's numbers (fl_rest_1117.sh: "numbers done" in rest-1117.log; the user's CPU order: the night, its commit, the
# rest lane, then this):
#   1. the field matrix on round 2's engine (pets answered: melee swings at a pet in reach, Hibernate, Scare Beast, Polymorph, Banish,
#      Fel Domination's re-summon; Bestial Wrath's immunity) -> _reference/pvp-matchups.md;
#   2. the search on every tree (pvp_search_all.py --round r2): tier chains, the signature talents kept, the Holy paladin's gear raced
#      both ways, PATIENCE 6, the round-1 winners, improved builds and battleground versions as starts (duellab/seeds/r2/);
#   3. the blind-spot check (blind_spots.py --fresh: two payments a candidate);
#   4. the follow-ups (blind_followups.py improve, battleground -> duellab/results-<date>.json);
#   5. the research pages' Duel lab section (render_pvp_research.py).
# BelowNormal on 10 of 12 (RESERVE_CPUS=2). Log deep-runs/pvp-round2.log; markers deep-runs/pvp-r2/. Resume: the same command (the
# search skips trees done in round r2; the check, with --fresh only on its first start, resumes per tree). No commit: Claude reviews,
# then writes the PvP player pages (duel build and battleground version per spec).
# Stop: Stop-Process this bash process and its python children (never TaskStop).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/pvp-r2
LOG=$L/pvp-round2.log
DL=_reference/data/duellab
mkdir -p $M
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-2}" -Priority "${PRIORITY:-BelowNormal}" >> $LOG 2>&1
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {   # run <marker> <command...>: skipped when the marker exists; the marker is written on rc=0
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> $LOG
  "$@" >> $LOG 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
if [ ! -e $M/started ]; then
  say "waiting for the eat-and-drink lane's numbers (numbers done in rest-1117.log)"
  until grep -q "numbers done" $L/rest-1117.log 2>/dev/null; do sleep 120; done
  touch $M/started
fi
say "PvP round 2 start"
run matrix python -u $DL/pvp_field.py --matrix --n 200 --workers 10 --write || { say "STOP: the matrix failed"; exit 1; }
echo 10 > $L/pvp1115/workers
run search python -u $DL/pvp_search_all.py --round r2 || { say "STOP: the search failed"; exit 1; }
if [ ! -e $M/check-started ]; then   # round 1's record kept as blind-spots-r1.json; round 2's starts empty (and resumes per tree)
  [ -e $DL/blind-spots.json ] && mv $DL/blind-spots.json $DL/blind-spots-r1.json
  touch $M/check-started
fi
run check python -u $DL/blind_spots.py --workers 10 || { say "STOP: the blind-spot check failed"; exit 1; }
run improve python -u $DL/blind_followups.py improve --workers 10 || say "WARNING: improve failed"
run battleground python -u $DL/blind_followups.py battleground --workers 10 || say "WARNING: battleground failed"
run pages python -u $DL/render_pvp_research.py || say "WARNING: the research pages failed"
say "all done (review; then the PvP player pages: duel build and battleground version per spec)"
