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

`--stacks "Winter's Chill=5"` casts a forced spell only while the target's debuff has that many stacks (the audit session's case of
2026-11-21: Cone of Cold at five Winter's Chill stacks, the raid's quarter of Frost's damage, never tried in leveling). `--keep-veto`
leaves a rule's veto on the module's own lines: only the forced casts pass it (the Frost rules veto Cone of Cold; lifting it would also
open the module's own melee cone). With `--add`, the reference is the page build as it stands (2026-11-21: it had been the paid build
without the forced spell, so a talent bought for the spell made its own baseline weaker); the paid build alone is reported beside it.

Nothing in the lab's shared files changes: the module's decide is wrapped in this process only, so a running search is untouched.

    python _reference/data/fightlab/force_run.py <class> --guide <spec> --spell "Fireball" --spell "Scorch"
        [--levels 20,30,40,50,60] [--where top,filler] [--fights 2000] [--seeds 1,2] [--jobs 4] [--add T=N --pay A,B]
        [--stacks "Debuff=N"] [--keep-veto] [--write]
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path[:0] = [str(HERE), str(DATA)]
OUT = HERE / "never-tried.json"
BAR = 0.005


def _init():
    sys.path[:0] = [str(HERE), str(DATA)]


class _Veto(dict):
    """A rule's vetoes with an exception: the spell a forced cast is starting passes (--keep-veto)."""
    allow = set()

    def get(self, k, d=None):
        return None if k in self.allow else super().get(k, d)


from usable import HP_LIMIT, min_range, spell_row, usable, why_unusable  # noqa: E402,F401  (2026-11-22: shared with the engine)


