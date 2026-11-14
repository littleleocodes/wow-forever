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
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
# The user's combined readable files (2026-11-13: All_RestedXP_Guides_READABLE.txt, Alliance_Guides_READABLE.txt,
# Alliance_Dungeon_Guide_READABLE.txt) hold one guide per "===== group|subgroup|name|n =====" block, and the per-guide files under
# Individual_Guides/ repeat them; every guide comes in each version the add-on has imported (#version 24 twice, 25).
SEP = re.compile(r"^===== .+ =====[ \t]*\r?$", re.M)
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
        parts = [x for x in SEP.split(text) if "#name" in x]   # a combined file: one text per block
        return parts or [text]
    return [m.group(2) for m in re.finditer(r"RegisterGuide\(\s*(?:\"[^\"]*\"\s*,\s*)?\[(=*)\[(.*?)\]\1\]", text, re.S)]


def world(arg, maps):
    """(continent map id, world x, world y, zone) of a .goto argument, the inverse of `position` for the zone-name form."""
    m = re.match(r"(\d+)/\d+,(-?[\d.]+),(-?[\d.]+)", arg)
    if m:
        b = maps.get(m.group(1))
        return (b["map"], float(m.group(3)), float(m.group(2)), b["name"]) if b else None
    m = re.match(r"([A-Za-z][^,]*),([\d.]+),([\d.]+)", arg)
    if m:
        b = next((v for v in maps.values() if v["name"] == m.group(1).strip()), None)
        if b:
            x, y = float(m.group(2)) / 100, float(m.group(3)) / 100
            return (b["map"], b["x1"] - y * (b["x1"] - b["x0"]), b["y1"] - x * (b["y1"] - b["y0"]), b["name"])
    return None


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


def a32(s):
    """The add-on's Adler-32 (GuideLoader addon.A32): a guide key's hash, the base of its step ids."""
    d = s.encode("utf-8")
    n, a, b, i = len(d), 1, 0, 0
    while i <= n - 16:
        x = d[i:i + 16]
        b = (b + 16 * a + sum((16 - k) * x[k] for k in range(16))) % 65521
        a = (a + sum(x)) % 65521
        i += 16
    while i < n:
        a = (a + d[i]) % 65521
        b = (b + a) % 65521
        i += 1
    return (b * 65536 + a) & 0xffffffff


def affix(name):
    """The name the add-on shows and saves: a one-digit first level gets a zero ("1-6 Northshire" -> "01-06 Northshire")."""
    return re.sub(r"^(\d)-(\d\d?)(?=\D)", lambda m: f"{int(m.group(1)):02d}-{int(m.group(2)):02d}", name.strip())


def step_ids(text, head, builtin):
    """RestedXP's id of each step (GuideLoader.ParseGuide: the step line's number among the text's non-empty lines plus addon.A32 of the
    guide's key), in parse_file's step order; None when the two disagree. An imported guide (the readable files are the add-on's imported
    cache: its first line is the cache's "--" stamp) has the key group|subgroup|name and is counted as it is; a guide the add-on ships
    (Guides/forever/*.lua) has the key group||name and loses its "--" comments first."""
    if builtin:
        text = re.sub(r"--[^\r\n]*[\r\n]+", "\n", text)
        key = f"{head['group']}||{head['name'].strip()}"
    else:
        key = f"{head['group']}|{head.get('subgroup') or ''}|{head['name'].strip()}"
    gid, ids = a32(key), []
    for i, line in enumerate(x for x in re.split(r"[\r\n]+", text) if x):
        s = line.strip()
        if not s.startswith("--") and s.split("<<", 1)[0].strip() == "step":
            ids.append(gid + i + 1)
    return ids


_CATALOG = {}


def catalog(roots):
    """Every distinct guide text on this PC, parsed once per run: [{"head", "steps", "ids", "builtin", "version", "digest", "files"}].
    The same guide in several files (the combined files, Individual_Guides/, the add-on's own) counts once: texts equal apart from
    whitespace and comment lines are one entry (2026-11-13, user: "Avoid double-counting guide entries that appear in multiple combined
    files"). Nothing is written to disk."""
    k = tuple(roots)
    if k in _CATALOG:
        return _CATALOG[k]
    out, seen = [], {}
    for root, pattern in roots:
        if not pathlib.Path(root).is_dir():
            continue
        for p in sorted(pathlib.Path(root).rglob(pattern)):
            try:
                texts = blocks(p)
            except OSError:
                continue
            builtin = p.suffix.lower() == ".lua"
            for t in texts:
                if "#group" not in t or "#name" not in t:
                    continue
                norm = "\n".join(x.strip() for x in t.replace("\r", "").split("\n") if x.strip() and not x.strip().startswith("--"))
                dg = hashlib.md5(norm.encode("utf-8")).hexdigest()
                if (dg, builtin) in seen:
                    seen[(dg, builtin)]["files"].add(p.name)
                    continue
                head, steps = parse_file(t)
                if not head.get("name") or not head.get("group"):
                    continue
                ids = step_ids(t, head, builtin)
                e = {"head": head, "steps": steps, "ids": ids if len(ids) == len(steps) else None, "builtin": builtin, "digest": dg,
                     "version": int(head["version"]) if str(head.get("version", "")).isdigit() else 0, "files": {p.name}}
                seen[(dg, builtin)] = e
                out.append(e)
    _CATALOG[k] = out
    return out


