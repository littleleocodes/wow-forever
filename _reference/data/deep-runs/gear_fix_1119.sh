#!/usr/bin/env bash
# gear_fix_1119.sh (2026-11-19): what the gear night left out, found while answering the Addons session.
#  1. sets the night did not make again: the Shockadin's own Raid BiS set and the paladin tank's standard set held later-phase items;
#     seven orphaned tier files did too (gear_fix_1119.py);
#  2. the paladin tank raced again and its tank values measured again in the fixed set;
#  3. GearCheck's raid values for every damage page measured on the page's own pick (page_stat_weights.py --all): the ML records'
#     BiS weights were measured on each search's starting build, and 17 of 29 searches started from a fallback (Frost: the old
#     21/0/30 while the page shows 15/5/31); their error bars; the add-on file; the pages; the checks.
# BelowNormal on 10 of 12. Log deep-runs/gear-fix-1119.log, output gear-fix-1119-out.log, markers deep-runs/g1119/.
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
export WOW_FOREVER_NO_RACIALS=1
export WOW_FOREVER_SIM="$HOME/.wow-forever-tools/wowsims-forever-y"
L=_reference/data/deep-runs
M=$L/g1119
LOG=$L/gear-fix-1119.log
OUT=$L/gear-fix-1119-out.log
R=_reference/data/raidsim
D=_reference/data
mkdir -p $M
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve 2 -Priority BelowNormal >> $LOG 2>&1
say() { echo "=== $(date +%F_%H:%M) $*" >> $LOG; }
run() {
  local mk=$1; shift
  if [ -e "$M/$mk" ]; then return 0; fi
  echo "##### $(date +%F_%H:%M) $mk: $*" >> $OUT
  "$@" >> $OUT 2>&1; local rc=$?
  say "$mk rc=$rc"
  [ $rc -eq 0 ] && touch "$M/$mk"
  return $rc
}
say "start"
run shockadin python -u $L/gear_fix_1119.py shockadin || { say "STOP: the Shockadin set"; exit 1; }
run tankshield python -u $L/gear_fix_1119.py tankshield || { say "STOP: the tank shield"; exit 1; }
run orphans python -u $L/gear_fix_1119.py orphans || say "WARNING: orphans"
run race-prot-tank bash -c "python -u $R/run.py paladin --spec prot-tank --write && python -u $R/run.py paladin --spec prot-tank --env environments --write" || say "WARNING: the prot-tank race"
run tank-paladin python -u $D/characters/tank_weights.py paladin prot-tank protection-ml-tank Protection || say "WARNING: tank_weights paladin"
run psw-all python -u $R/page_stat_weights.py --all || { say "STOP: page_stat_weights --all"; exit 1; }
KEYS=$(python -c "import json; d = json.load(open('$R/page-stat-weights.json', encoding='utf-8'))['specs']; print(' '.join([f'page:{k}' for k, v in d.items() if v.get('weights')] + [f'pagehit:{k}' for k, v in d.items() if v.get('hit_below_cap')]))")
run errors python -u $R/weight_errors.py --only $KEYS tank:paladin --jobs 2 || say "WARNING: weight_errors"
run addon python -u $D/characters/addon_values.py || say "WARNING: addon_values"
run pages python -u $D/render_modes.py || say "WARNING: render_modes"
run page-lint python -u $D/page_lint.py --write || say "WARNING: page_lint"
say "all done (Claude: review, commit, push; tell the Addons session which entries were re-measured)"
