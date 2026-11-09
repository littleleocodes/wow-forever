#!/usr/bin/env bash
# 2026-11-06 (self-audit at the warrior and druid class boundaries of the patch queue; page-audit K1). The priest is in no lane of the
# 2026-11-02 patch queue: the patch changed every class but the priest. The data capture date moved to 2026-11-03 for every class
# all the same, so render_modes.current_record ignores the priest's leveling records and reports of 2026-10-23, and its leveling index
# has said "No leveling numbers yet" since the 2026-11-02 checkpoint. Its rules were re-tuned from scratch on 2026-11-02 and its three
# open winners certified on 2026-11-03 (tonight_1102.sh), both on its current data (the 10-31 port), so no new level-60 search:
# this lane re-measures what the pages read. The open records from the 20-60 race on (priest_refresh_keys.py, then a plain
# fl_open_search.py run), the open builds, the orders, the races and reports: cls_steps of patch_1103.sh without the rules step.
# The file name ends in _1103.sh on purpose: rebalance.ps1 then treats its python as queue processes (cores and priority follow the
# balancer, 4 logical processors unless the user asked for more). Log: deep-runs/lane-p.log and patch-1103.log.
# Resume: the same command (markers deep-runs/p1103/priest-*).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/p1103
LOG=$L/patch-1103.log
FL=_reference/data/fightlab
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-8}"
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {   # run <marker> <log> <command...>: skipped when the marker exists; the marker is written on rc=0; returns rc
  local mk=$1 lg=$2; shift 2
  if [ -e "$M/$mk" ]; then return 0; fi
  "$@" >> "$L/$lg" 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
say "start priest refresh (open records from the 20-60 race on, builds, orders, races and reports)"
run priest-strip lane-p.log python -u $L/priest_refresh_keys.py || exit 1
run priest-open lane-p.log python -u $FL/fl_open_search.py priest --jobs 4 || exit 1
run priest-builds lane-p.log python -u _reference/data/open_builds.py priest --write --only leveling || exit 1
run priest-orders lane-p.log python -u _reference/data/order_repair.py priest --jobs 4 --write
run priest-race lane-p.log python -u _reference/data/rebuild.py priest --steps race,report
say "priest refresh done"
