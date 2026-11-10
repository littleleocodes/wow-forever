"""The character's RestedXP route step by step, from the readable guide files the user keeps on this PC (2026-11-10, user: "I am explicitly
withdrawing that instruction for my personal, local use ... read the supplied text files as reference material to improve my personal WoW:
Forever leveling and dungeon planner ... Keep the original guide files local. Do not commit them to GitHub or include their text in the
published checklist").

Facts only: for each step the route shows this character, the quests it accepts, completes and turns in (ids), the NPCs it names and the map
position (zone, x, y), with the level the route is at there; from RestedXP's per-dungeon quest guides, each dungeon's quests with their givers.
The files are read where the user keeps them (character.json "rxp_dir", default F:/wow-addons, outside the repository) and nothing is cached:
the planner's pages name zones, quests, NPCs and levels, never the guide's wording or its section names.

Which steps a character sees follows the add-on's own rules (RXPGuides 2026-11-07: GuideLoader.applies, RXPGuides.lua stepLogic,
functions.dungeon/enabledungeon): class, race, faction, gender and level filters on steps and lines; the season (0), hardcore (off), phase (6),
XP rate (1), solo-self-found (off) and loremaster (off) switches; group quests by the character's RestedXP profile; dungeon steps by the
dungeons ticked in that profile, except the dungeons a guide group switches on itself (.enabledungeon), which are on for the whole group.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
QUEST_GUIDES = "RXP Forever Dungeon Quests (A)"   # RestedXP's per-dungeon quest guides (Alliance)
# RestedXP's dungeon tags (RXPGuides DB/forever/db.lua dungeonList) -> the planner's dungeon names (item_pool.DUNGEONS; Blizzard's area
# names for Forever's own dungeons)
NAMES = {"RFC": "Ragefire Chasm", "DM": "The Deadmines", "WC": "Wailing Caverns", "SFK": "Shadowfang Keep", "BFD": "Blackfathom Deeps",
         "STOCKS": "The Stockade", "GNOMER": "Gnomeregan", "RFK": "Razorfen Kraul", "SM": "Scarlet Monastery", "RFD": "Razorfen Downs",
         "ULDA": "Uldaman", "ZF": "Zul'Farrak", "MARA": "Maraudon", "ST": "Sunken Temple", "BRD": "Blackrock Depths", "DME": "Dire Maul",
         "SCHOLO": "Scholomance", "STRAT": "Stratholme", "LBRS": "Blackrock Spire", "HOT": "The Hall of Thanes",
         "ROL": "Ruins of Lordaeron", "ES": "Excavation Site: Wetlands", "COD": "City of Dalaran"}
ALT = {"DEADMINES": "DM", "VC": "DM", "STOCKADES": "STOCKS", "TEMPLE OF ATAL'HAKKAR": "ST", "DMW": "DME", "DMN": "DME", "ESW": "ES",
       "GNOMER": "GNOMER", "MARA": "MARA", "ULDA": "ULDA"}
FORMAT = re.compile(r"\|c[0-9A-Za-z_]{1,24}|\|r|\|T[^|]*\|t|\|H[^|]*\|h|\|h")


def tag_of(name):
    """RestedXP's tag for a dungeon name or tag ("Stockades" -> STOCKS, "01. Hall of Thanes" -> HOT, "Dire Maul (West)" -> DME)."""
    u = re.sub(r"^\d+\.\s*", "", name.strip()).upper()
    if u in NAMES:
        return u
    if u in ALT:
        return ALT[u]
    u = re.sub(r"\s*\(.*\)$", "", u)
    u = re.sub(r"^(LOWER|UPPER) ", "", u)
    for t, n in NAMES.items():
        if u in (n.upper(), n.upper().removeprefix("THE "), n.upper().split(":")[0]):
            return t
    return None


def bounds():
    return json.loads((HERE / "uimap_bounds.json").read_text(encoding="utf-8"))["maps"]


