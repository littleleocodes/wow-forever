#!/bin/bash
# heal_values_1117.sh (2026-11-17): the healer stat values again after the night's gear repair re-made every healer set (heal_gear.py
# --fresh: priest 02:25, shaman 03:22, druid 05:41; paladin 2026-11-16 17:52); heal-values.json (2026-11-16 19:21) predates them, and the
# night's lane B re-measures it only when a spellbook moves. Before the night's wrap (addon_values.py reads it). BelowNormal, 10 of 12.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
LOG=$L/heal-values-1117.log
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve 2 -Priority BelowNormal >> $LOG 2>&1
echo "=== $(date +%F_%H:%M) heal values start" >> $LOG
python -u _reference/data/heallab/heal_values.py --jobs "${JOBS:-4}" >> $LOG 2>&1
rc=$?
echo "=== $(date +%F_%H:%M) heal values rc=$rc" >> $LOG
exit $rc
