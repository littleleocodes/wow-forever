"""Links for the gear-tier sets (2026-10-03, user request: "is there any way to create an armory or link of sorts so that the pre-bis
and bis gear have a way to see the actual items?").

    python _reference/data/raidsim/gear_links.py [classes] [--write]

For every damage spec's pre-BiS and phase-1 BiS set (the machine-learning records, raidsim/ml/): each item and enchant with its Wowhead
Forever link (www.wowhead.com/forever, the database the simulator's own UI links to), its item level and where it comes from (the boss
and zone, the profession, the quest or the vendor; the simulator's item database), and the whole character as a share link for the
official simulator's live web UI (wowsims.com/forever since 2026-10-22; a spec page is `/forever/<class>/<spec>/`, ui/app/spec_entry.tsx):
the set, the talents the pages show for that tier and setting (ml_builds.shown), the setting's rotation, consumables, buffs and
encounter, exactly as our runs simulate them, encoded by foreverbench's "link" mode the way the UI's "copy link" does
(ui/features/import-export/exporters/link.ts: IndividualSimSettings, zlib, base64 in the URL hash). The site reads links of its own proto
version and older; links carry our simulator copy's version (proto/common.proto `current_version_number`: 2 in the official repository at
09e7398). Until 2026-10-18 the links went to the ElliotWood/Forever fork's GitHub Pages (elliotwood.github.io/Forever, proto version 18),
which is gone with the fork; links in a gear-links.json written before then no longer open.
--write: raidsim/gear-links.json, read by render_modes.py (raid pages), ml_builds.py --rank (_reference/dps-rankings.md) and the ranking
page.
"""
import argparse
import datetime
import importlib.util
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


A = _load("apl_opt_links", HERE / "apl_opt.py")
R = A.R
MADE = set(_load("gear_opt_links", HERE / "gear_opt.py").PHASE1_RAID_MADE)   # (2026-11-22: raid materials' crafts, for DB.raid)
MB = _load("ml_builds_links", HERE / "ml_builds.py")
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
OUT = HERE / "gear-links.json"
SITE = "https://wowsims.com/forever"   # the official simulator's web UI (vite base /forever/); the fork's elliotwood.github.io/Forever/forever until 2026-10-18
WOWHEAD = "https://www.wowhead.com/forever"
KEYS = ("dungeon-raid", "prebis-raid", "bis-raid", "prebis-dummy", "bis-dummy")   # (dungeon-raid: raidsim/dungeon_tier.py, 2026-11-18)
TODAY = datetime.date.today().isoformat()


def resolve(path):
    p = pathlib.Path(path)
    return p if p.is_absolute() else ROOT / p


def api_version(repo):
    m = re.search(r"option [(]current_version_number[)] = ([0-9]+);", (repo / "proto" / "common.proto").read_text(encoding="utf-8"))
    return int(m.group(1)) if m else 0


def professions(repo):
    """{number: name} of the proto's Profession enum (Blacksmithing, Leatherworking ...)."""
    txt = (repo / "proto" / "common.proto").read_text(encoding="utf-8")
    m = re.search(r"enum Profession [{]([^}]*)[}]", txt)
    split = lambda n: re.sub("([a-z])([A-Z])", lambda x: x.group(1) + " " + x.group(2), n)   # noqa: E731
    return {int(n): split(name) for name, n in re.findall(r"([A-Za-z]+) = ([0-9]+);", m.group(1) if m else "")}



def clean(name):
    """A database name cut at leaked source markup (2026-10-09: an NPC read 'Lord Valthalak"].." - "..format(AL["Tier %s Sets', an
    AtlasLoot Lua fragment in the simulator's database)."""
    if not name:
        return name
    for mark in ('"', "..", "[", "%s", "|c"):
        k = name.find(mark)
        if k > 0:
            name = name[:k]
    return name.strip(" -,")

# Raid items (2026-11-22, the user: no raid is in Forever yet, and Molten Core is not coming; The Barrow Deeps, Hyjal Summit and Onyxia's
# Lair open on 2026-12-09): an item counts as the raid's when it drops there, is made from its materials (gear_opt.PHASE1_RAID_MADE:
# the Scale of Onyxia items are Onyxia's, the rest Molten Core's) or is its quest's reward (gear_opt.PHASE1_QUEST: Molten Core's
# hunter quest; gear_opt.RAID_QUEST: Onyxia's); an enchant when its formula drops there. The pages' Raid BiS note reads the tags.
RAID_ZONES = ("Molten Core", "Onyxia's Lair")
MC_QUEST = {"Rhok'delar, Longbow of the Ancient Keepers", "Lok'delar, Stave of the Ancient Keepers"}
ONY_QUEST = {"Dragonslayer's Signet", "Onyxia Tooth Pendant", "Onyxia Blood Talisman"}


