#!/usr/bin/env bash
# tonight_1110.sh   (2026-11-10, the client 70862 update; user: "Update it and tell me what's different", then "Prep them for now if you
# can but don't start anything": started only when the user says so). Log deep-runs/tonight-1110.log, step logs next to it; markers
# deep-runs/r1110/; resume = the same command. Full power: balance_1104.ps1 -Run 12 -Bench 8 next to it (the user's "full power" mode).
#
# What changed (the session's survey of 2026-11-10; _reference/data/raw/2026-11-10-live-70888/README.md):
#  - the official simulator upstream: client 1.60.1.70862 with the hotfixes of 2026-11-10 (every spell group and the items), Lightning
#    Overload's copies at 50% of the bolt (were about 28%), Arcane Concentration split over a Missiles channel (Blizzard 2026-11-09), dot
#    crits in expected ticks (warlock), the druid's Rake, Rip, Ferocious Bite and Maul re-measured, warrior threat and rage rulings,
#    items removed from the database (every gear set lists some);
#  - applied before this queue (no run): 125 spell ranks of our spellbooks take the live client's numbers (live_spells.py: shaman
#    Lightning Bolt and Chain Lightning, the shocks and imbues; druid Starfire, the Feral finishers and bleeds; rogue Backstab and the
#    poisons; paladin Holy Strike; warrior Spearing Strike ...), the rogue module's Mutilate amounts (40/57/79), the Voidwalker's +40
#    health (Blizzard 2026-11-06), the planner's dungeon bar (2 quests: dungeon kills +50%, Blizzard 2026-11-09).
#
# Stages, each resumable by its markers:
#  0. re-pin: the newest upstream master (or PIN_FULL=<commit>), kept in r1110/pin so a resume uses the same commit. Rehearsed in
#     wowsims-forever-next first (every patch must apply, the bench must build), then wowsims-forever-y (the lanes' checkout; the lane
#     scripts check LANE_PIN) and the main clone; setup.py's pin; sim_info's commit table; apl_validate; spec_check (a field or enum
#     the protos lack stops the queue: an option would be dropped silently); sim_value_audit;
#  1. the gear repair for all nine classes (gear_repair_1103.sh: standard, tier, tank and healer sets from the new item database; it
#     clears each lane's own markers, so a lane run after it redoes everything);
#  2. every raid entry raced again (dummy and the environments) on the new commit;
#  3. the searches where the best build can move, two at once: the shaman lane (Lightning Overload) | the mage lane (Arcane
#     Concentration), then the druid's Feral ML final step (raid_rest_1103.sh druid "Feral Combat"), then the leveling stage;
#  4. leveling: the classes whose spell numbers moved (shaman, druid, rogue, paladin, hunter, warlock, warrior): the fight lab's races
#     and reports (rebuild.py --steps race,report) and the by-level guides re-measured; the mage regression checked (must not move);
#  5. the character planner: Tara's tank weights on the new commit, both characters' pages (no refresh baseline written);
#  6. wrap: validate, rankings and gear links, pages, guide check, page audit, a checkpoint commit (pushed after Claude's review).
# Not tonight: the leveling rules re-tunes and open searches for those classes (a second night if the races move their picks a lot).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/r1110
LOG=$L/tonight-1110.log
R=_reference/data/raidsim
FL=_reference/data/fightlab
D=_reference/data
T="$HOME/.wow-forever-tools"
C="$T/wowsims-forever"
Y="$T/wowsims-forever-y"
N="$T/wowsims-forever-next"
OLD_FULL=16e85426c43340f73f4f6ddc84938d4385890ea8
mkdir -p $M
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {   # run <marker> <log> <command...>: skipped when the marker exists; the marker is written on rc=0; returns rc
  local mk=$1 lg=$2; shift 2
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> "$L/$lg"
  "$@" >> "$L/$lg" 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
race() { python -u $R/run.py $1 --spec $2 --write && python -u $R/run.py $1 --spec $2 --env environments --write; }
entries() { python -c "import json,sys; print(' '.join(n for n, e in json.load(open('_reference/data/raidsim/specs.json', encoding='utf-8'))[sys.argv[1]].items() if isinstance(e, dict)))" "$1"; }
CLASSES="warrior paladin hunter rogue priest shaman mage warlock druid"
say "tonight 1110 start (client 70862 update)"

# ---- 0. re-pin
if [ ! -s $M/pin ]; then
  git -C "$C" fetch -q origin master || { say "STOP: git fetch failed"; exit 1; }
  echo "${PIN_FULL:-$(git -C "$C" rev-parse origin/master)}" > $M/pin
fi
PIN_FULL=$(cat $M/pin)
export LANE_PIN=$(echo "$PIN_FULL" | cut -c1-9)
export WOW_FOREVER_SIM="$Y"
say "pin $PIN_FULL (lanes check $LANE_PIN in $(basename "$Y"))"
rehearse() {   # rehearse <worktree>: our patches on the commit there and the bench built; an edit not applied fails it
  local W=$1 lg="$L/rehearse-$(basename "$1").log"
  git -C "$W" checkout -- . && git -C "$W" clean -fdq -- sim cmd || return 1
  git -C "$W" -c advice.detachedHead=false checkout -q "$PIN_FULL" || return 1
  python -u $R/repin_rehearsal.py --worktree "$W" > "$lg" 2>&1 || return 1
  ! grep -q -E "EDIT NOT APPLIED|edits to retire or adapt" "$lg"
}
repin_main() {   # setup.py's pin, sim_info's commit table, the main clone at the commit, its tools rebuilt
  python - "$OLD_FULL" "$PIN_FULL" <<'PY' || return 1
import gzip, json, pathlib, subprocess, sys, datetime
old, new = sys.argv[1], sys.argv[2]
p = pathlib.Path("_reference/data/raidsim/setup.py")
b = p.read_bytes()
if f'"commit": "{new}"'.encode() not in b:
    assert b.count(f'"commit": "{old}"'.encode()) == 1, "the old pin is not in setup.py"
    p.write_bytes(b.replace(f'"commit": "{old}"'.encode(), f'"commit": "{new}"'.encode()))
raw = subprocess.run(["git", "-C", str(pathlib.Path.home() / ".wow-forever-tools/wowsims-forever"), "show",
                      f"{new}:assets/db_inputs/spell_store_inputs.json"], capture_output=True).stdout
builds = sorted(set(json.loads(gzip.decompress(raw)).get("Builds", {}).values()))
client = builds[-1] if builds else "1.60.1.70862"
s = pathlib.Path("_reference/data/sim_info.py")
t = s.read_text(encoding="utf-8")
if f'"{new[:7]}"' not in t:
    anchor = '"16e8542": "1.60.1.70790"}'
    assert t.count(anchor) == 1, "sim_info's last entry moved"
    lines = t.split("\n")
    i = next(k for k, l in enumerate(lines) if anchor in l)
    lines[i] = lines[i].replace(anchor, '"16e8542": "1.60.1.70790",')
    lines.insert(i + 1, f'                    "{new[:7]}": "{client}"}}   # {new[:7]}: {datetime.date.today()} master (client {client[-5:]} with the '
                        'hotfixes of 2026-11-10: Lightning Overload at 50%, Arcane Concentration split, items; tonight_1110.sh)')
    s.write_text("\n".join(lines), encoding="utf-8")
print("pinned", new, "client", client)
PY
  git -C "$C" checkout -- . && git -C "$C" clean -fdq -- sim || return 1
  git -C "$C" -c advice.detachedHead=false checkout -q "$PIN_FULL" || return 1
  python -u $R/setup.py --rebuild || return 1
  [ "$(git -C "$C" rev-parse HEAD)" = "$PIN_FULL" ]
}
run rehearse-next repin.log rehearse "$N" || { say "STOP: the patches do not apply on $PIN_FULL (rehearse-wowsims-forever-next.log)"; exit 1; }
run rehearse-y repin.log rehearse "$Y" || { say "STOP: the lanes' checkout could not take $PIN_FULL"; exit 1; }
run repin-main repin.log repin_main || { say "STOP: the main clone's re-pin failed (repin.log)"; exit 1; }
run apl-validate repin.log python -u $R/apl_validate.py --all-talents --write
run spec-check repin.log python -u $R/spec_check.py --all-checkouts || { say "STOP: spec_check lists options the protos lack (repin.log): fix the entries' spec fragments"; exit 1; }
run sim-value-audit repin.log python -u $R/sim_value_audit.py --write

# ---- 1. the gear repair, every class (the lanes' own patterns: their markers go too)
declare -A PAT=([warrior]="war-*" [paladin]="pal-*" [hunter]="hun-*" [rogue]="rog-*" [priest]="rest-priest-*" [shaman]="sha-*"
                [mage]="*-mage* rank unused gear-links sim-value-audit" [warlock]="wl-*" [druid]="rest-druid-*")
gear() { rm -f "$L/r1103/gear-$1" "$L"/r1103/gear-*-"$1"; bash $L/gear_repair_1103.sh "$1" "${PAT[$1]}"; }
for c in $CLASSES; do
  run gear-$c gear.log gear $c || { say "STOP: the $c gear repair failed (gear-repair.log)"; exit 1; }
done

# ---- 2. every raid entry raced on the new commit
for c in $CLASSES; do
  for e in $(entries $c); do run race-$c-$e races.log race $c $e; done
done
say "raid races done"

# ---- 3. searches (two at once) and 4. leveling
leveling() {
  for c in shaman druid rogue paladin hunter warlock warrior; do
    run lev-race-$c leveling.log python -u $D/rebuild.py $c --steps race,report
    run lev-guide-$c leveling.log python -u $D/level_guides.py $c --measure
  done
  run lev-regression leveling.log python -u $FL/regression.py
  say "leveling done"
}
lane_a() { [ -e $M/lane-shaman ] || { bash $L/raid_shaman_1103.sh > $L/raid-shaman.console 2>&1 && touch $M/lane-shaman; }; say "lane A (shaman) done"; }
lane_b() {
  [ -e $M/lane-mage ] || { bash $L/raid_mage_1103.sh > $L/raid-mage.console 2>&1 && touch $M/lane-mage; }
  [ -e $M/lane-druid ] || { bash $L/raid_rest_1103.sh druid "Feral Combat" > $L/raid-druid.console 2>&1 && touch $M/lane-druid; }
  leveling
  say "lane B (mage, druid, leveling) done"
}
lane_a & PA=$!
lane_b & PB=$!
wait $PA $PB
for x in lane-shaman lane-mage lane-druid lev-regression; do [ -e $M/$x ] || say "WARNING: $x did not finish (see its log); the wrap goes on"; done

# ---- 5. the character planner
run tank-weights planner.log python -u $D/characters/tank_weights.py paladin prot-tank protection-ml-tank Protection
run plan-tara planner.log python -u $D/characters/plan.py tara --no-refresh
run plan-arcea planner.log python -u $D/characters/plan.py arcea --no-refresh

# ---- 6. wrap
run wrap-validate wrap.log python -u $D/validate_builds.py
run wrap-rank wrap.log python -u $R/ml_builds.py --rank
run wrap-regen wrap.log python -u $D/rebuild.py --steps regen
run wrap-guides wrap.log python -u $D/guides.py --check --write
run wrap-lint wrap.log python -u $D/page_lint.py --write
git -c core.safecrlf=false add -A
git -c core.safecrlf=false commit -q -F - <<EOF
Checkpoint $(date +%F_%H:%M): the client 70862 update (tonight_1110.sh): simulator re-pinned to $LANE_PIN, every gear set repaired, every raid entry raced, the shaman, mage and Feral searches, leveling races and guides for the classes whose spell numbers moved

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF
say "all done (committed $(git rev-parse --short HEAD))"
