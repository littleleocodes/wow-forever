"""One command for a class's deep optimisation and everything after it (2026-10-03, user request: the deep runs ready for every class
before the beta ends; the shaman's run on 2026-10-02/03 was the pilot).

    python -u _reference/data/deep_class.py <class> [--steps damage,heal,tank,builds,race,pages] [--cycles 3] [--smoke]

Steps, in order (a step the class has nothing for is skipped; the three deep steps resume from their own records, so a run that stops
can be started again with the same command):
- damage: raidsim/deep_opt.py <class> (every raid damage spec of the class's machine-learning records, raidsim/ml/);
- heal:   heallab/deep_heal.py <class> (every healer spec of the class: deep_heal.HEAL_SPECS, the priest's Holy and Discipline);
- tank:   raidsim/deep_tank.py <class> (the class's tank entry: deep_tank.TANK_ENTRY);
- builds: raidsim/ml_builds.py <class> --builds (the full-raid winners as `-ml-raid` builds), then validate_builds.py;
- race:   every raid entry of the class raced again (run.py --write, then --env environments --write: the pages' full-raid numbers and
          casts), ml_builds.py <class> --tidy-winners, ml_builds.py <class> --rank (the rankings and the gear links) and
          unused_abilities.py --write (every class: it writes one file);
- pages:  rebuild.py --steps regen (every class: the index pages rank across classes), linkcheck.py.
--smoke runs the deep steps with tiny budgets into separate records (raidsim/deep-smoke/, heallab/deep-smoke/; nothing else is written)
and stops: a test that the class runs end to end. Output goes to the console and to _reference/data/deep-runs/<class>.log (appended).
Simulations of the community's model of the beta and of the healer lab's stated assumptions, not in-game measurements.
"""
import argparse
import datetime
import json
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LOGS = HERE / "deep-runs"
STEPS = ("damage", "heal", "tank", "builds", "race", "pages")
HEAL = {"shaman", "priest", "paladin", "druid"}   # heallab/deep_heal.py HEAL_SPECS
TANK = {"warrior", "paladin", "druid"}            # raidsim/deep_tank.py TANK_ENTRY
CLASSES = ("druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior")


def has_damage(cls):
    return any(p.name.startswith(f"{cls}-") for p in (HERE / "raidsim" / "ml").glob("*.json"))


def entries(cls):
    specs = json.load(open(HERE / "raidsim" / "specs.json", encoding="utf-8"))
    return [e for e, v in specs.get(cls, {}).items() if isinstance(v, dict) and "apl" in v]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", choices=CLASSES)
    ap.add_argument("--steps", default=",".join(STEPS), help=f"comma-separated subset of {', '.join(STEPS)}")
    ap.add_argument("--cycles", type=int, default=3)
    ap.add_argument("--smoke", action="store_true", help="the deep steps on tiny budgets into separate records, then stop (a test)")
    a = ap.parse_args()
    steps = [s for s in a.steps.split(",") if s]
    bad = [s for s in steps if s not in STEPS]
    if bad:
        raise SystemExit(f"unknown steps {bad}; choose from {', '.join(STEPS)}")
    if a.smoke:
        steps = [s for s in steps if s in ("damage", "heal", "tank")]
    cls = a.cls
    LOGS.mkdir(exist_ok=True)
    logf = open(LOGS / f"{cls}.log", "a", encoding="utf-8")

    def log(m):
        line = f"{datetime.datetime.now():%Y-%m-%d %H:%M} {m}"
        print(line, flush=True)
        logf.write(line + "\n")
        logf.flush()

    def run(args, what):
        """A step's command, its output streamed to the console and the log; False when it fails."""
        log(f"$ {' '.join(str(x) for x in args)}")
        t0 = time.time()
        p = subprocess.Popen([sys.executable, "-u", *map(str, args)], cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             text=True, encoding="utf-8", errors="replace", env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
        for ln in p.stdout:
            print(ln, end="", flush=True)
            logf.write(ln)
        rc = p.wait()
        logf.flush()
        log(f"{what}: {'ok' if rc == 0 else f'FAILED (exit {rc})'} in {(time.time() - t0) / 60:.1f} min")
        return rc == 0

    smoke = ["--smoke", "--fresh"] if a.smoke else []   # a test starts over every time
    log(f"== {cls}: steps {', '.join(steps)}" + (" (smoke test)" if a.smoke else ""))
    plan = {
        "damage": ([[HERE / "raidsim" / "deep_opt.py", cls, "--cycles", a.cycles, *smoke]] if has_damage(cls) else []),
        "heal": ([[HERE / "heallab" / "deep_heal.py", cls, "--cycles", a.cycles, *smoke]] if cls in HEAL else []),
        "tank": ([[HERE / "raidsim" / "deep_tank.py", cls, "--cycles", a.cycles, *smoke]] if cls in TANK else []),
        "builds": [[HERE / "raidsim" / "ml_builds.py", cls, "--builds"], [HERE / "validate_builds.py"]],
        "race": ([[HERE / "raidsim" / "run.py", cls, "--spec", e, "--write"] for e in entries(cls)]
                 + [[HERE / "raidsim" / "run.py", cls, "--spec", e, "--env", "environments", "--write"] for e in entries(cls)]
                 + [[HERE / "raidsim" / "ml_builds.py", cls, "--tidy-winners"], [HERE / "raidsim" / "ml_builds.py", cls, "--rank"],
                    [HERE / "raidsim" / "unused_abilities.py", "--write"]]),
        "pages": [[HERE / "rebuild.py", "--steps", "regen"], [HERE / "linkcheck.py"]],
    }
    t0 = time.time()
    for s in steps:
        if not plan[s]:
            log(f"-- {s}: nothing for {cls}")
            continue
        log(f"-- {s}")
        for args in plan[s]:
            if not run(args, s):
                log(f"== stopped at {s}; fix the error and run the same command again (the deep steps resume from their records)")
                sys.exit(1)
    log(f"== {cls} done in {(time.time() - t0) / 3600:.1f} h")


if __name__ == "__main__":
    main()