def position(arg, maps):
    """(zone, x, y) of a .goto argument: "1431/0,-1213.54,-10531.89" (map id, world y, world x) or "Duskwood,75.8,45.3"."""
    m = re.match(r"(\d+)/\d+,(-?[\d.]+),(-?[\d.]+)", arg)
    if m:
        b = maps.get(m.group(1))
        if not b:
            return None
        wy, wx = float(m.group(2)), float(m.group(3))
        return (b["name"], round(100 * (b["y1"] - wy) / (b["y1"] - b["y0"]), 1), round(100 * (b["x1"] - wx) / (b["x1"] - b["x0"]), 1))
    m = re.match(r"([A-Za-z][^,]*),([\d.]+),([\d.]+)", arg)
    return (m.group(1).strip(), float(m.group(2)), float(m.group(3))) if m else None


def blocks(path):
    """The guide texts in a file: a readable guide .txt is one; the add-on's own .lua files hold one per RXPGuides.RegisterGuide([[...]])."""
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() != ".lua":
        return [text]
    return [m.group(2) for m in re.finditer(r"RegisterGuide\(\s*(?:\"[^\"]*\"\s*,\s*)?\[(=*)\[(.*?)\]\1\]", text, re.S)]


def parse_file(text):
    """(header {tag: value}, steps [{"filter", "els": [{"tag", "arg", "filter"}]}]) of one guide text."""
    head, steps, cur = {}, [], None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("--"):
            continue
        filt = ""
        if "<<" in line:   # the add-on reads everything after the first "<<" as the line's filter
            line, filt = (x.strip() for x in line.split("<<", 1))
        if re.fullmatch(r"step", line):
            cur = {"filter": filt, "els": []}
            steps.append(cur)
            continue
        if cur is None:
            if line.startswith("#"):
                k, _, v = line[1:].partition(" ")
                head.setdefault(k, v.strip() or True)
            elif not line and filt:
                head["filter"] = filt
            continue
        if line.startswith("#"):
            k, _, v = line[1:].partition(" ")
            cur["els"].append({"tag": "#" + k, "arg": v.strip(), "filter": filt})
        elif line.startswith("."):
            body = line.split(">>", 1)[0]
            tag, _, args = body[1:].strip().partition(" ")
            cur["els"].append({"tag": tag, "arg": re.sub(r"\s*,\s*", ",", args.strip()), "filter": filt})
    return head, steps


def load(roots, group):
    """{section name: [{"head", "steps"}, ...]} of every guide text whose #group is `group`: the readable .txt files under the user's folder
    and the add-on's own .lua guides (its free sections of the same group: the Alliance dungeon guide's 11-21, 2026-11-10). A name can
    have several sections, one per race filter (the 11-16 opening)."""
    out = {}
    for root, pattern in roots:
        if not pathlib.Path(root).is_dir():
            continue
        for p in sorted(pathlib.Path(root).rglob(pattern)):
            try:
                texts = blocks(p)
            except OSError:
                continue
            for t in texts:
                if f"#group {group}\n" not in t[:800].replace("\r", ""):
                    continue
                head, steps = parse_file(t)
                if head.get("name"):
                    out.setdefault(head["name"].strip(), []).append({"head": head, "steps": steps})
    return out


def roots_of(cfg, wow_dir):
    """Where the guide texts are: the user's readable files (character.json "rxp_dir", default F:/wow-addons) and the installed add-on."""
    return [(cfg.get("rxp_dir") or "F:/wow-addons", "*.txt"),
            (str(pathlib.Path(wow_dir) / "Interface" / "AddOns" / "RXPGuides" / "Guides" / "forever"), "*.lua")]


def pick(secs, who, level=60):
    """The section of a name whose own filter (its "<< Alliance NightElf" line) applies to the character."""
    for s in secs or []:
        if applies(s["head"].get("filter", ""), who, level):
            return s
    return None


