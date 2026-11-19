#!/usr/bin/env bash
# pvp_subtlety_1118.sh (2026-11-18; user: "Drop it"): Subtlety's PvP build holds Hemorrhage only (signature_spells.json modes.pvp).
# The round-2 search with Death Mark required ran from one start and won 40.2% of duels against the field; the round-1 build
# without it wins 50.6% on the same duels. Runs after pvp_holy_gear_1118.sh (both write blind-spots.json and the round's results):
# the search again for Subtlety (round r2 settings; every start is legal now), its blind-spot check and follow-ups, the pages.
# Low power mode (user, 2026-11-18 17:3x): Idle on 2 of 12 logical processors, 2 workers.
#   bash _reference/data/deep-runs/pvp_subtlety_1118.sh      log deep-runs/pvp-subtlety-1118.log
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
LOG=$L/pvp-subtlety-1118.log
D=_reference/data/duellab
WF=$L/pvp-r2/workers-low
mkdir -p $L/pvp-r2
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-10}" -Priority "${PRIORITY:-Idle}" >> $LOG 2>&1
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
say "waiting for the Holy paladin's re-run (all done or STOP in pvp-holy-gear-1118.log)"
until grep -q "all done\|STOP" $L/pvp-holy-gear-1118.log 2>/dev/null; do sleep 60; done
echo "${WORKERS:-2}" > $WF
if [ -e $D/search/rogue-subtlety.json ] && python -c "import json, sys; r = json.load(open(sys.argv[1], encoding='utf-8')); sys.exit(0 if 'Death Mark' in r['settings'].get('signature', []) else 1)" $D/search/rogue-subtlety.json; then
  mv $D/search/rogue-subtlety.json $L/pvp-r2/rogue-subtlety-death-mark-1118.json
  say "the Death Mark record moved to deep-runs/pvp-r2/rogue-subtlety-death-mark-1118.json"
fi
say "search"
python -u $D/pvp_search_all.py rogue --round r2 --workers-file $WF >> $LOG 2>&1 || { say "STOP: search rc=$?"; exit 1; }
say "check"
python -u $D/blind_spots.py rogue:Subtlety --fresh --workers ${WORKERS:-2} >> $LOG 2>&1 || { say "STOP: check rc=$?"; exit 1; }
python -u $D/blind_followups.py improve --only rogue:Subtlety --date 2026-11-18 --workers ${WORKERS:-2} >> $LOG 2>&1 || { say "STOP: improve rc=$?"; exit 1; }
python -u $D/blind_followups.py battleground --only rogue:Subtlety --date 2026-11-18 --workers ${WORKERS:-2} >> $LOG 2>&1 || { say "STOP: battleground rc=$?"; exit 1; }
say "follow-ups done"
python -u $D/render_pvp_research.py rogue >> $LOG 2>&1
python -u _reference/data/render_modes.py >> $LOG 2>&1
python -u _reference/data/page_lint.py --write >> $LOG 2>&1
say "all done (Claude: review Subtlety's PvP build, commit, push)"
