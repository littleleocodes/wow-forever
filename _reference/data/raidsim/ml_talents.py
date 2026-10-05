"""Machine-learning talent search in the community simulator (2026-10-01, user request: "approach these classes and specs in a more
systematic machine learning model method ... find the absolute most optimal").

    python _reference/data/raidsim/ml_talents.py <class> --spec "<spec>" --entry <specs.json entry> [--entry <another> ...]
           [--setting dummy|raid] [--gear <gear.json>] [--runs 2] [--budget 2500] [--seed 1] [--write <record.json>]

The search space is every legal 51-point build of the class (validate_builds rules: rank caps, tier gating, prerequisites) that belongs
to the spec as spec_modes.py files it (30+ points in the tree; a hybrid "A/B": no tree at 30 and A and B on top; a spec whose builds
carry a spec field, such as Frostfire or Smite, keeps no tree rule because its entry's rotation defines it) and keeps every talent the
entry's rotation reads (run.py apl_talents: without it the rotation misreads an unknown aura). The objective is the simulator's DPS of
the build in the entry: the setting's own rotation, the given gear (bench `gear_json`), 180 s, common random numbers within a stage.

1. Design: the starts (our builds of the spec, the simulator's presets and talentsforever.com's popular builds that are this spec),
   their mutations and crossovers, and random legal builds of the spec (a split drawn for the spec, each tree filled point by point in
   tier order); simulated at --screen iterations (1000) on seed 1.
2. Surrogate: a random forest (scikit-learn) on the talent ranks and tree totals predicts a build's DPS and its uncertainty (the spread
   of the trees' predictions): the random-forest Bayesian optimisation of SMAC.
3. Rounds: a genetic step proposes thousands of legal builds from the best simulated ones (mutation: random legal moves of 1, 2, 3 or 5
   points and prerequisite chains, the move that reaches Mortal Strike through Sweeping Strikes; crossover: each tree from one of two
   parents, repaired to 51 points); the surrogate ranks them by upper confidence bound (mean + kappa x spread) and the most promising,
   the best predicted and a few random ones are simulated; the forest is refitted. Stops when the best simulated build has not gained
   0.1% for --patience rounds or the budget is spent. With several entries (rotation families), a short screen of each picks the
   entries within 2% of the best for the full search.
4. --runs independent searches (separate random streams).
5. Racing: the best distinct builds of every run, on fresh seeds (run.sim_seed) with growing iterations (10k, 30k, 100k): successive
   halving to one winner, with standard errors and the gap to the runner-up.
6. Certificate: every one-move and prerequisite-chain neighbour of the winner on a fresh seed (3000 iterations); a neighbour more than
   0.1% ahead is raced (30k) and, if it holds, becomes the winner and the step repeats. A winner no neighbour beats is a local optimum
   of the whole move set; agreement of the independent runs is the evidence that it is the global one.
The record: the winner (allocation, split, DPS and standard error at 100k iterations), the runner-up and the gap, each run's own best,
the convergence trace, the certificate and the surrogate's most important talents. Simulations of the community's model of the beta.
"""
import argparse
import datetime
import importlib.util
import json
import math
import pathlib
import random
import sys
import time

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import validate_builds as VB  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


A = _load("aplopt", HERE / "apl_opt.py")
R = A.R
TOTAL = VB.TOTAL_POINTS
TODAY = datetime.date.today().isoformat()


def key(flat):
    return tuple(sorted((n, r) for n, r in flat.items() if r))


