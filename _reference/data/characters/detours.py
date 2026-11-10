"""Quests off the RestedXP route worth a detour (2026-11-10, user: "use the current RestedXP guide and route to help me decide when I should
pick up quests that are detours, requests that are out of the way, that aren't included in RestedXP, but that we deem are still worth it
because of the time they save when questing and leveling").

Every quest the character can take that the route leaves out (Classic's quest data: quest_geo.csv, spawns.csv and quest_item_sources.csv by
quest_geo_extract.py; the experience Forever gives from Blizzard's quest API) is played as a detour from the route at the level you would
do it: from the closest point the route passes at that level, walk to the giver, do each objective at the spawn nearest to where you are,
hand it in, walk back. A chain continues while its next part is off the route too; each first part of a chain is scored and the best kept.

Time: straight-line yards x PATH (terrain, roads) at running speed (x MOUNT_SPEED from MOUNT_LEVEL); kills x the fight lab's seconds per
kill at that level x SEARCH (finding the next mob); collected items over their drop chance; objects SECONDS_PER_OBJECT each; TALK seconds
for each quest's dialogs. Worth: the quest's experience (reduced as in Classic when you are 6+ levels above it) plus its kills' experience,
in minutes at your leveling pace (the planner's minutes_per_level: same-level kills and quests). Listed in three tiers: clear wins,
worth it if you like it (at your pace or better), and for the gear (a reward the gear plan wears: its minutes of faster killing
over the rest of leveling count with the experience). All of it is an estimate: straight lines, Classic positions (Forever moved some quests and added its own,
which have no positions here), and an average leveling pace rather than the route's own.
"""
import csv
import datetime
import json
import math

import item_pool as IP

RUN = 7.0                  # yards a second on foot
MOUNT_SPEED, MOUNT_LEVEL = 1.6, 40   # Classic's first mount: 60% faster
PATH = 1.4                 # straight lines to real paths (terrain, roads, going around camps)
SEARCH = 1.25              # a quest's kills: finding the next mob
SECONDS_PER_OBJECT = 25    # using an object (a chest, a plant): reaching the next one and the cast
TALK = 30                  # seconds of dialog a quest (accept and hand in)
# Three tiers (2026-11-10, user: "I don't necessarily want this to be 100% optimized ... if something is slightly less optimal, but it's
# still fun and somewhat easy to do and makes me stronger and level slightly faster, I'm willing to sacrifice some of the optimization"):
RATIO, MIN_SAVED = 1.2, 3.0            # clear wins: 20% faster than your pace and 3 minutes saved
EASY_RATIO, EASY_SAVED = 1.0, 1.0      # worth it if you like it: at least your pace, a minute saved
GEAR_SAVED = 1.0                       # for the gear: a reward the gear plan wears, its minutes of faster killing paying for the walk
MAX_CHAIN = 6
EXCLUDED_TYPES = {41: "PvP", 62: "raid", 81: "dungeon", 84: "escort"}   # dungeons are planned on their own (plan.dungeon_schedule)
CLASS_SORT = {-61: "warlock", -81: "warrior", -82: "shaman", -141: "paladin", -161: "mage", -162: "rogue", -261: "hunter", -262: "priest",
              -263: "druid"}
RACE_BIT = {"Human": 1, "Orc": 2, "Dwarf": 4, "Night Elf": 8, "Undead": 16, "Tauren": 32, "Gnome": 64, "Troll": 128}
ZERO_DIFF = [(8, 5), (10, 6), (12, 7), (16, 8), (20, 9), (30, 11), (40, 12), (45, 13), (50, 14), (55, 15), (61, 16)]

GEO, SPAWNS, NAMES, MOBLV, ISRC = {}, {}, {}, {}, {}


def load():
    if GEO:
        return
    for r in csv.DictReader(open(IP.RAW / "quest_geo.csv", encoding="utf-8")):
        parse = lambda s: [tuple(x.split(":")) for x in s.split(";") if x]
        GEO[int(r["quest"])] = {"type": int(r["type"]), "flags": int(r["special_flags"]), "prev": int(r["prev"]),
                                "next": int(r["next_in_chain"]), "src_item": int(r["src_item"]), "starts": parse(r["starts"]),
                                "ends": parse(r["ends"]), "objectives": parse(r["objectives"]), "point": r["point"]}
    for r in csv.DictReader(open(IP.RAW / "spawns.csv", encoding="utf-8")):
        k = (r["kind"], int(r["id"]))
        SPAWNS.setdefault(k, []).append((int(r["map"]), float(r["x"]), float(r["y"])))
        NAMES[k] = r["name"]
        if r["kind"] == "c":
            MOBLV[int(r["id"])] = (int(r["level_min"]), int(r["level_max"]))
    for r in csv.DictReader(open(IP.RAW / "quest_item_sources.csv", encoding="utf-8")):
        ISRC.setdefault(int(r["item"]), []).append((r["kind"], int(r["id"]), float(r["chance"])))


