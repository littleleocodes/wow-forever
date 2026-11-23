"""Bind types, race masks and the other faction's item for the gear lists (2026-11-22; the user: "All BoE's should also count if you can
buy off the AH"; "one-faction items show the other faction's alternative", the audit session's sixth reading, accepted by the user).

    python _reference/data/raidsim/bind_types.py --extract-cmangos ~/.wow-forever-tools/cmangos/ClassicDB.sql.gz
    python _reference/data/raidsim/bind_types.py --extract-client ~/.wow-forever-tools/wago/ItemSparse-1.60.1.70938.csv --build 1.60.1.70938
    python _reference/data/raidsim/bind_types.py --compare        # the two sources against each other, over the simulator's items

Two sources, both archived under raw/:
- the client's ItemSparse (wago.tools' DB2 export; the full table stays in ~/.wow-forever-tools/wago/, this keeps the columns below for
  the simulator database's items): `Bonding` (0 none, 1 when picked up, 2 when equipped, 3 when used, 4 quest item), `AllowableRace_0`
  (a race mask, -1 or 0 every race), `OppositeFactionItemID` (the other faction's version of the item), `RequiredHoliday` (an event),
  `MinFactionID` / `MinReputation` (a reputation the item asks for: 4 Friendly, 5 Honored, 6 Revered, 7 Exalted);
- Classic's item_template (CMaNGOS classic-db, the dump the character planner's CSVs come from): `bonding` (the same numbers) and
  `AllowableRace`.
Forever's client wins where both have the item: it is the game's own data. `--compare` counts the items where the two disagree.
"""
import argparse
import csv
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CMANGOS = ROOT / "_reference/data/raw/2026-11-09-cmangos-classic-db-c33f90b8e"
CLIENT = ROOT / "_reference/data/raw/2026-11-22-wago-1.60.1.70938"
CLIENT_COLS = ("ID", "Bonding", "AllowableRace_0", "OppositeFactionItemID", "RequiredHoliday", "MinFactionID", "MinReputation")
ALLIANCE_RACES = 1 | 4 | 8 | 64      # Human, Dwarf, Night Elf, Gnome
HORDE_RACES = 2 | 16 | 32 | 128      # Orc, Undead, Tauren, Troll
BIND = {0: "none", 1: "BoP", 2: "BoE", 3: "BoU", 4: "quest"}
_CACHE = {}


def sim_item_ids():
    sys.path[:0] = [str(HERE)]
    import setup
    db = json.load(open(pathlib.Path(setup.checkout()) / "assets" / "database" / "db.json", encoding="utf-8"))
    return {it["id"] for it in db["items"]}


