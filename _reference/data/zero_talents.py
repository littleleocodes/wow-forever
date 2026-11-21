"""The one source for a page's "points that do nothing" (2026-11-21, the audit session's B13: the Marksmanship page listed Trueshot Aura as
doing nothing while its removal changes the result; the line had come from page_lint.dead_talents, a reading of the tooltips against
the page's text). A talent does nothing only when a removal run says so:
- raid builds: the raid play check's zero talents (raidsim/play-check.json: the talent's removal leaves the full-raid DPS the same to
  the cent), with the check's reason for each (a gate's kind, a recorded filler, a utility tag, the raid's own buff);
- leveling builds: the leveling filler pass's record made on the build's own order (fightlab/filler/<class>-<slug>.json, its
  `no_better_home` entries whose removal is exact, with the gate's kind).

    raid(cls, bid, entry=None) -> {talent: why}
    leveling(cls, slug, order) -> {talent: why}
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent


def raid(cls, bid, entry=None):
    p = HERE / "raidsim" / "play-check.json"
    try:
        rec = json.load(open(p, encoding="utf-8")).get(cls) or {}
    except (OSError, ValueError):
        return {}
    ents = [entry] if entry in rec else list(rec)
    out = {}
    for e in ents:
        for line in ((rec.get(e) or {}).get("builds") or {}).get(bid, {}).get("zero_talents") or []:
            t, _, why = line.partition(": ")
            out.setdefault(re.sub(r" \d+$", "", t), why)
        if out and entry in rec:
            break
    return out


def leveling(cls, slug, order):
    out = {}
    if not slug:
        return out
    for p in (HERE / "fightlab" / "filler" / f"{cls}-{slug}.json",):
        try:
            x = json.load(open(p, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if x.get("final_order") != order:
            continue
        for t, e in (x.get("no_better_home") or {}).items():
            if e.get("exact", e.get("kind") != "zero point"):
                out[t] = e.get("kind") or "zero point"
    return out
