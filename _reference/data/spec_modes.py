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


# player names for the hybrids (hand-kept, 2026-09-29: "name the hybrids the way players do"): (name, page slug, one line on what it is).
# The line is a string, or {mode: line} when the hybrid's leveling and raid builds differ (2026-10-15 page audit C5: one line had served
# both modes, so the melee Elemental-Enhancement raid page read "a Lightning Bolt caster"); `hybrid_line` picks it. Lines name only
# talents the page's build holds (checked 2026-10-15 against the page picks).
HYBRID_NAMES = {
    ("hunter", "Hybrid Beast Mastery/Marksmanship"): ("Beast-Marks", "beast-marks", {
        "raid": "Beast Mastery's pet talents with Marksmanship's shot talents (Mortal Shots, Improved Arcane Shot, Careful Aim): a pet build "
                "short of 30 Beast Mastery points.",   # 2026-11-08 full page read H3: the raid pick 28/21/2 has no Trueshot Aura, Barrage, Sniper Shot
        "leveling": "Beast Mastery's pet talents (Ferocity, Frenzy, Spirit Bond) with Marksmanship's shot talents."}),
    ("hunter", "Hybrid Marksmanship/Survival"): ("Melee (split)", "melee-split", "Dual-wield melee with Marksmanship support, short of 30 Survival points."),
    ("hunter", "Hybrid Beast Mastery/Survival"): ("Beast-Survival", "beast-survival", "Dual-wield melee with Beast Mastery's aspect and pet talents (Summon Hawk and Lone Wolf in a raid, a pet while leveling), short of 30 Survival points."),
    ("mage", "Hybrid Arcane/Frost"): ("Arcane-Frost", "arcane-frost", {
        "raid": "Arcane's Missile Barrage, Arcane Wrath, Arcane Mind and Arcane Instability on a Frostbolt filler (Improved Frostbolt, Ice Shards).",
        "leveling": "Frost's Shatter and Fingers of Frost with Arcane's Missile Barrage: Frostbolt, Ice Lance into the freeze, free Arcane Missiles."}),
    ("mage", "Hybrid Fire/Frost"): ("Frostfire", "frostfire", "Built around Frostfire Bolt, a new Forever spell that uses both trees."),
    ("paladin", "Hybrid Holy/Retribution"): ("Shockadin", "shockadin", {
        "leveling": "Retribution's two-handed melee (Vengeance, Two-Handed Weapon Specialization) with Holy's Sacred Arbiter; despite the name, the open leveling search's winner takes no Holy Shock.",
        "raid": "Holy Shock burst and heals with Retribution's melee talents."}),
    ("paladin", "Hybrid Protection/Retribution"): ("Prot-Ret", "prot-ret", "Retribution's melee talents with Protection's Seal of Fury, Swift Judgement and Toughness: a melee split short of 30 Retribution points."),
    ("priest", "Hybrid Discipline/Holy"): ("Smite", "smite", "Damage from Smite and Holy Fire, carried by Discipline talents."),
    ("priest", "Hybrid Discipline/Shadow"): ("Discipline-Shadow", "hybrid-discipline-shadow", "Shadow's dots and Shadow Weaving, Vampiric Embrace and Darkness with Discipline's Mental Strength and Soul Warding."),
    ("priest", "Hybrid Holy/Shadow"): ("Holy-Shadow", "hybrid-holy-shadow", "Points in all three trees: Discipline's Soul Warding, Holy's Searing Light and Shadow's Shadow Weaving."),
    ("rogue", "Hybrid Assassination/Combat"): ("Daggers (split)", "daggers-split", "Daggers with points split between Assassination and Combat."),
    ("rogue", "Hybrid Combat/Subtlety"): ("Combat-Subtlety", "combat-subtlety", "Subtlety's openers, Ghostly Strike and Hemorrhage with Combat's weapon talents (2026-10-08, the open leveling search)."),
    ("shaman", "Hybrid Elemental/Enhancement"): ("Elemental-Enhancement", "elemental-enhancement", {
        "leveling": "A Lightning Bolt caster (Lightning Overload) that dips Enhancement for its passive bonuses.",
        "raid": "A melee shaman: Enhancement's Stormstrike and Flurry with Elemental's shock and Fire Nova talents."}),
    ("warlock", "Hybrid Affliction/Destruction"): ("Shadow Bolt hybrid", "shadow-bolt-hybrid", {
        "raid": "Shadow Bolt with Affliction's Malevolence and Destruction's Agonizing Flames, points in all three trees.",
        "leveling": "Shadow Bolt and dots with Affliction's Malevolence, Siphon Life and Shadow Mastery, a few Demonology and Destruction points."}),
    ("warlock", "Hybrid Affliction/Demonology"): ("Affliction-Demonology", "affliction-demonology", "Dots and Siphon Life with a demon tanking (Soul Link, Demonic Knowledge): the classic warlock leveling split."),
}


