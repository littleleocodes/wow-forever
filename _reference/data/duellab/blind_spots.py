"""The blind-spot check of the PvP search winners (2026-11-17; _reference/pvp-plan.md step 4).

User, 2026-11-16, after the Frost winner (20/0/31) had traded Ice Block for Arcane Concentration and Arcane Meditation: "make sure we
double check everything like that at the end". A duel scores one-against-one wins: time bought for help, escapes, several attackers
and battlegrounds count for nothing there, so a defensive, escape or control talent can read as worthless.

For each tree's winner (duellab/search/<class>-<tree slug>.json) it lists what the winner lacks that real PvP rates highly, each with
its evidence:
- `community`: the community's PvP builds of the tree (pvp-community-builds.json: talentsforever's PvP tags);
- `expansions`: the TBC and WotLK consensus of the tree (duellab/seeds/<class>-<tree>.json: taken by at least half of the builds);
- `stats model`: a talent whose PvP value is control, escape, defense, resistance, avoidance, movement, stealth, dispel or
  anti-healing, or that the class audits rated high (scorer/effects/forever/<class>.manual.json);
- `tooltip`: a talent no source above names whose text grants or improves a stun, root, slow, silence, fear, immunity, absorb,
  escape or a resistance to control;
- `signature`: a talent that grants one of the tree's required spells (signature_spells.json; that rule covers leveling and raid).
It races the winner with each one put back on the search's final-race duels (seed 3, 240 a matchup, the same dice): the talent at
its evidence's rank (the full rank for the stats model and the tooltip), its prerequisites, and up to 5 tier points its tree lacks
(each lower-row talent with room tried as the filler, the best kept); the points come from the winner's cheapest ranks by their
measured removal cost (seed 1, the screening duels; the rest of a talent's ranks at the mean of its remaining cost), every state
legal and 30+ points kept in the tree; since round 2 also by the floored costs (inert points first, every other at least 0.002 a
rank), the better of the payments kept. A put-back build that beats the winner by the search's bar (0.005 J) on seed 3 is raced again
on seed 4 (`confirmed`). Each row carries the casts and the control the foe took, the field means and per opponent for the talent's
own spell. Also listed: the abilities the winner holds that its duels never cast, and its points whose removal changes no duel
(bit-identical: the lab does not model them).

    python _reference/data/duellab/blind_spots.py [class[:tree] ...] [--workers 10] [--fresh]

Record: duellab/blind-spots.json, one entry per tree (resumes: a tree in the record is skipped unless --fresh). The verdicts are the
report's (_reference/pvp-results.md): the lab's verdict when the layer plays the talent and the race shows its cost, else a blind
spot, with the build that keeps it and its measured cost. A model of stated assumptions (duel.py), not a measurement.
"""
import argparse
import collections
import concurrent.futures as CF
import datetime
import json
import os
import pathlib
import re
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path.insert(0, str(HERE))
import duel_run as DR  # noqa: E402  (first: it sets the path)
import pvp_field as PF  # noqa: E402
import pvp_search as PS  # noqa: E402  (gear_rows, set_gear: a Holy-path paladin duels in its better gear, as in the search)

RECORD = HERE / "blind-spots.json"
SEARCH = HERE / "search"
MARGIN_W = 0.25          # pvp_search.MARGIN_W
BAR = 0.005              # pvp_search's replacement bar on J
RACE = (240, 3)          # the search's final race: n_confirm x 2 duels a matchup, seed + 2
CONFIRM = (240, 4)
COST = (40, 1)           # removal costs: the screening duels
MAX_GAP = 5
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
KINDS = {"stun", "kite", "stick", "escape", "defensive", "resist", "avoid", "move", "stealth", "dispel", "antiheal"}
TOOLTIP = re.compile(
    r"\b(stun\w*|root\w*|immobiliz\w*|snare\w*|slow(?:s|ed|ing)?|daze\w*|silence\w*|fear\w*|horror|incapacitat\w*|disorient\w*|"
    r"polymorph\w*|sleep|knock\w* back|interrupt\w*|disarm\w*|immune|immunity|absorb\w*|escape\w*|invisib\w*|stealth\w*|"
    r"duration of [^.]*?(?:stun|fear|snare|root|silence|movement|charm|polymorph|incapacitat)\w*|chance to resist|"
    r"movement speed|run speed|cheat death|spell reflect\w*|break free|movement impairing)", re.I)


