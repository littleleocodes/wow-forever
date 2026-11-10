#!/usr/bin/env bash
# 2026-11-03 (user: "wait for the sim to merge"): wowsims/forever #834 (merged 20:59Z) is the paladin's port of the 2026-11-02 notes on build
# 70755: Vengeance to 5 stacks, Two-Handed Weapon Specialization on Holy (our 70707 -> 70753 paladin talent diff is exactly these two),
# Holy Shield Rank 4 (our spell data has it). The simulator's tests: Retribution +3.4% to +6.4%, Protection +5% (Holy Shield R4).
# The mage lane (raid_mage_1103.sh) is still running on the pinned clone (5ad0894c9), so this lane runs on the second checkout
# ~/.wow-forever-tools/wowsims-forever-next at d97252f2a (2026-11-03 master, patched bench built by repin_rehearsal.py; every record
# names its commit). Since #812 the simulator keeps the paladin presets as SIML: the entries' base rotations and the tank's gear are the
# bac92dbd5 JSON copies in raidsim/apls/paladin/sim-presets/ and gear_sets/forever/paladin-protection-default.gear.json (same items),
# and run.py reads the SIML presets' talents. Steps: races, the three raid rotations re-tuned (full raid), races, the certificate and
# structural ranking, open builds, the ML final step for Retribution, builds, final races. The tank's deep search is not re-run (its
# rotation is re-tuned and it is raced on the new rank).
# Resume: the same command (markers deep-runs/r1103/pal-*).
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
LG=raid-paladin.log
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
[ "$(git -C "$WOW_FOREVER_SIM" rev-parse --short=9 HEAD)" = "${LANE_PIN:-16e85426c}" ] || { say "raid: paladin STOP, the second checkout is not at d97252f2a"; exit 1; }
# 2026-11-06 (the gear repair, page-audit.md J1-J4): the class sets are re-made first; the step removes this lane markers, so it
# runs again in the new sets (gear_repair_1103.sh; once per class, marker r1103/gear-paladin)
bash $L/gear_repair_1103.sh paladin "pal-*" || { say "raid: paladin STOP, the gear repair failed (gear-repair.log)"; exit 1; }

say "raid: paladin start (${LANE_PIN:-16e85426c} in wowsims-forever-y)"
for e in ret-dps shockadin-raid prot-tank; do run pal-race-$e $LG race paladin $e; done
for e in ret-dps shockadin-raid prot-tank; do
  run pal-apl-$e $LG python -u $R/apl_opt.py paladin --spec $e --write --setting raid --rounds 8 --lookahead 0
done
for e in ret-dps shockadin-raid prot-tank; do run pal-race-tuned-$e $LG race paladin $e; done
run pal-synergy $LG python -u $R/synergy.py paladin --fresh
run pal-structural $LG python -u $R/structural.py paladin --fresh
run pal-open-builds $LG python -u _reference/data/open_builds.py paladin --write --only raid --race
if [ ! -e "$M/pal-ml-cleared" ]; then
  python - <<'PY' >> $L/$LG 2>&1 && touch "$M/pal-ml-cleared"
import json, pathlib
d = pathlib.Path("_reference/data/raidsim/ml")
(d / "prev").mkdir(exist_ok=True)
p = d / "paladin-retribution.json"
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
run pal-ml-Retribution $LG python -u $R/ml_pipeline.py paladin --spec "Retribution" --steps final
run pal-ml-builds $LG python -u $R/ml_builds.py paladin --builds
run pal-validate $LG python -u _reference/data/validate_builds.py
for e in ret-dps shockadin-raid prot-tank; do run pal-final-race-$e $LG race paladin $e; done
run pal-tidy $LG python -u $R/ml_builds.py paladin --tidy-winners
run pal-unused $LG python -u $R/unused_abilities.py paladin --write
say "raid: paladin done (rankings and gear links: ml_builds.py --rank, gear_links.py --write after the last raid lane; pages at the regen)"
