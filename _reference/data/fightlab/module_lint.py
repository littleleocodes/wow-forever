"""Lint the fight-lab class modules against the current beta data (2026-10-09, after the class reviews found mechanics that had silently
stopped working: the mage module asked for the talent "Hot Streak", renamed Heating Up in 70170, so Heating Up was never simulated; the
shaman's Fire Nova and the hunter's Summon Hawk parsed to 0 damage because their tooltips' wording changed).

    python _reference/data/fightlab/module_lint.py [classes] [--write]

Checks, per class module:
1. every talent or spell name the module asks for by string (`self.rank("X")`, `self.tv("X", ...)`) and every key of its MECHANICS and
   FIT tables is a talent of the class's current tree or a spell of its beta spellbook (a removed or renamed talent reads 0 for ever);
2. every spell the module loaded (its `BOOK`, top rank) whose tooltip carries a damage number ("for 690 Fire damage", "inflicts 413 to
   459 fire damage", "causes 73 Fire damage") has some damage, periodic damage, healing or a buff kind, so a tooltip whose wording the
   parser misses shows up instead of being cast for nothing. A module lists spells it completes when it builds a fight in `LINT_FILLED`
   (the hunter's traps through `TRAPS`), and absorbs are skipped. Pet abilities and spells no rotation casts show up too: read the list;
3. (2026-10-18, audit row 34: six of seven parser misses that pass were not damage) every rank of every loaded spell whose tooltip names a
   stun, a heal, a weapon-damage percentage or a mana cost, where the parsed spell holds none (or a cost under half the spellbook's:
   "1,185 Mana" read as 1);
4. every regular expression the module defines at module level, against every rank of every spell and talent tooltip of the class: a
   pattern that matches nothing (Classic's "melee attack power by" after 70425 said "Attack Power by") and, for a spell whose ranks it
   matches somewhere, the ranks it misses (Seal of Fury rank 2 says "inflict" where the others say "deal"). Patterns meant for one rank
   or for talents show up too: read the list.
Writes `_reference/fightlab-lint.md` with --write. Exit status 1 when a name check fails."""
import argparse
import datetime
import importlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data"), str(ROOT / "_reference/data/scorer")]
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
PAGE = ROOT / "_reference" / "fightlab-lint.md"
# double-quoted names may hold an apostrophe (Nature's Grace, Winter's Chill)
ASK = re.compile(r"""self\.(?:rank|tv)\(\s*(?:"([^"]+)"|'([^']+)')""")
DMG_NUM = re.compile(r"\d[\d,]*(?: to \d[\d,]*)? (?:(?:fire|frost|arcane|nature|shadow|holy|physical) )?damage", re.I)