def slug(s):
    return "".join(c for c in s.lower().replace(" ", "-") if c.isalnum() or c == "-")


# ---- duels


def matchup(args):
    """(label, opponent class, gear) -> (win, draw, margin, casts, damage, foe control taken): field-shaped duels with what the side
    did. The gear row is set first (pvp_search.set_gear; None: the module's own)."""
    label, cls, alloc, fcls, fref, n, seed = args[:7]
    gear = args[7] if len(args) > 7 else None
    PS.set_gear(cls, gear)
    a = DR.side(cls, alloc)
    b = DR.side(fcls, DR.load_build(fcls, fref)[1])
    wins = draws = 0
    margins = []
    casts, dmg, cc = collections.Counter(), collections.Counter(), collections.Counter()
    for i in range(n):
        r, d = DR.duel(a, b, seed * 100_003 + i, swap=bool(i % 2))
        me, foe = (d.b, d.a) if i % 2 else (d.a, d.b)
        wins += r == "A"
        draws += r == "draw"
        margins.append(max(0.0, me.p.hp) / me.p.hp_max - max(0.0, foe.p.hp) / foe.p.hp_max)
        casts.update(me.fight.casts)
        dmg.update(me.fight.damage)
        cc.update(foe.stats["cc_taken"])
    per = lambda c: {k: v / n for k, v in c.items()}  # noqa: E731
    return (label, fcls, gear), (wins / n, draws / n, statistics.mean(margins), per(casts), per(dmg), per(cc))


def evaluate(cands, n, seed, pool):
    """[(label, class, allocation)] -> {label: {"J", "win", "margin", "by", "casts", "casts_by", "dmg_share", "foe_cc"[, "gear"]}}.
    Each build duels in each of its gear rows (pvp_search.gear_rows: both for a Holy-path paladin with Holy Shock) and keeps the
    better, as the search scores it (2026-11-18: the round-2 check had run the Holy winner in caster gear only, 75.0% against the
    search's 79.4% in melee gear on the same duels)."""
    rows_of = {lb: PS.gear_rows(c, al) for lb, c, al in cands}
    jobs = [(lb, c, al, fc, fr, n, seed, g) for lb, c, al in cands for g in rows_of[lb] for fc, fr in PF.FIELD]
    res = dict(pool.map(matchup, jobs, chunksize=1))
    out = {}
    for lb, c, al in cands:
        for g in rows_of[lb]:
            row = one_row({fc: res[(lb, fc, g)] for fc, _ in PF.FIELD})
            if g:
                row["gear"] = g
            if lb not in out or row["J"] > out[lb]["J"]:
                out[lb] = row
    return out


def one_row(rows):
    """{opponent class: matchup result} -> the build's scores, casts, damage and control."""
    win = statistics.mean(v[0] for v in rows.values())
    mg = statistics.mean(v[2] for v in rows.values())
    casts, dmg, cc = collections.Counter(), collections.Counter(), collections.Counter()
    for v in rows.values():
        casts.update(v[3])
        dmg.update(v[4])
        cc.update(v[5])
    k = len(rows)
    tot = sum(dmg.values()) or 1.0
    return {"J": win + MARGIN_W * mg, "win": win, "margin": mg,
            "by": {fc: [round(v[0], 4), round(v[1], 4), round(v[2], 4)] for fc, v in rows.items()},
            "casts": {s: round(x / k, 2) for s, x in casts.most_common() if x / k >= 0.005},
            "casts_by": {fc: v[3] for fc, v in rows.items()},
            "dmg_share": {s: round(x / tot, 4) for s, x in dmg.most_common() if x / tot >= 0.001},
            "foe_cc": {s: round(x / k, 2) for s, x in cc.most_common() if x / k >= 0.005}}