def profile(wow_dir, character):
    """The character's RestedXP settings: {"dungeons": {tag: bool}, "group": bool} from the account's saved file (its profile is
    "<Name> - <Realm>"), or defaults."""
    import rxp
    acc, _ = rxp.files(wow_dir, character)
    out = {"dungeons": {}, "group": False}
    if not acc:
        return out
    text = acc.read_text(encoding="utf-8", errors="replace")
    i = text.find("RXPSettings = {")
    name = character.split("-")[0]
    m = re.search(r'\n\["' + re.escape(name) + r' - [^"]+"\] = \{\n', text[i:]) if i >= 0 else None
    if not m:
        return out
    start, depth, j = i + m.end(), 1, i + m.end()
    while depth and j < len(text):   # the profile's block, by its braces
        depth += {"{": 1, "}": -1}.get(text[j], 0)
        j += 1
    block = text[start:j]
    d = re.search(r'\n\["dungeons"\] = \{(.*?)\n\}', block, re.S)
    if d:
        out["dungeons"] = {k: v == "true" for k, v in re.findall(r'\["(\w+)"\] = (true|false)', d.group(1))}
    out["group"] = bool(re.search(r'\n\["enableGroupQuests"\] = true', block))
    return out


def applies(text, who, level):
    """The add-on's filter (GuideLoader.applies): "/" separates alternatives, every entry of one must hold, "!" negates; entries are a
    class, race, faction, gender, level (reached), the game or the locale; parentheses group."""
    if not text:
        return True
    text = re.sub(r"(!?)\(\s*(.*?)\s*\)", lambda m: "TRUEX" if applies(m.group(2), who, level) != (m.group(1) == "!") else "NULLX", text)
    for alt in text.split("/"):
        ok = True
        for ent in re.findall(r"!?\w+", alt):
            neg, e = ent.startswith("!"), ent.lstrip("!")
            u = {"DK": "DEATHKNIGHT"}.get(e.upper(), e.upper())
            e = "Scourge" if e == "Undead" else e
            hit = (u == who["class"] or e == who["race"] or e == who["faction"] or u == who["gender"] or u == "FOREVER" or e == "enUS"
                   or e == "TRUEX" or (e.isdigit() and level >= int(e)))
            if hit == neg:
                ok = False
                break
        if ok:
            return True
    return False


def in_range(spec, value):
    """The add-on's phase and XP-rate ranges: "4", "4-6", "<1.99", ">1.5"."""
    m = re.match(r"\s*([<>]?)\s*(\d+\.?\d*)-?(\d*\.?\d*)", str(spec))
    if not m:
        return True
    op, a, b = m.group(1), float(m.group(2)), m.group(3)
    if op == "<":
        return value < a
    if op == ">":
        return value > a
    return a <= value <= (float(b) if b else 1e9)


def step_view(step, who, level, enabled):
    """(shown, tags, ops) of a step for this character: ops [(op, quest id)] for accept, complete and turnin; tags {name: value} of its
    #tags plus "targets", "goto", "dungeon", "xp"."""
    if not applies(step["filter"], who, level):
        return False, {}, []
    tags, ops = {"targets": [], "goto": []}, []
    dungeon = dskip = None
    for el in step["els"]:
        if el["filter"] and not applies(el["filter"], who, level):
            continue
        t, a = el["tag"], el["arg"]
        if t.startswith("#"):
            tags.setdefault(t[1:], a or True)
        elif t in ("accept", "turnin", "complete") and re.match(r"\d+", a):
            ops.append((t, int(re.match(r"\d+", a).group())))
        elif t == "target" and a:
            for t1 in a.split(","):   # "+Name" and "Name::3649" (the NPC's id); several names: the step's NPCs
                t1 = t1.split("::")[0].strip().lstrip("+").strip('"').strip()
                if t1:
                    tags["targets"].append(t1)
        elif t == "goto" and a:
            tags["goto"].append(a)
        elif t == "dungeon" and a:
            if a.startswith("!"):
                dskip = tag_of(a[1:])
            else:
                dungeon = tag_of(a)
        elif t == "group":
            tags["groupquest"] = True
        elif t == "solo":
            tags["soloquest"] = True
        elif t == "maxlevel" and re.match(r"\d+", a):
            tags["maxlevel"] = int(re.match(r"\d+", a).group())
        elif t == "xp" and re.match(r"\d+", a):
            tags["xp"] = int(re.match(r"\d+", a).group())
    tags["dungeon"] = dungeon
    for off in ("som", "hardcore", "hardcoreserver", "ssf", "questguide"):
        if tags.get(off):
            return False, tags, ops
    if "season" in tags and "0" not in re.split(r"[,;\s]+", str(tags["season"])):
        return False, tags, ops
    if "phase" in tags and not in_range(tags["phase"], 6):
        return False, tags, ops
    if "xprate" in tags and not in_range(tags["xprate"], 1.0):
        return False, tags, ops
    if (tags.get("groupquest") and not who["group"]) or (tags.get("soloquest") and who["group"]):
        return False, tags, ops
    if tags.get("maxlevel") and level > tags["maxlevel"]:
        return False, tags, ops
    if dskip and enabled(dskip):
        return False, tags, ops
    if dungeon and dungeon != dskip and not enabled(dungeon):
        return False, tags, ops
    return True, tags, ops