# ------------------------------------------------------------------------------------------------ the space of legal builds
class Space:
    """Legal 51-point builds of one class that belong to one spec and keep the protected talents."""

    def __init__(self, cls, spec, protect=(), any_split=False, start_splits=()):
        self.cls, self.spec = cls, spec
        trees = VB.load_forever()[cls]
        self.tree_names = list(trees)
        self.names = [n for t in self.tree_names for n in trees[t]["talents"]]
        self.tree_of = {n: t for t in self.tree_names for n in trees[t]["talents"]}
        self.max = {n: trees[self.tree_of[n]]["talents"][n]["max"] for n in self.names}
        self.row = {n: trees[self.tree_of[n]]["talents"][n]["row"] for n in self.names}
        norm = {VB.norm(n): n for n in self.names}
        self.req = {n: [(norm.get(VB.norm(q), q), int(r)) for q, r in (trees[self.tree_of[n]]["talents"][n].get("requires") or [])] for n in self.names}
        self.by_tree = {t: [n for n in self.names if self.tree_of[n] == t] for t in self.tree_names}
        self.cap = {t: sum(self.max[n] for n in self.by_tree[t]) for t in self.tree_names}
        self.protect = set(protect)
        self.any = any_split
        self.start_splits = [s for s in start_splits if s]
        self.pair = [t for t in self.tree_names if t in spec.replace("Hybrid ", "").split("/")] if spec.startswith("Hybrid") else []
        self.trees = trees

    # -- rules
    def points(self, flat):
        return {t: sum(flat.get(n, 0) for n in self.by_tree[t]) for t in self.tree_names}

    def classify(self, flat):
        pts = self.points(flat)
        top = sorted(self.tree_names, key=lambda t: -pts[t])
        if pts[top[0]] >= SM.SPEC_POINTS:
            return top[0]
        return "Hybrid " + "/".join(t for t in self.tree_names if t in top[:2])

    def ok_partial(self, flat):
        """Rank caps, tier gating and prerequisites (any total)."""
        rows = {}
        for n, r in flat.items():
            if n not in self.max or r < 0 or r > self.max[n]:   # a talent the current trees no longer have (a start from older trees)
                return False
            if r:
                k = (self.tree_of[n], self.row[n])
                rows[k] = rows.get(k, 0) + r
        for n, r in flat.items():
            if not r:
                continue
            rw = self.row[n]
            if rw:
                t = self.tree_of[n]
                if sum(v for (tt, rr), v in rows.items() if tt == t and rr < rw) < 5 * rw:
                    return False
            for q, qr in self.req[n]:
                if flat.get(q, 0) < qr:
                    return False
        return True

    def valid(self, flat):
        if sum(flat.values()) != TOTAL or not self.ok_partial(flat):
            return False
        if any(not flat.get(n) for n in self.protect):
            return False
        return self.any or self.classify(flat) == self.spec

    def vec(self, flat):
        pts = self.points(flat)
        return [flat.get(n, 0) for n in self.names] + [pts[t] for t in self.tree_names]

    def features(self):
        return list(self.names) + [f"{t} points" for t in self.tree_names]

    def split(self, flat):
        p = self.points(flat)
        return "/".join(str(p[t]) for t in self.tree_names)

    # -- random builds
    def unlocked(self, flat, n):
        rw = self.row[n]
        if not rw:
            return True
        t = self.tree_of[n]
        return sum(flat.get(m, 0) for m in self.by_tree[t] if self.row[m] < rw) >= 5 * rw

    def fill(self, rng, flat, t, p):
        placed, last = 0, None
        while placed < p:
            avail = [n for n in self.by_tree[t] if flat.get(n, 0) < self.max[n] and self.unlocked(flat, n)
                     and all(flat.get(q, 0) >= qr for q, qr in self.req[n])]
            if not avail:
                break
            if last in avail and rng.random() < 0.65:
                n = last
            else:
                n = rng.choices(avail, [6.0 if x in self.protect else 1.0 for x in avail])[0]
            flat[n] = flat.get(n, 0) + 1
            placed += 1
            last = n
        return placed

    def sample_split(self, rng):
        T = self.tree_names
        for _ in range(50):
            if self.any:
                if self.start_splits and rng.random() < 0.5:
                    base = dict(zip(T, (int(x) for x in rng.choice(self.start_splits).split("/"))))
                    sp = {t: max(0, base[t] + rng.randint(-6, 6)) for t in T}
                else:   # anywhere on the simplex (2026-10-05: drawing near the starts only never reached the 16/11/24 hunter)
                    cuts = sorted(rng.randint(0, TOTAL) for _ in range(len(T) - 1))
                    sp = dict(zip(T, [b - a for a, b in zip([0] + cuts, cuts + [TOTAL])]))
                d = TOTAL - sum(sp.values())
                big = max(T, key=lambda t: sp[t])
                sp[big] += d
            elif self.pair:
                a, b = self.pair
                c = [t for t in T if t not in self.pair][0]
                pc = rng.randint(0, 16)
                pa = rng.randint(max(TOTAL - pc - 29, pc + 1), 29)
                sp = {a: pa, b: TOTAL - pc - pa, c: pc}
                if not (pc < sp[b] <= 29):
                    continue
            else:
                main = self.spec
                pm = min(TOTAL, SM.SPEC_POINTS + int(rng.expovariate(1 / 7.0)))
                rest = TOTAL - pm
                o = [t for t in T if t != main]
                x = rng.randint(0, rest)
                sp = {main: pm, o[0]: x, o[1]: rest - x}
            sp = self.room_for_protected(sp)
            if sp and all(0 <= sp[t] <= self.cap[t] for t in T):
                return sp
        return None

    def room_for_protected(self, sp):
        """Shift points so every tree holds enough for its protected talents' tiers (a talent on tier r needs 5r points below it and one
        of its own); None when the spec's rule leaves no room (2026-10-01: the probe of Hemorrhage, 30 Assassination + 21 Subtlety, was
        never drawn by the plain split)."""
        need = {t: 0 for t in self.tree_names}
        for n in self.protect:
            need[self.tree_of[n]] = max(need[self.tree_of[n]], 5 * self.row[n] + 1)
        floor = dict(need)
        if not self.any and not self.pair:
            floor[self.spec] = max(floor[self.spec], SM.SPEC_POINTS)
        sp = dict(sp)
        for _ in range(TOTAL):
            short = [t for t in self.tree_names if sp[t] < need[t]]
            if not short:
                return sp
            donors = [d for d in self.tree_names if d != short[0] and sp[d] > floor[d]]
            if not donors:
                return None
            d = max(donors, key=lambda x: sp[x] - floor[x])
            sp[d] -= 1
            sp[short[0]] += 1
        return None

    def random_build(self, rng):
        for _ in range(60):
            sp = self.sample_split(rng)
            if not sp:
                continue
            flat = {}
            for t in sorted(self.tree_names, key=lambda t: -sum(1 for n in self.protect if self.tree_of[n] == t)):
                if self.fill(rng, flat, t, sp[t]) < sp[t]:
                    break
            else:
                if self.valid(flat):
                    return flat
        return None

    def keystones(self):
        """One-rank talents above the first two tiers: the trees' signature picks (Summon Hawk, Lone Wolf, Mortal Strike ...)."""
        return [n for n in self.names if self.max[n] == 1 and self.row[n] >= 2]

    def keystone_starts(self, rng, per_pair=3):
        """Random legal builds holding each pair of keystones from different trees: an open search's seeds for combinations no build
        of ours holds (2026-10-05: the 16/11/24 Summon Hawk + Lone Wolf hunter, 7.5% ahead, was never reached from our builds)."""
        out, keep = [], self.protect
        ks = self.keystones()
        for i, a in enumerate(ks):
            for b in ks[i + 1:]:
                if self.tree_of[a] == self.tree_of[b]:
                    continue
                self.protect = set(keep) | {a, b}
                for _ in range(per_pair):
                    x = self.random_build(rng)
                    if x:
                        out.append(x)
        self.protect = keep
        return out

    # -- moves
    def mutate(self, rng, flat, n_moves):
        cur = dict(flat)
        for _ in range(n_moves):
            for _try in range(40):
                if rng.random() < 0.15:
                    new = self.random_chain(rng, cur)
                else:
                    a = rng.choice([n for n in cur if cur[n] > 0])
                    b = rng.choice(self.names)
                    k = rng.choice((1, 1, 1, 2, 2, 3, 5))
                    if b == a or cur[a] < k or self.max[b] - cur.get(b, 0) < k:
                        continue
                    new = dict(cur)
                    new[a] -= k
                    if not new[a]:
                        del new[a]
                    new[b] = new.get(b, 0) + k
                if new and self.valid(new):
                    cur = new
                    break
        return cur

    def random_chain(self, rng, flat):
        cands = [b for b in self.names if not flat.get(b) and self.req[b] and any(flat.get(q, 0) < r for q, r in self.req[b])]
        if not cands:
            return None
        b = rng.choice(cands)
        add = {q: r - flat.get(q, 0) for q, r in self.req[b] if flat.get(q, 0) < r}
        add[b] = rng.choice(sorted({1, self.max[b]}))
        need = sum(add.values())
        srcs = [x for x, r in flat.items() if r > 0 and x not in add]
        rng.shuffle(srcs)
        new, left = dict(flat), need
        for x in srcs[:3]:
            t = min(new[x], left) - (1 if x in self.protect and new[x] <= left else 0)
            if t <= 0:
                continue
            new[x] -= t
            left -= t
            if not new[x]:
                del new[x]
            if not left:
                break
        if left:
            return None
        for x, n in add.items():
            new[x] = new.get(x, 0) + n
        return new

    def crossover(self, rng, p1, p2):
        child = {}
        for t in self.tree_names:
            src = p1 if rng.random() < 0.5 else p2
            for n in self.by_tree[t]:
                if src.get(n):
                    child[n] = src[n]
        return self.repair(rng, child)

    def repair(self, rng, flat):
        cur = dict(flat)
        for _ in range(120):
            tot = sum(cur.values())
            if tot == TOTAL:
                break
            if tot > TOTAL:
                cands = [n for n in cur if cur[n] > 0 and not (n in self.protect and cur[n] == 1)]
                rng.shuffle(cands)
                for n in cands:
                    new = dict(cur)
                    new[n] -= 1
                    if not new[n]:
                        del new[n]
                    if self.ok_partial(new):
                        cur = new
                        break
                else:
                    return None
            else:
                avail = [n for n in self.names if cur.get(n, 0) < self.max[n]]
                rng.shuffle(avail)
                for n in avail:
                    new = dict(cur)
                    new[n] = new.get(n, 0) + 1
                    if self.ok_partial(new):
                        cur = new
                        break
                else:
                    return None
        return cur if self.valid(cur) else None

    def neighbours(self, flat):
        """Every legal one-move (1, 2, 3 or 5 points from one talent to another) and prerequisite-chain neighbour."""
        out, seen = [], {key(flat)}
        for a, ra in list(flat.items()):
            if ra <= 0:
                continue
            for b in self.names:
                if b == a:
                    continue
                for k in (1, 2, 3, 5):
                    if k > ra or k > self.max[b] - flat.get(b, 0):
                        continue
                    new = dict(flat)
                    new[a] -= k
                    if not new[a]:
                        del new[a]
                    new[b] = new.get(b, 0) + k
                    kk = key(new)
                    if kk not in seen and self.valid(new):
                        seen.add(kk)
                        out.append((f"{k} {a} -> {b}", new))
        for b in self.names:
            if flat.get(b) or not self.req[b]:
                continue
            missing = {q: r - flat.get(q, 0) for q, r in self.req[b] if flat.get(q, 0) < r}
            if not missing:
                continue
            for kb in sorted({1, self.max[b]}):
                add = dict(missing, **{b: kb})
                need = sum(add.values())
                srcs = [x for x, rx in flat.items() if rx > 0 and x not in add]
                plans = [{x: need} for x in srcs if flat[x] >= need]
                for i, x1 in enumerate(srcs):
                    for x2 in srcs[i + 1:]:
                        t1 = min(flat[x1], need - 1)
                        if t1 >= 1 and flat[x2] >= need - t1:
                            plans.append({x1: t1, x2: need - t1})
                for take in plans:
                    new = dict(flat)
                    for x, n in take.items():
                        new[x] -= n
                        if not new[x]:
                            del new[x]
                    for x, n in add.items():
                        new[x] = new.get(x, 0) + n
                    kk = key(new)
                    if kk not in seen and self.valid(new):
                        seen.add(kk)
                        out.append((" + ".join(f"{n} {x}" for x, n in take.items()) + " -> " + " + ".join(f"{n} {x}" for x, n in add.items()), new))
        return out


