#!/bin/bash
# pvp_blind_1117.sh (2026-11-17): the PvP plan's blind-spot check (step 4, user 2026-11-16: "make sure we double check everything like
# that at the end"): duellab/blind_spots.py for every tree's search winner. BelowNormal on 10 of 12 logical processors (full power).
# Log deep-runs/pvp-blind-1117.log; record duellab/blind-spots.json (resumes: the same command skips the trees in the record).
# Stop: Stop-Process this bash process and its python children (never TaskStop).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
LOG=$L/pvp-blind-1117.log
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-2}" -Priority "${PRIORITY:-BelowNormal}" >> $LOG 2>&1
echo "=== $(date +%F_%H:%M) blind-spot check start" >> $LOG
python -u _reference/data/duellab/blind_spots.py --workers "${WORKERS:-10}" "$@" >> $LOG 2>&1
rc=$?
echo "=== $(date +%F_%H:%M) blind-spot check rc=$rc" >> $LOG
exit $rc
