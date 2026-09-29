"""How useful a talent is in a real raid beyond what the simulators measure (2026-09-29, user question on zero-value fillers).

A tag read from the beta tooltip, in order of usefulness: interrupt/pushback protection, threat reduction, mana cost, range, survival
(tanks: survival first); a talent with none ranks last. Used by raidsim/filler_audit.py to move zero-value points and by the scorer as
a tie-break in the raid profiles (TIE_BREAK per point, far below any measured effect), so optimizer builds make the same choice.
The simulators model no pushback, range, threat limit or (for DPS) incoming damage: the order is our judgment, not a measurement.
"""
import functools
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
TAGS = [("interrupt", r"interrupt|pushback|casting time lost|lose .* casting time|avoid interruption"),
        ("threat", r"threat"),
        ("mana", r"mana cost|reduces the mana|restores? .*mana|mana regeneration|regenerat.* mana"),
        ("range", r"\brange\b|radius"),
        ("survival", r"stamina|armor|damage taken|resistances?|dodge|parry|block|health")]
NONE = len(TAGS)
# talents whose tag is true but useless in a raid (a pet's revive or healing, crowd control, distraction): no raid usefulness
NO_RAID = {"Improved Revive Pet", "Improved Mend Pet", "Improved Health Funnel", "Fel Domination", "Improved Distract", "Scatter Shot",
           "Nature's Focus", "Improved Sprint", "Endurance", "Camouflage", "Master of Deception", "Improved Ghost Wolf", "Pathfinding",
           "Feral Swiftness", "Improved Concussive Shot", "Entrapment", "Improved Hamstring", "Piercing Howl"}
TIE_BREAK = 1e-5   # score per point per step of usefulness in the raid profiles
RAID_PROFILES = {"raid-dps", "raid-dps-extwc", "parse", "raid-tank"}


@functools.lru_cache(maxsize=None)
def usefulness(cls, tank=False):
    """{talent: rank (0 = most useful, NONE = no tag)} from the Forever beta tooltips."""
    order = [t for t, _ in TAGS]
    if tank:
        order = ["survival"] + [t for t in order if t != "survival"]
    out = {}
    for tr in json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]:
        for t in tr["talents"]:
            ranks = t.get("ranks") or []
            txt = str(ranks[-1] if ranks else "").lower()
            tags = [tag for tag, rx in TAGS if re.search(rx, txt)]
            out[t["name"]] = NONE if t["name"] in NO_RAID else min((order.index(g) for g in tags), default=NONE)
    return out


def tie_break(cls, alloc, tank=False):
    """The raid profiles' tie-break for an allocation {talent: rank}."""
    u = usefulness(cls, tank)
    return TIE_BREAK * sum(r * (NONE - u.get(n, NONE)) for n, r in alloc.items())
