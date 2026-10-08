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
import spec_modes as SM  # noqa: E402  (own-rotation rule: RAID_ENTRY_TREES)


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
        """Sequential fit on the certificate's builds (`builds_all`: what each changed against the winner, payment included):
        1. a present talent's main effect = the gain of the build that removes only it;
        2. a missing talent's main effect = the gain of its single build minus the main effects of the talents that paid for it;
        3. a pair's interaction = the gain of its build minus every main effect it changed (added, removed, paid).
        Each measured build is then reproduced exactly by the model; unmeasured pairs count 0."""
        self.space = space
        self.w = {n: r for items in syn["winner_allocation"].values() for n, r in items if r}
        self.rank = {n: self.w.get(n) or space.max[n] for n in space.relevant()}
        diffs = syn.get("builds_all") or {}
        self.main = {}
        for lab, d in diffs.items():   # 1. removals
            if lab.startswith("-") and " - " not in lab and len(d["removed"]) == 1 and not d["added"]:
                self.main[next(iter(d["removed"]))] = d["gain"]
        unknown = set()
        for lab, d in diffs.items():   # 2. additions (one talent added, possibly with tier fillers and prerequisites: all part of its effect)
            if lab.startswith("-") or " + " in lab or " - " in lab or lab.endswith((" -1", " -2")):
                continue
            paid = [n for n in d["removed"] if n != lab]
            if any(n not in self.main for n in paid):
                unknown.add(lab)
                continue
            self.main[lab] = d["gain"] - sum(self.main[n] for n in paid)
        self.pair = {}
        for lab, d in diffs.items():   # 3. pairs: (a added, b added) | (a added, b removed: "a - b") | (both removed: "-a - b")
            if " + " in lab:
                a, b = lab.split(" + ")
                changed = [n for n in list(d["added"]) + list(d["removed"]) if n not in (a, b)]
                if a in self.main and b in self.main and all(n in self.main for n in changed):
                    self.pair[(a, b)] = d["gain"] - self.main[a] - self.main[b] - sum(self.main[n] for n in changed)
            elif lab.startswith("-") and " - " in lab:
                a, b = lab[1:].split(" - ")
                if a in self.main and b in self.main:
                    self.pair[(a, b)] = d["gain"] - self.main[a] - self.main[b]
            elif " - " in lab:
                a, b = lab.split(" - ")   # a added, b removed, the rest paid
                changed = [n for n in list(d["added"]) + list(d["removed"]) if n not in (a, b)]
                if a in self.main and b in self.main and all(n in self.main for n in changed):
                    self.pair[(a, b)] = d["gain"] - self.main[a] - self.main[b] - sum(self.main[n] for n in changed)
        self.present = {n for n in self.main if self.w.get(n)}
        self.missing = {n for n in self.main if not self.w.get(n)}
        self.minus = {}    # present talent -> gain with one rank less (the state "minus")
        self.minus2 = {}   # present talent -> gain with two ranks less (the state "minus2", talents with 3+ ranks)
        for lab, d in diffs.items():
            if lab.endswith(" -1") and len(d["removed"]) == 1 and not d["added"]:
                self.minus[lab[:-3]] = d["gain"]
            elif lab.endswith(" -2") and len(d["removed"]) == 1 and not d["added"]:
                self.minus2[lab[:-3]] = d["gain"]
        if unknown:
            print(f"   model: {len(unknown)} single builds paid with a talent of unknown effect, left out", flush=True)

    def state_delta(self, n, state):
        """Main effect of talent n in a state: 'in' (the winner's rank or full), 'minus' (one rank less), 'minus2' (two less), 'out'."""
        if state == "in":
            return self.main[n] if n in self.missing else 0.0
        if state == "minus":
            return self.minus.get(n, self.main[n] / max(1, self.w.get(n, 1)))
        if state == "minus2":
            return self.minus2.get(n, 2 * self.main[n] / max(1, self.w.get(n, 1)))
        return 0.0 if n in self.missing else self.main[n]

    def state_pair(self, a, sa, b, sb):
        """Interaction for two states; a 'minus' / 'minus2' state takes the removal term scaled by the ranks out of the talent's ranks."""
        def frac(n, s):
            r = max(1, self.w.get(n, 1))
            return {"in": 0.0, "minus": 1.0 / r, "minus2": 2.0 / r, "out": 1.0}[s]
        fa, fb = frac(a, sa), frac(b, sb)
        if a in self.missing:
            fa = 1.0 if sa == "in" else 0.0
        if b in self.missing:
            fb = 1.0 if sb == "in" else 0.0
        v = self.pair.get((a, b))
        if v is None:
            v = self.pair.get((b, a))
            if v is None:
                return 0.0
            a, b, fa, fb = b, a, fb, fa
        # the measured term applies to: both missing in | a missing in and b present out | both present out
        return v * fa * fb

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
        if a in self.missing and b in self.present:   # fitted on the build with a added and b removed
            return v if (ina and not inb) else 0.0
        if a in self.present and b in self.present:
            return v if (not ina and not inb) else 0.0
        return 0.0


