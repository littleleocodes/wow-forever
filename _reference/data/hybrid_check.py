"""Hybrid builds the open searches found but never wrote (2026-11-18, user: "how would we go about checking hybrid builds within
classes? Ones that don't need rules but may be better than others. For example a melee hunter build", then "Let's queue it").

    python -u _reference/data/hybrid_check.py [classes] (--raid | --leveling) [--top 2] [--fights N] [--jobs 8] [--smoke] [--write]

An open search writes a build from each raid entry's or leveling rotation's winner only, filed under the winner's spec, so a hybrid
that loses a shared entry by a hair keeps no build and no page: the hunter's 16/11/24 Summon Hawk + Lone Wolf hybrid scored 738.3 in
the melee entry's family polish of 2026-11-13 against the Survival winner's 737.3 in the final race, and there has been no Beast
Mastery/Survival raid page since 2026-10-25. The searches keep every polished family (a climb from each pair of keystones of two
trees) in their caches: raidsim/families/cache/<class>-<entry>.families.json and fightlab/open/cache/<class>-<rotation>.families.json.
For each hybrid that may play an entry's or rotation's rotation (raid: one of its trees in the entry's, raid_signature._entry_trees;
leveling: spec_modes.HYBRID_LEVELING_ROTATION), its best `--top` legal families by the cached score race:
- raid: in a full raid on the current simulator (default 30,000 fights, seed 1), the entry's raid rotation and gear, against the
  entry's best build of ours by its last environments run and the hybrid's own builds listed there, with the raid signature check
  on each family's damage shares (raidsim/raid_signature.py);
- leveling: at levels 20-60 in the fight lab (default 3,000 fights, seed 3, as the open search's race), each with the stats model's
  order (signature talents first), against the rotation's record winner and the hybrid's own page build, with the signature check
  (fightlab/fl_signature.qualifying).
The two parts run as separate processes (raidsim/ and fightlab/ each have a module named `run`). Record _reference/data/hybrid-check.json
(a run keeps the rows of the classes and parts it did not run), page _reference/hybrid-check.md (`--write`). It writes no build: a
hybrid's best becomes its page build in a later step.
"""
import argparse
import datetime
import functools
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent   # _reference/data
ROOT = HERE.parents[1]
OUT = HERE / "hybrid-check.json"
PAGE = ROOT / "_reference" / "hybrid-check.md"
TODAY = datetime.date.today().isoformat()
CLASSES = "druid hunter mage paladin priest rogue shaman warlock warrior".split()


@functools.lru_cache(maxsize=None)
def talent_trees(cls):
    """[(tree name, [talent names in the tree's order])] from the current Forever talent data."""
    d = json.loads((HERE / "forever-talents" / f"{cls}.json").read_text(encoding="utf-8"))
    return [(tr["name"], [t["name"] for t in tr["talents"]]) for tr in d["trees"]]


def by_tree(cls, flat):
    """{tree: [[talent, rank], ...]} (the builds file's allocation shape); None when the build names a talent the trees lack."""
    trees = talent_trees(cls)
    known = {n for _, ns in trees for n in ns}
    if any(n not in known for n in flat):
        return None
    return {t: [[n, flat[n]] for n in ns if flat.get(n)] for t, ns in trees}


def split_of(alloc):
    return "/".join(str(sum(r for _, r in v)) for v in alloc.values())


def legal(cls, flat):
    """A legal 51-point Forever build (validate_builds.check_state: ranks, tier gating, prerequisites)."""
    alloc = by_tree(cls, flat)
    if alloc is None or sum(flat.values()) != 51:
        return False
    errors = []
    vb = _vb(cls)
    VB_MOD.check_state(vb, {t: {n: r for n, r in v} for t, v in alloc.items() if v}, "x", errors)
    return not errors


@functools.lru_cache(maxsize=None)
def _vb(cls):
    sys.path[:0] = [str(HERE)]
    import validate_builds as VB
    global VB_MOD
    VB_MOD = VB
    return VB.load_forever()[cls]


def hybrid_trees(h):
    return set(h[len("Hybrid "):].split("/")) if h.startswith("Hybrid ") else {h}


