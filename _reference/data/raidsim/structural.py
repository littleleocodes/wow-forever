"""Exhaustive structural ranking of an open-search entry (2026-10-06, the plan's steps 3 and 4: "I want us to be able to know that we've
searched every possible combination that makes sense in theory and is feasible").

    python _reference/data/raidsim/structural.py <class> [--entry <entry>] [--top 300] [--race 20] [--fresh]

Needs the synergy certificate's full measurements (raidsim/synergy.py: `singles_all`, `pairs_all`, `removed_pairs_all` in the entry's
record). The model: a quadratic pseudo-boolean function of "talent in the build at its rank or not" fitted to those measurements (main
effects from the singles, interactions from the pairs; unmeasured pairs 0), relative to the winner. Dead talents (no effect above 0.1%
alone and no interaction above 0.2%) stop being variables: they are tier filler budget. Then every subset of each tree's live talents
is scored (with the tier points it needs, filled from the tree's dead talents, and its prerequisites), the best few kept per tree and
point count, every split of 51 points over the trees combined with the cross-tree pair terms, and the model's top `--top` legal
structures are simulated (1,500 fights, common random numbers), the best `--race` raced on 10,000 fights, the best of those polished
(every move) and raced on 30,000 against the winner. A structure 0.5% ahead is a structural lead: recorded in `entry["structural"]`
(the certificate's re-search path takes it from there: synergy.py --fresh). The model's fit on the simulated top is logged (an audit
of the pairwise assumption). Simulator numbers are the community's model of the beta, not measurements.
"""
import argparse
import datetime
import importlib.util
import itertools
import json
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data"), str(ROOT / "_reference/data/scorer")]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


SY = _load("synergy_st", HERE / "synergy.py")
FS, MLT, R = SY.FS, SY.MLT, SY.R
TODAY = datetime.date.today().isoformat()
DEAD_MAIN, DEAD_PAIR = 0.001, 0.002
KEEP_PER_TREE_POINTS = 8     # subsets kept per (tree, points)
SCREEN, RACE, CONFIRM = 1500, 10000, 30000
LEAD_BAR = 0.005


def log(m):
    print(m, flush=True)


class Model:
    """Quadratic model relative to the winner, on binary x_t (t at its rank in the build); gains as fractions of the winner's DPS."""

    def __init__(self, space, syn):
        self.space = space
        self.w = {n: r for items in syn["winner_allocation"].values() for n, r in items if r}
        self.rank = {}   # a talent's rank when in the build: the winner's rank if present, else full
        self.main = {}   # t -> (gain when added if missing | gain when removed if present)
        for n in space.relevant():
            self.rank[n] = self.w.get(n) or space.max[n]
        for t, g in syn["singles_all"].items():
            if t.startswith("-"):
                self.main[t[1:]] = g       # present: gain of removal (negative)
            else:
                self.main[t] = g           # missing: gain of adding
        self.pair = {}   # frozenset -> interaction term for (a added, b added) | (a added, b removed) | (a removed, b removed)
        for lab, v in syn["pairs_all"].items():
            a, b = lab.split(" + ")
            self.pair[(a, b)] = v["interaction"]
        for lab, v in syn["removed_pairs_all"].items():
            a, b = lab.split(" + ")
            self.pair[(a, b)] = v["interaction"]
        self.present = {n for n in self.main if self.w.get(n)}
        self.missing = {n for n in self.main if not self.w.get(n)}

    def live(self):
        hot = {n for n, g in self.main.items() if abs(g) >= DEAD_MAIN}
        for (a, b), v in self.pair.items():
            if abs(v) >= DEAD_PAIR:
                hot.add(a)
                hot.add(b)
        return hot

    def delta(self, n, inside):
        """Main-effect contribution of talent n being inside (True) or outside the build."""
        if n in self.present:
            return 0.0 if inside else self.main[n]
        return self.main[n] if inside else 0.0

    def pair_term(self, a, ina, b, inb):
        """Interaction contribution for the pair's states (relative to the winner's states)."""
        v = self.pair.get((a, b))
        if v is None:
            v = self.pair.get((b, a))
            if v is None:
                return 0.0
            a, ina, b, inb = b, inb, a, ina
        if a in self.missing and b in self.missing:
            return v if (ina and inb) else 0.0
        if a in self.missing and b in self.present:   # measured as (a with b) - (a without b) + (-b): the term applies to a in, b out
            return -v if (ina and not inb) else 0.0
        if a in self.present and b in self.present:
            return v if (not ina and not inb) else 0.0
        return 0.0