# ---- the talent data


class Trees:
    def __init__(self, cls):
        import validate_builds as VB
        self.VB = VB
        self.trees = VB.load_forever()[cls]
        self.tree_of = {n: t for t, tr in self.trees.items() for n in tr["talents"]}
        self.info = {n: tr["talents"][n] for tr in self.trees.values() for n in tr["talents"]}

    def state(self, flat):
        out = {t: {} for t in self.trees}
        for n, r in flat.items():
            if r:
                out[self.tree_of[n]][n] = r
        return out

    def legal(self, flat):
        errs = []
        self.VB.check_state(self.trees, self.state(flat), "x", errs)
        return not errs

    def points(self, flat, tree):
        return sum(r for n, r in flat.items() if self.tree_of.get(n) == tree)


def community_builds(cls, T):
    src = json.load(open(DATA / "pvp-community-builds.json", encoding="utf-8"))
    out = []
    for b in src["builds"]:
        if b["class"] != cls:
            continue
        al = {n: r for n, r in DR.load_build(cls, f"community:{b['key']}")[1].items() if r}
        pts = collections.Counter()
        for n, r in al.items():
            pts[T.tree_of.get(n)] += r
        out.append((b["key"], pts.most_common(1)[0][0], al))
    return out


def pvp_values(cls):
    """{talent: (tier, kind)} for the talents the stats model gives a PvP effect (the class audits' notes: "PvP (date): tier, kind:")."""
    m = json.load(open(DATA / "scorer" / "effects" / "forever" / f"{cls}.manual.json", encoding="utf-8"))
    out = {}
    for name, ent in m.items():
        if name.startswith("_") or not isinstance(ent, dict):
            continue
        effs = [e for e in ent.get("effects", []) if "pvp" in (e.get("modes") or [])]
        if not effs:
            continue
        mt = re.search(r"PvP \([^)]*\):\s*([a-z-]+)(?:,\s*([a-z /-]+))?:", ent.get("note", ""))
        tier = mt.group(1) if mt else ""
        kinds = {k.strip() for k in (mt.group(2) or "").split("/")} if mt and mt.group(2) else set()
        kinds |= {e["kind"] for e in effs if e.get("kind")}
        out[name] = (tier, kinds)
    return out


def signature_talents(cls, tree, T):
    sig = json.load(open(DATA / "signature_spells.json", encoding="utf-8")).get(cls, {}).get(tree, {})
    return [s for s in PS.pvp_required(sig) if s in T.info]


def active_spells(cls):
    d = json.load(open(DATA / "forever-spells" / f"{cls}.json", encoding="utf-8"))
    out = set()
    for tab in d["tabs"]:
        for s in tab["spells"]:
            cast = (s["ranks"][-1].get("cast") or "").lower()
            if "passive" not in cast:
                out.add(s["name"])
    return out


def candidates(cls, tree, W, T):
    """{talent: {"rank": target, "sources": [...]}} of what the winner lacks (or holds below the evidence's rank)."""
    out = {}

    def add(n, rank, src):
        if n not in T.info:
            return
        rank = min(rank, T.info[n]["max"])
        if W.get(n, 0) >= rank:
            return
        e = out.setdefault(n, {"rank": 0, "sources": []})
        e["rank"] = max(e["rank"], rank)
        e["sources"].append(src)

    for key, lead, al in community_builds(cls, T):
        if lead == tree:
            for n, r in al.items():
                add(n, r, f"community {key} ({r})")
    seed = HERE / "seeds" / f"{cls}-{slug(tree)}.json"
    if seed.exists():
        s = json.load(open(seed, encoding="utf-8"))
        for c in s.get("consensus", []):
            add(c["talent"], c["rank"], f"expansions {c['builds']} of {s['expansion_builds']} ({c['rank']})")
    pv = pvp_values(cls)
    for n, (tier, kinds) in pv.items():
        hit = sorted(kinds & KINDS)
        if hit or tier == "high":
            add(n, T.info.get(n, {}).get("max", 0), "stats model: " + ", ".join(x for x in [tier] + hit if x))
    for n, inf in T.info.items():
        if n in out or (n in pv and (pv[n][1] & KINDS or pv[n][0] == "high")):
            continue
        words = sorted({m.group(1).lower() for m in TOOLTIP.finditer(" ".join(inf["ranks"]))})
        if words:
            add(n, inf["max"], "tooltip: " + ", ".join(words[:4]))
    for n in signature_talents(cls, tree, T):
        add(n, T.info[n]["max"], "signature (the leveling and raid rule)")
    return out


