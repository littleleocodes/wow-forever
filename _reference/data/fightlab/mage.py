"""Mage module for the fight lab.

Spell ranks (damage, cost, cast, cooldown, chill, root, coefficient, burn) are read from
`_reference/data/forever-spells/mage.json` (the beta client build in forever-spells/); talent numbers are read from each rank's
tooltip in `_reference/data/forever-talents/mage.json`. What a talent *does* (the mechanic) is coded here per talent;
the numbers are the client's. Talents with no entry in MECHANICS are not simulated (listed by `not_simulated()`).

Playstyles:
- `frost-leveling`: single-target Frostbolt kiting: pull at max range, Frostbolt while the mob walks in, Frost Nova
  when it reaches melee, step back, Ice Lance / Frostbolt into the freeze, Fire Blast and wand to finish without
  overkill, Cone of Cold and Cold Snap as extra control, Ice Barrier before pulls.
- `fire-leveling`: Fireball at range, Scorch and Fire Blast when the mob is close, Frost Nova / Blast Wave for
  distance, Ice Lance into freezes if talented, Pyroblast on a full Heating Up, Combustion on the pull.
- `arcane-leveling` (2026-09-30, `decide_arcane`): Arcane Power and Presence of Mind on the pull, Arcane Blast stacked while the
  mana allows (client 70425: each stack 15% of Intellect as spell damage for 15 s from the first, +175% to the next Arcane Blast's
  cost; Arcane Wrath when talented), Arcane Missiles as the channel
  (free and twice as fast on a Missile Barrage proc), Frost Nova / Cone of Cold and a step back when the mob reaches you, Ice Lance
  into freezes if talented, Fire Blast and wand to finish without overkill. Frostbolt only when Arcane Missiles is unaffordable.
All drink conjured water and use Evocation between fights.
"""
import copy
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell
from tables import (GCD, MELEE_RANGE, SPELL_CRIT_BASE, WAND_SPEED, base_health, base_mana, gear_stats, int_per_spell_crit,
                    interp, mage_base_stats, mana_regen_tick, wand_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/mage.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/mage.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
BLIZZARD = re.compile(r"doing (\d[\d,]*) Frost damage over (\d+) sec")
DMG = re.compile(r"(\d[\d,]*) to (\d[\d,]*) (\w+) damage")
BURN = re.compile(r"additional (\d[\d,]*) (\w+) damage over (\d+) sec")
CHILL = re.compile(r"(?:slowing movement speed|slowed) by (\d+)% for (\d+) sec")
ROOTRX = re.compile(r"freezes them in place for up to (\d+) sec")
ABSORB = re.compile(r"absorbing ([\d,]+) damage")
ARMOR = re.compile(r"Increases Armor by (\d+)")
COEF = re.compile(r"([\d.]+)% of spell power")
TICK_COEF = re.compile(r"([\d.]+)% of spell power \(per tick\)")   # a burn's own coefficient (Pyroblast: 15% a tick, client 70425)
DAZE = re.compile(r"Dazing them for (\d+)% reduced movement speed for (\d+) sec")   # Blast Wave (client 70425)
# Cone of Cold (client 70425; Blizzard's 16 Oct notes: "Movement speed of the first 4 targets hit is decreased by an additional 10% and the
# slow lasts an additional 3 seconds on those targets"): leveling pulls hold at most 4 mobs, so every mob in the cone gets it
COC_EXTRA = re.compile(r"The first (\d+) targets hit by this cone are slowed by an additional (\d+)% for an additional (\d+) sec")
# a burn's tick period: the client's periodic aura (the community simulator's spell store, de2b4da): Pyroblast 3 s, Fireball 2 s
BURN_PERIOD = {"Pyroblast": 3.0}
MISSILES = re.compile(r"causing (\d[\d,]*) Arcane damage each second for (\d+) sec")
# client 70425: "Each time you cast Arcane Blast, you gain 15% of your Intellect as Spell Damage and the mana cost of Arcane Blast is
# increased by 175%. Effect stacks up to 4 times and lasts 15 sec from time of initial application." (70291: +10% to other spells' damage)
AB_STACK = re.compile(r"gain (\d+)% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by (\d+)%\. "
                      r"Effect stacks up to (\d+) times and lasts (\d+) sec")
# Winter's Chill (client 70425; Blizzard's beta notes of 2026-10-16, "increasing the target's damage taken from your next Cone of Cold
# by 5%"): Frostbolt, Frost Blast and a Fingers of Frost Ice Lance roll a stack; each stack gives the next Cone of Cold +5% damage and
# +7% spell damage coefficient (the triggered spell 12579's two effects, as the community simulator reads them, f72c7d7/de2b4da), and that
# Cone of Cold spends them. The tooltip's "40%" was read until 2026-10-17 (any Frost spell, never spent).
WC_DMG, WC_COEF = 0.05, 0.07
WC_SOURCES = ("Frostbolt", "Frost Blast")
AW_MANA = re.compile(r"Spell Damage equal to (\d+)% of your maximum Mana")   # Arcane Wrath (client 70425)
LANCE_FROZEN = re.compile(r"Deals (\d+)% increased damage to Frozen targets")   # Ice Lance: 200% since 70425 (300% before)

TALENT_SPELLS = {"Ice Lance": "Ice Lance", "Ice Barrier": "Ice Barrier", "Cold Snap": "Cold Snap", "Ice Block": "Ice Block",
                 "Pyroblast": "Pyroblast", "Blast Wave": "Blast Wave", "Arcane Wrath": "Arcane Wrath"}
DEFAULT_RANGE = {"Frost Nova": 10.0, "Cone of Cold": 10.0, "Arcane Explosion": 10.0, "Blast Wave": 10.0}
# the client carries none for Ice Lance: 0.10, the community simulator's fit to beta combat logs (2ce8265: hits of two level 20-26 mages at
# known spell power; 0.143 until 2026-10-09). Pyroblast and Blast Wave read theirs from the 70425 spellbook since 2026-10-17 (these two
# values are the fallback for an export without their ranks)
ASSUMED_COEF = {"Ice Lance": 0.10, "Pyroblast": 1.0, "Blast Wave": 0.129}


def _num(s):
    return float(s.replace(",", ""))


def _seconds(s):
    m = re.search(r"([\d.]+)\s*(sec|min)", s or "")
    if not m:
        return 0.0
    return float(m.group(1)) * (60 if m.group(2) == "min" else 1)


def load_spellbook():
    """{spell name: [Spell ranks sorted by level]} for the spells the module uses."""
    book = {}
    for tab in SPELLBOOK["tabs"]:
        for sp in tab["spells"]:
            for r in sp["ranks"]:
                txt = r.get("text", "")
                cost_txt = (r.get("cost") or "").replace(",", "")
                cost = _num(NUM.search(cost_txt).group(1)) if NUM.search(cost_txt) else 0.0
                cost_pct = "base mana" in cost_txt
                cast_txt = (r.get("cast") or "").lower()
                cast = 0.0 if "instant" in cast_txt or "channel" in cast_txt else _seconds(cast_txt)
                dm, ch, rt, bn = DMG.search(txt), CHILL.search(txt), ROOTRX.search(txt), BURN.search(txt)
                co = COEF.search(r.get("coefficient") or "")
                rm = re.search(r"(\d+) yd range", r.get("range") or "")
                rng = _num(rm.group(1)) if rm else DEFAULT_RANGE.get(sp["name"], 30.0)
                s = Spell(name=sp["name"], school=(r.get("school") or "arcane").lower(),
                          rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")), range=rng,
                          dmg_min=_num(dm.group(1)) if dm else 0.0, dmg_max=_num(dm.group(2)) if dm else 0.0,
                          coef=float(co.group(1)) / 100 if co else ASSUMED_COEF.get(sp["name"], 0.0),
                          chill=float(ch.group(1)) / 100 if ch else 0.0, chill_dur=float(ch.group(2)) if ch else 0.0,
                          root=float(rt.group(1)) if rt else 0.0,
                          aoe=sp["name"] in ("Frost Nova", "Cone of Cold", "Arcane Explosion", "Blizzard", "Blast Wave", "Flamestrike"),
                          tags=("cost_pct",) if cost_pct else ())
                s.text = txt
                if sp["name"] == "Frostfire Bolt" and not s.chill and "slowing movement speed by 40%" in txt:
                    s.chill, s.chill_dur = 0.40, 9.0   # assumption: the tooltip gives no duration; its burn and Frostbolt's chill last 9 s
                s.interrupt = parse_interrupt(txt)
                s.burn = _num(bn.group(1)) if bn else 0.0
                s.burn_dur = float(bn.group(3)) if bn else 0.0
                s.burn_period = BURN_PERIOD.get(sp["name"], 2.0)
                tc = TICK_COEF.search(r.get("coefficient") or "")
                # the burn's coefficient over all its ticks (Pyroblast 15% x 4 = 60%; Fireball's burn has none)
                s.burn_coef = float(tc.group(1)) / 100 * max(1, int(round(s.burn_dur / s.burn_period))) if (tc and s.burn) else 0.0
                dz = DAZE.search(txt)
                if dz:   # a daze is not a Chill effect: on_chill leaves Frostbite and Fingers of Frost out, __init__ undoes Permafrost
                    s.daze, s.chill_dur = float(dz.group(1)) / 100, float(dz.group(2))
                ce = COC_EXTRA.search(txt)
                if sp["name"] == "Cone of Cold" and ce and s.chill:   # 50% for 9 s on the first 4 targets
                    s.chill, s.chill_dur = s.chill + float(ce.group(2)) / 100, s.chill_dur + float(ce.group(3))
                ab = ABSORB.search(txt)
                s.absorb = _num(ab.group(1)) if ab else 0.0
                ar = ARMOR.search(txt)
                s.armor = _num(ar.group(1)) if ar else 0.0
                if "channel" in cast_txt:
                    s.tags = s.tags + ("channel",)
                bz = BLIZZARD.search(txt)
                if sp["name"] == "Blizzard" and bz:   # channelled area damage: 8 ticks over 8 s, per-tick coefficient
                    s.kind, s.channel, s.dot, s.dot_ticks, s.dot_dur = "channel", float(bz.group(2)), _num(bz.group(1)), int(float(bz.group(2))), float(bz.group(2))
                    s.dot_coef = float(co.group(1)) / 100 if co else 0.0
                    s.coef = 0.0
                ms = MISSILES.search(txt)
                if sp["name"] == "Arcane Missiles" and ms:   # one missile per second: N ticks over N sec, per-tick coefficient (2026-09-30)
                    n = int(ms.group(2))
                    s.kind, s.channel, s.dot, s.dot_ticks, s.dot_dur = "channel", float(n), _num(ms.group(1)) * n, n, float(n)
                    s.dot_coef, s.coef = s.coef, 0.0
                abs_ = AB_STACK.search(txt)
                # Arcane Blast: (Intellect share gained as spell damage per stack, own cost per stack, max stacks, duration from the first)
                s.ab_stack = (float(abs_.group(1)) / 100, float(abs_.group(2)) / 100, int(abs_.group(3)), float(abs_.group(4))) if abs_ else None
                aw = AW_MANA.search(txt)
                s.mana_sp = float(aw.group(1)) / 100 if aw else 0.0
                lf = LANCE_FROZEN.search(txt)
                s.frozen_mult = 1 + float(lf.group(1)) / 100 if lf else 0.0
                book.setdefault(sp["name"], []).append(s)
    for name in book:
        book[name].sort(key=lambda x: (x.level, x.rank))
    # Pyroblast and Blast Wave: the 70425 export holds every rank (Pyroblast 1-8 from level 20, Blast Wave 1-5 from 30, with costs and
    # coefficients); until 2026-10-17 they were synthesised (Pyroblast from Fireball's ranks, Blast Wave from the talent tooltip, no daze).
    # The synthesis stays as the fallback for an export that holds rank 1 only.
    if "Fireball" in book and len(book.get("Pyroblast", [])) < 2:
        pyro = []
        for fb in book["Fireball"]:
            if fb.level < 20:
                continue
            p = Spell(name="Pyroblast", school="fire", rank=len(pyro) + 1, level=fb.level, cost=round(fb.cost * 1.25), cast=6.0, range=35.0,
                      dmg_min=round(fb.dmg_min * 1.2), dmg_max=round(fb.dmg_max * 1.2), coef=1.0)
            p.text, p.burn, p.burn_dur, p.absorb, p.armor = "synthesised from Fireball", round(fb.burn * 3.5), 12.0, 0.0, 0.0
            pyro.append(p)
        if pyro:
            book["Pyroblast"] = pyro
    bw = []
    for L in (30, 38, 46, 54, 60) if len(book.get("Blast Wave", [])) < 2 else ():
        avg = interp([(30, 169.0), (60, 493.0)], L)
        b = Spell(name="Blast Wave", school="fire", rank=len(bw) + 1, level=L, cost=215.0, cast=0.0, cooldown=45.0, range=10.0,
                  dmg_min=round(avg * 0.92), dmg_max=round(avg * 1.08), coef=0.129, aoe=True)
        b.text, b.burn, b.burn_dur, b.absorb, b.armor = "synthesised from the talent tooltip", 0.0, 0.0, 0.0, 0.0
        b.burn_period, b.burn_coef, b.daze, b.chill_dur = 2.0, 0.0, 0.5, 6.0
        bw.append(b)
    if bw:
        book["Blast Wave"] = bw
    return book


BOOK = load_spellbook()


def talent_numbers():
    out = {}
    for tr in TREE["trees"]:
        for t in tr["talents"]:
            out[t["name"]] = [[float(x) for x in NUM.findall(rank.replace(",", ""))] for rank in t["ranks"]]
    return out


TNUM = talent_numbers()

MECHANICS = {
    "Improved Frostbolt": "Frostbolt (and Frost Blast, client 70425) cast time -0.1s per rank",
    "Improved Counterspell": "Counterspell also silences: +2/4 s lockout on a caster mob (tables.MOB_CASTER_SHARE of pulls)",
    "Elemental Precision": "+1% hit per rank with Frost and Fire spells",
    "Ice Shards": "Frost crit damage bonus +20% per rank of the 50% spell bonus (x2.0 at 5/5)",
    "Permafrost": "chill duration +11/22/33%, extra slow +3/6/10%",
    "Improved Frost Nova": "Frost Nova cooldown -2s per rank",
    "Frostbite": "each chill (Frostbolt, Cone of Cold, Ice Armor proc) has 5% per rank to freeze 5s",
    "Piercing Ice": "+2% Frost damage per rank",
    "Frost Channeling": "-5% Frost mana cost per rank",
    "Ice Lance": "unlocks Ice Lance (ranks by level; x3 damage vs Frozen since client 70425, x4 before; coefficient 0.10, the simulator's fit to beta logs)",
    "Arctic Reach": "+10% Frostbolt range per rank (longer pull)",
    "Shatter": "+17/33/50% crit vs Frozen targets (Frost Nova, Frostbite, Fingers of Frost)",
    "Improved Cone of Cold": "+12/23/35% Cone of Cold damage",
    "Cold Snap": "resets Frost Nova / Cone of Cold / Ice Barrier when the mob is in melee and Nova is down",
    "Fingers of Frost": "15% per chill: the next 1 (rank 1) / 2 (rank 2) spell casts count as Frozen, 15s",
    "Winter's Chill": ("20%/rank per Frostbolt, Frost Blast or Fingers of Frost Ice Lance hit: the next Cone of Cold +5% damage and +7% "
                       "spell damage coefficient per stack and spends them, up to 5 stacks, 15s (client 70425 and the 16 Oct beta notes; the "
                       "duration is an assumption; until 70291 +2% Frostbolt/Ice Lance crit per stack)"),
    "Ice Barrier": "absorb (447..819 by level) before every pull, 30s cooldown; no pushback while it holds",
    "Frost Warding": "+15/30% armor from Frost/Ice Armor",
    "Wand Specialization": "+13/25% wand damage",
    "Arcane Concentration": "2%/rank per damaging spell hit: next damage spell is free (Clearcasting)",
    "Arcane Meditation": "17/33/50% of Spirit regen continues inside the five-second rule",
    "Arcane Subtlety": "lower target resistance: partial-resist loss -20% per rank",
    "Magic Absorption": "1%/rank of maximum mana back when a spell misses (full resist)",
    "Arcane Resilience": "armor equal to 25/50% of Intellect",
    "Arcane Instability": "+1% spell damage and +1% spell crit per rank",
    "Arcane Mind": "+2% Intellect per rank (Arcane crit damage unused)",
    "Presence of Mind": "an instant Frostbolt/Fireball opener every 3 min",
    "Improved Fire Blast": "Fire Blast cooldown -1s and range +8/15 yd per rank (client 70425; replaced Wake of Fire and its on-kill crit)",
    "Incineration": "+2% crit per rank on Fire Blast, Ice Lance, Arcane Blast, Scorch",
    "Master of Elements": "Fire/Frost crits refund 10% per rank of the spell's base mana",
    "Fire Power": "+1% Fire damage per rank per Fire effect of yours on the target (burns, Ignite, Improved Scorch, Impact's stun), up to 4 "
                  "effects (client 70425; the 16 Oct notes list the effects)",
    "Arcane Focus": "+1% hit per rank with Arcane spells (neither loop casts Arcane spells)",
    "Improved Fireball": "Fireball cast time -0.1s per rank",
    "Flame Throwing": "+3 yd Fire range per rank (longer pull for the Fire loop)",
    "Ignite": "Fire crits burn for 8% per rank of the crit's damage over 4s",
    "Impact": "Fire spell hits have 3/7/10% chance to stun 2s (no movement, no swings)",
    "Burning Soul": "23%/rank chance to ignore pushback on Fire spells",
    "Pyroblast": "unlocks Pyroblast (6s cast; ranks 1-8 from the 70425 spellbook, burn 15% of spell power a tick every 3 s); cast on a full Heating Up",
    "Improved Scorch": "Scorch's chance (the rank) to stack +3% Fire damage taken, up to 5 stacks at every rank, 30s",
    "Heating Up": ("Fireball/Fire Blast/Scorch crits stack, Fire Blast adds one more whenever it hits (3 = Pyroblast cast -75%), 20s; a Presence "
                   "of Mind Pyroblast keeps them (client 70425 and the beta notes of 16 Oct)"),
    "Critical Mass": "+2% Fire crit per rank (5 ranks since client 70425)",
    "Blast Wave": "unlocks Blast Wave (instant AoE, daze 50% 6s, not a Chill effect, 45s cooldown; ranks 1-5 from the 70425 spellbook): a snare "
                  "when the mob is on us",
    "Combustion": "on the pull every 3 min (shared with Presence of Mind): +10% Fire crit per Fire hit until 3 crits",
}
# Talent effects only the Arcane playstyle (spec strings starting with "arcane", decide_arcane, 2026-09-30) applies; the Frost, Fire
# and Frostfire playstyles keep MECHANICS as it is (they never cast Arcane Blast or Arcane Missiles, so these are worth nothing there).
ARCANE_MECHANICS = {
    "Arcane Blast": "unlocks Arcane Blast (ranks by level, 15% of base mana, 1.5 s): each cast 15% of Intellect as spell damage and "
                    "+175% to its own cost per stack, up to 4 stacks, 15 s from the first (client 70425)",
    "Arcane Wrath": "unlocks Arcane Wrath (ranks by level, 3.5 s, 6 s cooldown; spell damage +5% of maximum mana): cast after the Arcane "
                    "Blast stacks while it can finish before the mob reaches you (client 70425)",
    "Missile Barrage": "Arcane Blast 20%/rank, each Arcane Missile 5%/rank, Arcane Wrath, Frostbolt, Fireball, Frostfire Bolt 10%/rank: the "
                       "next Arcane Missiles is free and fires its missiles every 0.5 s (half the channel), 15 s (duration assumed; client 70425)",
    "Improved Channeling": "20%/rank to lose no channel time to a hit during Arcane Missiles, 14%/rank no pushback on Arcane Blast and Arcane Wrath",
    "Arcane Power": "on the pull every 3 min (mana above half): +30% spell damage, +30% mana cost for 15 s",
    "Arcane Impact": "+2% crit per rank with Arcane spells",
    "Arcane Geometry": "+3 yd Arcane range per rank (longer Arcane Blast pull)",
    "Presence of Mind": "an instant Arcane Blast (Frostbolt without it) opener every 3 min",
    "Arcane Focus": "+1% hit per rank with Arcane spells",
}

# ------------------------------------------------------------ calibration and report metadata (read by calibrate.py / run.py)
SHARE_SOURCE = {"Frostbolt": "frostbolt", "Fire Blast": "fire_blast", "Frost Nova": "frost_nova", "Cone of Cold": "cone",
                "Arcane Missiles": "missiles", "Wand": "wand", "Ice Lance": "ice_lance"}
NEW_SOURCES = {"ice_lance": {"id": "ice_lance", "share": 0.0, "min_level": 20, "tags": ["type:spell", "school:frost", "instant", "frozen", "ability:Ice Lance"]}}
# talents to fit: "scale" = scale the entry's leveling-mode effects (created from its mode-less ones if needed);
# ("replace", [...]) = use this template as the leveling-mode effects, then scale
FIT = {"Improved Counterspell": "scale", 
    "Ice Lance": ("replace", [{"channel": "dmg", "scope": ["type:spell"], "values": [0.30]}]),
    "Shatter": ("replace", [{"channel": "dmg", "scope": ["school:frost"], "per_rank": 0.10}]),
    "Fingers of Frost": ("replace", [{"channel": "dmg", "scope": ["school:frost"], "per_rank": 0.03, "requires": {"Shatter": 3}}]),
    "Frostbite": ("replace", [{"channel": "dmg", "scope": ["school:frost"], "per_rank": 0.04}]),
    "Permafrost": ("replace", [{"channel": "surv", "scope": ["all"], "per_rank": 0.10}, {"channel": "sustain", "scope": ["all"], "per_rank": 0.08}]),
    "Ice Barrier": ("replace", [{"channel": "sustain", "scope": ["all"], "values": [0.15]}, {"channel": "surv", "scope": ["all"], "values": [0.30]}, {"channel": "dmg", "scope": ["type:spell"], "values": [0.02]}]),
    "Elemental Precision": ("replace", [{"channel": "hit", "scope": ["school:frost", "school:fire"], "per_rank": 0.01}, {"channel": "dmg", "scope": ["school:frost", "school:fire"], "per_rank": 0.005}]),
    "Cold Snap": "scale",
    "Winter's Chill": "scale",
    "Improved Frostbolt": "scale",
    "Ice Shards": ("replace", [{"channel": "dmg", "scope": ["school:frost"], "per_rank": 0.04, "requires": {"Shatter": 1}}, {"channel": "crit_bonus", "scope": ["school:frost"], "per_rank": 0.2}]),
    "Arcane Meditation": "scale",
    "Arcane Instability": "scale",   # crit + damage: the scorer has no crit cap, the Frozen Ice Lance already crits ~80% (sim: half the scorer value)
    "Arcane Mind": "scale",          # 2%/rank Intellect (the Arcane crit-bonus part is irrelevant to a Frost mage): ~0 in the sim
    "Frost Channeling": "scale",
    "Piercing Ice": "scale",
    "Presence of Mind": "scale",
    "Arcane Concentration": "scale",
    # Fire loop
    "Improved Fireball": "scale",
    "Ignite": "scale",
    "Fire Power": "scale",
    "Critical Mass": "scale",
    "Improved Scorch": "scale",
    "Heating Up": "scale",
    "Master of Elements": "scale",
    "Impact": "scale",
    "Burning Soul": "scale",
    "Improved Fire Blast": "scale",
    "Incineration": "scale",
    "Pyroblast": "scale",
    "Blast Wave": "scale",
    "Combustion": "scale",
    "Improved Frost Nova": "scale",
    "Frost Warding": "scale",
}
KEY_TALENTS = ["Ice Lance", "Shatter"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level: pull at max range, the mob walks in at 7 yd/s (slowed by chills), "
               "swings every 2 s once in melee (pushing casts back), Frost Nova when it arrives, a 2-second step back, Ice Lance/Frostbolt into the freeze, "
               "Fire Blast and wand to finish without overkill. Between fights: 2 s loot, 6 s travel, Evocation when low, conjured water below 35% mana, "
               "food below 65% health; a death costs 90 s. Every hit, miss, crit, partial resist, chill, freeze, proc and pushback is rolled.")
NOT_MODELLED = "runners, Ice Block, Mana Shield, Arcane Missiles (outside the arcane-leveling rotation), gear upgrades within a level bracket (adds and Blizzard only in the AoE variant, tables.MOBS_PER_PULL)."
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"spec": "frost-leveling", "hand": "leveling-frost", "opt": "opt-frost-leveling-leveling-st", "tag": "frost", "lookahead": 12,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60", "compare_extra": ["opt-fire-leveling-leveling-st"],
            "extra_reports": [{"spec": "fire-leveling", "build": "opt-fire-leveling-leveling-st"},
                              # the Frost optimizer build playing Frostfire Bolt instead of Frostbolt from 40 (decide_frostfire), against itself
                              # playing Frost: what the new spell is worth in leveling (new-builds survey, 2026-09-28)
                              {"spec": "frostfire-leveling", "build": "opt-frost-leveling-leveling-st", "compare": ["opt-frost-leveling-leveling-st"]}],
            "variants": [{"spec": "frost-aoe", "opt": "opt-frost-aoe-leveling-aoe", "tag": "aoe", "profile": "leveling-aoe", "lookahead": 12,
                          "sets": ["MOBS_PER_PULL=4"], "levels": "30,40,50,60", "calibrate_levels": "40,60", "label": "AoE grinding, 4 mobs per pull"}]}


