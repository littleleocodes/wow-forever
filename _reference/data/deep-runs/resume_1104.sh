#!/usr/bin/env bash
# 2026-11-04 (user: "Resume the runs, 3 lanes at a time, hunter first"), after the 11:05 reboot: seven raid lanes (each a bench at
# every core) plus the three leveling lanes and the one-tree searches had run at once. This runs the nine 2026-11-02 patch lanes
# through three slots: the hunter's raid lane first (its entries ran a 2 s pet without its Faster Attack passive and no quiver haste
# since the port, fixed in 81c3aaa3; its r1103/hun-* markers were removed, so it redoes everything from its races), then the leveling
# queue, the two short raid lanes (mage, paladin), the one-tree leveling searches, shaman, warlock, warrior, rogue. Every lane resumes
# from its own markers. After the last lane: validate, rankings and gear links, pages, guide check, a checkpoint commit.
# Log: deep-runs/resume-1104.log (each lane's own log as before; its stdout in deep-runs/<lane>.console). Resume: the same command.
# Stop: kill this script's bash, then each lane's bash (parent and subshell) and its python / foreverbench children (TaskStop on the
# task alone does not stop a lane: memory, 2026-11-04 06:50).
cd F:/wow-forever || exit 1
export PYTHONIOENCODING=utf-8
L=_reference/data/deep-runs
LOG=$L/resume-1104.log
MAX=${MAX:-3}
# 12:20 (user: three lanes still froze the desktop; 12:40: "make sure the CPU doesn't max out at 100%, I still need to be able to
# function on my PC"): throttle.ps1 pins this bash, and by inheritance every lane, python and bench process it starts (tested), to all
# but RESERVE_CPUS (default 4) of the logical processors at BelowNormal priority: the run can use at most 8 of 12 (about 67% in Task
# Manager), the other 4 stay the desktop's, and on the shared 8 the desktop wins. Go's NumCPU follows the mask (a bench starts 8
# workers); python's cpu_count does not (the leveling lanes' 12 fight-lab processes share the 8). RESERVE_CPUS=6 halves it.
WINPID=$(cat /proc/$$/winpid 2>/dev/null)
[ -n "$WINPID" ] && powershell -NoProfile -ExecutionPolicy Bypass -File "$L/throttle.ps1" -ProcId "$WINPID" -Reserve "${RESERVE_CPUS:-4}" | tee -a "$LOG"
LANES=(
  "raid-hunter|$L/raid_hunter_1103.sh"
  "leveling|$L/patch_1103.sh"
  "raid-mage|$L/raid_mage_1103.sh"
  "raid-paladin|$L/raid_paladin_1103.sh"
  "pure|$L/pure_1103.sh"
  "raid-shaman|$L/raid_shaman_1103.sh"
  "raid-warlock|$L/raid_warlock_1103.sh"
  "raid-warrior|$L/raid_warrior_1103.sh"
  "raid-rogue|$L/raid_rogue_1103.sh"
)
say() { echo "=== $(date +%F_%H:%M) $*" | tee -a "$LOG"; }
declare -A PIDS
start_lane() {   # start_lane <name> <script>
  bash "$2" > "$L/$1.console" 2>&1 &
  PIDS[$!]=$1
  say "start $1 (pid $!, ${#PIDS[@]} of $MAX slots)"
}
reap() {         # log and free every finished lane
  local pid
  for pid in "${!PIDS[@]}"; do
    if ! kill -0 "$pid" 2>/dev/null; then
      wait "$pid"; local rc=$?
      say "done ${PIDS[$pid]} rc=$rc"
      unset "PIDS[$pid]"
    fi
  done
}

say "resume: ${#LANES[@]} lanes, $MAX at a time, hunter first"
i=0
while [ $i -lt ${#LANES[@]} ] || [ ${#PIDS[@]} -gt 0 ]; do
  reap
  while [ ${#PIDS[@]} -lt $MAX ] && [ $i -lt ${#LANES[@]} ]; do
    lane=${LANES[$i]}
    start_lane "${lane%%|*}" "${lane#*|}"
    i=$((i + 1))
  done
  sleep 60
done
say "all lanes done"

# After the last raid lane: rankings and gear links (ml_builds --rank runs gear_links.py), the pages, the guide check, a checkpoint.
wrap() { local mk=$1; shift; say "wrap $mk"; "$@" >> "$L/wrap-1104.log" 2>&1; say "wrap $mk rc=$?"; }
wrap validate python -u _reference/data/validate_builds.py
wrap rank python -u _reference/data/raidsim/ml_builds.py --rank
wrap regen python -u _reference/data/rebuild.py --steps regen
wrap guides python -u _reference/data/guides.py --check --write
git -c core.safecrlf=false add -A
git -c core.safecrlf=false commit -q -F - <<EOF
Checkpoint $(date +%F_%H:%M): the 2026-11-02 patch queues done (resume_1104.sh, three lanes at a time)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
EOF
say "all done (committed $(git rev-parse --short HEAD))"
