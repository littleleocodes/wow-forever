"""The live client's mana costs against forever-spells (2026-11-21; the extended lint's cost check. The audit session: "write it up as a
check that runs with live_spells at every client update, since the export's cost field is never refreshed").

    python _reference/data/client_costs.py [--build 1.60.1.70938] [--fetch] [--diff 1.60.1.70862] [--write]

Reads the client's SpellPower table (wago.tools, product wowf; ~/.wow-forever-tools/wago/SpellPower-<build>.csv, never the repository;
--fetch downloads it; without --build the newest table there). Mana rows only (PowerType 0, OrderIndex 0): the client stores rage in
tenths, and the modules keep rage, energy and focus themselves. Lists every rank of every class spell in forever-spells/<class>.json whose
cost text differs from the client's: a flat cost against ManaCost, a share of base mana against PowerCostPct. --write puts them in
fightlab/client_costs.json, which the fight lab applies when a module loads its spellbook (tables.CLIENT_COSTS, through
tables.trainer_ranks_only; the healer lab has its own loader, and its one listed heal, Riptide, it reads from the notes within 3 mana). --diff lists the class spells' rows that changed between two client builds. live_spells.py runs it (--fetch
--write) at the end of a --write pull, on the client build the pull names.

Found on 2026-11-21: Chain Lightning 245/360/425/495 (the export's 145/200/250/315), Riptide 150/180/230 (245/300/385), and since client
70938 Arcane Shot and Summon Hawk at 11% of base mana (flat 25-190 before)."""
import argparse
import csv
import datetime
import json
import pathlib
import re
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
WAGO = pathlib.Path.home() / ".wow-forever-tools" / "wago"
OUT = HERE / "fightlab" / "client_costs.json"
CLASSES = ("druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior")
COST = re.compile(r"(\d[\d,]*(?:\.\d+)?)\s*(%?)")


def table_path(build):
    return WAGO / f"SpellPower-{build}.csv"


def newest_build():
    found = sorted((tuple(int(x) for x in p.stem.split("-", 1)[1].split(".")), p.stem.split("-", 1)[1]) for p in WAGO.glob("SpellPower-*.csv"))
    if not found:
        raise SystemExit(f"no SpellPower table in {WAGO}: run with --build <client build> --fetch")
    return found[-1][1]


def fetch(build):
    p = table_path(build)
    WAGO.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(f"https://wago.tools/db2/SpellPower/csv?build={build}", headers={"User-Agent": "forever-tools"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    if not data.startswith(b"ID,"):
        raise SystemExit(f"wago.tools gave no SpellPower table for {build}")
    p.write_bytes(data)
    return p


def load_table(build):
    """{spell id: (flat mana cost, share of base mana)} for the mana rows of the client's SpellPower table."""
    out = {}
    with open(table_path(build), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("PowerType") or "0") != "0" or (r.get("OrderIndex") or "0") != "0":
                continue
            out[int(r["SpellID"])] = (int(float(r.get("ManaCost") or 0)), float(r.get("PowerCostPct") or 0))
    return out


def client_text(flat, pct):
    return f"{pct:g}% of base mana" if pct and not flat else f"{flat:,} Mana"


def cast_names(cls):
    """Spells the class's by-level guides press (level-guides/<class>.measured.json), for the report only."""
    p = HERE / "level-guides" / f"{cls}.measured.json"
    if not p.exists():
        return set()
    m = json.load(open(p, encoding="utf-8")).get("guides") or {}
    return {s for g in m.values() for r in (g.get("levels") or {}).values() if isinstance(r, dict) for s, n in (r.get("casts") or {}).items() if n}


def compare(build):
    """[(class, spell, rank, level, id, ours, client text)] for every rank whose mana cost differs from the client's."""
    tab = load_table(build)
    rows = []
    for cls in CLASSES:
        for t in json.load(open(HERE / "forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
            for sp in t.get("spells", []):
                for r in sp.get("ranks", []):
                    sid, cost = int(r.get("id") or 0), (r.get("cost") or "")
                    if not sid or sid not in tab or "mana" not in cost.lower():
                        continue
                    m = COST.search(cost)
                    if not m:
                        continue
                    v, is_pct = float(m.group(1).replace(",", "")), bool(m.group(2))
                    flat, pct = tab[sid]
                    if not flat and not pct:
                        continue   # the client lists no mana cost on that row: nothing to compare
                    same = (abs(v - pct) < 0.01 and not flat) if is_pct else (abs(v - flat) < 0.5 and not pct)
                    if not same:
                        rows.append((cls, sp["name"], r.get("rank") or "", r.get("level"), sid, cost, client_text(flat, pct)))
    return rows


def diff(old, new):
    """Class spells' mana rows that changed between two client builds: [(class, spell, rank, id, old text, new text)]."""
    a, b = load_table(old), load_table(new)
    names = {}
    for cls in CLASSES:
        for t in json.load(open(HERE / "forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
            for sp in t.get("spells", []):
                for r in sp.get("ranks", []):
                    if r.get("id"):
                        names[int(r["id"])] = (cls, sp["name"], r.get("rank") or "")
    out = []
    for sid in sorted(set(a) | set(b)):
        if sid in names and a.get(sid) != b.get(sid):
            out.append(names[sid] + (sid, client_text(*a[sid]) if sid in a else "-", client_text(*b[sid]) if sid in b else "-"))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--build", help="client build, e.g. 1.60.1.70938 (default: the newest table in ~/.wow-forever-tools/wago)")
    ap.add_argument("--fetch", action="store_true", help="download the table from wago.tools when it is not there")
    ap.add_argument("--diff", help="an older client build: list the class spells' rows that changed")
    ap.add_argument("--write", action="store_true", help="write fightlab/client_costs.json")
    a = ap.parse_args(argv)
    build = a.build or newest_build()
    if a.build and not table_path(build).exists():
        if not a.fetch:
            raise SystemExit(f"no table for {build}: add --fetch")
        fetch(build)
    if a.diff:
        if not table_path(a.diff).exists() and a.fetch:
            fetch(a.diff)
        ch = diff(a.diff, build)
        print(f"class spells' mana costs changed from {a.diff} to {build}: {len(ch)}")
        for cls, n, rk, sid, x, y in ch:
            print(f"  {cls} {n} {rk} (id {sid}): {x} -> {y}")
    rows = compare(build)
    casts = {cls: cast_names(cls) for cls in CLASSES}
    print(f"forever-spells against the client's SpellPower table ({build}): {len(rows)} ranks differ")
    for cls, n, rk, lvl, sid, ours, cl in rows:
        print(f"  {'CAST ' if n in casts[cls] else '     '}{cls} {n} {rk} (id {sid}, level {lvl}): ours \"{ours}\", client \"{cl}\"")
    if a.write:
        rec = {"build": build, "date": datetime.date.today().isoformat(), "source": f"wago.tools SpellPower, product wowf, build {build}",
               "note": "Ranks whose forever-spells cost differs from the live client's; applied by tables.CLIENT_COSTS. Made by client_costs.py.",
               "costs": {str(sid): {"class": cls, "spell": n, "rank": rk, "level": lvl, "ours": ours, "client": cl}
                         for cls, n, rk, lvl, sid, ours, cl in rows}}
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {OUT.relative_to(HERE.parents[1])}")
    return rows


if __name__ == "__main__":
    sys.exit(0 if main() is not None else 1)
