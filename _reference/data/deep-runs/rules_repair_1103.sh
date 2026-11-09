#!/usr/bin/env bash
# 2026-11-06 (self-audit at the end of lane A of the patch queue; search-improvements.md 0e). The queue's rules step
# (rotation_opt.py <class> --fresh --write) tunes a class pipeline's rotations only. The rule files of the other leveling rotations
# were left as they were before their class's module was ported to the 2026-11-02 patch (2026-11-03): mage arcane-leveling and
# barrage-frost-leveling, rogue subtlety-leveling (tuned before the rework and before Death Mark became a required spell: a continued
# tune finds DEATH_MARK_CP = 1, +0.7% at levels 20-60 and +2.3% at 60), warlock demonology-leveling and destruction-leveling, paladin
# holy-leveling; the warrior's and the paladin's prot-leveling have no rule file and were not tried again. The priest's two (ported
# 2026-10-31) are left out: Shadow's rules from scratch on 2026-11-02 gave the time of before its port.
# Part A, this script: fightlab/rules_retune.py per rotation on its page pick (from scratch and continued from the saved file; the
# fastest set is installed only when it beats the saved rules by 0.3% on seed 3). The paladin's two run before lane C reaches
# open-paladin; the warlock's Demonology file waits until lane C has saved that rotation (its one-tree search comes later);
# Destruction was tuned apart, before its search started. Part B, by hand afterwards: for every rotation whose rules changed, the
# open record from the 20-60 race on, builds, races and reports (page-audit.md B24's remedy).
# The file name ends in _1103.sh on purpose: rebalance.ps1 then treats its python as queue processes. Log: deep-runs/lane-r.log and
# patch-1103.log. Resume: the same command (markers deep-runs/p1103/rules2-*).
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
tune() { run rules2-$1-$2 lane-r.log python -u $FL/rules_retune.py $1 $2 $3 --jobs 4; }   # tune <class> <rotation> <build>
say "start rules repair (the rotations the rules step skipped)"
tune rogue subtlety-leveling subtlety-open-leveling
tune paladin holy-leveling holy-leveling
tune paladin prot-leveling protection-leveling
tune mage arcane-leveling arcane-open-leveling
tune mage barrage-frost-leveling arcane-frost-open-leveling
tune warrior prot-leveling protection-open-leveling
until grep -q "warlock demonology-leveling: open winner" $L/lane-c.log; do sleep 120; done
tune warlock demonology-leveling demonology-leveling
say "rules repair: tunes done"