# ------------------------------------------------------------------------------------------------ the simulator
class Sim:
    """DPS of builds in one entry and setting, with one gear set (bench gear_json); counts the builds simulated."""

    def __init__(self, cls, entry, setting, gear_items, repo, tag):
        self.cls, self.entry_name, self.setting, self.gear, self.repo, self.tag = cls, entry, setting, gear_items, repo, tag
        self.entry = R.SPECS[cls][entry]
        self.sim_trees = R.load_trees(repo, cls)
        self.n = 0
        self.fights = 0

    def run(self, allocs, iterations, seed):
        out = []
        for i0 in range(0, len(allocs), 400):
            chunk = allocs[i0:i0 + 400]
            bl = [{"label": str(i), "talents": R.talents_string(self.sim_trees, al), **({"gear_json": {"items": self.gear}} if self.gear else {})}
                  for i, al in enumerate(chunk)]
            rows = A.bench(self.entry, self.repo, bl, iterations, seed, self.setting, self.tag)
            for i in range(len(chunk)):
                r = rows.get(str(i)) or {}
                out.append((float(r.get("dps") or 0.0), float(r.get("dps_stdev") or 0.0)))
            self.n += len(chunk)
            self.fights += len(chunk) * iterations
        return out


# ------------------------------------------------------------------------------------------------ the search
def _r(x, nd=2):
    """A score as stored: DPS to 2 decimals; a small-scale score (healer capacity, tank value: about 1) to 4."""
    return round(x, nd if abs(x) >= 10 else 4)