def where(tags, maps):
    """(zone, x, y) of a step's last .goto (the spot the step ends at)."""
    for a in reversed(tags.get("goto") or []):
        p = position(a, maps)
        if p:
            return p
    return None


def who_of(cfg, snap, prof):
    p = snap["profile"]
    return {"class": cfg["class"].upper(), "race": p["race"]["name"].replace(" ", ""), "faction": p["faction"]["name"],
            "gender": p["gender"]["type"], "group": prof["group"]}


def facts(cfg, snap, wow_dir, route):
    """The route as facts, or None when the guide files are not on this PC:
    {"quests": {id: {"accept": spot, "turnin": spot, "complete": level}} from the character's current step on,
     "past": {ids the route handled before the current step},
     "dungeons": {name: {"tag", "level", "quests": [ids]}} the route runs from here on (its own dungeons and the ticked ones),
     "runs": {name: (lo, hi)} every dungeon the guide group runs itself, by its section's levels (also the ones behind you),
     "taggable": {name: tag} optional dungeons whose quests the route would pick up if ticked in RestedXP (not ticked now),
     "npcs": {name: spot}, "extra": {dungeon name: [{"quest", "giver", "spot"}]} (RestedXP's per-dungeon quest guides),
     "who", "profile"}; a spot is {"level", "zone", "x", "y", "npc"}."""
    if not route:
        return None
    roots = roots_of(cfg, wow_dir)
    sections = load(roots, route["group"])
    if not sections:
        return None
    character = f"{snap['profile']['name']}-{snap['profile'].get('surname', '')}".strip("-")
    prof = profile(wow_dir, character)
    who = who_of(cfg, snap, prof)
    maps = bounds()
    mine = {n: s for n, secs in sections.items() if (s := pick(secs, who))}
    override, runs, tagged = {}, {}, set()   # dungeons the group switches on itself (functions.enabledungeon: group-wide once parsed)
    for n, sec in mine.items():
        m = re.match(r"(\d+)-(\d+)", n)
        for st in sec["steps"]:
            for el in st["els"]:
                if el["tag"] == "enabledungeon" and el["arg"]:
                    t = tag_of(el["arg"].lstrip("!"))
                    if t:
                        override[t] = not el["arg"].startswith("!")
                        if m and not el["arg"].startswith("!"):
                            runs.setdefault(NAMES[t], (int(m.group(1)), int(m.group(2))))
                elif el["tag"] == "dungeon" and el["arg"] and not el["arg"].startswith("!"):
                    t = tag_of(el["arg"])
                    if t:
                        tagged.add(t)
    disabled = any(sec["head"].get("disabledungeons") for sec in mine.values())

    def enabled(t):
        if t in override:
            return override[t]
        return False if disabled else bool(prof["dungeons"].get(t))

    out = {"quests": {}, "dungeons": {}, "past": set(), "who": who, "profile": prof, "runs": runs, "npcs": {},
           "taggable": {NAMES[t]: t for t in sorted(tagged) if not enabled(t)}}
    for sec in mine.values():   # where each NPC stands (the guide's own positions)
        for st in sec["steps"]:
            ok, tags, _ = step_view(st, who, 60, lambda _t: True)
            spot = where(tags, maps) if ok and tags.get("targets") else None
            if spot:
                for npc in tags["targets"]:
                    out["npcs"].setdefault(npc, {"zone": spot[0], "x": spot[1], "y": spot[2]})
    for k, rs in enumerate(route["sections"]):
        sec = mine.get(rs["name"])
        if not sec:
            continue
        lo, hi = rs["lo"], rs["hi"]
        steps = [s for s in sec["steps"] if applies(s["filter"], who, lo)]   # the add-on's step list (its saved step indexes it)
        cur = route["step"] if rs["name"] == route["current"] and route.get("step") else 0
        floor, n = lo, max(1, len(steps))
        for i, st in enumerate(steps):
            level = max(floor, round(lo + (hi - lo) * i / n))
            ok, tags, ops = step_view(st, who, level, enabled)
            if not ok:
                continue
            if tags.get("xp"):
                floor = max(floor, min(hi, tags["xp"]))
            spot = where(tags, maps)
            past = i + 1 < cur
            for op, q in ops:
                if past:
                    out["past"].add(q)
                    continue
                e = out["quests"].setdefault(q, {})
                s = {"level": level, "zone": spot[0] if spot else None, "x": spot[1] if spot else None, "y": spot[2] if spot else None,
                     "npc": tags["targets"][0] if tags["targets"] else None}
                if op == "accept" and "accept" not in e:
                    e["accept"] = s
                elif op == "turnin":
                    e["turnin"] = s
                elif op == "complete" and "complete" not in e:
                    e["complete"] = level
                if tags["dungeon"]:
                    d = out["dungeons"].setdefault(NAMES[tags["dungeon"]], {"tag": tags["dungeon"], "level": None, "quests": []})
                    if q not in d["quests"]:
                        d["quests"].append(q)
                    if op == "complete" and d["level"] is None:
                        d["level"] = level
        for t in {tag_of(el["arg"].lstrip("!")) for st in sec["steps"] for el in st["els"] if el["tag"] == "enabledungeon" and el["arg"]}:
            if t:
                d = out["dungeons"].setdefault(NAMES[t], {"tag": t, "level": None, "quests": []})
                d["level"] = d["level"] or lo
    for d in out["dungeons"].values():   # a ticked dungeon is run where the route completes its quests (else at the first turn-in)
        if d["level"] is None:
            lv = sorted(out["quests"][q].get("complete") or (out["quests"][q].get("turnin") or {}).get("level") or 99 for q in d["quests"])
            d["level"] = lv[0] if lv and lv[0] < 99 else None
    out["extra"] = dungeon_quest_guides(roots, who, maps)
    out["givers"] = givers(roots, who, maps)
    return out


