"""Turn talent tooltips into numeric effects.

An *effect* is {"channel": ..., "scope": [...tags...], "values": [cumulative value at rank 1..n], "note": ...}.

Channels (what the number does)            value unit
  dmg          multiplies damage of matching sources          fraction (0.05 = +5%)
  crit         adds crit chance to matching sources           fraction
  crit_bonus   adds to the crit damage bonus (base 0.5 spell / 1.0 melee-ranged)   fraction
  hit          removes miss chance for matching sources       fraction
  haste        expected attack/cast speed increase            fraction (proc EV already folded in)
  cast_time    reduces cast time of matching ability sources  seconds
  mana_cost    reduces mana cost of matching sources          fraction
  regen        % of mana regen that continues while casting   fraction
  sustain      direct downtime multiplier contribution        fraction (manual EV)
  surv         effective-health increase                      fraction
  pet_surv     pet effective-health increase                  fraction
  cooldown     cooldown reduction of an ability               seconds (converted if the source knows its cooldown)
  utility      direct score bonus for a profile               fraction of score (manual)
  heal         healing output multiplier                      fraction (healer profiles only)
  threat       ignored by DPS/leveling profiles               fraction

Scope tags (which sources it applies to): "all", "type:melee", "type:ranged", "type:spell", "pet",
"school:<fire|frost|arcane|nature|shadow|holy|physical>", "ability:<Name>", "yellow", "white", "dot", "heal".
An effect applies to a source if ANY of its tags matches one of the source's tags ("all" matches every
non-pet source).

Parsed effects come from regexes over the per-rank tooltip text (`<class>.parsed.json`, generated; never
hand-edit). Manual effects live in `<class>.manual.json` (hand-written, with a note explaining the number) and
override parsed ones talent by talent.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent  # _reference/data
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
SCHOOLS = ["fire", "frost", "arcane", "nature", "shadow", "holy", "physical"]

# ------------------------------------------------------------------ tree loading (both games)

def load_tree(game: str, cls: str):
    """Return {tree_name: {talent_name: {"row","max","requires","ranks","status"}}} for either dataset."""
    if game == "classic-era":
        raw = json.load(open(DATA / "classic-era-talents.json", encoding="utf-8"))["classes"][cls]
        out = {}
        for tr in raw["trees"]:
            id2name = {t["id"]: t["name"] for t in tr["talents"]}
            out[tr["name"]] = {t["name"]: {"row": t["row"], "max": t["maxRank"],
                                           "requires": [(id2name[q["talent"]], q["rank"]) for q in t.get("requires", [])],
                                           "ranks": t.get("ranks", []), "status": "classic"} for t in tr["talents"]}
        return out
    raw = json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    out = {}
    for tr in raw["trees"]:
        id2name = {t["id"]: t["name"] for t in tr["talents"]}
        d = {}
        for t in tr["talents"]:
            req = [(id2name.get(t["prereq"]["id"], t["prereq"]["id"]), t["prereq"].get("rank", 1))] if t.get("prereq") else []
            d[t["name"]] = {"row": t["row"], "max": t["maxRank"], "requires": req,
                            "ranks": t.get("ranks", []), "status": t.get("status", "?")}
        out[tr["name"]] = d
    return out


# ------------------------------------------------------------------ scope parsing

def _abilities_from(subj: str):
    """'your Lightning Bolt, Chain Lightning, and Earth Shock spells' -> ['Lightning Bolt', 'Chain Lightning', 'Earth Shock']"""
    s = subj.strip()
    s = re.sub(r"^(your|all your|all of your|all|the)\s+", "", s, flags=re.I)
    s = re.sub(r"\s+(spells?|abilit(?:y|ies)|attacks?)\s*$", "", s, flags=re.I)
    s = re.sub(r"\s+(spell|ability)\b", "", s, flags=re.I)
    parts = re.split(r",\s*(?:and\s+)?|\s+and\s+|\s+or\s+", s)
    names = []
    for p in parts:
        p = p.strip().strip(".")
        if not p:
            continue
        # keep only capitalised ability names (Lightning Bolt, Holy Light, Shadow Word: Pain, Mind Flay)
        if re.match(r"^[A-Z][\w':-]*(?:\s+(?:of|the|and)?\s*[A-Z][\w':-]*)*$", p) and p.lower() not in SCHOOLS:
            names.append(p)
    return names


def scope_from_subject(subj: str):
    names = _abilities_from(subj)
    # remove ability names before looking for schools/types so "Frost Nova" does not tag school:frost
    rest = subj
    for n in names:
        rest = rest.replace(n, " ")
    s = rest.lower()
    tags = []
    if re.search(r"\ball (?:damage|attacks and spells|spells and attacks|your attacks|attacks|spells and abilities)\b", s) or s.strip() in ("all", "you deal"):
        tags.append("all")
    if "pet" in s or "hawk" in s:
        tags.append("pet")
    if re.search(r"\bmelee\b", s):
        tags.append("type:melee")
    if re.search(r"\branged\b", s):
        tags.append("type:ranged")
    if not names and re.search(r"\bspells?\b", s) and not any(sc in s for sc in SCHOOLS):
        tags.append("type:spell")
    for sc in SCHOOLS:
        if re.search(rf"\b{sc}\b", s):
            tags.append(f"school:{sc}")
    if not names and re.search(r"\b(your )?abilities\b", s) and not re.search(r"\b(melee|ranged)\b", s):
        tags.append("yellow")
    if "two-handed" in s:
        tags = [t for t in tags if t != "type:melee"] + ["weapon:2h"]
    if "one-handed" in s:
        tags = [t for t in tags if t != "type:melee"] + ["weapon:1h"]
    if "wand" in s:
        tags.append("ability:Wand")
    if re.search(r"\bheal", s):
        tags.append("heal")
    if re.search(r"\b(periodic|bleed|dot)\b", s):
        tags.append("dot")
    for name in names:
        tags.append(f"ability:{name}")
    if "shock spells" in s or "shocks" in s:
        tags += ["ability:Earth Shock", "ability:Flame Shock", "ability:Frost Shock"]
    if not tags:
        tags.append(f"unknown:{subj.strip()[:40]}")
    return tags


# ------------------------------------------------------------------ patterns

NUM = r"(?P<v>\d+(?:\.\d+)?)"
PATTERNS = [
    # crit chance
    ("crit", re.compile(r"(?:increases|improves) (?:your |the )?(?:chance to (?:get|score) a critical (?:strike|effect)|critical (?:strike|effect) chance) (?:with|of|on|for) (?P<subj>.+?) by " + NUM + "%", re.I)),
    ("crit", re.compile(r"increases (?:your |the )?(?P<subj>[\w' ]+?) critical strike chance by " + NUM + "%", re.I)),
    # damage AND crit in one clause (Improved Moonfire)
    ("dmg+crit", re.compile(r"increases the damage and critical strike chance of (?:your )?(?P<subj>.+?) by " + NUM + "%", re.I)),
    # crit damage bonus
    ("crit_bonus", re.compile(r"increases (?:your |the )?critical strike damage bonus (?:of|on) (?:your |all )?(?P<subj>.+?) by " + NUM + "%", re.I)),
    ("crit_bonus", re.compile(r"increases your (?P<subj>melee|ranged|spell) critical strike damage by " + NUM + "%", re.I)),
    # damage
    ("dmg", re.compile(r"increase[sd]? (?:all |the )?(?P<kind>bleed |periodic )?damage (?:done|dealt)?\s*(?:or life drained )?(?:by|of|with) (?:your )?(?P<subj>.+?) by " + NUM + "%", re.I)),
    ("dmg", re.compile(r"increases (?:all |the )?damage you deal(?: with (?P<subj>.+?))? by " + NUM + "%", re.I)),
    ("dmg", re.compile(r"(?:all )?damage you deal(?: to [^.,]+?)? is increased by " + NUM + "%", re.I)),
    ("dmg", re.compile(r"increases all damage dealt by " + NUM + "%", re.I)),
    ("dmg", re.compile(r"increases your (?P<subj>fire|frost|shadow|nature|arcane|holy|physical)(?: and (?P<subj2>fire|frost|shadow|nature|arcane|holy|physical))? damage(?: done| dealt)? by " + NUM + "%", re.I)),
    ("dmg", re.compile(r"increases your damage with (?P<subj>wands) by " + NUM + "%", re.I)),
    # healing
    ("heal", re.compile(r"increases the (?:amount healed by|effect of|effectiveness of|amount of healing done by) (?:all )?(?:your )?(?P<subj>.+?) by " + NUM + "%", re.I)),
    ("heal", re.compile(r"increases your spell healing by up to " + NUM + "% of your total spirit", re.I)),
    # hit
    ("hit", re.compile(r"(?:increases|improves) (?:your |the )?chance to hit with (?P<subj>.+?) by " + NUM + "%", re.I)),
    ("hit", re.compile(r"increases the chance for (?P<subj>.+?) to hit by " + NUM + "%", re.I)),
    ("hit", re.compile(r"increases (?:your )?hit chance by " + NUM + "%", re.I)),
    ("hit", re.compile(r"(?:increases|improves) (?:your |the )?chance to hit by " + NUM + "%", re.I)),  # beta client wording: no subject -> all
    ("hit", re.compile(r"reduces the chance (?:that )?(?:the opponent|your target) can resist your (?P<subj>.+?) by " + NUM + "%", re.I)),
    # cast time / cooldown / cost / regen
    ("cast_time", re.compile(r"reduces the cast(?:ing)? time of (?:your )?(?P<subj>.+?) by " + NUM + " sec", re.I)),
    ("cooldown", re.compile(r"(?:reduces|decreases) the cooldown (?:of|on) (?:your )?(?P<subj>.+?) by " + NUM + " (?P<unit>sec|min)", re.I)),
    ("mana_cost", re.compile(r"reduces the mana cost of (?:your |all )?(?P<subj>.+?) by " + NUM + "%", re.I)),
    ("resource_cost", re.compile(r"reduces the (?:rage|energy|focus)?\s*cost of (?:your |all )?(?P<subj>.+?) by " + NUM + r"\b(?!\s*%)(?:\s*(?:rage|energy|focus)(?: points?)?)?", re.I)),
    ("regen", re.compile(r"allows " + NUM + "% of your mana regeneration to continue while casting", re.I)),
    # stats / survivability
    ("stat", re.compile(r"increases your (?:total )?(?P<subj>strength|agility|intellect|stamina|spirit) by " + NUM + "%", re.I)),
    ("stat", re.compile(r"increases your (?P<subj>intellect) by " + NUM + r"%\. in addition, while in bear form or dire bear form your stamina is increased by (?P<v2>[\d.]+)% and while in cat form your strength is increased by (?P<v3>[\d.]+)%", re.I)),
    ("surv", re.compile(r"increases your (?P<subj>dodge|parry|block) chance by " + NUM + "%", re.I)),
    ("surv", re.compile(r"increases your chance to (?P<subj>dodge|parry|block)(?: attacks)? by " + NUM + "%", re.I)),
    ("surv", re.compile(r"increases your armor(?: value)?(?: from items)? by " + NUM + "%", re.I)),
    ("surv", re.compile(r"reduces all damage taken by " + NUM + "%", re.I)),
    ("surv", re.compile(r"increases your (?:total )?health by " + NUM + "%", re.I)),
    ("pet_surv", re.compile(r"increases the health(?: and armor)? of your pets? by " + NUM + "%", re.I)),
    # misc
    ("threat", re.compile(r"reduces (?:all )?(?:the )?threat (?:generated by|caused by|you generate)(?: your)? ?(?P<subj>[^.,]*?) by " + NUM + "%", re.I)),
    ("threat_up", re.compile(r"increases (?:all |the )?threat (?:generated|caused)?(?: by| in)?(?: your)? ?(?P<subj>[^.,]*?) by(?: an additional)? " + NUM + "%", re.I)),
    ("surv", re.compile(r"increases your defense skill by " + NUM + r"\b", re.I)),
    ("range", re.compile(r"increases the range of (?:your )?(?P<subj>.+?) by " + NUM + "(?: yards| yds?|%)", re.I)),
    ("pushback", re.compile(r"gives (?:you|your (?P<subj>.+?)) a " + NUM + "% chance to (?:avoid|resist|not lose) (?:interruption|casting time)", re.I)),
]

SURV_WEIGHTS = {"dodge": 1.2, "parry": 1.2, "block": 0.5, "armor": 0.35, "damage": 1.0, "health": 1.0}


def parse_rank(text: str):
    """Return a list of effects (channel, scope, value) found in one rank's tooltip."""
    if not text:
        return []
    t = " ".join(text.split())
    found = []
    for channel, rx in PATTERNS:
        for m in rx.finditer(t):
            g = m.groupdict()
            v = float(g["v"])
            subj = g.get("subj") or ""
            if channel == "dmg+crit":
                scope = scope_from_subject(subj)
                found.append(("dmg", scope, v / 100)); found.append(("crit", scope, v / 100))
            elif channel == "dmg":
                if g.get("subj2"):
                    subj = f"{subj} and {g['subj2']}"
                scope = scope_from_subject(subj) if subj else ["all"]
                if g.get("kind"):
                    scope = [s for s in scope if s != "all"] + ["dot"]
                found.append(("dmg", scope, v / 100))
            elif channel in ("crit", "crit_bonus", "hit", "heal", "mana_cost", "threat", "threat_up"):
                found.append((channel, scope_from_subject(subj) if subj else ["all"], v / 100))
            elif channel == "cast_time":
                found.append(("cast_time", scope_from_subject(subj), v))
            elif channel == "cooldown":
                secs = v * 60 if g.get("unit") == "min" else v
                found.append(("cooldown", scope_from_subject(subj), secs))
            elif channel == "resource_cost":
                found.append(("resource_cost", scope_from_subject(subj), v))
            elif channel == "regen":
                found.append(("regen", ["all"], v / 100))
            elif channel == "stat":
                found.append(("stat", [f"stat:{subj.lower()}"], v / 100))
                if g.get("v2"):
                    found.append(("stat", ["stat:stamina", "form:bear"], float(g["v2"]) / 100))
                    found.append(("stat", ["stat:strength", "form:cat"], float(g["v3"]) / 100))
            elif channel == "surv":
                low = m.group(0).lower()
                if "defense skill" in low:
                    found.append(("surv", ["surv:defense"], v * 0.0016 * 1.2))
                    continue
                kind = (subj or ("armor" if "armor" in low else "damage" if "damage taken" in low else "health")).lower()
                found.append(("surv", [f"surv:{kind}"], v / 100 * SURV_WEIGHTS.get(kind, 1.0)))
            elif channel == "pet_surv":
                found.append(("pet_surv", ["pet"], v / 100))
            elif channel == "range":
                found.append(("range", scope_from_subject(subj), v))
            elif channel == "pushback":
                found.append(("pushback", ["all"], v / 100))
    return found


