"""PvP player pages from the duel lab (2026-11-18; user, 2026-11-17, on the PvP report's recommendations: "Go with all your
recommendations": the duel lab's results on the research pages, PvP player pages after round 2, each with the duel build and the
battleground version, the latter labelled as judged by duels only).

    python _reference/data/duellab/render_pvp_pages.py [classes]      (render_modes.py calls write() at every regen)

Writes <class>/pvp/README.md (the class's specs ranked by the duels they win against the field) and <class>/pvp/<spec>.md (the duel
build, its battleground version, how it plays in the lab's duels, its matchups, the talents real PvP rates that it leaves out, the
limits), and gives render_modes.py the PvP column of the class page's grid, the class page's PvP ranking and the player index's column.
Every number comes from the records render_pvp_research.py reads: duellab/search/, duellab/blind-spots.json and the newest
duellab/results-*.json. No spec is marked recommended: the lab's AI against the lab's AI in an open field is a model of PvP, not PvP.
"""
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA), str(HERE)]
import render_pvp_research as RP  # noqa: E402
import render_start_here as RS  # noqa: E402
import spec_modes as SM  # noqa: E402

TODAY = datetime.date.today().isoformat()
MARK = "🔬"
TITLE = "PvP (duels)"
WHITE = {"Melee", "Melee (off-hand)", "Auto Shot", "Wand", "Shoot"}   # auto attacks: named once, not as presses
PET = {"hunter": {"Claw", "Bite", "Growl"}}   # the pet's own abilities in a hunter's casts (fightlab/hunter.py's pet decisions)
EVENTS = {"Shield block"}   # counters, not presses (fightlab/paladin.py on_block counts blocks there)
_cache = {}


def records():
    if not _cache:
        recs = {}
        for f in sorted((HERE / "search").glob("*.json")):
            r = RP.load(f)
            recs[f"{r['class']}:{r['tree']}"] = r
        _cache["recs"] = recs
        _cache["bs"] = (RP.load(HERE / "blind-spots.json", {"trees": {}}) or {}).get("trees", {})
        _cache["extra"] = RP.newest_results()
        src = RP.load(DATA / "pvp-community-builds.json", {"builds": []}) or {"builds": []}
        _cache["field"] = {b["class"]: b for b in src["builds"] if f"community:{b['key']}" in {r for _, r in field()}}
    return _cache["recs"], _cache["bs"], _cache["extra"], _cache["field"]


def field():
    """pvp_field.FIELD without importing the duel engine: [(class, community ref)]."""
    import ast
    src = (HERE / "pvp_field.py").read_text(encoding="utf-8")
    line = src[src.index("FIELD = "):]
    return ast.literal_eval(line[len("FIELD = "):line.index("]\n") + 1])


def rows(cls):
    """Each tree of the class with a duel-lab record: the duel build (the blind-spot check's improved build when it adopted one, else
    the search's winner, as render_pvp_research.py), its wins, matchups and battleground version; best first."""
    recs, bs, extra, _ = records()
    imp = {k: v for k, v in (extra.get("improved") or {}).items() if v.get("adopt")}
    bg = extra.get("battleground") or {}
    out = []
    for tree in SM.trees(cls):
        k = f"{cls}:{tree}"
        r = recs.get(k)
        if not r:
            continue
        e = bs.get(k) or {}
        im = imp.get(k)
        duel = im["allocation"] if im else {n: v for n, v in r["final"].items() if v}
        out.append({"tree": tree, "slug": SM.spec_slug(cls, tree), "name": SM.spec_name(cls, tree), "duel": duel,
                    "split": RP.split_of(cls, duel), "link": RS.tf_link(cls, duel),
                    "win": im["win3"] if im else (e.get("win") or r["win"]),
                    "by": (im or {}).get("by") or e.get("by") or r["by"], "improved": im, "search": r, "blind": e, "bg": bg.get(k)})
    return sorted(out, key=lambda x: -x["win"])


def pct(x):
    return f"{round(x * 100)}%"


def cell(cls, spec):
    """The class page grid's PvP cell for a tree, or '-'."""
    x = next((x for x in rows(cls) if x["tree"] == spec), None)
    if not x:
        return "-"
    return f"[{x['name']} — PvP](pvp/{x['slug']}.md) {MARK}<br>{pct(x['win'])} of duels"