def hybrid_line(cls, spec, mode=None):
    """The one line on what a hybrid is, for a mode's page (the raid line when no mode is given)."""
    line = HYBRID_NAMES[(cls, spec)][2]
    return line if isinstance(line, str) else line.get(mode or "raid") or next(iter(line.values()))


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
    ("paladin", "shockadin-raid"): {"Hybrid Holy/Retribution"},   # 2026-10-24: Shockadin under the signature rule (sweep_raid2.sh)
    ("shaman", "elemental-dps"): {"Elemental"}, ("shaman", "enhancement-dps"): {"Enhancement"}, ("shaman", "stormcaller-dps"): {"Elemental"},
    ("druid", "balance-dps"): {"Balance"}, ("druid", "feral-cat-dps"): {"Feral Combat"}, ("druid", "feral-bear-tank"): {"Feral Combat"},
}
# weapon and stance variants of a spec's raid play (2026-10-08, the improvement log's "weapon variants on the pages": the rogue's swords
# entry found a build 1.9% ahead of our swords builds, hidden behind the daggers pick): the open-build writer keeps each variant's best
# build next to the spec's pick, and the page lists it among the spec's other builds
RAID_ENTRY_VARIANT = {
    ("rogue", "combat-swords-raid"): "Swords", ("rogue", "combat-daggers-raid"): "Daggers",
    ("warrior", "arms-2h-raid"): "Two-handed", ("warrior", "fury-dw-raid"): "Dual-wield", ("warrior", "arms-battle-raid"): "Battle Stance",
    ("hunter", "mm-raid"): "With a pet", ("hunter", "mm-lonewolf-raid"): "Lone Wolf",
    ("warlock", "fire-destro-raid"): "Fire", ("warlock", "sb-raid"): "Shadow Bolt", ("warlock", "incinerate-raid"): "Incinerate",
    ("shaman", "stormcaller-dps"): "Stormcaller",
}
# leveling rotations come from derive_leveling.LEVEL (each tree's rotation; a healing tree without one levels as LEVEL_AS's damage spec,
# the 2026-09-29 agreement); a weapon variant of a tree's rotation counts as that tree's too:
LEVELING_EXTRA_TREES = {("rogue", "combat-daggers-raid"): {"Combat"}}