def quest_xp(ids, region="us"):
    """{quest id: experience} from Blizzard's quest API for Forever (cached with item_pool.forever_quests' records, a week)."""
    path = IP.HERE / "cache" / f"quests-forever-{region}.json"
    cache = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    today = datetime.date.today()
    stale = lambda v: (today - datetime.date.fromisoformat(v.get("fetched", "2000-01-01"))).days > 7
    todo = [q for q in ids if str(q) not in cache or stale(cache[str(q)])]
    if todo:
        import bnet
        from concurrent.futures import ThreadPoolExecutor
        tok = bnet.token(region)

        def one(q):
            st, js = bnet.get(region, tok, f"/data/wow/quest/{q}", f"static-forever-{region}")
            if st == 200:
                return q, {"title": js.get("title"), "area": (js.get("area") or {}).get("name"), "type": (js.get("type") or {}).get("name"),
                           "faction": ((js.get("requirements") or {}).get("faction") or {}).get("type"),
                           "xp": (js.get("rewards") or {}).get("experience"), "fetched": today.isoformat()}
            return q, {"error": st, "fetched": today.isoformat()}
        with ThreadPoolExecutor(8) as pool:
            for q, v in pool.map(one, todo):
                cache[str(q)] = v
        path.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return {q: (cache.get(str(q)) or {}).get("xp") for q in ids}


def xp_at(xp, ql, L):
    """A quest's experience done at level L: Classic's reduction from 6 levels above it (80, 60, 40, 20, then 10%)."""
    d = L - ql
    return xp * (1.0 if d <= 5 else {6: 0.8, 7: 0.6, 8: 0.4, 9: 0.2}.get(d, 0.1))


def mob_xp(L, ml):
    """A mob's experience for a level-L character (Classic: 45 + 5 x level, more for higher mobs, down to grey by the zero difference)."""
    base = 45 + 5 * L
    if ml >= L:
        return base * (1 + 0.05 * min(ml - L, 4))
    z = next(z for top, z in ZERO_DIFF if L < top)
    return 0.0 if L - ml >= z else base * (1 - (L - ml) / z)


def dist(a, b):
    return math.hypot(a[1] - b[1], a[2] - b[2]) if a[0] == b[0] else math.inf


def nearest(key, p):
    best = None
    for s in SPAWNS.get(key, []):
        if s[0] == p[0] and (best is None or dist(s, p) < dist(best, p)):
            best = s
    return best


def legs(q, cur, inlog, L, tpk, speed):
    """The stops of one quest from point `cur`: [(point, seconds of work, kill experience)], or None when a step has no known place (an
    item starts it, a giver or target off the continents, an item with no known source)."""
    g = GEO[q]
    out = []
    if g["flags"] & 2 and not any(o[0] == "t" for o in g["objectives"]):
        return None   # an escort or a scripted event: no objective to time
    if not inlog:
        st = [p for k, i in g["starts"] if k in "co" for p in [nearest((k, int(i)), cur)] if p]
        if not st:
            return None
        cur = min(st, key=lambda p: dist(p, cur))
        out.append((cur, 0.0, 0.0))
    for ob in g["objectives"]:
        kind, oid = ob[0], int(ob[1])
        n = int(ob[2]) if len(ob) > 2 else 1
        if kind == "c":
            p = nearest(("c", oid), cur)
            if not p:
                return None
            ml = sum(MOBLV.get(oid, (L, L))) / 2
            out.append((p, n * tpk * SEARCH, n * mob_xp(L, ml)))
        elif kind == "o":
            p = nearest(("o", oid), cur)
            if not p:
                return None
            out.append((p, n * SECONDS_PER_OBJECT, 0.0))
        elif kind == "i":
            if oid == g["src_item"]:
                continue
            best = None
            for sk, sid, ch in ISRC.get(oid, []):
                p = nearest((sk, sid), cur)
                if not p or ch <= 0:
                    continue
                tries = n / min(1.0, ch / 100)
                work = tries * (tpk * SEARCH if sk == "c" else SECONDS_PER_OBJECT)
                cost = work + PATH * 2 * dist(cur, p) / speed
                xp = tries * mob_xp(L, sum(MOBLV.get(sid, (L, L))) / 2) if sk == "c" else 0.0
                if best is None or cost < best[0]:
                    best = (cost, p, work, xp)
            if not best:
                return None
            out.append((best[1], best[2], best[3]))
        elif kind == "t":
            if not g["point"]:
                return None
            m, x, y = g["point"].split(":")
            p = (int(m), float(x), float(y))
            if p[0] != cur[0]:
                return None
            out.append((p, 0.0, 0.0))
        cur = out[-1][0] if out else cur
    en = [p for k, i in g["ends"] if k in "co" for p in [nearest((k, int(i)), cur)] if p]
    if not en:
        return None
    out.append((min(en, key=lambda p: dist(p, cur)), 0.0, 0.0))
    return out