def live(copies, saved):
    """The copy of a guide the add-on runs: the one holding a step id the character's saved progress names (exact), else the highest
    #version (then the most steps). The add-on keeps one copy per guide key and loads its imported copies in no fixed order, so without a
    saved step id the newest version is a guess, and the record says so."""
    hit = [c for c in copies if c["ids"] and saved & set(c["ids"])]
    pool = hit or copies
    best = max(pool, key=lambda c: (c["version"], len(c["steps"])))
    rivals = [c for c in copies if c is not best and c["version"] == best["version"] and len(c["steps"]) != len(best["steps"])]
    return dict(best, by_id=bool(hit), versions=sorted({c["version"] for c in copies}), ambiguous=not hit and bool(rivals))


def load(roots, group, progress=None):
    """{section name: [{"head", "steps", "ids", "by_id", "versions", "ambiguous", ...}, ...]} of every guide whose #group is `group`: the
    readable files under the user's folder and the add-on's own .lua guides (its free sections of the same group: the Alliance dungeon
    guide's 11-21, 2026-11-10), one live copy per name and race filter (a name can have several sections, one per race filter: the 11-16
    opening). Names as the add-on saves them (affix). `progress`: the character's saved {guide key: (step, step id)} (rxp.route)."""
    saved = {}
    for key, (_, sid) in (progress or {}).items():
        g, _, n = key.partition("|")[0], None, key.split("|")[-1]
        saved.setdefault((g, affix(n)), set()).add(sid)
    by = {}
    for c in catalog(roots):
        if c["head"]["group"] != group:
            continue
        by.setdefault((affix(c["head"]["name"]), c["head"].get("filter", "")), []).append(c)
    out = {}
    for (name, _), copies in by.items():
        out.setdefault(name, []).append(live(copies, saved.get((group, name), set())))
    return out


def chain(route, mine):
    """The route's sections from the add-on's current guide on, each guide's "next" in its own text first (the guides the add-on ships
    have no imported metadata: Tara's 20-21 guide had sent the route to the group's lowest imported section, 2026-11-13), else in the saved
    metadata; [{"name", "lo", "hi", "zones"}]."""
    import rxp
    out, name, seen = [], route.get("current"), set()
    while name and name not in seen:
        seen.add(name)
        m = rxp.SECTION.match(name)
        if not m:
            break
        out.append({"name": name, "lo": int(m.group(1)), "hi": int(m.group(2)), "zones": rxp.zones(name)})
        sec = mine.get(name)
        nx = str(sec["head"].get("next") or "") if sec else ""
        nx = affix(nx.split(";")[0].strip().split("\\")[-1].strip()) if nx else (route.get("meta") or {}).get(name)
        name = nx or None
    return out


