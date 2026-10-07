"""Synergy certificate for an open-search winner (2026-10-06, user request after the third missed build: "how do we stop missing
potentially good builds?"). Every build we missed was a synergy package: talents worth nothing alone and a lot together, behind a step
that costs value (Mortal Strike behind Sweeping Strikes; Summon Hawk with Lone Wolf; Shatter + Fingers of Frost + Ice Lance behind a
Frost tier). One-talent moves, random mutations and a model trained on random builds cannot see a package. This tool measures every
pair directly around the winner, so a two-talent package cannot hide, and polishes the leads into builds.

    python _reference/data/raidsim/synergy.py <class> [--entry <entry>] [--fresh] [--no-search]

Per done entry of `raidsim/families/<class>.json` (the open search's record), around the entry's final winner in a full raid:
1. relevant talents: those with damage wording (ml_talents.Space.relevant); missing = not in the winner, present = in it;
2. singles: the winner with each missing talent added at full rank (tier points the tree lacks come from a lower-row talent of the tree,
   present ones first; the cost is paid from the winner's cheapest points by its removal values, one point at a time, skipping any
   removal that breaks a tier or prerequisite) and the winner without each present talent (removal);
3. pairs: every pair of missing talents (any trees, the lower row added first so a pair's own lower talent is the tier filler) and every
   missing x present pair from different trees; all on SCREEN fights with common random numbers. Interaction = DPS(both) - DPS(a) - DPS(b)
   + DPS(winner): a package shows as a large positive interaction even when each half alone loses;
4. leads: the best pair builds (within LEAD_WINDOW of the winner) polished by the search's hill climb keeping the pair (every move,
   POLISH_FIGHTS), the best three raced against the winner on a fresh seed (RACE fights); a lead LEAD_BAR ahead is a miss of the search:
   the rotation is re-tuned on it, the open search runs again seeded with the leads (family_search's AGAIN budget), and the entry's
   winner, race and values are redone (--no-search: measure and report only);
5. record: entry["synergy"] = {relevant, missing, pairs, top singles, top interactions, leads, researched, minutes}; the class report
   (family_search.write_class) shows it. --fresh redoes an entry's certificate.
The certificate is complete at the pairwise level: three-talent packages are reached because the third member is one move from a pair
(Ice Lance from Shatter + Fingers of Frost). Simulator numbers are the community's model of the beta, not measurements.
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

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data"), str(ROOT / "_reference/data/scorer")]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


FS = _load("family_search_syn", HERE / "family_search.py")
MLT, R, SM, RSH = FS.MLT, FS.R, FS.SM, FS.RSH
TODAY = datetime.date.today().isoformat()
SCREEN = 1500        # fights per single and pair build (common random numbers, one seed)
POLISH_FIGHTS = 800  # the leads' hill climb
RACE = 10000         # the leads against the winner, a fresh seed
LEAD_WINDOW = 0.01   # pair builds within this of the winner on the screen are polished
LEAD_BAR = 0.005     # a polished lead this far ahead on the race means the search missed it
MAX_PAIRS = 2500
TOP_LEADS = 5


def log(m):
    print(m, flush=True)


def pay(space, flat, need, cost, keep):
    """Remove `need` points from `flat`, cheapest first (cost: {talent: value per point}; unknown = 0), never from `keep`, skipping any
    removal that breaks a tier or prerequisite. None when the points cannot be found."""
    new = dict(flat)
    left = need
    order = sorted((n for n in new if new[n] > 0 and n not in keep), key=lambda n: (cost.get(n, 0.0), n))
    progress = True
    while left and progress:
        progress = False
        for n in order:
            if not new.get(n):
                continue
            trial = dict(new)
            trial[n] -= 1
            if not trial[n]:
                del trial[n]
            if space.ok_partial(trial):
                new = trial
                left -= 1
                progress = True
                break
    return None if left else new


def add_talent(space, flat, t, ranks, cost):
    """`flat` with `ranks` of t, the tree's missing tier points filled from a lower-row talent (present ones first, then by row);
    returns (build, points added) or None."""
    new = dict(flat)
    tree = space.tree_of[t]
    below = sum(new.get(m, 0) for m in space.by_tree[tree] if space.row[m] < space.row[t])
    gap = 5 * space.row[t] - below
    added = 0
    if gap > 0:
        fillers = sorted((m for m in space.by_tree[tree] if space.row[m] < space.row[t] and space.max[m] > new.get(m, 0)),
                         key=lambda m: (0 if new.get(m) else 1, space.row[m], cost.get(m, 0.0), m))
        for m in fillers:
            take = min(gap, space.max[m] - new.get(m, 0))
            new[m] = new.get(m, 0) + take
            gap -= take
            added += take
            if not gap:
                break
        if gap:
            return None
    for q, r in space.req.get(t, []):   # a prerequisite the build lacks comes along
        if new.get(q, 0) < r:
            added += r - new.get(q, 0)
            new[q] = r
    new[t] = new.get(t, 0) + ranks
    added += ranks
    return new, added


def fill_up(space, flat, need, cost, keep):
    """Add `need` points to the cheapest talents with room (by cost; unknown = 0), legality kept; None when impossible."""
    new = dict(flat)
    left = need
    order = sorted((n for n in space.names if n not in keep), key=lambda n: (cost.get(n, 0.0), space.row[n], n))
    progress = True
    while left and progress:
        progress = False
        for n in order:
            if new.get(n, 0) >= space.max[n]:
                continue
            trial = dict(new)
            trial[n] = trial.get(n, 0) + 1
            if space.ok_partial(trial):
                new = trial
                left -= 1
                progress = True
                break
    return None if left else new


def with_talents(space, flat, talents, cost, drop=()):
    """A legal build: the winner without `drop`, with `talents` added (lower rows first, tier points filled, prerequisites brought
    along), then the points over 51 paid from its cheapest points, or the points short of 51 added to its cheapest talents with room."""
    new = {n: r for n, r in flat.items() if n not in drop}
    for t in sorted(talents, key=lambda t: (space.row[t], t)):
        r = add_talent(space, new, t, space.max[t] - new.get(t, 0), cost)
        if r is None:
            return None
        new, _ = r
    over = sum(new.values()) - 51
    keep = set(talents) | set(space.protect)
    if over > 0:
        new = pay(space, new, over, cost, keep=keep)
    elif over < 0:
        new = fill_up(space, new, -over, cost, keep=keep | set(drop))
    if new is None or not space.valid(new):
        return None
    return new


def tuned_near(cls, entry, flat, within=4):
    """Was the entry's rotation last tuned on a build within `within` rank differences of `flat` (the tune files family_search and
    apl_opt --tune leave under families/tune/)?"""
    for p in sorted((FS.OUT / "tune").glob(f"{cls}-{entry}*.json")):
        try:
            for b in json.load(open(p, encoding="utf-8")):
                al = b.get("allocation") or {}
                if al and all(isinstance(v, list) for v in al.values()):
                    al = {n: r for items in al.values() for n, r in items}
                if al and sum(abs(flat.get(n, 0) - al.get(n, 0)) for n in set(flat) | set(al)) <= within:
                    return True
        except (ValueError, AttributeError, TypeError):
            continue
    return False


def certificate(cls, entry, e, repo, st, save, a):
    t0 = time.time()
    space = MLT.Space(cls, "any", any_split=True)
    space.protect = set(e.get("first", {}).get("protected") or ())
    fin = e.get("again") or e["first"]
    w = FS.flat_of(fin["winner"]["allocation"])
    vals = e.get("values") or {}
    cost = {n: v["per_point"] for n, v in vals.items()}
    relevant = space.relevant()
    missing = [n for n in relevant if not w.get(n)]
    present = [n for n in relevant if w.get(n)]
    sim = MLT.Sim(cls, entry, "raid", None, repo, f"synergy-{cls}-{entry}")
    # Singles and pairs are measured UNPAID (2026-10-07): the winner with the talent(s) added at full rank or removed, no points taken
    # back, no tier fillers. The simulator applies a talent string as given, 51 points or not, so each effect is a clean marginal and
    # the structural model's variables stay binary; legality, tiers and the 51-point budget belong to the structural ranking and to the
    # lead builds below. (The first version paid for every addition from the winner's cheapest points, which confounded the effects
    # with partial ranks of the talents that paid, and skipped most removals as "illegal".)
    singles = {}
    builds, labels = [w], ["winner"]

    def added(flat, names):
        new = dict(flat)
        for n in names:
            new[n] = space.max[n]
        return new

    def removed(flat, names):
        return {n: r for n, r in flat.items() if n not in names}

    for t in missing:
        builds.append(added(w, [t]))
        labels.append(t)
    for t in present:
        builds.append(removed(w, [t]))
        labels.append(f"-{t}")
    for t in present:   # one rank less (2026-10-07): the structural model's third state; the real optimum shaves single points
        if w[t] >= 2:
            builds.append(dict(w, **{t: w[t] - 1}))
            labels.append(f"{t} -1")
    pairs = []   # (a, b, kind): "add" = both missing; "swap" = a missing in, b present out; "drop" = both present out
    for i, a1 in enumerate(missing):
        for b1 in missing[i + 1:]:
            pairs.append((a1, b1, "add"))
    for a1 in missing:
        for b1 in present:
            if space.tree_of[a1] != space.tree_of[b1]:
                pairs.append((a1, b1, "swap"))
    for i, a1 in enumerate(present):
        for b1 in present[i + 1:]:
            pairs.append((a1, b1, "drop"))
    rng = random.Random(97)
    if len(pairs) > MAX_PAIRS:
        rng.shuffle(pairs)
        pairs = pairs[:MAX_PAIRS]
    pair_kind = {}
    for a1, b1, kind in pairs:
        if kind == "add":
            builds.append(added(w, [a1, b1]))
            labels.append(f"{a1} + {b1}")
        elif kind == "swap":
            builds.append(removed(added(w, [a1]), [b1]))
            labels.append(f"{a1} - {b1}")
        else:
            builds.append(removed(w, [a1, b1]))
            labels.append(f"-{a1} - {b1}")
        pair_kind[(a1, b1)] = kind
    log(f"== {cls} {entry}: synergy certificate around {space.split(w)}: {len(relevant)} relevant talents, {len(missing)} missing; "
        f"{len(builds) - 1} builds ({len(pair_kind)} pairs) on {SCREEN} fights")
    res = sim.run(builds, SCREEN, 61)
    score = {lab: r[0] for lab, r in zip(labels, res)}
    base = score["winner"]
    # what each measured build changed against the winner (the structural model fits its effects from these)
    diffs = {}
    for lab, b in zip(labels, builds):
        if lab == "winner":
            continue
        diffs[lab] = {"added": {n: b[n] - w.get(n, 0) for n in b if b[n] > w.get(n, 0)},
                      "removed": {n: w[n] - b.get(n, 0) for n in w if w[n] > b.get(n, 0)}, "gain": round(score[lab] / base - 1, 5)}
    for t in missing:
        singles[t] = round(score[t] / base - 1, 4)
    for t in present:
        singles[f"-{t}"] = round(score[f"-{t}"] / base - 1, 4)
        if f"{t} -1" in score:
            singles[f"{t} -1"] = round(score[f"{t} -1"] / base - 1, 4)
    inter = {}
    removed_pairs = {}
    for (a1, b1), kind in pair_kind.items():
        if kind == "add":
            g = score[f"{a1} + {b1}"] / base - 1
            inter[f"{a1} + {b1}"] = {"gain": round(g, 4), "interaction": round(g - singles[a1] - singles[b1], 4)}
        elif kind == "swap":
            g = score[f"{a1} - {b1}"] / base - 1
            inter[f"{a1} + {b1}"] = {"gain": round(g, 4), "interaction": round(g - singles[a1] - singles[f"-{b1}"], 4), "kind": "swap"}
        else:
            g = score[f"-{a1} - {b1}"] / base - 1
            removed_pairs[f"{a1} + {b1}"] = {"gain": round(g, 4), "interaction": round(g - singles[f"-{a1}"] - singles[f"-{b1}"], 4)}
    top_pairs = sorted(inter.items(), key=lambda kv: -kv[1]["gain"])[:12]
    top_inter = sorted(inter.items(), key=lambda kv: -kv[1]["interaction"])[:12]
    rec = {"date": TODAY, "winner": space.split(w), "relevant": len(relevant), "missing": len(missing), "pairs": len(pair_kind),
           "screen_fights": SCREEN, "singles": dict(sorted(singles.items(), key=lambda kv: -kv[1])[:12]),
           "top_pairs": [{"pair": k, **v} for k, v in top_pairs], "top_interactions": [{"pair": k, **v} for k, v in top_inter], "leads": [],
           # every measurement, for the structural ranking (raidsim/structural.py): gains relative to the winner's DPS
           "base": round(base, 1), "winner_allocation": {t: [[n, w[n]] for n in space.by_tree[t] if w.get(n)] for t in space.tree_names},
           "singles_all": singles, "pairs_all": inter, "removed_pairs_all": removed_pairs, "builds_all": diffs}
    # leads: the pairs that gain or interact, ranked by gain plus interaction, built LEGALLY (tier points filled, the cost paid from
    # the winner's cheapest points, or points added where a swap leaves the build short) and screened; those within the window are
    # polished keeping the pair (a pair whose build neither gains nor interacts is a filler swap around the winner: 2026-10-07 audit)
    ranked = sorted(((v["gain"] + v["interaction"], k) for k, v in inter.items() if v["gain"] >= 0.002 or v["interaction"] >= 0.002), reverse=True)
    legal = []
    for _, lab in ranked[:TOP_LEADS * 4]:
        a1, b1 = lab.split(" + ")
        b = with_talents(space, w, [a1], cost, drop=[b1]) if b1 in present else with_talents(space, w, [a1, b1], cost)
        if b is not None:
            legal.append(((a1, b1), b))
    cands = []
    if legal:
        res2 = sim.run([b for _, b in legal], SCREEN, 61)
        cands = [(r[0], pair, b) for (pair, b), r in zip(legal, res2) if r[0] >= base * (1 - LEAD_WINDOW)]
        cands.sort(key=lambda x: -x[0])
        log(f"   {len(legal)} lead builds screened, {len(cands)} within {LEAD_WINDOW:.0%} of the winner")
    polished = []
    for sc, pair, b in cands[:TOP_LEADS]:
        x, sx = MLT.polish(space, sim, b, POLISH_FIGHTS, 62, rounds=24, min_gain=0.002, keep=pair, small=False)
        polished.append((sx, pair, x))
        log(f"    lead {pair[0]} + {pair[1]}: {space.split(b)} {sc:.1f} -> polished {space.split(x)} {sx:.1f} (winner {base:.1f} on {SCREEN})")
    leads = []
    if polished:
        polished.sort(key=lambda t: -t[0])
        top = polished[:3]
        r2 = sim.run([w] + [x for _, _, x in top], RACE, 63)
        for (sx, pair, x), (d, sd) in zip(top, r2[1:]):
            gain = d / r2[0][0] - 1
            leads.append({"pair": f"{pair[0]} + {pair[1]}", "split": space.split(x), "dps": round(d, 1), "gain": round(gain, 4),
                          "allocation": {t: [[n, x[n]] for n in space.by_tree[t] if x.get(n)] for t in space.tree_names}})
            log(f"    race: {pair[0]} + {pair[1]} {space.split(x)} {d:.1f} against the winner {r2[0][0]:.1f} ({gain:+.2%})")
    rec["leads"] = leads
    rec["minutes"] = round((time.time() - t0) / 60, 1)
    e["synergy"] = rec
    save()
    ahead = [ld for ld in leads if ld["gain"] >= LEAD_BAR]
    if not ahead or a.no_search:
        log(f"  {cls} {entry}: certificate {'confirms the winner' if not ahead else 'found leads (no search: --no-search)'} ({rec['minutes']} min)")
        return
    research(cls, entry, e, repo, save, leads, max(ahead, key=lambda ld: ld["gain"]), rec, "synergy certificate")


def research(cls, entry, e, repo, save, leads, best, rec, source):
    """The search missed something (a lead `best` of the certificate or the structural ranking, LEAD_BAR ahead of the winner): re-tune
    the rotation on it, run the open search again seeded with the leads, redo the entry's race and values; `rec` gets `researched`."""
    w = FS.flat_of((e.get("again") or e["first"])["winner"]["allocation"])
    lead_flat = FS.flat_of(best["allocation"])
    log(f"== {cls} {entry}: the {source}'s lead {best['split']} is {best['gain']:+.1%} ahead: re-tuning the rotation on it and searching again")
    if tuned_near(cls, entry, lead_flat):   # audit 2026-10-06: a re-tune on a build the rotation was just tuned on finds nothing
        log(f"   rotation: already tuned on a build within 2 points of the lead; re-tune skipped")
    else:
        e["rotation_changed"] = FS.retune(cls, entry, lead_flat, quick=True) or e.get("rotation_changed")
    mine_all = FS.ours(cls)
    here = {bid: mine_all[bid] for bid in R.SPECS[cls][entry].get("builds", []) if bid in mine_all}
    starts = [FS.flat_of(ld["allocation"]) for ld in leads] + [w] + [R.alloc_of(b) for b in mine_all.values()] + FS.known_positives(cls)
    sp, rec2 = FS.run_search(cls, entry, repo, FS.AGAIN, starts, 73, protect=e["first"]["protected"], reuse=True)
    e["again"] = {"winner": rec2["winner"], "family": sp.classify(FS.flat_of(rec2["winner"]["allocation"])), "runs_agree": rec2["runs_agree"],
                  "important_features": rec2.get("important_features"), "simulated_builds": rec2["simulated_builds"], "from": source}
    w2 = FS.flat_of(rec2["winner"]["allocation"])
    e["race"] = FS.race(cls, entry, repo, w2, here)
    e["values"], e["values_base"] = FS.values(cls, entry, repo, w2)
    best_ours = max((k for k in e["race"] if k != "open winner"), key=lambda k: e["race"][k]["dps"], default=None)
    if best_ours:
        e["values_ours"], e["values_ours_base"] = FS.values(cls, entry, repo, R.alloc_of(mine_all[best_ours]))
        e["ours_best"] = best_ours
    e.update({"family": sp.classify(w2), "split": sp.split(w2), "dps": e["race"]["open winner"]["dps"], "link": RSH.tf_link(cls, w2),
              "gap_vs_ours": round(e["race"]["open winner"]["dps"] / e["race"][best_ours]["dps"] - 1, 4) if best_ours else None})
    rec["researched"] = {"winner": e["split"], "dps": e["dps"], "lead": best["split"], "source": source}
    e.pop("builds", None)   # open_builds.py writes the entry's build again from the new winner
    save()
    log(f"  {cls} {entry}: after the {source} the open winner is {e['split']} ({e['family']}) {e['dps']:.1f} DPS"
        + (f", {e['gap_vs_ours']:+.1%} vs our best there ({best_ours})" if e.get("gap_vs_ours") is not None else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--entry", action="append")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--no-search", action="store_true", help="measure and report only; no re-search on a lead")
    a = ap.parse_args()
    cls = a.cls
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    rp = FS.OUT / f"{cls}.json"
    if not rp.exists():
        raise SystemExit(f"no open-search record for {cls} ({rp})")
    st = json.load(open(rp, encoding="utf-8"))

    def save():
        rp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    for entry, e in st["entries"].items():
        if a.entry and entry not in a.entry:
            continue
        if not e.get("done"):
            log(f"== {cls} {entry}: not done, skipped")
            continue
        if e.get("synergy") and not a.fresh:
            log(f"== {cls} {entry}: certificate done ({e['synergy'].get('date')}; {len(e['synergy'].get('leads') or [])} leads)")
            continue
        certificate(cls, entry, e, repo, st, save, a)
    FS.write_class(cls, st)
    FS.write_page()
    log("== done")


if __name__ == "__main__":
    main()