# ---- builds


def removal_costs(cls, W, pool):
    """{talent: [cost of its first rank, cost of all its ranks]} in J, unpaid (its points left unspent), on the screening duels."""
    cands = [("W", cls, W)]
    for t, r in W.items():
        one = dict(W)
        one[t] = r - 1
        cands.append((f"-1 {t}", cls, {k: v for k, v in one.items() if v}))
        if r > 1:
            cands.append((f"-all {t}", cls, {k: v for k, v in W.items() if k != t}))
    res = evaluate(cands, COST[0], COST[1], pool)
    base = res["W"]["J"]
    out, inert = {}, []
    for t, r in W.items():
        c1 = base - res[f"-1 {t}"]["J"]
        ca = base - res[f"-all {t}"]["J"] if r > 1 else c1
        out[t] = [round(c1, 4), round(ca, 4)]
        if res[f"-1 {t}" if r == 1 else f"-all {t}"]["by"] == res["W"]["by"]:
            inert.append(t)
    return out, inert


FLOOR = 0.002   # a measured removal cost under this (40 duels) counts as this much: only inert points are free (round 2)


def floored_costs(cost, inert, W):
    """The removal costs with the noise taken out (round 2, 2026-11-17: round 1 paid the Frost winner's Ice Block with Arcane
    Shielding, whose 40-duel cost read below zero; on 240 duels that point costs 1.2, 11 of them against the druid, while a Frostbite
    point costs 0.6): points that changed no duel pay first, every other at least FLOOR a rank. The check races both payments."""
    out = {}
    for t, (c1, ca) in cost.items():
        out[t] = [0.0, 0.0] if t in inert else [max(c1, FLOOR), max(ca, FLOOR * W.get(t, 1))]
    return out


def rank_cost(cost, W, t, cur):
    """The cost of taking one more rank from talent t, which holds `cur` of the winner's W[t] ranks now."""
    c1, ca = cost[t]
    if cur == W[t]:
        return c1
    return (ca - c1) / max(1, W[t] - 1)


def pay(T, W, al, fixed, cost, tree, beam=24):
    """The cheapest legal way to take the points `al` holds over the winner's total back from its other talents, one rank at a time
    (a beam of the `beam` cheapest partial states, so a greedy dead end, a removal that breaks the tier gating of what is left, is not
    fatal) -> (allocation, Counter of ranks taken) or None."""
    need = sum(al.values()) - sum(W.values())
    states = [(0.0, al, collections.Counter())]
    for _ in range(need):
        nxt, seen = [], set()
        for c0, st, taken in states:
            for m, r in st.items():
                if m in fixed or not r:
                    continue
                t2 = dict(st)
                t2[m] -= 1
                if not t2[m]:
                    del t2[m]
                key = tuple(sorted(t2.items()))
                if key in seen or T.points(t2, tree) < 30 or not T.legal(t2):
                    continue
                seen.add(key)
                c = c0 + (rank_cost(cost, W, m, r) if m in cost else 0.0)
                nxt.append((c, t2, taken + collections.Counter({m: 1})))
        if not nxt:
            return None
        states = sorted(nxt, key=lambda s: s[0])[:beam]
    c, st, taken = states[0]
    return st, taken


