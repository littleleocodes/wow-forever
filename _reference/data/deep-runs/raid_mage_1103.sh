#!/usr/bin/env bash
# 2026-11-03 (user: "Stop them and go ahead, wait for the sim to merge"): the first class of the 2026-11-02 notes the raid simulator has
# merged in full is the mage. Its talent data moved 70707 -> 70753 only by dropping Frost Blast (the simulator never had it); the notes'
# other mage changes came with the 10-30 hotfixes (70707, already pinned); the last two, "Clearcasting is no longer consumed on Arcane
# Missiles if Missile Barrage is active" and "Fixed an issue where Arcane Missiles did not proc Clearcasting", are wowsims/forever #831
# (merged 2026-11-03 17:37Z; their tests: Arcane +1.2% in a full raid, Fire +0.2%, Frost and Frostfire unchanged).
# Re-pin bac92dbd5 -> 5ad0894c9 (2026-11-03 master; spell data still 70707; also items of 11-03 #819, the warrior's Whirlwind/Cleave APL
# #818, rogue Riposte/Setup #802, APL values #825/#828). Rehearsed the same day in wowsims-forever-next: every patch applies, the bench
# builds, an Arcane smoke race runs. The leveling queue (patch_1103.sh) uses only the fight lab: the re-pin does not touch it.
# The other classes keep their bac92dbd5 raid numbers (each record names its commit) until their ports merge.
# Then the mage's raid half: the rotations the fix touches re-tuned (Arcane, Fire), every mage entry raced, the certificates and the
# structural ranking, the open builds, the ML final step for the Missile Barrage specs (Arcane, Arcane-Frost), builds, rankings.
# Resume: the same command (markers deep-runs/r1103/<step>).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
L=_reference/data/deep-runs
M=$L/r1103
mkdir -p $M
LOG=$L/patch-1103.log
LG=raid-mage.log
R=_reference/data/raidsim
OLD_FULL=bac92dbd59e8101e4c37b737bb6d6d071cff0d5d
PIN_FULL=5ad0894c9def891221a88705f90e306757133014
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

repin() {
  local C="$HOME/.wow-forever-tools/wowsims-forever"
  python - "$OLD_FULL" "$PIN_FULL" <<'PY' || return 1
import pathlib, sys
p = pathlib.Path("_reference/data/raidsim/setup.py")
b = p.read_bytes()
old, new = f'"commit": "{sys.argv[1]}"'.encode(), f'"commit": "{sys.argv[2]}"'.encode()
if new not in b:
    assert b.count(old) == 1, "the old pin is not in setup.py"
    p.write_bytes(b.replace(old, new))
print("setup.py pinned to", sys.argv[2])
PY
  git -C "$C" fetch -q origin master || return 1
  git -C "$C" checkout -- . && git -C "$C" clean -fdq -- sim || return 1   # our patch edits and the files the patches add, off
  git -C "$C" -c advice.detachedHead=false checkout "$PIN_FULL" || return 1
  python -u $R/setup.py --rebuild || return 1
  [ "$(git -C "$C" rev-parse HEAD)" = "$PIN_FULL" ] || return 1
  python -u $R/apl_validate.py --all-talents --write
}

say "raid: start (re-pin to 5ad0894c9, then the mage's raid half)"
run repin repin-1103.log repin
if [ ! -e "$M/repin" ]; then say "raid: STOP, the re-pin failed (repin-1103.log)"; exit 1; fi
for e in arcane-dps fire-raid frost-raid frostfire-raid; do run race-mage-$e $LG race mage $e; done
for e in arcane-dps fire-raid; do
  run apl-mage-$e $LG python -u $R/apl_opt.py mage --spec $e --write --setting raid --rounds 8 --lookahead 0
done
for e in arcane-dps fire-raid frost-raid frostfire-raid; do run race-tuned-mage-$e $LG race mage $e; done
run synergy-mage $LG python -u $R/synergy.py mage --fresh
run structural-mage $LG python -u $R/structural.py mage --fresh
run open-builds-mage $LG python -u _reference/data/open_builds.py mage --write --only raid --race
if [ ! -e "$M/ml-cleared-mage" ]; then   # the Missile Barrage specs' gear and final searches cleared (kept under ml/prev/)
  python - <<'PY' >> $L/$LG 2>&1 && touch "$M/ml-cleared-mage"
import json, pathlib
d = pathlib.Path("_reference/data/raidsim/ml")
(d / "prev").mkdir(exist_ok=True)
for n in ("mage-arcane.json", "mage-hybrid-arcane-frost.json"):
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
run ml-mage-Arcane $LG python -u $R/ml_pipeline.py mage --spec "Arcane" --steps final
run ml-mage-Arcane-Frost $LG python -u $R/ml_pipeline.py mage --spec "Hybrid Arcane/Frost" --steps final
run ml-builds-mage $LG python -u $R/ml_builds.py mage --builds
run validate-mage $LG python -u _reference/data/validate_builds.py
for e in arcane-dps fire-raid frost-raid frostfire-raid; do run final-race-mage-$e $LG race mage $e; done
run tidy-mage $LG python -u $R/ml_builds.py mage --tidy-winners
run rank $LG python -u $R/ml_builds.py --rank
run unused $LG python -u $R/unused_abilities.py mage --write
run gear-links $LG python -u $R/gear_links.py --write
run sim-value-audit $LG python -u $R/sim_value_audit.py --write
say "raid: mage done (pages at patch_1103.sh's regen, or rebuild.py --steps regen)"