# the fight-lab rotation each hybrid levels with (user rule 2026-10-22: "make sure that the specs we're testing are actually using the
# spells for that spec ... the Frostfire mage leveling build doesn't even use Frostfire. It uses Fireball"): the rotation that plays the
# hybrid's signature spells (signature_spells.json), not its lead tree's. The lead-tree rule had given Frostfire the Fire rotation
# (Fireball), the Discipline-Shadow priest the Penance rotation. A hybrid levels with this rotation only (leveling_rotation_ok).
HYBRID_LEVELING_ROTATION = {
    ("hunter", "Hybrid Beast Mastery/Marksmanship"): "bm-leveling",    # the pet with Aimed Shot (the BM list casts it when the build has it)
    ("hunter", "Hybrid Marksmanship/Survival"): "melee-dps",
    ("hunter", "Hybrid Beast Mastery/Survival"): "melee-dps",
    ("mage", "Hybrid Arcane/Frost"): "barrage-frost-leveling",         # Frostbolt with Missile Barrage's Arcane Missiles (fightlab/mage.py
                                                                        # is_barrage, 2026-10-22: the Frost list never cast them)
    ("mage", "Hybrid Fire/Frost"): "frostfire-leveling",               # Frostfire Bolt from 40 (decide_frostfire)
    ("paladin", "Hybrid Holy/Retribution"): "holy-leveling",           # Shockadin: Holy Shock on cooldown
    ("paladin", "Hybrid Protection/Retribution"): "ret-dps",
    ("priest", "Hybrid Discipline/Holy"): "holy-leveling",             # Smite: Smite and Holy Fire
    ("priest", "Hybrid Discipline/Shadow"): "shadow-dps",              # Shadow's dots and Mind Flay
    ("priest", "Hybrid Holy/Shadow"): "holy-leveling",                 # Shadow Word: Pain and Holy Fire (the Holy list keeps the dot up)
    ("rogue", "Hybrid Assassination/Combat"): "combat-daggers-raid",   # Daggers: Backstab
    ("rogue", "Hybrid Combat/Subtlety"): "subtlety-leveling",          # Ghostly Strike and the openers
    ("shaman", "Hybrid Elemental/Enhancement"): "elemental-dps",       # a Lightning Bolt caster
    ("warlock", "Hybrid Affliction/Destruction"): "destruction-leveling",   # Shadow Bolt
    ("warlock", "Hybrid Affliction/Demonology"): "demonology-leveling",     # dots with the demon (Demonic Brand); the rotation it was found in
}


# A leveling rotation that files a split under one tree (2026-11-06, user decision on page-audit K3: "Make it the Feral page's build and
# drop the separate page"). The cat rotation's open winner was 11/29/11, one point short of 30 Feral Combat points, and had its own
# hybrid page ("Cat (split)") next to the Feral page, whose build was 0.5% slower. It casts only cat spells and the 30th point by
# itself unlocks nothing, so in that rotation a build with a majority of its points in the tree is a build of the tree
# (fl_signature.spec_for; open_builds.py writes it with `spec`: the tree). {(class, rotation): (tree, the points that make it the tree's)}
LEVELING_FILE_AS = {("druid", "feral-cat-dps"): ("Feral Combat", 26)}


def leveling_rotation_ok(cls, spec, rot, trees_=None):
    """Whether `spec` may be shown leveling with fight-lab rotation `rot`: a hybrid with a HYBRID_LEVELING_ROTATION only with that
    rotation (2026-10-22, the signature rule); otherwise rotation_allows on the rotation's trees. A rotation no tree levels with: only
    its hybrid's (a rotation unknown to both maps, a report's variant, stays allowed as before)."""
    if (cls, spec) in HYBRID_LEVELING_ROTATION:
        return rot == HYBRID_LEVELING_ROTATION[(cls, spec)]
    if trees_ is None:
        trees_ = leveling_rotation_trees(cls).get(rot)
    if not trees_:
        return rot not in {r for (c, _), r in HYBRID_LEVELING_ROTATION.items() if c == cls}
    return rotation_allows(spec, trees_)


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
    """The rotation a spec levels with: its tree's (derive_leveling.LEVEL); a hybrid's: HYBRID_LEVELING_ROTATION (the rotation that plays
    its signature spells, 2026-10-22), else its lead tree's (the most points in `alloc`)."""
    import derive_leveling as DL
    if (cls, spec) in HYBRID_LEVELING_ROTATION:
        return HYBRID_LEVELING_ROTATION[(cls, spec)]
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
    # 2026-11-06 (user decision on page-audit K7): a hybrid's leveling slot that holds nothing but optimizer exports (`opt-<model>-<profile>`:
    # builds of a tree's stats model whose points happen to split across two trees) is no page. The rogue's "Daggers (split)" leveling
    # page showed the swords model's AoE export, without numbers, as its only build once the daggers rotation's winner became a pure
    # Assassination build. The exports stay in the builds file and on the research pages.
    for spec, modes in out.items():
        if spec.startswith("Hybrid ") and modes["leveling"] and all(b["id"].startswith("opt-") for b in modes["leveling"]):
            modes["leveling"] = []
    return out
