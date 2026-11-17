"""A character's next talent points, raced in the fight lab (2026-11-17; user, asked whether the planner should test the options for a
character off the page's order: "Yes, test the options").

The planner listed the page's remaining points in the page's order from where the character is (plan.talents_check's queue). A
character off that order was then told a slower point: Arcea at 37 had Arctic Reach next, and Missile Barrage was 1.1 s a kill faster
there (33.99 against 35.10 s). Now the same remaining points are put in order one at a time, so the destination stays the page's build:
- at each next point, every remaining talent that is legal to add (rank cap, five points per tier, prerequisites) is raced at the level
  the point is taken, on common dice (the fight lab's leveling setup for the page's rotation, FIGHTS fights, seed SEED), and the fastest
  is taken. Within NOISE of the page's next point, the page's point is kept;
- a signature talent of the spec (signature.py's rule: the talents granting its required spells) is taken as soon as its tree allows,
  as every order of the project does;
- that order and the page's order are then raced over the planned levels (each level's build, weighted by level as fl_levels does). The
  page's order stays unless the raced one is faster by NOISE.
Tank characters (a tank-first order of their own) and respecs are not raced (plan.talents_check decides).

    python _reference/data/characters/next_talents.py <character>     # print the race for a character (no page written)
"""
import concurrent.futures as CF
import importlib.util
import json
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
FIGHTS, SEED, NOISE, POINTS = 3000, 1, 0.005, 6
_FR = {}


def fightlab_run():
    if "m" not in _FR:
        for p in (str(DATA), str(DATA / "fightlab")):
            if p not in sys.path:
                sys.path.insert(0, p)
        m = sys.modules.get("fightlab_run")
        if m is None:
            spec = importlib.util.spec_from_file_location("fightlab_run", DATA / "fightlab" / "run.py")
            m = importlib.util.module_from_spec(spec)
            sys.modules["fightlab_run"] = m
            spec.loader.exec_module(m)
        _FR["m"] = m
    return _FR["m"]


def _ttk(job):
    cls, rot, alloc, level, fights, seed = job
    try:
        return fightlab_run().simulate(cls, dict(alloc), level, rot, fights, seed, 0)["time_per_kill"]
    except Exception as e:   # noqa: BLE001
        print(f"  next_talents: {type(e).__name__}: {e}", flush=True)
        return float("inf")


def _sig():
    if str(DATA) not in sys.path:
        sys.path.insert(0, str(DATA))
    import signature as SG
    return SG


def signature_talents(cls, spec):
    """The talents that grant the spec's required spells (the leveling rule), any the character may still take."""
    SG = _sig()
    rl = SG.rule(cls, spec) or {}
    return set(SG.granting_talents(cls, rl.get("required") or []))


