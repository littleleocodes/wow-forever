"""Extract the parts of the CMaNGOS Classic world database the character gear planner needs (2026-11-09, user: "build folders/guides for
my specific characters ... optimizes the gear that I'm getting at each level ... tailoring ... enchanting").

    python -I _reference/data/characters/cmangos_extract.py <ClassicDB_1_12_1_z2815.sql.gz> <out folder>

Source: https://github.com/cmangos/classic-db, Full_DB/ClassicDB_1_12_1_z2815.sql.gz (13 MB; not archived, the CSVs are). Writes:
- trainer_spells.csv: spell, reqskill, reqskillvalue, reqlevel (the lowest over every trainer that teaches it)
- recipe_items.csv: item, name, required_skill, required_rank, teaches (the recipe spell), vendor, drop
- quests.csv: quest, title, zone_or_sort, min_level, quest_level, required_races, required_classes, rewards, choices
- craft_spells.csv: spell, name, creates (item), enchant (item enchantment id), reagents (item:count;...)
- instances.csv: map, level_min, level_max
- item_names.csv: item, name, class, subclass, quality, required_level, required_skill, required_rank
- dungeon_drops.csv, class_training.csv, mob_income.csv (coin and vendor value per kill by level) and mob_loot.csv (level, item, per_kill,
  quality, class, sell: every item a level's mobs drop, expected count per kill), quest_chain.csv (quest, prev, next_in_chain, givers),
  dungeon_quests.csv (quest, map, how: a creature to kill, an item that drops, or a giver in a leveling dungeon)
Classic Era data: WoW: Forever changed some items and recipes; the planner takes item stats and sources from the simulator's Forever
database and only skill levels, quest levels and reagents from here.
"""
import csv
import gzip
import pathlib
import re
import sys

WANT = {"npc_trainer", "npc_trainer_template", "quest_template", "item_template", "spell_template", "npc_vendor", "npc_vendor_template",
        "creature_loot_template", "reference_loot_template", "gameobject_loot_template", "instance_template", "creature_template", "creature",
        "creature_questrelation", "gameobject_questrelation", "gameobject_template", "creature_involvedrelation"}
# the leveling dungeons' map ids (Classic)
DUNGEON_MAPS = {389, 43, 36, 33, 48, 34, 90, 47, 189, 129, 70, 209, 349, 109, 230, 229, 429, 289, 329}


def loot_chances(table, refs, entry, depth=0):
    """{item: chance} of one loot entry: ungrouped rows roll on their own; a group drops one of its rows (rows with chance 0 share what the
    others leave); a negative mincountOrRef is a reference table rolled with the row's chance, maxcount times (CMaNGOS loot rules)."""
    out = {}
    rows = table.get(entry, [])
    groups = {}
    for r in rows:
        groups.setdefault(int(r["groupid"]), []).append(r)
    for g, rs in groups.items():
        fixed = [r for r in rs if float(r["ChanceOrQuestChance"]) != 0]
        equal = [r for r in rs if float(r["ChanceOrQuestChance"]) == 0]
        left = max(0.0, 100.0 - sum(abs(float(r["ChanceOrQuestChance"])) for r in fixed)) if g else 0.0
        for r in rs:
            ch = abs(float(r["ChanceOrQuestChance"])) if float(r["ChanceOrQuestChance"]) != 0 else (left / len(equal) if g and equal else 0.0)
            ch /= 100.0
            ref = int(r["mincountOrRef"])
            if ref < 0 and depth < 3:
                times = max(1, int(r["maxcount"] or 1))
                for it, c in loot_chances(refs, refs, -ref, depth + 1).items():
                    out[it] = 1 - (1 - out.get(it, 0.0)) * (1 - ch * c) ** times
            elif ref >= 0:
                it = int(r["item"])
                out[it] = 1 - (1 - out.get(it, 0.0)) * (1 - ch)
    return out


