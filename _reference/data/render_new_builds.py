"""Write the new-builds survey: `_reference/new-builds-survey.md` and the "New spells and builds" section of every
`<class>/research/raid/README.md` (generated).

    python _reference/data/render_new_builds.py [classes...]

For each class: the spells the Forever beta spellbook marks new against Classic Era (`forever-spells/<class>.json`), what the
community simulator measured them doing in the raid races (damage share and casts per minute, `<class>/research/raid/raidsim/<spec>.json`)
and what the fight lab measured in leveling at level 60 (`<class>/research/leveling/fightlab/*.json`); then the builds searched around them
(`_reference/data/new-builds.json`, hand-kept: each target is a rotation-only entry of `raidsim/specs.json` with its own rotation,
its talents found by `raidsim/talent_opt.py`) with their training-dummy and raid DPS against the class's best raid build.
Numbers come from the last races (`raidsim/run.py --write`); nothing is simulated here. `rebuild.py --steps regen` runs it.
"""
import datetime
import fnmatch
import functools
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import paths  # noqa: E402
import readme_sections as rs  # noqa: E402
from data_build import BUILD as DATA_BUILD, CAPTURED as DATA_CAPTURED  # noqa: E402

CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
HEAD = "## New spells and builds"
PAGE = ROOT / "_reference/new-builds-survey.md"
NOTES = HERE / "new-builds.json"
CLOSE = 0.02   # "within 2%" of the class's best


