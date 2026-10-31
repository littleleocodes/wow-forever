"""Refresh _reference/data/forever-talents/<class>.json from the WoW: Forever beta client datamines.

Three fan-site reads of the beta client are merged (each is archived under _reference/data/raw/<pull>/):

  1. warcraftforever.games/talents/<class>   (Next.js payload; beta client 1.60.1.69893, captured 2026-09-18)
     -> base records: talent ids, icons, Classic status/diff, Classic tooltips, removed-talent lists.
  2. talentsforever.com/data.json             (CC BY 4.0 export, generated 2026-09-24, beta client 1.60.1.70009)
     -> per-rank tooltip text at level 60 with no gear, rank caps, positions; also the class spellbooks
        (used by build_forever_spells.py).
  3. thewowdb.com/wow-forever/talents/<class> (Trait-table snapshot of build 1.60.1.70009 embedded in the page)
     -> positions, rank caps and prerequisite arrows straight from TraitNode/TraitEdge; used to cross-check 2.

Usage (from anywhere):
    python _reference/data/refresh_forever_talents.py --raw 2026-09-25-beta-70009            # merge an archived pull
    python _reference/data/refresh_forever_talents.py --fetch --raw <new-pull-name>           # download, archive, merge
    python _reference/data/refresh_forever_talents.py --raw <pull> --build 1.60.1.70009 --captured 2026-09-25 [class ...]

The merged JSON keeps the schema the renderers/validator/scorer read (id, row, col, name, icon, maxRank, ranks,
status, diff, classic, prereq, tree.removed) and adds provenance: build, captured, sources, tooltip_level, and per
class `removed_since_demo` / `renamed_since_demo`. Ranks whose text changed between the 69893 and 70009 reads keep the
older text in `ranks_prev` so the tuning can be audited. The diff against the file being replaced is written to
_reference/data/forever-talents/README.md.  Afterwards run render_trees.py, validate_builds.py, render_builds.py and
the scorer (effects.py <class>, then run.py ... --write --export).
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import ssl
import sys
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "forever-talents"
RAW = HERE / "raw"
CLASSES = ["warrior", "paladin", "hunter", "rogue", "priest", "shaman", "mage", "warlock", "druid"]
UA = {"User-Agent": "Mozilla/5.0 (wow-forever notes; talent data refresh)"}
URL_WF = "https://warcraftforever.games/talents/{cls}"
URL_TF = "https://talentsforever.com/data.json"
URL_WD = "https://thewowdb.com/wow-forever/talents/{cls}/"

# tree renames the beta client made against the demo transcription (old name -> client name)
TREE_RENAMES = {"Shadow Magic": "Shadow", "Elemental Combat": "Elemental"}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def norm_text(s):
    """Whitespace/rounding-insensitive tooltip comparison ('1.0 sec' == '1 sec')."""
    s = (s or "").replace("’", "'").replace("–", "-")
    s = re.sub(r"(\d)\.0\b", r"\1", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as e:  # expired certificate on warcraftforever.games (seen 2026-09-25): retry unverified
        if "CERTIFICATE" not in str(e).upper():
            raise
        ctx = ssl._create_unverified_context()
        with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
            return r.read().decode("utf-8", errors="replace")


def fetch_all(raw_dir):
    sys.path.insert(0, str(HERE))
    from extract_forever_talents import extract  # the Next.js payload reader
    (raw_dir / "warcraftforever-games").mkdir(parents=True, exist_ok=True)
    (raw_dir / "talentsforever-com").mkdir(parents=True, exist_ok=True)
    (raw_dir / "thewowdb-com").mkdir(parents=True, exist_ok=True)
    def get(site, url):   # 2026-10-16: thewowdb answered 503; a site that fails for a class falls back to an earlier pull (find_raw)
        try:
            return fetch(url)
        except Exception as e:
            print(f"{site}: {url} failed ({e}); the merge uses the newest earlier pull for it")
            return ""

    for cls in CLASSES:
        obj = extract(cls, get("warcraftforever", URL_WF.format(cls=cls)))
        if obj:
            (raw_dir / "warcraftforever-games" / f"{cls}.json").write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"warcraftforever {cls}: build {obj.get('build')} captured {obj.get('captured')}")
        html = get("thewowdb", URL_WD.format(cls=cls))
        m = re.search(r'(\{"schemaVersion":1,"snapshotId":"forever-beta-trait[^<]*)</script>', html)
        if m:
            snap = json.loads(m.group(1).strip())
            (raw_dir / "thewowdb-com" / f"{cls}.json").write_text(json.dumps(snap, indent=1, ensure_ascii=False), encoding="utf-8")
            print(f"thewowdb {cls}: build {snap.get('build')}")
    (raw_dir / "talentsforever-com" / "data.json").write_text(fetch(URL_TF), encoding="utf-8")
    print("talentsforever data.json saved")


def find_raw(raw_dir, sub_prefix, name):
    for d in raw_dir.iterdir():
        if d.is_dir() and d.name.startswith(sub_prefix):
            p = d / name
            if p.exists():
                return p
    # a site that did not answer for this class in this pull (2026-10-03: thewowdb had no paladin, mage or warlock page): the newest
    # earlier pull's read, said so in the output; merge_class falls back to the export where the trees disagree
    for older in sorted((d for d in raw_dir.parent.iterdir() if d.is_dir() and d.name < raw_dir.name), reverse=True):
        for d in older.iterdir():
            if d.is_dir() and d.name.startswith(sub_prefix) and (d / name).exists():
                print(f"  {name}: not in {raw_dir.name}; using {older.name}/{d.name}")
                return d / name
    raise SystemExit(f"{name} not found under {raw_dir}/{sub_prefix}*")


def tf_ranks(t):
    desc = t["desc"]
    if isinstance(desc, list):
        return list(desc)
    if all(str(i + 1) in desc for i in range(t["max"])):
        return [desc[str(i + 1)] for i in range(t["max"])]
    return None


URL_WH = "https://nether.wowhead.com/forever/tooltip/spell/{id}"


def wowhead_text(raw_dir, spell_id):
    """A spell's tooltip text from Wowhead's Forever database (cached under the pull's wowhead-com/), or ''."""
    d = raw_dir / "wowhead-com"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{spell_id}.json"
    if not p.exists():
        try:
            p.write_text(fetch(URL_WH.format(id=spell_id)), encoding="utf-8")
        except Exception as e:
            print(f"  wowhead {spell_id}: {e}")
            return ""
    try:
        html = json.loads(p.read_text(encoding="utf-8")).get("tooltip") or ""
    except ValueError:
        return ""
    qs = re.findall(r'<div class="q">(.*?)</div>', html, flags=re.S)
    txt = re.sub(r"<[^>]+>", "", qs[-1] if qs else "").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", txt).strip()


def scale_text(txt, k):
    """Rank k+1 of a rank-1 tooltip by scaling its numbers (an estimate: the client's own ranks are not always linear)."""
    def f(m):
        v = float(m.group(0)) * (k + 1)
        return f"{v:g}"
    return re.sub(r"\d+(?:\.\d+)?", f, txt)


def sim_sources(cls, tf, sim_dir, raw_dir):
    """The official simulator's trees (ui/sim/talents/trees/<class>.json, extracted from the live game files with the hotfix caches;
    2026-10-30: the live hotfixes of 27-30 Oct reworked the druid and mage trees, and the fan sites' reads stopped at 70532) as the
    tree structure: names, positions, rank caps and prerequisite arrows (at the required talent's full rank, as the client's arrows ask).
    Tooltip text comes from the talentsforever export by name where its rank count matches, else from Wowhead's Forever tooltip of the
    talent's spell (rank 1; higher ranks scaled from it and marked `estimated`). Returns (tf-shaped trees, wd-shaped snapshot,
    {(tree, talent): estimated rank indices}, notes)."""
    sim = json.load(open(sim_dir / f"{cls}.json", encoding="utf-8"))
    tf_trees = {TREE_RENAMES.get(tr["name"], tr["name"]): tr for tr in tf["trees"]}
    tf_out, wd_out, est, notes = [], [], {}, []
    for tr in sim:
        tname = TREE_RENAMES.get(tr["name"], tr["name"])
        # by name across the class's trees: a talent that changed trees keeps its text (70707: Furor to Feral Combat, Heart of the Wild
        # to Restoration)
        old = {t["name"]: t for x in tf_trees.values() for t in x["talents"]}
        old.update({t["name"]: t for t in (tf_trees.get(tname) or {}).get("talents", [])})
        at = {(t["location"]["rowIdx"], t["location"]["colIdx"]): t for t in tr["talents"]}
        tts, nodes = [], []
        for t in tr["talents"]:
            n, r, c, mx = t["fancyName"], t["location"]["rowIdx"], t["location"]["colIdx"], t["maxPoints"]
            pre = at.get((t["prereqLocation"]["rowIdx"], t["prereqLocation"]["colIdx"])) if t.get("prereqLocation") else None
            o = old.get(n)
            ranks = tf_ranks(o) if o else None
            if ranks and len(ranks) > mx:   # a lower rank cap: the export's first ranks (an estimate when the steps changed)
                ranks = ranks[:mx]
                est[(tname, n)] = []
                notes.append(f"{tname}/{n}: rank cap {len(tf_ranks(o))} -> {mx}; the export's first {mx} ranks kept")
            elif ranks and len(ranks) < mx:   # a higher cap: the export's ranks, then its rank-1 step (Arcane Resilience 25/50 -> 25/50/75)
                k0 = len(ranks)
                ranks = ranks + [scale_text(ranks[0], k) for k in range(k0, mx)]
                est[(tname, n)] = list(range(k0, mx))
                notes.append(f"{tname}/{n}: rank cap {k0} -> {mx}; ranks {k0 + 1}-{mx} extended from the export's rank-1 step (estimated)")
            if ranks is None or len(ranks) != mx:
                first = wowhead_text(raw_dir, t["spellId"]) or (ranks or [""])[0]
                ranks = [first] + [scale_text(first, k) for k in range(1, mx)]
                est[(tname, n)] = list(range(1, mx))
                notes.append(f"{tname}/{n}: tooltip from Wowhead's spell {t['spellId']} ({'new talent' if not o else 'rank cap ' + str(o['max']) + ' -> ' + str(mx)})"
                             + (f"; ranks 2-{mx} scaled from rank 1 (estimated)" if mx > 1 else ""))
            tts.append({"name": n, "row": r + 1, "col": c + 1, "max": mx, "desc": ranks, "icon": (o or {}).get("icon"),
                        **({"req": pre["fancyName"]} if pre else {})})
            nodes.append({"id": f"sim:{tname}:{n}", "name": n, "row": r, "col": c, "maxRanks": mx, "iconName": (o or {}).get("icon"),
                          "requires": [{"id": f"sim:{tname}:{pre['fancyName']}", "rank": pre["maxPoints"]}] if pre else []})
        tf_out.append({"name": tname, "talents": tts})
        wd_out.append({"name": tname, "nodes": nodes})
    return {"trees": tf_out}, {"trees": wd_out}, est, notes


def merge_class(cls, wf, tf, wd, build, captured, sources):
    wf_trees = {TREE_RENAMES.get(tr["name"], tr["name"]): tr for tr in wf["trees"]}
    tf_trees = {TREE_RENAMES.get(tr["name"], tr["name"]): tr for tr in tf["trees"]}
    wd_trees = {tr["name"]: tr for tr in wd["trees"]}
    assert set(wf_trees) == set(tf_trees) == set(wd_trees), (cls, set(wf_trees), set(tf_trees), set(wd_trees))
    node_name = {}
    for tr in wd["trees"]:
        for n in tr["nodes"]:
            node_name[n["id"]] = (tr["name"], n["name"])
    out_trees, removed_now, renamed_now, tooltip_changes, notes = [], [], [], [], []
    for tname in [tr["name"] for tr in wd["trees"]]:  # client tab order
        wtr, ttr, dtr = wf_trees[tname], tf_trees[tname], wd_trees[tname]
        tslug = slug(tname)
        wmap = {t["name"]: t for t in wtr["talents"]}
        tmap = {t["name"]: t for t in ttr["talents"]}
        dmap = {n["name"]: n for n in dtr["nodes"]}
        # 2026-10-16: also when a talent moved or changed its rank cap (thewowdb down, its 70291 read against the 70425 export: Mental Strength)
        moved = sorted(n for n, x in tmap.items() if n in dmap and (x["row"] - 1, x["col"] - 1, x["max"]) != (dmap[n]["row"], dmap[n]["col"], dmap[n]["maxRanks"]))
        if set(tmap) != set(dmap) or moved:
            # the Trait-edge snapshot lags (or leads) the export: 2026-10-03, the warrior's Fury tree after the hotfixes of 1-2 Oct, which
            # only the talentsforever export carries. The export's positions, rank caps and prerequisites (`req`, at the required talent's
            # full rank, as the client's arrows ask) stand in for this tree.
            notes.append(f"{tname}: the Trait-edge snapshot disagrees with the talentsforever export (only in the snapshot: "
                         f"{', '.join(sorted(set(dmap) - set(tmap))) or 'none'}; only in the export: {', '.join(sorted(set(tmap) - set(dmap))) or 'none'}; moved or re-capped: {', '.join(moved) or 'none'}); "
                         f"the export's positions, rank caps and prerequisites used for this tree")
            mx = {t["name"]: t["max"] for t in ttr["talents"]}
            dmap = {}
            for t in ttr["talents"]:
                node_name[f"tf:{tname}:{t['name']}"] = (tname, t["name"])
                dmap[t["name"]] = {"name": t["name"], "row": t["row"] - 1, "col": t["col"] - 1, "maxRanks": t["max"], "iconName": t.get("icon"),
                                   "requires": [{"id": f"tf:{tname}:{t['req']}", "rank": mx.get(t["req"], 1)}] if t.get("req") else []}
        # renames: a 70009 talent missing from 69893 whose grid cell held a 69893 talent missing from 70009
        wf_only = {n: t for n, t in wmap.items() if n not in tmap}
        tf_all_names = {t["name"] for x in tf_trees.values() for t in x["talents"]}
        wf_all = {t["name"]: t for x in wf_trees.values() for t in x["talents"]}
        for n, t in tmap.items():
            if n in wmap:
                continue
            if n in wf_all:   # 70707: a talent that changed trees (Furor, Heart of the Wild) is a move, not a rename
                wmap[n] = dict(wf_all[n])
                continue
            old = [on for on, ot in wf_only.items() if (ot["row"], ot["col"]) == (t["row"] - 1, t["col"] - 1)]
            if old:
                renamed_now.append({"tree": tname, "from": old[0], "to": n, "build": build})
                wmap[n] = dict(wf_only.pop(old[0]), _renamed_from=old[0])
        for n, t in wf_only.items():
            if n in tf_all_names:   # moved to another tree of the class
                continue
            removed_now.append({"tree": tname, "name": n, "build": build, "row": t["row"] + 1, "col": t["col"] + 1, "maxRank": t["maxRank"], "rank1": t["ranks"][0]})
        # rebuild id map for prerequisites after renames
        new_id = {n: f"{tslug}/{slug(n)}" for n in tmap}
        talents = []
        for t in sorted(ttr["talents"], key=lambda x: (x["row"], x["col"])):
            n = t["name"]
            w = wmap.get(n)
            d = dmap[n]
            row, col = t["row"] - 1, t["col"] - 1
            assert (row, col, t["max"]) == (d["row"], d["col"], d["maxRanks"]), (cls, n)
            ranks = tf_ranks(t)
            if ranks is None:
                notes.append(f"{tname}/{n}: 70009 export lacks full rank text; kept 69893 text")
                ranks = w["ranks"] if w else [t["desc"].get("1", "")]
            rec = {"id": new_id[n], "row": row, "col": col, "name": n, "icon": (w or {}).get("icon", d.get("iconName")),
                   "maxRank": t["max"], "ranks": ranks}
            if w:
                rec["status"] = w["status"]
                diff = list(w.get("diff", []))
                if w.get("classic"):
                    rec["classic"] = w["classic"]
                if w.get("evidence"):
                    rec["evidence"] = w["evidence"]
                if w.get("_renamed_from"):
                    diff.append(f"renamed from {w['_renamed_from']} in build {build}")
                if (w["row"], w["col"]) != (row, col):
                    diff.append(f"moved in build {build}: was row {w['row'] + 1}, col {w['col'] + 1}")
                if w["maxRank"] != t["max"]:
                    diff.append(f"max rank {w['maxRank']} -> {t['max']} in build {build}")
                changed = [i for i, (a, b) in enumerate(zip(w["ranks"], ranks)) if norm_text(a) != norm_text(b)] if len(w["ranks"]) == len(ranks) else list(range(len(ranks)))
                if changed:
                    diff.append(f"tooltip changed in build {build} (ranks {', '.join(str(i + 1) for i in changed)})")
                    rec["ranks_prev"] = w["ranks"]
                    rec["ranks_prev_build"] = wf.get("build", "1.60.1.69893")
                    tooltip_changes.append((tname, n, changed, w["ranks"], ranks))
                rec["diff"] = diff
            else:
                rec["status"] = "new"
                rec["diff"] = [f"added in build {build}"]
            # prerequisite: client trait edges (thewowdb) win; note disagreements
            req = d.get("requires") or []
            tf_req = t.get("req")
            wf_req = (w or {}).get("prereq", {}).get("id", "").split("/")[-1].replace("-", " ") if w else ""
            if req:
                r0 = req[0]
                ptree, pname = node_name[r0["id"]]
                rec["prereq"] = {"id": new_id.get(pname, f"{slug(ptree)}/{slug(pname)}"), "rank": r0.get("rank", 1)}
            elif tf_req and w and w.get("prereq") and slug(tf_req) == slug(wf_req):
                # two client reads (69893 payload and the 70009 export) carry an arrow the Trait-edge snapshot lacks: keep it
                rec["prereq"] = {"id": new_id.get(tf_req, f"{tslug}/{slug(tf_req)}"), "rank": w["prereq"].get("rank", 1)}
                notes.append(f"{tname}/{n}: Trait-edge snapshot has no prerequisite arrow, but the 69893 payload and the 70009 export both require {tf_req} rank {w['prereq'].get('rank', 1)} (kept)")
            if bool(tf_req) != bool(req) and not rec.get("prereq"):
                notes.append(f"{tname}/{n}: prerequisite disagreement - Trait edges: {node_name[req[0]['id']][1] if req else 'none'}; talentsforever export: {tf_req or 'none'} (Trait edges used)")
            elif req and tf_req and slug(tf_req) != slug(node_name[req[0]["id"]][1]):
                notes.append(f"{tname}/{n}: prerequisite disagreement - Trait edges: {node_name[req[0]['id']][1]}; talentsforever export: {tf_req} (Trait edges used)")
            if w and w.get("prereq"):
                old_p = w["prereq"]["id"].split("/")[-1]
                new_p = rec.get("prereq", {}).get("id", "").split("/")[-1]
                if old_p != new_p:
                    rec["diff"].append(f"prerequisite changed in build {build}: was {old_p.replace('-', ' ')}")
            talents.append(rec)
        out_trees.append({"id": tslug, "name": tname, "icon": wtr.get("icon"), "background": wtr.get("background"),
                          "talents": talents, "removed": wtr.get("removed", [])})
    # audit 2026-10-18 row 86: warcraftforever.games' removed-Classic-talent lists date from 70205; a talent the current tree has again
    # (Improved Fire Blast, Elemental Mastery, Grim Reach in 70425) is not removed, and render_trees printed it both ways
    present = {t["name"] for tr in out_trees for t in tr["talents"]}
    for tr in out_trees:
        tr["removed"] = [r for r in tr["removed"] if (r if isinstance(r, str) else r.get("name")) not in present]
    obj = {"slug": cls, "name": wf["name"], "build": build, "captured": captured, "tooltip_level": 60,
           "source": f"World of Warcraft: Forever beta client, build {build}: per-rank tooltips (level 60, no gear), rank caps and positions from talentsforever.com's data export (generated {sources['talentsforever']['generated']}, CC BY 4.0); positions and prerequisite arrows cross-checked against thewowdb.com's Trait-table snapshot of build {sources['thewowdb']['build']}; talent ids, Classic status/diff/tooltips and removed-Classic-talent lists from warcraftforever.games (beta client {wf.get('build')}, captured {wf.get('captured')}). Earlier snapshot: BlizzCon 2026 demo transcription captured 2026-09-13 (archived under raw/2026-09-13-demo).",
           "sources": sources, "removed_since_demo": removed_now, "renamed_since_demo": renamed_now, "merge_notes": notes,
           "trees": out_trees}
    return obj, tooltip_changes


def diff_against_previous(prev, new):
    """Summarise what changed against the file being replaced (the demo snapshot the first time)."""
    lines = []
    pt = {(TREE_RENAMES.get(tr["name"], tr["name"]), t["name"]): t for tr in prev["trees"] for t in tr["talents"]}
    nt = {(tr["name"], t["name"]): t for tr in new["trees"] for t in tr["talents"]}
    for k in sorted(set(pt) - set(nt)):
        lines.append(f"- removed: {k[0]} / {k[1]} (was row {pt[k]['row'] + 1}, {pt[k]['maxRank']} ranks)")
    for k in sorted(set(nt) - set(pt)):
        lines.append(f"- added: {k[0]} / {k[1]} (row {nt[k]['row'] + 1}, {nt[k]['maxRank']} ranks): {nt[k]['ranks'][0][:120]}")
    moved = rank_changed = text_changed = est_resolved = 0
    for k in sorted(set(pt) & set(nt)):
        a, b = pt[k], nt[k]
        if (a["row"], a["col"]) != (b["row"], b["col"]):
            moved += 1
            lines.append(f"- moved: {k[0]} / {k[1]} row {a['row'] + 1} col {a['col'] + 1} -> row {b['row'] + 1} col {b['col'] + 1}")
        if a["maxRank"] != b["maxRank"]:
            rank_changed += 1
            lines.append(f"- rank cap: {k[0]} / {k[1]} {a['maxRank']} -> {b['maxRank']}")
        real_prev = [i for i in range(len(a["ranks"])) if i not in a.get("estimated", [])]
        if any(i < len(b["ranks"]) and norm_text(a["ranks"][i]) != norm_text(b["ranks"][i]) for i in real_prev):
            text_changed += 1
        if a.get("estimated"):
            est_resolved += 1
    lines.insert(0, f"{len(set(pt) - set(nt))} removed, {len(set(nt) - set(pt))} added, {moved} moved, {rank_changed} rank-cap changes, "
                    f"{text_changed} talents whose previously real tooltip text changed, {est_resolved} talents whose extrapolated ranks are now real.")
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--raw", default="2026-09-25-beta-70009", help="pull folder under _reference/data/raw/")
    ap.add_argument("--fetch", action="store_true", help="download the three sources into the pull folder first")
    ap.add_argument("--build", default=None, help="client build the merged data represents (default: thewowdb snapshot's)")
    ap.add_argument("--captured", default=dt.date.today().isoformat())
    ap.add_argument("--previous", default=None, help="raw folder holding the snapshot to diff against (default: the file being replaced)")
    ap.add_argument("--sim-trees", default=None, help="the official simulator's ui/sim/talents/trees folder: its trees give the structure "
                    "(2026-10-30, live hotfixes the fan sites had not read yet); tooltips from the export, else Wowhead")
    a = ap.parse_args()
    raw_dir = RAW / a.raw
    if a.fetch:
        fetch_all(raw_dir)
    tf_all = json.load(open(find_raw(raw_dir, "talentsforever-com", "data.json"), encoding="utf-8"))
    report = [f"# Forever talent data: provenance and last refresh", "",
              f"> Generated by `_reference/data/refresh_forever_talents.py` on {a.captured} from `raw/{a.raw}/`. Do not hand-edit.", ""]
    for cls in [c for c in CLASSES if not a.classes or c in a.classes]:
        wf = json.load(open(find_raw(raw_dir, "warcraftforever-games", f"{cls}.json"), encoding="utf-8"))
        wd = json.load(open(find_raw(raw_dir, "thewowdb-com", f"{cls}.json"), encoding="utf-8"))
        tf = tf_all["talents"][cls.capitalize()]
        build = a.build or wd["build"]
        sources = {"talentsforever": {"url": URL_TF, "generated": tf_all.get("generated"), "build": build, "license": tf_all.get("license"), "attribution": tf_all.get("attribution")},
                   "thewowdb": {"url": URL_WD.format(cls=cls), "build": wd["build"], "evidence": [e.get("url") for e in wd.get("evidence", [])]},
                   "warcraftforever": {"url": URL_WF.format(cls=cls), "build": wf.get("build"), "captured": wf.get("captured")}}
        est, sim_notes = {}, []
        if a.sim_trees:
            tf, wd, est, sim_notes = sim_sources(cls, tf, pathlib.Path(a.sim_trees), raw_dir)
            sources["simulator_trees"] = {"path": "wowsims/forever ui/sim/talents/trees", "build": build,
                                          "note": "tree structure (positions, rank caps, prerequisites) from the simulator's live-client trees"}
        obj, tooltip_changes = merge_class(cls, wf, tf, wd, build, a.captured, sources)
        if a.sim_trees:
            obj["merge_notes"] = sim_notes + [x for x in obj["merge_notes"] if "Trait-edge snapshot disagrees" not in x]
            obj["source"] += (f" Tree structure (positions, rank caps, prerequisites) from the official wowsims/forever simulator's trees "
                              f"(extracted from the live client {build} with its hotfix caches); talents the export lacks take Wowhead's tooltip.")
            for tr in obj["trees"]:
                for t in tr["talents"]:
                    if (tr["name"], t["name"]) in est and est[(tr["name"], t["name"])]:
                        t["estimated"] = est[(tr["name"], t["name"])]
        import hotfix_text as HT   # live hotfix numbers the export has not read yet (2026-10-30)
        hf = HT.apply_talents(cls, obj)
        if hf:
            obj["merge_notes"].append(f"live hotfix numbers of {HT.DATE} written into {', '.join(hf)} (hotfix_text.py; sources {', '.join(HT.SOURCES)})")
        out = OUT / f"{cls}.json"
        prev_path = (RAW / a.previous / f"{cls}.json") if a.previous else out
        prev = json.load(open(prev_path, encoding="utf-8")) if prev_path.exists() else None
        out.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")
        n = sum(len(t["talents"]) for t in obj["trees"])
        print(f"{cls}: {n} talents, build {build}; removed now {[r['name'] for r in obj['removed_since_demo']]}, renamed {[(r['from'], r['to']) for r in obj['renamed_since_demo']]}, tooltip changes 69893->{build}: {len(tooltip_changes)}, notes: {len(obj['merge_notes'])}")
        report.append(f"## {cls.capitalize()}: {n} talents, build {build}")
        report.append("")
        report.append(f"Source: {obj['source']}")
        report.append("")
        if prev:
            report.append(f"Against the previous file ({prev.get('build', 'BlizzCon 2026 demo')}, captured {prev.get('captured')}):")
            report.append("")
            report += diff_against_previous(prev, obj)
            report.append("")
        if tooltip_changes:
            prev_builds = sorted({t.get("ranks_prev_build", "1.60.1.69893") for tr in obj["trees"] for t in tr["talents"] if t.get("ranks_prev")})
            report.append(f"Tooltips that changed between the {', '.join(prev_builds) or 'previous'} and {build} reads (older text kept in `ranks_prev`):")
            report.append("")
            for tname, name, changed, old, new in tooltip_changes:
                i = changed[-1]
                o = old[i][:150] if i < len(old) else f"(had {len(old)} ranks)"   # a rank cap that changed (70425)
                report.append(f"- {tname} / {name} (rank {i + 1}): {o} -> {new[i][:150]}")
            report.append("")
        if obj["merge_notes"]:
            report.append("Merge notes:")
            report.append("")
            report += [f"- {x}" for x in obj["merge_notes"]]
            report.append("")
    (OUT / "README.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"wrote {OUT / 'README.md'}")


if __name__ == "__main__":
    main()
