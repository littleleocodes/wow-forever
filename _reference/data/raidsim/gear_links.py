"""Links for the gear-tier sets (2026-10-03, user request: "is there any way to create an armory or link of sorts so that the pre-bis
and bis gear have a way to see the actual items?").

    python _reference/data/raidsim/gear_links.py [classes] [--write]

For every damage spec's pre-BiS and phase-1 BiS set (the machine-learning records, raidsim/ml/): each item and enchant with its Wowhead
Forever link (www.wowhead.com/forever, the database the simulator's own UI links to), its item level and where it comes from (the boss
and zone, the profession, the quest or the vendor; the simulator's item database), and the whole character as a share link for the
community simulator's live web UI (the ElliotWood/Forever fork's GitHub Pages): the set, the talents the pages show for that tier and
setting (ml_builds.shown), the setting's rotation, consumables, buffs and encounter, exactly as our runs simulate them, encoded by
foreverbench's "link" mode the way the UI's "copy link" does. The site reads links of its own proto version and older; links carry our
simulator copy's version (proto/common.proto: 18, the same as the live site's on 2026-10-03).
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
MB = _load("ml_builds_links", HERE / "ml_builds.py")
OUT = HERE / "gear-links.json"
SITE = "https://elliotwood.github.io/Forever/forever"
WOWHEAD = "https://www.wowhead.com/forever"
KEYS = ("prebis-raid", "bis-raid", "prebis-dummy", "bis-dummy")
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

class DB:
    """The simulator's item database (assets/database/db.json): items, enchants, zones and bosses."""

    def __init__(self, repo):
        d = json.load(open(repo / "assets" / "database" / "db.json", encoding="utf-8"))
        self.items = {i["id"]: i for i in d["items"]}
        self.enchants = {}   # effect id -> every enchant with it (one effect serves a bracer and a glove enchant, a 1H and a 2H one)
        for e in d["enchants"]:
            self.enchants.setdefault(e.get("effectId"), []).append(e)
        self.zones = {z["id"]: z["name"] for z in d.get("zones", [])}
        self.npcs = {n["id"]: n for n in d.get("npcs", [])}
        self.prof = professions(repo)

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
        if e.get("spellId") and (e.get("name", "").startswith("Enchant ") or not e.get("itemId")):
            url = f"{WOWHEAD}/spell={e['spellId']}"
        else:
            url = f"{WOWHEAD}/item={e['itemId']}" if e.get("itemId") else None
        return {"name": e.get("name", f"enchant {effect_id}"), "url": url}

    def rows(self, gear_path):
        """[{slot, id, name, url, ilvl, quality, source, enchant?}] for a gear set file, empty slots left out."""
        g = json.load(open(resolve(gear_path), encoding="utf-8"))
        out = []
        for i, it in enumerate(g.get("items", [])):
            if not it.get("id"):
                continue
            item = self.items.get(it["id"], {})
            row = {"slot": MB.SLOTS[i] if i < len(MB.SLOTS) else "?", "id": it["id"], "name": item.get("name", f"item {it['id']}"),
                   "url": f"{WOWHEAD}/item={it['id']}", "ilvl": ((item.get("scalingOptions") or {}).get("0") or {}).get("ilvl"),
                   "quality": item.get("quality"), "source": self.source(item)}
            ench = self.enchant(it["enchant"], item) if it.get("enchant") else None
            if ench:
                row["enchant"] = ench
            out.append(row)
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
    for r in MB.records(a.classes or None):
        if not MB.complete(r):
            continue
        sets = {t: (MB.page_gear(r, t) or {}) for t in ("prebis", "bis")}   # the pages' sets (full raid)
        gear = {t: db.rows(v["gear"]) for t, v in sets.items() if v.get("gear")}
        key = f"{r['class']}|{r['spec']}"
        specs[key] = {"class": r["class"], "spec": r["spec"], "gear": gear, "ilvl": {t: sets[t].get("ilvl") for t in gear},
                      "sim": sim_links(r, repo, apiv)}
        print(f"{key}: {sum(len(v) for v in gear.values())} items, {len(specs[key]['sim'])} simulator links", flush=True)
    rec = {"date": TODAY, "site": SITE, "wowhead": WOWHEAD, "api_version": apiv, "commit": R.git_commit(repo), "specs": specs}
    if a.write:
        OUT.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)} ({len(specs)} specs)")


if __name__ == "__main__":
    main()
