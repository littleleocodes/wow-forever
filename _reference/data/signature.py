"""Signature spells: the spells that make a spec that spec (user rule 2026-10-22: "make sure that the specs we're testing are actually
using the spells for that spec, or else it's pointless ... The specs should use the spells that make that spec, that spec. Especially the
hybrid ones."; strictness "main damage", leveling and raid). The rules are hand-kept in `signature_spells.json` (read its _doc); this
module reads them for the fight lab (rotation_opt.py, the open leveling search, open_builds.py, render_modes.py and
fightlab/signature_audit.py). The raid side reads the same file in raidsim/.

    rule(cls, spec, mode)            -> {"required", "core", "min_share", "note"} or None
    rule_specs(cls, spec, trees, mode) -> the specs whose rule a build must pass: its own, or a rule-less hybrid's trees' (any one)
    granting_talents(cls, spells)    -> the talents that grant required spells (a search keeps them; a build lacking one cannot qualify)
    core_share(shares, rule, pets)   -> the share of the damage the core sources carry ("melee", "pet", "Auto Shot", spell names)
    rotation_specs(cls, rot)         -> the specs (trees and hybrids) whose leveling builds play a fight-lab rotation
    rotation_required(cls, rot)      -> the required spells of every spec that levels with that rotation (rotation_opt protects them)
    check_levels(cls, spec, build, per_level, mode) -> the verdict of a build's fight-lab results against its spec's rule
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
FILE = HERE / "signature_spells.json"
_DATA = []
# fight-lab damage names that belong to a core source of another name (the lab books Windfury Weapon's extra attacks as "Windfury",
# Combat's Hack and Slash extra swings under their talent, the hawk's swings under Summon Hawk)
ALIASES = {"Windfury": "Windfury Weapon", "Hack and Slash": "melee", "Melee": "melee", "Melee (off-hand)": "melee", "Wand": "wand",
           "Summon Hawk": "pet"}
# a required spell counts as played at a level when it is cast at least this often per kill, or half of what its cooldown allows
MIN_CASTS_PER_KILL = 0.5


def data():
    if not _DATA:
        _DATA.append(json.load(open(FILE, encoding="utf-8")))
    return _DATA[0]


def rule(cls, spec, mode="leveling"):
    r = (data().get(cls) or {}).get(spec)
    if not r:
        return None
    out = {k: r.get(k) for k in ("required", "core", "min_share", "note", "min_casts", "enabled_by", "grace_levels")}
    out.update(((r.get("modes") or {}).get(mode)) or {})
    out["required"] = list(out.get("required") or [])
    out["core"] = list(out.get("core") or [])
    out["min_share"] = float(out.get("min_share") or 0.0)
    out["min_casts"] = dict(out.get("min_casts") or {})     # optional {spell: casts per kill} (a proc or reactive spell: Arcane Missiles
    out["enabled_by"] = dict(out.get("enabled_by") or {})   # on Missile Barrage); optional {spell: talent}: counted from that talent's level
    out["grace_levels"] = dict(out.get("grace_levels") or {})   # optional {spell: levels}: counted that many levels after it is learned
    return out


def rule_specs(cls, spec, trees=None, mode="leveling"):
    """The specs whose rule a build filed under `spec` must pass (any one of them): its own; a hybrid without a rule of its own, the rules
    of its two trees, only the trees the rotation is built for when `trees` names any of them (2026-10-23: the paladin's Holy leveling
    rotation found a 17/17/17 Holy/Protection Seal of Command build without Holy Shock, which passed as 'no rule')."""
    if rule(cls, spec, mode):
        return [spec]
    if not spec or not spec.startswith("Hybrid "):
        return []
    two = spec[len("Hybrid "):].split("/")
    own = [t for t in two if trees and t in trees]
    return [t for t in (own or two) if rule(cls, t, mode)]


def specs_of(cls):
    return [k for k in (data().get(cls) or {}) if not k.startswith("_")]


_TAL = {}


def talent_names(cls):
    if cls not in _TAL:
        _TAL[cls] = {t["name"] for tr in json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"] for t in tr["talents"]}
    return _TAL[cls]


def granting_talents(cls, spells):
    """The required spells that a talent grants (the talent has the spell's name: Holy Shock, Mortal Strike, Arcane Blast ...)."""
    tal = talent_names(cls)
    return [s for s in spells if s in tal]


_BOOK = {}


def spellbook(cls):
    """{spell name: (trainer level of rank 1, cooldown seconds)} from forever-spells/<class>.json."""
    if cls not in _BOOK:
        out = {}
        p = HERE / "forever-spells" / f"{cls}.json"
        for tab in (json.load(open(p, encoding="utf-8")).get("tabs", []) if p.exists() else []):
            for s in tab.get("spells", []):
                ranks = [r for r in s.get("ranks", []) if r.get("level") is not None]
                if not ranks:
                    continue
                cd = 0.0
                m = re.match(r"([\d.]+)\s*(sec|min)", (ranks[-1].get("cooldown") or "").strip())
                if m:
                    cd = float(m.group(1)) * (60 if m.group(2) == "min" else 1)
                lv = min(int(r["level"]) for r in ranks)
                if s["name"] not in out or lv < out[s["name"]][0]:
                    out[s["name"]] = (lv, cd)
        _BOOK[cls] = out
    return _BOOK[cls]


def held(build_or_alloc):
    alloc = build_or_alloc.get("allocation", build_or_alloc) if isinstance(build_or_alloc, dict) else {}
    if alloc and all(isinstance(v, list) for v in alloc.values()):
        return {n: r for items in alloc.values() for n, r in items if r}
    return {n: r for n, r in alloc.items() if r}


def learn_level(cls, spell, build):
    """The level a build can first cast `spell`: a talent spell at the first level its order gives the talent (60 without an order),
    None when the build does not take the talent; a trained spell at its trainer level (1 when the spellbook does not list it)."""
    if spell in talent_names(cls):
        if spell not in held(build):
            return None
        for step in build.get("order") or []:
            if step.get("talent") == spell:
                return int(str(step["levels"]).split("-")[0])
        return 60
    return spellbook(cls).get(spell, (1, 0.0))[0]


# ------------------------------------------------------------------------------------------------ signature talents as early as the tree allows
# 2026-11-06 (user decision on page-audit K5, "Go with your recs": "Signature talent timing. Take it as early as the tree allows"): the
# checks counted a talent spell from the level the build's order takes its talent, and the orders were picked on speed alone, so the
# Assassination page took Mutilate at 60, Subtlety Hemorrhage at 54 and Death Mark at 60, Beast Mastery Bestial Wrath at 56, Holy
# (paladin) Holy Shock at 60: a spec that levels for fifty levels without the spell that makes it that spec. A leveling order now
# takes every talent that grants a required spell at the earliest level its tree allows (`late_talents` fails the check otherwise;
# `signature_first` is the order every leveling tool starts from).
_INFO = {}


def talent_info(cls):
    """{talent: {"tree", "row" (0-based), "max", "req": [(talent, rank)]}} of the current trees (validate_builds.load_forever)."""
    if cls not in _INFO:
        if sys.path[:1] != [str(HERE)]:
            sys.path.insert(0, str(HERE))
        import validate_builds as VB
        for c, trees in VB.load_forever().items():
            _INFO[c] = {n: {"tree": tn, "row": int(t["row"]), "max": int(t["max"]), "req": [(q, int(r)) for q, r in t["requires"]]}
                        for tn, tr in trees.items() for n, t in tr["talents"].items()}
    return _INFO.get(cls, {})


def signature_talents(cls, rl, build):
    """The talents that grant the rule's required spells and that the build holds, in the order they are learned: the lower row first."""
    info, have = talent_info(cls), held(build)
    return sorted((s for s in granting_talents(cls, (rl or {}).get("required") or []) if have.get(s) and s in info),
                  key=lambda s: (info[s]["row"], s))


def earliest_levels(cls, rl, build):
    """{signature talent: the earliest level its tree allows}. A talent of row r is its tree's point 5r + 1, so level 10 + 5r (Mutilate
    40, Pyroblast 20); two in one tree: the tree's points simply go on (Hemorrhage 30, Death Mark 40); two in different trees: the lower
    row first, the other tree's points after it."""
    info, need, out = talent_info(cls), {}, {}
    for s in signature_talents(cls, rl, build):
        t = info[s]["tree"]
        need[t] = max(need.get(t, 0), 5 * info[s]["row"]) + 1
        out[s] = 9 + sum(need.values())
    return out


def late_talents(cls, rl, build):
    """[(talent, the level the build's order takes it, the earliest level its tree allows)] for the signature talents taken later than
    the tree allows; [] for a build without an order (nothing to judge)."""
    if not (build.get("order") or []):
        return []
    out = []
    for s, lv in earliest_levels(cls, rl, build).items():
        got = learn_level(cls, s, build)
        if got is not None and got > lv:
            out.append((s, int(got), int(lv)))
    return out


def order_points(order):
    """A compressed order as one (tree, talent) per point."""
    return [(s["tree"], s["talent"]) for s in order for _ in range(int(s["points"]))]


def order_alloc(order):
    """{talent: points} an order ends on."""
    out = {}
    for s in order:
        out[s["talent"]] = out.get(s["talent"], 0) + int(s["points"])
    return out


def compress_points(points, start=10):
    """One (tree, talent) per point -> the builds' compressed order (levels from `start`)."""
    out = []
    for i, (tree, name) in enumerate(points):
        lv = start + i
        if out and out[-1]["talent"] == name:
            out[-1]["points"] += 1
            out[-1]["levels"] = f"{out[-1]['levels'].split('-')[0]}-{lv}"
        else:
            out.append({"levels": str(lv), "tree": tree, "talent": name, "points": 1})
    return out


def _below(info, alloc, tree, row):
    return sum(r for n, r in alloc.items() if info[n]["tree"] == tree and info[n]["row"] < row)


def _addable(info, alloc, name):
    i = info[name]
    if alloc.get(name, 0) >= i["max"]:
        return False
    if i["row"] and _below(info, alloc, i["tree"], i["row"]) < 5 * i["row"]:
        return False
    return all(alloc.get(q, 0) >= qr for q, qr in i["req"])


def legal_points(cls, points):
    """Every prefix of a per-point order is a legal partial build (rank caps, 5 points per tier, prerequisites)."""
    info, alloc = talent_info(cls), {}
    for _, name in points:
        if name not in info or not _addable(info, alloc, name):
            return False
        alloc[name] = alloc.get(name, 0) + 1
    return True


def signature_first(cls, rl, build):
    """The build's order with every signature talent at the earliest level its tree allows (earliest_levels). For each one, the lower
    row first: its tree's points of the rows above it come forward in the order they already had, as many as its row needs (the
    talent's prerequisites among them), then the talent; every other point keeps its place in line. Returns the order itself when
    nothing is late, when the build has no order, or when no legal order could be made (the check then says what is late)."""
    order = build.get("order") or []
    if not order or not late_talents(cls, rl, build):
        return order
    info = talent_info(cls)
    rest = order_points(order)
    if any(n not in info for _, n in rest):
        return order
    out, alloc = [], {}

    def take(i):
        p = rest.pop(i)
        out.append(p)
        alloc[p[1]] = alloc.get(p[1], 0) + 1

    for s in signature_talents(cls, rl, build):
        if alloc.get(s):
            continue
        tree, row = info[s]["tree"], info[s]["row"]
        must, stack = {}, [s]   # the prerequisite chain: the ranks that have to be in before the talent
        while stack:
            for q, qr in info[stack.pop()]["req"]:
                if must.get(q, 0) < qr:
                    must[q] = qr
                    stack.append(q)
        while True:
            have = _below(info, alloc, tree, row)
            owed = sum(max(0, qr - alloc.get(q, 0)) for q, qr in must.items())
            if have >= 5 * row and not owed:
                break
            free = 5 * row - have - owed   # the points left for talents outside the chain
            pick = next((i for i, (t, n) in enumerate(rest) if t == tree and n != s and info[n]["row"] < row
                         and (alloc.get(n, 0) < must.get(n, 0) or free > 0) and _addable(info, alloc, n)), None)
            if pick is None:
                return order
            take(pick)
        i = next((i for i, (_, n) in enumerate(rest) if n == s), None)
        if i is None or not _addable(info, alloc, s):
            return order
        take(i)
    out += rest
    return compress_points(out) if legal_points(cls, out) else order


def min_casts(cls, spell, time_per_kill):
    """Casts per kill that count as playing the spell: MIN_CASTS_PER_KILL, or half of what its cooldown allows in a kill's time."""
    cd = spellbook(cls).get(spell, (1, 0.0))[1]
    if cd <= 0 or not time_per_kill:
        return MIN_CASTS_PER_KILL
    return min(MIN_CASTS_PER_KILL, 0.5 * time_per_kill / cd)


def source_of(name, pets=()):
    if name in pets:
        return "pet"
    if name.endswith(" melee") and name != "Melee":   # a pet's or demon's swings ("Cat melee", "Voidwalker melee")
        return "pet"
    return ALIASES.get(name, name)


def core_share(shares, rl, pets=()):
    """The share of the damage the rule's core sources carry. A damage name that extends a core spell's name counts as that spell (the
    lab books Pyroblast's burn as "Pyroblast burn")."""
    core = set(rl["core"])

    def is_core(k):
        src = source_of(k, pets)
        return src in core or any(src.startswith(c + " ") for c in core if c not in ("melee", "pet", "wand"))
    return sum(v for k, v in (shares or {}).items() if is_core(k))


def kills_of(r):
    return max(1, int(r.get("kills") or 0))


def casts_per_kill(r, spell):
    return (r.get("casts") or {}).get(spell, 0) / kills_of(r)


def check_levels(cls, spec, build, per_level, mode="leveling", rl=None):
    """A build's fight-lab results ({level: Session result with shares, casts, kills, pet_sources}) against its spec's rule.
    {"ok", "missing_talents", "uncast": [(spell, level, casts per kill, needed)], "core_share" (at the highest level), "min_share", "rule"}."""
    rl = rl or rule(cls, spec, mode)
    if not rl:
        return {"ok": True, "rule": None, "missing_talents": [], "uncast": [], "late": [], "core_share": None, "min_share": None}
    miss = [s for s in granting_talents(cls, rl["required"]) if s not in held(build)]
    late = late_talents(cls, rl, build) if mode == "leveling" else []   # 2026-11-06: a signature talent taken later than its tree allows
    uncast = []
    checked = list(rl["required"]) + [s for s in (rl.get("min_casts") or {}) if s not in rl["required"]]
    for spell in checked:   # the required spells, and the spells given a cast rate only (reactive: Mongoose Bite)
        lv0 = learn_level(cls, spell, build)
        by = (rl.get("enabled_by") or {}).get(spell)
        if by and lv0 is not None:   # a proc spell counts from the talent that makes it fire (None: the build lacks that talent)
            lb = learn_level(cls, by, build)
            lv0 = None if lb is None else max(lv0, lb)
        if lv0 is None:
            continue
        lv0 += int((rl.get("grace_levels") or {}).get(spell, 0))
        for L, r in sorted(per_level.items(), key=lambda kv: int(kv[0])):
            if int(L) < lv0:
                continue
            need = (rl.get("min_casts") or {}).get(spell, min_casts(cls, spell, r.get("time_per_kill")))
            got = casts_per_kill(r, spell)
            if got < need:
                uncast.append((spell, int(L), round(got, 3), round(need, 3)))
    top = max(per_level, key=lambda L: int(L)) if per_level else None
    cs = core_share(per_level[top].get("shares"), rl, per_level[top].get("pet_sources") or ()) if top is not None else None
    ok = not miss and not uncast and not late and (cs is None or cs >= rl["min_share"])
    return {"ok": ok, "rule": rl, "missing_talents": miss, "uncast": uncast, "late": late, "core_share": cs, "min_share": rl["min_share"],
            "level": int(top) if top is not None else None}


def verdict_text(v):
    if v["rule"] is None:
        return "no rule"
    bits = []
    if v["missing_talents"]:
        bits.append("lacks " + ", ".join(v["missing_talents"]))
    if v["uncast"]:
        bits.append("; ".join(f"{s} {g:.2f}/kill at {L} (needs {n:.2f})" for s, L, g, n in v["uncast"]))
    if v.get("late"):
        bits.append("; ".join(f"{s} taken at {g} (its tree allows {e})" for s, g, e in v["late"]))
    if v["core_share"] is not None and v["core_share"] < v["min_share"]:
        bits.append(f"core share {v['core_share']:.0%} < {v['min_share']:.0%}")
    return "OK" if v["ok"] else "FAIL: " + "; ".join(bits)


# ------------------------------------------------------------------------------------------------ rotations and the specs that play them
def rotation_specs(cls, rot):
    """The specs whose leveling builds play fight-lab rotation `rot`: the trees derive_leveling.LEVEL gives it (plus
    spec_modes.LEVELING_EXTRA_TREES) and the hybrids spec_modes.HYBRID_LEVELING_ROTATION gives it."""
    if sys.path[:1] != [str(HERE)]:   # this folder first: derive_leveling imports its own filelock.py, which the pip package of that
        sys.path.insert(0, str(HERE))  # name shadows when a script (fightlab/run.py) only appends the folder
    import spec_modes as SM
    out = sorted(SM.leveling_rotation_trees(cls).get(rot, set()))
    out += sorted(h for (c, h), r in SM.HYBRID_LEVELING_ROTATION.items() if c == cls and r == rot)
    return out


def rotation_required(cls, rot, mode="leveling"):
    """{required spell: [specs]} of every spec that levels with `rot`: rotation_opt.py never switches these off or starves them."""
    out = {}
    for spec in rotation_specs(cls, rot):
        rl = rule(cls, spec, mode)
        for s in (rl or {}).get("required", []):
            out.setdefault(s, []).append(spec)
    return out
