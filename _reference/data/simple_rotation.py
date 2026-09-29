"""Plain-language rotations for the player pages (2026-09-29, user request: "simple to understand as just the class, no racials or
item usage, noob friendly").

The simulator's rotation (its APL, translated by render_sim_presets.py into lines such as "If time left on Corruption <= cast time of
Corruption: cast Corruption") is exact but hard to read. `simplify(cls, lines)` turns the lines a build actually casts into a short
list a new player can follow:

- only the class's own spells and talents stay (the beta spellbook and the talent trees): potions, runes, mana gems, engineering
  explosives, trinkets, racials and "use every other cooldown" go;
- conditions become plain words: keep a damage-over-time spell or a buff up, use a proc when it lights up, below 20% health, when
  low on mana, at 5 combo points, with spare rage; fight-timer, swing-timer, target-count and mana-budget conditions are dropped;
- each spell appears once (its first, highest-priority line) and the list stops at LIMIT lines.

The exact list stays on the research pages (research/raid/rotation.md). Nothing here changes a simulation.
"""
import functools
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
LIMIT = 8


@functools.lru_cache(maxsize=None)
def class_spells(cls):
    """Every spell of the class's beta spellbook and every talent name: what a player of the class presses."""
    names = set()
    book = json.load(open(HERE / "forever-spells" / f"{cls}.json", encoding="utf-8"))
    for tab in book["tabs"]:
        names.update(sp["name"] for sp in tab["spells"])
    for tr in json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]:
        names.update(t["name"] for t in tr["talents"])
    return names


# buffs a player keeps on themselves (the rest of the "keep up" spells are debuffs on the target)
SELF = ("Seal of ", " Aura", " Shout", " Form", "Shadowform", "Slice and Dice", "Inner Fire", "Demon Armor", "Demon Skin", "Mage Armor",
        "Ice Armor", "Frost Armor", "Molten Armor", "Lightning Shield", "Water Shield", "Aspect of", "Blessing of", "Righteous Fury",
        "Bone Shield", "Trueshot", "Moonkin", "Omen", "Nature's Grasp", "Thorns", "Mark of the Wild", "Arcane Intellect", "Power Word: Fortitude")


@functools.lru_cache(maxsize=None)
def other_class_spells(cls):
    """Spells of every other class (a condition on one of them, a rogue's Expose Armor for a warrior, is fine tuning)."""
    others = set()
    for f in (HERE / "forever-spells").glob("*.json"):
        if f.stem != cls:
            others |= class_spells(f.stem)
    return others - class_spells(cls)


def is_self(spell):
    return any(k in spell for k in SELF)


def _unwrap(c):
    c = c.strip()
    while c.startswith("(") and c.endswith(")") and c.count("(") == c.count(")"):
        c = c[1:-1].strip()
    return c


def _clause(c, spell, ok):
    """One condition clause -> (kind, plain text) or None to drop it."""
    c = _unwrap(c)
    if " or " in c:   # an either-or group: keep the first part a player can see (a proc, rage, the execute phase), drop the rest
        for part in c.split(" or "):
            got = _clause(part, spell, ok)
            if got and got[0] == "when":
                return got
        return None
    if re.search(r"time left in the fight|time to the next auto attack|time until .* is ready|number of targets|mana ≥ \(|mana \+|energy|mana % ≥|can be cast|^false$|^true$", c):
        return None
    m = re.match(r"(?:time left on (.+?) (?:≤|<) .+|not (.+?) is on the target|(.+?) should be refreshed)$", c)
    if m:
        x = next(g for g in m.groups() if g)
        return ("keep", x) if x == spell else None
    if re.match(r"time left on the totem ≤ .+", c):
        return ("keep", spell)
    m = re.match(r"(not )?(.+?) is up$", c)
    if m:
        if m.group(2) == spell:
            return ("keep", spell) if m.group(1) else None
        if m.group(2) not in ok and m.group(2) in other_class_spells(CUR[0]):   # another class's buff (a rogue's Expose Armor for a warrior)
            return None
        return ("when", f"{m.group(2)} is {'not ' if m.group(1) else ''}active")
    m = re.match(r"stacks of (.+?) (≥|=|<) ([\d.]+)$", c)
    if m:
        n = round(float(m.group(3)))
        if m.group(1) == spell and m.group(2) == "<":
            return ("stack", f"{n}")
        if m.group(2) != "<":
            return ("when", f"{m.group(1)} has {n} stacks")
        return ("when", f"the target has fewer than {n} stacks of {m.group(1)}")   # a debuff the spell builds (Scorch's Fire Vulnerability)
    m = re.match(r"execute phase \(E(\d+)\)$", c)
    if m:
        return ("when", f"the target is below {m.group(1)}% health")
    m = re.match(r"mana % (?:≤|<) (\d+)%$", c)
    if m:
        return ("when", f"your mana is below {m.group(1)}%")
    m = re.match(r"health % (?:≤|<) (\d+)%$", c)
    if m:
        return ("when", f"your health is below {m.group(1)}%")
    m = re.match(r"rage (?:≥|>) (\d+)$", c)
    if m:
        return ("when", f"you have {m.group(1)}+ rage to spare")
    m = re.match(r"combo points ≥ ([\d.]+)$", c)
    if m:
        return ("when", f"you have {round(float(m.group(1)))} combo points")
    return None   # anything else is fine tuning a new player can skip