def tree_subsets(space, model, tree, live_t, dead_t):
    """[(points, score, chosen)] for every subset of the tree's live talents, with tier fillers from the dead talents and prerequisites."""
    out = []
    dead_room = sorted(((space.row[d], d, space.max[d] - (0 if d in model.missing else 0)) for d in dead_t), key=lambda x: x[0])
    for k in range(len(live_t) + 1):
        for chosen in itertools.combinations(live_t, k):
            sel = set(chosen)
            # prerequisites: a chosen talent's missing prerequisite must be chosen (live) or is added (dead)
            ok = True
            extra = {}
            for t in chosen:
                for q, r in space.req.get(t, []):
                    if q in live_t and q not in sel:
                        ok = False
                        break
                    if q not in live_t:
                        extra[q] = max(extra.get(q, 0), r)
                if not ok:
                    break
            if not ok:
                continue
            ranks = {t: model.rank[t] for t in chosen}
            ranks.update(extra)
            # tier fillers: every chosen talent needs 5*row points in lower rows; fill from dead talents by row
            need = 0
            pts_rows = {}
            for t, r in ranks.items():
                pts_rows[space.row[t]] = pts_rows.get(space.row[t], 0) + r
            filler = {}
            feasible = True
            for t in sorted(ranks, key=lambda t: space.row[t]):
                below = sum(v for rw, v in pts_rows.items() if rw < space.row[t]) + sum(v for d, v in filler.items() if space.row[d] < space.row[t])
                gap = 5 * space.row[t] - below
                for rw, d, room in dead_room:
                    if gap <= 0:
                        break
                    if rw >= space.row[t] or d in ranks:
                        continue
                    take = min(gap, room - filler.get(d, 0))
                    if take > 0:
                        filler[d] = filler.get(d, 0) + take
                        gap -= take
                if gap > 0:
                    feasible = False
                    break
            if not feasible:
                continue
            points = sum(ranks.values()) + sum(filler.values())
            if points > 51:
                continue
            score = sum(model.delta(t, t in sel) for t in live_t)
            for a, b in itertools.combinations(live_t, 2):
                score += model.pair_term(a, a in sel, b, b in sel)
            out.append((points, score, dict(ranks, **filler)))
    return out


def rank_structures(space, model, top):
    live = model.live()
    by_tree = {t: [n for n in space.by_tree[t] if n in live] for t in space.tree_names}
    dead = {t: [n for n in space.by_tree[t] if n not in live] for t in space.tree_names}
    log("   live talents: " + ", ".join(f"{t} {len(by_tree[t])}" for t in space.tree_names) + f" (dead {sum(len(v) for v in dead.values())})")
    best = {}   # (tree, points) -> top K (score, build)
    for t in space.tree_names:
        if len(by_tree[t]) > 16:
            log(f"   {t}: {len(by_tree[t])} live talents, keeping the 16 with the largest effects")
            by_tree[t] = sorted(by_tree[t], key=lambda n: -abs(model.main.get(n, 0)))[:16]
        subs = tree_subsets(space, model, t, by_tree[t], dead[t])
        for points, score, build in subs:
            lst = best.setdefault((t, points), [])
            lst.append((score, build))
            lst.sort(key=lambda x: -x[0])
            del lst[KEEP_PER_TREE_POINTS:]
        log(f"   {t}: {len(subs):,} subsets scored")
    # combine: every split of 51 (a tree may hold more points than its subset needs only through dead filler room, ignored: exact splits)
    pts_lists = {t: sorted({p for (tt, p) in best if tt == t}) for t in space.tree_names}
    T = space.tree_names
    cands = []
    for p1 in pts_lists[T[0]]:
        for p2 in pts_lists[T[1]]:
            p3 = 51 - p1 - p2
            if p3 < 0 or (T[2], p3) not in best:
                continue
            for s1, b1 in best[(T[0], p1)]:
                for s2, b2 in best[(T[1], p2)]:
                    for s3, b3 in best[(T[2], p3)]:
                        build = dict(b1, **b2, **b3)
                        inside = {n for n in live if build.get(n)}
                        cross = 0.0
                        for a in by_tree[T[0]] + by_tree[T[1]] + by_tree[T[2]]:
                            for b in live:
                                if b <= a or space.tree_of[a] == space.tree_of[b]:
                                    continue
                                cross += model.pair_term(a, a in inside, b, b in inside)
                        cands.append((s1 + s2 + s3 + cross, build))
    cands.sort(key=lambda x: -x[0])
    out, seen = [], set()
    for sc, b in cands:
        k = tuple(sorted(b.items()))
        if k in seen or not space.valid(b):
            continue
        seen.add(k)
        out.append((sc, b))
        if len(out) >= top:
            break
    log(f"   {len(cands):,} structures combined, {len(out)} legal kept for simulation (model's best {out[0][0]:+.2%})" if out else "   no legal structure")
    return out