class DB:
    """The simulator's item database (assets/database/db.json): items, enchants, zones and bosses."""

    def __init__(self, repo):
        d = json.load(open(repo / "assets" / "database" / "db.json", encoding="utf-8"))
        self.items = {i["id"]: i for i in d["items"]}
        self.enchants = {}   # effect id -> every enchant with it (one effect serves a bracer and a glove enchant, a 1H and a 2H one)
        self.spell_names = {}   # spell id -> the enchant names that carry it (13823 is Bracer, Gloves and Boots Greater Agility)
        for e in d["enchants"]:
            self.enchants.setdefault(e.get("effectId"), []).append(e)
            if e.get("spellId"):
                self.spell_names.setdefault(e["spellId"], set()).add(e.get("name"))
        self.zones = {z["id"]: z["name"] for z in d.get("zones", [])}
        self.npcs = {n["id"]: n for n in d.get("npcs", [])}
        self.prof = professions(repo)

    def raid(self, item, made=()):
        """The raid an item or enchant entry belongs to (RAID_ZONES), or None; `made`: the names made from raid materials."""
        for s in item.get("sources") or []:
            x = s.get("drop") or {}
            zone = self.zones.get(x.get("zoneId") or (self.npcs.get(x.get("npcId")) or {}).get("zoneId"))
            if zone in RAID_ZONES:
                return zone
        name = item.get("name") or ""
        if name in MC_QUEST:
            return "Molten Core"
        if name in ONY_QUEST or name.startswith("Onyxia Scale"):
            return "Onyxia's Lair"
        if name in made:
            return "Molten Core"
        return None

    def source(self, item):
        """Where an item comes from, in a few words (the first source the database lists; empty when it lists none)."""
        for s in item.get("sources") or []:
            if "drop" in s:
                x = s["drop"]
                npc = self.npcs.get(x.get("npcId")) or {}
                zone = self.zones.get(x.get("zoneId") or npc.get("zoneId"))
                return ", ".join(v for v in (clean(npc.get("name")), clean(zone)) if v) or "world drop"
            if "crafted" in s:
                return self.prof.get(s["crafted"].get("profession"), "crafted")
            if "quest" in s:
                return "quest: " + (clean(s["quest"].get("name")) or "?")
            if "soldBy" in s:
                return "sold by " + s["soldBy"].get("npcName", "a vendor")
        return ""

    def enchant(self, effect_id, item):
        """{name, url} of the enchant on an item: the one of that effect for the item's slot (ItemType; a two-hander's 2H enchant);
        an enchanting formula links its spell, an arcanum, armor kit or oil its item."""
        cands = self.enchants.get(effect_id) or []
        fit = [e for e in cands if item.get("type") in [e.get("type"), *(e.get("extraTypes") or [])]] or cands
        two_hand = item.get("handType") == 4   # HandTypeTwoHand
        fit = [e for e in fit if ("2H" in e.get("name", "")) == two_hand] or fit
        e = fit[0] if fit else None
        if not e:
            return None
        # 2026-10-15 page audit B15: the database gives one spell id to enchants of several slots (13823: Enchant Bracer - Greater
        # Agility, Enchant Gloves - Agility, Enchant Boots - Greater Agility), and Wowhead's spell page is only one of them; such an
        # enchant links its own formula or scroll item, which is slot-specific
        shared = len(self.spell_names.get(e.get("spellId"), ())) > 1
        if e.get("spellId") and (not e.get("itemId") or (e.get("name", "").startswith("Enchant ") and not shared)):
            url = f"{WOWHEAD}/spell={e['spellId']}"
        else:
            url = f"{WOWHEAD}/item={e['itemId']}" if e.get("itemId") else None
        return {"name": e.get("name", f"enchant {effect_id}"), "url": url, "effect": effect_id}   # (effect: page_lint's gear row)

    def rows(self, gear_path):
        """[{slot, id, name, url, ilvl, quality, source, enchant?}] for a gear set file, empty slots left out."""
        g = json.load(open(resolve(gear_path), encoding="utf-8"))
        out = []
        for i, it in enumerate(g.get("items", [])):
            if not it.get("id"):
                continue
            item = self.items.get(it["id"], {})
            row = {"slot": MB.SLOTS[i] if i < len(MB.SLOTS) else "?", "index": i, "id": it["id"], "name": item.get("name", f"item {it['id']}"),
                   "url": f"{WOWHEAD}/item={it['id']}", "ilvl": ((item.get("scalingOptions") or {}).get("0") or {}).get("ilvl"),
                   "quality": item.get("quality"), "source": self.source(item)}
            ench = self.enchant(it["enchant"], item) if it.get("enchant") else None
            if ench:
                er = next((self.raid(e) for e in self.enchants.get(it["enchant"]) or [] if self.raid(e)), None)
                if er:
                    ench["raid"] = er
                row["enchant"] = ench
            rr = self.raid(item, MADE)
            if rr:
                row["raid"] = rr
            out.append(row)
        return out


