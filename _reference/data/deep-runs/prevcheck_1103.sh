#!/usr/bin/env bash
# 2026-11-06: one read-only check, named *_1103.sh so rebalance.ps1 keeps it on the queue's processors (see fightlab/prev_check.py).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-8}"
python -u $L/fightlab/prev_check.py 3 > $L/prev-check.log 2>&1
