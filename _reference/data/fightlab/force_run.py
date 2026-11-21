"""Forced runs for the leveling play check's Lg (2026-11-21, the audit session's ask). A spell the lab never presses goes into the
priority and races the rotation as tuned, on the same fights (common random numbers):
- top: cast whenever it is ready, affordable and in reach;
- filler: cast in place of the filler (the spell the tuned rotation casts most at that level, or the wand) whenever it can.
A dot, a buff, a shield or a heal over time is cast only while it is not up. A rule that vetoes the spell is lifted for the run.

A spell slower in both placements at every level tried, on both seeds, gets a verdict in fightlab/never-tried.json (class -> rotation
-> spell; Lg reads it): "forced into the priority on <date>: slower by X% (...)". A spell faster by the leveling bar (0.5% on both
seeds) at some level is a lead for the class's rotation tune, never a page change by itself.

`--add` and `--pay` test a talent the page build lacks: the audit's circular case, Hunter's Mark held off because no build took Expose
Prey and Expose Prey never taken because the mark was off. `--add "Expose Prey=2" --pay "Talent A,Talent B"` takes the ranks from the
listed talents in turn (the legal state checked at each level); a level where it cannot be done legally is skipped and said.

Nothing in the lab's shared files changes: the module's decide is wrapped in this process only, so a running search is untouched.

    python _reference/data/fightlab/force_run.py <class> --guide <spec> --spell "Fireball" --spell "Scorch"
        [--levels 20,30,40,50,60] [--where top,filler] [--fights 2000] [--seeds 1,2] [--jobs 4] [--write]
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path[:0] = [str(HERE), str(DATA)]
OUT = HERE / "never-tried.json"
BAR = 0.005


def _init():
    sys.path[:0] = [str(HERE), str(DATA)]


def wrap(mod, names, where, filler):
    """The module's decide with `names` forced in (see the module docstring)."""
    from engine import MELEE_RANGE
    orig = mod.decide
    for n in names:
        (mod.veto or {}).pop(n, None)

    def castable(fight):
        p, t, m = fight.p, fight.t, fight.m
        for n in names:
            s = mod.spells.get(n)
            if s is None or not p.ready(s.name, t) or not fight.can_afford(s, mod.mana_cost(s)):
                continue
            if s.dot and fight.dot_active(s.name):
                continue
            if (s.kind == "buff" or s.absorb or s.hot) and p.buff(s.name, t):
                continue
            reach = s.range if s.kind not in ("melee",) and s.range else MELEE_RANGE
            if (s.kind == "melee" and not m.in_melee) or m.dist > max(reach, MELEE_RANGE) + 0.5:
                continue
            return s
        return None

    def decide(fight):
        if where == "top":
            s = castable(fight)
            return s if s is not None else orig(fight)
        act = orig(fight)
        if act == "wand" or getattr(act, "name", None) == filler:
            s = castable(fight)
            if s is not None:
                return s
        return act

    mod.decide = decide
    return mod


def _job(a):
    import run as FR
    from engine import Session
    cls, rot, alloc, level, fights, seed, names, where, filler = a
    mod = FR.make_module(cls, alloc, level, rot)
    missing = [n for n in names if n not in mod.spells]
    if where:
        wrap(mod, names, where, filler)
    out = Session(mod, level=level, fights=fights, seed=seed, mob_level_offset=0).run()
    k = max(1, out.get("kills") or 1)
    casts = {s: round(n / k, 2) for s, n in (out.get("casts") or {}).items() if n}
    return {"seconds": out["time_per_kill"], "casts": casts, "missing": missing}


def pay(where, alloc, add, pay_from):
    """`alloc` with `add` ({talent: ranks}) taken from `pay_from` in turn, or (None, why) when the points run short (legality: legal())."""
    st = {tree: {} for tree in set(where.values())}
    for n, r in alloc.items():
        st[where[n]][n] = r
    need = 0
    for n, r in add.items():
        have = st[where[n]].get(n, 0)
        if have < r:
            st[where[n]][n] = r
            need += r - have
    for n in pay_from:
        while need and st[where[n]].get(n, 0) > 0:
            st[where[n]][n] -= 1
            if not st[where[n]][n]:
                del st[where[n]][n]
            need -= 1
    if need:
        return None, f"{need} point(s) short after paying from {', '.join(pay_from)}"
    return {n: r for v in st.values() for n, r in v.items() if r}, None


def legal(cls, alloc, level):
    import validate_builds as VB
    T = VB.load_forever()[cls]
    where = {n: tree for tree, d in T.items() for n in d["talents"]}
    st = {}
    for n, r in alloc.items():
        st.setdefault(where[n], {})[n] = r
    e = []
    VB.check_state(T, st, "forced", e)
    pts = sum(alloc.values())
    if pts > max(0, level - 9):
        e.append(f"{pts} points at level {level} (at most {max(0, level - 9)})")
    return e


