"""The client's talent trees between two builds (2026-11-21, the audit session: "the talent data is on 1.60.1.70753 while the spell numbers
are on 70938 and the live client is 71037 ... diff the client's trait tables from 70753 through every build to 71037").

    python _reference/data/talent_client_diff.py --from 1.60.1.70753 --to 1.60.1.71037 [--steps] [--fetch] [--write]

Reads wago.tools' tables (product wowf; ~/.wow-forever-tools/wago/<Table>-<build>.csv, never the repository; --fetch downloads what is
missing): TraitTree, TraitNode, TraitNodeEntry, TraitDefinition, TraitEdge, TraitNodeXTraitNodeEntry, TraitCond (the talent trees and their
gates), SpellName, Spell (tooltips) and SpellEffect (numbers). A class's talents are the trait definitions whose spell names are talents
of forever-talents/<class>.json, in the trees where most of that class's names sit. Lists per class: talents added or removed, moved (row,
column), rank count changed, prerequisites changed, tier gates changed, and talents whose spell's tooltip or effects changed. --steps diffs
every pair of consecutive builds between the two (the builds wago.tools lists), so each change is dated. --write keeps the result in
_reference/data/talent-client-diff.json. Run it at every client update with the cost check (client_costs.py) and the live spell pull."""
import argparse
import csv
import json
import pathlib
import re
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
WAGO = pathlib.Path.home() / ".wow-forever-tools" / "wago"
OUT = HERE / "talent-client-diff.json"
CLASSES = ("druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior")
TABLES = ("TraitTree", "TraitNode", "TraitNodeEntry", "TraitDefinition", "TraitEdge", "TraitNodeXTraitNodeEntry", "TraitCond",
          "SpellName", "Spell", "SpellEffect")
EFFECT_FIELDS = ("Effect", "EffectAura", "EffectBasePointsF", "EffectAuraPeriod", "EffectBonusCoefficient", "BonusCoefficientFromAP",
                 "EffectTriggerSpell", "EffectMiscValue_0", "EffectSpellClassMask_0", "EffectSpellClassMask_1", "EffectSpellClassMask_2",
                 "EffectSpellClassMask_3", "EffectRealPointsPerLevel", "EffectChainTargets")


def vkey(v):
    return tuple(int(x) for x in re.findall(r"\d+", v))


def path(table, build):
    return WAGO / f"{table}-{build}.csv"


def fetch(table, build):
    req = urllib.request.Request(f"https://wago.tools/db2/{table}/csv?build={build}", headers={"User-Agent": "forever-tools"})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = r.read()
    if not data.startswith(b"ID,") and b",ID," not in data[:400]:
        raise SystemExit(f"wago.tools gave no {table} table for {build}: {data[:120]!r}")
    WAGO.mkdir(parents=True, exist_ok=True)
    path(table, build).write_bytes(data)


def rows(table, build, do_fetch):
    p = path(table, build)
    if not p.exists() or p.stat().st_size < 50:
        if not do_fetch:
            raise SystemExit(f"missing {p.name}: add --fetch")
        fetch(table, build)
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def talent_names():
    out = {}
    for cls in CLASSES:
        d = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
        out[cls] = {t["name"] for tr in d.get("trees", []) for t in tr.get("talents", [])}
    return out