def top_families(cache, classify, ok, top):
    """{hybrid: [{label, flat, score}]}: the best `top` distinct legal families of each hybrid `ok` accepts, by the cached score
    (`higher`: raid DPS, leveling kills per hour)."""
    out = {}
    for f in sorted(json.loads(cache.read_text(encoding="utf-8")), key=lambda x: -(x.get("score") or 0)):
        flat = {k: v for k, v in (f.get("build") or {}).items() if v}
        h = classify(flat)
        if not h or not h.startswith("Hybrid ") or not ok(h):
            continue
        lst = out.setdefault(h, [])
        if len(lst) < top and all(flat != x["flat"] for x in lst):
            lst.append({"label": f.get("label"), "flat": flat, "score": round(f.get("score") or 0, 2)})
    return {h: v for h, v in out.items() if v}


# ---------------------------------------------------------------------------------------------------------------------------------- raid
def raid_part(classes, a):
    sys.path[:0] = [str(HERE / "raidsim"), str(HERE)]
    import paths
    import spec_modes as SM
    import run as R
    import apl_opt as A
    import raid_signature as RS
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    fights = a.fights or (1500 if a.smoke else 30000)
    rows = []
    for cls in classes:
        names = R.spell_names(repo, cls)
        trees_sim = R.load_trees(repo, cls)
        builds = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
        for entry, e in R.SPECS.get(cls, {}).items():
            if not isinstance(e, dict) or "apl" not in e or e.get("tank"):
                continue
            cache = HERE / "raidsim" / "families" / "cache" / f"{cls}-{entry}.families.json"
            if not cache.exists():
                continue
            etrees = set(RS._entry_trees(cls, entry) or [])
            # one of the hybrid's trees in the entry's, or the entry built for the hybrid itself (frostfire-raid, shockadin-raid, smite-dps)
            fams = top_families(cache, lambda fl: RS.classify(cls, fl) if legal(cls, fl) else None,
                                lambda h: h in etrees or bool(hybrid_trees(h) & etrees), a.top)
            if not fams:
                continue
            listed = [b for b in e.get("builds", []) if b in builds]
            ref = best_listed(cls, entry, listed)
            ours = {h: [b for b in listed if SM.spec_of(cls, builds[b]) == h] for h in fams}
            blist = [{"label": f"ref|{ref}", "talents": R.talents_string(trees_sim, flat_of(builds[ref]))}] if ref else []
            for h, lst in fams.items():
                blist += [{"label": f"ours|{b}", "talents": R.talents_string(trees_sim, flat_of(builds[b]))} for b in ours[h] if b != ref]
                blist += [{"label": f"fam|{h}|{k}", "talents": R.talents_string(trees_sim, f["flat"])} for k, f in enumerate(lst)]
            print(f"== {cls} {entry} (trees {sorted(etrees)}): reference {ref}; " + "; ".join(
                f"{h}: {', '.join(x['label'] for x in lst)}" for h, lst in fams.items()), flush=True)
            if a.smoke:
                blist = blist[:3]
            res = A.bench(e, repo, blist, fights, 1, "raid", f"hybrid-{cls}-{entry}")
            rd = (res.get(f"ref|{ref}") or {}).get("dps") if ref else None
            for h, lst in fams.items():
                best_ours = max(((b, (res.get(f"ours|{b}") or {}).get("dps")) for b in ours[h] if (res.get(f"ours|{b}") or {}).get("dps")),
                                key=lambda x: x[1], default=(None, None))
                for k, f in enumerate(lst):
                    row = res.get(f"fam|{h}|{k}")
                    if not row or row.get("error") or not row.get("dps"):
                        continue
                    sig = RS.check(cls, h, row.get("actions"), names, held=f["flat"], mode="raid", trees=sorted(etrees)) or {}
                    alloc = by_tree(cls, f["flat"])
                    rows.append({"class": cls, "mode": "raid", "where": entry, "hybrid": h, "family": f["label"], "split": split_of(alloc),
                                 "allocation": alloc, "value": round(row["dps"], 1), "se": round(row.get("se") or 0, 2),
                                 "cached_score": f["score"], "ref": ref, "ref_value": round(rd, 1) if rd else None,
                                 "vs_ref": round(row["dps"] / rd - 1, 4) if rd else None, "ours": best_ours[0],
                                 "ours_value": round(best_ours[1], 1) if best_ours[1] else None,
                                 "vs_ours": round(row["dps"] / best_ours[1] - 1, 4) if best_ours[1] else None,
                                 "signature": {"ok": sig.get("ok", True), "core_share": sig.get("core_share"), "why": sig.get("why")},
                                 "fights": fights, "date": TODAY})
                    print(f"   {h:36s} {f['label']:40s} {split_of(alloc):9s} {row['dps']:7.1f}"
                          + (f"  vs {ref} {row['dps'] / rd - 1:+.2%}" if rd else "")
                          + ("" if sig.get("ok", True) else "  (fails its signature check)"), flush=True)
    return rows


