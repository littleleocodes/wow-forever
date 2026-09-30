"""Names for the spell and item ids the simulator's rotations and reports use (2026-09-30, user report: pages showed "item 8008"
and "spell 44404").

    python _reference/data/raidsim/id_names.py      # rebuild id-names.json from the beta client tables

The simulator's own name lists miss consumables, trinket effects and some talent auras. The beta client's tables (SpellName,
ItemSparse, build 1.60.1.69893, cached by the simulator repo's data_watch tool) name all of them; this keeps the names of every id
our rotations (raidsim/apls, the simulator's ui/specs apls) and race reports mention in id-names.json, so rendering works without
the simulator repo. Lookups fall back to "spell N" / "item N" when an id is unknown.
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
CACHE = pathlib.Path(os.path.expanduser("~/.wow-forever-tools/forever-repo/tools/data_watch/.cache"))


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
    files = glob.glob(str(HERE / "apls/*/*.apl.json")) + glob.glob(os.path.expanduser("~/.wow-forever-tools/forever-repo/ui/specs/*/*/apls/*.apl.json"))
    for f in files:
        walk(json.load(open(f, encoding="utf-8")))
    for f in glob.glob(str(ROOT / "*/research/**/*.json"), recursive=True) + glob.glob(str(ROOT / "*/research/**/*.md"), recursive=True):
        txt = open(f, encoding="utf-8", errors="replace").read()
        spells |= {int(m) for m in re.findall(r"\bspell (\d{3,})", txt)}
        items |= {int(m) for m in re.findall(r"\bitem (\d{3,})", txt)}
    return spells, items


def build():
    sn = max(CACHE.glob("SpellName_*.csv"), default=None)
    it = max(CACHE.glob("ItemSparse_*.csv"), default=None)
    if not sn or not it:
        raise SystemExit(f"the client tables are not under {CACHE} (run raidsim/setup.py)")
    spells, items = _ids()
    old = _names()
    out = {"source": f"{sn.name}, {it.name}", "spells": dict(old["spells"]), "items": dict(old["items"])}
    with open(sn, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if int(row["ID"]) in spells:
                out["spells"][row["ID"]] = row["Name_lang"]
    with open(it, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if int(row["ID"]) in items:
                out["items"][row["ID"]] = row["Display_lang"]
    out["spells"] = dict(sorted(out["spells"].items(), key=lambda kv: int(kv[0])))
    out["items"] = dict(sorted(out["items"].items(), key=lambda kv: int(kv[0])))
    OUT.write_text(json.dumps(out, indent=0, ensure_ascii=False) + "\n", encoding="utf-8")
    miss_s = sorted(spells - {int(k) for k in out["spells"]})
    miss_i = sorted(items - {int(k) for k in out["items"]})
    print(f"wrote {OUT.relative_to(ROOT)}: {len(out['spells'])} spells, {len(out['items'])} items; unknown: spells {miss_s[:20]}, items {miss_i[:20]}")


if __name__ == "__main__":
    build()