def ranking(cls, prefix=""):
    """The class's specs ranked by duels won (class page "Which spec is best?" and the PvP index)."""
    rr = rows(cls)
    if not rr:
        return []
    o = ["Ranked by the share of duels the spec's best build wins against the field (nine opponents, one PvP build per class; "
         "level 60, one against one):", "", "| # | Spec and build | Wins vs the field | Easiest matchup | Hardest matchup |",
         "|---|---|---|---|---|"]
    for i, x in enumerate(rr, 1):
        by = sorted(x["by"].items(), key=lambda kv: -kv[1][0])
        o.append(f"| {i} | [{x['name']}]({prefix}{x['slug']}.md) {MARK} {x['split']} | {pct(x['win'])} | {by[0][0].capitalize()} "
                 f"{pct(by[0][1][0])} | {by[-1][0].capitalize()} {pct(by[-1][1][0])} |")
    return o + [""]


def best(cls, tie=0.03):
    """The player index's PvP cell: the class's best spec in duels and any within `tie` (3 points of win rate) of it."""
    rr = rows(cls)
    if not rr:
        return "-"
    top = rr[0]["win"]
    return ", ".join(f"[{x['name']}]({cls}/pvp/{x['slug']}.md) ({pct(x['win'])} of duels)" for x in rr if x["win"] >= top - tie)


def caveat(cls):
    """The class's limit of the duel lab, as of the newest records (render_pvp_research.CAVEAT, round 2's wording)."""
    return RP.caveat_text(cls, records()[0], records()[2])


def white_text(names):
    """The auto attacks a build keeps up, in words."""
    s = set(names)
    out = []
    if {"Melee", "Melee (off-hand)"} <= s:
        out.append("white swings with both weapons")
    elif "Melee" in s:
        out.append("white swings")
    if "Auto Shot" in s:
        out.append("Auto Shot")
    if s & {"Wand", "Shoot"}:
        out.append("the wand")
    return " and ".join(out)


def plays(cls, x):
    r, e = x["search"], x["blind"]
    allc = r.get("casts") or e.get("casts") or {}
    pet = PET.get(cls, set())
    casts = [(k, v) for k, v in allc.items() if k not in WHITE | pet | EVENTS and v >= 0.1]
    pets = [(k, v) for k, v in allc.items() if k in pet and v >= 0.1]
    white = [k for k, v in allc.items() if k in WHITE and v >= 1]
    o = ["## How it plays", "", "In the lab's duels (averages a duel, against the whole field):", ""]
    if casts:
        o.append("- **Presses:** " + ", ".join(f"{k} {v:.1f}" for k, v in casts[:10])
                 + (f"; between them, {white_text(white)}" if white else "") + ".")
    if pets:
        o.append("- **Your pet:** " + ", ".join(f"{k} {v:.1f}" for k, v in pets) + ".")
    dm = sorted((e.get("dmg_share") or {}).items(), key=lambda kv: -kv[1])[:5]
    if dm:
        o.append("- **Damage:** " + ", ".join(f"{k[:-6] + ' on the foe' + chr(39) + 's pet' if k.endswith(' (pet)') else k} {round(v * 100)}%"
                                              for k, v in dm) + ".")
    cc = sorted((e.get("foe_cc") or {}).items(), key=lambda kv: -kv[1])[:4]
    o.append("- **Control on the foe:** " + (", ".join(f"{k} {v:.1f} s" for k, v in cc) if cc else "none") + ".")
    sig = r.get("signature") or {}
    if sig:
        o.append(f"- **Signature:** {' and '.join(f'**{k}**' for k in sig)}, cast {' and '.join(f'{v:.1f}' for v in sig.values())} times a "
                 "duel: every PvP build here keeps its spec's signature talents and casts their spells.")
    if r.get("gear"):
        o.append(f"- **Gear:** {r['gear']} gear, the better of melee and caster gear in its duels.")
    if x["improved"]:
        o.append(f"- Measured on the search's winner; the duel build adds {', '.join(x['improved']['added'])} to it.")
    return o + [""]


def matchups(x):
    _, _, _, fb = records()
    o = ["## Matchups", "", "| Against | Their build | Wins | Health margin |", "|---|---|---|---|"]
    for c, _ in field():
        v = x["by"].get(c)
        if not v:
            continue
        b = fb.get(c) or {}
        their = f"[{b['split']}](https://{b['link']})" if b.get("link") else "-"
        o.append(f"| {c.capitalize()} | {their} | {pct(v[0])}{f' ({pct(v[1])} draws)' if v[1] >= 0.005 else ''} | {round(v[2] * 100):+d} |")
    return o + ["", "**Their build:** the class's most-tagged PvP build on talentsforever.com (the field). **Health margin:** your share of "
                "health left at the end minus theirs, in points, averaged over the duels (above 0: you end healthier).", ""]