LIST_KEYS = ("dungeon", "prebis", "bis")


def skipped_ids():
    """The item ids whose effect the simulator leaves for manual implementation (effects_inventory.py's record), or an empty set."""
    p = HERE / "effects-inventory.json"
    if not p.exists():
        return set()
    d = json.load(open(p, encoding="utf-8"))
    return {x["id"] for lst in d.get("lists", {}).values() for c in lst.get("classes", {}).values() for x in c.get("skipped_matters") or []}


def support_lists(sets_rec, files, db, skipped):
    """{list key: {...}} for a tank's or healer's sets made under the lists (2026-11-23): `sets_rec` {tier: the maker's record of the set}
    (tank-gear.json's class entry, heal-gear.json's sets), `files` {tier: set file}; the rows with kinds and marks, the currency."""
    out = {}
    for t in LIST_KEYS:
        g, f = sets_rec.get(t) or {}, files.get(t)
        if not g.get("rules") or not f:
            continue
        rows = db.rows(f)
        kinds, marks = g.get("kinds") or {}, g.get("marks") or {}
        for row in rows:
            row["kinds"] = kinds.get(str(row["index"])) or []
            row["marks"] = marks.get(str(row["index"])) or {}
            if row["id"] in skipped:
                row["effect_not_simulated"] = True
        out[t] = {"list": g.get("list"), "rules": g.get("rules"), "rows": rows, "ilvl": g.get("ilvl"), "currency_cost": g.get("currency_cost"),
                  "faction_alternatives": g.get("faction_alternatives") or [], "pvp_alternatives": g.get("pvp_alternatives") or []}
    return out


def list_sets(r, db, skipped):
    """{list key: {...}} the pages' three lists for a record made under the lists (2026-11-23, the audit session's page spec): each list's
    set and its no-PvP and side sets as the record names them, every row with its kinds (where it comes from), marks (PvP, a profession)
    and whether its effect is simulated; the set's hit against the caps, its set bonuses (simulated and not), its currency cost, the
    faction alternatives, the budget, a close call, and the build's full-raid DPS in it on the missed-set check's fights."""
    out = {}
    gear = r.get("gear") or {}
    for t in LIST_KEYS:
        for v in ("", "-nopvp", "-alliance", "-horde", "-nopvp-alliance", "-nopvp-horde"):
            g = gear.get(t + v)
            if not isinstance(g, dict) or not g.get("rules") or not g.get("gear"):
                continue
            rows = db.rows(g["gear"])
            kinds, marks = g.get("kinds") or {}, g.get("marks") or {}
            alts = {(a.get("slot"), a.get("item")): a for a in g.get("faction_alternatives") or []}
            for row in rows:
                row["kinds"] = kinds.get(str(row["index"])) or []
                row["marks"] = marks.get(str(row["index"])) or {}
                if row["id"] in skipped:
                    row["effect_not_simulated"] = True
                a = alts.get((row["index"], row["id"]))
                if a and a.get("alternative"):   # (2026-11-23) the other side's item for a one-faction item, named in the row
                    row["faction_alt"] = {"faction": a.get("faction"), "for": a.get("for"), "name": a.get("alternative_name"),
                                          "url": f"{WOWHEAD}/item={a['alternative']}", "twin": a.get("value") == a.get("alternative_value")}
            hit = g.get("hit") or {}
            sc = g.get("set_check") or {}
            mc = (g.get("miss_check") or {}).get("dps") or {}
            dps = [mc[s]["shown"] for s in mc if (mc[s] or {}).get("shown")]
            out[t + v] = {"list": g.get("list"), "rules": g.get("rules"), "rows": rows, "ilvl": g.get("ilvl"),
                          "hit": {k: hit.get(k) for k in ("used", "flags", "notes") if hit.get(k)},
                          "sets_on": hit.get("sets") or sc.get("active") or [], "unsimulated": sc.get("unsimulated") or [],
                          "currency_cost": g.get("currency_cost"), "faction_alternatives": g.get("faction_alternatives") or [],
                          "pvp_alternatives": g.get("pvp_alternatives") or [], "budget": g.get("budget"),
                          "close_call": bool((g.get("confirm_margin") or {}).get("close_call")), "chosen_source": g.get("chosen_source"),
                          **({"dps": round(sum(dps) / len(dps), 1), "dps_seeds": len(dps)} if dps else {})}
    return out


