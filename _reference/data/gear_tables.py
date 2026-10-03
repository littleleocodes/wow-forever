"""Markdown for the gear-tier sets with links (2026-10-03, user request: a way to see the actual pre-BiS and BiS items).

Reads raidsim/gear-links.json (written by raidsim/gear_links.py: every item and enchant with its Wowhead Forever link and source, and
share links that open each tier x setting character in the community simulator's live web UI). Used by render_modes.py (raid pages)
and raidsim/ml_builds.py --rank (_reference/dps-rankings.md). Without the file the callers fall back to plain item names.
"""
import functools
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
LINKS = HERE / "raidsim" / "gear-links.json"
TIER_NAME = {"prebis": "Pre-BiS", "bis": "Phase 1 BiS"}


@functools.lru_cache(maxsize=None)
def data():
    try:
        return json.load(open(LINKS, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def spec(cls, spec_name):
    return (data().get("specs") or {}).get(f"{cls}|{spec_name}")


def sim_link(cls, spec_name, key):
    """The simulator share link of a tier x setting ("bis-raid", "prebis-dummy" ...), or None."""
    return ((spec(cls, spec_name) or {}).get("sim") or {}).get(key)


def cell(row):
    """One item: its Wowhead link, where it comes from, its enchant."""
    out = f"[{row['name']}]({row['url']})"
    if row.get("source"):
        out += f" · *{row['source']}*"
    e = row.get("enchant")
    if e:
        out += "<br>+ " + (f"[{e['name']}]({e['url']})" if e.get("url") else e["name"])
    return out


def table(cls, spec_name):
    """Markdown lines: a Slot | Pre-BiS | Phase 1 BiS table of the spec's two sets, every item linked; [] without links."""
    s = spec(cls, spec_name)
    if not s or not s.get("gear"):
        return []
    tiers = [t for t in ("prebis", "bis") if t in s["gear"]]
    keyed = {}
    order = []
    for t in tiers:
        seen = {}
        for row in s["gear"][t]:
            n = seen.get(row["slot"], 0)
            seen[row["slot"]] = n + 1
            k = (row["slot"], n)
            if k not in keyed:
                keyed[k] = {}
                order.append(k)
            keyed[k][t] = row
    o = ["| Slot | " + " | ".join(TIER_NAME[t] for t in tiers) + " |", "|---" * (len(tiers) + 1) + "|"]
    for k in order:
        o.append(f"| {k[0]} | " + " | ".join(cell(keyed[k][t]) if t in keyed[k] else "-" for t in tiers) + " |")
    return o


def sim_line(cls, spec_name, raid_first=True):
    """'Open in the simulator' links for both tiers and settings, or ''."""
    s = spec(cls, spec_name)
    if not s or not s.get("sim"):
        return ""
    parts = []
    for t in ("prebis", "bis"):
        links = [f"[{lab}]({s['sim'][f'{t}-{st}']})" for st, lab in (("raid", "full raid"), ("dummy", "training dummy")) if s["sim"].get(f"{t}-{st}")]
        if links:
            parts.append(f"{TIER_NAME[t]}: " + " · ".join(links))
    return ("**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, "
            "rotation, consumables and buffs we simulate): " + "; ".join(parts) + ".") if parts else ""
