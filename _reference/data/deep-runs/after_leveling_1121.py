"""After the leveling numbers (2026-11-21, the audit session's order for the gear re-make): the tank lane no longer starts by itself.
  1. wait for "numbers done" in deep-runs/pass-1120.log (the leveling queue's compute);
  2. the stale tier sets first: every raid page pick whose interim tier race (raidsim/tier-best.json) found a tier's own set beaten by a
     lower tier's set or by the standard set gets its sets made again for it (raidsim/pick_tiers.py --make: Raid BiS and Pre-BiS, chosen
     in a full raid for the pick under its current rotation; then dungeon_tier.py --fresh), then tier_best.py for those classes, the raid
     regen and the page lint; a marker in the log ("stale sets done") for Claude's review and push;
  3. the tank lane (deep-runs/tank_lane_1120c.sh, which its waiting copy had been stopped for);
  4. the remaining picks' sets (every other pick with tier sets, Beast-Survival's first sets), tier_best.py for every class, the raid
     regen, page_stat_weights.py --all for GearCheck's raid values, and the page lint; the bear's after its lane, by hand.
Log deep-runs/after-leveling-1121.log; markers in deep-runs/al1121/ (a step done is skipped on a restart).

    python -u _reference/data/deep-runs/after_leveling_1121.py
"""
import json
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
D = ROOT / "_reference" / "data"
L = D / "deep-runs"
LOG = L / "after-leveling-1121.log"
M = L / "al1121"
TB = D / "raidsim" / "tier-best.json"
env = dict(os.environ, PYTHONIOENCODING="utf-8", WOW_FOREVER_NO_RACIALS="1",
           WOW_FOREVER_SIM=str(pathlib.Path.home() / ".wow-forever-tools/wowsims-forever-y"))


def say(msg):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"=== {time.strftime('%Y-%m-%d_%H:%M')} {msg}\n")


def run(mark, args, shell=False):
    m = M / mark
    if m.exists():
        return 0
    with open(LOG, "a", encoding="utf-8") as log:
        log.write(f"##### {time.strftime('%Y-%m-%d_%H:%M')} {mark}: {' '.join(map(str, args)) if not shell else args}\n")
        log.flush()
        rc = subprocess.run(args if not shell else args, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, shell=shell).returncode
    say(f"{mark} rc={rc}")
    if rc == 0:
        m.touch()
    return rc


def picks(stale):
    """[(class, spec, entry, build)] from the interim race: the stale ones (a tier's own set beaten) or the others with tier sets."""
    rec = json.load(open(TB, encoding="utf-8"))
    out = []
    for cls, specs in rec.items():
        for spec, r in specs.items():
            beaten = any(v.get("set") != t for t, v in (r.get("tiers") or {}).items() if t in (r.get("sets") or {}))
            if beaten == stale:
                out.append((cls, spec, r["entry"], r["build"]))
    return out


def remake(cls, spec, entry, build, tag):
    py = sys.executable
    rc = run(f"{tag}-make-{cls}-{spec.replace('/', '-').replace(' ', '_')}",
             [py, "-u", str(D / "raidsim" / "pick_tiers.py"), cls, spec, "--entry", entry, "--build", build, "--make"])
    if rc == 0:
        run(f"{tag}-dungeon-{cls}-{spec.replace('/', '-').replace(' ', '_')}",
            [py, "-u", str(D / "raidsim" / "dungeon_tier.py"), cls, "--spec", spec, "--fresh"])


def main():
    M.mkdir(exist_ok=True)
    py = sys.executable
    if "numbers done" not in (L / "pass-1120.log").read_text(encoding="utf-8", errors="replace"):
        say("waiting for the leveling queue's compute (numbers done in pass-1120.log)")
        while "numbers done" not in (L / "pass-1120.log").read_text(encoding="utf-8", errors="replace"):
            time.sleep(60)
    say("start")
    stale = picks(True)
    say("stale sets: " + "; ".join(f"{c} {s}" for c, s, _, _ in stale))
    for cls, spec, entry, build in stale:
        remake(cls, spec, entry, build, "stale")
    classes = sorted({c for c, _, _, _ in stale})
    if classes:
        run("stale-tierbest", [py, "-u", str(D / "raidsim" / "tier_best.py"), *classes, "--write"])
    run("stale-regen", [py, "-u", str(L / "raid_regen_1120.py")])
    say("stale sets done (Claude: review the tier tables, push the raid pages by path, tell the audit session)")
    run("tank-lane", [r"C:\Program Files\Git\usr\bin\bash.exe", "_reference/data/deep-runs/tank_lane_1120c.sh"])   # Git Bash, not WSL's
    say("tank lane done")
    rest = picks(False)
    for cls, spec, entry, build in rest:
        remake(cls, spec, entry, build, "rest")
    run("rest-tierbest", [py, "-u", str(D / "raidsim" / "tier_best.py"), "--write"])
    run("rest-regen", [py, "-u", str(L / "raid_regen_1120.py")])
    run("rest-weights", [py, "-u", str(D / "raidsim" / "page_stat_weights.py"), "--all"])
    say("all done (Claude: review, push, the Addons message: GearCheck's raid values; the bear's sets after its lane)")


if __name__ == "__main__":
    main()
