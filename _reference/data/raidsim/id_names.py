"""Names for the spell and item ids the simulator's rotations and reports use (2026-09-30, user report: pages showed "item 8008"
and "spell 44404").

    python _reference/data/raidsim/id_names.py      # rebuild id-names.json from the beta client tables

The simulator's own name lists miss consumables, trinket effects and some talent auras. Names come from the official simulator's
clone (setup.checkout(), since 2026-10-22): its spell store `sim/core/spelldata/spells_auto_gen.go` (client 1.60.1.70450: every spell
with a name) and item database `assets/database/db.json` (items and consumables); ids neither has keep the name id-names.json already
holds (the first names came from the beta client's SpellName and ItemSparse tables, build 1.60.1.69893, cached by the ElliotWood/Forever
fork's data_watch tool; that cache in the fork's archived clone ~/.wow-forever-tools/forever-repo is read too when it exists). This keeps
the names of every id our rotations (raidsim/apls, raidsim/presets, the simulator's ui/specs apls) and race reports mention in
id-names.json, so rendering works without the simulator repo. Lookups fall back to "spell N" / "item N" when an id is unknown.
"""
import csv
import functools
import glob
import json
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE / "id-names.json"
# ids the client table lacks: the simulator's own (Missile Barrage's aura), our patch's (Quick Strikes, patches/forever) and
# Classic ids a simulator rotation still names
MANUAL = {"spells": {"44404": "Missile Barrage", "1299448": "Quick Strikes (Deadly Aspects)", "9846": "Tiger's Fury", "26297": "Berserking"},
          "items": {}}
sys.path.insert(0, str(HERE))
import setup as SETUP  # noqa: E402  (raidsim/setup.py: the simulator checkout)
SIM = SETUP.checkout()
STORE = SIM / "sim" / "core" / "spelldata" / "spells_auto_gen.go"
DB = SIM / "assets" / "database" / "db.json"
CACHE = SETUP.tools_dir() / "forever-repo" / "tools" / "data_watch" / ".cache"   # the fork's client tables (archive; optional)


@functools.lru_cache(maxsize=None)
def _names():
    return json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {"spells": {}, "items": {}}


def spell(sid, default=None):
    return _names()["spells"].get(str(sid)) or MANUAL["spells"].get(str(sid)) or (default if default is not None else f"spell {sid}")


def item(iid, default=None):
    return _names()["items"].get(str(iid)) or MANUAL["items"].get(str(iid)) or (default if default is not None else f"item {iid}")


def _ids():
    spells, items = set(), set()

    def walk(x):
        if isinstance(x, dict):
            sid = x.get("spellId")
            if isinstance(sid, int):
                spells.add(sid)
            iid = x.get("itemId")
            if isinstance(iid, int):
                items.add(iid)
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    files = (glob.glob(str(HERE / "apls/*/*.apl.json")) + glob.glob(str(HERE / "presets/*/ui/specs/*/*/apls/*.apl.json"))
             + glob.glob(str(SIM / "ui/specs/*/*/apls/*.apl.json")))
    for f in files:
        walk(json.load(open(f, encoding="utf-8")))
    for f in glob.glob(str(ROOT / "*/research/**/*.json"), recursive=True) + glob.glob(str(ROOT / "*/research/**/*.md"), recursive=True):
        txt = open(f, encoding="utf-8", errors="replace").read()
        spells |= {int(m) for m in re.findall(r"\bspell (\d{3,})", txt)}
        items |= {int(m) for m in re.findall(r"\bitem (\d{3,})", txt)}
    return spells, items


def official_names():
    """({spell id: name}, {item id: name}) from the simulator checkout: the spell store and db.json's items and consumables."""
    spells, items = {}, {}
    if STORE.exists():
        for line in open(STORE, encoding="utf-8"):
            m = re.search(r'\{ID: (\d+), Name: "((?:[^"\\]|\\.)*)"', line)
            if m:
                spells[m.group(1)] = m.group(2).replace('\\"', '"')
    if DB.exists():
        db = json.load(open(DB, encoding="utf-8"))
        for x in (db.get("items") or []) + (db.get("consumables") or []):
            if x.get("id") and x.get("name"):
                items.setdefault(str(x["id"]), x["name"])
    return spells, items


def build(out_path=None):
    spells, items = _ids()
    old = _names()
    out = {"source": "", "spells": dict(old["spells"]), "items": dict(old["items"])}
    src = []
    sn = max(CACHE.glob("SpellName_*.csv"), default=None) if CACHE.exists() else None
    it = max(CACHE.glob("ItemSparse_*.csv"), default=None) if CACHE.exists() else None
    if sn and it:   # the fork's client tables (69893), where the archive still exists: first, so the official names win below
        with open(sn, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if int(row["ID"]) in spells:
                    out["spells"][row["ID"]] = row["Name_lang"]
        with open(it, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if int(row["ID"]) in items:
                    out["items"][row["ID"]] = row["Display_lang"]
        src.append(f"{sn.name}, {it.name}")
    osp, oit = official_names()
    if not osp and not oit and not src:
        raise SystemExit(f"no simulator checkout with a spell store under {SIM} (run raidsim/setup.py)")
    for k, v in osp.items():
        if int(k) in spells:
            out["spells"][k] = v
    for k, v in oit.items():
        if int(k) in items:
            out["items"][k] = v
    if osp or oit:
        src.append(f"wowsims/forever {SIM.name} spells_auto_gen.go and db.json")
    out["source"] = "; ".join(src)
    out["spells"] = dict(sorted(out["spells"].items(), key=lambda kv: int(kv[0])))
    out["items"] = dict(sorted(out["items"].items(), key=lambda kv: int(kv[0])))
    out_path = pathlib.Path(out_path or OUT)
    out_path.write_text(json.dumps(out, indent=0, ensure_ascii=False) + "\n", encoding="utf-8")
    miss_s = sorted(spells - {int(k) for k in out["spells"]})
    miss_i = sorted(items - {int(k) for k in out["items"]})
    print(f"wrote {out_path}: {len(out['spells'])} spells, {len(out['items'])} items; unknown: spells {miss_s[:20]}, items {miss_i[:20]}")


if __name__ == "__main__":
    build()