def extract_cmangos(dump):
    spec = importlib.util.spec_from_file_location("cmangos_extract", ROOT / "_reference/data/characters/cmangos_extract.py")
    cx = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cx)
    cx.WANT = {"item_template", "quest_template", "npc_vendor", "conditions"}
    d = cx.load(pathlib.Path(dump))
    # (2026-11-23) a vendor's reputation gate: Classic's dump puts the Warsong Gulch quartermasters' standings in npc_vendor.condition_id
    # (conditions type 5, CONDITION_REPUTATION_RANK_MIN: value1 faction, value2 rank, one per side under an OR), not in item_template
    # (Caretaker's Cape: OR(889 >= 5, 890 >= 5)). Every type-5 leaf under an item's vendor conditions (NOT branches left out); the
    # highest rank when they differ (the audit session's rule for two lines).
    cond = {int(r["condition_entry"]): r for r in d["conditions"]}

    def leaves(cid, seen=()):
        r = cond.get(cid)
        if not r or cid in seen:
            return []
        t, v = int(r["type"]), [int(r[f"value{k}"] or 0) for k in (1, 2, 3, 4)]
        if t == 5:
            return [(v[0], v[1])]
        if t in (-1, -2):   # AND, OR of other conditions
            return [x for c in v if c for x in leaves(c, seen + (cid,))]
        return []
    vrep = {}
    for r in d["npc_vendor"]:
        for f, rank in leaves(int(r.get("condition_id") or 0)):
            it = int(r["item"])
            cur = vrep.get(it)
            if not cur or rank > cur[1]:
                vrep[it] = (f, rank, {f} | (cur[2] if cur else set()))
            else:
                cur[2].add(f)
    out = CMANGOS / "vendor_rep.csv"
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item", "rep_faction", "rep_rank", "factions"])
        w.writerows(sorted((it, fa, rk, "|".join(str(x) for x in sorted(fs))) for it, (fa, rk, fs) in vrep.items()))
    print(f"{out.relative_to(ROOT)}: {len(vrep)} vendor items behind a reputation condition")
    # (2026-11-23) RequiredReputationFaction / Rank too: the client's MinReputation is empty on items that ask a standing (Don Julio's
    # Band asks Exalted with Stormpike Guard or Frostwolf Clan; the audit session from Wowhead's Forever tooltip)
    rows = sorted((int(r["entry"]), int(r.get("bonding") or 0), int(r.get("AllowableRace") or -1), int(r.get("RequiredReputationFaction") or 0),
                   int(r.get("RequiredReputationRank") or 0)) for r in d["item_template"])
    out = CMANGOS / "item_bonding.csv"
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item", "bonding", "allowable_race", "rep_faction", "rep_rank"])
        w.writerows(rows)
    print(f"{out.relative_to(ROOT)}: {len(rows)} items")
    # a quest's reputation requirement (2026-11-23: Alterac Valley's insignia quests ask Honored to Exalted; Easy Pre-BiS stops at
    # Honored): RequiredMinRepValue is a raw value (3,000 Friendly, 9,000 Honored, 21,000 Revered, 42,000 Exalted)
    qs = sorted((int(r["entry"]), int(r.get("RequiredMinRepFaction") or 0), int(r.get("RequiredMinRepValue") or 0))
                for r in d["quest_template"] if int(r.get("RequiredMinRepFaction") or 0))
    out = CMANGOS / "quest_rep.csv"
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["quest", "rep_faction", "rep_min"])
        w.writerows(qs)
    print(f"{out.relative_to(ROOT)}: {len(qs)} quests with a reputation requirement")


def extract_client(path, build):
    keep = sim_item_ids()
    out_dir = ROOT / f"_reference/data/raw/2026-11-22-wago-{build}"
    out_dir.mkdir(parents=True, exist_ok=True)
    n = 0
    with open(path, encoding="utf-8") as f, open(out_dir / "ItemSparse-bind.csv", "w", encoding="utf-8", newline="") as g:
        r = csv.DictReader(f)
        w = csv.writer(g)
        w.writerow(CLIENT_COLS)
        for row in r:
            if int(row["ID"]) in keep:
                w.writerow([row[c] for c in CLIENT_COLS])
                n += 1
    print(f"{(out_dir / 'ItemSparse-bind.csv').relative_to(ROOT)}: {n} of the simulator database's {len(keep)} items")


CLIENT_REAGENTS = ROOT / "_reference/data/raw/2026-11-23-wago-1.60.1.71037"
WOWHEAD_REP = ROOT / "_reference/data/raw/2026-11-23-wowhead-forever-item-rep"   # the fourth standing source (gear_lists.standing)
_REAG = {}


