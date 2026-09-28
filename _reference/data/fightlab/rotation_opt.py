"""Tune the leveling rotations in the fight lab: rules on top of each class module's hand-written priority list.

    python _reference/data/fightlab/rotation_opt.py mage [--spec frost-leveling] [--write]
    python _reference/data/fightlab/rotation_opt.py --all [--write] [--jobs 10]

The rules are the engine's `veto` (engine.Fight.can_afford: outside them the spell counts as unaffordable, so the priority list
falls through to its next choice) plus the rest thresholds and the module's own `ROTATION_KNOBS`:
  * never cast a spell;
  * cast it only above a share of mana (keep mana for what matters);
  * cast it only while the mob has more than a share of its health left (no expensive casts on a dying mob), or only below one;
  * drink below / eat below (the downtime thresholds: rest earlier or later);
  * a module knob (the priest's wand-below and shield-below).
Local search like raidsim/apl_opt.py: every candidate plays the spec's leveling build (the class pipeline's hand draft for the
main spec model, the extra reports' builds for the others) at the pipeline's levels with common random numbers (seed 1,
`--fights`); the best candidates run again on seed 2 with `--confirm` fights, and a rule is kept only when it wins there by more
than `--min-gain` of the level-weighted time per kill (weights level / 10, as the races). With --write the rules go to
`fightlab/rotations/<class>-<spec>.json`, which `run.make_module` applies to every fight-lab run of that spec model
(WOW_FL_ROTATION=default switches them off; the mage regression runs without them).
"""
import argparse
import copy
import datetime
import json
import multiprocessing
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
sys.path.insert(0, str(ROOT / "_reference/data/scorer"))
sys.path.insert(0, str(HERE))
import run as FR  # noqa: E402  (fightlab/run.py)
import tables  # noqa: E402

MIN_MANA = (0.15, 0.3, 0.5)
MIN_HP = (0.1, 0.2, 0.35)
MAX_HP = (0.2, 0.35)
DRINK = (0.15, 0.25, 0.45, 0.6, 0.8)
EAT = (0.4, 0.5, 0.8, 0.9)


def targets(cls):
    """[(spec model, build id)] the fight lab plays for a class: the main spec's hand draft and every extra report's build."""
    P = getattr(FR.class_module(cls), "PIPELINE", {})
    out, seen = [], set()
    for spec, bid in [(P.get("spec"), P.get("hand"))] + [(x.get("spec"), x.get("build") or x.get("hand")) for x in P.get("extra_reports", [])]:
        if spec and bid and spec not in seen:
            seen.add(spec)
            out.append((spec, bid))
    return out, [int(x) for x in str(P.get("levels", "20,30,40,50,60")).split(",") if x]


def _init():
    import engine
    # a hopeless candidate (a Balance druid told not to cast Starfire on a wounded mob) times out after 3 minutes of fight time instead
    # of 10: no leveling fight here lasts a minute and a half, and 600 ten-minute fights per level stalled the search for hours (2026-09-28)
    engine.Fight.run.__defaults__ = (180.0,)
    orig = engine.Fight.run

    def run(self, max_time=180.0):   # a candidate that times out 20 fights is hopeless: stop it there (_run scores it as never killing)
        r = orig(self, max_time)
        if r == "timeout":
            _TIMEOUTS[0] += 1
            if _TIMEOUTS[0] > 20:
                raise _Hopeless()
        return r
    engine.Fight.run = run
    FR.apply_gear("greens")
    os.environ["WOW_FL_ROTATION"] = "default"   # the candidate's rules are passed explicitly


class _Hopeless(Exception):
    pass


_TIMEOUTS = [0]


def _run(job):
    cls, spec, bid, level, fights, seed, rot = job
    build = FR.load_build(cls, bid)
    _TIMEOUTS[0] = 0
    try:
        r = FR.simulate(cls, FR.allocation_at(build, level), level, spec, fights, seed, 0, rot=rot)
    except _Hopeless:
        return {"time_per_kill": 1e9, "deaths_per_100": 0.0, "casts": {}, "mana_per_kill": 0.0, "shares": {}}
    return {"time_per_kill": r["time_per_kill"], "deaths_per_100": r["deaths_per_100"], "casts": r["casts"], "mana_per_kill": r["mana_per_kill"],
            "shares": r.get("shares", {})}


def weighted(per_level):
    tot = sum(L / 10 for L in per_level)
    return sum(v * L / 10 for L, v in per_level.items()) / tot


