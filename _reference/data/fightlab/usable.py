"""What the game asks of a cast beyond its being ready, affordable and in reach (2026-11-22, the audit session): the stance, form,
shield, weapon, stealth, position, combo points, minimum range and health limit a spell's spellbook entry and tooltip state. Shared by
fightlab/force_run.py (a forced spell must pass it) and the engine's forced lines (engine.BaseModule.forced_line)."""
import json
import pathlib
import re

DATA = pathlib.Path(__file__).resolve().parent.parent

_SPELL_ROW = {}
# "Only usable on enemies that have 20% or less health" (Execute, Hammer of Wrath; "less than 20% health" in other texts)
HP_LIMIT = re.compile(r"[Oo]nly usable on (?:enemies|targets) (?:that have |with )?(?:less than |at or below )?(\d+)%(?: or less)? "
                      r"(?:health|of their health)")


def spell_row(cls, name):
    """(minimum range, "requires" text) of a spell's top rank in the spellbook ("8-35 yd range": 8; "Requires Cat Form")."""
    if (cls, name) not in _SPELL_ROW:
        row = (0.0, "")
        for tab in json.load(open(DATA / "forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
            for s in tab.get("spells", []):
                if s["name"] == name and s.get("ranks"):
                    r = s["ranks"][-1]
                    m = re.search(r"(\d+(?:\.\d+)?)\s*-\s*\d+ yd range", r.get("range") or "")
                    row = (float(m.group(1)) if m else 0.0, r.get("requires") or "")
        _SPELL_ROW[(cls, name)] = row
    return _SPELL_ROW[(cls, name)]


def min_range(cls, name):
    """A spell's minimum range from the spellbook's range text, 0 without one (2026-11-22)."""
    return spell_row(cls, name)[0]


def why_unusable(mod, cls, s, m, p=None):
    """None when the game allows the cast beyond its being ready, affordable and in reach, else the reason (2026-11-22, the audit
    session: the forced runs of the morning had cast Execute at full health and in Defensive Stance, Intercept in melee and in Battle
    Stance, and the melee hunters' Arcane Shot inside its 8-yard minimum range):
    - the stance its spellbook entry requires (the warrior's stance_ok), a druid form ("Requires Cat Form", "Requires Bear Form"),
      a shield (the player's block), daggers (the rogue's main hand);
    - stealth and "behind the target" (Ambush, Garrote, Cheap Shot; Backstab, Shred, Ravage, Pounce): the lab plays them only in the
      opener, which a forced cast never is, or from behind while a pet holds the mob;
    - combo points for a finisher; a pet's or a demon's ability is not the player's cast;
    - its minimum range and a tooltip's health limit."""
    mn, req = spell_row(cls, s.name) if cls else (0.0, "")
    tip = getattr(s, "text", "") or ""
    if getattr(mod, "stance_ok", None) and not mod.stance_ok(s.name):
        need = re.search(r"Requires ([A-Z][\w ,]*?Stance(?:, [A-Z][\w ]*?Stance)*)", req)
        return f"needs {need.group(1) if need else 'another stance'} (in {getattr(mod, 'stance', '?')})"
    form = getattr(mod, "form", None)
    if "Requires Cat Form" in req and form != "cat":
        return f"needs Cat Form (in {form})"
    if ("Requires Bear Form" in req or "Dire Bear Form" in req) and form != "bear":
        return f"needs Bear Form (in {form})"
    if "Requires Shields" in req and not (p is not None and (getattr(p, "block", 0) or 0) > 0):
        return "needs a shield"
    if "Requires Daggers" in req and not getattr(mod, "mh_dagger", False):
        return "needs a dagger in the main hand"
    if "Requires Stealth" in req or re.search(r"[Mm]ust be stealthed", tip):
        return "needs stealth (the opener only)"
    if re.search(r"behind the target", tip) and (m is None or getattr(m, "target", "player") == "player"):
        return "from behind the target only (the mob is on you)"
    if "Combo Points" in req and not (p is not None and (getattr(p, "combo", 0) or 0) >= 1):
        return "needs combo points"
    if re.search(r"(?:^|; )(?:Pet|Demon): ", req):
        return "a pet's or a demon's ability"
    if mn and m is not None and m.dist < mn:
        return f"inside its {mn:g}-yard minimum range"
    hl = HP_LIMIT.search(tip)
    if hl and m is not None and m.hp_max > 0 and m.hp > float(hl.group(1)) / 100 * m.hp_max:
        return f"only on a target below {hl.group(1)}% health"
    return None


def usable(mod, cls, s, m, p=None):
    """Whether the game allows the cast (why_unusable is None)."""
    return why_unusable(mod, cls, s, m, p) is None