def check(route, mine, who, maps):
    """Whether the guide text on this PC is the route the add-on runs (2026-11-13, user: "verify that the current RestedXP guide section and
    step match the extracted content ... when guide data is missing or mismatched, show a warning"): {"ok", "problems": [text],
    "current": {"found", "by_id", "step", "window", "versions", "ops", "npc", "zone"}, "missing": [(lo, hi)], "ambiguous": [(lo, hi)]}.
    The step is matched by the add-on's own step id (exact: a copy and a step), else by its saved step number (unverified)."""
    out = {"ok": True, "mismatch": False, "problems": [], "current": {}, "missing": [], "ambiguous": []}
    cur = route.get("current")
    sec = mine.get(cur)
    lv = lambda n: tuple(int(x) for x in (re.match(r"(\d+)-(\d+)", n) or re.match(r"(0)-(0)", "0-0")).groups())
    if not sec:
        out["ok"], out["mismatch"] = False, True
        out["problems"].append(f"the guide part you are on in RestedXP (levels {lv(cur)[0]}-{lv(cur)[1]}) is not in the guide text on this PC")
    else:
        steps = [s for s in sec["steps"] if applies(s["filter"], who, lv(cur)[0])]
        ids = [i for s, i in zip(sec["steps"], sec["ids"] or [None] * len(sec["steps"])) if applies(s["filter"], who, lv(cur)[0])]
        c = out["current"] = {"found": True, "by_id": False, "versions": sec.get("versions"), "version": sec["head"].get("version")}
        sid = route.get("step_id")
        if sid and sec["ids"] and sid in ids:
            k = ids.index(sid)
            c.update(by_id=True, index=k + 1)
        elif sid and sec["ids"] and route.get("saved_current") == cur:
            out["ok"], out["mismatch"] = False, True
            out["problems"].append(f"your current step in RestedXP (step {route.get('step')} of the part for levels {lv(cur)[0]}-{lv(cur)[1]}) "
                                   "is not in any copy of that part's guide text on this PC: the add-on runs a version this PC lacks")
        elif route.get("step"):
            k = min(len(steps), route["step"]) - 1
            c["index"] = k + 1
            if route["step"] > len(steps):
                out["ok"], out["mismatch"] = False, True
                out["problems"].append(f"RestedXP's saved step {route['step']} is past the end of that part's guide text ({len(steps)} steps)")
        if c.get("index"):
            st = steps[c["index"] - 1]
            ok, tags, ops = step_view(st, who, lv(cur)[0], lambda _t: True)
            spot = where(tags, maps) if tags else None
            num = sum(1 for s in steps[:c["index"]] if step_view(s, who, lv(cur)[0], lambda _t: True)[1].get("loaded"))
            c.update(step=c["index"], window=num, ops=ops, npc=(tags.get("targets") or [None])[0] if tags else None,
                     zone=spot[0] if spot else None, xy=(spot[1], spot[2]) if spot else None)
    for rs in route.get("sections") or []:
        if rs["name"] not in mine:
            out["missing"].append((rs["lo"], rs["hi"]))
        elif mine[rs["name"]].get("ambiguous"):
            out["ambiguous"].append((rs["lo"], rs["hi"]))
    if out["missing"]:
        out["ok"] = False
        spans = []   # adjacent or overlapping parts read as one span ("levels 29-60")
        for a, b in sorted(out["missing"]):
            if spans and a <= spans[-1][1] + 1:
                spans[-1][1] = max(spans[-1][1], b)
            else:
                spans.append([a, b])
        out["problems"].append("the guide text for the route's parts at levels " + ", ".join(f"{a}-{b}" for a, b in spans)
                               + " is not on this PC")
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
    out = {"dungeons": {}, "group": False, "ssf": False}
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
    out["ssf"] = bool(re.search(r'\n\["soloSelfFound"\] = true', block))
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
        elif t == "fly" and "travel" not in tags:
            tags["travel"] = f"the flight to {a}" if a else "a flight"
        elif t == "hs" and "travel" not in tags:
            tags["travel"] = "your hearthstone"
        elif t in ("zone", "zoneskip") and a and "travel" not in tags:
            tags["travel"] = f"the trip to {a.split(',')[0].split('/')[0]}"
    tags["dungeon"] = dungeon
    tags["loaded"] = loaded(tags, who, dungeon, dskip, enabled)
    if not tags["loaded"]:
        return False, tags, ops
    if tags.get("maxlevel") and level > tags["maxlevel"]:   # .maxlevel: numbered, skipped in play once you are past the level
        return False, tags, ops
    return True, tags, ops