def model(build, do_fetch):
    """{class: {talent name: {...}}} of one build, plus the spells' tooltips and effects by spell id."""
    names = {int(r["ID"]): r.get("Name_lang") or "" for r in rows("SpellName", build, do_fetch)}
    desc = {int(r["ID"]): (r.get("Description_lang") or "").strip() for r in rows("Spell", build, do_fetch)}
    eff = {}
    for r in rows("SpellEffect", build, do_fetch):
        eff.setdefault(int(r.get("SpellID") or 0), []).append(tuple(r.get(k, "") for k in ("EffectIndex",) + EFFECT_FIELDS))
    eff = {k: sorted(v) for k, v in eff.items()}
    defs = {int(r["ID"]): r for r in rows("TraitDefinition", build, do_fetch)}
    entries = {int(r["ID"]): r for r in rows("TraitNodeEntry", build, do_fetch)}
    node_entries = {}
    for r in rows("TraitNodeXTraitNodeEntry", build, do_fetch):
        node_entries.setdefault(int(r["TraitNodeID"]), []).append(int(r["TraitNodeEntryID"]))
    nodes = {int(r["ID"]): r for r in rows("TraitNode", build, do_fetch)}
    # prerequisites only: Type 2 (sufficient) and 3 (required); Type 0 is a drawn line (2026-11-21: Nature's Splendor -> Nature's Majesty
    # is a Type 0 line beside the Type 3 requirement the other way)
    edges = {(int(r["LeftTraitNodeID"]), int(r["RightTraitNodeID"])) for r in rows("TraitEdge", build, do_fetch) if r.get("Type") in ("2", "3")}
    conds = rows("TraitCond", build, do_fetch)
    tn = talent_names()
    # each node: its name (the definition's spell name, or the override name), its tree, position, ranks and spell
    per_node = {}
    for nid, n in nodes.items():
        for eid in node_entries.get(nid, []):
            e = entries.get(eid)
            d = defs.get(int(e["TraitDefinitionID"])) if e else None
            if not d:
                continue
            sid = int(d.get("SpellID") or 0) or int(d.get("VisibleSpellID") or 0)
            name = (d.get("OverrideName_lang") or "").strip() or names.get(sid, "")
            per_node[nid] = {"name": name, "tree": int(n["TraitTreeID"]), "x": int(float(n["PosX"])), "y": int(float(n["PosY"])),
                             "ranks": int(e["MaxRanks"]), "spell": sid, "def": int(d["ID"])}
    # the trees where most of a class's talent names sit
    out = {}
    for cls in CLASSES:
        count = {}
        for nid, v in per_node.items():
            if v["name"] in tn[cls]:
                count[v["tree"]] = count.get(v["tree"], 0) + 1
        trees = {t for t, c in count.items() if c >= 5}
        talents = {}
        for nid, v in per_node.items():
            if v["tree"] in trees and v["name"]:
                prereq = sorted(per_node.get(a, {}).get("name", str(a)) for a, b in edges if b == nid)
                talents[v["name"]] = dict(v, node=nid, prereq=prereq)
        gates = sorted((int(c["TraitTreeID"] or 0), int(c.get("TraitNodeGroupID") or 0), int(c.get("SpentAmountRequired") or 0),
                        int(c.get("CondType") or 0)) for c in conds if int(c.get("TraitTreeID") or 0) in trees)
        out[cls] = {"trees": sorted(trees), "talents": talents, "gates": gates}
    return out, desc, eff, names


def compare(a, b, step, do_fetch):
    (ma, da, ea, na), (mb, db, eb, nb) = model(a, do_fetch), model(b, do_fetch)
    res = {}
    for cls in CLASSES:
        ta, tb = ma[cls]["talents"], mb[cls]["talents"]
        rows_ = []
        for n in sorted(set(ta) - set(tb)):
            rows_.append(f"removed: {n}")
        for n in sorted(set(tb) - set(ta)):
            rows_.append(f"added: {n} (ranks {tb[n]['ranks']})")
        for n in sorted(set(ta) & set(tb)):
            x, y = ta[n], tb[n]
            if (x["x"], x["y"]) != (y["x"], y["y"]):
                rows_.append(f"{n}: moved ({x['x']}, {x['y']}) -> ({y['x']}, {y['y']})")
            if x["ranks"] != y["ranks"]:
                rows_.append(f"{n}: ranks {x['ranks']} -> {y['ranks']}")
            if x["prereq"] != y["prereq"]:
                rows_.append(f"{n}: prerequisite {x['prereq'] or 'none'} -> {y['prereq'] or 'none'}")
            if x["spell"] != y["spell"]:
                rows_.append(f"{n}: spell {x['spell']} -> {y['spell']}")
            # the talent's spells: every spell id with its name (the rank spells share it)
            ids = {s for s, nm in nb.items() if nm == n} | {y["spell"]}
            for s in sorted(ids):
                if da.get(s, "") != db.get(s, "") and s in db:
                    rows_.append(f"{n}: tooltip of {s} changed: \"{da.get(s, '')[:140]}\" -> \"{db.get(s, '')[:140]}\"")
                if ea.get(s) != eb.get(s) and s in eb:
                    rows_.append(f"{n}: effects of {s} changed")
        if ma[cls]["gates"] != mb[cls]["gates"]:
            rows_.append(f"tier gates changed: {len(ma[cls]['gates'])} -> {len(mb[cls]['gates'])} conditions")
        if rows_:
            res[cls] = rows_
    return res


