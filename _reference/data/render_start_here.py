"""New-player pages (2026-09-29, user request: "files a new player would be able to follow easily").

    python _reference/data/render_start_here.py [classes...]

Writes `START-HERE.md` at the project root (what this is, how to read it, one line per class) and `<class>/START-HERE.md` for every
class: the recommendation in one minute, then leveling (talent order, what to press), raids (the best build per spec on the training
dummy and in a full raid, what to press), tanking and healing where the class has them, and PvP, each build with a talentsforever.com
link that opens its talent tree. Everything comes from the same data the research pages use (proposed-builds.json, the raid sim,
fight lab and healer lab reports), so the pages never go out of date; rebuild.py's regen step runs this. Do not hand-edit the output.
"""
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import paths  # noqa: E402
import render_rotations as rr  # noqa: E402
from data_build import BUILD as DATA_BUILD, CAPTURED as DATA_CAPTURED  # noqa: E402

CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
BUILD = DATA_BUILD
TODAY = datetime.date.today().isoformat()


# ------------------------------------------------------------------------------------------------ talent links
# The site's code version for the talent order our forever-talents/ data follows (its export at build 70425 since 2026-10-16). Until
# 2026-10-09 the links said '-4' (build 70009's order): the site read the digits in that order, so for the trees that changed since
# (druid Feral, warrior Fury and Protection, and renames in the mage and warlock trees) a link could open other talents than the page's
# build. Version 6 was the 70291 order; version 7 (2026-10-17) the 70425 trees (mage, priest, shaman and warlock moved). Checked on
# 2026-10-17: all 45 popular version-7 codes decode onto our 70425 data with the site's own per-tree points, no rank or tier error
# (popular_builds.CODE_VERSION).
TF_CODE_VERSION = "7"


def tf_link(cls, alloc):
    """talentsforever.com link for {talent: ranks}: one digit per talent in the tree's order (the site's order is our dataset's),
    trailing zeros dropped, the site's current code version at the end (TF_CODE_VERSION)."""
    data = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    parts = []
    for tr in data["trees"]:
        digits = "".join(str(min(int(alloc.get(t["name"], 0)), t["maxRank"])) for t in tr["talents"]).rstrip("0")
        parts.append(digits)
    return f"https://talentsforever.com/{cls}/60/" + "-".join(parts) + "-" + TF_CODE_VERSION


def flat(b):
    return {n: r for items in b["allocation"].values() for n, r in items if r}


def display_name(cls, b_or_name, alloc=None):
    """A build's name for a player: no "Optimizer —" prefix, no bracketed bookkeeping ("(fight-lab winner adopted ...)", "(raid-dps)"),
    cut at the first colon; a name that is still a damage breakdown (the optimizer's) becomes the lead tree's name."""
    import re
    name = b_or_name["name"] if isinstance(b_or_name, dict) else str(b_or_name)
    alloc = alloc if alloc is not None else (flat(b_or_name) if isinstance(b_or_name, dict) else {})
    n = re.sub(r"^Optimizer\s*[—-]\s*", "", name)
    while re.search(r"\([^()]*\)", n):
        n = re.sub(r"\s*\([^()]*\)", "", n)
    n = n.split(":")[0].strip(" —-")
    if not n or "%" in n or len(n) > 70:
        data = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
        pts = {tr["name"]: sum(alloc.get(t["name"], 0) for t in tr["talents"]) for tr in data["trees"]}
        n = max(pts, key=pts.get) if pts else name
    return n


def split_of(cls, alloc):
    data = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    return "/".join(str(sum(alloc.get(t["name"], 0) for t in tr["talents"])) for tr in data["trees"])


def page_link(cls, bid, src):
    p = paths.build_page_by_id("forever", cls, bid)
    return paths.rel(src, p) if p else None


def short(text, n=260):
    """First sentence(s) of a summary, cut at a sentence end near n characters."""
    t = " ".join(str(text or "").split())
    if len(t) <= n:
        return t
    cut = t.rfind(". ", 0, n)
    return t[: cut + 1] if cut > 80 else t[:n].rsplit(" ", 1)[0] + "..."


