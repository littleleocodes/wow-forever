"""Give every ability a talent grants a fair chance in the rotation (2026-10-01, user request: "make sure the system is allowed to use all
spells and stuff that is possible, similar to how we found traps and Wing Clip and Venom").

    python _reference/data/raidsim/spell_probe.py <class> --spec "<spec>" --entry <entry> --build <id | candidate .json>
           [--setting dummy|raid] [--gear <gear.json>] [--write]

The rotation search (apl_opt.py) offers every combat spell of the spellbook, but it tunes on builds: an ability that only a talent grants
(Venom, Wrack, Sniper Shot, Lacerate, Strider Kick, Penance, Holy Shock...) is tried only when a tuning build holds the talent, and the
talent searches value the talent only when the rotation casts it. Neither ever sees it. This probe breaks the loop, per entry and
setting, for every talent ability the rotation does not cast:
1. builds: the spec's build if it holds the talent, else every legal one-move and prerequisite-chain neighbour that adds it (ml_talents
   Space: the spec's tree rule kept), screened with the ability cast just before the filler; the best three go on;
2. rotation lines: the plain cast, "only while its dot is not ticking" (spells over N sec), "only while its aura is not on the target /
   on you" (spells lasting N sec or min), "at 5 combo points" (finishers), each at the top, the middle, before the filler and at the end;
   when no neighbour holds the talent (it sits deeper in another tree), random legal builds of the spec that hold it;
3. every build x line x spot is simulated (seed 1, 3000 fights) against the same build not casting the ability; the best line is
   re-checked on a fresh seed (20,000 fights). A line that gains 0.2% or more for a build holding the talent is written into the
   entry's rotation for that setting (a new pass in its rotation-search record, so the pages list it): it fires only for builds that
   know the spell, and whether the talent is worth its points is left to the talent search, which can now see it. Every ability
   tried goes into `raidsim/ml/spell-probe.json` with its best result, so "never pays" is recorded too.
Abilities the simulator does not implement cannot be cast at all (see `_reference/sim-gaps.md`).
"""
import argparse
import copy
import datetime
import importlib.util
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
from filelock import locked  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MLT = _load("ml_talents", HERE / "ml_talents.py")
A = MLT.A
R = MLT.R
OUT = HERE / "ml" / "spell-probe.json"
TODAY = datetime.date.today().isoformat()
MIN_GAIN = 0.002


