#!/usr/bin/env bash
# raid_rest_1103.sh <class> [<ML spec>...]   (2026-11-06, the gear repair: page-audit.md J1-J4; user: "Go with your recs").
# The raid half of a class that has no lane in the 2026-11-02 patch queue (the priest: unchanged by the patch; the druid: its port,
# wowsims/forever #823, is not merged) after its gear was re-made: gear_repair_1103.sh, then every entry raced again in the new
# standard set (race and environments), the ML final steps of the named specs (the tier sets and the talent searches in them: the
# priest's Shadow and Discipline-Holy records ran in sets holding Ahn'Qiraj and Naxxramas quest rewards), the ML builds, validate,
# the entries once more, the tidy step and the unused-abilities page. No rotation re-tune: the game did not change for these classes
# on the simulator's side. Runs on the main clone (no WOW_FOREVER_SIM). Called by gear_redo_1103.sh.
# Resume: the same command (markers deep-runs/r1103/rest-<class>-*).
c=$1
shift
# 2026-11-07 (user: "Go with your recs"): re-pinned to ~/.wow-forever-tools/wowsims-forever-y at 16e85426c (upstream master, classes, racials and
# items on 1.60.1.70790 up to hotfix push 113715), like every raid lane. The header above says what this lane was written for.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/r1103
mkdir -p $M
LOG=$L/patch-1103.log
LG=raid-$c.log
R=_reference/data/raidsim
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {
  local mk=${1////_} lg=$2; shift 2
  if [ -e "$M/$mk" ]; then return 0; fi
  "$@" >> "$L/$lg" 2>&1; local rc=$?
  say "raid $mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return 0
}
race() { python -u $R/run.py $1 --spec $2 --write && python -u $R/run.py $1 --spec $2 --env environments --write; }
[ -n "$c" ] || { echo "usage: raid_rest_1103.sh <class> [<ML spec>...]"; exit 2; }
bash $L/gear_repair_1103.sh $c "rest-$c-*" || { say "raid: $c STOP, the gear repair failed (gear-repair.log)"; exit 1; }
E=$(python -c "import json,sys; print(' '.join(n for n, e in json.load(open('_reference/data/raidsim/specs.json', encoding='utf-8'))[sys.argv[1]].items() if isinstance(e, dict)))" $c)
say "raid: $c start (the gear repair's re-races; entries: $E)"
for e in $E; do run rest-$c-race-$e $LG race $c $e; done
if [ $# -gt 0 ] && [ ! -e "$M/rest-$c-ml-cleared" ]; then
  python -u $L/ml_clear.py $c "$@" >> $L/$LG 2>&1 && touch "$M/rest-$c-ml-cleared"
fi
for s in "$@"; do
  k=${s// /_}
  run rest-$c-ml-${k//\//_} $LG python -u $R/ml_pipeline.py $c --spec "$s" --steps final
done
run rest-$c-ml-builds $LG python -u $R/ml_builds.py $c --builds
run rest-$c-validate $LG python -u _reference/data/validate_builds.py
for e in $E; do run rest-$c-final-race-$e $LG race $c $e; done
run rest-$c-tidy $LG python -u $R/ml_builds.py $c --tidy-winners
run rest-$c-unused $LG python -u $R/unused_abilities.py $c --write
say "raid: $c done (rankings and gear links after the last raid lane; pages at the regen)"
