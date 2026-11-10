"""Profession plans for a character: the cheapest way to raise a profession with the recipes it knows, at today's auction prices
(2026-11-09, user: "Profession plans ... Tailoring to 145, Enchanting to 200", with the ForeverTape add-on's prices).

Data:
- the recipes the character knows: the user's ForeverTape add-on records them from the open profession windows (F:/wow-addons, the
  duckdb table `recipes`, read only and never between :25 and :30, when its hourly task writes and imports the game's saved file); a copy is kept in
  `_characters/<name>/recipes.json` so a page refresh works while the database is busy. Enchants that make no item are not recorded.
- each recipe's skill-up range in Forever: the client's SkillLineAbility (raw/2026-11-09-wago-1.60.1.70862/): orange below
  TrivialSkillLineRankLow, yellow from it, green from halfway to TrivialSkillLineRankHigh, grey from there. Forever lists 1 as every
  recipe's minimum skill and lets a character learn recipes Classic's trainers held back (Arcea knew Spidersilk Boots, Classic 125, at 106).
- the chance of a skill point: 1 while orange, then (grey - skill) / (grey - yellow) (Classic's rule).
"""
import csv
import datetime
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
SLA = DATA / "raw" / "2026-11-09-wago-1.60.1.70862" / "SkillLineAbility.csv"
LINE = {"Tailoring": 197, "Enchanting": 333, "Cooking": 185, "Alchemy": 171, "First Aid": 129, "Blacksmithing": 164, "Mining": 186}


def thresholds():
    """{recipe spell: (skill line, yellow, grey)}."""
    out = {}
    for r in csv.DictReader(open(SLA, encoding="utf-8")):
        hi = int(r["TrivialSkillLineRankHigh"])
        if hi:
            out[int(r["Spell"])] = (int(r["SkillLine"]), int(r["TrivialSkillLineRankLow"]), hi)
    return out


PROFESSION_ID = {"Tailoring": 197, "Enchanting": 333, "Cooking": 185, "Alchemy": 171, "First Aid": 129, "Blacksmithing": 164,
                 "Leatherworking": 165, "Engineering": 202, "Mining": 186}


def forever_recipes(professions, region="us"):
    """{craft spell: {"recipe", "profession", "item", "reagents": [(item, count)], "yellow"}} for the professions given, from Blizzard's
    Forever API (profession -> skill tiers -> recipes, each with its crafted item and reagents; 2026-11-09: Forever's own recipes, Earthen
    Silk Slippers among them, are missing from the Classic data). A recipe id is a SkillLineAbility id: its spell and skill range come
    from the client table (SLA). Cached in cache/recipes-forever-<region>.json, asked again weekly."""
    path = HERE / "cache" / f"recipes-forever-{region}.json"
    cache = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    today = datetime.date.today()
    todo = [x for x in professions if x in PROFESSION_ID and (x not in cache or (today - datetime.date.fromisoformat(
        cache[x].get("fetched", "2000-01-01"))).days > 7)]
    if todo:
        import bnet
        tok = bnet.token(region)
        ns = f"static-forever-{region}"
        for prof in todo:
            st, js = bnet.get(region, tok, f"/data/wow/profession/{PROFESSION_ID[prof]}", ns)
            if st != 200:
                continue
            ids = []
            for tier in js.get("skill_tiers") or []:
                st, t = bnet.get(region, tok, f"/data/wow/profession/{PROFESSION_ID[prof]}/skill-tier/{tier['id']}", ns)
                for cat in (t.get("categories") or []) if st == 200 else []:
                    ids += [r["id"] for r in cat.get("recipes") or []]
            old = (cache.get(prof) or {}).get("recipes") or {}
            rec = {}

            def one(rid):
                return rid, bnet.get(region, tok, f"/data/wow/recipe/{rid}", ns)

            from concurrent.futures import ThreadPoolExecutor
            with ThreadPoolExecutor(8) as pool:   # about 470 recipes for Tailoring: eight at a time
                for rid, (st, x) in pool.map(one, ids):
                    if st == 200:
                        rec[str(rid)] = {"name": x.get("name"), "item": (x.get("crafted_item") or {}).get("id"),
                                         "reagents": [[g["reagent"]["id"], g["quantity"]] for g in x.get("reagents") or []]}
                    elif str(rid) in old:   # a failed read keeps last week's copy
                        rec[str(rid)] = old[str(rid)]
            cache[prof] = {"fetched": today.isoformat(), "recipes": rec}
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps(cache, separators=(",", ":")) + "\n", encoding="utf-8")   # saved after each profession
    sla = {int(r["ID"]): (int(r["Spell"]), int(r["TrivialSkillLineRankLow"])) for r in csv.DictReader(open(SLA, encoding="utf-8"))}
    out = {}
    for prof in professions:
        for rid, r in ((cache.get(prof) or {}).get("recipes") or {}).items():
            if int(rid) in sla:
                spell, yellow = sla[int(rid)]
                out[spell] = {"recipe": int(rid), "profession": prof, "name": r["name"], "item": r["item"],
                              "reagents": [tuple(g) for g in r["reagents"]], "yellow": yellow}
    return out