def tree_subsets(space, model, tree, live_t, dead_t):
    """[(points, score, chosen)] for every subset of the tree's live talents, with tier fillers from the dead talents and prerequisites."""
    out = []
    dead_room = sorted(((space.row[d], d, space.max[d]) for d in dead_t), key=lambda x: x[0])
    # states per live talent: missing -> out / in; present -> out / (minus two) / (minus one) / in by its ranks; the combinations per
    # tree are capped at 300,000 by dropping the minus-two state of the talents with the smallest effects
    def opts(t, two=True):
        r = model.w.get(t, 0)
        if t in model.missing or r < 2:
            return ("out", "in")
        if r >= 3 and two:
            return ("out", "minus2", "minus", "in")
        return ("out", "minus", "in")
    options = [opts(t) for t in live_t]
    total = 1
    for o in options:
        total *= len(o)
    by_effect = sorted(live_t, key=lambda n: abs(model.main.get(n, 0)))
    while total > 300000 and by_effect:
        t = by_effect.pop(0)
        i = live_t.index(t)
        if len(options[i]) == 4:
            options[i] = opts(t, two=False)
            total = 1
            for o in options:
                total *= len(o)
    for states in itertools.product(*options):
            sel = {t for t, s in zip(live_t, states) if s != "out"}
            st_of = dict(zip(live_t, states))
            chosen = tuple(sel)
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
            ranks = {t: model.rank[t] - {"minus": 1, "minus2": 2}.get(st_of[t], 0) for t in chosen}
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
            score = sum(model.state_delta(t, st_of[t]) for t in live_t)
            for a, b in itertools.combinations(live_t, 2):
                score += model.state_pair(a, st_of[a], b, st_of[b])
            out.append((points, score, dict(ranks, **filler), st_of))
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
        for points, score, build, st_of in subs:
            lst = best.setdefault((t, points), [])
            lst.append((score, build, st_of))
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
            for s1, b1, st1 in best[(T[0], p1)]:
                for s2, b2, st2 in best[(T[1], p2)]:
                    for s3, b3, st3 in best[(T[2], p3)]:
                        build = dict(b1, **b2, **b3)
                        states = dict(st1, **st2, **st3)
                        cross = 0.0
                        for a in by_tree[T[0]] + by_tree[T[1]] + by_tree[T[2]]:
                            for b in live:
                                if b <= a or space.tree_of[a] == space.tree_of[b] or b not in states:
                                    continue
                                cross += model.state_pair(a, states[a], b, states[b])
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
    cur = FS.flat_of((e.get("again") or e["first"])["winner"]["allocation"])
    measured = {n: r for items in (syn.get("winner_allocation") or {}).values() for n, r in items if r} if syn else {}
    if "singles_all" not in syn or measured != cur:
        # the certificate measured around an older winner (its own re-search moved it): measure again around the current one
        # (2026-10-07 audit: the standalone run re-found the hunter Lone Wolf lead against the old winner and re-searched it for nothing)
        log(f"== {cls} {entry}: {'no full measurements' if 'singles_all' not in syn else 'the certificate measured an older winner'}; measuring around the current winner")
        if syn:
            e["synergy_before_structural"] = syn
        e.pop("synergy", None)
        SY.certificate(cls, entry, e, repo, None, save, argparse.Namespace(no_search=True))
        syn = e.get("synergy") or {}
        if "singles_all" not in syn:
            return
    space = MLT.Space(cls, "any", any_split=True)
    space.allow_trees = SM.RAID_ENTRY_TREES.get((cls, entry))   # leads only among builds that may use the entry's rotation (2026-10-08)
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
    if leads and not getattr(a, "no_search", False):
        SY.research(cls, entry, e, repo, save, leads, leads[0], e["structural"], "structural ranking")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--entry", action="append")
    ap.add_argument("--top", type=int, default=300)
    ap.add_argument("--race", type=int, default=20)
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--no-search", action="store_true", help="rank, simulate and race only; no re-search on a lead")
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
