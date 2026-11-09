"""Restoration druid raid healer for the healer lab: Rejuvenation kept on the tank, Healing Touch (downranked to the deficit)
when the tank is low, Regrowth as the fast heal, Swiftmend and Nature's Swiftness in emergencies, Wild Growth or Tranquility
when the group is hurt, Innervate on yourself when mana runs low.

Talent mechanics follow the 70291 tooltips (`forever-talents/druid.json`, numbers read from them; 2026-10-09 fixes): Nature's Grace
gives 10% faster casts and a 10% shorter global cooldown for 3 s after a critical direct heal (Classic's was 0.5 s off the next
cast); Gift of the Earthmother takes 0.5 s off the global cooldown of Rejuvenation, Swiftmend and Wild Growth (it was modelled as
+5% periodic healing); Nature's Splendor lengthens Rejuvenation by 3 s and Regrowth by 6 s, more ticks of the same size (it was
+4%); Swiftmend leaves the heal over time in place (Forever's tooltip dropped Classic's "Consumes"; SWIFTMEND_CONSUMES reads it);
Moonglow does nothing for heals (it cheapens damaging spells only, and the engine's damage-only test reads "damage spell", not
"damaging spells", so its parsed -25% mana had reached every heal)."""
import json
import re

import engine as E
import tables as T

PIPELINE = {"spec": "resto-heal", "hand": "resto-raid-healer", "opt": "opt-resto-heal-raid-heal", "tag": "resto"}

_TREE = json.load(open(E.ROOT / "_reference/data/forever-talents/druid.json", encoding="utf-8"))
_RANKS = {t["name"]: t["ranks"] for tr in _TREE["trees"] for t in tr["talents"]}
_NUM = re.compile(r"(\d+(?:\.\d+)?)")


def talent_text(name, rank=1):
    """A talent's beta tooltip at a rank ('' when the tree has no such talent)."""
    ranks = _RANKS.get(name) or [""]
    return ranks[min(max(rank, 1), len(ranks)) - 1] or ""


def talent_numbers(name, rank=1):
    return [float(x) for x in _NUM.findall(talent_text(name, rank).replace(",", ""))]


def _first(nums, i, default=0.0):
    return nums[i] if len(nums) > i else default


# Nature's Grace: "... increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec."
NG_HASTE = _first(talent_numbers("Nature's Grace"), 0) / 100
NG_DURATION = _first(talent_numbers("Nature's Grace"), 1, 3.0)
# Gift of the Earthmother: "Reduces the global cooldown by 0.5 seconds on your Rejuvenation, Swiftmend, and Wild Growth spells."
_gote = re.search(r"by ([\d.]+) seconds? on your (.+?) spells?", talent_text("Gift of the Earthmother"))
GOTE_CUT = float(_gote.group(1)) if _gote else 0.0
GOTE_SPELLS = tuple(x.strip() for x in re.split(r",\s*(?:and\s+)?|\s+and\s+", _gote.group(2)) if x.strip()) if _gote else ()
# Nature's Splendor: "Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, ..."
SPLENDOR = {}
for _name in ("Rejuvenation", "Regrowth"):
    _m = re.search(rf"{_name} spells? by ([\d.]+) sec", talent_text("Nature's Splendor"))
    if _m:
        SPLENDOR[_name] = float(_m.group(1))
# Bloom (2026-11-08, the user's audit: the deep search had parked spare points on Furor and Improved Wrath because Bloom read 0):
# "When your Rejuvenation or Regrowth spell expires due to its duration, the target is instantly healed for an amount equal to 100% of
# your Spirit." Read as a flat heal of that share of Spirit, no healing bonus or crit (the tooltip names none). Dispels are not modelled.
_bloom = re.search(r"equal to (\d+)% of your Spirit", talent_text("Bloom"))
BLOOM_SPIRIT = float(_bloom.group(1)) / 100 if _bloom else 0.0
BLOOM_SPELLS = ("Rejuvenation", "Regrowth")
# Improved Tranquility: "Reduces threat caused by Tranquility by 100% and its cooldown by 60%." (rank 2; 30% at rank 1): the cooldown cut.
# Threat is not modelled.


def tranquility_cut(rank):
    m = re.search(r"cooldown by (\d+)%", talent_text("Improved Tranquility", rank))
    return float(m.group(1)) / 100 if (m and rank) else 0.0


# Swiftmend: Classic "Consumes a Rejuvenation or Regrowth effect ..."; Forever's tooltip no longer says so.
SWIFTMEND_CONSUMES = bool(re.search(r"\bconsume", talent_text("Swiftmend"), re.I))