def zone_of(p, maps, prefer=None):
    """(zone, x%, y%) of a world point. Neighbouring zones' map rectangles overlap at their edges: the `prefer`red zone when its map holds
    the point (the quest's own zone, the route's), else the map the point lies deepest inside (relative to the map's size: a city inside
    its zone's map lies deeper in the city's)."""
    best = None
    for v in maps.values():
        if v["map"] == p[0] and v["x0"] <= p[1] <= v["x1"] and v["y0"] <= p[2] <= v["y1"] and v["x1"] - v["x0"] < 9000:   # (no continents)
            depth = min((p[1] - v["x0"]) / (v["x1"] - v["x0"]), (v["x1"] - p[1]) / (v["x1"] - v["x0"]),
                        (p[2] - v["y0"]) / (v["y1"] - v["y0"]), (v["y1"] - p[2]) / (v["y1"] - v["y0"]))
            if prefer and v["name"] == prefer and depth >= 0.05:   # (not at its very edge: the Fallen Hero stands in Swamp of Sorrows,
                depth = 1.0                                          # his quest is filed under Blasted Lands)
            if best is None or depth > best[0]:
                best = (depth, v)
    if not best:
        return None
    v = best[1]
    return (v["name"], round(100 * (v["y1"] - p[2]) / (v["y1"] - v["y0"]), 1), round(100 * (v["x1"] - p[1]) / (v["x1"] - v["x0"]), 1))