def evaluate(pool, cls, spec, bid, levels, rots, fights, seed):
    """[{level: result}] for each rule set in rots."""
    jobs = [(cls, spec, bid, L, fights, seed, rot) for rot in rots for L in levels]
    res = pool.map(_run, jobs, chunksize=1)
    out = []
    k = 0
    for _ in rots:
        out.append({L: res[k + i] for i, L in enumerate(levels)})
        k += len(levels)
    return out


def describe(change):
    kind, spell, val = change
    return {"off": f"never cast {spell}", "min_mana": f"{spell} only above {val:.0%} mana", "min_hp": f"{spell} only while the mob has more than {val:.0%} health",
            "max_hp": f"{spell} only when the mob is below {val:.0%} health", "drink_below": f"drink below {val:.0%} mana",
            "eat_below": f"eat below {val:.0%} health", "knob": f"{spell} = {val}", "clear": f"drop the rules on {spell}"}[kind]


def apply_change(rot, change):
    rot = copy.deepcopy(rot)
    kind, spell, val = change
    if kind in ("drink_below", "eat_below"):
        rot[kind] = val
    elif kind == "knob":
        rot.setdefault("knobs", {})[spell] = val
    elif kind == "clear":
        rot.get("veto", {}).pop(spell, None)
    else:
        rot.setdefault("veto", {}).setdefault(spell, {})[kind] = True if kind == "off" else val
    return rot


MAIN_SHARE = 0.30   # a spell dealing this share of the damage at some level is the build's main attack: never switched off or starved


def candidates(rot, spells, mod_cls, main=()):
    """Rule candidates. The main attacks (MAIN_SHARE) are never switched off, limited to a dying mob or held above more than the
    lowest mana share: a Balance druid without Starfire could not kill, and every fight ran to the timeout (a 9-hour search, 2026-09-28)."""
    out = []
    veto = rot.get("veto", {})
    for s in spells:
        if veto.get(s):
            out.append(("clear", s, None))
        if s not in main and not veto.get(s, {}).get("off"):
            out.append(("off", s, True))
        out += [("min_mana", s, x) for x in (MIN_MANA[:1] if s in main else MIN_MANA) if veto.get(s, {}).get("min_mana") != x]
        out += [("min_hp", s, x) for x in MIN_HP if veto.get(s, {}).get("min_hp") != x]
        if s not in main:
            out += [("max_hp", s, x) for x in MAX_HP if veto.get(s, {}).get("max_hp") != x]
    cur_d = rot.get("drink_below", mod_cls.drink_below or tables.DRINK_BELOW)
    cur_e = rot.get("eat_below", mod_cls.eat_below or tables.EAT_BELOW)
    out += [("drink_below", None, x) for x in DRINK if abs(x - cur_d) > 1e-9]
    out += [("eat_below", None, x) for x in EAT if abs(x - cur_e) > 1e-9]
    for k, vals in (getattr(mod_cls, "ROTATION_KNOBS", {}) or {}).items():
        cur = rot.get("knobs", {}).get(k, getattr(mod_cls, k, None))
        out += [("knob", k, v) for v in vals if v != cur]
    return out


