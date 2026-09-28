"""Find the best legal 51-point build for a (class, spec model, profile), then order the points by level.

Stage A — 60 build:
  1. Bundle-greedy: at each step every talent's next rank is evaluated as a *bundle* = the rank itself plus any
     unmet prerequisites plus the cheapest gating filler needed to unlock its tier; bundles are ranked by value
     per point. This is what lets a 1-point capstone behind a 3-point prerequisite compete fairly.
     Restarted once unconstrained and once per tree with a "reach 31 in this tree first" constraint.
  2. Re-spend search: for each talent in the build, remove all its points and refill greedily; keep the best.
  3. Local search: move 1-3 points between talents while legal, until nothing improves.
Stage B — leveling order: at each level pick the legal talent from the target build that maximises the
cumulative score over the next `lookahead` levels (greedy rollout), so gating fillers that unlock a strong
talent are taken early enough and earlier rows are backfilled when they score higher. A receding horizon
still misses talents deeper than the horizon (Mortal Strike at 31 points), so the order is also built by
rushing each deep talent of the build (its cheapest path first, then the horizon rule) and the variant with
the best sum of per-level scores from 10 to the last point wins (`order_label` names it).

Both stages use the same legality rules as validate_builds.py (tiers, prerequisites, rank caps).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from effects import load_tree, load_effects  # noqa: E402
from model import Evaluator, effects_for, load_profiles, load_specs, profile_modes  # noqa: E402

TOTAL = 51


class Tree:
    def __init__(self, game, cls):
        self.game, self.cls = game, cls
        self.trees = load_tree(game, cls)
        self.info = {}       # talent -> (tree, row, max, requires)
        for tname, talents in self.trees.items():
            for name, t in talents.items():
                self.info[name] = (tname, t["row"], t["max"], t["requires"])
        self.order = list(self.trees)

    def tree_points(self, alloc, tname):
        return sum(r for n, r in alloc.items() if self.info[n][0] == tname)

    def points_below(self, alloc, tname, row):
        return sum(r for n, r in alloc.items() if self.info[n][0] == tname and self.info[n][1] < row)

    def can_add(self, alloc, name):
        tname, row, mx, req = self.info[name]
        if alloc.get(name, 0) >= mx:
            return False
        if self.points_below(alloc, tname, row) < row * 5:
            return False
        for rn, rr in req:
            if alloc.get(rn, 0) < rr:
                return False
        return True

    def legal(self, alloc):
        for name, r in alloc.items():
            if r <= 0:
                continue
            tname, row, mx, req = self.info[name]
            if r > mx or self.points_below(alloc, tname, row) < row * 5:
                return False
            for rn, rr in req:
                if alloc.get(rn, 0) < rr:
                    return False
        return True

    def split(self, alloc):
        return "/".join(str(self.tree_points(alloc, t)) for t in self.order)


def _add(alloc, name, k=1):
    alloc[name] = alloc.get(name, 0) + k


def _remove(alloc, name, k=1):
    alloc[name] -= k
    if alloc[name] <= 0:
        del alloc[name]


class Optimizer:
    def __init__(self, game, cls, spec_id, profile_id):
        self.tree = Tree(game, cls)
        self.effects = load_effects(game, cls)
        self.spec = dict(load_specs(cls)[spec_id], id=spec_id)   # effects may be restricted to spec models via "specs"
        self.profile = load_profiles()[profile_id]
        self.profile["id"] = profile_id
        self._ev = {}
        self._cache = {}
        self.total = TOTAL   # points to spend (51 at 60; respec.py lowers it for level-N builds)
        # synergy ("requires") talents declared on effects are bundled like prerequisites when evaluating a talent
        self.soft_req = {}
        for name, e in self.effects.items():
            for eff in e["effects"]:
                for t, r in (eff.get("requires") or {}).items():
                    self.soft_req.setdefault(name, {})
                    self.soft_req[name][t] = max(self.soft_req[name].get(t, 0), r)

    def evaluator(self, level):
        if level not in self._ev:
            self._ev[level] = Evaluator(self.spec, self.profile, level, self.tree.game, talents=set(self.tree.info))
        return self._ev[level]

    def score(self, alloc, level=60, detail=False):
        sup = [x if isinstance(x, str) else x["talent"] for x in self.profile.get("suppress_talents", [])
               if isinstance(x, str) or ((not x.get("games") or self.tree.game in x["games"]) and (not x.get("classes") or self.tree.cls in x["classes"]))]
        a = {n: r for n, r in alloc.items() if n not in sup and r > 0} if sup else {n: r for n, r in alloc.items() if r > 0}
        ctx = (self.spec["id"], frozenset(profile_modes(self.profile)), None)
        if detail:
            return self.evaluator(level).score(effects_for(a, self.effects, *ctx), True, allocation=a)
        key = (level, tuple(sorted(a.items())))
        v = self._cache.get(key)
        if v is None:
            v = self.evaluator(level).score(effects_for(a, self.effects, *ctx), allocation=a)
            self._cache[key] = v
        return v

    # ------------------------------------------------------------ bundles
    def _marginals(self, alloc, level, names=None):
        base = self.score(alloc, level)
        out = {}
        for name in (names or self.tree.info):
            if alloc.get(name, 0) >= self.tree.info[name][2]:
                continue
            _add(alloc, name)
            out[name] = self.score(alloc, level) - base
            _remove(alloc, name)
        return out

    def _ensure(self, work, bundle, name, ranks, pool, level, _stack=frozenset()):
        """Recursively add (to `work`, recording in `bundle`) everything needed for `name` to reach `ranks`:
        its prerequisites (each with their own gating), then gating filler for its tier, then the ranks.
        `pool` restricts usable talents/ranks to a target build (None = whole tree). Returns False if impossible.
        `_stack` holds the talents being resolved: synergy partners can need each other (Fingers of Frost needs Shatter,
        Shatter's raid value needs Fingers of Frost), and a partner already on the stack is being added by its caller."""
        tname, row, mx, req = self.tree.info[name]
        if ranks > mx or (pool is not None and ranks > pool.get(name, 0)):
            return False
        _stack = _stack | {name}
        for rn, rr in req:
            if not self._ensure(work, bundle, rn, rr, pool, level, _stack):
                return False
        for rn, rr in self.soft_req.get(name, {}).items():
            if rn in _stack:
                continue
            if pool is not None and pool.get(rn, 0) < rr:
                continue  # the target build does not contain the synergy partner: value it without it
            if work.get(rn, 0) < rr and not self._ensure(work, bundle, rn, rr, pool, level, _stack):
                return False
        while self.tree.points_below(work, tname, row) < row * 5:
            names = pool if pool is not None else self.tree.info
            cands = [n for n in names if self.tree.info[n][0] == tname and self.tree.info[n][1] < row
                     and self.tree.can_add(work, n) and (pool is None or work.get(n, 0) < pool[n])]
            if not cands:
                return False
            m = self._marginals(work, level, cands)
            pick = max(cands, key=lambda n: (m[n], -self.tree.info[n][1]))
            _add(work, pick)
            bundle.append(pick)
        while work.get(name, 0) < ranks:
            _add(work, name)
            bundle.append(name)
        return True

    def bundle_for(self, alloc, name, level, budget, focus_tree=None):
        """Points needed to legally add one rank of `name`: {talent: extra ranks}. None if it does not fit."""
        tname, row, mx, req = self.tree.info[name]
        if alloc.get(name, 0) >= mx or (focus_tree and tname != focus_tree):
            return None
        work, seq = dict(alloc), []
        if not self._ensure(work, seq, name, alloc.get(name, 0) + 1, None, level):
            return None
        if len(seq) > budget or not self.tree.legal(work):
            return None
        bundle = {}
        for n in seq:
            bundle[n] = bundle.get(n, 0) + 1
        return bundle

    def greedy(self, focus_tree=None, level=60):
        alloc = {}
        while sum(alloc.values()) < self.total:
            budget = self.total - sum(alloc.values())
            focus = focus_tree if (focus_tree and self.tree.tree_points(alloc, focus_tree) < 31) else None
            base = self.score(alloc, level)
            best, best_v = None, None
            for name in self.tree.info:
                b = self.bundle_for(alloc, name, level, budget, focus)
                if not b:
                    continue
                trial = dict(alloc)
                for n, k in b.items():
                    _add(trial, n, k)
                cost = sum(b.values())
                v = (self.score(trial, level) - base) / cost - self.tree.info[name][1] * 1e-7
                if best_v is None or v > best_v:
                    best, best_v = b, v
            if best is None:
                break
            for n, k in best.items():
                _add(alloc, n, k)
        return alloc

    # ------------------------------------------------------------ improvement passes
    def local_search(self, alloc, level=60, max_move=3):
        alloc = dict(alloc)
        cur = self.score(alloc, level)
        improved = True
        while improved:
            improved = False
            names = list(self.tree.info)
            for k in range(1, max_move + 1):
                for src in [n for n in names if alloc.get(n, 0) >= k]:
                    for dst in names:
                        if dst == src:
                            continue
                        trial = dict(alloc)
                        _remove(trial, src, k)
                        _add(trial, dst, k)
                        if trial[dst] > self.tree.info[dst][2] or not self.tree.legal(trial):
                            continue
                        s = self.score(trial, level)
                        if s > cur + 1e-9:
                            alloc, cur, improved = trial, s, True
                            break
                    if improved:
                        break
                if improved:
                    break
        return alloc, cur

    def refill(self, alloc, level=60):
        """Greedy bundle fill from a partial allocation."""
        alloc = dict(alloc)
        while sum(alloc.values()) < self.total:
            budget = self.total - sum(alloc.values())
            base = self.score(alloc, level)
            best, best_v = None, None
            for name in self.tree.info:
                b = self.bundle_for(alloc, name, level, budget)
                if not b:
                    continue
                trial = dict(alloc)
                for n, k in b.items():
                    _add(trial, n, k)
                v = (self.score(trial, level) - base) / sum(b.values())
                if best_v is None or v > best_v:
                    best, best_v = b, v
            if best is None:
                break
            for n, k in best.items():
                _add(alloc, n, k)
        return alloc

    def respend_search(self, alloc, level=60):
        best, best_s = dict(alloc), self.score(alloc, level)
        improved = True
        while improved:
            improved = False
            for name in list(best):
                trial = dict(best)
                del trial[name]
                # dropping a talent may orphan dependants / gating: strip until legal
                changed = True
                while changed and trial:
                    changed = False
                    for n in list(trial):
                        t2 = dict(trial); del t2[n]
                        if not self.tree.legal(trial) and self.tree.legal(t2):
                            trial = t2; changed = True; break
                if not self.tree.legal(trial):
                    continue
                cand = self.refill(trial, level)
                s = self.score(cand, level)
                if s > best_s + 1e-9:
                    best, best_s, improved = cand, s, True
                    break
        return best, best_s

    def best_build(self, level=60, seeds=()):
        """Best of the greedy starts (overall and per tree) and any seed builds (e.g. the compared community or hand build), each
        improved by respend and local search: the result never scores below a seed's own local optimum."""
        candidates = [self.greedy(None, level)] + [self.greedy(t, level) for t in self.tree.order] + [dict(s) for s in seeds]
        best, best_s = None, None
        for c in candidates:
            a, s = self.respend_search(c, level)
            a, s = self.local_search(a, level)
            if best_s is None or s > best_s:
                best, best_s = a, s
        return best, best_s

    # ------------------------------------------------------------ stage B
    def _target_bundle(self, state, target, name):
        """Ordered points (from the target build only) needed before `name` takes its next rank, ending with it."""
        if state.get(name, 0) >= target.get(name, 0):
            return None
        work, seq = dict(state), []
        if not self._ensure(work, seq, name, state.get(name, 0) + 1, target, 60):
            return None
        return seq

    def _plan_value(self, state, target, first_bundle, level, horizon):
        """Cumulative score over `horizon` levels: take the bundle one point per level, then greedy bundles."""
        st = dict(state)
        total, lv = 0.0, level
        queue = list(first_bundle)
        end = min(level + horizon - 1, 60)
        while lv <= end:
            if not queue:
                # greedy: best value-per-point bundle among remaining target talents
                best, best_v = None, None
                base = self.score(st, lv)
                for n in target:
                    b = self._target_bundle(st, target, n)
                    if not b:
                        continue
                    trial = dict(st)
                    for x in b:
                        _add(trial, x)
                    v = (self.score(trial, lv) - base) / len(b)
                    if best_v is None or v > best_v:
                        best, best_v = b, v
                if best is None:
                    break
                queue = list(best)
            _add(st, queue.pop(0))
            total += self.score(st, lv)
            lv += 1
        return total

    def order(self, target, lookahead=6, start_state=None, start_level=10):
        """Best of the receding-horizon order and one 'rush' variant per deep talent (tier 5 and deeper) of the
        target, judged by the sum of the per-level scores over the whole order. Sets `order_label`."""
        best = self.order_horizon(target, lookahead, start_state, start_level)
        best_v, label = self.order_value(best), "receding horizon"
        for name in self.milestones(target):
            steps = self.order_rush(target, name, lookahead, start_state, start_level)
            if steps is None:
                continue
            v = self.order_value(steps)
            if v > best_v + 1e-9:
                best, best_v, label = steps, v, f"rush {name} (reached at level {next(lv for lv, n, _, _ in steps if n == name)})"
        self.order_label = label
        return best

    @staticmethod
    def order_value(steps):
        return sum(sc for _, _, _, sc in steps)

    def milestones(self, target):
        """Deep talents of the build: row index 4 and deeper (20+ points in the tree), deepest first."""
        names = [n for n in target if self.tree.info[n][1] >= 4]
        return sorted(names, key=lambda n: (-self.tree.info[n][1], n))

    def order_rush(self, target, name, lookahead, start_state=None, start_level=10):
        """Buy the cheapest path (within the target build) to `name`'s first rank one point per level, then continue
        with the receding-horizon rule."""
        state = dict(start_state or {})
        seq = self._target_bundle(state, target, name)
        if not seq:
            return None
        steps, level = [], start_level
        for pick in seq:
            _add(state, pick)
            steps.append((level, pick, state[pick], self.score(state, level)))
            level += 1
        return steps + self.order_horizon(target, lookahead, state, level)

    def order_horizon(self, target, lookahead=6, start_state=None, start_level=10):
        """Receding-horizon order: at each level evaluate every target talent's bundle over `lookahead`
        levels and commit only the first point of the best plan. Runs from `start_state` at `start_level`
        until the target is fully bought (level 9 + its point count)."""
        state = dict(start_state or {})
        steps = []
        last = 9 + sum(target.values())
        for level in range(start_level, last + 1):
            best, best_v = None, None
            for n in target:
                b = self._target_bundle(state, target, n)
                if not b:
                    continue
                v = self._plan_value(state, target, b, level, lookahead)
                if best_v is None or v > best_v + 1e-12:
                    best, best_v = b, v
            pick = best[0]
            _add(state, pick)
            steps.append((level, pick, state[pick], self.score(state, level)))
        return steps

    # ------------------------------------------------------------ analysis helpers
    def marginal_table(self, alloc, level=60):
        base = self.score(alloc, level)
        rows = []
        for name, (tname, row, mx, req) in self.tree.info.items():
            r = alloc.get(name, 0)
            if r >= mx:
                continue
            trial = dict(alloc); trial[name] = r + 1
            s = self.score(trial, level) - base
            rows.append((s, name, tname, row + 1, r + 1, mx, self.tree.can_add(alloc, name), self.effects[name]["source"]))
        rows.sort(key=lambda x: -x[0])
        return rows

    def compress_order(self, steps):
        runs = []
        for level, name, rank, _ in steps:
            if runs and runs[-1][2] == name:
                runs[-1][3] += 1
                runs[-1][0] = f"{runs[-1][0].split('-')[0]}-{level}"
            else:
                runs.append([str(level), self.tree.info[name][0], name, 1])
        return [tuple(r) for r in runs]