def extract_reagents(reagents_csv, effects_csv, build):
    """The client's reagents of every spell that makes an item of the simulator's database (2026-11-23, the audit session: Forever's own
    recipes are unknown to Classic's dump, and 97 of them take Malleable Essence of Nature, disenchanted from the new raids' items):
    SpellReagents (Reagent_0-7, ReagentCount_0-7) joined to SpellEffect's create-item effects (24). Writes SpellReagents-crafts.csv:
    spell, creates, reagents ("item:count;...")."""
    keep = sim_item_ids()
    creates = {}
    for r in csv.DictReader(open(effects_csv, encoding="utf-8")):
        if r["Effect"] == "24" and int(r["EffectItemType"] or 0) in keep:
            creates[int(r["SpellID"])] = int(r["EffectItemType"])
    import setup   # the database's own recipe spells too (a create effect the client lacks for the item)
    for it in json.load(open(pathlib.Path(setup.checkout()) / "assets" / "database" / "db.json", encoding="utf-8"))["items"]:
        for s in it.get("sources") or []:
            sp = int((s.get("crafted") or {}).get("spellId") or 0)
            if sp and sp not in creates:
                creates[sp] = it["id"]
    out_dir = ROOT / f"_reference/data/raw/2026-11-23-wago-{build}"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for r in csv.DictReader(open(reagents_csv, encoding="utf-8")):
        sp = int(r["SpellID"])
        if sp in creates:
            rs = [f"{int(r[f'Reagent_{k}'])}:{int(r[f'ReagentCount_{k}'])}" for k in range(8) if int(r[f"Reagent_{k}"] or 0)]
            rows.append((sp, creates[sp], ";".join(rs)))
    with open(out_dir / "SpellReagents-crafts.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["spell", "creates", "reagents"])
        w.writerows(sorted(rows))
    print(f"{(out_dir / 'SpellReagents-crafts.csv').relative_to(ROOT)}: {len(rows)} crafting spells of {len(set(creates.values()))} items")


STANDING_RANK = {"Neutral": 3, "Friendly": 4, "Honored": 5, "Revered": 6, "Exalted": 7}


def wowhead_rep(iid):
    """(item, [(faction name, standing)]) from Wowhead's Forever item tooltip ("Requires <faction> - <standing>"); as live_spells.py
    fetches Wowhead's spell tooltips (the same endpoint family, user agent and timeout)."""
    import html
    import re
    import urllib.request
    req = urllib.request.Request(f"https://nether.wowhead.com/forever/tooltip/item/{iid}", headers={"User-Agent": "wow-forever-planner"})
    try:
        js = json.loads(urllib.request.urlopen(req, timeout=25).read())
    except Exception:  # noqa: BLE001
        return iid, None
    text = html.unescape(re.sub(r"<[^>]+>", "\n", js.get("tooltip") or ""))
    return iid, re.findall(r"Requires ([^\n]+?) - (Neutral|Friendly|Honored|Revered|Exalted)", text)


def pull_wowhead_rep(ids):
    """The fourth standing source (2026-11-23, the audit session): Wowhead's Forever tooltips for the items no other source gives a
    standing, archived in WOWHEAD_REP/tooltip_rep.csv (item, factions, rep_rank: one standing when the lines agree, else the higher);
    the make reads the archive, never the site."""
    from concurrent.futures import ThreadPoolExecutor
    WOWHEAD_REP.mkdir(parents=True, exist_ok=True)
    p = WOWHEAD_REP / "tooltip_rep.csv"
    have = {int(r["item"]): r for r in csv.DictReader(open(p, encoding="utf-8"))} if p.exists() else {}
    with ThreadPoolExecutor(3) as pool:
        for iid, reqs in pool.map(wowhead_rep, sorted(set(ids))):
            if reqs is None:
                print(f"  {iid}: no answer")
                continue
            rank = max((STANDING_RANK[s] for _, s in reqs), default="")
            have[iid] = {"item": iid, "factions": "|".join(f for f, _ in reqs), "rep_rank": rank}
            print(f"  {iid}: {reqs or 'no reputation line'}")
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["item", "factions", "rep_rank"])
        w.writeheader()
        w.writerows(have[i] for i in sorted(have))
    print(f"{p.relative_to(ROOT)}: {len(have)} items")


def reagents():
    """({spell: {reagent item ids}}, {item: [spells that make it]}) from the client (CLIENT_REAGENTS)."""
    if not _REAG:
        by_spell, by_item = {}, {}
        for r in csv.DictReader(open(CLIENT_REAGENTS / "SpellReagents-crafts.csv", encoding="utf-8")):
            sp, it = int(r["spell"]), int(r["creates"])
            by_spell[sp] = {int(x.split(":")[0]) for x in r["reagents"].split(";") if x}
            by_item.setdefault(it, []).append(sp)
        _REAG.update(spell=by_spell, item=by_item)
    return _REAG["spell"], _REAG["item"]