# ------------------------------------------------------------------------------------------------ data
def raid_rows(cls, setting="dummy"):
    """Every raid entry's rows (our builds and the simulator's presets) with the entry's lines, from the raid sim reports (setting "raid":
    the raid rotation's lines and the builds' casts in a full raid, render_rotations.spec_data)."""
    out = []
    for spec, entry in rr.raid_specs(cls):
        try:
            d = rr.spec_data(cls, spec, setting)
        except Exception:   # noqa: BLE001 - a missing report or rotation leaves the entry out
            d = None
        if not d:
            continue
        for i, r in enumerate(d["rows"]):
            out.append({"spec": spec, "d": d, "row": r, "tank": d["tank"]})
    return out


def healer_rows(cls):
    rows = []
    for f in sorted(paths.heallab_dir(cls).glob("*.json")) if paths.heallab_dir(cls).exists() else []:
        if f.name.endswith("-calibration.json"):
            continue
        rep = json.load(open(f, encoding="utf-8"))
        for bid, r in (rep.get("results") or {}).items():
            if bid in rr.builds(cls):
                rows.append({"id": bid, "capacity": r["capacity"], "hps": r["summary"].get("hps")})
    return sorted(rows, key=lambda r: -r["capacity"])


def leveling_pick(cls):
    """The recommended leveling build: the fight lab pipeline's hand draft (the race winner is adopted into it)."""
    import importlib
    sys.path.insert(0, str(HERE / "fightlab"))
    fl = rr.fl_module(cls)
    pipe = getattr(fl, "PIPELINE", {})
    return pipe.get("hand"), pipe.get("spec")


def fl_level_table(cls, spec):
    rep = rr._json(paths.fightlab_dir(cls) / f"{spec}.json")
    if not rep:
        return {}
    return {int(L): r for L, r in (rep.get("levels") or {}).items()}


# ------------------------------------------------------------------------------------------------ pages
def build_line(cls, b, src, extra=""):
    al = flat(b)
    page = page_link(cls, b["id"], src)
    name = f"[{display_name(cls, b)}]({page})" if page else display_name(cls, b)
    return f"{name} ({split_of(cls, al)}){extra} — [open the talent tree]({tf_link(cls, al)})"


def rotation_lines(d, row, limit=12):
    """The rotation lines a build actually casts, in priority order, as plain numbered steps."""
    o = []
    if d["pre"]:
        o.append("Before the pull: " + "; ".join(a for _, a in d["pre"]) + ".")
        o.append("")
    n = 0
    for ln, pl in zip(d["lines"], row["lines"]):
        if not pl["used"]:
            continue
        n += 1
        if n > limit:
            o.append(f"{n}. ... (the full list: the build's page)")
            break
        o.append(f"{n}. {ln['text'][0].upper() + ln['text'][1:]}")
    return o