class MageModule(BaseModule):
    special_stat = ("Frozen casts", "frozen_cast_share")
    # Arcane rotation knobs (decide_arcane; a rotations/mage-arcane-leveling.json "knobs" entry overrides them)
    AB_MAX_STACKS = 2        # Arcane Blasts in a row before Arcane Missiles spends the stacks
    AB_MANA_SHARE = 0.25     # the next Arcane Blast only while it costs at most this share of the current mana
    AP_MIN_MANA = 0.5        # Arcane Power on the pull only above this share of maximum mana
    AW_OPENER = 1            # Arcane Wrath (client 70425) as the pull's first cast when its 3.5 s cast fits before the mob arrives
    # client 70425 rewrote Arcane Blast (stacks are spell damage for every spell, 15 s, no longer spent by other spells): the stack
    # knobs set by hand for the 70291 rule are searched again by rotation_opt.py, with the Arcane Wrath opener
    ROTATION_KNOBS = {"AB_MAX_STACKS": [1, 2, 3, 4], "AB_MANA_SHARE": [0.15, 0.25, 0.4], "AW_OPENER": [0, 1]}

    def __init__(self, talents, level, spec="frost-leveling", gear="leveling", armor_spell="auto"):
        self.t = {k: v for k, v in talents.items() if v > 0}
        self.level = level
        self.spec = spec
        self.gear = gear
        self.armor_spell = armor_spell
        self.book = {name: self.rank_at(name) for name in BOOK}
        self.spells = {n: s for n, s in self.book.items() if s is not None}
        for tname, sname in TALENT_SPELLS.items():
            if not self.t.get(tname):
                self.spells.pop(sname, None)
        if self.rank("Improved Fire Blast") and "Fire Blast" in self.spells:   # +8/15 yd range (client 70425)
            self.spells["Fire Blast"] = copy.copy(self.spells["Fire Blast"])
            self.spells["Fire Blast"].range += self.tv("Improved Fire Blast", 1)
        bw = self.spells.get("Blast Wave")
        if bw is not None and getattr(bw, "daze", 0) and self.rank("Permafrost"):
            # the engine runs a daze through apply_chill, which adds Permafrost's duration and slow; a daze is not a Chill effect, so the
            # copy is pre-scaled to land at the tooltip's 50% for 6 s
            bw = self.spells["Blast Wave"] = copy.copy(bw)
            bw.chill_dur = bw.chill_dur / (1 + self.tv("Permafrost", 0) / 100)
            bw.daze = max(0.0, bw.daze - self.tv("Permafrost", 1) / 100)
        self._fight = None
        self._am_first_tick = None
        self._base_mana = 0.0

    # ------------------------------------------------------------ talent helpers
    def rank(self, name):
        return self.t.get(name, 0)

    def tv(self, name, idx=0, default=0.0):
        r = self.rank(name)
        if not r:
            return default if default else 0.0
        nums = TNUM.get(name, [])
        if r - 1 < len(nums) and idx < len(nums[r - 1]):
            return nums[r - 1][idx]
        return 0.0

    def not_simulated(self):
        mech = dict(MECHANICS, **ARCANE_MECHANICS) if self.is_arcane() else MECHANICS
        return sorted(n for n in self.t if n not in mech)

    def rank_at(self, name):
        ranks = [s for s in BOOK.get(name, []) if s.level <= self.level]
        return ranks[-1] if ranks else None

    # ------------------------------------------------------------ character
    def make_player(self, level):
        base = mage_base_stats(level)
        g = gear_stats(level, self.gear)
        intellect = (base["intellect"] + g["intellect"]) * (1 + self.tv("Arcane Mind", 0) / 100)
        spirit = base["spirit"] + g["spirit"]
        stamina = base["stamina"] + g["stamina"]
        armor_spell = self.armor_choice()
        armor = g["armor"] + (armor_spell.armor if armor_spell else 0.0) * (1 + self.tv("Frost Warding", 0) / 100)
        armor += intellect * self.tv("Arcane Resilience", 0) / 100
        bm = base_mana(level)
        p = Player(level=level, hp_max=base_health(level) + 10 * stamina, hp=0.0, mana_max=bm + 15 * intellect, mana=0.0,
                   base_mana=bm, spirit=spirit, intellect=intellect, spell_power=g["spell_power"], armor=armor,
                   spell_crit=SPELL_CRIT_BASE + intellect / int_per_spell_crit(level) / 100 + self.tv("Arcane Instability", 1) / 100,
                   dodge=0.04, ranged_crit=0.03)
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Arcane Meditation", 0) / 100
        if armor_spell is not None and armor_spell.name == "Mage Armor":
            p.regen_while_casting = min(1.0, p.regen_while_casting + 0.5)
        self.armor_spell_used = armor_spell.name if armor_spell else "none"
        return p

    def armor_choice(self):
        if self.armor_spell == "mage" and "Mage Armor" in self.spells:
            return self.spells["Mage Armor"]
        for name in ("Ice Armor", "Frost Armor"):
            if name in self.spells:
                return self.spells[name]
        return None

    def is_fire(self):
        return self.spec.startswith("fire")

    def is_frostfire(self):
        return self.spec.startswith("frostfire")

    def is_arcane(self):
        return self.spec.startswith("arcane")

    def arcane_blast(self):
        """The Arcane Blast rank to cast (None without the talent)."""
        return self.spells.get("Arcane Blast") if self.rank("Arcane Blast") else None

    def ab_stacks(self, fight):
        b = fight.p.buff("Arcane Blast", fight.t)
        return b["stacks"] if b else 0

    @staticmethod
    def sch(spell, school):
        """True when the spell is of this school; Frostfire Bolt ("fire, frost") counts as both (2026-09-28)."""
        return school in {x.strip() for x in (spell.school or "").split(",")}

    def pull_range(self):
        if self.is_arcane() and self.arcane_blast() is not None:
            return self.arcane_blast().range + self.tv("Arcane Geometry", 0)
        if self.is_frostfire() and self.spells.get("Frostfire Bolt"):
            return self.spells["Frostfire Bolt"].range + self.tv("Flame Throwing", 0)
        if self.is_fire():
            fb = self.spells.get("Fireball")
            return (fb.range if fb else 35.0) + self.tv("Flame Throwing", 0)
        fb = self.spells.get("Frostbolt")
        return (fb.range if fb else 30.0) * (1 + self.tv("Arctic Reach", 0) / 100)

    # ------------------------------------------------------------ engine hooks: numbers
    def cast_time(self, spell):
        c = spell.cast
        if spell.name in ("Frostbolt", "Frost Blast"):   # Frost Blast: client 70425
            c = max(GCD, c - 0.1 * self.rank("Improved Frostbolt"))
        if spell.name in ("Fireball", "Frostfire Bolt"):
            c = max(GCD, c - 0.1 * self.rank("Improved Fireball"))
        if spell.name == "Pyroblast" and self._fight:
            hs = self._fight.p.buff("Heating Up", self._fight.t)
            if hs:
                c = max(GCD, c * (1 - 0.25 * hs["stacks"]))
        if c > 0 and self._fight and self._fight.p.buff("Presence of Mind", self._fight.t):
            return 0.0
        return c

    def mana_cost(self, spell):
        cost = spell.cost
        if "cost_pct" in spell.tags:
            cost = cost / 100 * self._base_mana
        if self.sch(spell, "frost"):
            cost *= 1 - self.tv("Frost Channeling", 0) / 100
        if self.is_arcane() and self._fight is not None:
            f = self._fight
            if spell.name == "Arcane Blast" and getattr(spell, "ab_stack", None):
                cost *= 1 + spell.ab_stack[1] * self.ab_stacks(f)
            if f.p.buff("Arcane Power", f.t):
                cost *= 1 + self.tv("Arcane Power", 2) / 100
        return cost

    def final_cost(self, fight, spell, cost):
        cc = fight.p.buff("Clearcasting", fight.t)
        if cc and (spell.dmg_max > 0 or (spell.name == "Arcane Missiles" and cost > 0)):   # (a Missile Barrage missile is free already)
            del fight.p.buffs["Clearcasting"]
            return 0.0
        return cost

    def hit_bonus(self, spell):
        if (self.sch(spell, "frost") or self.sch(spell, "fire")):
            return self.tv("Elemental Precision", 0) / 100
        if self.sch(spell, "arcane"):
            return self.tv("Arcane Focus", 0) / 100
        return 0.0

    def crit_bonus(self, spell, frozen):
        c = 0.0
        f = self._fight
        if frozen:
            c += self.tv("Shatter", 0) / 100
        if spell.name in ("Fire Blast", "Ice Lance", "Arcane Blast", "Scorch"):
            c += self.tv("Incineration", 0) / 100
        if self.sch(spell, "fire"):
            c += self.tv("Critical Mass", 0) / 100
            if f and f.p.buff("Combustion", f.t):
                c += 0.10 * f.p.buffs["Combustion"].get("hits", 0)
        if self.is_arcane() and self.sch(spell, "arcane"):
            c += self.tv("Arcane Impact", 0) / 100
        return c

    def crit_damage_bonus(self, spell):
        # "increases the critical strike damage bonus of your Frost spells by 100%": 100% of a spell crit's 50% bonus, x2.0 at 5/5 (as the
        # warlock's Ruin and the druid's Vengeance). Until 2026-10-09 the full rank value was added: x2.5 (found by the shaman's review)
        if self.sch(spell, "frost"):
            return 0.5 * self.tv("Ice Shards", 0) / 100
        if self.sch(spell, "arcane"):
            return 0.5 * self.tv("Arcane Mind", 1) / 100
        return 0.0

    def lance_frozen_mult(self):
        """Ice Lance's damage factor against a Frozen target, from its tooltip (x3 since client 70425, x4 before)."""
        s = self.spells.get("Ice Lance")
        return getattr(s, "frozen_mult", 0.0) or 3.0

    def sp_bonus(self, spell):
        """Spell damage the module adds on top of the player's (client 70425): Arcane Blast's stacks (15% of Intellect each, every
        spell) and Arcane Wrath's 5% of maximum mana (its own damage). The engine adds coef x spell power itself, so the module turns
        this into an exact expected-damage factor (sp_factor) instead of writing a buff into the player's stats."""
        f = self._fight
        if f is None:
            return 0.0
        b = 0.0
        if self.is_arcane():
            ab = self.arcane_blast()
            if ab is not None and ab.ab_stack:
                b += ab.ab_stack[0] * self.ab_stacks(f) * f.p.intellect
        if getattr(spell, "mana_sp", 0.0):
            b += spell.mana_sp * f.p.mana_max
        return b

    def sp_factor(self, spell, periodic):
        b = self.sp_bonus(spell)
        if b <= 0 or self._fight is None:
            return 1.0
        sp = self._fight.p.spell_power
        if periodic:
            base, coef = spell.dot / max(1, spell.dot_ticks), spell.dot_coef
        else:
            base, coef = (spell.dmg_min + spell.dmg_max) / 2, spell.coef
        mean = base + coef * sp
        return (mean + coef * b) / mean if coef > 0 and mean > 0 else 1.0

    def damage_multiplier(self, spell, frozen):
        return self.talent_multiplier(spell, frozen) * self.sp_factor(spell, False)

    def periodic_multiplier(self, spell):
        return self.talent_multiplier(spell, False) * self.sp_factor(spell, True)

    def fire_effects(self):
        """Fire effects of yours on the target, for Fire Power (client 70425: "per your Fire effects on the target ... Effects which mix
        multiple schools of magic do not qualify"): the burns and dots of pure Fire spells, Ignite, the Improved Scorch vulnerability and
        Impact's stun (Blizzard's 16 Oct notes: "the effects which can grant increased Fire damage from this talent are Ignite, Improved
        Scorch, Fireball, and Pyroblast, and Impact"; Impact counted since 2026-10-17)."""
        f = self._fight
        if f is None:
            return 0
        names = set()
        for d in f.m.dots:
            if d[2] <= 0:
                continue
            n = d[0][:-5] if d[0].endswith(" burn") else d[0]
            src = BOOK.get(n)
            if n == "Ignite" or (src and (src[0].school or "") == "fire"):
                names.add(n)
        sc, im = f.m.debuffs.get("Improved Scorch"), f.m.debuffs.get("Impact")
        return len(names) + (1 if sc and sc["until"] > f.t else 0) + (1 if im and im["until"] > f.t else 0)

    def talent_multiplier(self, spell, frozen):
        m = 1.0 + self.tv("Arcane Instability", 0) / 100
        if self.sch(spell, "frost"):
            m *= 1 + self.tv("Piercing Ice", 0) / 100
        if self.sch(spell, "fire"):
            if self.rank("Fire Power"):   # per Fire effect, up to the cap (client 70425; a flat 2%/rank before)
                m *= 1 + min(self.fire_effects() * self.tv("Fire Power", 0), self.tv("Fire Power", 1)) / 100
            if self._fight:
                sc = self._fight.m.debuffs.get("Improved Scorch")
                if sc and sc["until"] > self._fight.t:
                    m *= 1 + 0.03 * sc["stacks"]
        if spell.name == "Ice Lance" and frozen:
            m *= self.lance_frozen_mult()
        if spell.name == "Cone of Cold":
            m *= 1 + self.tv("Improved Cone of Cold", 0) / 100
            wc = self._fight.m.debuffs.get("Winter's Chill") if self._fight else None
            if wc and wc["until"] > self._fight.t:   # client 70425: +5% damage and +7% coefficient per stack (WC_DMG, WC_COEF)
                n = wc["stacks"]
                sp = self._fight.p.spell_power + self.sp_bonus(spell)
                mean = (spell.dmg_min + spell.dmg_max) / 2 + spell.coef * sp
                m *= (1 + WC_DMG * n) * ((mean + WC_COEF * n * sp) / mean if mean > 0 else 1.0)
        if self.is_arcane() and self._fight is not None:
            f = self._fight
            if f.p.buff("Arcane Power", f.t):
                m *= 1 + self.tv("Arcane Power", 1) / 100
        return m

    def periodic_can_crit(self, spell):
        return spell.name == "Arcane Missiles"   # missiles crit like direct hits; Blizzard ticks and burns do not

    def resist_factor(self):
        return 1.0 - 0.2 * self.rank("Arcane Subtlety")

    def chill_duration_bonus(self):
        return self.tv("Permafrost", 0) / 100

    def chill_extra_slow(self):
        return self.tv("Permafrost", 1) / 100

    def armor_bonus(self):
        return 0.0

    def wand_damage(self):
        return wand_dps(self.level) * WAND_SPEED * (1 + self.tv("Wand Specialization", 0) / 100)

    def retreat_time(self):
        return 2.0

    def pushback_resisted(self, fight, spell):
        if fight.p.absorb > 0 and fight.t < fight.p.absorb_until:
            return True
        if self.sch(spell, "fire") and self.rank("Burning Soul"):
            return fight.rng.random() < self.tv("Burning Soul", 0) / 100
        if spell.name in ("Arcane Missiles", "Arcane Blast", "Arcane Wrath") and self.rank("Improved Channeling"):
            return fight.rng.random() < self.tv("Improved Channeling", 0 if spell.name == "Arcane Missiles" else 1) / 100
        return False

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        self._base_mana = fight.p.base_mana
        p, t = fight.p, fight.t
        fight.retreated_for = -1.0
        ib = self.spells.get("Ice Barrier")
        if ib and p.ready("Ice Barrier", t) and not (p.absorb > 0 and t < p.absorb_until):
            cost = self.mana_cost(ib)
            if p.mana >= cost + 150:
                p.mana -= cost
                p.fsr_until = t + 5.0
                p.absorb, p.absorb_until = ib.absorb, t + 60.0
                p.cooldowns["Ice Barrier"] = t + ib.cooldown
                fight.note(f"Ice Barrier ({ib.absorb:.0f})")
        # one 3-minute cooldown for both (client category 1151, the simulator since 2ce8265): a Fire model with Combustion uses it,
        # anything else Presence of Mind
        if self.rank("Combustion") and p.ready("Combustion", t) and self.is_fire():
            p.buffs["Combustion"] = {"until": t + 120.0, "hits": 0, "crits": 0}
            p.cooldowns["Combustion"] = p.cooldowns["Presence of Mind"] = t + 180.0
        elif self.rank("Presence of Mind") and p.ready("Presence of Mind", t):
            p.buffs["Presence of Mind"] = {"until": t + 60.0}
            p.cooldowns["Presence of Mind"] = p.cooldowns["Combustion"] = t + 180.0
        if self.is_arcane():
            p.buffs.pop("Arcane Blast", None)   # 15 s from the first stack (70425): spent by the next pull, cleared for simplicity
            if self.rank("Arcane Power") and p.ready("Arcane Power", t) and p.mana >= self.AP_MIN_MANA * p.mana_max:
                p.buffs["Arcane Power"] = {"until": t + self.tv("Arcane Power", 0)}
                p.cooldowns["Arcane Power"] = t + 180.0
                fight.note("Arcane Power")

    def on_chill(self, fight, spell):
        p, m, t, rng = fight.p, fight.m, fight.t, fight.rng
        if not self.sch(spell, "frost"):   # Frostbite and Fingers of Frost proc from Chill effects: Blast Wave's daze is none (2026-10-17)
            return
        fb = self.tv("Frostbite", 0)
        if fb and not m.frozen(t) and rng.random() < fb / 100:
            m.root_until = t + 5.0
            fight.note("Frostbite freeze")
        if self.rank("Fingers of Frost") and rng.random() < self.tv("Fingers of Frost", 0) / 100:
            charges = int(self.tv("Fingers of Frost", 1)) or 1
            p.buffs["Fingers of Frost"] = {"until": t + 15.0, "charges": charges}

    def consume_frozen_charge(self, fight):
        self._fof_cast = False   # whether this cast spent a Fingers of Frost charge (Winter's Chill on a Fingers of Frost Ice Lance)
        b = fight.p.buff("Fingers of Frost", fight.t)
        if b and b.get("charges", 0) > 0:
            b["charges"] -= 1
            if b["charges"] <= 0:
                del fight.p.buffs["Fingers of Frost"]
            self._fof_cast = True
            return True
        return False

    def on_hit(self, fight, spell, amount, crit, frozen):
        if amount > 0 and self.is_arcane() and self.rank("Missile Barrage") and spell.name in ("Arcane Blast", "Arcane Wrath", "Frostbolt", "Fireball", "Frostfire Bolt"):
            # client 70425 numbers: Arcane Blast 20%/rank (index 0), each missile 5%/rank (1, on_tick), the others 10%/rank (2)
            chance = self.tv("Missile Barrage", 0) if spell.name == "Arcane Blast" else self.tv("Missile Barrage", 2)
            if chance and fight.rng.random() < chance / 100:
                fight.p.buffs["Missile Barrage"] = {"until": fight.t + 15.0, "since": fight.t}
                fight.note("Missile Barrage")
        self._on_hit(fight, spell, amount, crit, frozen)

    def _on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t, rng = fight.p, fight.m, fight.t, fight.rng
        if amount <= 0:
            return
        if spell.burn > 0:   # the burn: its own coefficient over all its ticks (Pyroblast 15% a tick, 3 s; Fireball's has none) and the talents
            period = getattr(spell, "burn_period", 2.0) or 2.0
            total = (spell.burn + getattr(spell, "burn_coef", 0.0) * (p.spell_power + self.sp_bonus(spell))) * self.talent_multiplier(spell, False)
            fight.add_dot(spell.name + " burn", total, max(1, int(round(spell.burn_dur / period))), period)
        if spell.name == "Cone of Cold":   # spends the stacks it was boosted by (talent_multiplier ran before this)
            m.debuffs.pop("Winter's Chill", None)
        elif self.rank("Winter's Chill") and (spell.name in WC_SOURCES or (spell.name == "Ice Lance" and getattr(self, "_fof_cast", False)))                 and rng.random() < self.tv("Winter's Chill", 0) / 100:
            b = m.debuffs.get("Winter's Chill")
            # client 70425: "stacking up to 5 times" at every rank (70009-70291: up to the rank)
            stacks = min(int(self.tv("Winter's Chill", 2)) or 5, (b["stacks"] if b and b["until"] > t else 0) + 1)
            m.debuffs["Winter's Chill"] = {"until": t + 15.0, "stacks": stacks}
        if self.rank("Arcane Concentration") and rng.random() < self.tv("Arcane Concentration", 0) / 100:
            p.buffs["Clearcasting"] = {"until": t + 15.0}
        if crit and (self.sch(spell, "fire") or self.sch(spell, "frost")) and self.rank("Master of Elements"):
            p.mana = min(p.mana_max, p.mana + spell.cost * self.tv("Master of Elements", 0) / 100)
        if self.sch(spell, "fire"):
            if crit and self.rank("Ignite"):
                fight.add_dot("Ignite", amount * self.tv("Ignite", 0) / 100, 2, 2.0)
            # Heating Up (Hot Streak until 70170): a crit of these four adds a stack; client 70425: "Fire Blast grants an additional stack
            # every time it deals damage" (a Fire Blast crit adds two)
            add = (1 if crit and spell.name in ("Fireball", "Frostfire Bolt", "Fire Blast", "Scorch") else 0) + (1 if spell.name == "Fire Blast" else 0)
            if add and self.rank("Heating Up"):
                b = p.buffs.get("Heating Up")
                stacks = min(3, (b["stacks"] if b and b["until"] > t else 0) + add)
                p.buffs["Heating Up"] = {"until": t + 20.0, "stacks": stacks}
            if self.rank("Impact") and rng.random() < self.tv("Impact", 0) / 100 and not m.frozen(t):
                m.stun_until = t + 2.0
                m.debuffs["Impact"] = {"until": t + 2.0}   # a Fire effect on the target for Fire Power (16 Oct notes)
                fight.note("Impact stun")
            if spell.name == "Scorch" and self.rank("Improved Scorch") and rng.random() < self.tv("Improved Scorch", 0) / 100:
                b = m.debuffs.get("Improved Scorch")
                stacks = min(5, (b["stacks"] if b and b["until"] > t else 0) + 1)   # 70291: "stacking up to 5 times" at every rank (it used Winter's Chill's rank until 2026-10-09)
                m.debuffs["Improved Scorch"] = {"until": t + 30.0, "stacks": stacks}
            cb = p.buff("Combustion", t)
            if cb:
                cb["hits"] += 1
                if crit:
                    cb["crits"] += 1
                    if cb["crits"] >= 3:   # 70291: "until you have caused 3 non-periodic critical strikes" (4 in 70009)
                        del p.buffs["Combustion"]

    def on_tick(self, fight, spell, amount, crit):
        # Arcane Concentration: one roll per Arcane Missiles cast (on its first missile), like one damage spell hitting
        if spell.name == "Arcane Missiles" and fight.channel and fight.channel[2] == spell.dot_ticks:
            self._am_first_tick = fight.t   # the channel's first missile: a Missile Barrage proc from before it is spent (after_cast)
            if self.rank("Arcane Concentration") and fight.rng.random() < self.tv("Arcane Concentration", 0) / 100:
                fight.p.buffs["Clearcasting"] = {"until": fight.t + 15.0}
        # client 70425: each Arcane Missile hit has 5%/rank to proc Missile Barrage for the next channel
        if spell.name == "Arcane Missiles" and amount > 0 and self.is_arcane() and self.rank("Missile Barrage") \
                and fight.rng.random() < self.tv("Missile Barrage", 1) / 100:
            fight.p.buffs["Missile Barrage"] = {"until": fight.t + 15.0, "since": fight.t}

    def on_miss(self, fight, spell):
        ma = self.tv("Magic Absorption", 1)
        if ma:
            fight.p.mana = min(fight.p.mana_max, fight.p.mana + fight.p.mana_max * ma / 100)

    def after_cast(self, fight, spell):
        p, m, t = fight.p, fight.m, fight.t
        cd = spell.cooldown
        if spell.name == "Fire Blast":
            cd = max(0.0, cd - self.tv("Improved Fire Blast", 0))
        if spell.name == "Frost Nova":
            cd = max(0.0, cd - self.tv("Improved Frost Nova", 0))
        if cd > 0:
            p.cooldowns[spell.name] = t + cd
        pom = spell.cast > 0 and p.buff("Presence of Mind", t)
        if pom:
            del p.buffs["Presence of Mind"]
        if spell.name == "Pyroblast" and p.buff("Heating Up", t) and not pom:   # a Presence of Mind Pyroblast keeps them (beta notes 16 Oct)
            del p.buffs["Heating Up"]
        if self.is_arcane():
            if spell.name == "Arcane Blast" and spell.ab_stack:
                # client 70425: the stacks last 15 s from the first and no other spell spends them (70291: 8 s, spent by any damage spell)
                b = p.buff("Arcane Blast", t)
                stacks = min(spell.ab_stack[2], (b["stacks"] if b else 0) + 1)
                p.buffs["Arcane Blast"] = {"until": b["until"] if b else t + spell.ab_stack[3], "stacks": stacks}
            if spell.name == "Arcane Missiles":   # spends the proc it was cast on; one its own missiles gave stays for the next channel
                b = p.buffs.get("Missile Barrage")
                if b and (self._am_first_tick is None or b.get("since", -1.0) < self._am_first_tick):
                    p.buffs.pop("Missile Barrage", None)
                self._am_first_tick = None
            # Missile Barrage rolls in on_hit: only a spell that lands procs it (2026-10-09; it rolled after every cast, misses too)
        if spell.name in ("Frost Nova", "Cone of Cold", "Blast Wave") and m.in_melee and m.hp > 0:
            if spell.name == "Frost Nova" and m.rooted(t):
                fight.retreat_until = t + self.retreat_time()
                fight.retreated_for = m.root_until
            elif spell.name in ("Cone of Cold", "Blast Wave") and not m.rooted(t):
                fight.retreat_until = t + 1.5

    def on_hit_taken(self, fight, dmg, crit=False):
        if self.armor_spell_used in ("Ice Armor", "Frost Armor"):
            m, t = fight.m, fight.t
            m.attack_slow_until = t + 5.0
            fight.apply_chill(Spell("Ice Armor chill", "frost"), 0.30, 5.0)

    def evocation(self, p, t):
        if self.level < 20 or not p.ready("Evocation", t) or p.mana >= 0.4 * p.mana_max:
            return 0.0
        p.mana = min(p.mana_max, p.mana + 4 * 16 * mana_regen_tick(p.spirit))
        p.cooldowns["Evocation"] = t + 480.0
        return 8.0

    # ------------------------------------------------------------ priority lists
    def decide(self, fight):
        p, m, t = fight.p, fight.m, fight.t
        cs = self.spells.get("Counterspell")
        if m.caster and m.casting(t) and cs is not None and p.ready("Counterspell", t) and p.mana >= self.mana_cost(cs) and m.dist <= cs.range:
            return cs
        if fight.others():
            return self.decide_aoe(fight)
        if self.is_arcane():
            return self.decide_arcane(fight)
        if self.is_frostfire():
            return self.decide_frostfire(fight)
        return self.decide_fire(fight) if self.is_fire() else self.decide_frost(fight)

    def decide_aoe(self, fight):
        """A pull of several mobs: Frost Nova once they are in melee, walk out of the root, Blizzard while they are held or
        walking back, Cone of Cold and Arcane Explosion when at least two are in reach, single-target Frost when one is left."""
        p, m, t, in_melee, rooted, frozen, avg, can = self._common(fight)
        sp = self.spells
        nova, coc, ae, bliz, blast, fb = (sp.get(n) for n in ("Frost Nova", "Cone of Cold", "Arcane Explosion", "Blizzard", "Blast Wave", "Frostbolt"))
        alive = fight.alive()
        near = [x for x in alive if x.dist <= 10.5]
        melee = [x for x in alive if x.in_melee]
        loose = [x for x in melee if not x.rooted(t)]           # in melee and free to swing
        controlled = all(x.rooted(t) or x.slow_until > t or x.dist > 8.0 for x in alive)
        # 1. the pack is on me: Frost Nova, then walk out of the root
        if nova and can(nova) and len(melee) >= 2 and loose:
            return nova
        if melee and not loose and min(x.root_until for x in melee) - t >= 1.5 and fight.retreated_for != m.root_until:
            fight.retreated_for = m.root_until
            return "retreat"
        # 2. Blizzard while they are held, slowed or still walking back; Cone of Cold when they reach me and Nova is down
        if bliz and can(bliz) and len(alive) >= 3 and not loose and controlled and all(x.dist <= bliz.range for x in alive) and p.mana > self.mana_cost(bliz) * 1.3:
            return bliz
        if coc and can(coc) and len(near) >= 2 and loose:
            return coc
        if blast and can(blast) and len(near) >= 2:
            return blast
        # 3. loose mobs on me, no control up: Arcane Explosion them down if there are still several, else single target
        if ae and can(ae) and len(near) >= 2 and p.mana > self.mana_cost(ae) * 2:
            return ae
        if not melee and not near and fb and can(fb):   # the pull: bolt the first one while they walk in
            return fb
        if self.is_arcane():
            return self.decide_arcane(fight)
        if self.is_frostfire():
            return self.decide_frostfire(fight)
        return self.decide_fire(fight) if self.is_fire() else self.decide_frost(fight)

    def interrupt_bonus(self, fight, spell):
        return self.tv("Improved Counterspell", 0) if spell.name == "Counterspell" else 0.0

    def _common(self, fight):
        p, m, t = fight.p, fight.m, fight.t
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5
        rooted = m.rooted(t)
        frozen = rooted or bool(p.buff("Fingers of Frost", t))

        def avg(s):
            return (s.dmg_min + s.dmg_max) / 2 + s.coef * p.spell_power if s else 0.0

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        return p, m, t, in_melee, rooted, frozen, avg, can

    def decide_frost(self, fight):
        p, m, t, in_melee, rooted, frozen, avg, can = self._common(fight)
        sp = self.spells
        fb, blast, nova, coc, lance, snap = (sp.get(n) for n in ("Frostbolt", "Fire Blast", "Frost Nova", "Cone of Cold", "Ice Lance", "Cold Snap"))
        if fb is None:
            return "wand"
        hp = m.hp
        fb_cast = self.cast_time(fb)
        wand_hit = self.wand_damage() * 0.65
        if blast and can(blast) and hp <= avg(blast) * 0.9:
            return blast
        if lance and can(lance) and hp <= avg(lance) * (self.lance_frozen_mult() if frozen else 1) * 0.9:
            return lance
        if hp <= wand_hit * 1.5:
            return "wand"
        if in_melee and not rooted:
            if nova and can(nova) and hp > 0.12 * m.hp_max:
                return nova
            if snap and can(snap) and nova and not p.ready("Frost Nova", t) and p.cooldowns.get("Frost Nova", 0) - t > 8 and hp > 0.4 * m.hp_max:
                p.cooldowns["Frost Nova"] = t
                p.cooldowns["Cone of Cold"] = t
                p.cooldowns["Ice Barrier"] = t
                p.cooldowns["Cold Snap"] = t + snap.cooldown
                fight.note("Cold Snap")
                return nova if can(nova) else None
            if coc and can(coc) and hp > avg(coc):
                return coc
        if in_melee and rooted and m.root_until - t >= 1.0 and fight.retreated_for != m.root_until:
            fight.retreated_for = m.root_until
            return "retreat"
        if frozen:
            if lance and can(lance):
                return lance
            if can(fb):
                return fb
        if p.buff("Presence of Mind", t) and can(fb):
            return fb
        if not in_melee and not rooted:
            time_to_melee = (m.dist - MELEE_RANGE) / max(0.1, m.speed(t))
            if time_to_melee < fb_cast:
                if blast and can(blast):
                    return blast
                if nova and can(nova):
                    return "wand"
        if in_melee and blast and can(blast):
            return blast
        if can(fb):
            return fb
        if blast and can(blast):
            return blast
        return "wand"

    def missiles(self, fight):
        """Arcane Missiles to cast now: on a Missile Barrage proc a free copy that fires every 0.5 s (half the channel)."""
        am = self.spells.get("Arcane Missiles")
        if am is None or am.kind != "channel":
            return None
        if self.rank("Missile Barrage") and fight.p.buff("Missile Barrage", fight.t):
            fast = copy.copy(am)
            # client 70425 rank text numbers: [20/40 Arcane Blast, 5/10 per missile, 10/20 others, 50 duration, 100 cost, 0.5 s]
            # (70291's [40, 20, 50, 100, 0.5] had the cut at index 2 and the cost at 3: until 2026-10-17 a proc read the 70291 indices,
            # cutting the channel 20% and the cost 50%, so decide_arcane, which knows a proc by its zero cost, never saw one)
            fast.channel = am.channel * (1 - self.tv("Missile Barrage", 3) / 100)
            fast.cost = am.cost * (1 - self.tv("Missile Barrage", 4) / 100)
            return fast
        return am

    def decide_arcane(self, fight):
        """Arcane leveling (spec strings starting with "arcane", 2026-09-30). Arcane Power and Presence of Mind are used on the pull
        (on_fight_start); Arcane Blast (instant with Presence of Mind) is stacked up to AB_MAX_STACKS while the mob is out of reach or
        held and the next one costs at most AB_MANA_SHARE of the mana (each stack 15% of Intellect as spell damage for every spell, 15 s
        from the first: client 70425); Arcane Wrath on cooldown when talented and its cast can finish; Arcane Missiles is the channel
        filler, first on a Missile Barrage proc (free, 2.5 s). Frost Nova / Cone of Cold and a 2-second step back when the mob
        reaches you, Ice Lance into a freeze if talented, Fire Blast, Ice Lance and the wand to finish without overkill. Frostbolt
        only when Arcane Missiles is unaffordable (or before level 8)."""
        p, m, t, in_melee, rooted, frozen, avg, can = self._common(fight)
        sp = self.spells
        fb, blast, nova, coc, lance = (sp.get(n) for n in ("Frostbolt", "Fire Blast", "Frost Nova", "Cone of Cold", "Ice Lance"))
        ab, am = self.arcane_blast(), self.missiles(fight)
        if fb is None and am is None:
            return "wand"
        hp = m.hp
        wand_hit = self.wand_damage() * 0.65
        stacks = self.ab_stacks(fight)

        def am_total(s):   # a whole Arcane Missiles channel with the current stacks and buffs
            return (s.dot + s.dot_coef * p.spell_power * s.dot_ticks) * self.periodic_multiplier(s) if s else 0.0

        # 1. finishers without overkill
        if blast and can(blast) and hp <= avg(blast) * self.damage_multiplier(blast, False) * 0.9:
            return blast
        if lance and can(lance) and hp <= avg(lance) * (self.lance_frozen_mult() if frozen else 1) * 0.9:
            return lance
        if hp <= wand_hit * 1.5:
            return "wand"
        # 2. the mob is on me: freeze it and step back
        if in_melee and not rooted:
            if nova and can(nova) and hp > 0.12 * m.hp_max:
                return nova
            if coc and can(coc) and hp > avg(coc):
                return coc
        if in_melee and rooted and m.root_until - t >= 1.0 and fight.retreated_for != m.root_until:
            fight.retreated_for = m.root_until
            return "retreat"
        if frozen and lance and can(lance):
            return lance
        aw = sp.get("Arcane Wrath")

        def aw_fits():   # Arcane Wrath (client 70425) only while its cast can finish before the mob is on me
            if aw is None or not can(aw) or hp <= avg(aw) * self.damage_multiplier(aw, False) * 0.5:
                return False
            c = self.cast_time(aw)
            return c <= 0 or (rooted and m.root_until - t >= c) \
                or (not in_melee and not rooted and (m.dist - MELEE_RANGE) / max(0.1, m.speed(t)) >= c)

        if self.AW_OPENER and stacks == 0 and aw_fits():   # the pull's first cast (AW_OPENER)
            return aw
        # 3. a Missile Barrage proc: free fast missiles (after the stacks the pull allows)
        barrage = am is not None and am.cost == 0 and am is not sp.get("Arcane Missiles")
        if barrage and can(am) and (stacks >= self.AB_MAX_STACKS or ab is None or in_melee):
            return am
        # 4. Arcane Blast stacks: instant with Presence of Mind; otherwise only while the cast can finish before the mob is on me
        if ab is not None and can(ab) and stacks < self.AB_MAX_STACKS and self.mana_cost(ab) <= self.AB_MANA_SHARE * p.mana \
                and hp > avg(ab) + am_total(am) * 0.5:
            ab_cast = self.cast_time(ab)
            if ab_cast <= 0:
                return ab
            if rooted and m.root_until - t >= ab_cast:
                return ab
            if not in_melee and not rooted and (m.dist - MELEE_RANGE) / max(0.1, m.speed(t)) >= ab_cast:
                return ab
        # 4b. Arcane Wrath on cooldown after the stacks, while its cast fits
        if aw_fits():
            return aw
        # 5. Arcane Missiles: the channel (Improved Channeling keeps it whole in melee)
        if am is not None and can(am):
            return am
        if blast and can(blast) and in_melee:
            return blast
        if fb and can(fb):
            return fb
        if blast and can(blast):
            return blast
        return "wand"

    def decide_frostfire(self, fight):
        """Frostfire Bolt (from level 40; Frostbolt before) as the bolt: it chills like Frostbolt and counts as Frost and Fire, so both
        trees' talents apply. Finish with Fire Blast, Ice Lance or the wand; Pyroblast on a full Heating Up; Frost Nova, Cone of Cold and
        a step back when the mob reaches you; Ice Lance on a frozen mob."""
        p, m, t, in_melee, rooted, frozen, avg, can = self._common(fight)
        sp = self.spells
        ffb, fb, blast, nova, coc, lance, pyro = (sp.get(n) for n in ("Frostfire Bolt", "Frostbolt", "Fire Blast", "Frost Nova", "Cone of Cold", "Ice Lance", "Pyroblast"))
        bolt = ffb or fb
        if bolt is None:
            return "wand"
        hp = m.hp
        bolt_cast = self.cast_time(bolt)
        wand_hit = self.wand_damage() * 0.65
        if blast and can(blast) and hp <= avg(blast) * 0.9:
            return blast
        if lance and can(lance) and hp <= avg(lance) * (self.lance_frozen_mult() if frozen else 1) * 0.9:
            return lance
        if hp <= wand_hit * 1.5:
            return "wand"
        hs = p.buff("Heating Up", t)
        if pyro and hs and hs["stacks"] >= 3 and can(pyro) and hp > avg(bolt) * 1.2:
            return pyro
        if in_melee and not rooted:
            if nova and can(nova) and hp > 0.12 * m.hp_max:
                return nova
            if coc and can(coc) and hp > avg(coc):
                return coc
        if in_melee and rooted and m.root_until - t >= 1.0 and fight.retreated_for != m.root_until:
            fight.retreated_for = m.root_until
            return "retreat"
        if frozen and lance and can(lance):
            return lance
        if p.buff("Presence of Mind", t) and can(bolt):
            return bolt
        if not in_melee and not rooted:
            time_to_melee = (m.dist - MELEE_RANGE) / max(0.1, m.speed(t))
            if time_to_melee < bolt_cast:
                if blast and can(blast):
                    return blast
                if nova and can(nova):
                    return "wand"
        if in_melee and blast and can(blast):
            return blast
        if can(bolt):
            return bolt
        if blast and can(blast):
            return blast
        return "wand"

    def decide_fire(self, fight):
        p, m, t, in_melee, rooted, frozen, avg, can = self._common(fight)
        sp = self.spells
        fireball, blast, scorch, nova, lance, pyro, wave = (sp.get(n) for n in ("Fireball", "Fire Blast", "Scorch", "Frost Nova", "Ice Lance", "Pyroblast", "Blast Wave"))
        if fireball is None:
            return "wand"
        hp = m.hp
        fb_cast = self.cast_time(fireball)
        wand_hit = self.wand_damage() * 0.65
        # finishers without overkill
        if blast and can(blast) and hp <= avg(blast) * 0.9:
            return blast
        if lance and can(lance) and hp <= avg(lance) * (self.lance_frozen_mult() if frozen else 1) * 0.9:
            return lance
        if scorch and can(scorch) and hp <= avg(scorch) * 0.9 and hp > wand_hit * 1.5:
            return scorch
        if hp <= wand_hit * 1.5:
            return "wand"
        # a full Heating Up: a 1.5s Pyroblast beats everything
        hs = p.buff("Heating Up", t)
        if pyro and hs and hs["stacks"] >= 3 and can(pyro) and hp > avg(scorch) * 1.5 if scorch else False:
            return pyro
        # control when the mob is on us
        if in_melee and not rooted and not m.stunned(t):
            if nova and can(nova) and hp > 0.12 * m.hp_max:
                return nova
            if wave and can(wave) and hp > avg(wave):
                return wave
            if blast and can(blast):
                return blast
        if in_melee and rooted and m.root_until - t >= 1.0 and fight.retreated_for != m.root_until:
            fight.retreated_for = m.root_until
            return "retreat"
        if frozen and lance and can(lance):
            return lance
        if p.buff("Presence of Mind", t) and can(fireball):
            return fireball
        if not in_melee and not rooted and not m.stunned(t):
            time_to_melee = (m.dist - MELEE_RANGE) / max(0.1, m.speed(t))
            if time_to_melee < fb_cast:
                if blast and can(blast):
                    return blast
                if scorch and can(scorch) and time_to_melee >= 1.5:
                    return scorch
                if nova and can(nova):
                    return "wand"
        if in_melee:
            # the mob is on us and every control is down: Scorch (1.5s) suffers less pushback than a Fireball
            if scorch and can(scorch):
                return scorch
        if can(fireball):
            return fireball
        if scorch and can(scorch):
            return scorch
        if blast and can(blast):
            return blast
        return "wand"