def _f(x):
    """A score as printed: DPS to 0.1; a small-scale score to 0.0001."""
    return f"{x:.1f}" if abs(x) >= 10 else f"{x:.4f}"


def fit_forest(X, y, rng):
    from sklearn.ensemble import RandomForestRegressor
    rf = RandomForestRegressor(n_estimators=160, min_samples_leaf=2, max_features=0.4, n_jobs=-1, random_state=rng.randrange(1 << 30))
    rf.fit(X, y)
    return rf


def predict(rf, X):
    P = np.stack([t.predict(X) for t in rf.estimators_])
    return P.mean(0), P.std(0)


def search(space, sim, starts, rng, a, log, label=""):
    """One run: design, then surrogate-guided genetic rounds. Returns {key: (flat, dps)} of every build simulated (seed 1)."""
    data = {}

    def evaluate(cands):
        new, seen = [], set()
        for c in cands:
            if c is None:
                continue
            k = key(c)
            if k in data or k in seen:
                continue
            seen.add(k)
            new.append(c)
        if not new:
            return 0
        res = sim.run(new, a.screen, 1)
        for c, (d, _) in zip(new, res):
            data[key(c)] = (c, d)
        return len(new)

    starts = [s for s in starts if s and space.valid(s)]
    init = list(starts)
    for s in starts:
        init += [space.mutate(rng, s, rng.choice((1, 1, 2, 3))) for _ in range(max(10, 120 // max(1, len(starts))))]
    if len(starts) > 1:
        init += [space.crossover(rng, rng.choice(starts), rng.choice(starts)) for _ in range(60)]
    init += [space.random_build(rng) for _ in range(a.random_init)]
    evaluate(init)
    best = max(v[1] for v in data.values()) if data else 0.0
    trace = [{"round": 0, "simulated": len(data), "best": _r(best)}]
    log(f"    {label}design: {len(data)} builds, best {_f(best)}")
    quiet = 0
    for rnd in range(1, a.max_rounds + 1):
        if len(data) >= a.budget or quiet >= a.patience:
            break
        flats = [v[0] for v in data.values()]
        X = np.array([space.vec(f) for f in flats], dtype=float)
        y = np.array([v[1] for v in data.values()])
        rf = fit_forest(X, y, rng)
        order = np.argsort(-y)
        parents = [flats[i] for i in order[: a.parents]]
        pool = [space.mutate(rng, rng.choice(parents), rng.choice((1, 1, 2, 2, 3, 4))) for _ in range(a.pool * 6 // 10)]
        pool += [space.crossover(rng, rng.choice(parents), rng.choice(parents)) for _ in range(a.pool * 3 // 10)]
        pool += [space.random_build(rng) for _ in range(a.pool // 10)]
        uniq = {}
        for c in pool:
            if c is not None and key(c) not in data:
                uniq.setdefault(key(c), c)
        pool = list(uniq.values())
        if not pool:
            break
        mu, sd = predict(rf, np.array([space.vec(c) for c in pool], dtype=float))
        ucb = mu + a.kappa * sd
        pick = []
        for idx in list(np.argsort(-ucb)[: a.batch * 5 // 10]) + list(np.argsort(-mu)[: a.batch * 3 // 10]):
            if pool[idx] not in pick:
                pick.append(pool[idx])
        rest = [c for c in pool if c not in pick]
        pick += rng.sample(rest, min(len(rest), a.batch - len(pick)))
        evaluate(pick[: a.batch])
        nb = max(v[1] for v in data.values())
        quiet = 0 if nb > best * (1 + a.min_gain) else quiet + 1
        best = max(best, nb)
        trace.append({"round": rnd, "simulated": len(data), "best": _r(best), "predicted_top": _r(float(mu.max()))})
        log(f"    {label}round {rnd}: {len(data)} simulated, best {_f(best)}" + (" (no gain)" if quiet else ""))
    return data, trace


def race(sim, cands, log, stages=((10000, 2, 5), (30000, 3, 2), (100000, 4, 2)), first=None):
    """Successive halving on fresh seeds; returns (ranked [(flat, dps, se)] of the last stage, history). `first`, when given, receives
    {build key: DPS} of the first stage (every candidate on the same seed)."""
    cur, hist = list(cands), []
    for its, seed, keep in stages:
        res = sim.run(cur, its, seed)
        if first is not None and not hist:
            first.update({key(f): r[0] for f, r in zip(cur, res)})
        ranked = sorted(zip(cur, res), key=lambda x: -x[1][0])
        hist.append({"iterations": its, "seed": seed, "dps": [_r(r[1][0]) for r in ranked]})
        cur = [r[0] for r in ranked[:keep]]
        last = [(f, d, sd / math.sqrt(its)) for f, (d, sd) in ranked]
    log(f"    race: " + " -> ".join(f"{h['iterations'] // 1000}k: " + ", ".join(_f(x) for x in h["dps"][:5]) for h in hist))
    return last, hist


def certificate(space, sim, winner, log, its=3000, seed=5, conf_its=30000):
    """Every neighbour of the winner on a fresh seed; a neighbour 0.1% ahead is raced and, if it holds, becomes the winner."""
    steps = []
    for step in range(6):
        nb = space.neighbours(winner)
        res = sim.run([winner] + [x[1] for x in nb], its, seed + 2 * step)
        w = res[0][0]
        gaps = sorted(((res[i + 1][0] / w - 1, i) for i in range(len(nb))), reverse=True)
        top = [(g, i) for g, i in gaps[:4] if g > 0.001]
        rec = {"neighbours": len(nb), "best_gap": round(gaps[0][0], 4) if gaps else None, "best_move": nb[gaps[0][1]][0] if gaps else None}
        if not top:
            steps.append(rec)
            log(f"    certificate: {len(nb)} neighbours, none 0.1% ahead (best {gaps[0][0]:+.2%}: {nb[gaps[0][1]][0]})" if gaps else "    certificate: no neighbours")
            return winner, steps
        conf = sim.run([winner] + [nb[i][1] for _, i in top], conf_its, seed + 2 * step + 1)
        g2, j = max(((conf[k + 1][0] / conf[0][0] - 1, k) for k in range(len(top))))
        rec.update({"raced": [nb[i][0] for _, i in top], "confirmed_gap": round(g2, 4)})
        steps.append(rec)
        if g2 <= 0.001:
            log(f"    certificate: {len(nb)} neighbours; the best ahead on {its} iterations did not hold ({g2:+.2%})")
            return winner, steps
        winner = nb[top[j][1]][1]
        log(f"    certificate: moved {nb[top[j][1]][0]} ({g2:+.2%} on {conf_its})")
    return winner, steps


def two_moves(space, flat, expand=None):
    """(one-move neighbours, two-move neighbours) of a build: every legal build reached by one move (1, 2, 3 or 5 points from one talent to
    another, or a prerequisite chain) and by two such moves in a row, deduplicated. `expand` limits the second move to the given
    one-move neighbours (keys), for slow labs."""
    first = space.neighbours(flat)
    seen = {key(flat)} | {key(n) for _, n in first}
    second = []
    for m1, n1 in first:
        if expand is not None and key(n1) not in expand:
            continue
        for m2, n2 in space.neighbours(n1):
            k = key(n2)
            if k not in seen:
                seen.add(k)
                second.append((f"{m1}; then {m2}", n2))
    return first, second


def two_move_certificate(space, sim, winner, log, screen=1000, seed=21, conf=(20000, 100000), top=60, expand_top=None, rounds=3):
    """'No better build within two talent moves', checked exhaustively: every one- and two-move neighbour of the winner simulated on one
    seed with common random numbers (`screen` fights each), the best `top` raced against the winner on a fresh seed (conf[0] fights), the
    best 5 of those once more (conf[1]); a neighbour still 0.1% ahead replaces the winner and the check repeats (at most `rounds` times).
    `expand_top`: expand only the best one-move neighbours a second time (for labs too slow for the full two-move set)."""
    steps = []
    for rep in range(rounds):
        expand = None
        if expand_top:
            first = space.neighbours(winner)
            r0 = sim.run([winner] + [c for _, c in first], screen, seed + 30 + rep)
            ranked = sorted(range(len(first)), key=lambda i: -r0[i + 1][0])[:expand_top]
            expand = {key(first[i][1]) for i in ranked}
        first, second = two_moves(space, winner, expand)
        cands = first + second
        t0 = time.time()
        res = sim.run([winner] + [c for _, c in cands], screen, seed + rep)
        w = res[0][0] or 1.0
        gaps = sorted(((res[i + 1][0] / w - 1, i) for i in range(len(cands))), reverse=True)
        best = gaps[:top]
        r1 = sim.run([winner] + [cands[i][1] for _, i in best], conf[0], seed + 10 + rep)
        g1 = sorted(((r1[k + 1][0] / (r1[0][0] or 1.0) - 1, best[k][1]) for k in range(len(best))), reverse=True)[:5]
        r2 = sim.run([winner] + [cands[i][1] for _, i in g1], conf[1], seed + 20 + rep)
        g2 = sorted(((r2[k + 1][0] / (r2[0][0] or 1.0) - 1, g1[k][1]) for k in range(len(g1))), reverse=True)
        rec = {"one_move": len(first), "two_move": len(second), "expanded": len(expand) if expand is not None else None, "screen": screen,
               "screen_best": [(cands[i][0], round(g, 4)) for g, i in gaps[:5]], "raced": len(best),
               "confirmed": [(cands[i][0], round(g, 4)) for g, i in g2], "minutes": round((time.time() - t0) / 60, 1)}
        steps.append(rec)
        lead = g2[0] if g2 else None
        log(f"    two-move check: {len(first)} one-move + {len(second)} two-move builds, the best {len(best)} raced; "
            + (f"best {lead[0]:+.2%} ({cands[lead[1]][0]})" if lead else "none raced") + f"; {rec['minutes']} min")
        if lead and lead[0] > 0.001:
            winner = cands[lead[1]][1]
            log(f"    two-move check: moved to {space.split(winner)} ({lead[0]:+.2%} on {conf[1]})")
            continue
        return winner, steps
    return winner, steps


def importance(space, data, rng, top=12):
    flats = [v[0] for v in data.values()]
    X = np.array([space.vec(f) for f in flats], dtype=float)
    y = np.array([v[1] for v in data.values()])
    rf = fit_forest(X, y, rng)
    names = space.features()
    order = np.argsort(-rf.feature_importances_)[:top]
    return [{"feature": names[i], "importance": round(float(rf.feature_importances_[i]), 4)} for i in order]


def optimize(space, sims, starts, a, log):
    """The whole search for one spec in one setting over one or more entries (rotation families). Returns the record."""
    t0 = time.time()
    rng0 = random.Random(a.seed)
    # entries: a short screen of each when there are several
    screens = {}
    if len(sims) > 1:
        for name, sim in sims.items():
            sub = argparse.Namespace(**dict(vars(a), budget=a.screen_budget, max_rounds=3))
            data, _ = search(space, sim, starts, random.Random(rng0.randrange(1 << 30)), sub, log, label=f"[{name} screen] ")
            screens[name] = max(v[1] for v in data.values()) if data else 0.0
        top = max(screens.values())
        chosen = [n for n, v in sorted(screens.items(), key=lambda x: -x[1]) if v >= top * (1 - a.entry_margin)]
    else:
        chosen = list(sims)
    runs, finalists = [], []
    for name in chosen:
        sim = sims[name]
        for r in range(a.runs):
            rng = random.Random(rng0.randrange(1 << 30))
            data, trace = search(space, sim, starts, rng, a, log, label=f"[{name} run {r + 1}] ")
            ranked = sorted(data.values(), key=lambda v: -v[1])
            runs.append({"entry": name, "run": r + 1, "simulated": len(data), "best_screen": _r(ranked[0][1]), "best_split": space.split(ranked[0][0]),
                         "best": key(ranked[0][0]), "trace": trace})
            for f, d in ranked[: a.finalists]:
                finalists.append((name, f))
            runs[-1]["finalists"] = [key(f) for f, d in ranked[: a.finalists]]
            if r == 0 and name == chosen[0]:
                imp = importance(space, data, rng)
    # race per entry (an entry's rotation is part of the build), then across entries on the same seeds
    best_per_entry = []
    for name in chosen:
        cands, seen = [], set()
        for n, f in finalists:
            if n == name and key(f) not in seen:
                seen.add(key(f))
                cands.append(f)
        stage1 = {}
        stages = getattr(a, "race_stages", None) or ((10000, 2, 5), (30000, 3, 2), (100000, 4, 2))
        last, hist = race(sims[name], cands, log, stages=stages, first=stage1)
        top1 = max(stage1.values()) if stage1 else 0.0
        for r in runs:
            if r["entry"] == name and stage1:
                r["best_stage1_gap"] = round(max(stage1.get(k, 0.0) for k in r["finalists"]) / top1 - 1, 4) if top1 else None
        its, conf_its = getattr(a, "cert_its", None) or (3000, 30000)
        win, cert = certificate(space, sims[name], last[0][0], log, its=its, conf_its=conf_its)
        if key(win) != key(last[0][0]):
            last, hist2 = race(sims[name], [win, last[0][0]], log, stages=(stages[-1][:2] + (2,),))
            hist += hist2
        best_per_entry.append((name, last, hist, cert))
    best_per_entry.sort(key=lambda x: -x[1][0][1])
    name, last, hist, cert = best_per_entry[0]
    win, wd, wse = last[0]
    ru = last[1] if len(last) > 1 else None
    # a run agrees when its own finalists reached the top within noise (0.3%) on the race's first stage (every finalist, one seed)
    agree = [r["entry"] == name and (r.get("best_stage1_gap") is not None and r["best_stage1_gap"] >= -0.003) for r in runs]
    rec = {"class": space.cls, "spec": space.spec, "setting": sims[name].setting, "entry": name, "date": TODAY,
           "constraint": "spec field (entry rotation)" if space.any else (f"Hybrid of {' and '.join(space.pair)}" if space.pair else f"{space.spec} 30+"),
           "protected": sorted(space.protect), "entries_screened": {k: _r(v) for k, v in screens.items()}, "entries_searched": chosen,
           "winner": {"allocation": {t: [[n, win[n]] for n in space.by_tree[t] if win.get(n)] for t in space.tree_names}, "split": space.split(win),
                      "dps": _r(wd), "se": _r(wse, 3), "iterations": 100000},
           "runner_up": ({"split": space.split(ru[0]), "dps": _r(ru[1]), "se": _r(ru[2], 3),
                          "differs": sorted(set(key(ru[0])) ^ set(key(win)))} if ru else None),
           "gap_to_runner_up": round(wd / ru[1] - 1, 4) if ru else None,
           "runs": [dict({k: v for k, v in r.items() if k not in ("best", "finalists")}, agrees_with_winner=ag) for r, ag in zip(runs, agree)],
           "runs_agree": sum(agree), "race": hist, "certificate": cert,
           "other_entries": [{"entry": n, "dps": _r(l[0][1]), "split": space.split(l[0][0])} for n, l, _, _ in best_per_entry[1:]],
           "important_features": imp, "simulated_builds": sum(s.n for s in sims.values()),
           "simulated_fights": sum(s.fights for s in sims.values()), "minutes": round((time.time() - t0) / 60, 1)}
    return rec, win


# ------------------------------------------------------------------------------------------------ starts
def popular_allocs(cls):
    p = HERE.parent / "popular-builds.json"
    if not p.exists():
        return []
    d = json.load(open(p, encoding="utf-8")).get("classes", {}).get(cls, {})
    return [{n: r for items in b["allocation"].values() for n, r in items} for b in d.get("top") or [] if b.get("valid") and b.get("allocation")]


def preset_allocs(cls, entry, repo):
    sim_trees = R.load_trees(repo, cls)
    out = []
    for p in R.sim_presets(repo, {k: v for k, v in entry.items() if k != "preset_names"}):
        out.append({n: r for items in R.preset_allocation(sim_trees, p["talents"]).values() for n, r in items})
    return out


def protected(cls, entries, repo, setting, start_builds):
    """Talents the rotations read that the spec's builds hold."""
    sim_trees = R.load_trees(repo, cls)
    names = {(t.get("fancyName") or t.get("fieldName")): (R.talent_key(t) or t.get("fieldName")) for tr in sim_trees for t in tr["talents"]}
    held = set().union(*[set(b) for b in start_builds]) if start_builds else set()
    common = None
    for e in entries:
        dep = {names.get(n, n) for n in R.apl_talents(repo, R.SPECS[cls][e], sim_trees, setting)}
        common = dep if common is None else common & dep
    # a talent every start holds and the rotation reads stays; one only some starts hold is left to the search
    return {n for n in (common or set()) if start_builds and all(b.get(n) for b in start_builds)} & held


def parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--entry", action="append", required=True)
    ap.add_argument("--setting", default="dummy", choices=["dummy", "raid"])
    ap.add_argument("--gear", help="gear set (.gear.json) passed per build; default: each entry's gear")
    ap.add_argument("--start", action="append", default=[], help="extra start: build id or candidate .json")
    ap.add_argument("--any-split", action="store_true", help="no tree rule (a spec defined by its entry's rotation)")
    ap.add_argument("--runs", type=int, default=2)
    ap.add_argument("--budget", type=int, default=2500, help="builds simulated per run (screening)")
    ap.add_argument("--screen-budget", type=int, default=600, help="builds per entry in the entry screen")
    ap.add_argument("--entry-margin", type=float, default=0.02)
    ap.add_argument("--screen", type=int, default=1000, help="iterations per screened build (seed 1)")
    ap.add_argument("--max-rounds", type=int, default=14)
    ap.add_argument("--patience", type=int, default=4)
    ap.add_argument("--batch", type=int, default=200)
    ap.add_argument("--pool", type=int, default=6000)
    ap.add_argument("--parents", type=int, default=32)
    ap.add_argument("--random-init", type=int, default=250)
    ap.add_argument("--kappa", type=float, default=1.5)
    ap.add_argument("--min-gain", type=float, default=0.001)
    ap.add_argument("--finalists", type=int, default=6)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--write")
    return ap


def own_starts(cls, spec, entries, repo, extra=()):
    """The search's starts: our raid builds of the spec, the entries' simulator presets, talentsforever.com's popular builds and any
    extra allocations (earlier winners); the caller keeps those its space admits."""
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    starts = [R.alloc_of(b) for b in data.values()
              if SM.mode_of(b) == "raid" and b.get("role") not in ("healer", "tank") and SM.spec_of(cls, b) == spec]
    for e in entries:
        starts += preset_allocs(cls, R.SPECS[cls][e], repo)
    return starts + popular_allocs(cls) + [dict(x) for x in extra if x]


def run_target(cls, spec, entries, setting, gear_path, a, log, extra_starts=(), any_split=False, protect=None):
    """One spec, one setting, one gear set: the record and the winning allocation."""
    repo = R.repo_path(argparse.Namespace(repo=None))
    starts = own_starts(cls, spec, entries, repo, extra_starts)
    gear = json.load(open(ROOT / gear_path if not pathlib.Path(gear_path).is_absolute() else gear_path, encoding="utf-8"))["items"] if gear_path else None
    space = Space(cls, spec, any_split=any_split)
    own = [st for st in starts if space.valid(st)]
    space.protect = set(protect) if protect is not None else protected(cls, entries, repo, setting, own)
    space.start_splits = [space.split(st) for st in own]
    starts = [st for st in starts if space.valid(st)]
    log(f"== {cls} {spec} ({setting}, {pathlib.Path(gear_path).name if gear_path else 'entry gear'}): {len(starts)} valid starts, "
        f"entries {', '.join(entries)}; kept: {', '.join(sorted(space.protect)) or 'none'}")
    if not starts:
        b = space.random_build(random.Random(a.seed))
        starts = [b] if b else []
    sims = {e: Sim(cls, e, setting, gear, repo, f"ml-{cls}-{e}-{setting}") for e in entries}
    rec, win = optimize(space, sims, starts, a, log)
    rec["gear"] = gear_path
    log(f"  winner {rec['winner']['split']} in {rec['entry']}: {_f(rec['winner']['dps'])} ± {rec['winner']['se']:.2f} DPS"
        + (f"; runner-up {rec['runner_up']['split']} {rec['gap_to_runner_up']:+.2%}" if rec.get("runner_up") else "")
        + f"; runs agreeing {rec['runs_agree']}/{len(rec['runs'])}; {rec['simulated_builds']} builds, {rec['minutes']} min")
    return rec, win


def defaults(**kw):
    """The search's settings as parsed from an empty command line, with overrides (for callers such as ml_pipeline.py)."""
    a = parser().parse_args(["x", "--spec", "x", "--entry", "x"])
    for k, v in kw.items():
        setattr(a, k, v)
    return a


def main():
    a = parser().parse_args()
    R.set_game("forever")
    extra = []
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", a.cls), encoding="utf-8"))["builds"]}
    for st in a.start:
        extra.append(R.alloc_of(json.load(open(st, encoding="utf-8"))) if st.endswith(".json") else R.alloc_of(data[st]))
    rec, win = run_target(a.cls, a.spec, a.entry, a.setting, a.gear, a, lambda m: print(m, flush=True), extra, a.any_split)
    if a.write:
        pathlib.Path(a.write).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(a.write).write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