@functools.lru_cache(maxsize=None)
def rr():
    spec = importlib.util.spec_from_file_location("render_rotations_mod", HERE / "render_rotations.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@functools.lru_cache(maxsize=None)
def notes():
    return json.load(open(NOTES, encoding="utf-8"))


def first_sentence(text, n=150):
    s = (text or "").replace("\n", " ").strip()
    cut = s.find(". ")
    s = s[: cut + 1] if cut > 0 else s
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def new_spells(cls):
    """([spell], [pet ability names]): the spells with a rank the beta spellbook marks new against Classic Era."""
    d = json.load(open(HERE / "forever-spells" / f"{cls}.json", encoding="utf-8"))
    out, pets = [], []
    for tab in d.get("tabs", []):
        for sp in tab.get("spells", []):
            ranks = [r for r in sp.get("ranks", []) if r.get("id")]
            if not any((r.get("classic") or {}).get("status") == "new" for r in ranks):
                continue
            if tab.get("name") == "Pets":
                pets.append(sp["name"])
                continue
            top = max(ranks, key=lambda r: r.get("level") or 0)
            out.append({"name": sp["name"], "tab": tab.get("name", ""), "level": top.get("level"), "cooldown": (top.get("cooldown") or "").replace(" cooldown", ""),
                        "text": first_sentence(top.get("text")), "ids": {int(r["id"]) for r in ranks}})
    return out, pets


# ------------------------------------------------------------------------------------------------ what the simulators measured
@functools.lru_cache(maxsize=None)
def data(cls):
    """{spec: render_rotations.spec_data} for every raid entry of the class that has a race."""
    out = {}
    for spec, _ in rr().raid_specs(cls):
        d = rr().spec_data(cls, spec)
        if d and d["rows"]:
            out[spec] = d
    return out


@functools.lru_cache(maxsize=None)
def race_rows(cls):
    """[(spec, race row, fight seconds)]: every build of the last races (no removal runs, no candidates)."""
    out = []
    for spec in data(cls):
        p = paths.raidsim_dir(cls) / f"{spec}.json"
        rep = json.load(open(p, encoding="utf-8"))
        dur = float(rep["sim"].get("duration") or 120.0)
        for x in rep["results"]:
            if x.get("removal") or x["label"].startswith("cand-") or not x.get("dps"):
                continue
            out.append((spec, x, dur))
    return out


def share_of(shares, name):
    return sum(v for k, v in (shares or {}).items() if k == name or k.startswith(name + " "))


def raid_use(cls, sp):
    """(damage share, casts a minute, spec, label) in the best raced build (training-dummy DPS) that casts the spell, or None."""
    best = None
    for spec, x, dur in race_rows(cls):
        casts = sum(v for k, v in (x.get("spell_casts") or {}).items() if int(k) in sp["ids"])
        share = share_of(x.get("shares"), sp["name"])
        if casts <= 0 and share <= 0:
            continue
        if best is None or x["dps"] > best[0]:
            best = (x["dps"], (share, casts / dur * 60, spec, x["label"]))
    return best[1] if best else None


@functools.lru_cache(maxsize=None)
def search_changes(cls):
    """[(spec, setting, change record)] of every kept change in the class's rotation searches (raidsim/apl_opt.py records)."""
    out = []
    for p in sorted(paths.raidsim_dir(cls).glob("*-rotation-search.json")):
        rec = json.load(open(p, encoding="utf-8"))
        rec = {rec.get("setting", "dummy"): rec} if "changes" in rec else rec
        for st, r in rec.items():
            for c in (r or {}).get("changes", []):
                out.append((p.name[: -len("-rotation-search.json")], st, c))
    return out


def search_use(cls, sp):
    """The rotation searches' kept changes that name the spell (inserted, moved, loosened), best gain first."""
    def names_it(change):   # the action a change acts on: after the last "cast " of each part of a two-edit change
        return any(part.rsplit("cast ", 1)[-1].startswith(sp["name"]) for part in change.split(" + ") if "cast " in part)
    hits = [(spec, st, c) for spec, st, c in search_changes(cls) if names_it(c["change"])]
    hits.sort(key=lambda x: -x[2].get("gain_seed2", 0))
    def gain(c):   # a rotation adopted whole (the open search's cross-race) records one seed only
        g = c.get("gain_seed2") if isinstance(c.get("gain_seed2"), (int, float)) else c.get("gain_seed1")
        return f"{g * 100:+.1f}%" if isinstance(g, (int, float)) else "gain not re-measured"
    return "; ".join(f"{spec} ({'training dummy' if st == 'dummy' else 'raid'}): {c['change'][:90]} ({gain(c)})" for spec, st, c in hits[:3]) or "-"


@functools.lru_cache(maxsize=None)
def fl_reports(cls):
    d = paths.fightlab_dir(cls)
    out = []
    for p in sorted(d.glob("*.json")) if d.exists() else []:
        if p.name.endswith("-calibration.json"):
            continue
        r = json.load(open(p, encoding="utf-8"))
        if isinstance(r, dict) and r.get("levels"):
            out.append((p.stem, r))
    return out


def leveling_use(cls, sp):
    """(damage share, casts a kill, report, build, level) at the highest level of the fight-lab report that gets most from it."""
    best = None
    for stem, r in fl_reports(cls):
        lv = r["levels"][max(r["levels"], key=int)]
        kills = lv.get("kills") or 1
        share = share_of(lv.get("shares"), sp["name"])
        casts = (lv.get("casts") or {}).get(sp["name"], 0) / kills
        if share <= 0 and casts <= 0:
            continue
        cand = (share, casts, stem, r.get("build"), lv.get("level"))
        if best is None or cand[:2] > best[:2]:
            best = cand
    return best


def tank(cls, spec):
    return bool(data(cls)[spec]["tank"])


def class_best(cls):
    """(spec, row) of the best raid DPS build on the training dummy (tanks left out), and of the best in a raid."""
    rows = [(spec, r) for spec, d in data(cls).items() if not d["tank"] for r in d["rows"] if r.get("dps")]
    if not rows:
        return None, None
    dummy = max(rows, key=lambda x: x[1]["dps"])
    raid = max(rows, key=lambda x: x[1].get("raid") or 0)
    return dummy, (raid if raid[1].get("raid") else None)


def search_record(cls, pattern):
    """The candidate files of a target's talent searches: [(file stem, search record)], best end first."""
    folder = paths.raidsim_dir(cls) / "candidates"
    out = []
    for p in sorted(folder.glob("*.json")) if folder.exists() else []:
        if fnmatch.fnmatch(p.name, pattern + ".json"):
            doc = json.load(open(p, encoding="utf-8"))
            if doc.get("search"):
                out.append((p.stem, doc["search"]))
    return sorted(out, key=lambda x: -(x[1].get("dps_end") or 0))


# ------------------------------------------------------------------------------------------------ text
def pct(x):
    return f"{x * 100:+.1f}%"


def use_text(share, count, unit):
    sh = "no damage of its own" if share <= 0 else ("under 1% of the damage" if share < 0.005 else f"{share * 100:.0f}% of the damage")
    return f"{sh}, {count:.1f} {unit}" if count >= 0.05 else f"{sh}, under 0.1 {unit}"


def verdict(cls, label, row, best, best_raid):
    if row is None:
        return None
    (bspec, b), rb = best, best_raid
    parts = []
    if b["label"] == label:
        parts.append("the class's best raid build on the training dummy")
    else:
        gap = row["dps"] / b["dps"] - 1
        parts.append(f"{pct(gap)} on the dummy" + (" (within 2%)" if -CLOSE <= gap < 0 else ""))
    if rb and row.get("raid"):
        if rb[1]["label"] == label:
            parts.append("the best in a raid")
        else:
            g = row["raid"] / rb[1]["raid"] - 1
            parts.append(f"{pct(g)} in a raid")
    return "; ".join(parts)


def target_label(t):
    """The race row a target is judged by: its build, else the build its entry races for it (the Retribution draft playing Seal of Fury),
    else the simulator preset it tuned."""
    return t.get("build") or t.get("race") or (f"sim preset: {t['preset']}" if t.get("preset") else None)


def leveling_text(cls, t):
    """A target's leveling check: its fight-lab report (the build playing the new spell) against the compared build."""
    lv = t.get("leveling")
    if not lv:
        return "-"
    p = paths.fightlab_dir(cls) / f"{lv['report']}.json"
    if not p.exists():
        return "not run yet"
    r = json.load(open(p, encoding="utf-8"))
    comp = next(iter((r.get("compare") or {}).items()), None)
    parts = []
    for L in sorted(r["levels"], key=int):
        if int(L) < lv.get("from", 0):
            continue
        mine = r["levels"][L]["time_per_kill"]
        if comp and L in comp[1]:
            other = comp[1][L]["time_per_kill"]
            parts.append(f"{L}: {mine:.1f} s a kill against {other:.1f} ({mine / other - 1:+.0%})")
        else:
            parts.append(f"{L}: {mine:.1f} s a kill")
    return f"{lv.get('what', '')} (fight lab `{lv['report']}`): " + "; ".join(parts)


def target_rows(cls, src):
    """Table lines for the class's targets (links relative to `src`)."""
    best, best_raid = class_best(cls)
    o = []
    for t in notes()["classes"].get(cls, {}).get("targets", []):
        d = data(cls).get(t["spec"])
        label = target_label(t)
        row = next((r for r in d["rows"] if r["label"] == label), None) if (d and label) else None
        srch = search_record(cls, t["candidates"]) if t.get("candidates") else []
        found = ""
        if srch:
            stem, s = srch[0]
            moves = s.get("moves") or []
            start = s.get("start") or "?"
            start = pathlib.Path(start).stem if start.endswith(".json") else start
            found = f"from `{start}`, {len(moves)} move{'s' if len(moves) != 1 else ''}"
        build = (rr().label_md(cls, label, src) + (f" ({t['race_note']})" if t.get("race_note") else "")) if label else "none"
        if row and best:
            v = verdict(cls, label, row, best, best_raid)
            if t.get("result"):
                v = f"{v}. {t['result']}"
            raid = f"{row['raid']:.0f}" if row.get("raid") else "-"
            o.append(f"| {t['idea']} | {build} | {row.get('split') or '-'} | {row['dps']:.0f} | {raid} | {v} | {found or '-'} | {leveling_text(cls, t)} |")
        else:
            o.append(f"| {t['idea']} | {build} | - | - | - | {t.get('result') or 'not raced yet'} | {found or '-'} | {leveling_text(cls, t)} |")
    return o


def spell_lines(cls, src):
    spells, pets = new_spells(cls)
    nts = notes()["classes"].get(cls, {}).get("notes", {})
    o = ["| Spell | Tree | Level | Cooldown | What it does (beta tooltip) | Raid: the best raced build casting it (training dummy) | Rotation search: kept changes naming it | Leveling at the fight lab's top level | Note |",
         "|---|---|---|---|---|---|---|---|---|"]
    for sp in spells:
        ru = raid_use(cls, sp)
        lu = leveling_use(cls, sp)
        raid = "not cast by any raced build"
        if ru:
            share, cpm, spec, label = ru
            raid = use_text(share, cpm, "casts/min") + f": {rr().label_md(cls, label, src)} ({spec})"
        lev = "not cast"
        if lu:
            share, casts, stem, bid, level = lu
            lev = use_text(share, casts, "casts a kill") + f": `{bid}` at {level} ({stem})"
        o.append(f"| {sp['name']} | {sp['tab']} | {sp['level'] or '-'} | {sp['cooldown'] or '-'} | {sp['text']} | {raid} | {search_use(cls, sp)} | {lev} | {nts.get(sp['name'], '')} |")
    if pets:
        o.append(f"| Pet family abilities ({len(pets)}) | Pets | - | - | {', '.join(pets)} | - | - | - | {nts.get('Pet family abilities', '')} |")
    return o


def class_part(cls, src, level=3):
    h = "#" * level
    best, best_raid = class_best(cls)
    o = [f"{h} New spells", ""] + spell_lines(cls, src) + [""]
    targets = notes()["classes"].get(cls, {}).get("targets", [])
    o += [f"{h} Builds searched around them", ""]
    if targets:
        o += ["| Idea | Build | Split | Dummy DPS | Raid DPS | Against the class's best | Talent search | Leveling |", "|---|---|---|---|---|---|---|---|"]
        o += target_rows(cls, src) + [""]
    else:
        o += ["No new spell of this class opened a build of its own: the new spells go into the existing builds' rotations (above).", ""]
    if best:
        (bspec, b) = best
        o.append(f"The class's best raid DPS build on the training dummy: {rr().label_md(cls, b['label'], src)} ({bspec}), {b['dps']:.0f} DPS"
                 + (f"; in a raid: {rr().label_md(cls, best_raid[1]['label'], src)} ({best_raid[0]}), {best_raid[1]['raid']:.0f} DPS." if best_raid else "."))
        o.append("")
    return o


INTRO = ("Every spell the Forever beta spellbook (build " + DATA_BUILD + ") marks new against Classic Era, what the community simulator "
         "(with this project's patches, `raidsim/patches/`; the ElliotWood/Forever fork for runs before 2026-10-18, the official wowsims/forever since: each report names its commit) and the fight lab measured it doing, and the builds "
         "searched around the new spells: each target has its own rotation (a rotation-only entry of `raidsim/specs.json`, tuned by "
         "`raidsim/apl_opt.py`, whose pool offers every new spell) and its talents found by `raidsim/talent_opt.py` (a local search over "
         "legal 51-point builds in the simulator, keeping every talent the rotation reads). Raid numbers are the last races: the boss-level "
         "training dummy with your own buffs and consumables, and the same build in a fully buffed raid. Models of the beta, not measurements.")


def write_page(classes):
    today = datetime.date.today().isoformat()
    o = ["# New spells and new builds (generated)", "",
         f"> Generated by `_reference/data/render_new_builds.py` on {today} from the beta spellbook, the raid races, the fight-lab "
         f"reports and the survey notes (`_reference/data/new-builds.json`, {notes()['date']}). Do not hand-edit.", "",
         INTRO, "", "## Builds searched", "",
         "| Class | Idea | Build | Dummy DPS | Raid DPS | Against the class's best |", "|---|---|---|---|---|---|"]
    for cls in classes:
        best, best_raid = class_best(cls)
        for t in notes()["classes"].get(cls, {}).get("targets", []):
            d = data(cls).get(t["spec"])
            label = target_label(t)
            row = next((r for r in d["rows"] if r["label"] == label), None) if (d and label) else None
            build = (rr().label_md(cls, label, PAGE) + (f" ({t['race_note']})" if t.get("race_note") else "")) if label else "none"
            if row and best:
                raid = f"{row['raid']:.0f}" if row.get("raid") else "-"
                v = verdict(cls, label, row, best, best_raid) + (f". {t['result']}" if t.get("result") else "")
                o.append(f"| {cls.title()} | {t['idea']} | {build} | {row['dps']:.0f} | {raid} | {v} |")
            else:
                o.append(f"| {cls.title()} | {t['idea']} | {build} | - | - | {t.get('result') or 'not raced yet'} |")
    o.append("")
    for cls in classes:
        o += [f"## {cls.title()}", ""] + class_part(cls, PAGE, level=3)
    PAGE.write_text("\n".join(o).rstrip("\n") + "\n", encoding="utf-8")
    print(f"wrote {PAGE.relative_to(ROOT)}")


def write_sections(classes):
    for cls in classes:
        readme = paths.scenario_readme(cls, "raid")
        o = [HEAD, "", f"The spells new in Forever, what the simulators measured them doing, and the builds searched around them "
                       f"([all classes]({paths.rel(readme, PAGE)}); generated by `_reference/data/render_new_builds.py` on "
                       f"{datetime.date.today().isoformat()}).", ""]
        o += class_part(cls, readme, level=3)
        rs.splice_ordered(readme, "raid", HEAD, "\n".join(o))
    print(f"wrote the {HEAD[3:]} section of {len(classes)} raid READMEs")


def main():
    classes = [c for c in sys.argv[1:] if c in CLASSES] or CLASSES
    write_page(CLASSES)
    write_sections(classes)


if __name__ == "__main__":
    main()
