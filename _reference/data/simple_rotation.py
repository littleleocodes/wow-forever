"""Plain-language rotations for the player pages (2026-09-29, user request: "simple to understand as just the class, no racials or
item usage, noob friendly").

The simulator's rotation (its APL, translated by render_sim_presets.py into lines such as "If time left on Corruption <= cast time of
Corruption: cast Corruption") is exact but hard to read. `simplify(cls, lines)` turns the lines a build actually casts into a short
list a new player can follow:

- only the class's own spells and talents stay (the beta spellbook and the talent trees): potions, runes, mana gems, engineering
  explosives, trinkets, racials and "use every other cooldown" go;
- conditions become plain words: keep a damage-over-time spell or a buff up, use a proc when it lights up, below 20% health, with
  enough mana or rage, at N combo points or stacks (rounded the way the condition works: "4.218 or more stacks" is 5), while another
  spell is on cooldown, until the last seconds of the fight; swing-timer and cooldown-timing conditions are dropped;
- a spell appears again further down only when its earlier lines were conditional (Pyroblast at 3 stacks below Pyroblast with 2 stacks
  about to run out; Devouring Plague alone below Inner Focus + Devouring Plague) and the later line is not a stricter copy;
- lines cast only in the last seconds of a fight (Searing Pain, Shadowburn, the Frost mage's Fire Blast) go to `late`, seal twisting
  and other advanced tricks to `extras`; the list stops at LIMIT lines.

2026-10-09 (the rotation-guide review of every class): decimal thresholds, mana, rage, energy, combo-point ceilings, fight-time windows
(Death Wish "in the last 45 seconds", not at the pull), Maelstrom Weapon's 4.218 stacks (5), Mongoose Bite after *you* dodge, Cold
Blood before the finisher (it spends no combo points), seal twisting, the filler only for a spell without a cooldown.

The exact list stays on the research pages (research/raid/rotation.md). Nothing here changes a simulation.
"""
import functools
import json
import math
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
LIMIT = 8
FIGHT = 180   # raidsim/run.py FIGHT: every page number is a 3-minute fight (a window that opens later than this never happens)


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


