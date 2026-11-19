"""The duel lab's results on each class's PvP research page (2026-11-17; user, on the PvP report's recommendations: "Go with all your
recommendations": the results on the research pages now, PvP player pages after round 2).

    python _reference/data/duellab/render_pvp_research.py [classes]

Writes the "## Duel lab" section of <class>/research/pvp/README.md (readme_sections, the pvp order) from the records:
duellab/search/<class>-<tree>.json (the search), duellab/blind-spots.json (the blind-spot check: what each winner lacks that real
PvP rates highly, raced back in) and duellab/results-1117.json (the follow-ups: the improved builds, the battleground versions,
pets, Ice Block, Holy Shock, the matrices). Per tree: the duel build (the check's improved build where it found one, else the
search's winner), its battleground version (the talents duels undervalue put back one at a time while within a point of the duel
build), the win rate against each field build, how it plays, and what it lacks with the cost of keeping each. A model of stated
assumptions (duel.py), not a measurement.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA), str(HERE)]
import readme_sections as rs  # noqa: E402
import render_start_here as RS  # noqa: E402

FIELD = ["warrior", "rogue", "priest", "hunter", "warlock", "paladin", "shaman", "druid", "mage"]
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
RATED = ("community", "expansions", "signature", "stats model: high", "stats model: medium")
APPLIED = {"Arcane Power", "Presence of Mind", "Combustion", "Shadowform", "Inner Focus", "Trueshot Aura", "Rage of the Farseer",
           "Soul Link", "Amplify Curse"}
NEVER_NOTE = {"Sweeping Strikes": "the prerequisite of Mortal Strike", "Demonic Sacrifice": "the prerequisite of Soul Link",
              "Fel Domination": "a fast re-summon after the demon dies", "Bane of Havoc": "no use one against one",
              "Feral Charge": "a form ability the Balance play never uses", "Lacerate": "a Bear Form ability; the duels play Cat Form",
              "Seal of Command": "the Protection path plays other seals", "Vampiric Embrace": "the healing trees' play does not cast it"}
CAVEAT = {   # round 2 on (2026-11-17: pets answered, the Holy gear raced both ways, the signature rule)
    "hunter": "Pets since round 2 (2026-11-17): each class answers a pet the way players do (Polymorph, Scare Beast, Hibernate or "
              "Banish on it; a melee side the hunter keeps out of reach swings at the pet), but no class turns its attacks on the pet "
              "beyond white swings, so a pet that keeps the foe busy still counts for a lot (Bestial Wrath's 18 s of immunity covers "
              "most of the Beast Mastery hunter's duels). The hunter's numbers lean high.",
    "warlock": "Demons since round 2 (2026-11-17): each class answers a demon the way players do (control on it; a melee side kept "
               "out of reach swings at it), and the warlock summons a dead demon again through Fel Domination, but no class turns its "
               "attacks on the demon beyond white swings. The warlock's numbers lean high where the demon keeps the foe busy.",
    "mage": "Ice Block: {iceblock}. Keep it whatever the duels say: its value outside a duel is what one-against-one scoring cannot "
            "see.",
    "paladin": "Holy: since round 2 (2026-11-17) a Holy build with Holy Shock duels in the better of melee and caster gear, and every "
               "Holy build keeps Holy Shock (the PvP signature rule); the Holy duel build plays in {holy_gear} gear.",
}
CAVEAT_R1 = {   # round 1 (results-1117.json, which carries "pets" and "holy_gear")
    "hunter": "The engine never attacks, controls or dispels a pet on purpose, so the hunter's numbers are an upper bound: with the pet "
              "lost 15 s in, or from the start, the winners fall to {pets}. Round 2 makes pets targetable.",
    "warlock": "The engine never attacks, controls or dispels a demon on purpose, so the warlock's numbers are an upper bound: with the "
               "demon lost 15 s in, or from the start, the winners fall to {pets}. Round 2 makes pets targetable.",
    "mage": "Ice Block: every winner had dropped it, and with the cheapest point given for it, it costs the duels 0 to 0.6 points of "
            "win rate (Frost 0.6, Arcane 0.0, Fire +0.6). Keep it; its value outside a duel is what one-against-one scoring cannot see.",
    "paladin": "The Holy tree: the paladin module put a Holy build with Holy Shock into caster gear, and the duels kept that rule, so "
               "taking Holy Shock also swapped the gear and the Holy search ran against it. With the gear held to melee, Holy Shock "
               "costs {hs} points. The PvP signature rule (2026-11-17: hold the signature talents and cast them) and a search with the "
               "gear raced both ways come in round 2.",
}


def slug(s):
    return "".join(c for c in s.lower().replace(" ", "-") if c.isalnum() or c == "-")


def load(p, default=None):
    try:
        return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default


def split_of(cls, al):
    T = json.loads((DATA / "forever-talents" / f"{cls}.json").read_text(encoding="utf-8"))["trees"]
    return "/".join(str(sum(al.get(t["name"], 0) for t in tr["talents"])) for tr in T)


def pct(x, d=1):
    return f"{x * 100:.{d}f}%"


def pts(x):
    return f"{'+' if x >= 0 else ''}{x * 100:.1f}"


def rows_of(e, repay):
    """The rated rows (real PvP's evidence) of a tree, each with the cheaper of the two payments raced."""
    out = []
    for r in e["rows"]:
        x = (repay or {}).get(r["talent"])
        if x and x["dJ"] > r["dJ"]:
            r = dict(r, dwin=x["dwin"], allocation=x["allocation"], move=x["move"])
        if any(s.startswith(RATED) for s in r["sources"]) or any("stats model:" in s and any(k in s for k in (
                "escape", "defensive", "stun", "kite", "stick", "move", "resist", "stealth", "dispel", "antiheal", "avoid")) for s in r["sources"]):
            out.append(r)
    return sorted(out, key=lambda r: -r["dwin"])


def evidence(r):
    parts = []
    for s in r["sources"]:
        if s.startswith("community"):
            parts.append("the community's build")
        elif s.startswith("expansions"):
            parts.append(" ".join(s.split(" ")[1:4]) + " TBC/WotLK builds")
        elif s.startswith("stats model"):
            parts.append("class audit: " + s.split(":", 1)[1].strip())
        elif s.startswith("signature"):
            parts.append("signature spell")
    return "; ".join(parts)


def newest_results():
    """The newest follow-ups record: duellab/results-*.json by its "date" (round 1: results-1117.json; round 2 on: results-<date>.json),
    with its file name as "_file"."""
    best = None
    for f in HERE.glob("results-*.json"):
        d = load(f, {}) or {}
        if best is None or (d.get("date") or "") > (best.get("date") or ""):
            best = dict(d, _file=f.name)
    return best or {}


def and_list(xs):
    xs = list(xs)
    return ", ".join(xs[:-1]) + " and " + xs[-1] if len(xs) > 1 else (xs[0] if xs else "")


def duel_alloc(k, recs, extra):
    """The duel build of a tree (the blind-spot check's improved build when it adopted one, else the search's winner)."""
    im = (extra.get("improved") or {}).get(k)
    if im and im.get("adopt"):
        return im["allocation"]
    return {a: b for a, b in recs[k]["final"].items() if b}


def caveat_text(cls, recs, extra):
    """The class's limit of the duel lab for its pages ("" when it has none). Round 1's record (results-1117.json: "pets",
    "holy_gear") keeps round 1's wording and numbers; from round 2 on, the wording of CAVEAT, filled from the records."""
    keys = sorted(k for k in recs if k.startswith(cls + ":"))
    if "pets" in extra or "holy_gear" in extra:
        txt = CAVEAT_R1.get(cls, "")
        pets, holy = extra.get("pets") or {}, extra.get("holy_gear") or {}
        if "{pets}" in txt:
            got = []
            for k in keys:
                tree = k.split(":", 1)[1]
                a, z = pets.get(f"{cls}-{slug(tree)} 15.0"), pets.get(f"{cls}-{slug(tree)} 0.0")
                b = pets.get(f"{cls}-{slug(tree)} None")
                if a and z and b:
                    got.append(f"{tree} {pct(b['win'], 0)} -> {pct(a['win'], 0)} / {pct(z['win'], 0)}")
            txt = txt.format(pets="; ".join(got) or "much less")
        if "{hs}" in txt:
            w, s = holy.get("winner|melee"), holy.get("winner + Holy Shock|melee")
            txt = txt.format(hs=f"{abs(s['win'] - w['win']) * 100:.1f}" if w and s else "about 2.4")
        return txt
    txt = CAVEAT.get(cls, "")
    if "{iceblock}" in txt:
        held = [k.split(":", 1)[1] for k in keys if duel_alloc(k, recs, extra).get("Ice Block")]
        out = [k.split(":", 1)[1] for k in keys if k.split(":", 1)[1] not in held]
        back = [tr for tr in out if "Ice Block 1" in ((extra.get("battleground") or {}).get(f"{cls}:{tr}") or {}).get("added", [])]
        s = []
        if held:
            s.append(f"the {and_list(held)} duel build{'s hold' if len(held) > 1 else ' holds'} it")
        if out:
            s.append(f"the {and_list(out)} duel build{'s leave' if len(out) > 1 else ' leaves'} it out"
                     + (f" ({and_list(back)}'s battleground version takes it back)" if back else ""))
        txt = txt.format(iceblock="; ".join(s))
    if "{holy_gear}" in txt:
        txt = txt.format(holy_gear=(recs.get(f"{cls}:Holy") or {}).get("gear") or "melee")
    return txt


def section(cls, recs, bs, extra):
    imp = {k: v for k, v in (extra.get("improved") or {}).items() if v.get("adopt")}
    bg = extra.get("battleground") or {}
    repay = extra.get("repay") or {}
    o = ["## Duel lab", "",
         "> Generated by `_reference/data/duellab/render_pvp_research.py` from the duel lab's records (`duellab/search/`, "
         f"`duellab/blind-spots.json`, `duellab/{extra.get('_file') or 'results-1117.json'}`; {extra.get('date') or '2026-11-17'}). "
         "Level-60 one-against-one duels in an open field against "
         "a field of nine opponents, each class's most-tagged PvP build on talentsforever.com; dungeon-blue gear, no consumables or "
         "racials; 240 duels a matchup, both start orders. The lab's AI against the lab's AI: a model of stated assumptions, not a "
         "measurement. Plan and log: [`pvp-plan.md`](../../../_reference/pvp-plan.md); the field matrix: "
         "[`pvp-matchups.md`](../../../_reference/pvp-matchups.md).", ""]
    keys = sorted(k for k in recs if k.startswith(cls + ":"))
    txt = caveat_text(cls, recs, extra)
    if txt:
        o += [txt, ""]
    o += ["| Tree | Duel build | Wins vs field | Battleground version | The search's winner |", "|---|---|---|---|---|"]
    detail = []
    heat = ["| Duel build vs | " + " | ".join(c.title() for c in FIELD) + " |", "|---|" + "---|" * len(FIELD)]
    for k in keys:
        r = recs[k]
        tree = r["tree"]
        e = bs.get(k)
        im = imp.get(k)
        win_search = e["win"] if e else r["win"]
        W = {a: b for a, b in r["final"].items() if b}
        duel = im["allocation"] if im else W
        win = im["win3"] if im else win_search
        by = (im or {}).get("by") or (e or {}).get("by") or r["by"]
        kp = bg.get(k)
        bg_cell = (f"[{split_of(cls, kp['allocation'])}]({RS.tf_link(cls, kp['allocation'])}) {pts(kp['dwin'])}: "
                   + ", ".join(kp["added"])) if kp else "the same"
        search_cell = (f"[{split_of(cls, W)}]({RS.tf_link(cls, W)}) {pct(win_search)}" if im else "the duel build")
        o.append(f"| {tree} | [{split_of(cls, duel)}]({RS.tf_link(cls, duel)}) | {pct(win)} | {bg_cell} | {search_cell} |")
        heat.append(f"| {tree} | " + " | ".join(f"{round(by[c][0] * 100)}%" if c in by else "-" for c in FIELD) + " |")
        if not e:
            continue
        dm = sorted(e.get("dmg_share", {}).items(), key=lambda kv: -kv[1])[:4]
        cc = sorted(e.get("foe_cc", {}).items(), key=lambda kv: -kv[1])[:3]
        d = [f"### {tree}", "",
             f"How the search's winner plays: damage {', '.join(f'{a} {round(b * 100)}%' for a, b in dm)}; control on the foe "
             f"{', '.join(f'{a} {b:.1f} s' for a, b in cc) or 'none'} a duel."]
        if im:
            d.append(f"The blind-spot check improved it: {', '.join(im['added'])} put back wins {pct(im['win3'])} and {pct(im['win4'])} on two "
                     f"independent sets of duels ({pts(im['dwin3'])} and {pts(im['dwin4'])} points).")
        rr = rows_of(e, repay.get(k))
        if rr:
            d += ["", "What real PvP rates highly that the winner lacks, and the cost of keeping it (points of win rate; its points "
                  "taken from the winner's cheapest):", ""]
            d += [f"- **{x['talent']}** {x['held']} -> {x['rank']} ({evidence(x)}): {pts(x['dwin'])}; "
                  f"[build]({RS.tf_link(cls, x['allocation'])})" for x in rr[:10]]
        never = [f"{a['talent']} ({NEVER_NOTE[a['talent']]})" if a["talent"] in NEVER_NOTE else a["talent"]
                 for a in e.get("abilities", []) if a["casts"] < 0.01 and a["talent"] not in APPLIED]
        if never:
            d += ["", "Held but never cast in its duels: " + ", ".join(never) + "."]
        oor = [x for x in e.get("out_of_reach", []) if any(s.startswith(RATED) for s in x["sources"])]
        if oor:
            d += ["", "Out of reach in one step: " + "; ".join(f"{x['talent']} ({x['why']})" for x in oor) + "."]
        detail += d + [""]
    o += ["", "Battleground version: the duel build with the talents duels undervalue (escapes, defensive cooldowns, control, "
          "resistances) put back one at a time, each kept only while the whole stays within a point of the duel build (the number "
          "after the link). Judged by duels only: no battleground is simulated yet.", ""]
    o += ["Win rate of each duel build against the field (its row against each class's field build):", ""] + heat + [""]
    o += detail
    o += ["---", "*Generated section — do not edit by hand.*"]
    return "\n".join(o)


def main():
    only = sys.argv[1:]
    recs = {}
    for f in sorted((HERE / "search").glob("*.json")):
        r = load(f)
        recs[f"{r['class']}:{r['tree']}"] = r
    bs = (load(HERE / "blind-spots.json", {"trees": {}}) or {}).get("trees", {})
    extra = newest_results()
    for cls in CLASSES:
        if only and cls not in only:
            continue
        readme = ROOT / cls / "research" / "pvp" / "README.md"
        rs.splice_ordered(readme, "pvp", "## Duel lab", section(cls, recs, bs, extra))
        print(f"wrote {readme.relative_to(ROOT)} (Duel lab)")


if __name__ == "__main__":
    main()