class Healer(E.BaseHealer):
    CLASS = "druid"
    SPEC = "resto-heal"
    ROLES = {"big": "Healing Touch", "fast": "Regrowth", "hot": "Rejuvenation", "group": "Wild Growth", "instant": "Swiftmend"}
    TALENT_SPELLS = {"Swiftmend": "Swiftmend", "Wild Growth": "Wild Growth", "Nature's Swiftness": "Nature's Swiftness"}
    MECHANICS = {
        "Swiftmend": "instant heal for the full periodic amount of the target's Regrowth or Rejuvenation, 15 s cooldown; the heal over time "
                     "is consumed when the tooltip says so (SWIFTMEND_CONSUMES, read from it: 70753's \"the consumed spell\")",
        "Nature's Swiftness": "instant Healing Touch on a tank under the emergency threshold, every 3 min",
        "Nature's Grace": "a critical direct heal: 10% faster casts and a 10% shorter global cooldown for 3 s",
        "Genesis": "+1%/rank periodic healing",
        "Gift of the Earthmother": "Rejuvenation, Swiftmend and Wild Growth: 0.5 s shorter global cooldown",
        "Nature's Splendor": "Rejuvenation +3 s, Regrowth +6 s: one or two more ticks of the same size",
        "Moonglow": "nothing for heals: Forever's Moonglow cheapens damaging spells only",
        "Wild Growth": "679 over 7 s on the group, 6 s cooldown: the group heal",
        "Bloom": "a Rejuvenation or Regrowth that runs its full duration heals its target for 100% of your Spirit (2026-11-08)",
        "Improved Tranquility": "Tranquility's cooldown 30% / 60% shorter (2026-11-08); threat not modelled",
        "Innervate": "on yourself under 40% mana (every 6 min): 5x regeneration for 20 s, all of it while casting (the tooltip; until "
                     "2026-10-17 the five-second rule still cut it)",
    }
    SIMULATED = {"Swiftmend", "Nature's Swiftness", "Nature's Grace", "Genesis", "Gift of the Earthmother", "Nature's Splendor", "Wild Growth", "Gift of Nature",
                 "Improved Rejuvenation", "Naturalist", "Improved Regrowth", "Reflection", "Tranquil Spirit", "Living Spirit", "Nature's Majesty", "Moonglow", "Heart of the Wild",
                 "Bloom", "Improved Tranquility"}
    SHARE_SOURCE = {"Healing Touch": "healing_touch", "Regrowth": "regrowth", "Rejuvenation": "rejuvenation", "Tranquility": "tranquility"}

    def __init__(self, allocation, game="forever"):
        super().__init__(allocation, game)
        if "Wild Growth" not in self.book:
            self.ROLES = dict(self.ROLES, group="Tranquility")
        cut = tranquility_cut(self.rank("Improved Tranquility"))
        if cut:
            for h in self.book.get("Tranquility", []):
                h.cooldown *= 1 - cut
        if self.rank("Nature's Splendor"):
            for name, extra in SPLENDOR.items():
                for h in self.book.get(name, []):   # this healer's own copy of the spellbook
                    if h.hot > 0 and h.hot_dur > 0 and h.tick_every > 0:
                        ticks = max(1, int(round(h.hot_dur / h.tick_every)))
                        add = max(1, int(round(extra / h.tick_every)))
                        h.hot *= (ticks + add) / ticks
                        h.hot_dur += add * h.tick_every

    def heal_mult_hook(self, spell, target, sim):
        if "hot" in spell.tags:
            return 1 + _first(talent_numbers("Genesis", self.rank("Genesis")), 0) / 100 if self.rank("Genesis") else 1.0
        return 1.0

    def cast_hook(self, spell, sim):
        return 1.0

    def cast_time(self, spell, sim):
        t = super().cast_time(spell, sim)
        if t > 0 and sim.buffs.get("Nature's Grace", 0.0) > sim.t:
            t = max(T.GCD * (1 - NG_HASTE), t / (1 + NG_HASTE))
        return t

    def on_hot_expire(self, sim, name, target):
        if name in BLOOM_SPELLS and BLOOM_SPIRIT and self.rank("Bloom"):
            sim.apply_heal(self.book[name][-1], target, self.spirit * BLOOM_SPIRIT, False, label="Bloom")

    def on_heal(self, sim, spell, target, amount, crit):
        if crit and self.rank("Nature's Grace") and spell.heal_min > 0:
            sim.buffs["Nature's Grace"] = sim.t + NG_DURATION

    def before_decide(self, sim):
        tank = sim.tank
        if "Innervate" in self.book and sim.mana < 0.4 * self.mana_max and self.cooldown_ready(sim, "Innervate", 360.0):
            sim.cd["Innervate"] = sim.t
            sim.buffs["Innervate"] = sim.t + 20.0
            sim.gcd_until = sim.t + T.GCD
            return None
        if "Nature's Swiftness" in self.book and tank.hp > 0 and tank.frac < T.EMERGENCY and self.cooldown_ready(sim, "Nature's Swiftness", 180.0):
            sim.cd["Nature's Swiftness"] = sim.t
            sim.instant_next = True
            return (self.book["Healing Touch"][-1], tank)
        return None

    def emergency_spell(self, sim, role, target):
        if role == "instant":
            sm = self.book.get("Swiftmend")
            if sm and self.cooldown_ready(sim, "Swiftmend", 15.0):
                for name in ("Regrowth", "Rejuvenation"):
                    if name in target.hots:
                        return (sm[-1], target)
            return None
        return super().emergency_spell(sim, role, target)

    def on_cast_done(self, sim, spell, target):
        if spell.name == "Swiftmend":
            for name in ("Regrowth", "Rejuvenation"):
                if name in target.hots:
                    src = self.book[name][-1]
                    per = target.hots[name][0]
                    ticks = max(1, int(round(src.hot_dur / src.tick_every)))
                    if SWIFTMEND_CONSUMES:
                        del target.hots[name]
                    sim.apply_heal(spell, target, per * ticks, False, label="Swiftmend")
                    break
        # a shorter global cooldown after an instant (the engine set the full one just before this hook; a cast spell's has run out):
        # Gift of the Earthmother on its three spells, Nature's Grace 10% of the base global cooldown (the simulator's flat reading)
        gcd = T.GCD
        if self.rank("Gift of the Earthmother") and spell.name in GOTE_SPELLS:
            gcd -= GOTE_CUT
        if self.rank("Nature's Grace") and sim.buffs.get("Nature's Grace", 0.0) > sim.t:
            gcd -= T.GCD * NG_HASTE
        if gcd < T.GCD:
            sim.gcd_until = min(sim.gcd_until, sim.t + gcd)
