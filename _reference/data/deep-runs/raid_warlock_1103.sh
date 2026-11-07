#!/usr/bin/env bash
# 2026-11-04 (user: "wait for the sim to merge"): wowsims/forever #827 (merged 08:24Z) is the warlock's port of the 11-02 notes, the
# warlock group regenerated on build 70755 up to hotfix push 113600: Agony, Shadow and Flame, Wrack, pets; #843 reads Life Tap's and
# Hellfire's health costs from base health. The simulator's talent trees are unchanged since 6ee3c30f3 (names, rank caps, positions and
# prerequisite arrows equal ours, checked 2026-11-04 01:00 and 03:50); every rotation of ours validates without a warning on 92c4c35b9
# (racials off; the committed record's Eureka! warnings are the Gnome racial). Number changes, no tree rework: the paladin's and hunter's
# treatment (re-tunes, certificate and structural ranking, the ML final step), not the full family search. Presets: presets.ts (five).
# Runs on ~/.wow-forever-tools/wowsims-forever-z at 92c4c35b9, shared with the rogue lane.
# Resume: the same command (markers deep-runs/r1103/wl-*).
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
LG=raid-warlock.log
R=_reference/data/raidsim
E="affliction-raid fire-destro-raid sb-raid demonology-raid incinerate-raid"
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
[ "$(git -C "$WOW_FOREVER_SIM" rev-parse --short=9 HEAD)" = "16e85426c" ] || { say "raid: warlock STOP, the checkout is not at 92c4c35b9"; exit 1; }
# 2026-11-06 (the gear repair, page-audit.md J1-J4): the class sets are re-made first; the step removes this lane markers, so it
# runs again in the new sets (gear_repair_1103.sh; once per class, marker r1103/gear-warlock)
bash $L/gear_repair_1103.sh warlock "wl-*" || { say "raid: warlock STOP, the gear repair failed (gear-repair.log)"; exit 1; }

say "raid: warlock start (16e85426c in wowsims-forever-y)"
for e in $E; do run wl-race-$e $LG race warlock $e; done
for e in $E; do
  run wl-apl-$e $LG python -u $R/apl_opt.py warlock --spec $e --write --setting raid --rounds 8 --lookahead 0
done
for e in $E; do run wl-race-tuned-$e $LG race warlock $e; done
run wl-synergy $LG python -u $R/synergy.py warlock --fresh
run wl-structural $LG python -u $R/structural.py warlock --fresh
run wl-open-builds $LG python -u _reference/data/open_builds.py warlock --write --only raid --race
if [ ! -e "$M/wl-ml-cleared" ]; then
  python - <<'PY' >> $L/$LG 2>&1 && touch "$M/wl-ml-cleared"
import json, pathlib
d = pathlib.Path("_reference/data/raidsim/ml")
(d / "prev").mkdir(exist_ok=True)
for n in ("warlock-affliction.json", "warlock-demonology.json", "warlock-destruction.json", "warlock-hybrid-affliction-destruction.json"):
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
run wl-ml-Aff $LG python -u $R/ml_pipeline.py warlock --spec "Affliction" --steps final
run wl-ml-Demo $LG python -u $R/ml_pipeline.py warlock --spec "Demonology" --steps final
run wl-ml-Destro $LG python -u $R/ml_pipeline.py warlock --spec "Destruction" --steps final
run wl-ml-Hybrid $LG python -u $R/ml_pipeline.py warlock --spec "Hybrid Affliction/Destruction" --steps final
run wl-ml-builds $LG python -u $R/ml_builds.py warlock --builds
run wl-validate $LG python -u _reference/data/validate_builds.py
for e in $E; do run wl-final-race-$e $LG race warlock $e; done
run wl-tidy $LG python -u $R/ml_builds.py warlock --tidy-winners
run wl-unused $LG python -u $R/unused_abilities.py warlock --write
say "raid: warlock done (rankings and gear links after the last raid lane; pages at the regen)"