def put_back(T, W, n, rank, cost, tree, protect=(), prefer=()):
    """[(description, allocation)] of the winner with talent n at `rank` (one per filler option, at most 3: talents in `prefer`
    first), or ([], reason). Talents in `protect` (the tree's signature talents) never pay."""
    add = {n: rank - W.get(n, 0)}
    for p, rp in T.info[n].get("requires") or []:
        if W.get(p, 0) < rp:
            add[p] = rp - W.get(p, 0)
    tn = T.tree_of[n]
    row = T.info[n]["row"]
    trial = dict(W)
    for x, k in add.items():
        trial[x] = trial.get(x, 0) + k
    below = sum(r for x, r in trial.items() if T.tree_of.get(x) == tn and T.info[x]["row"] < row and x != n)
    gap = 5 * row - below
    if gap > MAX_GAP:
        return [], f"needs {gap} more points in {tn} below row {row + 1}"
    fillers = [None]
    if gap > 0:
        fillers = [f for f in T.trees[tn]["talents"] if T.info[f]["row"] < row and f not in add
                   and T.info[f]["max"] - trial.get(f, 0) >= gap] or []
        if not fillers:
            return [], f"needs {gap} tier points in {tn} and no lower-row talent has room"
        fillers = sorted(fillers, key=lambda f: (f not in prefer, -trial.get(f, 0), f))[:3]
    out, why = [], ""
    for f in fillers:
        al = dict(trial)
        if f:
            al[f] = al.get(f, 0) + gap
        fixed = set(add) | ({f} if f else set()) | set(protect)
        paid = pay(T, W, al, fixed, cost, tree)
        if paid is None or sum(paid[0].values()) != sum(W.values()) or not T.legal(paid[0]):
            why = "no legal way to pay its points with 30 kept in " + tree
            continue
        al, taken = paid
        desc = " + ".join(f"{k} {x}" for x, k in taken.most_common()) + " -> " + " + ".join(f"{k} {x}" for x, k in add.items())
        if f:
            desc += f" + {gap} {f} (tier points)"
        out.append((desc, al))
    return out, why


def ability_rows(cls, W, base, T):
    spells = active_spells(cls)
    rows = []
    for t in sorted(W):
        if t in spells:
            rows.append({"talent": t, "casts": base["casts"].get(t, 0.0),
                         "by": {fc: round(v.get(t, 0.0), 2) for fc, v in base["casts_by"].items()}})
    return rows


