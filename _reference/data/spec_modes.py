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
    ("rogue", "Hybrid Combat/Subtlety"): ("Combat-Subtlety", "combat-subtlety", "Subtlety's openers, Ghostly Strike and Hemorrhage with Combat's weapon talents (2026-10-08, the open leveling search)."),
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


# ------------------------------------------------------------------------------------------------ each spec plays its own rotation
# User decision 2026-10-08: "I don't want classes specs taking other specs rotations or builds or anything just because it's faster."
# A build is ranked on its spec's page only with a rotation built for its own tree; a hybrid with a rotation of either of its two trees
# or one built for the hybrid itself (Frostfire's frostfire-raid, Smite's smite-dps). No step may move a build to another spec's rotation
# because it is faster there (the cross-rotation races stay as research). The trees each raid entry's rotation is built for:
RAID_ENTRY_TREES = {
    ("mage", "frost-raid"): {"Frost"}, ("mage", "fire-raid"): {"Fire"}, ("mage", "arcane-dps"): {"Arcane"},
    ("mage", "frostfire-raid"): {"Hybrid Fire/Frost"},
    ("priest", "shadow-dps"): {"Shadow"}, ("priest", "smite-dps"): {"Hybrid Discipline/Holy"},
    ("warlock", "affliction-raid"): {"Affliction"}, ("warlock", "fire-destro-raid"): {"Destruction"}, ("warlock", "sb-raid"): {"Destruction"},
    ("warlock", "demonology-raid"): {"Demonology"}, ("warlock", "incinerate-raid"): {"Destruction"},
    ("hunter", "mm-raid"): {"Marksmanship"}, ("hunter", "mm-lonewolf-raid"): {"Marksmanship"}, ("hunter", "bm-raid"): {"Beast Mastery"},
    ("hunter", "melee-dps"): {"Survival"},
    ("rogue", "combat-swords-raid"): {"Combat"}, ("rogue", "combat-daggers-raid"): {"Combat"}, ("rogue", "assassination-raid"): {"Assassination"},
    ("rogue", "subtlety-raid"): {"Subtlety"},
    # the simulator has one warrior DPS rotation for Arms and Fury; the two entries are its two-handed and dual-wield gear setups
    ("warrior", "arms-2h-raid"): {"Arms", "Fury"}, ("warrior", "fury-dw-raid"): {"Arms", "Fury"}, ("warrior", "arms-battle-raid"): {"Arms"},
    ("warrior", "prot-tank"): {"Protection"},
    ("paladin", "ret-dps"): {"Retribution"}, ("paladin", "prot-tank"): {"Protection"},
    ("shaman", "elemental-dps"): {"Elemental"}, ("shaman", "enhancement-dps"): {"Enhancement"}, ("shaman", "stormcaller-dps"): {"Elemental"},
    ("druid", "balance-dps"): {"Balance"}, ("druid", "feral-cat-dps"): {"Feral Combat"}, ("druid", "feral-bear-tank"): {"Feral Combat"},
}
# leveling rotations come from derive_leveling.LEVEL (each tree's rotation; a healing tree without one levels as LEVEL_AS's damage spec,
# the 2026-09-29 agreement); a weapon variant of a tree's rotation counts as that tree's too:
LEVELING_EXTRA_TREES = {("rogue", "combat-daggers-raid"): {"Combat"}}


def rotation_allows(spec, trees_):
    """Whether a rotation built for `trees_` is `spec`'s own: the spec itself, or for a hybrid either of its two trees."""
    if not trees_:
        return False
    if spec in trees_:
        return True
    if spec.startswith("Hybrid "):
        return any(t in trees_ for t in spec[len("Hybrid "):].split("/"))
    return False


def leveling_rotation_trees(cls):
    """{fight-lab rotation: {trees it is built for}} of a class (derive_leveling.LEVEL plus LEVELING_EXTRA_TREES)."""
    import derive_leveling as DL   # (imported here: derive_leveling imports this module)
    out = {}
    for (c, tree), (rot, _model) in DL.LEVEL.items():
        if c == cls:
            out.setdefault(rot, set()).add(tree)
    for (c, rot), ts in LEVELING_EXTRA_TREES.items():
        if c == cls:
            out.setdefault(rot, set()).update(ts)
    return out


def own_leveling_rotation(cls, spec, alloc=None):
    """The rotation a spec levels with: its tree's (derive_leveling.LEVEL); a hybrid's: its lead tree's (the most points in `alloc`)."""
    import derive_leveling as DL
    tree = spec
    if spec.startswith("Hybrid ") and alloc:
        pts = {t: sum(k for _, k in items) for t, items in alloc.items()}
        parts = spec[len("Hybrid "):].split("/")
        tree = max(parts, key=lambda t: pts.get(t, 0))
    hit = DL.LEVEL.get((cls, tree))
    return hit[0] if hit else None


def grid(cls, builds):
    """{spec: {mode: [build, ...]}} with the class's three trees first (empty where no build exists), hybrids after."""
    out = {t: {m: [] for m in MODES} for t in trees(cls)}
    for b in builds:
        out.setdefault(spec_of(cls, b), {m: [] for m in MODES})[mode_of(b)].append(b)
    return out