def structural(cls, entry, e, repo, save, a):
    t0 = time.time()
    syn = e.get("synergy") or {}
    if "singles_all" not in syn:
        log(f"== {cls} {entry}: no full measurements in the record; run synergy.py --fresh first")
        return
    space = MLT.Space(cls, "any", any_split=True)
    space.protect = set(e.get("first", {}).get("protected") or ())
    model = Model(space, syn)
    w = dict(model.w)
    log(f"== {cls} {entry}: structural ranking around {space.split(w)} ({len(model.main)} measured talents, {len(model.pair)} pairs)")
    ranked = rank_structures(space, model, a.top)
    if not ranked:
        return
    sim = MLT.Sim(cls, entry, "raid", None, repo, f"structural-{cls}-{entry}")
    res = sim.run([w] + [b for _, b in ranked], SCREEN, 64)
    base = res[0][0]
    sims = [(r[0] / base - 1, sc, b) for (sc, b), r in zip(ranked, res[1:])]
    # the model's fit: correlation between predicted and simulated gains on the screened top
    n = len(sims)
    mx = sum(s for _, s, _ in sims) / n
    my = sum(g for g, _, _ in sims) / n
    cov = sum((s - mx) * (g - my) for g, s, _ in sims)
    vx = sum((s - mx) ** 2 for _, s, _ in sims) ** 0.5
    vy = sum((g - my) ** 2 for g, _, _ in sims) ** 0.5
    corr = cov / (vx * vy) if vx and vy else 0.0
    sims.sort(key=lambda x: -x[0])
    log(f"   screen: model-simulation correlation {corr:+.2f} on {n} structures; best simulated {sims[0][0]:+.2%} {space.split(sims[0][2])}, "
        f"model said {sims[0][1]:+.2%}")
    top = sims[:a.race]
    r2 = sim.run([w] + [b for _, _, b in top], RACE, 65)
    raced = sorted(((r[0] / r2[0][0] - 1, b) for (_, _, b), r in zip(top, r2[1:])), key=lambda x: -x[0])
    leads = []
    if raced:
        g, b = raced[0]
        x, sx = MLT.polish(space, sim, b, 800, 66, rounds=8, min_gain=0.002, small=False)
        r3 = sim.run([w, x], CONFIRM, 67)
        gain = r3[1][0] / r3[0][0] - 1
        log(f"   race: best {space.split(b)} {g:+.2%} on {RACE}; polished {space.split(x)} {gain:+.2%} on {CONFIRM} against the winner")
        if gain >= LEAD_BAR:
            leads.append({"split": space.split(x), "gain": round(gain, 4), "dps": round(r3[1][0], 1),
                          "allocation": {t: [[n, x[n]] for n in space.by_tree[t] if x.get(n)] for t in space.tree_names}})
    e["structural"] = {"date": TODAY, "winner": space.split(w), "live": len(model.live()), "screened": n, "correlation": round(corr, 3),
                       "screen_best": [{"split": space.split(b), "simulated": round(g, 4), "model": round(s, 4)} for g, s, b in sims[:8]],
                       "raced": [{"split": space.split(b), "gain": round(g, 4)} for g, b in raced[:5]], "leads": leads,
                       "minutes": round((time.time() - t0) / 60, 1)}
    save()
    verdict = f"found a lead {leads[0]['split']} ({leads[0]['gain']:+.1%})" if leads else "confirms the winner"
    log(f"  {cls} {entry}: structural ranking {verdict} ({e['structural']['minutes']} min)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--entry", action="append")
    ap.add_argument("--top", type=int, default=300)
    ap.add_argument("--race", type=int, default=20)
    ap.add_argument("--fresh", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    rp = FS.OUT / f"{a.cls}.json"
    st = json.load(open(rp, encoding="utf-8"))

    def save():
        rp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    for entry, e in st["entries"].items():
        if a.entry and entry not in a.entry:
            continue
        if not e.get("done"):
            continue
        if e.get("structural") and not a.fresh:
            log(f"== {a.cls} {entry}: structural ranking done ({e['structural']['date']})")
            continue
        structural(a.cls, entry, e, repo, save, a)
    log("== done")


if __name__ == "__main__":
    main()