def loaded(tags, who, dungeon, dskip, enabled):
    """The add-on's load-time step rules (addon.stepLogic, run by ProcessGuideTable when the guide loads): a step that fails one is left
    out of the guide's step list and gets no number in its window (2026-11-10: the one solo-self-found step of the 24-27 Duskwood part
    put every later step number one above the window's). The .maxlevel element is not one of them: that step keeps its number and is
    skipped in play."""
    for off in ("som", "hardcore", "hardcoreserver", "questguide", "beta"):
        if tags.get(off):
            return False
    if (tags.get("ssf") and not who.get("ssf")) or (tags.get("ah") and who.get("ssf")):
        return False
    if "season" in tags and "0" not in re.split(r"[,;\s]+", str(tags["season"])):
        return False
    if "phase" in tags and not in_range(tags["phase"], 6):
        return False
    if "xprate" in tags and not in_range(tags["xprate"], 1.0):
        return False
    if (tags.get("groupquest") and not who["group"]) or (tags.get("soloquest") and who["group"]):
        return False
    if dskip and enabled(dskip):
        return False
    if dungeon and dungeon != dskip and not enabled(dungeon):
        return False
    return True


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
            "gender": p["gender"]["type"], "group": prof["group"], "ssf": prof.get("ssf", False)}


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
    sections = load(roots, route["group"], route.get("progress"))
    if not sections:
        return None
    character = f"{snap['profile']['name']}-{snap['profile'].get('surname', '')}".strip("-")
    prof = profile(wow_dir, character)
    who = who_of(cfg, snap, prof)
    maps = bounds()
    mine = {n: s for n, secs in sections.items() if (s := pick(secs, who))}
    route["sections"] = chain(route, mine) or route.get("sections") or []   # from the add-on's current guide (updates ROUTE in place)
    trust = check(route, mine, who, maps)
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

    out = {"quests": {}, "dungeons": {}, "past": set(), "who": who, "profile": prof, "runs": runs, "npcs": {}, "path": [], "behind": {},
           "taggable": {NAMES[t]: t for t in sorted(tagged) if not enabled(t)}, "trust": trust}
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
        here = rs["name"] == route["current"]
        at = trust["current"].get("index") if here else None   # the current step by its id (or its saved number), 1-based
        cur = route["step"] if here and route.get("step") else 0
        floor, n, num = lo, max(1, len(steps)), 0
        for i, st in enumerate(steps):
            level = max(floor, round(lo + (hi - lo) * i / n))
            ok, tags, ops = step_view(st, who, level, enabled)
            num += bool(tags.get("loaded"))   # the step's number in the guide window (the add-on's saved step counts the same way)
            if not ok:
                continue
            if tags.get("xp"):
                floor = max(floor, min(hi, tags["xp"]))
            spot = where(tags, maps)
            past = (i + 1 < at) if at else num < cur
            w = next((x for x in (world(a, maps) for a in reversed(tags.get("goto") or [])) if x), None)
            if w and not past:   # where the route takes you, level by level (detours.py measures from here): level, continent, world x, y,
                out["path"].append((level, w[0], w[1], w[2], w[3], lo, hi, num, tuple(ops),   # zone, the section's levels, the step's
                                    tags["targets"][0] if tags["targets"] else None, spot,        # number in it, its quests, NPC, map spot,
                                    tags.get("travel")))                                          # the travel the step starts (a flight...)
            pidx = len(out["path"]) - 1   # the route point at or just before this step (a detour's anchor)
            for el in st["els"]:   # where the guide runs its own dungeon (.enabledungeon); one you have passed is behind you
                if el["tag"] == "enabledungeon" and el["arg"] and not el["arg"].startswith("!") and applies(el["filter"], who, level):
                    t = tag_of(el["arg"])
                    if t and past:
                        out["behind"][NAMES[t]] = (num, lo, hi)
                    elif t:
                        d = out["dungeons"].setdefault(NAMES[t], {"tag": t, "level": None, "quests": []})
                        d["level"], d["at"] = level, (max(0, pidx), num, lo, hi)
            for op, q in ops:
                if past:
                    out["past"].add(q)
                    continue
                e = out["quests"].setdefault(q, {})
                s = {"level": level, "zone": spot[0] if spot else None, "x": spot[1] if spot else None, "y": spot[2] if spot else None,
                     "npc": tags["targets"][0] if tags["targets"] else None, "at": pidx, "step": num, "lo": lo, "hi": hi}
                if op == "accept" and "accept" not in e:
                    e["accept"] = s
                elif op == "turnin":
                    e["turnin"] = s
                elif op == "complete" and "complete" not in e:
                    e["complete"], e["complete_at"] = level, (pidx, num, lo, hi)
                if tags["dungeon"]:
                    d = out["dungeons"].setdefault(NAMES[tags["dungeon"]], {"tag": tags["dungeon"], "level": None, "quests": []})
                    if q not in d["quests"]:
                        d["quests"].append(q)
                    if op == "complete" and d["level"] is None:
                        d["level"] = level
    for d in out["dungeons"].values():   # a ticked dungeon is run where the route completes its quests (else at the first turn-in)
        if d["level"] is None:
            lv = sorted(out["quests"][q].get("complete") or (out["quests"][q].get("turnin") or {}).get("level") or 99 for q in d["quests"])
            d["level"] = lv[0] if lv and lv[0] < 99 else None
    out["before"] = before(mine, route, who, maps, enabled, trust["current"].get("index"))
    out["extra"] = dungeon_quest_guides(roots, who, maps)
    out["givers"] = givers(roots, who, maps)
    return out


