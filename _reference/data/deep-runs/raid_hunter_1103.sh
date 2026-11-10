#!/usr/bin/env bash
# 2026-11-03 (user: "wait for the sim to merge"): wowsims/forever #824 (merged 22:46Z; it took the closed #838's branch, hotfix push 113578)
# is the hunter's port: the live hotfix's shot buffs and the 70755 spell data up to push 113596 (Barrage 15%, Lightning Reflexes 15%,
# Counterattack, the Trueshot Aura and Resourcefulness texts). Our 70707 -> 70753 hunter tree: names and rank caps identical to the
# simulator's (checked 2026-11-03 22:40); every number is read from the regenerated spell data. Number changes, no tree rework: the
# paladin's treatment (re-tunes, certificate and structural ranking, the ML final step), not the full family search.
# The simulator's hunter presets are SIML since #824 (defaults.siml, builds/*.siml): run.sim_presets reads all seven (open item 0b).
# Runs on the fourth checkout ~/.wow-forever-tools/wowsims-forever-x at 7c3453f5a, shared with the shaman lane.
# Resume: the same command (markers deep-runs/r1103/hun-*).
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
LG=raid-hunter.log
R=_reference/data/raidsim
E="mm-raid mm-lonewolf-raid bm-raid melee-dps"
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
[ "$(git -C "$WOW_FOREVER_SIM" rev-parse --short=9 HEAD)" = "${LANE_PIN:-16e85426c}" ] || { say "raid: hunter STOP, the fourth checkout is not at 7c3453f5a"; exit 1; }
# 2026-11-06 (the gear repair, page-audit.md J1-J4): the class sets are re-made first; the step removes this lane markers, so it
# runs again in the new sets (gear_repair_1103.sh; once per class, marker r1103/gear-hunter)
bash $L/gear_repair_1103.sh hunter "hun-*" || { say "raid: hunter STOP, the gear repair failed (gear-repair.log)"; exit 1; }

say "raid: hunter start (${LANE_PIN:-16e85426c} in wowsims-forever-y)"
for e in $E; do run hun-race-$e $LG race hunter $e; done
for e in $E; do
  run hun-apl-$e $LG python -u $R/apl_opt.py hunter --spec $e --write --setting raid --rounds 8 --lookahead 0
done
for e in $E; do run hun-race-tuned-$e $LG race hunter $e; done
run hun-synergy $LG python -u $R/synergy.py hunter --fresh
run hun-structural $LG python -u $R/structural.py hunter --fresh
run hun-open-builds $LG python -u _reference/data/open_builds.py hunter --write --only raid --race
if [ ! -e "$M/hun-ml-cleared" ]; then
  python - <<'PY' >> $L/$LG 2>&1 && touch "$M/hun-ml-cleared"
import json, pathlib
d = pathlib.Path("_reference/data/raidsim/ml")
(d / "prev").mkdir(exist_ok=True)
for n in ("hunter-beast-mastery.json", "hunter-marksmanship.json", "hunter-survival.json", "hunter-hybrid-beast-mastery-marksmanship.json"):
    p = d / n
    r = json.load(open(p, encoding="utf-8"))
    (d / "prev" / p.name).write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for k in ("bis2", "prebis", "bis-raid", "prebis-raid"):
        r.get("gear", {}).pop(k, None)
    for k in ("bis-dummy", "bis-raid", "prebis-dummy", "prebis-raid"):
        r.get("search", {}).pop(k, None)
    for k in ("compare", "compare_raid", "builds", "tidied", "aligned_raid", "signature_check"):
        r.pop(k, None)
    p.write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("cleared", p.name)
PY
fi
run hun-ml-BM $LG python -u $R/ml_pipeline.py hunter --spec "Beast Mastery" --steps final
run hun-ml-MM $LG python -u $R/ml_pipeline.py hunter --spec "Marksmanship" --steps final
run hun-ml-SV $LG python -u $R/ml_pipeline.py hunter --spec "Survival" --steps final
run hun-ml-Hybrid $LG python -u $R/ml_pipeline.py hunter --spec "Hybrid Beast Mastery/Marksmanship" --steps final
run hun-ml-builds $LG python -u $R/ml_builds.py hunter --builds
run hun-validate $LG python -u _reference/data/validate_builds.py
for e in $E; do run hun-final-race-$e $LG race hunter $e; done
run hun-tidy $LG python -u $R/ml_builds.py hunter --tidy-winners
run hun-unused $LG python -u $R/unused_abilities.py hunter --write
say "raid: hunter done (rankings and gear links after the last raid lane; pages at the regen)"
