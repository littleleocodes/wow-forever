#!/usr/bin/env bash
# 2026-11-04 (user: "wait for the sim to merge"): wowsims/forever #840 + #849 (merged 05:01Z) are the rogue's port of the talent rework of
# hotfix pushes 113351 and 113483 on build 70755 up to push 113583: every tree reshuffled, Mutilate the Assassination capstone (needs Venom),
# Death Mark the Subtlety capstone (needs Preparation), Shank (off-hand, 25 energy) with Venom, Boot Knife and Flash of Steel, Poised and
# Composure, Coup de Grace and Efficient Strikes; Murder, Quietus, Cutthroat, Thousand Cuts gone. Not modelled: Death Mark, Quick Getaway,
# Camouflage, so the Subtlety raid build keeps its Hemorrhage-only rule (modes.raid; the signature-spell rule waits for Death Mark).
# Our rogue tree took the simulator's structure the same night (--sim-trees 6ee3c30f3: six prerequisite arrows the talentsforever export
# lacked); names and rank caps were already identical.
# Base rotation: the simulator's new default (raidsim/apls/rogue/sim-presets/, README there) for all four entries; our tuned rotations of
# before the rework (archived in apls/rogue/prev-70753/) named removed spells and lost 10.7% (Combat swords) and 20% (Subtlety) to it on
# our builds, tied for Assassination and Combat daggers, and the simulator's presets gained 8-66% under it (2026-11-04 00:45).
# A reworked tree: the full raid search (as warrior and shaman). Runs on the fifth checkout ~/.wow-forever-tools/wowsims-forever-r at
# 6ee3c30f3 (patched bench by repin_rehearsal.py).
# Resume: the same command (markers deep-runs/r1103/rog-*; family_search resumes from its record without --fresh).
# 2026-11-04 03:45: moved to ~/.wow-forever-tools/wowsims-forever-z at 92c4c35b9 (shared with the warlock lane): #851 doubled the poisons'
# attack-power scaling (Instant 0.005 -> 0.01, Deadly 0.0045 -> 0.009 over the ticks) and #854 tuned the default rotation's Vanish line; the
# races on 6ee3c30f3 (00:52-02:04) were discarded and the rotation search stopped in its second round.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-z"
L=_reference/data/deep-runs
M=$L/r1103
mkdir -p $M
LOG=$L/patch-1103.log
LG=raid-rogue.log
R=_reference/data/raidsim
E="combat-swords-raid combat-daggers-raid assassination-raid subtlety-raid"
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
[ "$(git -C "$WOW_FOREVER_SIM" rev-parse --short=9 HEAD)" = "92c4c35b9" ] || { say "raid: rogue STOP, the checkout is not at 92c4c35b9"; exit 1; }

say "raid: rogue start (92c4c35b9 in wowsims-forever-z)"
for e in $E; do run rog-race-$e $LG race rogue $e; done
for e in $E; do
  run rog-apl-$e $LG python -u $R/apl_opt.py rogue --spec $e --write --setting raid --rounds 8 --lookahead 0
done
for e in $E; do run rog-race-tuned-$e $LG race rogue $e; done
run rog-family $LG python -u $R/family_search.py rogue $(fresh rog-family)
run rog-open-builds $LG python -u _reference/data/open_builds.py rogue --write --only raid --race
if [ ! -e "$M/rog-ml-cleared" ]; then
  python - <<'PY' >> $L/$LG 2>&1 && touch "$M/rog-ml-cleared"
import json, pathlib
d = pathlib.Path("_reference/data/raidsim/ml")
(d / "prev").mkdir(exist_ok=True)
for n in ("rogue-assassination.json", "rogue-combat.json", "rogue-hybrid-assassination-combat.json", "rogue-subtlety.json"):
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
run rog-ml-Assassination $LG python -u $R/ml_pipeline.py rogue --spec "Assassination" --steps final
run rog-ml-Combat $LG python -u $R/ml_pipeline.py rogue --spec "Combat" --steps final
run rog-ml-Hybrid $LG python -u $R/ml_pipeline.py rogue --spec "Hybrid Assassination/Combat" --steps final
run rog-ml-Subtlety $LG python -u $R/ml_pipeline.py rogue --spec "Subtlety" --steps final
run rog-ml-builds $LG python -u $R/ml_builds.py rogue --builds
run rog-validate $LG python -u _reference/data/validate_builds.py
for e in $E; do run rog-final-race-$e $LG race rogue $e; done
run rog-tidy $LG python -u $R/ml_builds.py rogue --tidy-winners
run rog-unused $LG python -u $R/unused_abilities.py rogue --write
say "raid: rogue done (rankings and gear links after the last raid lane; pages at the regen)"
