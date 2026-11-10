"""The character's RestedXP route, from the guide add-on's saved files (2026-11-09, user: "Lift the restriction"): which guide group the
character follows, the section it is on (by its saved step) and the sections after it, each with its level range and zones.

Only plain-text metadata is read here (section names, level ranges, the next section, the current step). The route step by step comes
from rxp_guide.py (2026-11-10: the readable guide files the user extracted and keeps outside the repository, read for facts only; the
user withdrew the earlier never-decode rule for personal, local use). No section name is written into the repository: the plan uses the
route to time dungeon runs and quest rewards and to flag quests off it. The files are found by the character's folder name at run time (the
account folder's name is the account's: it is never printed or stored).
"""
import pathlib
import re

ABBREV = {"WPL": ["Western Plaguelands"], "EPL": ["Eastern Plaguelands"], "STV": ["Stranglethorn Vale"], "RFD": ["Razorfen Downs"],
          "Stockades": ["The Stockade"], "UnGoro Crater": ["Un'Goro Crater"], "Un'Goro": ["Un'Goro Crater"], "Hinterlands": ["The Hinterlands"],
          "Stonetalon": ["Stonetalon Mountains"], "Redridge": ["Redridge Mountains"], "Hillsbrad": ["Hillsbrad Foothills"],
          "Alterac": ["Alterac Mountains"], "Arathi": ["Arathi Highlands"], "Excavation Site": ["Wetlands"], "Dalaran": ["Alterac Mountains"],
          "Western": ["Western Plaguelands"], "Eastern Plaguelands": ["Eastern Plaguelands"], "Elwynn": ["Elwynn Forest"],
          "Dun Morogh": ["Dun Morogh"], "Loch Modan": ["Loch Modan"]}
SECTION = re.compile(r"^(\d+)-(\d+) (.+?)(?: part \d+|\d)?$")


def files(wow_dir, character):
    """(account-wide saved file, the character's saved file) or (None, None)."""
    base = pathlib.Path(wow_dir) / "WTF" / "Account"
    for c in base.glob(f"*/*/{character}/SavedVariables/RXPGuides.lua"):
        acc = c.parents[3] / "SavedVariables" / "RXPGuides.lua"
        return (acc if acc.exists() else None), c
    return None, None


def zones(name):
    """The zones of a section name ("24-27 Duskwood/Redridge/Stockades" -> Duskwood, Redridge Mountains, The Stockade)."""
    m = SECTION.match(name)
    rest = m.group(3) if m else name
    out = []
    for z in rest.split("/"):
        z = re.sub(r" (I|II|III)$", "", z.strip())   # "Stranglethorn Vale I"
        out += ABBREV.get(z, [z])
    return out


def route(wow_dir, character):
    """{"group", "current", "step", "sections": [{"name", "lo", "hi", "zones"}] from the current section on} or None."""
    acc, char = files(wow_dir, character)
    if not acc or not char:
        return None
    ctext = char.read_text(encoding="utf-8", errors="replace")
    g = re.search(r'\["currentGuideGroup"\] = "([^"]+)"', ctext)
    st = re.search(r'\["currentStep"\] = (\d+)', ctext)
    if not g:
        return None
    group, step = g.group(1), int(st.group(1)) if st else None
    cur = None
    for key, s in re.findall(r'\["([^"]+)"\] = \{\s*\["step"\] = (\d+)', ctext):
        if key.startswith(group + "|") and step is not None and int(s) == step:
            cur = key.split("|")[-1]
    meta = {}
    for b in re.findall(r'\["metadata"\] = \{(.*?)\n\}', acc.read_text(encoding="utf-8", errors="replace"), re.S):
        kv = dict(re.findall(r'\["(\w+)"\] = "([^"]*)"', b))
        if kv.get("group") == group and kv.get("name"):
            meta[kv["name"]] = kv.get("next", "")
    if not meta:
        return None
    if cur not in meta:   # no saved step matches: start from the lowest section
        cur = min(meta, key=lambda n: int((SECTION.match(n) or re.match(r"(\d+)", "99")).group(1)))
    out, name, seen = [], cur, set()
    while name and name in meta and name not in seen:
        seen.add(name)
        m = SECTION.match(name)
        if m:
            out.append({"name": name, "lo": int(m.group(1)), "hi": int(m.group(2)), "zones": zones(name)})
        nxt = meta[name].split(";")[0].strip()
        name = nxt.split("\\")[-1].strip() if nxt else None
    return {"group": group, "current": cur, "step": step, "sections": out}


def zones_at(rt, lo, hi):
    """Every zone the route visits in sections overlapping levels lo to hi."""
    return {z for s in (rt or {}).get("sections", []) if s["lo"] <= hi and s["hi"] >= lo for z in s["zones"]}


def dungeon_level(rt, dungeon):
    """The first level of the route's section that names this dungeon, or None."""
    for s in (rt or {}).get("sections", []):
        if dungeon in s["zones"] or dungeon.replace("The ", "") in s["zones"]:
            return s["lo"]
    return None