def _cond_parts(cond):
    """Split a condition on its top-level ' and '."""
    parts, depth, cur = [], 0, ""
    for tok in re.split(r"(\(|\)| and )", cond):
        if tok == "(":
            depth += 1
        elif tok == ")":
            depth -= 1
        if tok == " and " and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += tok
    parts.append(cur)
    return [p for p in parts if p.strip()]


LINE = re.compile(r"^(?:[Ii]f (.+): )?((?:cast|channel|keep|use|strict sequence|sequence)\b.*)$", re.I)


# abilities that only light up after something happens: said so when the rotation line has no condition of its own
REACTIVE = {"Mongoose Bite": "when it lights up (after the target dodges)", "Overpower": "when it lights up (after the target dodges)",
            "Riposte": "after you parry", "Counterattack": "after you parry", "Revenge": "after you block, dodge or parry",
            "Victory Rush": "after a kill", "Hammer of Wrath": "when the target is below 20% health", "Shadow Word: Death": "",
            "Execute": "when the target is below 20% health"}
CUR = [None]   # the class being parsed (for _clause's other-class test)


def _parse(cls, t):
    """A translated line -> (spells, plain line, is_swing_timed) or None when nothing of it stays."""
    ok = class_spells(cls)
    CUR[0] = cls
    m = LINE.match(t.strip())
    if not m:
        return None
    cond, act = m.group(1), m.group(2)
    swing = bool(cond and "time to the next auto attack" in cond)
    if "every other cooldown" in act:
        return None
    if act.lower().startswith(("strict sequence", "sequence")):
        sp = [x.strip() for x in re.findall(r"cast ([^;]+)", act) if x.strip() in ok]
        return (sp, f"**{sp[0]}**, then straight away **{sp[1]}**", swing) if len(sp) >= 2 else None
    km = re.match(r"^[Kk]eep (.+?) on up to", act)
    if km:
        sp = km.group(1).strip()
        return ([sp], f"**{sp}**: keep it on the target", swing) if sp in ok else None
    cm = re.match(r"^(?:[Cc]ast|[Cc]hannel) (.+?)(?: \(interrupt.*)?$", act)
    if not cm:
        return None
    sp = cm.group(1).strip()
    if sp not in ok:
        return None
    if swing and sp.startswith("Seal of"):   # seal twisting (a second seal timed to the swing): an advanced trick
        return None
    if sp.endswith("Totem") or is_self(sp):   # totems and self-buffs go in the "keep up all fight" line
        return ([sp], f"KEEP:{sp}", swing)
    clauses = [c for c in (_clause(x, sp, ok) for x in (_cond_parts(cond) if cond else [])) if c]
    if cond and re.search(r"time left in the fight (?:≤|<) ([\d.]+)", cond) and " or " not in cond and not clauses:
        left = float(re.search(r"time left in the fight (?:≤|<) ([\d.]+)", cond).group(1))
        if left < 10:   # a last-seconds filler (Searing Pain, Shadowburn as the boss dies): fine tuning
            return None
        return ([sp], f"**{sp}**: in the last {round(left / 5) * 5:.0f} seconds of the fight", swing)
    if cond and re.search(r"time left in the fight ≥ \d{2,}", cond) and " or " in cond and not clauses:
        return ([sp], f"**{sp}**: a big cooldown, use it at the start of the fight and again whenever it is ready", swing)
    kinds = dict((k, v) for k, v in clauses if k != "when")
    whens = [v for k, v in clauses if k == "when"]
    if "stack" in kinds:
        txt = f"**{sp}**: stack it to {int(kinds['stack']) + 1 if int(kinds['stack']) < 5 else 5} on the target"
    elif "keep" in kinds:
        txt = f"**{sp}**: " + ("keep it down" if sp.endswith("Totem") else "keep it up" if is_self(sp) else "keep it on the target")
    else:
        txt = f"**{sp}**"
    if not whens and REACTIVE.get(sp):
        whens = [REACTIVE[sp].replace("when ", "", 1)] if REACTIVE[sp].startswith("when ") else []
        if not whens:
            txt += f" {REACTIVE[sp]}"
    if whens:
        txt += (" when " if txt == f"**{sp}**" else ", when ") + " and ".join(whens)
    return ([sp], txt, swing)


def simplify(cls, texts):
    """(keep up all fight, the priority list) for a build's used rotation lines (the translated APL texts, in priority order)."""
    parsed = [x for x in (_parse(cls, t) for t in texts) if x]
    plain = {s for sp, _, sw in parsed if not sw for s in sp}   # swing-timed lines (clipped shots) only when nothing else casts the spell
    keep, out, seen = [], [], set()
    for sp, txt, sw in parsed:
        if (sw and all(s in plain for s in sp)) or set(sp) & seen:
            continue
        seen.update(sp)
        if txt.startswith("KEEP:"):
            keep.append(txt[5:])
        elif len(out) < LIMIT:
            out.append(txt)
    return keep, out


def pre_pull(cls, pre):
    """Spells of the class cast before the pull (the APL's prepull actions)."""
    ok = class_spells(cls)
    names = [m.group(1).strip() for _, a in pre for m in [re.match(r"^(?:cast|channel) (.+)$", a)] if m]
    return [n for n in names if n in ok]