def flat_of(b):
    return {n: r for items in b["allocation"].values() for n, r in items if r}


def best_listed(cls, entry, listed):
    """The entry's best build of ours in a full raid by its last environments run, else its first listed build."""
    sys.path[:0] = [str(HERE)]
    import paths
    p = paths.raidsim_dir(cls) / f"{entry}-environments.json"
    try:
        res = json.loads(p.read_text(encoding="utf-8"))["results"]
    except (OSError, ValueError, KeyError):
        return listed[0] if listed else None
    vals = {r.get("label"): (r.get("dps") or {}).get("raid") for r in res if isinstance(r.get("dps"), dict)}
    cand = [(b, vals[b]) for b in listed if vals.get(b)]
    return max(cand, key=lambda x: x[1])[0] if cand else (listed[0] if listed else None)


# ------------------------------------------------------------------------------------------------------------------------------ leveling
def leveling_part(classes, a):
    sys.path[:0] = [str(HERE / "fightlab"), str(HERE / "scorer"), str(HERE)]
    import multiprocessing
    import spec_modes as SM
    import fl_open_search as FO
    import fl_talent_opt as FT
    import fl_signature as FS
    import level_guides as LG
    fights = a.fights or (300 if a.smoke else 3000)
    rows = []
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        for cls in classes:
            rp = HERE / "fightlab" / "open" / f"{cls}.json"
            if not rp.exists():
                continue
            rec = json.loads(rp.read_text(encoding="utf-8"))
            rots = FO.rotations(cls)
            for rot, r in rec.get("rotations", {}).items():
                hybs = {h for (c, h), rr in SM.HYBRID_LEVELING_ROTATION.items() if c == cls and rr == rot}
                cache = HERE / "fightlab" / "open" / "cache" / f"{cls}-{rot}.families.json"
                if not r.get("done") or not hybs or not cache.exists() or rot not in rots:
                    continue
                model = rots[rot][0]
                fams = top_families(cache, lambda fl: FS.spec_for(cls, rot, fl) if legal(cls, fl) else None, lambda h: h in hybs, a.top)
                if not fams:
                    continue
                cands = [{"id": "winner", "allocation": r["winner"]["allocation"], "order": r["order"]}]
                pages = {}
                for h in fams:
                    b, order, _, prot = LG.pick(cls, h)
                    if b and order and prot == rot:
                        pages[h] = b["id"]
                        cands.append({"id": f"page|{h}", "allocation": b["allocation"], "order": order})
                for h, lst in fams.items():
                    for k, f in enumerate(lst):
                        alloc = by_tree(cls, f["flat"])
                        order = FS.sig_order(cls, rot, {"allocation": alloc, "order": FT.order_of(cls, model, f["flat"])})
                        cands.append({"id": f"fam|{h}|{k}", "allocation": alloc, "order": order, "_h": h, "_k": k})
                print(f"== {cls} {rot}: winner {r['winner'].get('split')}; pages {pages}; " + "; ".join(
                    f"{h}: {', '.join(x['label'] for x in lst)}" for h, lst in fams.items()), flush=True)
                if a.smoke:
                    cands = cands[:3]
                res = FT.race(pool, cls, rot, [{"allocation": c["allocation"], "order": c["order"]} for c in cands], fights, 3)
                qual = FS.qualifying(pool, cls, rot, [{"allocation": c["allocation"], "order": c["order"]} for c in cands])
                t = {c["id"]: (w, per, q) for c, (w, per), q in zip(cands, res, qual)}
                wt = t["winner"][0]
                for c in cands:
                    if not c["id"].startswith("fam|"):
                        continue
                    h, k = c["_h"], c["_k"]
                    f = fams[h][k]
                    w, per, (ok, sm) = t[c["id"]]
                    pw = t.get(f"page|{h}", (None,))[0]
                    rows.append({"class": cls, "mode": "leveling", "where": rot, "hybrid": h, "family": f["label"],
                                 "split": split_of(c["allocation"]), "allocation": c["allocation"], "order": c["order"],
                                 "value": round(w, 2), "levels": {str(L): round(v, 2) for L, v in per.items()},
                                 "cached_score": f["score"], "ref": "winner", "ref_split": r["winner"].get("split"),
                                 "ref_value": round(wt, 2), "vs_ref": round(w / wt - 1, 4),
                                 "ours": pages.get(h), "ours_value": round(pw, 2) if pw else None,
                                 "vs_ours": round(w / pw - 1, 4) if pw else None,
                                 "signature": {"ok": bool(ok), "verdict": (sm or {}).get("verdict")}, "fights": fights, "date": TODAY})
                    print(f"   {h:36s} {f['label']:40s} {split_of(c['allocation']):9s} {w:6.2f} s  vs winner {w / wt - 1:+.2%}"
                          + (f", vs {pages[h]} {w / pw - 1:+.2%}" if pw else ", no page build")
                          + ("" if ok else f"  (signature: {(sm or {}).get('verdict')})"), flush=True)
    return rows