def parse_talent(ranks):
    """Parse every rank; merge into effects with cumulative value lists. Ranks that fail to parse repeat the last value."""
    per_rank = [parse_rank(r) for r in ranks]
    keys = []
    for eff in per_rank:
        for ch, scope, _ in eff:
            k = (ch, tuple(scope))
            if k not in keys:
                keys.append(k)
    effects = []
    for ch, scope in keys:
        values, last = [], 0.0
        for eff in per_rank:
            match = [v for c2, s2, v in eff if (c2, tuple(s2)) == (ch, scope)]
            last = match[0] if match else last
            values.append(round(last, 5))
        effects.append({"channel": ch, "scope": list(scope), "values": values, "source": "parsed"})
    return effects


# ------------------------------------------------------------------ files

def parsed_path(game, cls):
    return HERE / "effects" / game / f"{cls}.parsed.json"


def manual_path(game, cls):
    return HERE / "effects" / game / f"{cls}.manual.json"


def build_parsed(game: str, cls: str):
    tree = load_tree(game, cls)
    out = {}
    for tname, talents in tree.items():
        for name, t in talents.items():
            effects = parse_talent(t["ranks"])
            out[name] = {"tree": tname, "max": t["max"], "text": (t["ranks"][0] or "").replace("\n", " ")[:220],
                         "effects": effects}
    p = parsed_path(game, cls)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    return out


