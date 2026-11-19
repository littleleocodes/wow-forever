#!/usr/bin/env bash
# pvp_holy_gear_1118.sh (2026-11-18): the Holy paladin's blind-spot check and follow-ups again after the gear fix. blind_spots.evaluate
# had dueled the Holy winner in caster gear only (75.0%), where the search had raced both rows and kept melee (79.4% on the same
# duels). Low power mode (user, 2026-11-18 17:3x: "go low power mode"): Idle on 2 of 12 logical processors, 2 workers.
#   bash _reference/data/deep-runs/pvp_holy_gear_1118.sh      log deep-runs/pvp-holy-gear-1118.log
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
LOG=$L/pvp-holy-gear-1118.log
D=_reference/data/duellab
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-10}" -Priority "${PRIORITY:-Idle}" >> $LOG 2>&1
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
say "start"
python -u $D/blind_spots.py paladin:Holy --fresh --workers 2 >> $LOG 2>&1 || { say "STOP: check rc=$?"; exit 1; }
say "check done"
python -u $D/blind_followups.py improve --only paladin:Holy --date 2026-11-18 --workers 2 >> $LOG 2>&1 || { say "STOP: improve rc=$?"; exit 1; }
python -u $D/blind_followups.py battleground --only paladin:Holy --date 2026-11-18 --workers 2 >> $LOG 2>&1 || { say "STOP: battleground rc=$?"; exit 1; }
say "follow-ups done"
python -u $D/render_pvp_research.py paladin >> $LOG 2>&1
python -u _reference/data/render_modes.py >> $LOG 2>&1
python -u _reference/data/page_lint.py --write >> $LOG 2>&1
say "all done (Claude: review the Holy paladin's PvP numbers, commit, push)"