def sim_links(r, repo, apiv):
    """{key: share url} for a record's tier x setting winners, with the talents the pages show (ml_builds.shown)."""
    cls = r["class"]
    trees = R.load_trees(repo, cls)
    out = {}
    for k in KEYS:
        s = (r.get("search") or {}).get(k) or {}
        tier, setting = k.split("-")
        g = ((MB.page_gear(r, tier) if setting == "raid" else (r.get("gear") or {}).get(tier)) or {}).get("gear")
        w = MB.shown(r, k) if s.get("winner") else None
        if not (w and g):
            continue
        e = R.SPECS[cls][s["entry"]]
        try:
            tal = R.talents_string(trees, MB.flat_of(w["allocation"]))
        except SystemExit as err:   # a record searched on older trees (2026-10-09: King of the Jungle, removed in 70170): no link until it reruns
            print(f"  {cls} {r['spec']} {k}: no link ({err})", flush=True)
            continue
        b = {"label": k, "talents": tal, "gear_json": json.load(open(resolve(g), encoding="utf-8"))}
        row = A.bench(e, repo, [b], 3000, 1, setting, f"link-{cls}", extra={"link": True, "api_version": apiv}).get(k) or {}
        if row.get("link"):
            out[k] = f"{SITE}/{e['sim_spec']}/#{row['link']}"
        else:
            print(f"  {cls} {r['spec']} {k}: no link ({row.get('error', 'no output')})", flush=True)
    return out


def page_records(classes=None):
    """The finished machine-learning records the pages show: the current one, else the finished one ml_pipeline --fresh kept in ml/prev/
    while it re-runs (flagged `_prev`). 2026-10-15 page audit B2: render_modes.ml_tiers makes the same choice; before, the pages fell back
    to ml/prev/ for their tier numbers while this file dropped the spec, so a re-running spec showed numbers without its gear."""
    cur = {(r["class"], r["spec"]): r for r in MB.records(classes) if MB.complete(r)}
    prev_dir = MB.OUT / "prev"
    for p in sorted(prev_dir.glob("*.json")) if prev_dir.exists() else []:
        try:
            r = json.load(open(p, encoding="utf-8"))
        except ValueError:
            continue
        k = (r.get("class"), r.get("spec"))
        if r.get("class") and (not classes or r["class"] in classes) and k not in cur and MB.complete(r):
            cur[k] = dict(r, _prev=True)
    return list(cur.values())