def rows(values):
    """Tuples of a VALUES list: (...),(...); strings with backslash escapes."""
    i, n = 0, len(values)
    while i < n:
        if values[i] != "(":
            i += 1
            continue
        i += 1
        row, cur, q = [], [], False
        while i < n:
            c = values[i]
            if q:
                if c == "\\" and i + 1 < n:
                    cur.append(values[i + 1])
                    i += 2
                    continue
                if c == "'":
                    q = False
                else:
                    cur.append(c)
            elif c == "'":
                q = True
            elif c == ",":
                row.append("".join(cur))
                cur = []
            elif c == ")":
                row.append("".join(cur))
                i += 1
                break
            else:
                cur.append(c)
            i += 1
        yield row


def load(path):
    cols, data, table = {}, {t: [] for t in WANT}, None
    create = re.compile(r"^CREATE TABLE `([a-z_]+)`")
    colre = re.compile(r"^\s+`([A-Za-z0-9_]+)`")
    insert = re.compile(r"^INSERT INTO `([a-z_]+)`(?: \(([^)]*)\))? VALUES ?(.*)$")
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        for line in f:
            m = create.match(line)
            if m:
                table = m.group(1)
                cols[table] = []
                continue
            if table and line.startswith(")"):
                table = None
                continue
            if table:
                c = colre.match(line)
                if c and table in WANT:
                    cols[table].append(c.group(1))
                continue
            m = insert.match(line)
            if m and m.group(1) in WANT:
                t = m.group(1)
                names = [x.strip(" `") for x in m.group(2).split(",")] if m.group(2) else cols[t]
                for r in rows(m.group(3)):
                    data[t].append(dict(zip(names, r)))
    return data


def write(path, header, items):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(items)
    print(f"  {path.name}: {len(items)} rows")