def known_recipes(char, duckdb_path, cache):
    """[{profession, spell, name, out_item, reagents: [(item, count)]}] of the character's known recipes; from the add-on's database when
    it can be read now, else the last copy."""
    cache = pathlib.Path(cache)
    m = datetime.datetime.now().minute
    if duckdb_path and pathlib.Path(duckdb_path).exists() and not 25 <= m <= 30:
        try:
            import duckdb
            con = duckdb.connect(str(duckdb_path), read_only=True)
            try:
                rows = con.execute("select profession, recipe_key, name, out_item, reagents from recipes where char_key like ?",
                                   [f"{char}-%"]).fetchall()
            finally:
                con.close()
            out = []
            for prof, key, name, item, reag in rows:
                if not (key or "")[:1] in ("r", "e") or not key[1:].isdigit():   # "r<spell>" (modern window), "e<spell>" (classic window, enchants)
                    continue
                rg = [(int(a), int(b)) for a, b in (x.split(":") for x in (reag or "").split(",") if ":" in x)]
                out.append({"profession": prof, "spell": int(key[1:]), "name": name, "out_item": item, "reagents": rg})
            cache.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            return out
        except Exception as e:   # noqa: BLE001   (a lock held by the add-on's writer: the last copy)
            print(f"  recipes: the add-on database could not be read ({type(e).__name__}); using the last copy")
    return json.loads(cache.read_text(encoding="utf-8")) if cache.exists() else []


def chance(yellow, grey, skill):
    if skill >= grey:
        return 0.0
    if skill < yellow:
        return 1.0
    return (grey - skill) / max(1, grey - yellow)


def color(yellow, grey, skill):
    if skill >= grey:
        return "grey"
    if skill < yellow:
        return "orange"
    return "yellow" if skill < (yellow + grey) / 2 else "green"


def skill_plan(prof, skill, target, known, tri, price, sell=None):
    """Cheapest expected path from `skill` to `target` with the known recipes: per skill point the recipe with the lowest expected
    material cost per point (cost / chance). [(from, to, recipe, crafts, cost)] grouped by recipe, the skill where it stops (no known
    recipe gives points), and the material count {item: n} of the whole path. With `sell` (item -> what one sells for after the auction
    cut, None when unknown) the cost is net of selling what the craft makes: the path then favors recipes whose product sells."""
    line = LINE.get(prof)
    rec = [r for r in known if tri.get(r["spell"], (None,))[0] == line]
    cost, back = {}, {}
    for r in rec:
        c = 0.0
        for item, n in r["reagents"]:
            p = price(item)
            if p is None:
                c = None
                break
            c += p * n
        cost[r["spell"]] = c
        # what selling the product brings back, for the first `limit` made only: a market takes a few, not 60 pairs of boots
        b = sell(r["out_item"]) if sell and r.get("out_item") else None
        back[r["spell"]] = b if b and b[0] else (0.0, 0)
    made = {r["spell"]: 0.0 for r in rec}
    steps, s = [], skill
    while s < target:
        best = None
        for r in rec:
            y, g = tri[r["spell"]][1], tri[r["spell"]][2]
            p = chance(y, g, s)
            if p <= 0 or cost[r["spell"]] is None:
                continue
            n = 1 / p
            value, limit = back[r["spell"]]
            sold = max(0.0, min(n, limit - made[r["spell"]]))
            e = cost[r["spell"]] * n - value * sold   # below zero when selling what it makes pays more than its materials (2026-11-09:
                                                      # Spidersilk Boots made money and read "0c")
            if best is None or e < best[0]:
                best = (e, r, n)
        if best is None:
            break
        steps.append((s, best[1], best[2], best[0]))
        made[best[1]["spell"]] += best[2]
        s += 1
    groups, mats = [], {}
    for s0, r, crafts, c in steps:
        if groups and groups[-1][2]["spell"] == r["spell"]:
            g = groups[-1]
            groups[-1] = (g[0], s0 + 1, r, g[3] + crafts, g[4] + c)
        else:
            groups.append((s0, s0 + 1, r, crafts, c))
        for item, n in r["reagents"]:
            mats[item] = mats.get(item, 0) + n * crafts
    return groups, s, mats