def load():
    """{item id: {"client": bind or None, "classic": bind or None, "bind": the client's else Classic's, "races": mask or None,
    "opposite": item id or 0, "holiday": id or 0, "min_faction": id or 0, "min_rep": rank or 0}}."""
    if _CACHE:
        return _CACHE
    for row in csv.DictReader(open(CMANGOS / "item_bonding.csv", encoding="utf-8")):
        _CACHE[int(row["item"])] = {"classic": int(row["bonding"]), "classic_races": int(row["allowable_race"]),
                                    "classic_rep_faction": int(row.get("rep_faction") or 0), "classic_rep_rank": int(row.get("rep_rank") or 0)}
    if (CMANGOS / "vendor_rep.csv").exists():
        for row in csv.DictReader(open(CMANGOS / "vendor_rep.csv", encoding="utf-8")):
            _CACHE.setdefault(int(row["item"]), {}).update(vendor_rep_faction=int(row["rep_faction"]), vendor_rep_rank=int(row["rep_rank"]))
    if (WOWHEAD_REP / "tooltip_rep.csv").exists():
        for row in csv.DictReader(open(WOWHEAD_REP / "tooltip_rep.csv", encoding="utf-8")):
            if row["rep_rank"]:
                _CACHE.setdefault(int(row["item"]), {}).update(wowhead_rep_faction=row["factions"], wowhead_rep_rank=int(row["rep_rank"]))
    for row in csv.DictReader(open(CLIENT / "ItemSparse-bind.csv", encoding="utf-8")):
        e = _CACHE.setdefault(int(row["ID"]), {})
        e.update(client=int(row["Bonding"]), races=int(row["AllowableRace_0"]), opposite=int(row["OppositeFactionItemID"] or 0),
                 holiday=int(row["RequiredHoliday"] or 0), min_faction=int(row["MinFactionID"] or 0), min_rep=int(row["MinReputation"] or 0))
    for e in _CACHE.values():
        e["bind"] = e["client"] if e.get("client") is not None else e.get("classic")
        e.setdefault("races", e.get("classic_races"))
    return _CACHE


def bind_of(iid):
    return BIND.get((load().get(iid) or {}).get("bind"))


def race_faction(mask):
    """"Alliance" or "Horde" when a race mask holds only one faction's races; None for every race (-1, 0) or both."""
    if mask is None or mask <= 0:
        return None
    a, h = bool(mask & ALLIANCE_RACES), bool(mask & HORDE_RACES)
    return "Alliance" if a and not h else "Horde" if h and not a else None


def compare(ids=None):
    """(counts, [(item id, client bind, Classic bind)]) over the items both sources hold (ids: limit to these)."""
    d = load()
    dis, both, only_client, only_classic = [], 0, 0, 0
    for iid, e in sorted(d.items()):
        if ids is not None and iid not in ids:
            continue
        c, k = e.get("client"), e.get("classic")
        if c is None and k is None:
            continue
        if c is None:
            only_classic += 1
        elif k is None:
            only_client += 1
        else:
            both += 1
            if c != k:
                dis.append((iid, BIND.get(c, c), BIND.get(k, k)))
    return {"both": both, "client_only": only_client, "classic_only": only_classic, "disagree": len(dis)}, dis


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extract-cmangos")
    ap.add_argument("--extract-client")
    ap.add_argument("--extract-reagents", nargs=2, metavar=("SPELLREAGENTS_CSV", "SPELLEFFECT_CSV"))
    ap.add_argument("--pull-wowhead-rep", nargs="+", type=int, metavar="ITEM", help="archive Wowhead's Forever tooltip standings of these items")
    ap.add_argument("--build")
    ap.add_argument("--compare", action="store_true")
    a = ap.parse_args()
    if a.extract_cmangos:
        extract_cmangos(a.extract_cmangos)
    if a.extract_client:
        extract_client(a.extract_client, a.build)
    if a.extract_reagents:
        extract_reagents(a.extract_reagents[0], a.extract_reagents[1], a.build)
    if a.pull_wowhead_rep:
        pull_wowhead_rep(a.pull_wowhead_rep)
    if a.compare:
        ids = sim_item_ids()
        counts, dis = compare(ids)
        print(json.dumps(counts))
        kinds = {}
        for _, c, k in dis:
            kinds[(c, k)] = kinds.get((c, k), 0) + 1
        print("client / Classic:", ", ".join(f"{c} / {k}: {n}" for (c, k), n in sorted(kinds.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