def class_page(cls):
    src = ROOT / cls / "START-HERE.md"
    B = rr.builds(cls)
    intro = ""
    readme = (ROOT / cls / "README.md").read_text(encoding="utf-8").splitlines()
    for line in readme:
        if line.startswith("> "):
            intro += line[2:] + " "
        elif intro:
            break
    o = [f"# {cls.capitalize()}: start here", "",
         f"> For new players: what to play, which talents to take and what to press. Generated by `_reference/data/render_start_here.py` on {TODAY} "
         f"from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build {BUILD}; raid numbers: "
         f"{rr.sims_text(cls)}). The numbers are simulations, not "
         "measurements in the game; the class's other pages hold the evidence. Do not hand-edit.", ""]
    if intro:
        o += [intro.strip(), ""]

    # --- gather
    lvl_id, lvl_spec = leveling_pick(cls)
    rows = raid_rows(cls)
    dps = [x for x in rows if not x["tank"]]
    tanks = [x for x in rows if x["tank"]]

    def best(rs, key):
        rs = [x for x in rs if x["row"].get(key)]
        return max(rs, key=lambda x: x["row"][key]) if rs else None
    best_dummy = best(dps, "dps")
    best_raid = max((x for x in dps if x["row"].get("raid")), key=lambda x: x["row"]["raid"], default=None)
    heal = healer_rows(cls)
    pvp = [b for b in B.values() if b.get("content") == "pvp"]

    def name_of(x):
        lab = x["row"]["label"]
        if lab in B:
            return display_name(cls, B[lab]), lab
        return (lab.replace("sim preset: ", "") + " (the community simulator's build)"), lab

    def alloc_of(x):
        lab = x["row"]["label"]
        return flat(B[lab]) if lab in B else rr.decode(cls, x["row"].get("talents") or "")

    def row_line(x, what):
        n, lab = name_of(x)
        al = alloc_of(x)
        page = page_link(cls, lab, src) if lab in B else None
        nm = f"[{n}]({page})" if page else n
        return f"{nm} ({split_of(cls, al)}), {what} — [open the talent tree]({tf_link(cls, al)})"

    # --- one minute
    o += ["## In one minute", ""]
    if lvl_id in B:
        o.append(f"- **Leveling:** {build_line(cls, B[lvl_id], src)}")
    if best_dummy:
        o.append(f"- **Raid damage, training dummy** (your own buffs only): " + row_line(best_dummy, f"{best_dummy['row']['dps']:.0f} DPS"))
    if best_raid and (not best_dummy or best_raid["row"]["label"] != best_dummy["row"]["label"]):
        o.append(f"- **Raid damage, full raid** (every raid buff): " + row_line(best_raid, f"{best_raid['row']['raid']:.0f} DPS"))
    elif best_raid:
        o.append(f"- **Raid damage, full raid**: the same build, {best_raid['row']['raid']:.0f} DPS.")
    if tanks:
        t = max(tanks, key=lambda x: x["row"].get("value") or 0)
        o.append(f"- **Tanking:** " + row_line(t, "the best tank value in the simulator"))
    if heal:
        o.append(f"- **Healing:** {build_line(cls, B[heal[0]['id']], src)}")
    if pvp:
        p = sorted(pvp, key=lambda b: (b.get("tier") != "primary", b["id"]))[0]
        o.append(f"- **PvP:** {build_line(cls, p, src)}")
    o.append("")

    # --- leveling
    if lvl_id in B:
        b = B[lvl_id]
        o += ["## Leveling", "", f"**{display_name(cls, b)}**: the fastest build in this project's leveling simulator (time per kill, eating and drinking "
              "included, levels 20 to 60). [Why these talents](" + (page_link(cls, lvl_id, src) or "leveling/README.md") + ").", ""]
        if b.get("order"):
            o += ["Talent order (one point per level from 10):", "", "| Levels | Talent | Points |", "|---|---|---|"]
            o += [f"| {s['levels']} | {s['talent']} ({s['tree']}) | {s['points']} |" for s in b["order"]]
            o.append("")
        desc = rr.fl_description(cls, lvl_spec) if lvl_spec else ""
        if desc:
            o += ["What to press: " + " ".join(desc.split()), ""]
        lv = fl_level_table(cls, lvl_spec)
        if lv:
            o += ["How it goes (fight lab: same-level mobs, quest greens):", "", "| Level | Seconds per kill | Kills per hour |", "|---|---|---|"]
            o += [f"| {L} | {r['time_per_kill']:.0f} | {r['kills_per_hour']:.0f} |" for L, r in sorted(lv.items())]
            o.append("")

    # --- raids
    if dps:
        o += ["## Raid damage", "",
              "Ranked on a boss-level training dummy with only your own buffs (the fairest test of your own damage); the full-raid number, "
              "with every raid buff, is next to it. One line per spec: its best build.", "",
              "| Best build of each spec | Training dummy DPS | Full raid DPS | Talents |", "|---|---|---|---|"]
        by_spec = {}
        for x in dps:
            if x["spec"] not in by_spec or (x["row"]["dps"] or 0) > (by_spec[x["spec"]]["row"]["dps"] or 0):
                by_spec[x["spec"]] = x
        for spec, x in sorted(by_spec.items(), key=lambda kv: -(kv[1]["row"]["dps"] or 0)):
            n, lab = name_of(x)
            raid = x["row"].get("raid")
            o.append(f"| {n} ({split_of(cls, alloc_of(x))}) | {x['row']['dps']:.0f} | {f'{raid:.0f}' if raid else '-'} | "
                     f"[tree]({tf_link(cls, alloc_of(x))}) |")
        o.append("")
        if best_dummy:
            n, _ = name_of(best_dummy)
            o += [f"What to press with the top build, {n} (the first line that is ready is the one you cast):", ""]
            o += rotation_lines(best_dummy["d"], best_dummy["row"])
            o.append("")
    if tanks:
        t = max(tanks, key=lambda x: x["row"].get("value") or 0)
        n, _ = name_of(t)
        o += ["## Tanking", "", row_line(t, "ranked by threat and damage taken under a boss in the simulator"), "",
              "What to press:", ""] + rotation_lines(t["d"], t["row"]) + [""]
    if heal:
        o += ["## Healing", "", f"{build_line(cls, B[heal[0]['id']], src)}. Healers are not in the community simulator: this project's "
              "healer lab keeps a five-player group alive under raid damage and ranks builds by how much damage they can heal through.", ""]
    if pvp:
        o += ["## PvP", ""] + [f"- {build_line(cls, b, src)}: {short(b.get('summary'), 220)}" for b in sorted(pvp, key=lambda b: (b.get('tier') != 'primary', b['id']))] + [
              "", "PvP is not simulated: these builds rest on the talents' descriptions and the Classic community's PvP builds.", ""]
    o += ["## Good to know", "",
          "- Everything here is from the beta (level cap 20, later 30). Talents and numbers can still change before launch (2026-11-04).",
          "- Links open the build on talentsforever.com, a fan-made talent calculator with the beta's talent trees.",
          f"- More detail: the [class overview](README.md), the [leveling pages](leveling/README.md) and the [raid pages](raid/README.md).", ""]
    src.write_text("\n".join(o) + "\n", encoding="utf-8")
    return {"cls": cls, "lvl": B.get(lvl_id), "dummy": best_dummy, "raid": best_raid, "name_of": name_of, "tank": bool(tanks), "heal": bool(heal)}


