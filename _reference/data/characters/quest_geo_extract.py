"""Where every quest happens, from the CMaNGOS Classic world database (2026-11-10, user: "use the current RestedXP guide and route to help me
decide when I should pick up quests that are detours ... that aren't included in RestedXP, but that we deem are still worth it because
of the time they save"): who starts and ends each quest, what it asks for, and where those NPCs, mobs and objects stand.

    python -I _reference/data/characters/quest_geo_extract.py <ClassicDB_1_12_1_z2815.sql.gz> <out folder>

Source: https://github.com/cmangos/classic-db at c33f90b8e, Full_DB/ClassicDB_1_12_1_z2815.sql.gz (the dump cmangos_extract.py reads; not
archived, the CSVs are). Writes:
- quest_geo.csv: quest, type (QuestInfo: 1 elite, 41 PvP, 62 raid, 81 dungeon, 84 escort), special_flags (1 repeatable, 2 an event or
  exploration objective), method, prev, next_in_chain, exclusive_group, src_item (given when you accept), starts (c:<creature> / o:<object> /
  i:<item that starts it>, ";"-joined), ends (c:/o:), objectives (c:<creature>:<count> kill or talk, o:<object>:<count> use,
  i:<item>:<count> collect, t:<areatrigger> explore), point (the quest's map point: map:x:y, or "")
- quest_item_sources.csv: item, kind (c creature / o object), id, chance (percent per kill or per object; quest drops as positive), map
  (where it spawns: 0 and 1 the continents, else a dungeon's map); objective items and the items that start a quest
- source_names.csv: kind, id, name of every creature and object in quest_item_sources.csv (dungeon bosses included)
- spawns.csv: kind, id, name, level_min, level_max (creatures), map, x, y: every spawn of the creatures and objects quest_geo.csv names (start, end, objective, item source), on
  the two continents (maps 0 and 1; dungeons are planned elsewhere). World coordinates: x north, y west (uimap_bounds.json converts).
Classic Era data: WoW: Forever moved or changed some quests; its own quests are not in it (the RestedXP guides give those positions).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cmangos_extract as CE  # noqa: E402


def main():
    src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    CE.WANT.clear()
    CE.WANT.update({"quest_template", "creature", "gameobject", "creature_template", "gameobject_template", "creature_loot_template",
                    "gameobject_loot_template", "creature_questrelation", "creature_involvedrelation", "gameobject_questrelation",
                    "gameobject_involvedrelation", "item_template", "areatrigger_involvedrelation"})
    d = CE.load(src)
    starts, ends = {}, {}
    for t, kind, dst in (("creature_questrelation", "c", starts), ("gameobject_questrelation", "o", starts),
                         ("creature_involvedrelation", "c", ends), ("gameobject_involvedrelation", "o", ends)):
        for r in d[t]:
            dst.setdefault(int(r["quest"]), []).append(f"{kind}:{int(r['id'])}")
    start_items = set()
    for r in d["item_template"]:
        if int(r.get("startquest") or 0):
            starts.setdefault(int(r["startquest"]), []).append(f"i:{int(r['entry'])}")
            start_items.add(int(r["entry"]))
    explore = {}
    for r in d["areatrigger_involvedrelation"]:
        explore.setdefault(int(r["quest"]), []).append(int(r["id"]))
    rows, want_c, want_o, want_items = [], set(), set(), set()
    for r in d["quest_template"]:
        q = int(r["entry"])
        obj = []
        for k in range(1, 5):
            c, n = int(r.get(f"ReqCreatureOrGOId{k}") or 0), int(r.get(f"ReqCreatureOrGOCount{k}") or 0)
            if c > 0:
                obj.append(f"c:{c}:{n}")
                want_c.add(c)
            elif c < 0:
                obj.append(f"o:{-c}:{n}")
                want_o.add(-c)
            it, n = int(r.get(f"ReqItemId{k}") or 0), int(r.get(f"ReqItemCount{k}") or 0)
            if it:
                obj.append(f"i:{it}:{n}")
                want_items.add(it)
        obj += [f"t:{a}" for a in explore.get(q, [])]
        for x in starts.get(q, []) + ends.get(q, []):
            k, i = x.split(":")
            (want_c if k == "c" else want_o if k == "o" else set()).add(int(i))
        pm = int(r.get("PointMapId") or 0)
        point = f"{pm}:{float(r['PointX']):.1f}:{float(r['PointY']):.1f}" if float(r.get("PointX") or 0) or float(r.get("PointY") or 0) else ""
        rows.append([q, int(r.get("Type") or 0), int(r.get("SpecialFlags") or 0), int(r.get("Method") or 0), int(r.get("PrevQuestId") or 0),
                     int(r.get("NextQuestInChain") or 0), int(r.get("ExclusiveGroup") or 0), int(r.get("SrcItemId") or 0),
                     ";".join(starts.get(q, [])), ";".join(ends.get(q, [])), ";".join(obj), point])
    CE.write(out / "quest_geo.csv", ["quest", "type", "special_flags", "method", "prev", "next_in_chain", "exclusive_group", "src_item",
                                     "starts", "ends", "objectives", "point"], sorted(rows))
    # where the collected items come from: creature loot (by the creature's LootId) and object loot (a chest's data1)
    by_loot = {}
    for r in d["creature_template"]:
        if int(r.get("LootId") or 0):
            by_loot.setdefault(int(r["LootId"]), []).append(int(r["Entry"]))
    go_loot = {}
    for r in d["gameobject_template"]:
        if int(r.get("type") or -1) in (3, 25) and int(r.get("data1") or 0):   # a chest or a fishing hole: data1 is its loot id
            go_loot.setdefault(int(r["data1"]), []).append(int(r["entry"]))
    want_items |= start_items   # where a chain's first item drops (2026-11-10: The Unsent Letter, Edwin VanCleef in The Deadmines)
    cmap, omap = {}, {}
    for r in d["creature"]:
        cmap.setdefault(int(r["id"]), int(r["map"]))
    for r in d["gameobject"]:
        omap.setdefault(int(r["id"]), int(r["map"]))
    src = []
    for r in d["creature_loot_template"]:
        it = int(r["item"])
        if it in want_items and int(r.get("mincountOrRef") or 0) >= 0:
            for c in by_loot.get(int(r["entry"]), []):
                src.append([it, "c", c, round(abs(float(r["ChanceOrQuestChance"] or 0)), 3), cmap.get(c, -1)])
                want_c.add(c)
    for r in d["gameobject_loot_template"]:
        it = int(r["item"])
        if it in want_items and int(r.get("mincountOrRef") or 0) >= 0:
            for o in go_loot.get(int(r["entry"]), []):
                src.append([it, "o", o, round(abs(float(r["ChanceOrQuestChance"] or 0)), 3) or 100.0, omap.get(o, -1)])
                want_o.add(o)
    CE.write(out / "quest_item_sources.csv", ["item", "kind", "id", "chance", "map"], sorted(src))
    nm = {("c", int(r["Entry"])): r["Name"] for r in d["creature_template"]}
    nm.update({("o", int(r["entry"])): r["name"] for r in d["gameobject_template"]})
    CE.write(out / "source_names.csv", ["kind", "id", "name"], sorted([k, i, nm.get((k, i), "")] for k, i in {(x[1], x[2]) for x in src}))
    names = {("c", int(r["Entry"])): r["Name"] for r in d["creature_template"]}
    names.update({("o", int(r["entry"])): r["name"] for r in d["gameobject_template"]})
    levels = {int(r["Entry"]): (int(r.get("MinLevel") or 0), int(r.get("MaxLevel") or 0)) for r in d["creature_template"]}
    sp = []
    for t, kind, want in (("creature", "c", want_c), ("gameobject", "o", want_o)):
        for r in d[t]:
            i, m = int(r["id"]), int(r["map"])
            if i in want and m in (0, 1):
                lo, hi = levels.get(i, (0, 0)) if kind == "c" else (0, 0)
                sp.append([kind, i, names.get((kind, i), ""), lo, hi, m, round(float(r["position_x"]), 1), round(float(r["position_y"]), 1)])
    CE.write(out / "spawns.csv", ["kind", "id", "name", "level_min", "level_max", "map", "x", "y"], sorted(sp))
    print(f"{len(rows)} quests, {len(src)} item sources, {len(sp)} spawns")


if __name__ == "__main__":
    main()
