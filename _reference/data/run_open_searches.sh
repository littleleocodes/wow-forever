#!/usr/bin/env bash
# The open talent searches, raid then leveling, class by class (2026-10-05, user request: a command to pause and resume them).
#
#     bash _reference/data/run_open_searches.sh                 # every class, in the order below
#     bash _reference/data/run_open_searches.sh mage paladin    # these classes only
#     bash _reference/data/run_open_searches.sh --fresh mage    # after a beta update: start over, seeded with the last run's winners
#                                                               # (the old record is kept as <class>.prev.json); resume WITHOUT --fresh
#
# Pause: stop it (Ctrl+C, or shut the PC down). Resume: run the same command again. Both searches save their record after every finished
# rotation (raidsim/families/<class>.json, fightlab/open/<class>.json) and skip what is done, so a resume loses only the rotation that was
# running. Logs: _reference/data/deep-runs/open-<class>-raid.log and open-<class>-leveling.log, plus open-searches.log (one line a step).
cd "$(dirname "$0")/../.." || exit 1
export PYTHONIOENCODING=utf-8
LOGS=_reference/data/deep-runs
mkdir -p "$LOGS"
FRESH=()
if [ "$1" = "--fresh" ]; then FRESH=(--fresh); shift; fi
CLASSES=("$@")
[ ${#CLASSES[@]} -eq 0 ] && CLASSES=(hunter mage paladin warrior rogue druid shaman warlock priest)
for c in "${CLASSES[@]}"; do
  for kind in raid leveling; do
    if [ "$kind" = raid ]; then tool=_reference/data/raidsim/family_search.py; else tool=_reference/data/fightlab/fl_open_search.py; fi
    echo "=== $(date +%Y-%m-%d_%H:%M) $c $kind" | tee -a "$LOGS/open-searches.log"
    if python -u "$tool" "$c" "${FRESH[@]}" >> "$LOGS/open-$c-$kind.log" 2>&1; then
      echo "=== $(date +%Y-%m-%d_%H:%M) $c $kind ok" | tee -a "$LOGS/open-searches.log"
    else
      echo "=== $(date +%Y-%m-%d_%H:%M) $c $kind FAILED (see $LOGS/open-$c-$kind.log)" | tee -a "$LOGS/open-searches.log"
    fi
  done
done
echo "=== $(date +%Y-%m-%d_%H:%M) all done" | tee -a "$LOGS/open-searches.log"