# --------------------------------------------------------------------------------------------------------------------------------- write
def write(rows, classes, part):
    old = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    keep = [x for x in old.get("rows", []) if not (x.get("mode") == part and x.get("class") in classes)]
    rec = {"date": TODAY, "rows": keep + rows}
    OUT.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    o = ["# Hybrid builds the open searches did not write (generated)", "",
         f"> Generated by `_reference/data/hybrid_check.py` on {TODAY}. Do not hand-edit. Each row: one of the best polished families of a "
         "hybrid (a climb from a pair of keystones of two trees) in an open search's cache, raced again against the best build of ours "
         "where the search ran: raid in a full raid on the current simulator, leveling at levels 20-60 in the fight lab (seconds per kill, "
         "lower is faster). Simulator and fight-lab numbers are models of the game, not measurements.", ""]
    for mode, unit in (("raid", "DPS"), ("leveling", "s per kill")):
        rs = [x for x in rec["rows"] if x["mode"] == mode]
        if not rs:
            continue
        o += [f"## {mode.capitalize()}", "", f"| Class | {'Entry' if mode == 'raid' else 'Rotation'} | Hybrid | Family | Split | {unit} | "
              "Against the best of ours | Against the hybrid's own page build | Signature |", "|---|---|---|---|---|---|---|---|---|"]
        for x in sorted(rs, key=lambda x: (x["class"], x["where"], x["hybrid"], -x["value"] if mode == "raid" else x["value"])):
            better = (lambda g: -g) if mode == "leveling" else (lambda g: g)   # a positive number is better for the hybrid
            vr = f"{better(x['vs_ref']):+.2%} ({x['ref']})" if x.get("vs_ref") is not None else ""
            vo = f"{better(x['vs_ours']):+.2%} ({x['ours']})" if x.get("vs_ours") is not None else "no page build"
            sg = "passes" if x["signature"].get("ok") else "fails"
            o.append(f"| {x['class']} | {x['where']} | {x['hybrid']} | {x['family']} | {x['split']} | {x['value']} | {vr} | {vo} | {sg} |")
        o.append("")
    o.append("A positive percentage is better for the hybrid: more DPS in a raid, fewer seconds per kill while leveling.")
    PAGE.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT).as_posix()} and {PAGE.relative_to(ROOT).as_posix()}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--raid", action="store_true")
    g.add_argument("--leveling", action="store_true")
    ap.add_argument("--top", type=int, default=2, help="families per hybrid and entry or rotation")
    ap.add_argument("--fights", type=int, help="raid 30,000, leveling 3,000 (smoke: 1,500 and 300)")
    ap.add_argument("--jobs", type=int, default=8, help="fight-lab processes (leveling)")
    ap.add_argument("--smoke", action="store_true", help="few fights and builds, nothing written: a test")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    classes = a.classes or CLASSES
    rows = raid_part(classes, a) if a.raid else leveling_part(classes, a)
    if a.write and not a.smoke:
        write(rows, classes, "raid" if a.raid else "leveling")


if __name__ == "__main__":
    main()