def find(cfg, snap, lv, RG, pace, tpk, completed, inlog, maps, group=False, last=59, gear_of=None):
    """Detours worth taking, best first within each level: [{"quests": [(id, title)], "level", "xp", "minutes", "saves", "ratio",
    "giver", "start", "near", "travel"}], plus the count of quests scored and of quests with no known place."""
    load()
    gear_of = gear_of or {}
    cq = IP.classic_quests()
    me = RACE_BIT.get(snap["profile"]["race"]["name"], 0)
    cls_bit = 1 << (IP.CLASS_ID[cfg["class"]] - 1)
    on_route = set(RG["quests"]) | RG["past"]
    route_turnin = {q: (v.get("turnin") or {}).get("level") for q, v in RG["quests"].items()}

    def ok(q):
        r, g = cq.get(q), GEO.get(q)
        if not r or not g or q in completed or q in on_route:
            return False
        ql, mn, sort = int(r["quest_level"] or 0), int(r["min_level"] or 0), int(r["zone_or_sort"] or 0)
        rr, rc = int(r["required_races"] or 0), int(r["required_classes"] or 0)
        return (0 < ql <= 62 and ql >= lv - 5 and mn <= last and (not rr or rr & me) and (not rc or rc & cls_bit)
                and g["type"] not in EXCLUDED_TYPES and (g["type"] != 1 or group) and not g["flags"] & 1
                and (sort >= 0 or CLASS_SORT.get(sort) == cfg["class"]))

    def ready(q):   # (the level from which it can be taken) or None: its prerequisite done, in your log, or on the route by then
        p = abs(GEO[q]["prev"])
        if not p or p in completed or p in inlog:
            return 0
        if p in RG["past"]:
            return 0
        return route_turnin.get(p)

    znames = {z["id"]: z["name"] for z in IP.sim_db()["zones"]}
    qzone = lambda q: znames.get(int(cq[q]["zone_or_sort"] or 0)) or IP.ZONE_ALIAS.get(int(cq[q]["zone_or_sort"] or 0))
    def spot_of(q, p):   # the giver's place: the guides' own position for that NPC when they name it, else the quest's zone
        for k, i in GEO[q]["starts"]:
            n = RG["npcs"].get(NAMES.get((k, int(i)), ""))
            if n:
                return (n["zone"], n["x"], n["y"])
        return zone_of(p, maps, qzone(q))

    cands = [q for q in cq if ok(q)]
    judged = {}
    xp = quest_xp(cands)
    heads = [q for q in cands if ready(q) is not None and xp.get(q)]
    path = RG["path"]
    out, unknown = [], 0
    for h in heads:
        chain = [h]
        while len(chain) < MAX_CHAIN:
            nx = GEO[chain[-1]]["next"]
            if not nx or nx in chain or not ok(nx) or not xp.get(nx):
                break
            chain.append(nx)
        r0 = cq[h]
        lmin = max(lv, int(r0["min_level"] or 0), ready(h) or 0)
        best, placed = None, False
        for L in range(lmin, min(last, int(r0["quest_level"]) + 4) + 1):
            speed = RUN * (MOUNT_SPEED if L >= MOUNT_LEVEL else 1.0)
            t = tpk(L)
            route = [(p[1], p[2], p[3], n) for n, p in enumerate(path) if abs(p[0] - L) <= 1]   # (continent, x, y, index on the route)
            for cont in {p[0] for p in route}:
                here = [p for p in route if p[0] == cont]
                lg = legs(h, here[0], h in inlog, L, t, speed)   # where the quest's first stop is, then from the route point nearest to it
                if lg is None:
                    continue
                placed = True
                near = min(here, key=lambda p: dist(p, lg[0][0]))
                stops, work, kxp, gain, cur = [], 0.0, 0.0, 0.0, near
                for k, q in enumerate(chain):
                    lg = legs(q, cur, q in inlog, L, t, speed)
                    if lg is None:
                        break
                    stops += [x[0] for x in lg]
                    work += sum(x[1] for x in lg) + TALK
                    kxp += sum(x[2] for x in lg)
                    gain += xp_at(xp[q], int(cq[q]["quest_level"]), L)
                    cur = stops[-1]
                    # this first part of the chain: from the best route point and back to it
                    rp = min(here, key=lambda p: dist(p, stops[0]) + dist(stops[-1], p))
                    yards = dist(rp, stops[0]) + sum(dist(stops[n], stops[n + 1]) for n in range(len(stops) - 1)) + dist(stops[-1], rp)
                    if math.isinf(yards):
                        break
                    travel = PATH * yards / speed
                    minutes = (travel + work) / 60
                    worth = (gain + kxp) / pace(L)
                    saves, ratio = worth - minutes, worth / max(minutes, 0.1)
                    gq = {gear_of[q2][0]: gear_of[q2][1] for q2 in chain[:k + 1] if q2 in gear_of}   # rewards the gear plan wears
                    gear, gmin = sorted(gq), sum(gq.values())
                    score = saves + gmin
                    if best is None or score > best["score"]:
                        best = {"quests": [(q2, cq[q2]["title"].strip()) for q2 in chain[:k + 1]], "level": L, "xp": round(gain + kxp),
                                "quest_xp": round(gain), "minutes": round(minutes, 1), "travel": round(travel / 60, 1),
                                "saves": round(saves, 1), "ratio": round(ratio, 2), "inlog": h in inlog, "gear": gear, "score": score,
                                "gear_minutes": round(gmin), "anchor": rp[3],
                                "giver": " / ".join(sorted({NAMES.get((kk, int(ii)), "") for kk, ii in GEO[h]["starts"] if kk in "co"} - {""})),
                                "start": spot_of(h, stops[0]), "near": zone_of(rp, maps, path[rp[3]][4])}
        if not placed:
            unknown += 1
        if not best:
            continue
        for q2, _ in best["quests"]:   # the gear plan's quests: their detour as judged, worth it or not (the timeline shows the cost)
            if q2 in gear_of:
                judged[q2] = best
        if best["ratio"] >= RATIO and best["saves"] >= MIN_SAVED:
            best["tier"] = "clear"
        elif best["ratio"] >= EASY_RATIO and best["saves"] >= EASY_SAVED:
            best["tier"] = "easy"
        elif best["gear"] and best["score"] >= GEAR_SAVED:
            best["tier"] = "gear"
        else:
            continue
        out.append(best)
    out.sort(key=lambda d: (d["level"], -d["saves"]))
    return out, {"scored": len(heads), "unknown": unknown, "judged": judged}
