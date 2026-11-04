#!/usr/bin/env bash
# 2026-11-03 (user: "wait for the sim to merge"): wowsims/forever #839 (merged 23:38Z), #846 and #847 are the shaman's port of the 11-02 notes
# from the game files at push 113596 on build 70755: Lava Burst and Elemental Mastery out of the Elemental tree, Call of Thunder (5%) and
# Lightning Mastery (a 15 s cooldown: Lightning Bolt 0.5 s faster, no Chain Lightning cooldown; a major cooldown, cast by the rotations'
# "use every other cooldown" line), Lightning Overload 30% read from the overload rows, Flurry 30%, Mental Dexterity 150%, Stormstrike 150%
# normalized: our 70707 -> 70753 shaman tree diff, names and rank caps identical (checked 2026-11-03 22:40). A reworked tree: the full raid
# search (as the warrior), not only re-tunes. The rotations' Lava Burst (1238300) and Elemental Mastery (1326047) lines read an absent
# spell (forever_absent.go: never cast); the re-tune may drop them.
# Runs on the fourth checkout ~/.wow-forever-tools/wowsims-forever-x at 7c3453f5a (2026-11-04 master, patched bench by repin_rehearsal.py),
# shared with the hunter lane (bench configs are named per class and spec, so the two do not collide).
# Resume: the same command (markers deep-runs/r1103/sha-*; family_search resumes from its record without --fresh).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-x"
L=_reference/data/deep-runs
M=$L/r1103
mkdir -p $M
LOG=$L/patch-1103.log
LG=raid-shaman.log
R=_reference/data/raidsim
E="elemental-dps enhancement-dps stormcaller-dps"
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
[ "$(git -C "$WOW_FOREVER_SIM" rev-parse --short=9 HEAD)" = "7c3453f5a" ] || { say "raid: shaman STOP, the fourth checkout is not at 7c3453f5a"; exit 1; }

say "raid: shaman start (7c3453f5a in wowsims-forever-x)"
for e in $E; do run sha-race-$e $LG race shaman $e; done
for e in $E; do
  run sha-apl-$e $LG python -u $R/apl_opt.py shaman --spec $e --write --setting raid --rounds 8 --lookahead 0
done
for e in $E; do run sha-race-tuned-$e $LG race shaman $e; done
run sha-family $LG python -u $R/family_search.py shaman $(fresh sha-family)
run sha-open-builds $LG python -u _reference/data/open_builds.py shaman --write --only raid --race
if [ ! -e "$M/sha-ml-cleared" ]; then
  python - <<'PY' >> $L/$LG 2>&1 && touch "$M/sha-ml-cleared"
import json, pathlib
d = pathlib.Path("_reference/data/raidsim/ml")
(d / "prev").mkdir(exist_ok=True)
for n in ("shaman-elemental.json", "shaman-enhancement.json", "shaman-hybrid-elemental-enhancement.json"):
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
run sha-ml-Elemental $LG python -u $R/ml_pipeline.py shaman --spec "Elemental" --steps final
run sha-ml-Enhancement $LG python -u $R/ml_pipeline.py shaman --spec "Enhancement" --steps final
run sha-ml-Hybrid $LG python -u $R/ml_pipeline.py shaman --spec "Hybrid Elemental/Enhancement" --steps final
run sha-ml-builds $LG python -u $R/ml_builds.py shaman --builds
run sha-validate $LG python -u _reference/data/validate_builds.py
for e in $E; do run sha-final-race-$e $LG race shaman $e; done
run sha-tidy $LG python -u $R/ml_builds.py shaman --tidy-winners
run sha-unused $LG python -u $R/unused_abilities.py shaman --write
say "raid: shaman done (rankings and gear links after the last raid lane; pages at the regen)"