def main():
    src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    d = load(src)
    print({t: len(v) for t, v in d.items()})
    # trainer recipes: the lowest requirement over every trainer
    tr = {}
    for r in d["npc_trainer"] + d["npc_trainer_template"]:
        sp = int(r["spell"])
        k = (int(r["reqskill"]), int(r["reqskillvalue"]), int(r["reqlevel"]))
        if sp not in tr or k[1] < tr[sp][1]:
            tr[sp] = k
    write(out / "trainer_spells.csv", ["spell", "reqskill", "reqskillvalue", "reqlevel"], sorted([s, *k] for s, k in tr.items()))
    # recipe items (item class 9): the spell they teach and where they come from
    vendor = {int(r["item"]) for r in d["npc_vendor"] + d["npc_vendor_template"]}
    looted = {int(r["item"]) for t in ("creature_loot_template", "reference_loot_template", "gameobject_loot_template") for r in d[t]}
    rec = []
    for r in d["item_template"]:
        if r.get("class") != "9":
            continue
        teaches = next((r[f"spellid_{k}"] for k in (2, 1) if r.get(f"spellid_{k}") not in (None, "0", "483", "55884")), "0")
        rec.append([int(r["entry"]), r["name"], r["RequiredSkill"], r["RequiredSkillRank"], teaches, int(int(r["entry"]) in vendor),
                    int(int(r["entry"]) in looted)])
    write(out / "recipe_items.csv", ["item", "name", "required_skill", "required_rank", "teaches", "vendor", "drop"], sorted(rec))
    # quests
    qs = []
    for r in d["quest_template"]:
        rew = ";".join(f"{r.get(f'RewItemId{k}')}" for k in range(1, 5) if r.get(f"RewItemId{k}") not in (None, "0"))
        cho = ";".join(f"{r.get(f'RewChoiceItemId{k}')}" for k in range(1, 7) if r.get(f"RewChoiceItemId{k}") not in (None, "0"))
        qs.append([int(r["entry"]), r["Title"], r["ZoneOrSort"], r["MinLevel"], r["QuestLevel"], r["RequiredRaces"], r["RequiredClasses"], rew, cho,
                   max(0, int(r.get("RewOrReqMoney") or 0))])
    write(out / "quests.csv", ["quest", "title", "zone_or_sort", "min_level", "quest_level", "required_races", "required_classes", "rewards",
                               "choices", "money"], sorted(qs))
    # crafting and enchanting spells: the item a spell creates (effect 24) or the enchantment it applies (effect 53), and its reagents
    cs = []
    for r in d["spell_template"]:
        eff = [(r.get(f"Effect{k}"), r.get(f"EffectItemType{k}"), r.get(f"EffectMiscValue{k}")) for k in (1, 2, 3)]
        creates = next((it for e, it, _ in eff if e == "24" and it not in (None, "0")), "")
        enchant = next((mv for e, _, mv in eff if e == "53" and mv not in (None, "0")), "")
        if not creates and not enchant:
            continue
        reag = ";".join(f"{r[f'Reagent{k}']}:{r[f'ReagentCount{k}']}" for k in range(1, 9) if r.get(f"Reagent{k}") not in (None, "0"))
        cs.append([int(r["Id"]), r.get("SpellName", ""), creates, enchant, reag])
    write(out / "craft_spells.csv", ["spell", "name", "creates", "enchant", "reagents"], sorted(cs))
    # trainers and recipe items teach a "learn" spell (effect 36) whose trigger spell is the craft spell
    ls = []
    for r in d["spell_template"]:
        for k in (1, 2, 3):
            if r.get(f"Effect{k}") == "36" and r.get(f"EffectTriggerSpell{k}") not in (None, "0"):
                ls.append([int(r["Id"]), int(r[f"EffectTriggerSpell{k}"])])
    write(out / "learn_spells.csv", ["spell", "learns"], sorted(ls))
    write(out / "instances.csv", ["map", "level_min", "level_max"], sorted([int(r["map"]), r["levelMin"], r["levelMax"]] for r in d["instance_template"]))
    # dungeon drops: every creature spawned in a leveling dungeon, each item it drops at 1% or more (green or better, equippable)
    spawned = {}
    for r in d["creature"]:
        if int(r["map"]) in DUNGEON_MAPS:
            spawned.setdefault(int(r["id"]), int(r["map"]))
    cl, rl = {}, {}
    for r in d["creature_loot_template"]:
        cl.setdefault(int(r["entry"]), []).append(r)
    for r in d["reference_loot_template"]:
        rl.setdefault(int(r["entry"]), []).append(r)
    items = {int(r["entry"]): r for r in d["item_template"]}
    rows = []
    for r in d["creature_template"]:
        e = int(r["Entry"])
        if e not in spawned or not int(r.get("LootId") or 0):
            continue
        for it, ch in loot_chances(cl, rl, int(r["LootId"])).items():
            x = items.get(it)
            if ch < 0.01 or not x or int(x["Quality"]) < 2 or x["class"] not in ("2", "4"):
                continue
            rows.append([spawned[e], e, r["Name"], r["Rank"], r["MaxLevel"], it, x["name"], round(ch, 4)])
    write(out / "dungeon_drops.csv", ["map", "creature", "name", "rank", "level", "item", "item_name", "chance"], sorted(rows))
    # class training (2026-11-09, the planner's gold budget: "how much training costs"): every spell a class trainer teaches, its level
    # and price (copper), by class (TrainerType 0 = class trainer; npc_trainer rows by creature, npc_trainer_template rows by template)
    names = {int(r["Id"]): r.get("SpellName", "") for r in d["spell_template"]}
    learns = {int(r["Id"]): int(r[f"EffectTriggerSpell{k}"]) for r in d["spell_template"] for k in (1, 2, 3)
              if r.get(f"Effect{k}") == "36" and r.get(f"EffectTriggerSpell{k}") not in (None, "0")}
    by_creature, by_template = {}, {}
    for r in d["npc_trainer"]:
        by_creature.setdefault(int(r["entry"]), []).append(r)
    for r in d["npc_trainer_template"]:
        by_template.setdefault(int(r["entry"]), []).append(r)
    tr = {}
    for r in d["creature_template"]:
        if r.get("TrainerType") != "0" or int(r.get("TrainerClass") or 0) == 0:
            continue
        cls = int(r["TrainerClass"])
        for t in by_creature.get(int(r["Entry"]), []) + by_template.get(int(r.get("TrainerTemplateId") or 0), []):
            sp = int(t["spell"])
            real = learns.get(sp, sp)
            k = (cls, real)
            row = [cls, real, names.get(real, ""), int(t["reqlevel"]), int(t["spellcost"])]
            if k not in tr or row[4] < tr[k][4]:
                tr[k] = row
    write(out / "class_training.csv", ["class", "spell", "name", "level", "cost"], sorted(tr.values()))
    # mob income by level: coin and the vendor value of gray and white loot per kill, over normal-rank creatures that spawn and fight
    # (no critters, no NPCs with services), weighted by their spawns (the fight lab's mob pool, mob_stats.py, uses the same filter idea)
    spawns = {}
    for r in d["creature"]:
        spawns[int(r["id"])] = spawns.get(int(r["id"]), 0) + 1
    sell = {int(r["entry"]): (int(r["Quality"]), int(r["SellPrice"])) for r in d["item_template"]}
    agg = {}
    for r in d["creature_template"]:
        e = int(r["Entry"])
        n = spawns.get(e, 0)
        if not n or r["Rank"] != "0" or r["CreatureType"] in ("8", "11", "12") or int(r["NpcFlags"] or 0):
            continue
        lv = (int(r["MinLevel"]) + int(r["MaxLevel"])) // 2
        coin = (int(r["MinLootGold"]) + int(r["MaxLootGold"])) / 2
        vend = 0.0
        if int(r.get("LootId") or 0):
            for it, ch in loot_chances(cl, rl, int(r["LootId"])).items():
                q, sp_ = sell.get(it, (9, 0))
                if q <= 1:
                    vend += ch * sp_
        a = agg.setdefault(lv, [0, 0.0, 0.0])
        a[0] += n
        a[1] += coin * n
        a[2] += vend * n
    write(out / "mob_income.csv", ["level", "spawns", "coin_per_kill", "vendor_per_kill"],
          [[lv, a[0], round(a[1] / a[0], 1), round(a[2] / a[0], 1)] for lv, a in sorted(agg.items())])
    # mob loot by level (2026-11-09, the planner's income: cloth and greens sell on the auction house for more than a vendor pays): the
    # expected count per kill of every item a level's mobs drop, same creatures and spawn weights as mob_income: items of 1 in 2,000 kills
    # or more, and every green or better (world drops come one in tens of thousands of kills each, but there are hundreds of them);
    # sell = the vendor's price, quality and class for the planner's valuation
    loot, kills = {}, {}
    for r in d["creature_template"]:
        e = int(r["Entry"])
        n = spawns.get(e, 0)
        if not n or r["Rank"] != "0" or r["CreatureType"] in ("8", "11", "12") or int(r["NpcFlags"] or 0):
            continue
        lv = (int(r["MinLevel"]) + int(r["MaxLevel"])) // 2
        kills[lv] = kills.get(lv, 0) + n
        if int(r.get("LootId") or 0):
            for it, ch in loot_chances(cl, rl, int(r["LootId"])).items():
                loot[(lv, it)] = loot.get((lv, it), 0.0) + ch * n
    klass = {int(r["entry"]): r["class"] for r in d["item_template"]}
    # quest chains and givers (2026-11-09, the planner's "work toward" list: where a reward's chain starts and who gives each step):
    # prev = PrevQuestId's quest (negative in the data when it only has to be active), next_in_chain, the creatures or objects that give it
    cname = {int(r["Entry"]): r["Name"] for r in d["creature_template"]}
    gname = {int(r["entry"]): r["name"] for r in d["gameobject_template"]}
    givers = {}
    for r in d["creature_questrelation"]:
        givers.setdefault(int(r["quest"]), set()).add(cname.get(int(r["id"]), ""))
    for r in d["gameobject_questrelation"]:
        givers.setdefault(int(r["quest"]), set()).add(gname.get(int(r["id"]), ""))
    write(out / "quest_chain.csv", ["quest", "prev", "next_in_chain", "givers"],
          sorted([int(r["entry"]), abs(int(r.get("PrevQuestId") or 0)), int(r.get("NextQuestInChain") or 0),
                  " / ".join(sorted(x for x in givers.get(int(r["entry"]), ()) if x))] for r in d["quest_template"]))
    # dungeon quests (2026-11-09, user: "dungeons are so worth to run at least once. The XP from the dungeon quests is significant"):
    # a quest belongs to a leveling dungeon when a creature it asks you to kill lives there, an item it asks for drops there, or its giver
    # or ender stands there (the quests' own zone often names the city that gives them: Gnomeregan's are filed under Dun Morogh and
    # Ironforge, Razorfen Kraul's under 1717); how = kill, item or giver
    # only what exists nowhere but in leveling dungeons counts (a quest item that also drops outside, such as Westfall Stew's meat, or a
    # creature that also roams outside, does not make a quest a dungeon quest)
    spawn_maps = {}
    for r in d["creature"]:
        spawn_maps.setdefault(int(r["id"]), set()).add(int(r["map"]))
    maps = {c: min(ms & DUNGEON_MAPS) for c, ms in spawn_maps.items() if ms and ms <= DUNGEON_MAPS}
    lootid = {int(r["Entry"]): int(r.get("LootId") or 0) for r in d["creature_template"]}
    item_maps = {}
    for cid, ms in spawn_maps.items():
        if lootid.get(cid):
            for it in loot_chances(cl, rl, lootid[cid]):
                item_maps.setdefault(it, set()).update(ms)
    item_map = {it: min(ms & DUNGEON_MAPS) for it, ms in item_maps.items() if ms and ms <= DUNGEON_MAPS}
    talk = {}
    for t in ("creature_questrelation", "creature_involvedrelation"):
        for r in d[t]:
            if int(r["id"]) in maps:
                talk.setdefault(int(r["quest"]), maps[int(r["id"])])
    dq = []
    for r in d["quest_template"]:
        q = int(r["entry"])
        found = None
        for k in (1, 2, 3, 4):
            c = int(r.get(f"ReqCreatureOrGOId{k}") or 0)
            if c > 0 and c in maps:
                found = (maps[c], "kill")
                break
        if not found:
            for k in (1, 2, 3, 4):
                it = int(r.get(f"ReqItemId{k}") or 0)
                if it and it in item_map:
                    found = (item_map[it], "item")
                    break
        if not found and q in talk:
            found = (talk[q], "giver")
        if found:
            dq.append([q, found[0], found[1]])
    write(out / "dungeon_quests.csv", ["quest", "map", "how"], sorted(dq))
    write(out / "mob_loot.csv", ["level", "item", "per_kill", "quality", "class", "sell"],
          [[lv, it, round(v / kills[lv], 5), sell.get(it, (9, 0))[0], klass.get(it, ""), sell.get(it, (9, 0))[1]]
           for (lv, it), v in sorted(loot.items()) if v / kills[lv] >= 0.0005 or (sell.get(it, (0, 0))[0] >= 2 and v / kills[lv] >= 0.000005)])
    # buy_price: what a vendor charges (copper); vendor: 1 when some vendor sells it (the planner's fallback for vendor-sold reagents,
    # thread, dyes, vials, when the user's ForeverTape export has not seen that vendor yet)
    write(out / "item_names.csv", ["item", "name", "class", "subclass", "quality", "required_level", "required_skill", "required_rank",
                                   "rep_faction", "rep_rank", "buy_price", "vendor"],
          sorted([int(r["entry"]), r["name"], r["class"], r["subclass"], r["Quality"], r["RequiredLevel"], r["RequiredSkill"], r["RequiredSkillRank"],
                  r.get("RequiredReputationFaction", "0"), r.get("RequiredReputationRank", "0"), r.get("BuyPrice", "0"),
                  int(int(r["entry"]) in vendor)] for r in d["item_template"]))


if __name__ == "__main__":
    main()
