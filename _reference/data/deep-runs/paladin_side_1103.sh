#!/usr/bin/env bash
# paladin_side_1103.sh (2026-11-07; user: "Activate full power for the runs", then "Go with your recs"; page-audit L11): the paladin's leveling
# block next to the warlock's search, on 8 workers, instead of after it at 4. Lane C (patch_1103.sh) runs its classes one after the other
# and has no guard, so before this lane started its paladin markers and the queue's tail markers were touched by hand: rules-paladin,
# open-paladin, builds-paladin, orders-paladin, race-paladin, lev-path, own-rotation, validate, regen, guides. Lane C therefore logs "class
# paladin done" and "all done" without doing them: this lane does them, under side-* markers. The tail waits for the fixes lane's last step
# (fix-guides), so it never writes the builds while that lane regenerates the pages, and it runs once, on the final leveling state.
# Resume: the same command (markers deep-runs/p1103/side-*). Stop: Stop-Process this bash and its python children, then list the processes.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/p1103
LOG=$L/patch-1103.log
LG=lane-pal.log
FL=_reference/data/fightlab
D=_reference/data
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {   # run <marker> <command...>: skipped when the marker exists; the marker is written on rc=0; a failure stops the lane
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> "$L/$LG"
  "$@" >> "$L/$LG" 2>&1; local rc=$?
  say "$mk rc=$rc"
  if [ $rc -ne 0 ]; then say "paladin side lane STOP at $mk"; exit 1; fi
  touch "$M/$mk"
}
fresh() { if [ -e "$M/$1.started" ]; then echo ""; else touch "$M/$1.started"; echo "--fresh"; fi; }

say "paladin side lane start (8 workers, next to the warlock's search)"
run side-rules-paladin python -u $FL/rotation_opt.py paladin --fresh --write --jobs 8
run side-open-paladin python -u $FL/fl_open_search.py paladin $(fresh side-open-paladin) --jobs 8
run side-builds-paladin python -u $D/open_builds.py paladin --write --only leveling
run side-orders-paladin python -u $D/order_repair.py paladin --jobs 8 --write
run side-race-paladin python -u $D/rebuild.py paladin --steps race,report
say "class paladin done (side lane)"

until [ -e "$M/fix-guides" ]; do sleep 120; done
run side-lev-path python -u $D/raid_path_leveling.py druid paladin shaman warrior priest --write
run side-own-rotation python -u $FL/own_rotation_race.py --jobs 10
run side-validate python -u $D/validate_builds.py
run side-regen python -u $D/rebuild.py --steps regen
run side-guides python -u $D/guides.py --check --write
touch "$M/side-paladin-done"
say "paladin side lane done"
