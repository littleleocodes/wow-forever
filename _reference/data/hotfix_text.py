"""Live hotfix numbers the fan-site datamines have not read yet, applied to our talent and spell text (2026-10-30).

The live client's hotfix push of 2026-10-30 (no Blizzard notes; read from the client's hotfix cache by the trackers below and by the
official simulator, whose numbers already carry it) changed talent and spell numbers after talentsforever.com's export of 2026-10-29,
the newest tooltip text we have. The raid simulator needs nothing from here; the fight lab, the stats model and the pages read our text,
so the changed numbers are written into it, each rank marked in `hotfix` with the source. Remove an entry once an export carries it.

Sources: https://foreverchanges.pro/patch-notes (per-rank numbers, "October 30 hotfix"), https://wowforever.be/news/druids-and-paladins-get-
reshuffled-talent-trees/ (the same list, citing Wowhead). Neither is confirmed in game; Blizzard posted notes only for 2026-10-27.

    refresh_forever_talents.py and build_forever_spells.py call apply_talents(cls, obj) / apply_spells(cls, obj) on what they write.
"""
import re

SOURCES = ["https://foreverchanges.pro/patch-notes", "https://wowforever.be/news/druids-and-paladins-get-reshuffled-talent-trees/"]
DATE = "2026-10-30"


def _sub(pat, rep):
    """A rank text edit: re.sub(pat, rep(rank_index, match)) once."""
    return lambda i, s: re.sub(pat, lambda m: rep(i, m), s, count=1)


# (class, talent) -> [edits applied to every rank's text]
TALENTS = {
    ("druid", "Genesis"): [_sub(r"by \d+%\.", lambda i, m: f"by {2 * (i + 1)}%.")],   # 2-10% (was 1-5%)
    ("druid", "Naturalist"): [_sub(r"increases all damage you deal by \d+%", lambda i, m: f"increases all damage you deal by {2 * (i + 1)}%"),
                              _sub(r"your Healing Touch spell", lambda i, m: "your Healing Touch and Wild Growth spells")],
    ("druid", "Leader of the Pack"): [_sub(r"the melee and ranged Critical Strike chance", lambda i, m: "the Critical Strike chance (melee, ranged and spell)")],
    ("druid", "Moonkin Form"): [_sub(r"their spell Critical Strike chance increased by 3%",
                                     lambda i, m: "their Critical Strike chance (melee, ranged and spell) increased by 3%")],
    ("mage", "Ice Barrier"): [_sub(r"increasing your Frost damage by 3%", lambda i, m: "increasing your Frost damage by 15%"),
                              _sub(r"an additional 3%", lambda i, m: "an additional 5%")],
    ("mage", "Winter's Chill"): [_sub(r"your next Cone of Cold by 5%", lambda i, m: "your next Cone of Cold by 20%")],
    ("mage", "Arctic Reach"): [_sub(r"Frostbolt, Frost Blast, and Blizzard spells", lambda i, m: "Frostbolt, Frost Blast, Ice Lance and Blizzard spells")],
}

# (class, spell) -> ([edits of every rank's text], {field: value} for every rank)
SPELLS = {
    ("mage", "Ice Lance"): ([_sub(r"Deals 200% increased damage to Frozen targets", lambda i, m: "Deals 300% increased damage to Frozen targets")],
                           {"cooldown": "8 sec cooldown"}),   # 300% (was 200%); the 8 s cooldown on every rank (70685 gave it rank 1 only)
    ("priest", "Shadow Word: Death"): ([_sub(r"backlash damage equal to 10% of your maximum health",
                                             lambda i, m: "backlash damage equal to 30% of your maximum health")], {}),   # 10% -> 30% (sim ac6387f)
    ("mage", "Arcane Blast"): ([_sub(r"you gain 15% of your Intellect", lambda i, m: "you gain 12% of your Intellect"),
                               _sub(r"increased by 175%", lambda i, m: "increased by 100%"),
                               _sub(r"lasts 15 sec", lambda i, m: "lasts 18 sec")], {}),
}


def _mark(rec, i, old):
    h = rec.setdefault("hotfix", {"date": DATE, "sources": SOURCES, "ranks": [], "before": {}})
    if i + 1 not in h["ranks"]:
        h["ranks"].append(i + 1)
        h["before"][str(i + 1)] = old


def apply_talents(cls, obj):
    """Edit a forever-talents object in place; returns the talents changed."""
    out = []
    for tr in obj.get("trees", []):
        for t in tr["talents"]:
            eds = TALENTS.get((cls, t["name"]))
            if not eds:
                continue
            for i, s in enumerate(t["ranks"]):
                new = s
                for e in eds:
                    new = e(i, new)
                if new != s:
                    _mark(t, i, s)
                    t["ranks"][i] = new
            if t.get("hotfix"):
                out.append(t["name"])
    return out


def apply_spells(cls, obj):
    """Edit a forever-spells object in place; returns the spells changed."""
    out = []
    for tab in obj.get("tabs", []):
        for sp in tab["spells"]:
            x = SPELLS.get((cls, sp["name"]))
            if not x:
                continue
            eds, fields = x
            for i, r in enumerate(sp["ranks"]):
                new = r.get("text", "")
                for e in eds:
                    new = e(i, new)
                changed = new != r.get("text", "") or any(r.get(k) != v for k, v in fields.items())
                if changed:
                    _mark(r, 0, {"text": r.get("text", ""), **{k: r.get(k) for k in fields}})
                    r["text"] = new
                    r.update(fields)
            if any(r.get("hotfix") for r in sp["ranks"]):
                out.append(sp["name"])
    return out