def givers(roots, who, maps):
    """{quest id: {"npc", "zone", "x", "y"}} of every quest any guide on this PC accepts for this character (every group: the leveling and
    speedrun guides, the per-dungeon quest guides, the class guides): where to pick up a quest the route leaves out."""
    out = {}
    for root, pattern in roots:
        if not pathlib.Path(root).is_dir():
            continue
        for p in sorted(pathlib.Path(root).rglob(pattern)):
            try:
                texts = blocks(p)
            except OSError:
                continue
            for t in texts:
                head, steps = parse_file(t)
                if "#group" not in t[:800] or not applies(head.get("filter", ""), who, 60):
                    continue
                for st in steps:
                    ok, tags, ops = step_view(st, who, 60, lambda _t: True)
                    if not ok:
                        continue
                    spot = where(tags, maps)
                    for op, q in ops:
                        if op == "accept" and q not in out and (tags["targets"] or spot):
                            out[q] = {"npc": " / ".join(tags["targets"]) or None, "zone": spot[0] if spot else None,
                                      "x": spot[1] if spot else None, "y": spot[2] if spot else None}
    return out


def dungeon_quest_guides(roots, who, maps):
    """{dungeon name: [{"quest", "giver", "spot": (zone, x, y)}]} from RestedXP's per-dungeon quest guides: every quest a guide accepts
    for this character (dungeon toggles do not apply there), with the NPC and position of the step that accepts it."""
    out = {}
    for name, secs in load(roots, QUEST_GUIDES).items():
        t, sec = tag_of(name), pick(secs, who)
        if not t or not sec:
            continue
        rows = out.setdefault(NAMES[t], [])
        for st in sec["steps"]:
            ok, tags, ops = step_view(st, who, 60, lambda _t: True)
            if not ok:
                continue
            for op, q in ops:
                if op == "accept" and not any(r["quest"] == q for r in rows):
                    rows.append({"quest": q, "giver": " / ".join(tags["targets"]) or None, "spot": where(tags, maps)})
    return out