def race(cls, rot, spec, have, queue, levels, fights=FIGHTS, seed=SEED, workers=4, pool=None):
    """The next len(levels) points: have {talent: ranks} now, queue the page's remaining points in its order (one name a point),
    levels the level each point is taken at. -> {"path": [(level, talent)], "page": [...], "steps": [...], "page_s", "raced_s",
    "changed"}; times are the fight lab's seconds a kill."""
    SG = _sig()
    info = SG.talent_info(cls)
    n = min(len(levels), len(queue))
    levels, page = list(levels[:n]), list(queue[:n])
    sig = signature_talents(cls, spec)
    cache = {}
    own = pool is None and workers > 1
    ex = CF.ProcessPoolExecutor(max_workers=workers) if own else pool

    def times(items):
        """[(alloc, level)] -> [seconds a kill], each distinct build and level run once."""
        todo = [(a, L) for a, L in items if (tuple(sorted(a.items())), L) not in cache]
        seen, jobs = set(), []
        for a, L in todo:
            k = (tuple(sorted(a.items())), L)
            if k not in seen:
                seen.add(k)
                jobs.append((k, (cls, rot, k[0], L, fights, seed)))
        res = (ex.map(_ttk, [j for _, j in jobs], chunksize=1) if ex else map(_ttk, [j for _, j in jobs]))
        for (k, _), v in zip(jobs, res):
            cache[k] = v
        return [cache[(tuple(sorted(a.items())), L)] for a, L in items]

    try:
        cur, rest, out, steps = dict(have), list(queue), [], []
        for i in range(n):
            L = levels[i]
            names = []
            for t in rest:
                if t not in names and t in info and SG._addable(info, cur, t):
                    names.append(t)
            if not names:   # nothing legal (cannot happen for a legal page order): the page's next point
                names = [rest[0]]
            due = [t for t in names if t in sig and not cur.get(t)]
            if due:
                pick, why, ts = due[0], "signature", {}
            elif len(names) == 1:
                pick, why, ts = names[0], "only", {}
            else:
                vals = times([(dict(cur, **{t: cur.get(t, 0) + 1}), L) for t in names])
                ts = dict(zip(names, vals))
                best = min(names, key=lambda t: ts[t])
                first = next((t for t in rest if t in ts), names[0])   # the page's next point among the legal ones
                pick = first if ts[first] <= ts[best] * (1 + NOISE) else best
                why = "raced"
            steps.append({"level": L, "pick": pick, "page": rest[0], "why": why, "times": {t: round(v, 2) for t, v in ts.items()}})
            out.append((L, pick))
            cur[pick] = cur.get(pick, 0) + 1
            rest.remove(pick)

        def score(path):
            a, per = dict(have), {}
            for L, t in path:
                a[t] = a.get(t, 0) + 1
                per[L] = dict(a)   # the build at the end of each level (owed points share the current level)
            lv = sorted(per)
            ts = times([(per[L], L) for L in lv])
            w = sum(L / 10 for L in lv)
            return sum(t * L / 10 for t, L in zip(ts, lv)) / w if lv else 0.0

        page_path = list(zip(levels, page))
        ps, rs = score(page_path), score(out)
        changed = [t for _, t in out] != page and rs < ps * (1 - NOISE)
        return {"path": out if changed else page_path, "page": page_path, "raced": out, "steps": steps, "page_s": round(ps, 2),
                "raced_s": round(rs, 2), "changed": changed, "fights": fights, "seed": seed, "rotation": rot}
    finally:
        if own:
            ex.shutdown()


def note(r):
    """One line for the page and the checklist: what the race changed, or that it confirms the page's order."""
    if not r:
        return ""
    if not r["changed"]:
        return f"the fight lab raced your next points from your own talents: the page's order is as fast ({r['page_s']:.2f} s a kill over those levels)"
    first = next((s for s in r["steps"] if s["pick"] != s["page"]), None)
    lead = ""
    if first and first["times"]:
        a, b = first["times"].get(first["pick"]), first["times"].get(first["page"])
        if a and b:
            lead = f"; at {first['level']}: {first['pick']} {a:.2f} s a kill, {first['page']} {b:.2f} s"
    return (f"raced in the fight lab from your own talents: {r['raced_s']:.2f} s a kill over those levels against {r['page_s']:.2f} s "
            f"for the page's order{lead}")


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("character")
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    sys.path[:0] = [str(HERE)]
    import plan as P
    d = ROOT / "_characters" / a.character
    cfg = json.loads((d / "character.json").read_text(encoding="utf-8"))
    cfg.setdefault("name", a.character)
    snap = {k: json.loads((d / "armory" / f"{k}.json").read_text(encoding="utf-8")) for k in ("profile", "specializations")}
    said = d / "level-said.json"
    lv = json.loads(said.read_text(encoding="utf-8")).get("level") if said.exists() else snap["profile"]["level"]
    P.NEXT_TALENTS_WORKERS = a.workers
    res = P.talents_check(cfg, snap, lv)
    r = P.LAST_TALENT_RACE.get("race")
    print(json.dumps({k: v for k, v in (r or {}).items() if k != "steps"}, indent=1))
    for s in (r or {}).get("steps", []):
        print(s)
    print(note(r))


if __name__ == "__main__":
    main()
