#!/usr/bin/env bash
# gear_repair_1103.sh <class> "<marker patterns>"   (2026-11-06; user, 2026-11-06: "Go with your recs": the gear repair before any
# raid lane; page-audit.md J1-J4, CLAUDE.md "The item database moves under the gear tools").
# The first step of every raid lane of the 2026-11-02 patch queue (raid_<class>_1103.sh calls it after its checkout check and
# inherits it its WOW_FOREVER_SIM). Once per class (marker r1103/gear-<class>):
#   1. the class's standard sets from the dated pool (gear_opt.py <class> --write --fresh, then <class> --apply): all 14 listed one or two
#      items the simulator dropped on 2026-10-30, and every run since had those slots empty;
#   2. every tier set of the class's ML records again (gear_tiers.py --remake --classes <class> --fresh): 49 held a rank-14 PvP weapon,
#      19 a later raid's quest rewards, 67 the Signet Ring of the Bronze Dragonflight (gear_opt.LATER_FACTIONS since this day);
#   3. the tank sets (tank_gear.py: warrior, paladin, druid) and the healer sets (heallab/heal_gear.py), which listed dropped items too;
#   4. gear_check.py <class> --pool: no entry set may list an item the database lacks (run.check_bench_stderr stops such a run);
#   5. the lane's own markers (the patterns) are removed: its races, re-tunes, searches and ML final steps were made in the old sets
#      and run again.
# A failed step stops the lane (exit 1; patch-1103.log says which). Resume: the lane's own command (markers r1103/gear-*-<class>).
c=$1
pats=$2
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/r1103
LOG=$L/patch-1103.log
R=_reference/data/raidsim
GL=$L/gear-repair.log
mkdir -p $M
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
step() {   # step <marker> <command...>: skipped when the marker exists; the marker is written on rc=0; returns rc
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> $GL
  "$@" >> $GL 2>&1; local rc=$?
  say "raid $mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
[ -n "$c" ] || { echo "usage: gear_repair_1103.sh <class> \"<marker patterns>\""; exit 2; }
[ -e "$M/gear-$c" ] && exit 0
say "raid: $c gear repair start (standard sets, tier sets, tank and healer sets; checkout $(basename "${WOW_FOREVER_SIM:-wowsims-forever}"))"
# one class at a time through the standard sets: gear_opt.py's record (raidsim/gear-opt.json) and --apply are shared by every class,
# and two lanes may reach this step together. The lock is a directory holding the holder's pid; a holder that is gone loses it.
until mkdir "$M/gear.lock" 2>/dev/null; do
  holder=$(cat "$M/gear.lock/pid" 2>/dev/null)
  if [ -n "$holder" ] && ! kill -0 "$holder" 2>/dev/null; then rm -rf "$M/gear.lock"; continue; fi
  sleep 30
done
echo $$ > "$M/gear.lock/pid"
step gear-opt-$c python -u $R/gear_opt.py $c --write --fresh && step gear-apply-$c python -u $R/gear_opt.py $c --apply
rc=$?
rm -rf "$M/gear.lock"
[ $rc -eq 0 ] || exit 1
step gear-tiers-$c python -u $R/gear_tiers.py --remake --classes $c --fresh || exit 1
case $c in
  warrior|paladin|druid) step gear-tank-$c python -u $R/tank_gear.py $c || exit 1 ;;
esac
case $c in
  priest|paladin|druid|shaman) step gear-heal-$c python -u _reference/data/heallab/heal_gear.py $c --fresh --jobs 4 || exit 1 ;;
esac
step gear-check-$c python -u $R/gear_check.py $c --pool || exit 1
for p in $pats; do rm -f "$M"/$p; done
touch "$M/gear-$c"
say "raid: $c gear repair done; the lane's steps run again in the new sets"
exit 0