def support_sets(classes, db, repo, apiv):
    """{"<class>|<spec>|tank" or "|heal": {gear, ilvl, sim, ...}}: the tanks' and healers' pre-BiS and BiS sets (2026-10-15, user decision
    of 2026-10-14: real sets for both, the same linked table as the damage pages). Tanks: raidsim/tank_gear.py, the sets chosen with
    Classic base armor filled in (`classic_armor`: the fork's item database lists armor for one armor item in five, so a set chosen
    without it favours the items that list it), with share links for the tank's page build in the raid setting. Healers:
    heallab/heal_gear.py (healer-lab stat weights; no simulator link: healers are not in the simulator). The druid's bear shares the
    Feral Combat page with the cat, hence the role in the key."""
    out = {}
    TG = _load("tank_gear", HERE / "tank_gear.py")
    rec = json.load(open(HERE / "tank-gear.json", encoding="utf-8")) if (HERE / "tank-gear.json").exists() else {}
    for cls, spec in sorted(SM.TANK_TREE.items()):
        if classes and cls not in classes:
            continue
        sets = {t: TG.tier_gear(cls, spec, t) for t in ("dungeon", "prebis", "bis")}   # (2026-11-23: Easy Pre-BiS too)   # plain sets: the armor patch (fill_armor.py) is in the simulator since 2026-10-15
        sets = {t: p for t, p in sets.items() if p}
        if not sets:
            continue
        gear = {t: db.rows(p) for t, p in sets.items()}
        ilvl = {t: round(sum(x["ilvl"] or 0 for x in rows) / max(1, sum(1 for x in rows if x["ilvl"])), 1) for t, rows in gear.items()}
        r = rec.get(cls) or {}
        sim = {}
        e = R.SPECS[cls].get(r.get("entry")) if r.get("entry") else None
        if e and r.get("build"):
            B = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
            if r["build"] in B:
                tal = R.talents_string(R.load_trees(repo, cls), MB.flat_of(B[r["build"]]["allocation"]))
                for t, p in sets.items():
                    b = {"label": t, "talents": tal, "gear_json": json.load(open(p, encoding="utf-8"))}
                    row = A.bench(e, repo, [b], 3000, 1, "raid", f"link-{cls}-tank", extra={"link": True, "api_version": apiv}).get(t) or {}
                    if row.get("link"):
                        sim[f"{t}-raid"] = f"{SITE}/{e['sim_spec']}/#{row['link']}"
        out[f"{cls}|{spec}|tank"] = {"class": cls, "spec": spec, "role": "tank", "gear": gear, "ilvl": ilvl, "sim": sim,
                                     "build": r.get("build"), "lists": support_lists(r, sets, db, skipped_ids())}
    hg = ROOT / "_reference/data/heallab/heal_gear.py"
    if hg.exists():
        HG = _load("heal_gear", hg)
        for cls, trees in sorted(SM.HEAL_TREES.items()):
            if classes and cls not in classes:
                continue
            for spec in trees:
                sets = HG.tier_gear(cls, spec) if hasattr(HG, "tier_gear") else {}   # {tier: {"gear": path, "ilvl", ...}}
                if not sets:
                    continue
                gear = {t: db.rows(v["gear"]) for t, v in sets.items()}
                ilvl = {t: v.get("ilvl") for t, v in sets.items()}
                hrec = ((json.load(open(hg.parent / "heal-gear.json", encoding="utf-8")) if (hg.parent / "heal-gear.json").exists() else {})
                        .get("specs") or {}).get(f"{cls}|{spec}") or {}
                lists = support_lists(hrec.get("sets") or {}, {t: v["gear"] for t, v in sets.items()}, db, skipped_ids())
                out[f"{cls}|{spec}|heal"] = {"class": cls, "spec": spec, "role": "heal", "gear": gear, "ilvl": ilvl, "sim": {}, "lists": lists}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    apiv = api_version(repo)
    db = DB(repo)
    old = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
    specs = dict(old.get("specs", {})) if a.classes else {}
    skipped = skipped_ids()
    for r in page_records(a.classes or None):
        sets = {t: (MB.page_gear(r, t) or {}) for t in ("dungeon", "prebis", "bis")}   # the pages' sets (full raid)
        gear = {t: db.rows(v["gear"]) for t, v in sets.items() if v.get("gear")}
        key = f"{r['class']}|{r['spec']}"
        specs[key] = {"class": r["class"], "spec": r["spec"], "gear": gear, "ilvl": {t: sets[t].get("ilvl") for t in gear},
                      "files": {t: sets[t]["gear"] for t in gear},   # (2026-11-22, G6: page_lint compares the table with these files)
                      "sim": sim_links(r, repo, apiv), "lists": list_sets(r, db, skipped)}
        if r.get("_prev"):
            specs[key]["prev"] = r.get("date")
        print(f"{key}: {sum(len(v) for v in gear.values())} items, {len(specs[key]['sim'])} simulator links", flush=True)
    for key, v in support_sets(a.classes or None, db, repo, apiv).items():
        specs[key] = v
        print(f"{key}: {sum(len(x) for x in v['gear'].values())} items, {len(v['sim'])} simulator links", flush=True)
    rec = {"date": TODAY, "site": SITE, "wowhead": WOWHEAD, "api_version": apiv, "commit": R.git_commit(repo), "specs": specs}
    if a.write:
        OUT.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)} ({len(specs)} specs)")


if __name__ == "__main__":
    main()