def search(pool, cls, spec, bid, levels, a):
    mod_cls = getattr(__import__(FR.MODULES[cls][0]), FR.MODULES[cls][1])
    rot0 = {}
    if not a.fresh and FR.rotation_file(cls, spec).exists():
        rot0 = {k: v for k, v in json.load(open(FR.rotation_file(cls, spec), encoding="utf-8")).items() if k in ("veto", "drink_below", "eat_below", "knobs")}
    rot = copy.deepcopy(rot0)
    base1 = evaluate(pool, cls, spec, bid, levels, [rot], a.fights, 1)[0]
    spells = sorted({s for L in levels for s, n in base1[L]["casts"].items() if n and s not in ("wand", "Wand", "Melee", "Auto Shot", "Melee (off-hand)")})
    main = {s for L in levels for s, sh in base1[L].get("shares", {}).items() if sh >= MAIN_SHARE}
    print(f"== {cls} {spec} ({bid}): levels {levels}, {len(spells)} spells cast; time/kill " + ", ".join(f"L{L} {base1[L]['time_per_kill']:.1f}s" for L in levels)
          + f" (weighted {weighted({L: base1[L]['time_per_kill'] for L in levels}):.2f}s)", flush=True)
    log = []
    for rnd in range(1, a.rounds + 1):
        cands = candidates(rot, spells, mod_cls, main)
        res = evaluate(pool, cls, spec, bid, levels, [apply_change(rot, c) for c in cands], a.fights, 1)
        w0 = weighted({L: base1[L]["time_per_kill"] for L in levels})
        scored = sorted(((weighted({L: r[L]["time_per_kill"] for L in levels}) / w0, i) for i, r in enumerate(res)), key=lambda x: x[0])
        top = [(sc, i) for sc, i in scored if sc < 1 - a.screen_gain][: a.top]
        if not top:
            print(f"  round {rnd}: {len(cands)} candidates, none ahead on seed 1 (best {1 - scored[0][0]:+.2%}: {describe(cands[scored[0][1]])})" if scored else "  no candidates", flush=True)
            break
        rots = [rot] + [apply_change(rot, cands[i]) for _, i in top]
        conf = evaluate(pool, cls, spec, bid, levels, rots, a.confirm, 2)
        w2 = weighted({L: conf[0][L]["time_per_kill"] for L in levels})
        best = None
        for k, (sc1, i) in enumerate(top, start=1):
            sc2 = weighted({L: conf[k][L]["time_per_kill"] for L in levels}) / w2
            if best is None or sc2 < best[0]:
                best = (sc2, sc1, i)
        if best[0] > 1 - a.min_gain:
            print(f"  round {rnd}: {len(cands)} candidates, {len(top)} ahead on seed 1, none confirmed on seed 2 (best {1 - best[0]:+.2%}: {describe(cands[best[2]])})", flush=True)
            break
        sc2, sc1, i = best
        ch = cands[i]
        log.append({"round": rnd, "change": describe(ch), "rule": list(ch), "gain_seed1": 1 - sc1, "gain_seed2": 1 - sc2})
        print(f"  round {rnd}: {describe(ch)}  ({1 - sc1:+.2%} seed 1, {1 - sc2:+.2%} seed 2 faster per kill; {len(cands)} candidates)", flush=True)
        rot = apply_change(rot, ch)
        base1 = res[i]
    # final check on a third seed
    fin = evaluate(pool, cls, spec, bid, levels, [rot0, rot], a.confirm, 3)
    wb, wa = weighted({L: fin[0][L]["time_per_kill"] for L in levels}), weighted({L: fin[1][L]["time_per_kill"] for L in levels})
    per_level = {L: {"before": fin[0][L]["time_per_kill"], "after": fin[1][L]["time_per_kill"], "deaths_before": fin[0][L]["deaths_per_100"],
                     "deaths_after": fin[1][L]["deaths_per_100"]} for L in levels}
    print(f"  final (seed 3, {a.confirm} fights): weighted time/kill {wb:.2f}s -> {wa:.2f}s ({1 - wa / wb:+.2%} faster); "
          + ", ".join(f"L{L} {v['before']:.1f}->{v['after']:.1f}s" for L, v in per_level.items()), flush=True)
    return dict(rot, **{"class": cls, "spec": spec, "build": bid, "levels": levels, "date": datetime.date.today().isoformat(),
                        "fights": a.fights, "confirm": a.confirm, "changes": log, "weighted_before": wb, "weighted_after": wa, "per_level": per_level})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--spec")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--rounds", type=int, default=12)
    ap.add_argument("--fights", type=int, default=600, help="fights per level and candidate on seed 1")
    ap.add_argument("--confirm", type=int, default=3000, help="fights per level on the confirmation seed 2 (and the final check on seed 3)")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--screen-gain", type=float, default=0.003)
    ap.add_argument("--min-gain", type=float, default=0.004, help="time per kill a rule must save on seed 2 to be kept")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument("--fresh", action="store_true", help="start from the hand-written rotation, not the saved rules")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    classes = list(FR.MODULES) if a.all else [a.cls]
    with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
        for cls in classes:
            tl, levels = targets(cls)
            for spec, bid in tl:
                if a.spec and spec != a.spec:
                    continue
                rec = search(pool, cls, spec, bid, levels, a)
                if a.write:
                    FR.ROTATIONS.mkdir(exist_ok=True)
                    p = FR.rotation_file(cls, spec)
                    if not rec["changes"] and not p.exists():
                        print(f"  no rule beat the hand-written rotation: nothing written", flush=True)
                        continue
                    p.write_text(json.dumps(rec, indent=1), encoding="utf-8")
                    print(f"  wrote {p.relative_to(ROOT)}", flush=True)


if __name__ == "__main__":
    main()
