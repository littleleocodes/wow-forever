#!/usr/bin/env bash
# 2026-11-03 (user: "wait for the sim to merge"): wowsims/forever #841 (merged 22:20Z) is the warrior's port of hotfix pushes 113539/113542
# on build 70755: the Fury tree reworked (Raging Blows -> Improved Whirlwind 2 ranks, Reckless Swings new), Flurry 3 ranks of 10%,
# Improved Tactical Mastery 3 ranks and Bloodthrill 2, Two-Handed Weapon Specialization 2/4/6%, Slam's cooldown 15 s, Booming Voice on
# Piercing Howl: every warrior change of our 70707 -> 70753 talent data (Defiance's 20% reads its row). A reworked tree: the full raid
# search (as the rogue and shaman will get), not only re-tunes.
# The mage (pinned clone, 5ad0894c9) and paladin (wowsims-forever-next, d97252f2a) lanes hold the other two checkouts, so this lane runs
# on a third one, ~/.wow-forever-tools/wowsims-forever-w at 02bd77cbe (2026-11-03 master; patched bench by repin_rehearsal.py).
# Steps: races of the repaired builds, every warrior rotation re-tuned (full raid), races, the open family search (fresh, warm start:
# certificate and structural ranking per entry), open builds, the ML final step for Arms and Fury, builds, final races. The tank's deep
# search is not re-run (rotation re-tuned, raced).
# Resume: the same command (markers deep-runs/r1103/war-*; family_search resumes from its record without --fresh).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-w"
L=_reference/data/deep-runs
M=$L/r1103
mkdir -p $M
LOG=$L/patch-1103.log
LG=raid-warrior.log
R=_reference/data/raidsim
E="arms-2h-raid fury-dw-raid arms-battle-raid prot-tank"
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {
  local mk=${1////_} lg=$2; shift 2
  if [ -e "$M/$mk" ]; then return 0; fi
  "$@" >> "$L/$lg" 2>&1; local rc=$?
  say "raid $mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return 0
}
fresh() { if [ -e "$M/$1.started" ]; then echo ""; else touch "$M/$1.started"; echo "--fresh"; fi; }
race() { python -u $R/run.py $1 --spec $2 --write && python -u $R/run.py $1 --spec $2 --env environments --write; }
[ "$(git -C "$WOW_FOREVER_SIM" rev-parse --short=9 HEAD)" = "02bd77cbe" ] || { say "raid: warrior STOP, the third checkout is not at 02bd77cbe"; exit 1; }

say "raid: warrior start (02bd77cbe in wowsims-forever-w)"
for e in $E; do run war-race-$e $LG race warrior $e; done
for e in $E; do
  run war-apl-$e $LG python -u $R/apl_opt.py warrior --spec $e --write --setting raid --rounds 8 --lookahead 0
done
for e in $E; do run war-race-tuned-$e $LG race warrior $e; done
run war-family $LG python -u $R/family_search.py warrior $(fresh war-family)
run war-open-builds $LG python -u _reference/data/open_builds.py warrior --write --only raid --race
if [ ! -e "$M/war-ml-cleared" ]; then
  python - <<'PY' >> $L/$LG 2>&1 && touch "$M/war-ml-cleared"
import json, pathlib
d = pathlib.Path("_reference/data/raidsim/ml")
(d / "prev").mkdir(exist_ok=True)
for n in ("warrior-arms.json", "warrior-fury.json"):
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
run war-ml-Arms $LG python -u $R/ml_pipeline.py warrior --spec "Arms" --steps final
run war-ml-Fury $LG python -u $R/ml_pipeline.py warrior --spec "Fury" --steps final
run war-ml-builds $LG python -u $R/ml_builds.py warrior --builds
run war-validate $LG python -u _reference/data/validate_builds.py
for e in $E; do run war-final-race-$e $LG race warrior $e; done
run war-tidy $LG python -u $R/ml_builds.py warrior --tidy-winners
run war-unused $LG python -u $R/unused_abilities.py warrior --write
say "raid: warrior done (rankings and gear links after the last raid lane; pages at the regen)"