def before(mine, route, who, maps, enabled, at=None):
    """What the route did before the character's current step (2026-11-10, user: what to do "to have the checklist and RestedXP the most
    sync it can be"): every earlier part of the guide group (followed back by its "next" links) and the current part up to the step,
    {quest: {"accept"|"complete"|"turnin": {"level", "zone", "x", "y", "npc", "step", "lo", "hi"}}} (the first time each)."""
    nxt = {}
    for n, sec in mine.items():
        x = str(sec["head"].get("next") or "").split(";")[0].strip().split("\\")[-1].strip()
        if x:
            nxt[n] = x
    back = {v: k for k, v in nxt.items()}
    order, n = [], route["current"]
    while n in back and back[n] not in order and back[n] != route["current"]:
        n = back[n]
        order.insert(0, n)
    out = {}
    for part in order + [route["current"]]:
        sec = mine.get(part)
        m = re.match(r"(\d+)-(\d+)", part)
        if not sec or not m:
            continue
        lo, hi = int(m.group(1)), int(m.group(2))
        steps = [x for x in sec["steps"] if applies(x["filter"], who, lo)]
        num = 0
        for i, st in enumerate(steps):
            level = round(lo + (hi - lo) * i / max(1, len(steps)))
            ok, tags, ops = step_view(st, who, level, enabled)
            num += bool(tags.get("loaded"))
            if part == route["current"] and ((i + 1 >= at) if at else num >= (route.get("step") or 0)):
                break
            if not ok:
                continue
            spot = where(tags, maps)
            for op, q in ops:
                out.setdefault(q, {}).setdefault(op, {"level": level, "zone": spot[0] if spot else None, "x": spot[1] if spot else None,
                                                      "y": spot[2] if spot else None, "npc": tags["targets"][0] if tags["targets"] else None,
                                                      "step": num, "lo": lo, "hi": hi})
    return out


def givers(roots, who, maps):
    """{quest id: {"npc", "zone", "x", "y"}} of every quest any guide on this PC accepts for this character (every group: the leveling and
    speedrun guides, the per-dungeon quest guides, the class guides): where to pick up a quest the route leaves out."""
    out = {}
    for c in sorted(catalog(roots), key=lambda c: -c["version"]):
        if not applies(c["head"].get("filter", ""), who, 60):
            continue
        for st in c["steps"]:
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


def main():
    """`python rxp_guide.py <character> [...]`: the RestedXP check (rxp_guide.check) for each character, plus how many guide texts the files
    hold and how many are distinct. Facts only (levels, step numbers, quest ids, NPC, zone), never the guide's wording or its part names."""
    import sys
    import rxp
    sys.stdout.reconfigure(encoding="utf-8")
    for name in sys.argv[1:]:
        d = HERE.parents[2] / "_characters" / name.lower()
        cfg = json.loads((d / "character.json").read_text(encoding="utf-8"))
        prof = json.loads((d / "armory" / "profile.json").read_text(encoding="utf-8"))
        wow = cfg.get("wow_dir") or str((cfg.get("ah") or {}).get("ahcopy", "")).split("/Interface/")[0]
        route = rxp.route(wow, f"{prof['name']}-{prof.get('surname', '')}".strip("-"))
        if not route:
            print(f"{name}: no RestedXP saved files for this character")
            continue
        cat = catalog(roots_of(cfg, wow))
        f = facts(cfg, {"profile": prof}, wow, route)
        if not f:
            print(f"{name}: no guide text for the add-on's guide on this PC ({len(cat)} distinct guide texts found)")
            continue
        tr, c = f["trust"], f["trust"]["current"]
        part = (route["sections"] or [{}])[0]
        print(f"{name} (level {prof['level']}): {len(cat)} distinct guide texts; route {len(route['sections'])} parts from levels "
              f"{part.get('lo')}-{part.get('hi')}")
        print(f"  current step: {c.get('window')} of the {part.get('lo')}-{part.get('hi')} part, "
              + ("matched by the add-on's step id" if c.get("by_id") else "by the saved step number only")
              + f" (guide version {c.get('version')} of {c.get('versions')}); quests {c.get('ops')}, NPC {c.get('npc')}, "
              f"{c.get('zone')} {c.get('xy')}")
        print("  " + ("OK" if tr["ok"] else "PROBLEMS: " + "; ".join(tr["problems"]))
              + (f"; versions differ with no saved step to tell them apart at levels {tr['ambiguous']}" if tr["ambiguous"] else ""))
        print(f"  route facts: {len(f['quests'])} quests ahead, {len(f['past'])} behind, {len(f['npcs'])} NPC positions, "
              f"{len(f['dungeons'])} dungeons ahead, {len(f['before'])} earlier quests for catch-up")


if __name__ == "__main__":
    main()