def wago_builds():
    req = urllib.request.Request("https://wago.tools/api/builds", headers={"User-Agent": "forever-tools"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return sorted({x["version"] for x in json.load(r).get("wowf", [])}, key=vkey)


def words(s):
    """A tooltip's words without numbers, client placeholders ($s1, $/1000;S1) or colour codes, for a wording comparison."""
    s = re.sub(r"\|c[0-9a-fA-F]{8}|\|r", " ", s or "")
    s = re.sub(r"\$[^ ,.;)]*", " ", s)
    s = re.sub(r"[\d.,%]+", " ", s)
    return {w for w in re.findall(r"[a-z']+", s.lower()) if len(w) > 1 and w not in ("sec", "by", "and", "the", "of", "to", "your", "you", "an")}


def against_ours(build, do_fetch):
    """forever-talents/<class>.json against one client build's main tree per class: talents missing on either side (the client's nodes
    parked off the grid left out), rank counts, rows (the 600-unit grid from the tree's top), prerequisites (edges of Type 2 and 3), and
    the talents whose last rank's wording differs from the client's description (numbers and placeholders aside)."""
    import collections
    m, desc, eff, names = model(build, do_fetch)
    res = {}
    for cls in CLASSES:
        d = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
        ours = {t["name"]: t for tr in d["trees"] for t in tr["talents"]}
        byid = {t["id"]: t["name"] for t in ours.values()}
        mine = {n: v for n, v in m[cls]["talents"].items() if n in ours}
        if not mine:
            res[cls] = ["no talent of ours in the client's trees"]
            continue
        main = collections.Counter(v["tree"] for v in mine.values()).most_common(1)[0][0]
        tree = {n: v for n, v in m[cls]["talents"].items() if v["tree"] == main}
        y0 = min(v["y"] for n, v in tree.items() if n in ours)
        rows_ = []
        for n, t in ours.items():
            v = tree.get(n)
            if not v:
                rows_.append(f"{n}: not in the client's tree")
                continue
            r = round((v["y"] - y0) / 600)
            if t.get("maxRank") != v["ranks"]:
                rows_.append(f"{n}: ranks ours {t.get('maxRank')}, client {v['ranks']}")
            if t.get("row") != r:
                rows_.append(f"{n}: row ours {t.get('row')}, client {r}")
            op = byid.get((t.get("prereq") or {}).get("id")) if t.get("prereq") else None
            cp = v["prereq"][0] if v["prereq"] else None
            if op != cp:
                rows_.append(f"{n}: prerequisite ours {op}, client {cp}")
            a_, b_ = words((t.get("ranks") or [""])[-1]), words(desc.get(v["spell"], ""))
            if b_ and (b_ - a_ or len(a_ - b_) > 1):
                rows_.append(f"{n}: wording differs (client adds {sorted(b_ - a_)[:8]}, ours has {sorted(a_ - b_)[:8]})")
        for n, v in tree.items():
            if n not in ours and 0 <= round((v["y"] - y0) / 600) <= 6:
                rows_.append(f"{n}: in the client's tree (row {round((v['y'] - y0) / 600)}, {v['ranks']} ranks), not ours")
        if rows_:
            res[cls] = rows_
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="a")
    ap.add_argument("--to", dest="b")
    ap.add_argument("--ours", help="a client build: compare forever-talents with its trees instead of two builds")
    ap.add_argument("--steps", action="store_true")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    if a.ours:
        res = against_ours(a.ours, a.fetch)
        n = sum(len(v) for v in res.values())
        print(f"== forever-talents against {a.ours}: " + (f"{n} differences in {len(res)} classes" if res else "no talent row differs"))
        for cls, rs in res.items():
            for r in rs:
                print(f"  {cls}: {r}")
        if a.write:
            OUT.write_text(json.dumps({"ours_against": a.ours, "diffs": res}, indent=1) + "\n", encoding="utf-8")
            print(f"wrote {OUT.relative_to(HERE.parents[1])}")
        return 0
    if not (a.a and a.b):
        ap.error("--from and --to, or --ours")
    pairs = [(a.a, a.b)]
    if a.steps:
        bs = [v for v in wago_builds() if vkey(a.a) <= vkey(v) <= vkey(a.b)]
        pairs = list(zip(bs, bs[1:]))
    rec = {"from": a.a, "to": a.b, "steps": a.steps, "diffs": {}}
    for x, y in pairs:
        res = compare(x, y, a.steps, a.fetch)
        rec["diffs"][f"{x}..{y}"] = res
        print(f"== {x} -> {y}: " + (f"{sum(len(v) for v in res.values())} changes in {len(res)} classes" if res else "no talent row changed"))
        for cls, rs in res.items():
            for r in rs:
                print(f"  {cls}: {r}")
    if a.write:
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {OUT.relative_to(HERE.parents[1])}")


if __name__ == "__main__":
    sys.exit(main())