def talent_abilities(cls):
    """[(talent, spell name, top-rank id, tooltip)] for every active spell a talent of the class grants (same name in the spellbook)."""
    talents = {t["name"] for tr in json.load(open(ROOT / "_reference/data/forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"] for t in tr["talents"]}
    out = []
    for tab in json.load(open(ROOT / "_reference/data/forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
        if tab.get("name") == "Pets":
            continue
        for sp in tab.get("spells", []):
            name = sp.get("name", "")
            ranks = [r for r in sp.get("ranks", []) if r.get("id")]
            if name not in talents or not ranks or "Passive" in (ranks[-1].get("rank") or ""):
                continue
            text = " ".join(str(r.get("text", "")) for r in ranks)
            if not A.COMBAT_TEXT.search(text):
                continue
            top = max(ranks, key=lambda r: (r.get("level") or 0, len(r.get("rank") or "")))
            out.append((name, name, int(top["id"]), str(top.get("text", ""))))
    return out


def lines_for(sid, text):
    """The rotation lines to try for one ability."""
    cast = {"castSpell": {"spellId": {"spellId": sid}}}
    out = [("plain", {"action": dict(cast)})]
    if re.search(r"over \d+ sec", text):
        out.append(("dot not ticking", {"action": {"condition": {"not": {"val": {"dotIsActive": {"spellId": {"spellId": sid}}}}}, **cast}}))
    if re.search(r"for \d+ (sec|min)", text):
        for unit in ("CurrentTarget", "Self"):
            out.append((f"aura not on {'the target' if unit == 'CurrentTarget' else 'you'}",
                        {"action": {"condition": {"auraIsInactive": {"sourceUnit": {"type": unit}, "auraId": {"spellId": sid}}}, **cast}}))
    if "Finishing move" in text:
        five = {"cmp": {"op": "OpGe", "lhs": {"currentComboPoints": {}}, "rhs": {"const": {"val": "5"}}}}
        out.append(("at 5 combo points", {"action": {"condition": five, **cast}}))
        out.append(("at 5 combo points, aura not on you", {"action": {"condition": {"and": {"vals": [five, {"auraIsInactive": {"sourceUnit": {"type": "Self"}, "auraId": {"spellId": sid}}}]}}, **cast}}))
    return out


def spots(apl):
    vis = [i for i, it in enumerate(apl.get("priorityList") or []) if not it.get("hide")]
    if not vis:
        return [("top", 0)]
    return [("at the top", vis[0]), ("in the middle", vis[len(vis) // 2]), ("before the filler", vis[-1]), ("at the end", vis[-1] + 1)]


def with_line(apl, line, at):
    a = copy.deepcopy(apl)
    a["priorityList"].insert(at, copy.deepcopy(line))
    return a


def probe(cls, spec, entry, build, setting, gear_items, any_split=False, log=print):
    repo = R.repo_path(argparse.Namespace(repo=None))
    e = R.SPECS[cls][entry]
    base_apl = json.load(open(R.apl_path(e, repo, setting), encoding="utf-8"))
    cast_ids = {i for k, i in A.explicit_ids(base_apl) if k == "spellId"}
    space = MLT.Space(cls, spec, any_split=any_split)
    sim_trees = R.load_trees(repo, cls)
    tag = f"probe-{cls}-{entry}-{setting}"

    def run(pairs, its, seed):
        """[(alloc, apl)] -> dps list."""
        bl = [{"label": str(i), "talents": R.talents_string(sim_trees, al), "apl_json": ap, **({"gear_json": {"items": gear_items}} if gear_items else {})}
              for i, (al, ap) in enumerate(pairs)]
        out = []
        for i0 in range(0, len(bl), 300):
            rows = A.bench(e, repo, bl[i0:i0 + 300], its, seed, setting, tag)
            out += [float((rows.get(b["label"]) or {}).get("dps") or 0.0) for b in bl[i0:i0 + 300]]
        return out

    import random
    rng = random.Random(7)
    base_dps = run([(build, base_apl)], 3000, 1)[0]
    filler = spots(base_apl)[2][1]
    results = []
    for talent, name, sid, text in talent_abilities(cls):
        rank_ids = set()
        for tab in json.load(open(ROOT / "_reference/data/forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
            for sp in tab.get("spells", []):
                if sp.get("name") == name:
                    rank_ids |= {int(r["id"]) for r in sp.get("ranks", []) if r.get("id")}
        if rank_ids & cast_ids:
            continue   # the rotation casts it already
        how = "the spec's build"
        if build.get(talent):
            cands = [build]
        else:
            cands, how = [nb for _, nb in space.neighbours(build) if nb.get(talent)], "one move from the spec's build"
            if not cands:   # deeper in another tree: random legal builds of the spec that hold it
                sp2 = MLT.Space(cls, spec, protect={talent}, any_split=any_split, start_splits=[space.split(build)])
                cands = [b for b in (sp2.random_build(rng) for _ in range(40)) if b][:20]
                how = "random builds of the spec holding it"
        if not cands:
            results.append({"ability": name, "talent": talent, "kept": False, "result": "no legal build of the spec can hold it"})
            log(f"    {name}: no legal build of the spec can hold it")
            continue
        plain = lines_for(sid, text)[0][1]
        scr = run([(c, base_apl) for c in cands] + [(c, with_line(base_apl, plain, filler)) for c in cands], 3000, 1)
        n = len(cands)
        top = sorted(range(n), key=lambda i: -max(scr[i], scr[n + i]))[:3]
        trials = [(cands[i], ln, sp) for i in top for ln in lines_for(sid, text) for sp in spots(base_apl)]
        dps = run([(b, with_line(base_apl, ln[1], at)) for b, ln, (sname, at) in trials], 3000, 1)
        own = {MLT.key(cands[i]): scr[i] for i in top}   # each build without the line
        gains = [(dps[k] / own[MLT.key(trials[k][0])] - 1 if own[MLT.key(trials[k][0])] else -1.0, k) for k in range(len(trials))]
        g1, k = max(gains)
        b, ln, (sname, at) = trials[k]
        rec = {"ability": name, "talent": talent, "spell": sid, "builds": how, "builds_tried": len(cands), "lines_tried": len(trials),
               "best": {"line": ln[0], "spot": sname, "gain_seed1": round(g1, 4), "split": space.split(b),
                        "vs_spec_build": round(dps[k] / base_dps - 1, 4) if base_dps else None}}
        if g1 >= MIN_GAIN:
            c = run([(b, base_apl), (b, with_line(base_apl, ln[1], at))], 20000, 2)
            g2 = c[1] / c[0] - 1 if c[0] else 0.0
            rec["best"]["gain_seed2"] = round(g2, 4)
            rec["kept"] = g2 >= MIN_GAIN
            if rec["kept"]:
                rec["line"], rec["at"] = ln[1], at
        else:
            rec["kept"] = False
        log(f"    {name}: {'kept' if rec['kept'] else 'not kept'} ({how}; best {ln[0]} {sname}: {g1:+.2%} against the same build not casting it"
            + (f", {rec['best']['gain_seed2']:+.2%} on seed 2" if "gain_seed2" in rec["best"] else "") + ")")
        results.append(rec)
    return {"class": cls, "spec": spec, "entry": entry, "setting": setting, "date": TODAY, "base_dps": round(base_dps, 2), "abilities": results}, base_apl


def write(cls, entry, setting, res, base_apl):
    """Insert every kept line (best first; each one re-checked is not needed: lines fire only for builds that know the spell) into the
    entry's rotation for the setting, as a pass of its rotation-search record (apl_opt.write)."""
    kept = [r for r in res["abilities"] if r.get("kept")]
    if kept:
        repo = R.repo_path(argparse.Namespace(repo=None))
        N = A.RSP().Names(repo)
        cur = copy.deepcopy(base_apl)
        changes = []
        for k, r in enumerate(sorted(kept, key=lambda r: r["at"], reverse=True), start=1):
            item = dict(r["line"], notes=f"spell probe {TODAY}: {r['ability']} ({r['best']['gain_seed2']:+.1%} for a build holding {r['talent']})")
            cur["priorityList"].insert(r["at"], item)
            changes.append({"round": k, "change": f"spell probe: insert {r['best']['spot']}: {A.text(r['line'], N)}",
                            "gain_seed1": r["best"]["gain_seed1"], "gain_seed2": r["best"]["gain_seed2"], "candidates": r["lines_tried"]})
        e = R.SPECS[cls][entry]
        rec = {"class": cls, "spec": entry, "date": TODAY, "commit": R.git_commit(repo), "setting": setting, "tank": bool(e.get("tank")),
               "simulator_apl": e["apl"], "start": "spell probe", "builds": [], "iterations": 3000, "confirm": 20000, "changes": changes,
               "final": {setting: {}}}
        A.write(cls, entry, rec, base_apl, cur, N)   # takes the specs.json lock itself
    with locked(OUT.with_suffix(".lock")):
        old = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
        old[f"{cls}/{entry}/{setting}/{res['spec']}"] = res
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(old, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return len(kept)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--entry", required=True)
    ap.add_argument("--build", required=True)
    ap.add_argument("--setting", default="dummy", choices=["dummy", "raid"])
    ap.add_argument("--gear")
    ap.add_argument("--any-split", action="store_true")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", a.cls), encoding="utf-8"))["builds"]}
    build = R.alloc_of(json.load(open(a.build, encoding="utf-8"))) if a.build.endswith(".json") else R.alloc_of(data[a.build])
    gear = json.load(open(a.gear, encoding="utf-8"))["items"] if a.gear else None
    res, base = probe(a.cls, a.spec, a.entry, build, a.setting, gear, a.any_split)
    if a.write:
        print(f"  {write(a.cls, a.entry, a.setting, res, base)} line(s) written")


if __name__ == "__main__":
    main()
