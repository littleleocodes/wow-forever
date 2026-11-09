#!/usr/bin/env bash
# 2026-11-06 (user: "Go with your recs for the changes and fixes"; page-audit.md K, search-improvements.md 0d-0f). The re-races the
# approved changes need, one class block at a time, next to lane C. It replaces rules_refresh_1103.sh (part B of the rules repair,
# stopped before it started anything) and covers its work too.
# What changed, and what each block therefore redoes:
#   - a leveling order takes its spec's signature talent as early as the tree allows (signature.late_talents fails the check
#     otherwise; fl_signature.sig_order is the order every tool starts from): rogue Assassination and Subtlety, mage Arcane and Fire,
#     priest Discipline, hunter Beast Mastery (one-tree); hand drafts and exports through order_repair.py;
#   - the Fire rotation opens every pull with a hard-cast Pyroblast (mage.PYRO_OPENER, a rule knob): Fire rules, then its record;
#   - signature rules: Survival counts the pet while leveling, Feral counts Ravage and Pounce, Beast Mastery's leveling floor is 30%;
#   - the cat rotation's 11/29/11 is a Feral Combat build (spec_modes.LEVELING_FILE_AS);
#   - part A's new rule files (rules_repair_1103.sh): rogue Subtlety, mage Arcane and Arcane-Frost, warrior Protection, warlock.
# Per record: refresh_keys.py takes the rotation back to the end of its level-60 search, a plain fl_open_search.py run redoes the
# 20-60 race (previous winner and our builds as finalists), the 20-60 polish, the order choice and polish, the values, the certificate
# and the signature check. Per class afterwards: the sibling-rotation table, open builds (which measures the class's signature audit
# first), orders, races and reports. A record is only touched while no fl_open_search.py of that class and record runs: the warlock
# block waits for lane C's race-warlock; the paladin needs no block (its search has not run and loads the new code).
# The file name ends in _1103.sh on purpose (rebalance.ps1 treats it as a lane). Log: deep-runs/lane-f.log and patch-1103.log.
# Resume: the same command (markers deep-runs/p1103/fix-*).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/p1103
LOG=$L/patch-1103.log
D=_reference/data
FL=$D/fightlab
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-8}"
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {   # run <marker> <command...>: skipped when the marker exists; the marker is written on rc=0; returns rc
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> "$L/lane-f.log"
  "$@" >> "$L/lane-f.log" 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
redo() {   # redo <marker> <class> <record under fightlab/open> [--tree <tree>] <rotation>...: one record from the 20-60 race on
  local mk=$1 c=$2 rec=$3; shift 3
  local tree=()
  if [ "$1" = "--tree" ]; then tree=(--tree "$2"); shift 2; fi
  local args=(); local r; for r in "$@"; do args+=(--rotation "$r"); done
  run fix-keys-$mk python -u $L/refresh_keys.py $rec "$@" &&
  run fix-open-$mk python -u $FL/fl_open_search.py $c "${tree[@]}" "${args[@]}" --jobs 4
}
after() {   # after <class>: the sibling-rotation table of the refreshed winners, open builds, orders, races and reports
  run fix-cross-$1 python -u $FL/fl_synergy.py $1 --jobs 4
  run fix-builds-$1 python -u $D/open_builds.py $1 --write --only leveling || return 1
  run fix-orders-$1 python -u $D/order_repair.py $1 --jobs 4 --write
  run fix-race-$1 python -u $D/rebuild.py $1 --steps race,report
  say "fixes: class $1 done"
}
say "start fixes lane (signature talents early, Fire opener, Survival / Feral / Beast Mastery rules, part A's rule files)"

# rogue: Assassination took Mutilate at 60, Subtlety Hemorrhage at 54 and Death Mark at 60; Subtlety's rules are part A's
run fix-orders0-rogue python -u $D/order_repair.py rogue --jobs 4 --write
redo rogue rogue rogue.json subtlety-leveling combat-daggers-raid &&
redo rogue-sub rogue pure/rogue-subtlety.json --tree Subtlety subtlety-leveling &&
redo rogue-assa rogue pure/rogue-assassination.json --tree Assassination combat-daggers-raid &&
after rogue

# mage: the Fire rules with the Pyroblast opener, then Fire, Arcane (Arcane Blast at 24, part A's rules) and Arcane-Frost (part A's rules)
run fix-orders0-mage python -u $D/order_repair.py mage --jobs 4 --write
run fix-rules-mage-fire python -u $FL/rules_retune.py mage fire-leveling opt-fire-leveling-leveling-st --jobs 4 &&
redo mage mage mage.json fire-leveling arcane-leveling barrage-frost-leveling &&
after mage

# hunter: the one-tree records. Survival's winner was refused at a 34% melee share (the pet counts now); Beast Mastery took Bestial
# Wrath at 56 and its floor is 30%
run fix-orders0-hunter python -u $D/order_repair.py hunter --jobs 4 --write
redo hunter-surv hunter pure/hunter-survival.json --tree Survival melee-dps &&
redo hunter-bm hunter pure/hunter-beast-mastery.json --tree "Beast Mastery" bm-leveling &&
after hunter

# druid: the cat rules again (Ravage and Pounce count: every cat build sat on the 80% floor), then the cat rotation's record
run fix-orders0-druid python -u $D/order_repair.py druid --jobs 4 --write
run fix-rules-druid-cat python -u $FL/rules_retune.py druid feral-cat-dps leveling-feral --jobs 4 &&
redo druid druid druid.json feral-cat-dps &&
after druid

# priest: Discipline took Penance at 51; a Shadow export Mind Flay at 50 (order_repair.py)
run fix-orders0-priest python -u $D/order_repair.py priest --jobs 4 --write
redo priest priest priest.json discipline-leveling &&
after priest

# warrior: Protection's rules are part A's; an Arms export filed under Fury took Bloodthirst at 43 (order_repair.py)
run fix-orders0-warrior python -u $D/order_repair.py warrior --jobs 4 --write
redo warrior warrior warrior.json prot-leveling &&
after warrior

say "fixes: rogue, mage, hunter, druid, priest and warrior done; the warlock waits for race-warlock and part A's Demonology rules"
until [ -e "$M/race-warlock" ] && [ -e "$M/rules2-warlock-demonology-leveling" ]; do sleep 120; done
# warlock: the Destruction rules once more on that search's result (replaced by hand before its search, after six rounds of a
# from-scratch tune); then all three rotations from the race on. Lane C's warlock process loaded the code before the 20-60 race took
# the previous record's winner and our builds as finalists: Affliction's fresh winner 38/11/2 ran 36.78 s against 36.20 for
# affliction-open-leveling, the winner it replaced, and lane C's builds step rewrites that build from the slower record.
run fix-rules-warlock-destro python -u $FL/rules_retune.py warlock destruction-leveling destruction-open-leveling --jobs 4
run fix-orders0-warlock python -u $D/order_repair.py warlock --jobs 4 --write
redo warlock warlock warlock.json affliction-leveling demonology-leveling destruction-leveling &&
after warlock

# the pages: when the leveling queue's tail has regenerated them before this lane ended, once more on the final state
if [ -e "$M/regen" ]; then
  run fix-validate python -u $D/validate_builds.py &&
  run fix-regen python -u $D/rebuild.py --steps regen &&
  run fix-guides python -u $D/guides.py --check --write
fi
say "fixes lane done"