def root_page(infos):
    o = ["# WoW: Forever class guides — start here", "",
         f"> Generated by `_reference/data/render_start_here.py` on {TODAY}. Do not hand-edit.", "",
         "This project works out the best talents and the best way to play every class in **World of Warcraft: Forever** (the Classic+ "
         "release, launching 2026-11-04), from the beta's own talent trees and simulations: a community combat simulator for raids and "
         "this project's own simulators for leveling and healing. Pick your class below: each page tells you what to level with, what to "
         "raid with and what to press, with a link that opens every build in a talent calculator.", "",
         "| Class | Leveling | Best raid damage (training dummy) | Guide |", "|---|---|---|---|"]
    for i in infos:
        cls = i["cls"]
        lvl = display_name(cls, i["lvl"]) if i["lvl"] else "-"
        dm = f"{i['name_of'](i['dummy'])[0]}, {i['dummy']['row']['dps']:.0f} DPS" if i["dummy"] else "-"
        o.append(f"| {cls.capitalize()} | {lvl} | {dm} | [{cls}/START-HERE.md]({cls}/START-HERE.md) |")
    o += ["", "## How to read the numbers", "",
          "- **Training dummy DPS**: your own damage against a raid boss with only the buffs you bring yourself. It ranks builds fairly.",
          "- **Full raid DPS**: the same with every raid buff and debuff; higher, and it favors builds that run out of mana alone.",
          "- **Seconds per kill** (leveling): a whole kill cycle against same-level mobs, including eating and drinking.",
          "- All numbers are simulations of the beta, not in-game measurements. Treat differences under 2-3% as a tie.", "",
          "## Everything else", "",
          "- [README.md](README.md): how the project works and where every file lives.",
          "- [_reference/](_reference/): cross-class reports (simulator summaries, the talentsforever.com comparison, the checklists for launch).", ""]
    (ROOT / "START-HERE.md").write_text("\n".join(o) + "\n", encoding="utf-8")


def main():
    """Superseded by render_modes.py (2026-09-29: the spec x mode layout); this file stays as its helper library."""
    import render_modes
    render_modes.main()


if __name__ == "__main__":
    main()
