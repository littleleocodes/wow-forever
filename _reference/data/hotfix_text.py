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
# 2026-10-31: talentsforever's export of 30 Oct (launch build 70685 = client 70630 + the hotfixes of 28 and 30 Oct) carries every
# number below that was listed here (druid Genesis, Naturalist, Leader of the Pack, Moonkin Form; paladin Boundless Light; mage Ice
# Barrier, Winter's Chill, Arctic Reach; spells: Ice Lance 300% and its 8 s cooldown on every rank, Shadow Word: Death's 30% backlash,
# Arcane Blast 12%/100%/18 s): those entries are removed. Oath of Light stays: the export words it without numbers.
TALENTS = {
    # paladin (hotfix push 113554): the numbers are the simulator's (oath_of_light.go: 400/115/229 at level 60); the heal lab reads them.
    # The 70685 export words it "your Holy Light, Flash of Light, and Holy Shock on them".
    ("paladin", "Oath of Light"): [_sub(r"Holy Light on them by up to \d+, your Flash of Light by up to \d+, and your Holy Shock by up to \d+"
                                        r"|Holy Light, Flash of Light, and Holy Shock on them",
                                        lambda i, m: "Holy Light on them by up to 400, your Flash of Light by up to 115, and your Holy Shock by up to 229")],
}

# (class, spell) -> ([edits of every rank's text], {field: value} for every rank)
SPELLS = {}


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
