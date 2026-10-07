"""Specs and modes (2026-09-29, user request: "each class's 3 specs get a build for each of the 3 modes: leveling, raid/dummy/parse,
PvP; a split like 0/29/22 is its own hybrid section").

The one place that decides which spec a build belongs to (render_modes.py and spec_builds.py use it):

- a tank build belongs to the class's tank tree (Protection, Feral Combat), a healer build to its healing tree (the one of Holy /
  Discipline / Restoration it spends most in): a role, whatever the split;
- otherwise the tree with 30 or more points is the spec;
- otherwise the build is a hybrid of its two biggest trees, named in the class's tree order ("Fire/Frost");
- a build's own `spec` field overrides all of this: builds played around another tree's spells are filed as hybrids although one
  tree has 30 points (Frostfire 0/35/16 casts Frostfire Bolt; Shockadin 31/0/20 heals and shocks as a melee; Smite 31/17/3 is a
  Discipline build that casts Holy spells). The user left the judgment to us (2026-09-29).

Modes: leveling (content leveling or solo), raid (raid or dungeon: the training dummy and the parse/raid setting), pvp.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
MODES = ("leveling", "raid", "pvp")
MODE_TITLE = {"leveling": "Leveling (solo)", "raid": "Raid (group)", "pvp": "PvP"}   # 2026-10-02: leveling ranks solo play, raid the full raid group
SPEC_POINTS = 30
HEAL_TREES = {"priest": ("Holy", "Discipline"), "paladin": ("Holy",), "shaman": ("Restoration",), "druid": ("Restoration",)}
TANK_TREE = {"warrior": "Protection", "paladin": "Protection", "druid": "Feral Combat"}
# healer and tank specs level as a damage spec and respec at 60 (agreed 2026-09-29): the spec they level as
LEVEL_AS = {("druid", "Restoration"): "Feral Combat", ("paladin", "Holy"): "Retribution", ("paladin", "Protection"): "Retribution",
            ("priest", "Discipline"): "Shadow", ("priest", "Holy"): "Shadow", ("shaman", "Restoration"): "Enhancement",
            ("warrior", "Protection"): "Arms"}


# player names for the hybrids (hand-kept, 2026-09-29: "name the hybrids the way players do"): (name, page slug, one line on what it is)
HYBRID_NAMES = {
    ("hunter", "Hybrid Beast Mastery/Marksmanship"): ("Beast-Marks", "beast-marks", "Marksmanship's shots with Beast Mastery's pet talents: the classic raid hunter split."),
    ("hunter", "Hybrid Marksmanship/Survival"): ("Melee (split)", "melee-split", "Dual-wield melee with Marksmanship support, short of 30 Survival points."),
    ("hunter", "Hybrid Beast Mastery/Survival"): ("Beast-Survival", "beast-survival", "Dual-wield melee with Beast Mastery's aspect and pet talents (Summon Hawk and Lone Wolf in a raid, a pet while leveling), short of 30 Survival points."),
    ("mage", "Hybrid Arcane/Frost"): ("Arcane-Frost", "arcane-frost", "A Frostbolt caster with Arcane's mana and cooldown talents (Arcane Power, Presence of Mind)."),
    ("mage", "Hybrid Fire/Frost"): ("Frostfire", "frostfire", "Built around Frostfire Bolt, a new Forever spell that uses both trees."),
    ("paladin", "Hybrid Holy/Retribution"): ("Shockadin", "shockadin", "Holy Shock burst and heals with Retribution's melee talents."),
    ("paladin", "Hybrid Protection/Retribution"): ("Prot-Ret", "prot-ret", "Retribution's melee talents with Protection's Seal of Fury, Swift Judgement and Toughness: a melee split short of 30 Retribution points."),
    ("priest", "Hybrid Discipline/Holy"): ("Smite", "smite", "Damage from Smite and Holy Fire, carried by Discipline talents."),
    ("rogue", "Hybrid Assassination/Combat"): ("Daggers (split)", "daggers-split", "Daggers with points split between Assassination and Combat."),
    ("shaman", "Hybrid Elemental/Enhancement"): ("Elemental-Enhancement", "elemental-enhancement", "A Lightning Bolt caster that dips Enhancement for its passive bonuses."),
    ("warlock", "Hybrid Affliction/Destruction"): ("Shadow Bolt hybrid", "shadow-bolt-hybrid", "Shadow Bolt and fire casters mixing Affliction's curses with Destruction's Ruin (DS/Ruin)."),
    ("warlock", "Hybrid Affliction/Demonology"): ("Affliction-Demonology", "affliction-demonology", "Dots with a Voidwalker tanking: the classic warlock leveling split."),
}


def spec_name(cls, spec):
    """What a player calls the spec: the tree name, or the hybrid's name."""
    if (cls, spec) in HYBRID_NAMES:
        return HYBRID_NAMES[(cls, spec)][0]
    return spec.replace("Hybrid ", "") + " hybrid" if spec.startswith("Hybrid") else spec


def spec_slug(cls, spec):
    """The spec's page name in the mode folders."""
    return HYBRID_NAMES[(cls, spec)][1] if (cls, spec) in HYBRID_NAMES else slug(spec)


def trees(cls):
    return [t["name"] for t in json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]]


def tree_points(cls, build):
    return {t: sum(r for _, r in build["allocation"].get(t, [])) for t in trees(cls)}


def mode_of(build):
    return {"leveling": "leveling", "solo": "leveling", "raid": "raid", "dungeon": "raid", "pvp": "pvp"}.get(build.get("content"), "raid")


def spec_of(cls, build):
    """The spec a build belongs to: a tree name, or 'Hybrid A/B'."""
    if build.get("spec"):
        return build["spec"]
    pts = tree_points(cls, build)
    if build.get("role") == "tank" and cls in TANK_TREE:
        return TANK_TREE[cls]
    if build.get("role") == "healer" and cls in HEAL_TREES:
        return max(HEAL_TREES[cls], key=lambda t: pts.get(t, 0))
    top = sorted(pts, key=lambda t: -pts[t])
    if pts[top[0]] >= SPEC_POINTS:
        return top[0]
    return "Hybrid " + "/".join(t for t in pts if t in top[:2])   # the class's tree order, so 22/29 and 29/22 share a section


def slug(spec):
    return spec.lower().replace("hybrid ", "hybrid-").replace("/", "-").replace(" ", "-")


def grid(cls, builds):
    """{spec: {mode: [build, ...]}} with the class's three trees first (empty where no build exists), hybrids after."""
    out = {t: {m: [] for m in MODES} for t in trees(cls)}
    for b in builds:
        out.setdefault(spec_of(cls, b), {m: [] for m in MODES})[mode_of(b)].append(b)
    return out
