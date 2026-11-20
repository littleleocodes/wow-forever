#!/bin/bash
# The mage tier records made by hand this morning (tiers-frost-1120b, tiers-arcfrost-1120b) again in the lanes' environment: the -y checkout,
# racials off (2026-11-20, search-improvements 0x: manual runs had used racials on). The audit session's request.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8 WOW_FOREVER_NO_RACIALS=1 WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs; LOG=$L/tiers-redo-1120.log; R=_reference/data/raidsim
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve 2 -Priority BelowNormal >> $LOG 2>&1
echo "=== $(date +%F_%H:%M) start" >> $LOG
python -u $R/pick_tiers.py mage Frost --entry frost-raid --build frost-med-raid >> $LOG 2>&1 || echo "WARNING: tiers frost" >> $LOG
python -u $R/dungeon_tier.py mage --spec Frost --fresh >> $LOG 2>&1 || echo "WARNING: dungeon frost" >> $LOG
python -u $R/pick_tiers.py mage "Hybrid Arcane/Frost" --entry arcane-frost-raid --build arcane-frost-open-raid >> $LOG 2>&1 || echo "WARNING: tiers arcfrost" >> $LOG
python -u $R/dungeon_tier.py mage --spec "Hybrid Arcane/Frost" --fresh >> $LOG 2>&1 || echo "WARNING: dungeon arcfrost" >> $LOG
echo "=== $(date +%F_%H:%M) all done" >> $LOG