def leaves_out(cls, x):
    e = x["blind"]
    if not e:
        return []
    rr = RP.rows_of(e, ((records()[2].get("repay") or {}).get(f"{cls}:{x['tree']}")))[:6]
    if not rr:
        return []
    o = ["## Talents real PvP rates that it leaves out", "",
         "What taking each would change in the duels (points of win rate, its points taken from the build's cheapest talents), and who "
         "rates it:", ""]
    o += [f"- **{t['talent']}** {t['held']} -> {t['rank']}: {RP.pts(t['dwin'])} ({RP.evidence(t)}); [that build]({RS.tf_link(cls, t['allocation'])})"
          for t in rr]
    return o + [""]


def page(cls, x, rank, n):
    o = [f"# {x['name']} {cls.capitalize()} — {TITLE}", "", f"[{cls.capitalize()}](../README.md) > [{TITLE}](README.md) > {x['name']}", "",
         f"**Duel build** {MARK} ({x['split']}) — [open the talent tree]({x['link']}). It wins {pct(x['win'])} of its duels against the "
         f"field, number {rank} of the {n} {cls} specs.", ""]
    b = x["bg"]
    if b:
        o += [f"**Battleground version** ({RP.split_of(cls, b['allocation'])}) — [open the talent tree]({RS.tf_link(cls, b['allocation'])}): "
              f"the duel build with {', '.join(f'**{t}**' for t in b['added'])} put back, talents for escapes, defense and control that "
              f"duels undervalue. It wins {abs(b['dwin']) * 100:.1f} points {'fewer' if b['dwin'] < 0 else 'more'} of its duels. Judged "
              "by duels only: no battleground is simulated yet.", ""]
    else:
        o += ["**Battleground version:** the same build (no talent duels undervalue fits within a point of its win rate).", ""]
    o += plays(cls, x) + matchups(x) + leaves_out(cls, x)
    lim = ["## Limits", "",
           "- The duel lab: level-60 one-against-one duels in an open field (no line of sight, no terrain), dungeon-blue gear, no "
           "consumables, racials or trinkets, 240 duels a matchup with both start orders; the lab's AI against the lab's AI. A model of "
           "stated assumptions, not a measurement."]
    cv = caveat(cls)
    if cv:
        lim.append(f"- {cv}")
    o += lim + ["", "More: [the research page](../research/pvp/README.md) (every tree's search, the blind-spot check, the never-cast "
                "talents) and [every matchup of the field](../../_reference/pvp-matchups.md)."]
    mac = (ROOT / cls / "macros.md").exists()
    if mac:
        o += ["", "**Macro ideas:** [every spec's macros](../macros.md), with the keys each one frees."]
    return o + ["", "---", foot(), ""]


def foot():
    ex = records()[2]
    return (f"*Generated by `_reference/data/duellab/render_pvp_pages.py` on {TODAY} from the duel lab's records (the newest: "
            f"{ex.get('date') or 'round 1'}). Do not hand-edit.*")


def write(cls):
    """<class>/pvp/: emptied, then the index and one page per tree with a record. Returns the pages written."""
    d = ROOT / cls / "pvp"
    rr = rows(cls)
    if d.exists():
        for old in d.glob("*.md"):
            old.unlink()
    if not rr:
        return []
    d.mkdir(parents=True, exist_ok=True)
    out = []
    for i, x in enumerate(rr, 1):
        p = d / f"{x['slug']}.md"
        p.write_text("\n".join(page(cls, x, i, len(rr))) + "\n", encoding="utf-8")
        out.append(p)
    idx = [f"# {cls.capitalize()} — {TITLE}", "", f"[{cls.capitalize()}](../README.md) > {TITLE}", "",
           "Each spec's best build in this project's duel lab. Every page has the duel build, a battleground version, how it plays, its "
           "matchups and what it leaves out.", ""]
    idx += ranking(cls)
    cv = caveat(cls)
    if cv:
        idx += [cv, ""]
    idx += [f"No spec is marked recommended: duels between the lab's AI in an open field are a model of PvP, not PvP, and battlegrounds "
            f"are not simulated. {MARK}: a build searched in the duel lab.", ""]
    if (ROOT / cls / "macros.md").exists():
        idx += ["**Macro ideas:** [every spec's macros](../macros.md), with the keys each one frees.", ""]
    idx += ["---", foot(), ""]
    (d / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    return out + [d / "README.md"]


def main():
    only = sys.argv[1:]
    for cls in RP.CLASSES:
        if only and cls not in only:
            continue
        ps = write(cls)
        print(f"{cls}: {len(ps)} PvP pages")


if __name__ == "__main__":
    main()