def load_effects(game: str, cls: str):
    """Merged effects: manual overrides parsed, talent by talent. Returns {talent: {"effects": [...], "source": ...}}."""
    parsed = json.load(open(parsed_path(game, cls), encoding="utf-8")) if parsed_path(game, cls).exists() else build_parsed(game, cls)
    manual = json.load(open(manual_path(game, cls), encoding="utf-8")) if manual_path(game, cls).exists() else {}
    merged = {}
    for name, entry in parsed.items():
        if name in manual and manual[name].get("effects") is not None:
            m = manual[name]
            effs = []
            for e in m["effects"]:
                e = dict(e); e.setdefault("source", "manual")
                if "per_rank" in e and "values" not in e:
                    e["values"] = [round(e["per_rank"] * (i + 1), 5) for i in range(entry["max"])]
                effs.append(e)
            if effs and all((e.get("modes") or []) == ["pvp"] for e in effs):
                # an entry that only adds PvP values (the 2026-09-27 PvP audit) keeps the tooltip numbers everywhere else: without
                # this its parsed effects vanished in every mode (Classic Reverberation, Deflection, Arcane Focus)
                effs = [dict(e) for e in entry["effects"]] + effs
            merged[name] = {"effects": effs, "source": "manual", "note": m.get("note", ""), "tree": entry["tree"], "max": entry["max"], "parsed": entry["effects"]}
        else:
            merged[name] = {"effects": entry["effects"], "source": "parsed" if entry["effects"] else "missing",
                            "note": "", "tree": entry["tree"], "max": entry["max"], "parsed": entry["effects"]}
    # what kind of value each talent's soft effects are, and whether it needs a pet out (scorer/kinds.json)
    for name, info in load_kinds(game, cls).items():
        if name in merged:
            merged[name]["kinds"] = {ch: k for ch, k in info.items() if ch in ("utility", "surv", "sustain")}
            merged[name]["needs_pet"] = info.get("needs_pet") or False   # True or the pet's name
    return merged


def load_kinds(game: str, cls: str):
    """{talent: {"utility": kind, "surv": kind, "sustain": kind, "needs_pet": bool}} for one class and game. An entry may be
    limited to one game with "games"."""
    path = HERE / "kinds.json"
    if not path.exists():
        return {}
    data = json.load(open(path, encoding="utf-8"))
    out = {}
    for name, info in data.get("talents", {}).get(cls, {}).items():
        if info.get("games") and game not in info["games"]:
            continue
        out[name] = info
    return out


if __name__ == "__main__":
    import sys
    games = ["forever", "classic-era"]
    classes = [c for c in CLASSES if not sys.argv[1:] or c in sys.argv[1:]]
    for game in games:
        for cls in classes:
            out = build_parsed(game, cls)
            n = len(out); ok = sum(1 for v in out.values() if v["effects"])
            print(f"{game:12s} {cls:8s} parsed {ok}/{n} talents")