def main():
    import level_guides as LG
    import run as FR
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--guide", required=True, help="the guide's spec (level-guides/<class>.json), whose page pick and rotation are used")
    ap.add_argument("--spell", action="append", required=True)
    ap.add_argument("--levels", default="20,30,40,50,60")
    ap.add_argument("--where", default="top,filler")
    ap.add_argument("--fights", type=int, default=2000)
    ap.add_argument("--seeds", default="1,2")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--add", action="append", default=[], help="Talent=ranks the build gets at every level tried (see --pay)")
    ap.add_argument("--pay", default="", help="comma-separated talents the added ranks come from, in turn")
    ap.add_argument("--together", action="store_true", help="force the listed spells together (default: each on its own)")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    b, order, prov, rot = LG.pick(a.cls, a.guide)
    if not b:
        sys.exit(f"no leveling page pick for {a.cls} {a.guide}")
    ob = {"allocation": b["allocation"], "order": order}
    levels = [int(x) for x in a.levels.split(",")]
    seeds = [int(x) for x in a.seeds.split(",")]
    wheres = [w for w in a.where.split(",") if w]
    add = {x.split("=")[0]: int(x.split("=")[1]) for x in a.add}
    pay_from = [x.strip() for x in a.pay.split(",") if x.strip()]
    import validate_builds as VB
    where = {n: tree for tree, d in VB.load_forever()[a.cls].items() for n in d["talents"]}
    allocs, skipped = {}, {}
    for L in levels:
        al = FR.allocation_at(ob, L) if L >= 10 else {}
        if add:
            al2, why = pay(where, al, add, pay_from)
            if al2 is None:
                skipped[L] = why
                continue
            e = legal(a.cls, al2, L)
            if e:
                skipped[L] = "; ".join(e)[:200]
                continue
            al = al2
        allocs[L] = al
    for L, why in skipped.items():
        print(f"   level {L} skipped: {why}", flush=True)
    jobs = [(a.cls, rot, allocs[L], L, a.fights, s, a.spell, None, None) for L in allocs for s in seeds]
    with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
        base = dict(zip([(L, s) for L in allocs for s in seeds], pool.map(_job, jobs, chunksize=1)))
        fill = {L: max((c for c in base[(L, seeds[0])]["casts"].items() if c[0] not in a.spell), key=lambda kv: kv[1], default=(None, 0))[0]
                for L in allocs}
        groups = [a.spell] if a.together else [[n] for n in a.spell]
        fj = [(a.cls, rot, allocs[L], L, a.fights, s, g, w, fill[L]) for g in groups for w in wheres for L in allocs for s in seeds]
        forced = dict(zip([(tuple(g), w, L, s) for g in groups for w in wheres for L in allocs for s in seeds], pool.map(_job, fj, chunksize=1)))
    today = datetime.date.today().isoformat()
    rec = json.loads(OUT.read_text(encoding="utf-8")) if (a.write and OUT.exists()) else {}
    with_add = f"; with {', '.join(f'{k} {v}' for k, v in add.items())}" if add else ""
    for g in groups:
        print(f"== {a.cls} {a.guide} ({b['id']}, rotation {rot}): forced {', '.join(g)}"
              + (f" with {', '.join(f'{k} {v}' for k, v in add.items())} paid from {', '.join(pay_from)}" if add else ""), flush=True)
        rows, lead = [], []
        for w in wheres:
            for L in allocs:
                fr = [forced[(tuple(g), w, L, s)] for s in seeds]
                d = [f["seconds"] / base[(L, s)]["seconds"] - 1 for f, s in zip(fr, seeds)]
                pressed = {n: fr[0]["casts"].get(n, 0) for n in g}
                miss = fr[0]["missing"]
                print(f"   {w:6s} {L:2d}: {base[(L, seeds[0])]['seconds']:.2f} -> {fr[0]['seconds']:.2f} s a kill "
                      f"({', '.join(f'{x:+.2%}' for x in d)}), pressed {pressed}" + (f", filler {fill[L]}" if w == "filler" else "")
                      + (f"; NOT IN THE MODULE: {', '.join(miss)}" if miss else ""), flush=True)
                rows.append({"where": w, "level": L, "delta": [round(x, 4) for x in d], "pressed": pressed, "missing": miss,
                             "filler": fill[L] if w == "filler" else None})
                if all(x <= -BAR for x in d):
                    lead.append(f"{w} at {L}: {max(d):+.2%}")
        tried = [r for r in rows if not r["missing"] and any(r["pressed"].values())]
        if lead:
            verdict = "LEAD: " + "; ".join(lead)
            print(f"   LEAD for the rotation tune (faster by the bar on every seed): {'; '.join(lead)}", flush=True)
        elif not tried:
            verdict = "never cast when forced (not in the module, never in reach, or never affordable)"
            print(f"   no verdict: {verdict}", flush=True)
        else:
            lo = min(min(r["delta"]) for r in tried)
            span = (f"{' and '.join(wheres)}, levels {min(allocs)}-{max(allocs)}, seeds {'/'.join(map(str, seeds))}, "
                    f"{a.fights} fights")
            verdict = (f"forced into the priority on {today} ({span}): slower at every level, by {lo:.1%} at least" if lo >= 0 else
                       f"forced into the priority on {today} ({span}): within noise at best ({lo:+.2%}), never faster by the bar") + with_add
            print(f"   verdict: {verdict}", flush=True)
        if a.write:
            for n in g:
                rec.setdefault(a.cls, {}).setdefault(rot, {})[n + (f" (with {', '.join(f'{k} {v}' for k, v in add.items())})" if add else "")] = verdict
            rec.setdefault("_runs", []).append({"class": a.cls, "guide": a.guide, "build": b["id"], "rotation": rot, "spells": g,
                                                "add": add, "pay": pay_from, "date": today, "rows": rows, "skipped": skipped})
    if a.write:
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
