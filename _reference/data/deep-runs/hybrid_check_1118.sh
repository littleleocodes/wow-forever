#!/usr/bin/env bash
# hybrid_check_1118.sh (2026-11-18; user: "how would we go about checking hybrid builds within classes? Ones that don't need rules but
# may be better than others. For example a melee hunter build", then "Let's queue it"): _reference/data/hybrid_check.py's raid and
# leveling parts for every class, once PvP round 2 has ended (wf_enh_1117.sh writes "PvP round 2 exited" in wf-enh-1117.log).
# A check only: it writes _reference/data/hybrid-check.json and _reference/hybrid-check.md, no build. BelowNormal on 10 of 12
# (RESERVE_CPUS=2). Log deep-runs/hybrid-check-1118.log. Stop: Stop-Process this bash process and its python children.
#   bash _reference/data/deep-runs/hybrid_check_1118.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
LOG=$L/hybrid-check-1118.log
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-2}" -Priority "${PRIORITY:-BelowNormal}" >> $LOG 2>&1
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
say "waiting for PvP round 2 (\"PvP round 2 exited\" in wf-enh-1117.log)"
until grep -q "PvP round 2 exited" $L/wf-enh-1117.log 2>/dev/null; do sleep 120; done
say "start"
python -u _reference/data/hybrid_check.py --raid --write >> $LOG 2>&1; say "raid rc=$?"
python -u _reference/data/hybrid_check.py --leveling --jobs 8 --write >> $LOG 2>&1; say "leveling rc=$?"
say "hybrid check done (Claude: review _reference/hybrid-check.md)"
