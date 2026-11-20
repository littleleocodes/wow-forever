#!/usr/bin/env bash
# clip_retune_1120.sh (2026-11-20, the audit's decision on the channel clip delay: 100 ms, upstream's, sent by run.CLIP_MS since ~03:40;
# a pick that moves more than 0.5% gets its entry's rotation re-tuned at 100 before its ML step). Measured (full raid, 3,000 fights,
# seeds 1 / 2, 100 against 50 ms): Arcane -1.10% / -1.06% (its fresh tune runs in audit_raid_1120b.sh at 100), Shadow -0.73% / -0.75%,
# Wrack -0.56% / -0.50%. ML Affliction ran at 50 ms (lane 1, in-process), so after the Affliction entries take their shards
# (destro_prep_1120.sh) Wrack's rotation is re-tuned at 100 and ML Affliction runs again; Shadow's rotation is re-tuned (no ML queued).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/cr1120
LOG=$L/clip-retune-1120.log
OUT=$L/clip-retune-1120-out.log
R=_reference/data/raidsim
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
say "start"
run tune-shadow python -u $R/apl_opt.py priest --spec shadow-dps --setting raid --write || say "WARNING: tune shadow"
if [ ! -e $L/dp1120/shards-affliction ]; then
  say "waiting for the Affliction entries' shards (destro_prep_1120.sh, after ML Affliction)"
  until [ -e $L/dp1120/shards-affliction ]; do sleep 60; done
fi
run tune-wrack python -u $R/apl_opt.py warlock --spec affliction-wrack-raid --setting raid --write || say "WARNING: tune wrack"
run ml-affliction python -u $R/ml_pipeline.py warlock --spec Affliction --fresh --steps targets,gear,talents,rotations,final || say "WARNING: ML Affliction"
run race-affliction bash -c "python -u $R/run.py warlock --spec affliction-wrack-raid --write && python -u $R/run.py warlock --spec affliction-raid --write" || say "WARNING: race affliction"
say "all done"