def wrap(mod, names, where, filler, stacks=None, keep_veto=False, cls=None):
    """The module's decide with `names` forced in (see the module docstring)."""
    from engine import MELEE_RANGE
    orig = mod.decide
    mod._force_refused = {}   # {spell: {reason: decisions refused}} (why_unusable)
    if keep_veto:
        mod.veto = _Veto(mod.veto or {})
    else:
        for n in names:
            (mod.veto or {}).pop(n, None)

    def castable(fight):
        p, t, m = fight.p, fight.t, fight.m
        for n in names:
            s = mod.spells.get(n)
            if keep_veto:
                _Veto.allow.add(n)
            if s is None or not p.ready(s.name, t) or not fight.can_afford(s, mod.mana_cost(s)):
                _Veto.allow.discard(n)
                continue
            if stacks:
                deb, need = stacks
                d = (m.debuffs or {}).get(deb) if m is not None else None
                if not d or d.get("until", 0) <= t or (d.get("stacks") or 0) < need:
                    _Veto.allow.discard(n)
                    continue
            if s.dot and fight.dot_active(s.name):
                continue
            if (s.kind == "buff" or s.absorb or s.hot) and p.buff(s.name, t):
                continue
            reach = s.range if s.kind not in ("melee",) and s.range else MELEE_RANGE
            if (s.kind == "melee" and not m.in_melee) or m.dist > max(reach, MELEE_RANGE) + 0.5:
                _Veto.allow.discard(n)
                continue
            why = why_unusable(mod, cls, s, m, p)
            if why:   # the reason is counted: a spell the game never allows here gets that as its verdict (2026-11-22)
                c = mod._force_refused.setdefault(n, {})
                c[why] = c.get(why, 0) + 1
                _Veto.allow.discard(n)
                continue
            return s   # with --keep-veto its name stays allowed until the next decision: the cast starts past the veto
        return None

    def decide(fight):
        _Veto.allow.clear()   # the module's own lines see the rule's vetoes
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
    cls, rot, alloc, level, fights, seed, names, where, filler = a[:9]
    stacks, keep_veto = (a[9], a[10]) if len(a) > 10 else (None, False)
    mod = FR.make_module(cls, alloc, level, rot)
    missing = [n for n in names if n not in mod.spells]
    if where:
        wrap(mod, names, where, filler, stacks, keep_veto, cls=cls)
    out = Session(mod, level=level, fights=fights, seed=seed, mob_level_offset=0).run()
    k = max(1, out.get("kills") or 1)
    casts = {s: round(n / k, 2) for s, n in (out.get("casts") or {}).items() if n}
    return {"seconds": out["time_per_kill"], "casts": casts, "missing": missing, "refused": getattr(mod, "_force_refused", {})}


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
    ap.add_argument("--pay", default="", help="comma-separated talents the added ranks come from, in turn; lists separated by ';' are "
                    "tried in turn at each level, the first that leaves a legal build is used (2026-11-21: Frost's cone package needs "
                    "Ice Barrier's point at 40 and not at 50-60)")
    ap.add_argument("--together", action="store_true", help="force the listed spells together (default: each on its own)")
    ap.add_argument("--stacks", default=None, help='"Debuff=N": a forced spell only while the target carries N stacks of it')
    ap.add_argument("--keep-veto", action="store_true", help="the module's own lines keep a rule's veto of the forced spell")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    stacks = (a.stacks.split("=")[0], int(a.stacks.split("=")[1])) if a.stacks else None
    b, order, prov, rot = LG.pick(a.cls, a.guide)
    if not b:
        sys.exit(f"no leveling page pick for {a.cls} {a.guide}")
    ob = {"allocation": b["allocation"], "order": order}
    levels = [int(x) for x in a.levels.split(",")]
    seeds = [int(x) for x in a.seeds.split(",")]
    wheres = [w for w in a.where.split(",") if w]
    add = {x.split("=")[0]: int(x.split("=")[1]) for x in a.add}
    pay_lists = [[x.strip() for x in part.split(",") if x.strip()] for part in a.pay.split(";")] or [[]]
    pay_from = pay_lists[0]
    paid_with, paid_ranks = {}, {}
    import validate_builds as VB
    where = {n: tree for tree, d in VB.load_forever()[a.cls].items() for n in d["talents"]}
    allocs, skipped, page = {}, {}, {}
    for L in levels:
        al = FR.allocation_at(ob, L) if L >= 10 else {}
        page[L] = al
        if add:
            why, ok = None, None
            for pl in pay_lists:
                al2, why = pay(where, al, add, pl)
                if al2 is None:
                    continue
                e = legal(a.cls, al2, L)
                if e:
                    why = "; ".join(e)[:200]
                    continue
                ok = (al2, pl)
                break
            if ok is None:
                skipped[L] = why
                continue
            paid_ranks[L] = {n: r - ok[0].get(n, 0) for n, r in al.items() if r > ok[0].get(n, 0)}
            al, paid_with[L] = ok[0], ok[1]
        allocs[L] = al
    for L, why in skipped.items():
        print(f"   level {L} skipped: {why}", flush=True)
    for L, pr in sorted(paid_ranks.items()):
        print(f"   level {L} paid: {', '.join(f'{n} {r}' for n, r in pr.items())}", flush=True)
    jobs = [(a.cls, rot, allocs[L], L, a.fights, s, a.spell, None, None) for L in allocs for s in seeds]
    with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
        base = dict(zip([(L, s) for L in allocs for s in seeds], pool.map(_job, jobs, chunksize=1)))
        ref = base   # the reference: the page build (with --add the paid build is `base`, reported beside it)
        if add:
            ref = dict(zip([(L, s) for L in allocs for s in seeds], pool.map(
                _job, [(a.cls, rot, page[L], L, a.fights, s, a.spell, None, None) for L in allocs for s in seeds], chunksize=1)))
        fill = {L: max((c for c in base[(L, seeds[0])]["casts"].items() if c[0] not in a.spell), key=lambda kv: kv[1], default=(None, 0))[0]
                for L in allocs}
        groups = [a.spell] if a.together else [[n] for n in a.spell]
        fj = [(a.cls, rot, allocs[L], L, a.fights, s, g, w, fill[L], stacks, a.keep_veto) for g in groups for w in wheres for L in allocs
              for s in seeds]
        forced = dict(zip([(tuple(g), w, L, s) for g in groups for w in wheres for L in allocs for s in seeds], pool.map(_job, fj, chunksize=1)))
    today = datetime.date.today().isoformat()
    rec = json.loads(OUT.read_text(encoding="utf-8")) if (a.write and OUT.exists()) else {}
    paid_txt = "; ".join(f"{L}: {', '.join(pl)}" for L, pl in sorted(paid_with.items())) if len({tuple(x) for x in paid_with.values()}) > 1 \
        else ", ".join(next(iter(paid_with.values()), pay_from))
    with_add = (f"; with {', '.join(f'{k} {v}' for k, v in add.items())} paid from {paid_txt}, against the page build" if add else "") \
        + (f"; only at {stacks[1]}+ {stacks[0]} stacks" if stacks else "") + ("; the rules' veto kept on the module's own lines" if a.keep_veto else "")
    for g in groups:
        print(f"== {a.cls} {a.guide} ({b['id']}, rotation {rot}): forced {', '.join(g)}"
              + (f" with {', '.join(f'{k} {v}' for k, v in add.items())} paid from {paid_txt}" if add else ""), flush=True)
        rows, lead = [], []
        for w in wheres:
            for L in allocs:
                fr = [forced[(tuple(g), w, L, s)] for s in seeds]
                d = [f["seconds"] / ref[(L, s)]["seconds"] - 1 for f, s in zip(fr, seeds)]
                dp = [base[(L, s)]["seconds"] / ref[(L, s)]["seconds"] - 1 for s in seeds] if add else None
                pressed = {n: fr[0]["casts"].get(n, 0) for n in g}
                miss = fr[0]["missing"]
                print(f"   {w:6s} {L:2d}: {ref[(L, seeds[0])]['seconds']:.2f} -> {fr[0]['seconds']:.2f} s a kill "
                      f"({', '.join(f'{x:+.2%}' for x in d)}), pressed {pressed}" + (f", filler {fill[L]}" if w == "filler" else "")
                      + (f"; the paid build alone {', '.join(f'{x:+.2%}' for x in dp)}" if dp else "")
                      + (f"; NOT IN THE MODULE: {', '.join(miss)}" if miss else ""), flush=True)
                rows.append({"where": w, "level": L, "delta": [round(x, 4) for x in d], "pressed": pressed, "missing": miss,
                             "filler": fill[L] if w == "filler" else None, **({"paid_alone": [round(x, 4) for x in dp]} if dp else {})})
                if all(x <= -BAR for x in d):
                    lead.append(f"{w} at {L}: {max(d):+.2%}")
        tried = [r for r in rows if not r["missing"] and any(r["pressed"].values())]
        refused = {}   # the reasons the game refused the forced casts, over every run of the group (why_unusable)
        for k, f in forced.items():
            if k[0] == tuple(g):
                for n, rs in (f.get("refused") or {}).items():
                    for why, c in rs.items():
                        refused[why] = refused.get(why, 0) + c
        if lead:
            verdict = "LEAD: " + "; ".join(lead)
            print(f"   LEAD for the rotation tune (faster by the bar on every seed): {'; '.join(lead)}", flush=True)
        elif not tried and refused:   # never cast because the game does not allow it in this playstyle: a tried verdict, with its reason
            top = sorted(refused.items(), key=lambda kv: -kv[1])
            verdict = (f"forced into the priority on {today}: the game never allows it in this playstyle ("
                       + "; ".join(why for why, _ in top[:3]) + ")")
            print(f"   verdict: {verdict}", flush=True)
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
                key = n + (f" (with {', '.join(f'{k} {v}' for k, v in add.items())})" if add else "") + (f" at {stacks[1]}+ {stacks[0]}" if stacks else "")
                rec.setdefault(a.cls, {}).setdefault(rot, {})[key] = verdict
            rec.setdefault("_runs", []).append({"class": a.cls, "guide": a.guide, "build": b["id"], "rotation": rot, "spells": g,
                                                "add": add, "pay": {str(L): pl for L, pl in paid_with.items()} if add else [], "stacks": list(stacks) if stacks else None,
                                                "paid_ranks": {str(L): pr for L, pr in paid_ranks.items()},
                                                "keep_veto": a.keep_veto, "reference": "page build" if add else "the build as given",
                                                "date": today, "rows": rows, "skipped": skipped})
    if a.write:
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