@functools.lru_cache(maxsize=None)
def talent_names(cls):
    return {t["name"] for tr in json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"] for t in tr["talents"]}


# buffs a player keeps on themselves (the rest of the "keep up" spells are debuffs on the target)
SELF = ("Seal of ", " Aura", " Shout", " Form", " Stance", "Shadowform", "Slice and Dice", "Inner Fire", "Demon Armor", "Demon Skin", "Mage Armor",
        "Ice Armor", "Frost Armor", "Molten Armor", "Lightning Shield", "Water Shield", "Aspect of", "Blessing of", "Righteous Fury",
        "Bone Shield", "Trueshot", "Moonkin", "Omen", "Nature's Grasp", "Thorns", "Mark of the Wild", "Arcane Intellect", "Power Word: Fortitude")
# race-only spells in the priest's spellbook (Classic 1.12's racial priest spells): the pages are race-neutral
RACIAL = {"Desperate Prayer", "Touch of Weakness", "Hex of Weakness", "Elune's Grace", "Starshards", "Feedback", "Shadowguard"}


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


@functools.lru_cache(maxsize=None)
def cooldowns(cls):
    """{spell: True when any rank of it has a cooldown} from the beta spellbook."""
    out = {}
    for tab in json.load(open(HERE / "forever-spells" / f"{cls}.json", encoding="utf-8"))["tabs"]:
        for sp in tab["spells"]:
            out[sp["name"]] = out.get(sp["name"], False) or any((r.get("cooldown") or "").strip() for r in sp.get("ranks", []))
    return out


@functools.lru_cache(maxsize=None)
def cooldown_seconds(cls):
    """{spell: its longest cooldown in seconds} from the beta spellbook ("3 min cooldown" -> 180)."""
    out = {}
    for tab in json.load(open(HERE / "forever-spells" / f"{cls}.json", encoding="utf-8"))["tabs"]:
        for sp in tab["spells"]:
            for r in sp.get("ranks", []):
                m = re.match(r"([\d.]+) (sec|min|hr)", (r.get("cooldown") or "").strip())
                if m:
                    s = float(m.group(1)) * {"sec": 1, "min": 60, "hr": 3600}[m.group(2)]
                    out[sp["name"]] = max(out.get(sp["name"], 0), s)
    return out


def _n(x):
    """A number as the page shows it: 7.5 -> "7.5", 3.0 -> "3"."""
    return f"{float(x):g}"


def _count(op, x):
    """The whole count (stacks, combo points) a comparison needs: "≥ 4.218" is 5 or more, "> 2" is 3 or more, "≤ 3.5" is 3 or fewer."""
    x = float(x)
    if op == "≥":
        return math.ceil(x - 1e-9)
    if op == ">":
        return math.floor(x + 1e-9) + 1
    if op == "≤":
        return math.floor(x + 1e-9)
    if op == "<":
        return math.ceil(x - 1e-9) - 1
    return round(x)


def _unwrap(c):
    c = c.strip()
    while c.startswith("(") and c.endswith(")") and c.count("(") == c.count(")"):
        c = c[1:-1].strip()
    return c


EITHER = "⁘"   # marks an either-or group's text (the word "or" alone cannot: "4 or more combo points")
DROP = re.compile(r"time to the next auto attack|time until .* is ready (?:<|≤|≥|=)|number of targets = 1|number of targets (?:<|≤)|can be cast|"
                  r"the global cooldown|is known|current cost|excess cat energy|^false$|^true$|mana \+|internal cooldown|energy (?:<|≤)")


def _clause(c, spell, ok):
    """One condition clause -> (kind, plain text) or None to drop it. Kinds: keep, stack, when, until."""
    c = _unwrap(c)
    ors = _split_top(c, " or ")
    if len(ors) > 1:   # an either-or group: every part a player can see, joined with "or" (parts the page cannot show are dropped)
        got = [g for g in (_clause(p, spell, ok) for p in ors) if g]
        whens = list(dict.fromkeys(v for k, v in got if k == "when"))
        if len(whens) > 1:
            return ("when", EITHER + " or ".join(w.replace(EITHER, "") for w in whens))   # marked: _parse says "either" beside other conditions
        if whens:
            return ("when", whens[0])
        return next((g for g in got if g[0] in ("keep", "stack")), None)
    if len(_cond_parts(c)) > 1:   # a group inside an either-or part: all of it or nothing
        got = [_clause(p, spell, ok) for p in _cond_parts(c)]
        if got and all(g and g[0] == "when" for g in got):
            return ("when", " and ".join(g[1] for g in got))
        return None
    if DROP.search(c):
        return None
    m = re.match(r"time until (.+?) is ready > 0s?$", c)
    if m:
        return ("when", f"{m.group(1)} is on cooldown")
    m = re.match(r"time left in the fight (≥|>) ([\d.]+)s?$", c)
    if m:
        return ("until", float(m.group(2))) if float(m.group(2)) >= 10 else None
    if c.startswith("time left in the fight"):
        return None
    m = re.match(r"mana ≥ \(time left in the fight × [\d.]+\)$", c)
    if m:
        return ("when", "you have mana to spare for the rest of the fight")
    m = re.match(r"mana % (≥|>) ([\d.]+)%$", c)
    if m:
        return ("when", f"you have at least {_n(m.group(2))}% mana")
    m = re.match(r"mana % (?:≤|<) ([\d.]+)%$", c)
    if m:
        return ("when", f"your mana is below {_n(m.group(1))}%")
    if c.startswith("mana"):
        return None
    m = re.match(r"energy (≥|>) ([\d.]+)$", c)
    if m:
        return ("when", f"you have {_count(m.group(1), m.group(2))}+ energy")
    if c.startswith("energy"):
        return None
    m = re.match(r"number of targets (≥|>) ([\d.]+)$", c)
    if m:
        return ("when", f"there are {_count(m.group(1), m.group(2))} or more targets")
    m = re.match(r"time left on (.+?) (≤|<) ([\d.]+)s?$", c)
    if m:
        if m.group(1) == spell:
            return ("keep", spell)
        return ("when", f"{m.group(1)} has under {_n(m.group(3))} seconds left")
    m = re.match(r"(?:time left on (.+?) (?:≤|<) .+|not (.+?) is on the target|(.+?) should be refreshed)$", c)
    if m:
        x = next(g for g in m.groups() if g)
        return ("keep", x) if x == spell else None
    m = re.match(r"(.+?) is on the target$", c)
    if m and m.group(1) != spell:
        return ("when", f"{m.group(1)} is on the target")
    if re.match(r"time left on the totem ≤ .+", c):
        return ("keep", spell)
    m = re.match(r"(not )?(.+?) is up$", c)
    if m:
        if m.group(2) == spell:
            return ("keep", spell) if m.group(1) else None
        if m.group(2) not in ok and m.group(2) in other_class_spells(CUR[0]):   # another class's buff (a rogue's Expose Armor for a warrior)
            return None
        return ("when", f"{m.group(2)} is {'not ' if m.group(1) else ''}active")
    m = re.match(r"stacks of (.+?) (≥|>|=|<|≤) ([\d.]+)$", c)
    if m:
        name, op, x = m.groups()
        if op in ("<", "≤"):
            n = math.ceil(float(x) - 1e-9) if op == "<" else math.floor(float(x) + 1e-9) + 1   # "fewer than n"
            if name == spell:
                return ("stack", f"{n - 1}")
            return ("when", f"the target has fewer than {n} stacks of {name}")   # a debuff the spell builds (Scorch's Fire Vulnerability)
        n = _count(op, x)
        if op == "=":
            return ("when", f"{name} has {n} stacks")
        return ("when", f"{name} has {n} or more stacks")
    m = re.match(r"execute phase \(E(\d+)\)$", c)
    if m:
        return ("when", f"the target is below {m.group(1)}% health")
    m = re.match(r"health % (?:≤|<) ([\d.]+)%$", c)
    if m:
        return ("when", f"your health is below {_n(m.group(1))}%")
    m = re.match(r"rage (≥|>) ([\d.]+)$", c)
    if m:
        return ("when", f"you have {_count(m.group(1), m.group(2))}+ rage")
    m = re.match(r"rage (<|≤) ([\d.]+)$", c)
    if m:
        n = math.ceil(float(m.group(2)) - 1e-9) if m.group(1) == "<" else math.floor(float(m.group(2)) + 1e-9) + 1
        return ("when", f"you have less than {n} rage")
    m = re.match(r"combo points (≥|>|=|≤|<) ([\d.]+)$", c)
    if m:
        n = _count(m.group(1), m.group(2))
        if m.group(1) in ("≥", ">"):
            return ("when", f"you have {n} combo points" if n >= 5 else f"you have {n} or more combo points")
        if m.group(1) == "=":
            return ("when", f"you have exactly {n} combo points")
        return ("when", f"you have {n} or fewer combo points")
    return None   # anything else is fine tuning a new player can skip


_JOINED = []


def _joined_names():
    """Every spell and talent name of any class that contains ' and ' or ' or ' (Slice and Dice): split conditions keep them whole."""
    if not _JOINED:
        names = set()
        for f in (HERE / "forever-spells").glob("*.json"):
            for tab in json.load(open(f, encoding="utf-8"))["tabs"]:
                names.update(sp["name"] for sp in tab["spells"])
        for f in (HERE / "forever-talents").glob("*.json"):
            for tr in json.load(open(f, encoding="utf-8")).get("trees", []):
                names.update(t["name"] for t in tr.get("talents", []))
        _JOINED.extend(sorted((n for n in names if " and " in n or " or " in n), key=len, reverse=True) or [""])
    return [n for n in _JOINED if n]


def _protect(c):
    for n in _joined_names():
        c = c.replace(n, n.replace(" and ", " ∧ ").replace(" or ", " ∨ "))
    return c


def _restore(c):
    return c.replace(" ∧ ", " and ").replace(" ∨ ", " or ")


def _split_top(cond, sep):
    """Split a condition on its top-level `sep` (" and " / " or "); names that contain it (Slice and Dice) stay whole."""
    parts, depth, cur = [], 0, ""
    for tok in re.split(r"(\(|\)|" + re.escape(sep) + ")", _protect(cond)):
        if tok == "(":
            depth += 1
        elif tok == ")":
            depth -= 1
        if tok == sep and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += tok
    parts.append(cur)
    return [_restore(p) for p in parts if p.strip()]


def _cond_parts(cond):
    """Split a condition on its top-level ' and ' (names that contain ' and ', such as Slice and Dice, stay whole)."""
    return _split_top(cond, " and ")


LINE = re.compile(r"^(?:[Ii]f (.+): )?((?:cast|channel|keep|use|strict sequence|sequence)\b.*)$", re.I)


# abilities that only light up after something happens: said so when the rotation line has no condition of its own
REACTIVE = {"Mongoose Bite": "after you dodge",   # Forever 70291: "Can only be performed after you dodge" (not the target's dodge)
            "Overpower": "when it lights up (after the target dodges)",
            "Riposte": "after you parry", "Counterattack": "after you parry", "Revenge": "after you block, dodge or parry",
            "Victory Rush": "after a kill", "Hammer of Wrath": "when the target is below 20% health", "Shadow Word: Death": "",
            "Execute": "when the target is below 20% health"}
# one-shot boosts whose condition times them for the ability after them (Cold Blood's "4 or more combo points" means: right before the
# finisher), said in those words alone so the line does not read as if the boost spent combo points (2026-10-09, user report)
PREP = {"Cold Blood": "right before your finisher", "Inner Focus": "right before your next big spell",
        "Presence of Mind": "right before a long cast", "Nature's Swiftness": "right before a long cast",
        "Elemental Mastery": "right before your next big spell", "Divine Favor": "right before your next big heal"}
KEEP_UP = {"Summon Hawk", "Ghostly Strike"}   # kept up on you (or as your pet), not on the target
MANA_TOOLS = {"Evocation", "Life Tap", "Innervate", "Mana Tide Totem", "Dark Pact", "Shadowfiend", "Aspect of the Viper", "Dark Sacrifice"}
CUR = [None]   # the class being parsed (for _clause's other-class test)
FLOOR = [None]   # (spell, seconds) when the line just parsed is an always-ready spell cast while more than that many seconds are left


def _window(cond):
    """A cooldown cast only at the pull or near the end: "(time left in the fight ≤ A or time left in the fight ≥ B)" -> plain words."""
    m = re.fullmatch(r"\(?time left in the fight ≤ ([\d.]+)s? or time left in the fight ≥ ([\d.]+)s?\)?", _unwrap(cond or ""))
    if not m:
        return None
    a, b = float(m.group(1)), float(m.group(2))
    if b >= FIGHT:   # the opening window never happens in a 3-minute fight: it is saved for the end
        return f"save it for the last {_n(a)} seconds of the fight"
    return f"at the pull, and again in the last {_n(a)} seconds of the fight"


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
        sp = [x.strip() for x in re.findall(r"cast ([^;]+)", act) if x.strip() in ok and x.strip() not in RACIAL]
        return (sp, f"**{sp[0]}**, then straight away **{sp[1]}**", swing) if len(sp) >= 2 else None
    km = re.match(r"^[Kk]eep (.+?) on up to", act)
    if km:
        sp = km.group(1).strip()
        return ([sp], f"**{sp}**: keep it on the target", swing) if sp in ok else None
    cm = re.match(r"^(?:[Cc]ast|[Cc]hannel) (.+?)(?: \(interrupt.*)?$", act)
    if not cm:
        return None
    sp = cm.group(1).strip()
    if sp not in ok or sp in RACIAL:
        return None
    if sp in MANA_TOOLS and sp != "Life Tap":   # Evocation, Innervate, Dark Sacrifice...: the Advanced list says when (advanced())
        return None
    if swing and sp.startswith("Seal of"):   # seal twisting (a second seal timed to the swing): the Advanced list explains it
        return None
    if sp.startswith("Seal of") and cond:
        other = re.search(r"(Seal of [A-Z][\w' ]+?) is up", cond)
        if other and other.group(1) != sp:   # a seal cast while another is up: seal twisting, not a second seal to keep up
            whens = [v for k, v in (_clause(x, sp, ok) or ("", "") for x in _cond_parts(cond)) if k == "when" and "Seal of" not in v]
            return ([sp], f"TWIST:{sp}|{other.group(1)}|{' and '.join(whens)}", swing)
    if sp.endswith("Totem") or is_self(sp):   # totems and self-buffs go in the "keep up all fight" line
        how = []
        cps = [(op, float(x)) for op, x in re.findall(r"combo points (≥|>) ([\d.]+)", cond or "")]
        if cps:   # a finisher kept up: how few combo points it may take, and when it is refreshed early (Slice and Dice)
            lo = min(_count(op, x) for op, x in cps)
            hi = max(_count(op, x) for op, x in cps)
            how.append(f"put it back up as soon as it drops, even with {lo} combo point{'s' if lo != 1 else ''}")
            rf = re.search(r"time left on " + re.escape(sp) + r" < ([\d.]+)", cond or "")
            if hi > lo and rf:
                how.append(f"refresh it early at {hi} combo points when it has under {_n(rf.group(1))} seconds left")
        return ([sp], f"KEEP:{sp}" + (f"|{'; '.join(how)}" if how else ""), swing)
    whole = _unwrap(cond) if cond else ""
    fl = re.fullmatch(r"time left in the fight (?:≥|>) ([\d.]+)s?", whole)
    if fl and float(fl.group(1)) <= 10 and cooldowns(cls).get(sp) is False:
        FLOOR[0] = (sp, float(fl.group(1)))   # an always-ready spell cast until the last seconds: what follows is end-of-fight play
        return ([sp], f"**{sp}**", swing)
    lm = re.fullmatch(r"time left in the fight (?:≤|<) ([\d.]+)s?", whole)
    if lm:
        left = float(lm.group(1))
        if left < 10:   # a last-seconds spell (Searing Pain, Shadowburn as the boss dies): the Advanced list's end-of-fight line
            return ([sp], f"LATE:{left}", swing)
        return ([sp], f"**{sp}**: in the last {_n(left)} seconds of the fight", swing)
    win = _window(cond)
    if win:
        return ([sp], f"**{sp}**: a big cooldown, {win}", swing)
    clauses = [c for c in (_clause(x, sp, ok) for x in (_cond_parts(cond) if cond else [])) if c]
    kinds = dict((k, v) for k, v in clauses if k not in ("when", "until"))
    whens = list(dict.fromkeys(v for k, v in clauses if k == "when"))
    until = max((v for k, v in clauses if k == "until"), default=None)
    if "stack" in kinds:
        txt = f"**{sp}**: stack it to {int(kinds['stack']) + 1 if int(kinds['stack']) < 5 else 5} on the target"
    elif "keep" in kinds:
        txt = f"**{sp}**: " + ("keep it down" if sp.endswith("Totem") else "keep it up" if is_self(sp) or sp in KEEP_UP else "keep it on the target")
    else:
        txt = f"**{sp}**"
    if PREP.get(sp):   # its condition times it for the next ability: say that alone
        return ([sp], f"**{sp}** {PREP[sp]}", swing)
    if not whens and REACTIVE.get(sp):
        whens = [REACTIVE[sp].replace("when ", "", 1)] if REACTIVE[sp].startswith("when ") else []
        if not whens:
            txt += f" {REACTIVE[sp]}"
    if whens:
        if len(whens) > 1:   # an either-or group next to other conditions: "and either A or B" (Eviscerate's Slice and Dice or 79 energy)
            whens = [("either " + w[1:]) if w.startswith(EITHER) else w for w in whens]
        whens = [w.replace(EITHER, "") for w in whens]
        txt += (" when " if txt == f"**{sp}**" else ", when ") + " and ".join(whens).replace(" and you have ", " and ")
    if until:
        txt += f"{',' if txt != f'**{sp}**' else ''} until the last {_n(until)} seconds of the fight"
    return ([sp], txt, swing)


def _cp_key(txt):
    """A line with its combo-point number taken out (stricter copies of a finisher line differ only in it)."""
    m = re.search(r"you have (\d+)(?: or more)? combo points", txt)
    return (re.sub(r"you have \d+(?: or more)? combo points", "you have CP combo points", txt), int(m.group(1)) if m else None)


def simplify(cls, texts, late=None, extras=None):
    """(keep up all fight, the priority list) for a build's used rotation lines (the translated APL texts, in priority order).
    A line after an always-ready spell cast only while some seconds of the fight are left (the Frost raid rotation's Frostbolt while 3+
    seconds are left, then Fire Blast), and a line cast only in the last seconds (Searing Pain), is end-of-fight play, not the filler:
    it goes to `late` as (spell, seconds, the filler). Seal twisting goes to `extras` as plain lines."""
    parsed = []
    for t in texts:
        FLOOR[0] = None
        x = _parse(cls, t)
        if x:
            parsed.append((*x, FLOOR[0]))
    plain = {s for sp, _, sw, _ in parsed if not sw for s in sp}   # swing-timed lines (clipped shots) only when nothing else casts the spell
    keep, out, closed, twists = [], [], None, {}
    shown = {}   # spell -> the texts shown for it
    done = set()   # spells shown with no condition: a later line of theirs adds nothing
    pend = []   # (spell, seconds, filler or None) for `late`
    for sp, txt, sw, floor in parsed:
        if sw and all(s in plain for s in sp):
            continue
        if txt.startswith("LATE:"):
            pend.append((sp[0], float(txt[5:]), None))
            continue
        if txt.startswith("TWIST:"):
            a, b, w = txt[6:].split("|")
            if (a, b) not in twists or len(w) < len(twists[(a, b)]):
                twists[(a, b)] = w
            continue
        if txt.startswith("KEEP:"):
            if txt[5:].split("|")[0] not in {k.split("|")[0] for k in keep}:
                keep.append(txt[5:])
            continue
        if closed:   # end-of-fight play after an always-ready filler
            pend += [(s, closed[1], closed[0]) for s in sp]
            continue
        if set(sp) & done or any(txt in shown.get(s, []) for s in sp):
            continue
        if len(sp) == 1 and shown.get(sp[0]):
            prev = shown[sp[0]]
            if ("keep it" in txt or "stack it" in txt) and any("keep it" in p or "stack it" in p for p in prev):
                continue   # the spell is already kept up
            if " when " not in txt and not all(", then straight away " in p for p in prev):
                continue   # a fallback with no condition of its own (Ret's rank-1 Consecration, a second Judgement): fine tuning
            if " when " in txt and any(txt.split(" when ", 1)[1] in p for p in prev):
                continue
            k, n = _cp_key(txt)
            if n is not None and any(_cp_key(p)[0] == k and (_cp_key(p)[1] or 0) <= n for p in prev):
                continue   # a stricter copy (Eviscerate at 5 combo points below Eviscerate at 4 or more)
        if len(out) < LIMIT:
            out.append(txt)
            for s in sp:
                shown.setdefault(s, []).append(txt)
            if len(sp) == 1 and txt in (f"**{sp[0]}**", f"**{sp[0]}** {REACTIVE.get(sp[0], '')}".strip()):
                done.add(sp[0])
            closed = floor
    if extras is not None:
        for (a, b), w in twists.items():
            extras.append(f"**{a}**: seal twisting. While **{b}** is up" + (f" and {w}" if w else "") + f", switch to {a}; just before "
                          f"your next swing, switch back to **{b}**, so the swing gets both seals")
    fill = filler(cls, out)
    if late is not None:
        late += [(s, n, f or fill or (re.findall(r"\*\*(.+?)\*\*", out[-1])[0] if out else None)) for s, n, f in pend]
    return keep, out


def filler(cls, prio):
    """The spell to cast whenever nothing above is ready: the last line, when it has no condition and the spell no cooldown (Bloodrage,
    Aimed Shot, Fire Nova or Sniper Shot at the bottom of a list are cooldowns, not fillers)."""
    if not prio:
        return None
    names = re.findall(r"\*\*(.+?)\*\*", prio[-1])
    if len(names) != 1 or prio[-1] != f"**{names[0]}**":
        return None
    return names[0] if cooldowns(cls).get(names[0]) is False else None


def auto_line(cls, entry):
    """What fills the gaps when the list has no filler: a hunter's Auto Shot, a melee's white swings (by the raid entry's range)."""
    dist = (entry or {}).get("distance", 5)
    if cls == "hunter" and dist > 5:
        return "Between these, **Auto Shot** keeps firing on its own."
    if dist <= 5:
        return "Between these, your white swings do the rest."
    return None


def pre_pull(cls, pre, held=None):
    """Spells of the class cast or activated before the pull (the APL's prepull actions); a talent's ability only when the build has the
    talent (`held`: the build's talent names; 2026-10-09: Amplify Curse was listed for builds without it)."""
    ok = class_spells(cls)
    tal = talent_names(cls)
    names = [m.group(1).strip() for _, a in pre for m in [re.match(r"^(?:cast|channel|activate) (.+)$", a)] if m]
    return [n for n in dict.fromkeys(names) if n in ok and n not in RACIAL and (held is None or n not in tal or n in held)]


def mcd_window(texts):
    """Seconds before the end of the fight in which the rotation fires its other cooldowns ("if time left in the fight ≤ 45s: use every
    other cooldown when ready": Fury's Recklessness and trinkets wait for the last 45 seconds), else None."""
    for t in texts:
        m = re.match(r"^if time left in the fight (?:≤|<) ([\d.]+)s?: use every other cooldown", t.strip(), re.I)
        if m:
            return float(m.group(1))
    return None


# what to say for a cooldown whose use the generic line gets wrong
ADV_TEXT = {"Preparation": "once a fight, right after **Vanish**: it finishes the cooldown on your other rogue abilities, so you can Vanish again",
            "Swift Judgement": "whenever it is ready: it finishes the cooldown on **Judgement** and makes the next one free, so judge again at once",
            "Readiness": "once a fight, right after your other cooldowns: it finishes their cooldowns"}


def advanced(cls, casts, shown, window=None):
    """The advanced extras: the class's own spells a build casts in the simulator that the simple list leaves out (cooldowns such as
    Presence of Mind, Bestial Wrath, Death Wish, mana tools such as Evocation), with how often per fight. `casts` is the report's casts
    per fight for the build; `shown` the spells already in the simple list; `window` the rotation's end-of-fight cooldown window
    (mcd_window)."""
    ok = set(cooldowns(cls))   # the active spells of the beta spellbook: a passive talent's effect (Ignite) shows in the casts too
    cds = cooldown_seconds(cls)
    out = []
    for sp, n in sorted(casts.items(), key=lambda kv: -kv[1]):
        if sp not in ok or sp in shown or sp in RACIAL or n < 0.05 or sp in ("Auto Shot", "Attack", "Shoot"):   # automatic attacks
            continue
        times = f"about {round(n)} time{'s' if round(n) != 1 else ''} a fight"
        if sp in ADV_TEXT:
            out.append(f"**{sp}**: {ADV_TEXT[sp]}")
        elif sp in MANA_TOOLS:
            out.append(f"**{sp}**: when you run out of mana (needed in about {min(10, round(n * 10))} of 10 fights)" if n < 0.95 else
                       f"**{sp}**: when you run low on mana ({times})")
        elif n >= 8:   # a regular spell the short list had no room for
            out.append(f"**{sp}**: part of the rotation (about {n:.0f} times a fight)")
        elif n >= 0.95:
            when = f"in the last {_n(window)} seconds of the fight" if window else "at the start of the fight"
            if cds.get(sp, 0) >= 600:   # Recklessness (30 min), Preparation (10 min): once a fight
                out.append(f"**{sp}**: once a fight, {when}")
            elif window:
                out.append(f"**{sp}**: a cooldown, use it {when} ({times})")
            else:
                out.append(f"**{sp}**: a cooldown, use it at the start of the fight and again whenever it is ready ({times})")
        else:
            out.append(f"**{sp}**: now and then (in about {round(n * 10)} of 10 fights)")
    return out