def run_tree(cls, tree, pool, log=print):
    rec = json.load(open(SEARCH / f"{cls}-{slug(tree)}.json", encoding="utf-8"))
    W = {k: v for k, v in rec["final"].items() if v}
    T = Trees(cls)
    cands = candidates(cls, tree, W, T)
    cost, inert = removal_costs(cls, W, pool)
    log(f"  {len(cands)} candidates; costs measured; inert points: {', '.join(inert) or 'none'}")
    builds, rows, out_of_reach = [("winner", cls, W)], [], []
    protect = signature_talents(cls, tree, T)
    floored = floored_costs(cost, inert, W)
    for n, c in sorted(cands.items()):
        prot = [p for p in protect if p != n]
        pb, why = put_back(T, W, n, c["rank"], cost, tree, protect=prot, prefer=set(cands))
        pb2, _ = put_back(T, W, n, c["rank"], floored, tree, protect=prot, prefer=set(cands))   # a second payment (round 2)
        seen = {tuple(sorted(al.items())) for _, al in pb}
        pb += [(d2, al) for d2, al in pb2 if tuple(sorted(al.items())) not in seen]
        if not pb:
            out_of_reach.append({"talent": n, "rank": c["rank"], "sources": c["sources"], "why": why})
            continue
        labels = []
        for i, (desc, al) in enumerate(pb):
            lb = f"{n}#{i}"
            builds.append((lb, cls, al))
            labels.append((lb, desc, al))
        rows.append({"talent": n, "rank": c["rank"], "held": W.get(n, 0), "sources": c["sources"], "options": labels})
    res = evaluate(builds, RACE[0], RACE[1], pool)
    base = res["winner"]
    keep = {}
    for r in rows:
        best = max(r.pop("options"), key=lambda o: res[o[0]]["J"])
        lb, desc, al = best
        x = res[lb]
        own = {fc: round(v.get(r["talent"], 0.0), 2) for fc, v in x["casts_by"].items()}
        r.update({"move": desc, "allocation": al, "J": round(x["J"], 4), "dJ": round(x["J"] - base["J"], 4),
                  "win": round(x["win"], 4), "dwin": round(x["win"] - base["win"], 4), "margin": round(x["margin"], 4),
                  "by": x["by"], "casts": x["casts"], "foe_cc": x["foe_cc"], "dmg_share": x["dmg_share"],
                  "own_casts": round(x["casts"].get(r["talent"], 0.0), 2), "own_casts_by": own,
                  "filler_options": len([1 for b in builds if b[0].startswith(r["talent"] + "#")])})
        if r["dJ"] > BAR:
            keep[lb] = (r, al)
    if keep:
        conf = evaluate([("winner", cls, W)] + [(lb, cls, al) for lb, (r, al) in keep.items()], CONFIRM[0], CONFIRM[1], pool)
        for lb, (r, al) in keep.items():
            g = conf[lb]["J"] - conf["winner"]["J"]
            r["confirm"] = {"seed": CONFIRM[1], "dJ": round(g, 4), "dwin": round(conf[lb]["win"] - conf["winner"]["win"], 4)}
            r["confirmed"] = g > BAR
    rows.sort(key=lambda r: -r["dJ"])
    entry = {"class": cls, "tree": tree, "date": datetime.date.today().isoformat(), "record_J": rec["J"], "record_win": rec["win"],
             "winner": W, "J": round(base["J"], 4), "win": round(base["win"], 4), "margin": round(base["margin"], 4), "by": base["by"],
             "casts": base["casts"], "dmg_share": base["dmg_share"], "foe_cc": base["foe_cc"], "gear": base.get("gear"),
             "abilities": ability_rows(cls, W, base, T), "inert": inert, "costs": cost, "rows": rows, "out_of_reach": out_of_reach,
             "settings": {"race": RACE, "confirm": CONFIRM, "cost": COST, "bar": BAR, "max_gap": MAX_GAP, "field": PF.FIELD}}
    return entry


def load_record():
    return json.load(open(RECORD, encoding="utf-8")) if RECORD.exists() else {"trees": {}}


def save_record(d):
    tmp = RECORD.with_name(RECORD.name + ".tmp")
    tmp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, RECORD)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("only", nargs="*", help="class or class:tree")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    ap.add_argument("--fresh", action="store_true")
    a = ap.parse_args()
    todo = []
    for f in sorted(SEARCH.glob("*.json")):
        r = json.load(open(f, encoding="utf-8"))
        key = f"{r['class']}:{r['tree']}"
        if a.only and not any(x == r["class"] or x == key for x in a.only):
            continue
        todo.append((r["class"], r["tree"]))
    d = load_record()
    for cls, tree in todo:
        key = f"{cls}:{tree}"
        if key in d["trees"] and not a.fresh:
            print(f"== {key}: in the record, skipped")
            continue
        t0 = datetime.datetime.now()
        print(f"== {t0:%H:%M} {key}", flush=True)
        for attempt in (1, 2):
            try:
                with CF.ProcessPoolExecutor(max_workers=a.workers) as pool:
                    e = run_tree(cls, tree, pool, log=lambda s: print(s, flush=True))
                break
            except CF.process.BrokenProcessPool:
                print(f"  a worker died (attempt {attempt})", flush=True)
                if attempt == 2:
                    raise
        d = load_record()
        d["trees"][key] = e
        save_record(d)
        mins = (datetime.datetime.now() - t0).total_seconds() / 60
        top = ", ".join(f"{r['talent']} {r['dJ']:+.3f}" for r in e["rows"][:4])
        print(f"  winner J {e['J']:.3f} (record {e['record_J']:.3f}), win {e['win']:.1%}; {len(e['rows'])} raced, "
              f"{len(e['out_of_reach'])} out of reach; best: {top}; {mins:.1f} min", flush=True)


if __name__ == "__main__":
    main()
