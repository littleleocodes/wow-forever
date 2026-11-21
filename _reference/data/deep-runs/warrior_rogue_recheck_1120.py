"""After the clean play check of 2026-11-20 evening: Jom Gabbar's dead line left seven warrior rotation files (dead_lines_1120.py), so the
three warrior damage entries are raced again (dummy and environments: the race fingerprints follow the rotation files), then the play
check for the warrior (all entries; the tank entry's rotation is unchanged) and the rogue (the check's talent-ability fix). Log
deep-runs/warrior-rogue-recheck-1120.log."""
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
LOG = ROOT / "_reference/data/deep-runs/warrior-rogue-recheck-1120.log"
R = "_reference/data/raidsim"
STEPS = []
for e in ("arms-2h-raid", "fury-dw-raid", "arms-battle-raid"):
    STEPS += [[f"{R}/run.py", "warrior", "--spec", e, "--write"], [f"{R}/run.py", "warrior", "--spec", e, "--env", "environments", "--write"]]
STEPS += [[f"{R}/play_check.py", "warrior", "rogue", "--write"]]
env = dict(os.environ, PYTHONIOENCODING="utf-8", WOW_FOREVER_NO_RACIALS="1",
           WOW_FOREVER_SIM=str(pathlib.Path.home() / ".wow-forever-tools/wowsims-forever-y"))
with open(LOG, "a", encoding="utf-8") as log:
    for s in STEPS:
        log.write(f"##### {time.strftime('%Y-%m-%d_%H:%M')} {' '.join(s)}\n")
        log.flush()
        rc = subprocess.run([sys.executable, "-u", *s], cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT).returncode
        log.write(f"=== {time.strftime('%Y-%m-%d_%H:%M')} rc={rc}\n")
        log.flush()
    log.write(f"=== {time.strftime('%Y-%m-%d_%H:%M')} all done\n")
