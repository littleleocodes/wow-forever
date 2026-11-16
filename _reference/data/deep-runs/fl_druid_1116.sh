#!/usr/bin/env bash
# fl_druid_1116.sh (2026-11-16; user: "Run both tonight"): fl_hotfix_1116.sh's druid part (Wild Growth's coefficient 3.3% -> 6.6% a
# tick, hotfix push 114015) without its wait for the night's druid gear repair. That repair runs ninth in tonight_1116.sh, whose gear
# step was taking over two hours a class next to the PvP queue (the warrior's alone: 12:20 -> past 14:26), so the druid would have
# started tomorrow. The search plays the current healer set (made before the re-pin); the night's druid gear repair re-makes the set
# later, so its heal values get one more heal_values.py druid run after that repair (the morning wrap).
# The waiting druid subshell of fl_hotfix_1116.sh was stopped by Claude (Stop-Process) before this started. The markers are the same
# ones (deep-runs/fh1116/), so a resumed fl_hotfix_1116.sh skips what this finished.
# Steps: deep_heal.py druid --fresh, one cycle (talents and the heal-choice policy); the healer set for the winner; the healer filler
# pass; validate; GearCheck's healer values; the add-on file (one addon_values.py at a time); the druid pages after the shaman part's
# regen; the guide checks and the page audit.
# Full power: BelowNormal on 10 of 12 logical processors. Log deep-runs/hotfix-1116.log (steps), dru1116-heal.log, hf1116-tail.log.
#   bash _reference/data/deep-runs/fl_druid_1116.sh
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
M=$L/fh1116
LOG=$L/hotfix-1116.log
HL=_reference/data/heallab
D=_reference/data
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-2}" -Priority "${PRIORITY:-BelowNormal}" >> $LOG 2>&1
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
running() {   # running <pattern>: a bash or python process whose command line holds the pattern is alive (not this check itself)
  powershell -NoProfile -Command "if (Get-CimInstance Win32_Process | Where-Object { (\$_.Name -eq 'bash.exe' -or \$_.Name -eq 'python.exe') -and \$_.CommandLine -like '*$1*' -and \$_.CommandLine -notlike '*CommandLine -like*' }) { exit 0 } else { exit 1 }" 2>/dev/null
}
addon_idle() { while running "characters/addon_values.py"; do sleep 60; done; }

LG=dru1116-heal.log
say "fl_druid_1116 start (the druid part, without the wait for the night's druid gear repair)"
run deep-heal-druid $LG python -u $HL/deep_heal.py druid --fresh --cycles 1 --jobs 6 || say "WARNING: deep_heal druid failed"
run heal-gear-druid $LG python -u $HL/heal_gear.py druid --fresh --jobs 4 || say "WARNING: heal_gear druid failed"
run heal-filler-druid $LG python -u $HL/filler_pass.py druid --build restoration-ml-heal --write --jobs 6 || say "WARNING: healer filler pass failed"
run validate-druid $LG python -u $D/validate_builds.py || { say "STOP (druid): validate_builds failed ($LG)"; exit 1; }
run heal-values-druid $LG python -u $HL/heal_values.py druid --jobs 6 || say "WARNING: heal_values druid failed"
until [ -e $M/shaman-addon-tried ] || [ -e $M/shaman-finished ]; do sleep 60; done
addon_idle
run addon-values-druid $LG python -u $D/characters/addon_values.py || say "WARNING: addon_values failed"
until [ -e $M/shaman-finished ]; do sleep 60; done   # one regen at a time (both write the shared pages)
run regen-druid hf1116-tail.log python -u $D/rebuild.py druid --steps regen || say "WARNING: druid regen failed"
say "druid part done"
run guide-check-druid hf1116-tail.log python -u $D/level_guides.py --check || say "WARNING: by-level guide check lists problems (hf1116-tail.log)"
run guides-druid hf1116-tail.log python -u $D/guides.py --check --write || say "WARNING: guides --check lists passages to rewrite (hf1116-tail.log)"
run page-lint-druid hf1116-tail.log python -u $D/page_lint.py --write || say "WARNING: page_lint lists findings (_reference/page-lint.md)"
say "druid all done (review the Restoration guide's stamp, heal_values druid again after the night's druid gear repair, commit with the night, message the Addons session)"