def names(cls):
    tal = {t["name"] for tr in json.load(open(ROOT / "_reference/data/forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"] for t in tr["talents"]}
    book = json.load(open(ROOT / "_reference/data/forever-spells" / f"{cls}.json", encoding="utf-8"))
    sp = {s["name"] for tab in book["tabs"] for s in tab["spells"]}
    return tal, sp


STUN = re.compile(r"\bstun(?:s|ning)?\b[^.]*?for (\d+(?:\.\d+)?) sec", re.I)
HEALS = re.compile(r"\bheals?\b[^.]*?\b(\d[\d,]*)\b", re.I)
WEAPON = re.compile(r"(\d+)% (?:of )?(?:your )?(?:main hand )?weapon damage", re.I)
COST = re.compile(r"^(\d[\d,]*) Mana$")


def book_ranks(cls):
    """{(spell, rank number): spellbook rank} of the class's beta spellbook."""
    book = json.load(open(ROOT / "_reference/data/forever-spells" / f"{cls}.json", encoding="utf-8"))
    out = {}
    for tab in book["tabs"]:
        for s in tab["spells"]:
            for i, r in enumerate(s["ranks"]):
                m = re.search(r"(\d+)", r.get("rank") or "")
                out[(s["name"], int(m.group(1)) if m else i + 1)] = r
    return out


def field_checks(cls, mod, filled):
    """Rows for check 3: a stun, heal, weapon percentage or mana cost in a tooltip that the parsed spell does not hold."""
    rows = []
    raw = book_ranks(cls)
    book = getattr(mod, "BOOK", None)
    if not isinstance(book, dict):
        return rows
    for n, ranks in sorted(book.items()):
        if n in filled:
            continue
        for s in ranks:
            text = getattr(s, "text", "") or ""
            miss = []
            if STUN.search(text) and not getattr(s, "stun", 0):
                miss.append("a stun")
            if HEALS.search(text) and not (getattr(s, "heal_max", 0) or getattr(s, "hot", 0) or getattr(s, "absorb", 0)) \
                    and not re.search(r"\b(?:drain|transfer|absorb)", text, re.I) and getattr(s, "kind", "") != "buff":
                miss.append("a heal")
            if WEAPON.search(text) and not getattr(s, "weapon_pct", 0):
                miss.append("a weapon-damage percentage")
            r = raw.get((n, getattr(s, "rank", 0) or 0))
            mc = COST.match((r or {}).get("cost") or "")
            if mc and getattr(s, "resource", "mana") == "mana":
                want = float(mc.group(1).replace(",", ""))
                if want >= 10 and getattr(s, "cost", 0) < 0.5 * want:
                    miss.append(f"its mana cost ({want:.0f}, parsed {getattr(s, 'cost', 0):.0f})")
            if miss:
                rows.append(f"**{n}** rank {getattr(s, 'rank', '?')}: the tooltip names {', '.join(miss)} the parsed spell lacks: \"{text[:100]}\"")
    return rows


def pattern_checks(cls, mod):
    """Rows for check 4: module-level regular expressions that match no tooltip of the class, or miss some ranks of a spell they match."""
    texts = {}
    for (n, k), r in book_ranks(cls).items():
        texts.setdefault(n, []).append((k, (r.get("text") or "") + " " + (r.get("coefficient") or "")))
    for tr in json.load(open(ROOT / "_reference/data/forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]:
        for t in tr["talents"]:
            for i, r in enumerate(t.get("ranks") or []):
                texts.setdefault(t["name"], []).append((i + 1, (r.get("text") if isinstance(r, dict) else str(r)) or ""))
    rows = []
    for var, pat in sorted(vars(mod).items()):
        if not isinstance(pat, re.Pattern) or var.startswith("_"):
            continue
        hit = {n: [k for k, tx in rk if pat.search(tx)] for n, rk in texts.items()}
        hit = {n: ks for n, ks in hit.items() if ks}
        if not hit:
            rows.append(f"`{var}` (`{pat.pattern[:70]}`) matches no spell or talent tooltip of the current {cls} data")
            continue
        for n, ks in sorted(hit.items()):
            allk = [k for k, _ in texts[n]]
            missing = [k for k in allk if k not in ks]
            if missing and len(ks) >= 1 and len(allk) > 1:
                rows.append(f"`{var}` matches **{n}** ranks {ks} but not ranks {missing}")
    return rows


def lint(cls):
    """(names the current data lacks, damage spells that parse to none, unparsed non-damage fields, regex coverage)"""
    tal, sp = names(cls)
    src = (HERE / f"{cls}.py").read_text(encoding="utf-8")
    bad, zero = [], []
    for n in sorted({a or b for a, b in ASK.findall(src)}):
        if n not in tal and n not in sp:
            bad.append(f"asks for **{n}** (self.rank / self.tv), which is no talent or spell of the current {cls} data")
    mod = importlib.import_module(cls)
    for table in ("MECHANICS", "FIT"):
        for n in sorted(getattr(mod, table, {}) or {}):
            if n not in tal and n not in sp:
                bad.append(f"{table} has **{n}**, which is no talent or spell of the current {cls} data")
    book = getattr(mod, "BOOK", None)
    filled = set(getattr(mod, "LINT_FILLED", ())) | set(getattr(mod, "TRAPS", ()))
    if isinstance(book, dict):
        for n, ranks in sorted(book.items()):
            s = ranks[-1]
            text = getattr(s, "text", "") or ""
            if n in filled or not DMG_NUM.search(text) or re.search(r"\babsorb", text, re.I):
                continue
            if getattr(s, "kind", "spell") in ("buff", "heal", "melee", "ranged"):
                continue
            if not (s.dmg_max or s.dot or getattr(s, "heal_max", 0) or getattr(s, "weapon_pct", 0) or getattr(s, "burn", 0)):
                zero.append(f"**{n}** (rank {s.rank}) parses to no damage: \"{text[:110]}\"")
    return bad, zero, field_checks(cls, mod, filled), pattern_checks(cls, mod)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    found = {}
    for cls in a.classes or CLASSES:
        try:
            found[cls] = lint(cls)
        except Exception as e:   # noqa: BLE001 - a module that does not load is itself a finding
            found[cls] = ([f"the module did not load: {e!r}"], [], [], [])
    o = ["# Fight-lab module lint (generated)", "", f"> Generated by `_reference/data/fightlab/module_lint.py` on {datetime.date.today().isoformat()}: "
         "talent and spell names each class module asks for, against the current beta data, and spells whose tooltip carries a damage number "
         "but parse to none (pet abilities and spells no rotation casts appear there too), tooltip stuns, heals, weapon percentages and mana "
         "costs the parsed spells lack, and module regular expressions that match no tooltip or miss some ranks of a spell. Do not hand-edit.", ""]
    for cls, (bad, zero, fields, pats) in found.items():
        o += [f"## {cls}", "", "**Names**", ""] + ([f"- {r}" for r in bad] or ["- all found"]) + [""]
        o += ["**Damage spells that parse to none**", ""] + ([f"- {r}" for r in zero] or ["- none"]) + [""]
        o += ["**Other tooltip numbers the parsed spells lack** (stun, heal, weapon %, mana cost)", ""] + ([f"- {r}" for r in fields] or ["- none"]) + [""]
        o += ["**Regular expressions: no match, or ranks missed**", ""] + ([f"- {r}" for r in pats] or ["- none"]) + [""]
    text = "\n".join(o) + "\n"
    if a.write:
        PAGE.write_text(text, encoding="utf-8")
    print(text)
    sys.exit(1 if any(v[0] for v in found.values()) else 0)


if __name__ == "__main__":
    main()
