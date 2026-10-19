"""Paladin module for the fight lab (two-handed Retribution leveling).

Spell ranks are read from `_reference/data/forever-spells/paladin.json` (beta client build 1.60.1.70009); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/paladin.json`. Weapon damage uses a quest-green two-hander by level,
attack power from the client's base stats (2 AP per Strength), Blessing of Might and Devotion Aura from the spellbook.

Playstyle `ret-dps` (the scorer's model id, used for leveling): Blessing of Might and Devotion Aura up, a Seal before each pull
(Seal of Command once talented, Seal of Righteousness before that), Judgement and Holy Strike on cooldown, Consecration while
mana allows, Hammer of Justice into a doubled Seal of Command judgement or as a breather, Hammer of Wrath under 20%; Divine
Protection then Holy Light when low, Lay on Hands in an emergency. Between fights: Holy Light / Flash of Light back to health,
water below 35% mana.

Playstyles `holy...` and `prot...` (e.g. `holy-leveling`, `holy-shield-leveling`, `prot-leveling`; the `_alt` methods, added
2026-09-30): paladins who level as Holy (two-hander, Seal of Righteousness, offensive Holy Shock, Divine Favor, heals with crit /
Illumination / Infusion of Light) or Protection (one-hander and shield with block, Seal of Fury and its absorb, Holy Shield,
Redoubt, Shield Specialization, Reckoning, Swift Judgement, Templar's Bulwark, Improved Righteous Fury / Iron Creed with Righteous
Fury assumed up). Every other spec string plays the Retribution path unchanged.
"""
import copy
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell, Weapon
from tables import (GCD, MELEE_MISS, MELEE_RANGE, WEAPON_SPEED, class_attack_power, class_base_health, class_base_mana, class_base_stats, class_dodge,
                    class_health_regen_tick, class_mana_regen_tick, class_melee_crit, class_spell_crit, gear_stats, weapon_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/paladin.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/paladin.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
COST = re.compile(r"(\d[\d,]*(?:\.\d+)?)")   # "1,340 Mana": NUM stopped at the comma and read Light's Vigil rank 3 as 1 mana (audit 2026-10-18 #30)
DMG = re.compile(r"(\d[\d,]*) to (\d[\d,]*) (?:as )?Holy damage")
HEAL = re.compile(r"[Hh]eals a friendly target for (\d[\d,]*) to (\d[\d,]*)")
WEAPON_PCT = re.compile(r"(\d+)% weapon damage")
SEAL_R = re.compile(r"additional (\d[\d,]*) to (\d[\d,]*) Holy damage")
SEAL_C = re.compile(r"Holy damage equal to (\d+)% of normal weapon damage")
JUDGE = re.compile(r"Unleashing this Seal's energy will (?:cause|judge an enemy, instantly causing) (\d[\d,]*) to (\d[\d,]*) Holy damage(?:, (\d[\d,]*) to (\d[\d,]*) if the target is stunned)?")
# 70425 splits the tooltip into two sentences ("... enter the area. The first 4 enemies who enter the area will take an additional N damage
# over 8 sec."): until 2026-10-17 the pattern stopped at the period and Consecration parsed to no damage at all
CONSEC = re.compile(r"doing (\d[\d,]*) Holy damage over (\d+) sec.*?additional (\d[\d,]*) damage over (\d+) sec")
CONSEC_TICK = 1.0   # the client ticks every second (each rank's periodic dummy: PeriodMs 1000 over DurationMs 8000; the lab had 4 ticks)
STUN = re.compile(r"Stuns the target for (\d+) sec")
AP = re.compile(r"increasing melee attack power by (\d+)|granting (\d+) melee attack power")
ARMOR = re.compile(r"Gives (\d[\d,]*) additional armor")
SEAL_LIGHT = re.compile(r"chance to heal the Paladin for (\d+)")
SEAL_WIS = re.compile(r"chance to restore (\d+) of the Paladin's mana")
COEF = re.compile(r"([\d.]+)% of spell power \((\w+(?: \w+)?)\)")

# Seal of Righteousness per melee hit, from the client's rows (the second effect of Judgement of Righteousness rank n, which the seal's
# tooltip renders each hit from; the ElliotWood/Forever simulator at origin/master reads the same rows: sim/paladin/seal_of_righteousness.go):
# rank: (base points, per level, spell level, max level, spell power coefficient). A hit deals value(level) / 100 x 1.2 (two-hander) or 0.85
# (one-hander) x swing speed; the coefficient is x1.2 with a two-hander (the fork's reading of the beta's public combat logs; a one-hander
# keeps the bare one). Each rank's tooltip range is the same value at the rank's top level for a 1.4 s one-hander and a 3.4 s two-hander
# (rank 8: 18.8 x 1.2 x 3.4 = 76.7 against the tooltip's 75), so the lab's earlier uniform roll over the tooltip range read a two-hander
# about a third low, and its earlier coefficient was the judgement's 42.9% (until 2026-10-17).
SOR_PER_HIT = {1: (108, 18, 1, 7, 0.058), 2: (216, 17, 10, 16, 0.125), 3: (352, 23, 18, 24, 0.185), 4: (541, 31, 26, 32, 0.20),
               5: (785, 37, 34, 40, 0.20), 6: (1082, 41, 42, 48, 0.20), 7: (1407, 47, 50, 56, 0.20), 8: (1786, 47, 58, 64, 0.20)}


def sor_hit(seal, level, speed, two_hand):
    """(base damage, spell power coefficient) of one Seal of Righteousness hit at `level` with a weapon of `speed`."""
    bp, ppl, lo, hi, coef = SOR_PER_HIT.get(seal.rank, SOR_PER_HIT[8])
    value = int(bp + ppl * max(0, min(level, hi) - lo))
    return value / 100 * (1.2 if two_hand else 0.85) * speed, coef * (1.2 if two_hand else 1.0)


TALENT_SPELLS = {"Seal of Command": "Seal of Command", "Repentance": "Repentance", "Holy Shock": "Holy Shock", "Light's Vigil": "Light's Vigil",
                 "Divine Favor": "Divine Favor", "Voice of Truth": "Voice of Truth", "Swift Judgement": "Swift Judgement", "Templar's Bulwark": "Templar's Bulwark",
                 "Holy Shield": "Holy Shield"}
SEALS = ("Seal of Command", "Seal of Righteousness", "Seal of the Crusader", "Seal of Light", "Seal of Wisdom", "Seal of Justice", "Seal of Fury")


def _num(s):
    return float(s.replace(",", ""))


def _seconds(s):
    m = re.search(r"([\d.]+)\s*(sec|min)", s or "")
    if not m:
        return 0.0
    return float(m.group(1)) * (60 if m.group(2) == "min" else 1)


def load_spellbook():
    book = {}
    for tab in SPELLBOOK["tabs"]:
        for sp in tab["spells"]:
            for r in sp["ranks"]:
                txt = (r.get("text") or "").replace("\n", " ")
                cost_txt = r.get("cost") or ""
                cost = _num(COST.search(cost_txt).group(1)) if COST.search(cost_txt) else 0.0
                cast_txt = (r.get("cast") or "").lower()
                cast = 0.0 if "instant" in cast_txt or not cast_txt else _seconds(cast_txt)
                coefs = {k: float(v) / 100 for v, k in COEF.findall(r.get("coefficient") or "")}
                rm = re.search(r"(\d+) yd range", r.get("range") or "")
                name = sp["name"]
                s = Spell(name=name, school=(r.get("school") or "holy").lower(), rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")),
                          range=_num(rm.group(1)) if rm else 5.0, coef=coefs.get("direct", 0.0), tags=("cost_pct",) if "base mana" in cost_txt else ())
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                dm, he, wp, sr, sc, jd, cs, st, ap, ar, sl, sw = (rx.search(txt) for rx in (DMG, HEAL, WEAPON_PCT, SEAL_R, SEAL_C, JUDGE, CONSEC, STUN, AP, ARMOR, SEAL_LIGHT, SEAL_WIS))
                if name in SEALS:
                    s.kind = "buff"
                    if sr:
                        s.seal_min, s.seal_max = _num(sr.group(1)), _num(sr.group(2))
                    if sc:
                        s.seal_pct = float(sc.group(1)) / 100
                    if jd:
                        s.judge = (_num(jd.group(1)), _num(jd.group(2)))
                        s.judge_stunned = (_num(jd.group(3)), _num(jd.group(4))) if jd.group(3) else None
                    if sl:
                        s.seal_heal = float(sl.group(1))
                    if sw:
                        s.seal_mana = float(sw.group(1))
                    if ap:
                        s.ap = float(ap.group(1) or ap.group(2))
                elif name == "Holy Strike":
                    s.kind = "melee"
                    s.weapon_pct = float(wp.group(1)) / 100 if wp else 0.5
                    if dm:
                        s.dmg_min, s.dmg_max = _num(dm.group(1)), _num(dm.group(2))
                    s.school = "holy"
                elif name == "Consecration":
                    s.kind = "spell"
                    if cs:
                        s.dot, s.dot_dur = _num(cs.group(1)) + _num(cs.group(3)), float(cs.group(2))
                        s.dot_ticks = max(1, int(round(s.dot_dur / CONSEC_TICK)))
                        s.dot_coef = coefs.get("per tick", 0.0)
                    s.aoe = True
                elif he and not dm:
                    s.kind = "heal"
                    s.heal_min, s.heal_max, s.heal_coef = _num(he.group(1)), _num(he.group(2)), coefs.get("heal", 0.0)
                elif dm:
                    s.dmg_min, s.dmg_max = _num(dm.group(1)), _num(dm.group(2))
                if st:
                    s.stun = float(st.group(1))
                    s.kind = "spell"
                if ap and name.startswith("Blessing"):
                    s.kind, s.ap = "buff", float(ap.group(1) or ap.group(2))
                if ar:
                    s.kind, s.armor = "buff", _num(ar.group(1))
                if name in ("Judgement", "Divine Protection", "Divine Shield", "Lay on Hands", "Blessing of Kings", "Retribution Aura", "Sanctity Aura",
                            "Righteous Fury", "Swift Judgement", "Templar's Bulwark", "Divine Favor", "Voice of Truth", "Blessing of Wisdom", "Concentration Aura"):
                    s.kind = "buff"
                if name == "Lay on Hands":
                    s.kind, s.resource = "heal", "none"
                book.setdefault(name, []).append(s)
    for name in book:
        book[name].sort(key=lambda x: (x.level, x.rank))
    return book


BOOK = load_spellbook()

# 70425 words rank 2's hit "inflict" and every judgement "inflicts" (audit 2026-10-18 #27: until then rank 2 did nothing and no rank's
# judgement had base damage)
FURY_HIT = re.compile(r"(?:deal|inflict) an additional (\d[\d,]*) Holy damage")
FURY_JUDGE = re.compile(r"Seal's energy (?:causes|inflicts) (\d[\d,]*) to (\d[\d,]*) Holy damage")
FURY_COEF = re.compile(r"(\d+(?:\.\d+)?)% and (\d+(?:\.\d+)?)% of spell power")
HSHIELD = re.compile(r"deals (\d[\d,]*) Holy damage for each attack blocked")
SHOCK_HEAL = re.compile(r"or (\d[\d,]*) to (\d[\d,]*) healing")


def _add_extras():
    """Numbers only the Holy and Protection leveling paths read (new attributes, so the Retribution path never sees them):
    Seal of Fury's per-hit damage, judgement and coefficients (the parser's seal regexes do not match its wording), Holy Shield's
    damage per block, Holy Shock's healing half."""
    for tab in SPELLBOOK["tabs"]:
        for sp in tab["spells"]:
            for r in sp["ranks"]:
                txt = (r.get("text") or "").replace("\n", " ")
                lvl = int(r.get("level") or 1)
                match = [s for s in BOOK.get(sp["name"], []) if s.level == lvl and (s.text or "") == txt]
                if not match:
                    continue
                s = match[0]
                if sp["name"] == "Seal of Fury":
                    fh, fj, fc = FURY_HIT.search(txt), FURY_JUDGE.search(txt), FURY_COEF.search(r.get("coefficient") or "")
                    s.fury_hit = _num(fh.group(1)) if fh else 0.0
                    s.fury_judge = (_num(fj.group(1)), _num(fj.group(2))) if fj else (0.0, 0.0)
                    # "45% and 10% of spell power (direct)": 45% read as the judgement's, 10% as each melee hit's (assumption)
                    s.fury_coefs = (float(fc.group(1)) / 100, float(fc.group(2)) / 100) if fc else (0.0, 0.0)
                elif sp["name"] == "Holy Shield":
                    hm = HSHIELD.search(txt)
                    s.hs_dmg = _num(hm.group(1)) if hm else 0.0
                    bm = re.search(r"chance to block by (\d+)%", txt)   # 70291: 30% (the module had 20% written in until 2026-10-09)
                    s.hs_block = float(bm.group(1)) / 100 if bm else 0.30
                elif sp["name"] == "Holy Shock":
                    hm = SHOCK_HEAL.search(txt)
                    s.shock_heal = (_num(hm.group(1)), _num(hm.group(2))) if hm else (0.0, 0.0)
                    s.shock_heal_coef = {k: float(v) / 100 for v, k in COEF.findall(r.get("coefficient") or "")}.get("heal", 0.0)


_add_extras()
# the engine rolls shield block itself when it has the block hooks (Player.block > 0); otherwise split_damage_taken rolls it here
ENGINE_BLOCK = "on_block" in BaseModule.__dict__ and "block_bonus" in BaseModule.__dict__


def talent_numbers():
    out = {}
    for tr in TREE["trees"]:
        for t in tr["talents"]:
            out[t["name"]] = [[float(x) for x in NUM.findall((rank or "").replace(",", ""))] for rank in t["ranks"]]
    return out


TNUM = talent_numbers()

MECHANICS = {
    "Divine Strength": "+2%/rank Strength",
    "Divine Intellect": "+2%/rank Intellect",
    "Healing Light": "+4%/rank Holy Light / Flash of Light",
    "Spiritual Focus": "35%/rank chance to ignore pushback on heals",
    "Improved Seals": "+5%/rank seal and judgement damage (seal procs and judgements roll on the melee table: miss, crit x2.0)",
    "Unyielding Faith": "PvP",
    "Voice of Truth": "casters only",
    "Reverence": "10%/rank mana regen while casting",
    "Purifying Power": "Exorcism / Holy Wrath (Undead and Demons): not used",
    "Infusion of Light": "healers",
    "Illumination": "20%/rank: crit heals refund 50% of base mana",
    "Divine Favor": "not used",
    "Divine Precision": "+6%/rank hit with Consecration, Exorcism, Holy Shock, Holy Strike, Holy Wrath (the client's class mask; not judgements)",
    "Holy Shock": "not used (Retribution)",
    "Consecrated Ground": "+5%/rank to every Holy spell against a mob standing in your Consecration (Consecration's own ticks after the first)",
    "Holy Power": "+3%/rank Holy Strike crit, +1%/rank spell crit",
    "Toughness": "+2%/rank armor",
    "Redoubt": "no shield",
    "Precision": "+1%/rank hit",
    "Guardian's Favor": "not used",
    "Anticipation": "+20 Defense: ~-1.6% chance to be hit (assumed)",
    "Improved Seal of Fury": "no shield",
    "Improved Righteous Fury": "not used",
    "Shield Specialization": "no shield",
    "Sacred Duty": "+2%/rank Stamina, -30 s/rank Divine Protection / Shield cooldown",
    "Swift Judgement": "not used",
    "One-Handed Weapon Specialization": "two-hander build",
    "Improved Hammer of Justice": "-5 s/rank Hammer of Justice cooldown",
    "Templar's Bulwark": "not used",
    "Reckoning": "20%/rank chance after a crit taken to store an extra attack (up to 4, one per 1.5 s); the next auto attack releases them all (client 70425)",
    "Iron Creed": "threat only",
    "Holy Shield": "no shield",
    "Deflection": "+1%/rank parry",
    "Benediction": "-2%/rank mana on instants",
    "Improved Judgement": "-1 s/rank Judgement cooldown",
    "Holy Conduit": "-20%/rank Consecration / Hammer of Wrath mana",
    "Conviction": "+1%/rank melee crit (white, Holy Strike, seal procs and judgements: all on the melee table)",
    "Vindication": "every landed melee attack: +1%/rank attack power for 30 s (client and fork: 100% chance; the mob's attack power loss is not modelled)",
    "Sanctified Judgement": "33%/rank chance per Judgement to refund 20%/rank of the seal's mana",
    "Seal of Command": "unlocks Seal of Command (7 procs per minute: 70% of weapon damage + 0.29 x spell power as Holy, hit and crit on the melee table; judgement 169..187, doubled on a stunned mob)",
    "Pursuit of Justice": "travel speed only",
    "Eye for an Eye": "10%/rank of crits taken dealt back",
    "Sacred Arbiter": "+20% Holy Strike",
    "Two-Handed Weapon Specialization": "+2%/rank Physical damage with a two-hander (white swings, Reckoning; not Holy Strike, seals or judgements)",
    "Vengeance": "+1%/rank Physical and Holy damage per stack after any non-periodic crit (melee, seal, judgement, spell; 3 stacks, 30 s)",
    "Repentance": "Humanoids only: not used",
    "Champion of the Light": "+10%/rank of Intellect as spell damage (seals, judgements, Consecration, Holy Shock); not healing (notes, 1 Oct)",
    "Instrument of Law": "-0.5 s/rank Hammer of Wrath cast",
    "Twist of Light": "-20% seal mana",
}
FIT = {
    "Divine Strength": "scale", "Divine Intellect": "scale", "Improved Seals": "scale", "Reverence": "scale", "Illumination": "scale", "Holy Power": "scale",
    "Healing Light": "scale", "Divine Precision": "scale", "Consecrated Ground": "scale", "Toughness": "scale", "Precision": "scale", "Anticipation": "scale",
    "Sacred Duty": "scale", "Improved Hammer of Justice": "scale", "Reckoning": "scale", "Deflection": "scale", "Benediction": "scale", "Improved Judgement": "scale",
    "Holy Conduit": "scale", "Conviction": "scale", "Vindication": "scale", "Sanctified Judgement": "scale",
    "Seal of Command": ("replace", [{"channel": "dmg", "scope": ["type:melee"], "values": [0.15]}]),
    "Eye for an Eye": "scale", "Sacred Arbiter": "scale", "Two-Handed Weapon Specialization": "scale", "Vengeance": "scale", "Champion of the Light": "scale",
    "Instrument of Law": "scale", "Twist of Light": "scale", "Spiritual Focus": "scale", "Repentance": "scale", "Voice of Truth": "scale",
}
SHARE_SOURCE = {"Melee": "white", "Seal of Command": "seal", "Seal of Righteousness": "seal", "Judgement": "judgement", "Consecration": "consecration",
                "Holy Strike": "holy_strike", "Hammer of Wrath": "hammer_of_wrath", "Retribution Aura": "ret_aura"}
NEW_SOURCES = {"hammer_of_wrath": {"id": "hammer_of_wrath", "share": 0.0, "min_level": 44, "tags": ["type:spell", "school:holy", "ability:Hammer of Wrath", "weapon:2h"], "cooldown": 6}}
KEY_TALENTS = ["Seal of Command", "Conviction", "Improved Seals"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with a two-hander: Blessing of Might and Devotion Aura up, a Seal recast before each "
               "pull (Seal of Command once talented, Seal of Righteousness before), the mob walks in (paladins have no charge), Judgement and Holy Strike on cooldown, "
               "Consecration while mana allows, Hammer of Justice into a doubled Seal of Command judgement or when hurt, Hammer of Wrath under 20%; Divine "
               "Protection and a Holy Light when low, Lay on Hands in an emergency. Between fights: 2 s loot, 6 s travel, Holy Light or Flash of Light back to "
               "80% health, water below 35% mana; a death costs 90 s.")
NOT_MODELLED = "runners, adds, Exorcism / Holy Wrath (Undead and Demons), Repentance, Retribution Aura (Devotion Aura is assumed up), Seal of Wisdom / Seal of Light twisting, Blessing of Kings, shields, gear upgrades within a level bracket."
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'ret-dps', 'opt': 'opt-ret-dps-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=3'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'AoE grinding, 3 mobs per pull'}], "spec": "ret-dps", "hand": "leveling-retribution", "opt": "opt-ret-dps-leveling-st", "tag": "ret", "lookahead": 16,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60"}

# ---------------------------------------------------------------- Holy and Protection leveling (spec strings "holy..." / "prot...")
# Shield armor by level: gear_stats.pick(pool, "paladin", L, "shield", "other") over the Classic 1.12 greens (item_stats.csv,
# 2026-09-30; examples Redbeard Crest at 20, Savage Boar's Guard at 40, Dreadguard's Protector at 60). The paladin's gear table
# assumes a two-hander, so a shield user keeps those armor-slot stats and adds the shield's armor and stamina (the two-hander's
# own stats are not taken back: small, an assumption).
SHIELD_ARMOR = [(10, 275.0), (20, 461.0), (30, 611.0), (40, 1257.0), (50, 1663.0), (60, 2113.5)]
SHIELD_STAMINA = [(10, 0.5), (20, 3.0), (30, 3.0), (40, 7.0), (50, 6.0), (60, 8.0)]
SHIELD_BLOCK_PER_LEVEL = 0.5   # shield block value ~ half the level (a level-60 green ~30; the item extract has no block column: assumption)
BASE_BLOCK = 0.05              # player base block chance with a shield (Classic rule)
DEFENSE_PER_POINT = 0.0004     # +0.04% dodge, parry and block per Defense point (Classic rule; Anticipation)
HOLY_SHIELD_CHARGES = 4        # rank 1 tooltip says 4 charges; ranks 2-3 do not repeat it (assumed unchanged)
SOF_SHIELD_TIME = 10.0         # Seal of Fury's absorb: duration not in the tooltip (assumed 10 s, refreshed, not stacked)
# Seal of Command's proc: (weapon damage + 0.29 x spell power) x the weapon percent (the client's coefficient on the weapon-percent effect of
# 20424, as the ElliotWood/Forever simulator reads it: sim/paladin/seal_of_command.go); the lab had no spell power on it until 2026-10-18
SOC_PROC_COEF = 0.29
# Reckoning: one 1.5 s proc cooldown shared by the block and the crit trigger (the client's ICD on 20177, the fork's reading; the tooltip
# names it for blocks only)
RECKONING_ICD = 1.5
# Consecrated Ground: Consecration marks the mobs each tick hits and every Holy spell does more to a marked mob; Consecration's own first
# tick lands before the mark, so its ticks get 7 of 8 (audit 2026-10-18 #16: the lab boosted Consecration alone)
CONSEC_MARKED_TICKS = 7.0 / 8.0
DIVINE_PRECISION_SPELLS = ("Consecration", "Exorcism", "Holy Shock", "Holy Strike", "Holy Wrath", "Light's Vigil")
MECHANICS_ALT = dict(MECHANICS, **{
    "Holy Shock": "offensive Holy Shock (Forever tooltip: damage to an enemy or healing to an ally; 10 s cooldown), a heal when low",
    "Holy Power": "+3%/rank Holy Shock and Holy Strike crit, +1%/rank other spells",
    "Divine Favor": "off the global cooldown before the next Holy Shock or heal: 100% crit",
    "Illumination": "20%/rank on a heal crit: 50% of the spell's base cost back (in-combat heals rolled, between fights the expected value)",
    "Infusion of Light": "Holy Shock / Flash of Light crit: -0.5 s/rank on the next Holy Light",
    "Spiritual Focus": "35%/rank chance to ignore pushback on Holy Light / Flash of Light",
    "Light's Vigil": "not used (1,340 mana at 60 for one free Holy Shock and 75% back: net mana loss for a solo leveler)",
    "Toughness": "+2%/rank armor from items (shield included)",
    "Redoubt": "2%/rank of melee hits taken: +4%/rank block for 10 s or 5 blocks",
    "Anticipation": "+4 Defense/rank: +0.04% dodge, parry and block per point (mob hit and crit chance unchanged)",
    "Improved Seal of Fury": "60 mana when a Seal of Fury shield is fully absorbed",
    "Improved Righteous Fury": "-2%/rank damage taken (Righteous Fury assumed always up)",
    "Shield Specialization": "+10%/rank block value; blocks restore 4% max mana at 33%/rank chance, once per 3 s",
    "Swift Judgement": "off the global cooldown: resets Judgement and makes it free when it has 3+ s left",
    "One-Handed Weapon Specialization": "+3/6/10% Physical damage with a one-hander (white swings, Reckoning)",
    "Templar's Bulwark": "emergency absorb of 100% max health for 8 s (Forbearance 1 min)",
    "Reckoning": "8%/rank after a block and 20%/rank after a crit taken (one 1.5 s proc cooldown for both): an extra attack stored (up to 4), "
                 "all released on the next auto attack (client 70425, notes of 16 Oct)",
    "Iron Creed": "Holy Strike: -2%/rank damage taken for 6 s (Righteous Fury assumed up)",
    "Holy Shield": "+30% block (the 70291 tooltip) for 10 s or 4 blocks, Holy damage per block, recast when down",
    "Two-Handed Weapon Specialization": "+2%/rank Physical damage with a two-hander (white swings, Reckoning)",
})


def _interp(pts, level):
    if level <= pts[0][0]:
        return pts[0][1]
    for (l0, v0), (l1, v1) in zip(pts, pts[1:]):
        if level <= l1:
            return v0 + (v1 - v0) * (level - l0) / (l1 - l0)
    return pts[-1][1]


class PaladinModule(BaseModule):
    resource = "mana"
    melee = True

    AOE = {'direct': ['Consecration'], 'min_near': 2}

    def __init__(self, talents, level, spec="ret-dps", gear="leveling"):
        self.t = {k: v for k, v in talents.items() if v > 0}
        self.level = level
        self.spec = spec
        self.gear = gear
        self.book = {name: self.rank_at(name) for name in BOOK}
        self.spells = {n: s for n, s in self.book.items() if s is not None}
        for tname, sname in TALENT_SPELLS.items():
            if not self.t.get(tname):
                self.spells.pop(sname, None)
        self._fight = None
        self._base_mana = 0.0
        self.armor_spell_used = "Devotion Aura" if "Devotion Aura" in self.spells else "none"
        # "holy..." and "prot..." spec strings play the Holy / Protection leveling paths (the _alt methods); everything else is Retribution
        self.path = "holy" if spec.startswith("holy") else "prot" if spec.startswith("prot") else "ret"
        if self.path != "ret":
            self._init_alt(spec)

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
        if self.path != "ret":
            return sorted(n for n in self.t if n not in MECHANICS_ALT)
        return sorted(n for n in self.t if n not in MECHANICS)

    def rank_at(self, name):
        ranks = [s for s in BOOK.get(name, []) if s.level <= self.level]
        return self.scale_rank(ranks[-1]) if ranks else None   # the rank at this level (row 8)

    def seal(self):
        if self.path != "ret":
            return self._seal_alt()
        return self.spells.get("Seal of Command") or self.spells.get("Seal of Righteousness")

    # ------------------------------------------------------------ character
    def make_player(self, level):
        if self.path != "ret":
            return self._make_player_alt(level)
        base = class_base_stats("paladin", level)
        g = gear_stats(level, self.gear, "paladin")
        strength = (base["strength"] + g["strength"]) * (1 + self.tv("Divine Strength", 0) / 100)
        agility = base["agility"] + g["agility"]
        stamina = (base["stamina"] + g["stamina"]) * (1 + self.tv("Sacred Duty", 0) / 100)
        intellect = (base["intellect"] + g["intellect"]) * (1 + self.tv("Divine Intellect", 0) / 100)
        spirit = base["spirit"] + g["spirit"]
        dev = self.book.get("Devotion Aura")
        armor = g["armor"] * (1 + self.tv("Toughness", 0) / 100) + (getattr(dev, "armor", 0.0) if dev else 0.0)
        bm = class_base_mana("paladin", level)
        might = self.book.get("Blessing of Might")
        self._cotl = intellect * self.tv("Champion of the Light", 0) / 100   # spell damage only (heal_multiplier takes it back out of heals)
        p = Player(level=level, hp_max=class_base_health("paladin", level) + 10 * stamina, hp=0.0, mana_max=bm + 15 * intellect, mana=0.0, base_mana=bm,
                   spirit=spirit, intellect=intellect, spell_power=g["spell_power"] + self._cotl, armor=armor,
                   spell_crit=class_spell_crit("paladin", level, intellect) + self.tv("Holy Power", 1) / 100, dodge=class_dodge("paladin", level, agility), ranged_crit=0.0)
        self._sp_total = p.spell_power
        self._reck = 0
        self._reck_block_ready = -1.0
        p.strength, p.agility, p.stamina = strength, agility, stamina
        p.attack_power = class_attack_power("paladin", level, strength, agility) + (getattr(might, "ap", 0.0) if might else 0.0)
        self.base_ap = p.attack_power
        p.melee_crit = class_melee_crit("paladin", level, agility) + self.tv("Conviction", 0) / 100
        p.hit_bonus = self.tv("Precision", 0) / 100
        p.parry = 0.05 + self.tv("Deflection", 0) / 100
        dps = weapon_dps(level, "2h")
        p.mh = Weapon(dmg_min=dps * WEAPON_SPEED["2h"] * 0.8, dmg_max=dps * WEAPON_SPEED["2h"] * 1.2, speed=WEAPON_SPEED["2h"], kind="2h")
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Reverence", 0) / 100
        return p

    def pull_range(self):
        return 20.0

    # ------------------------------------------------------------ engine hooks: numbers
    def mana_cost(self, spell):
        if self.path != "ret" and spell.name == "Judgement" and self._free_judge:
            return 0.0
        cost = spell.cost
        if "cost_pct" in spell.tags:
            cost = cost / 100 * self._base_mana
        if spell.cast == 0 and spell.kind != "heal":
            cost *= 1 - self.tv("Benediction", 0) / 100
        if spell.name in ("Consecration", "Hammer of Wrath", "Exorcism", "Holy Wrath"):
            cost *= 1 - self.tv("Holy Conduit", 0) / 100
        if spell.name in SEALS and self.rank("Twist of Light"):
            cost *= 0.8
        return cost

    def cast_time(self, spell):
        if self.path != "ret" and spell.name == "Holy Light" and self._fight is not None and self._fight.p.buff("Infusion of Light", self._fight.t):
            return max(0.0, spell.cast - 0.5 * self.rank("Infusion of Light"))
        c = spell.cast
        if spell.name == "Hammer of Wrath":
            c = max(0.0, c - 0.5 * self.rank("Instrument of Law"))
        return c

    def hit_bonus(self, spell):
        # Divine Precision is a miss-chance modifier on a class mask (the client's 1310904, the fork's SpellMaskDivinePrecision): Consecration,
        # Exorcism, Holy Shock, Holy Strike, Holy Wrath, Light's Vigil; not Hammer of Wrath, the seals or the judgements (until 2026-10-18 the
        # lab gave it to every Holy "spell" kind)
        if spell.name in DIVINE_PRECISION_SPELLS:
            return self.tv("Divine Precision", 0) / 100
        return 0.0

    # ------------------------------------------------------------ shared mechanics (both paths)
    def _weapon_spec(self, kind):
        """Two- or One-Handed Weapon Specialization: the client rows (20111 / 20196, A_MOD_DAMAGE_PERCENT_DONE, Misc 1) are Physical
        damage only: white swings and Reckoning's extra attacks, not Holy Strike (a Holy-school strike), seals, judgements or spells (audit
        2026-10-18 #5)."""
        return self.tv("Two-Handed Weapon Specialization" if kind == "2h" else "One-Handed Weapon Specialization", 0) / 100

    def _holy_marks(self, spell):
        """Consecrated Ground: +X% to every Holy spell against a mob standing in your Consecration (its dot ticking on the mob)."""
        if not self.rank("Consecrated Ground") or spell.school != "holy":
            return 1.0
        bonus = self.tv("Consecrated Ground", 0) / 100
        if spell.name == "Consecration":
            return 1 + bonus * CONSEC_MARKED_TICKS
        f = self._fight
        return 1 + bonus if (f is not None and f.dot_active("Consecration")) else 1.0

    def _vind_gain(self, fight):
        """Vindication's attack power gain while its buff is up: +1/2/3% of attack power (read from the buff, never written into the player)."""
        p = fight.p
        if not self.rank("Vindication") or not p.buff("Vindication", fight.t):
            return 0.0
        return p.attack_power * self.tv("Vindication", 1) / 100

    def _vind_factor(self, spell):
        """Vindication on the attacks the engine resolves: the expected weapon damage with the extra attack power over the one without
        (white swings and Reckoning: all weapon damage; Holy Strike: its 50% weapon part next to its flat Holy part)."""
        f = self._fight
        if f is None or spell.name not in ("Melee", "Reckoning", "Holy Strike"):
            return 1.0
        gain = self._vind_gain(f)
        if gain <= 0:
            return 1.0
        w = f.p.mh
        weapon = (w.dmg_min + w.dmg_max) / 2 + (f.p.attack_power / 14.0 + w.dps_bonus) * w.speed
        extra = gain / 14.0 * w.speed
        if spell.name == "Holy Strike":
            pct = spell.weapon_pct or 0.5
            flat = (spell.dmg_min + spell.dmg_max) / 2
            return 1 + pct * extra / max(1e-9, flat + pct * weapon)
        return 1 + extra / max(1e-9, weapon)

    def _on_landed_melee(self, fight, spell):
        """Vindication (client and fork: every damaging melee attack that lands procs it, white or special; 30 s)."""
        if self.rank("Vindication") and spell.kind == "melee":
            fight.p.buffs["Vindication"] = {"until": fight.t + 30.0}

    def _melee_roll(self, fight, can_miss=True):
        """The seals' procs and the judgements roll on the melee table (the fork: Seal of Righteousness and Seal of Fury hits "crit only",
        Seal of Command's proc hit and crit, the judgements hit and crit with no dodge, parry or block); crit x2.0 like a melee hit, at the
        melee crit chance plus Holy Power's 1%/rank on other Holy spells (the client's mask holds these procs and judgements). Until
        2026-10-18 the lab rolled judgements on the spell table (never missing, crit x1.5) and seal hits never crit (audit #22)."""
        p = fight.p
        r = fight.rng.random()
        if can_miss:
            miss = max(0.0, MELEE_MISS - p.hit_bonus)
            if r < miss:
                return "miss"
            r -= miss
        return "crit" if r < p.melee_crit + self.tv("Holy Power", 1) / 100 else "hit"

    def _seal_hit(self, fight, seal, dmg, can_miss=False):
        """Deal a seal's proc on the melee table; a crit doubles it and stacks Vengeance."""
        out = self._melee_roll(fight, can_miss)
        if out == "miss":
            fight.note(f"{seal.name} proc MISS")
            return
        crit = out == "crit"
        if crit:
            dmg *= 2.0
            self._vengeance(fight)
        fight.deal(Spell(seal.name, "holy"), dmg, crit)

    def _judge(self, fight, spell, lo, hi, coef):
        """A judgement's damage on the melee table (miss and crit, crit x2.0)."""
        p, m = fight.p, fight.m
        out = self._melee_roll(fight, True)
        if out == "miss":
            fight.note("Judgement MISS")
            return
        dmg = (fight.rng.uniform(lo, hi) + coef * p.spell_power) * self.damage_multiplier(spell, False)
        jcrit = out == "crit"
        if jcrit:
            dmg *= 2.0
            self._vengeance(fight)
        fight.deal(spell, dmg, jcrit)
        fight.note(f"Judgement{' CRIT' if jcrit else ''} {dmg:.0f} -> mob {max(0, m.hp):.0f}")

    def _soc_proc(self, fight, seal):
        """Seal of Command's proc: 7 per minute, (weapon damage + 0.29 x spell power) x 70%, hit and crit on the melee table."""
        p = fight.p
        if fight.rng.random() < 7.0 * p.mh.speed / 60.0:
            wd = fight.weapon_damage(p.mh) + self._vind_gain(fight) / 14.0 * p.mh.speed
            dmg = seal.seal_pct * (wd + SOC_PROC_COEF * p.spell_power) * self.damage_multiplier(seal, False)
            self._seal_hit(fight, seal, dmg, can_miss=True)

    def crit_bonus(self, spell, frozen):
        if self.path != "ret":
            return self._crit_bonus_alt(spell)
        if spell.name == "Holy Strike":
            return self.tv("Holy Power", 0) / 100
        return 0.0

    def damage_multiplier(self, spell, frozen):
        if self.path != "ret":
            return self._damage_multiplier_alt(spell)
        m = (1 + self._weapon_spec("2h")) if spell.school == "physical" else 1.0
        f = self._fight
        if f:
            v = f.p.buff("Vengeance", f.t)
            if v:
                m *= 1 + 0.01 * self.rank("Vengeance") * v["stacks"]
        if spell.name in SEALS or spell.name == "Judgement":
            m *= 1 + self.tv("Improved Seals", 0) / 100
        if spell.name == "Holy Strike" and self.rank("Sacred Arbiter"):
            m *= 1.20
        return m * self._holy_marks(spell) * self._vind_factor(spell)

    def heal_multiplier(self, spell):
        """Healing Light, and Champion of the Light taken back out: the player's spell power carries it for damage, but it "did not" increase
        healing (Blizzard's notes of 1 Oct; the 70425 tooltip says spell damage). The expected heal is exact; a roll keeps its spread."""
        m = 1 + self.tv("Healing Light", 0) / 100
        cotl, coef = getattr(self, "_cotl", 0.0), getattr(spell, "heal_coef", 0.0)
        if cotl > 0 and coef > 0:
            mean = (spell.heal_min + spell.heal_max) / 2 + coef * self._sp_total
            if mean > 0:
                m *= (mean - coef * cotl) / mean
        return m

    def _vengeance(self, fight):
        """Vengeance (70425): "after landing a non-periodic critical strike", any school: melee, seal procs, judgements and spells."""
        if self.rank("Vengeance"):
            p, t = fight.p, fight.t
            v = p.buffs.get("Vengeance")
            stacks = min(3, (v["stacks"] if v and v["until"] > t else 0) + 1)
            p.buffs["Vengeance"] = {"until": t + 30.0, "stacks": stacks}

    def _reckoning_gain(self, fight, chance):
        """Reckoning (70425): a stored extra attack, up to 4, at most one per RECKONING_ICD from either trigger."""
        if self.rank("Reckoning") and fight.t >= getattr(self, "_reck_block_ready", -1.0) and fight.rng.random() < chance:
            self._reck = min(4, getattr(self, "_reck", 0) + 1)
            self._reck_block_ready = fight.t + RECKONING_ICD
            return True
        return False

    def _reckoning_release(self, fight):
        """Blizzard's notes of 16 Oct: "Your next melee swing (auto attack) will trigger all accumulated charges for 1 extra attack each"."""
        n, self._reck = getattr(self, "_reck", 0), 0
        for _ in range(n):
            fight.resolve_attack(Spell("Reckoning", "physical", kind="melee", resource="none"), white=True, hand="mh")

    def periodic_can_crit(self, spell):
        return True

    def mana_regen(self, p, t):
        if self.path != "ret":
            return class_mana_regen_tick("paladin", p.spirit) + self._wisdom_tick
        return class_mana_regen_tick("paladin", p.spirit)

    def on_regen_tick(self, fight, p, t):
        if self.path != "ret" and self._wisdom_tick and t < p.fsr_until:   # Blessing of Wisdom ignores the five-second rule
            p.mana = min(p.mana_max, p.mana + self._wisdom_tick * (1.0 - min(1.0, p.regen_while_casting)))

    def armor_bonus(self):
        if self.path != "ret":
            self._melee_pending = True   # only Fight.mob_swing asks for it: the next split_damage_taken is a melee hit (block roll)
        return 0.0

    def health_regen(self, p):
        return class_health_regen_tick("paladin", p.spirit)

    def pushback_resisted(self, fight, spell):
        if self.path != "ret" and getattr(spell, "selfheal", False) and spell.cast > 0 and self.rank("Spiritual Focus"):
            return fight.rng.random() < self.tv("Spiritual Focus", 0) / 100
        if spell.kind == "heal" and self.rank("Spiritual Focus"):
            return fight.rng.random() < self.tv("Spiritual Focus", 0) / 100
        return False

    def split_damage_taken(self, fight, dmg):
        if self.path != "ret":
            return self._split_damage_taken_alt(fight, dmg)
        p = fight.p
        if p.buff("Divine Protection", fight.t):
            return 0.0
        return dmg

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        if self.path != "ret":
            return self._on_fight_start_alt(fight)
        self._fight = fight
        self._base_mana = fight.p.base_mana
        p, t = fight.p, fight.t
        seal = self.seal()
        if seal is not None and p.mana >= self.mana_cost(seal) + 100:
            p.mana -= self.mana_cost(seal)
            p.fsr_until = t + 5.0
            p.buffs["Seal"] = {"until": t + 30.0, "name": seal.name}
            fight.casts[seal.name] = fight.casts.get(seal.name, 0) + 1

    def on_swing(self, fight, spell, outcome, amount, hand):
        if self.path != "ret":
            return self._on_swing_alt(fight, spell, outcome, amount, hand)
        p, m, t = fight.p, fight.m, fight.t
        if spell.name == "Melee" and getattr(self, "_reck", 0):   # Reckoning's stored attacks go with the next auto attack, landed or not
            self._reckoning_release(fight)
        if outcome in ("miss", "dodge", "parry"):
            return
        sealb = p.buff("Seal", t)
        seal = self.spells.get(sealb["name"]) if sealb else None
        if seal is not None and spell.name == "Melee":
            if getattr(seal, "seal_pct", 0.0):
                self._soc_proc(fight, seal)
            elif getattr(seal, "seal_max", 0.0):   # Seal of Righteousness: the client's per-hit rows (SOR_PER_HIT; the Retribution path holds a two-hander)
                base, coef = sor_hit(seal, self.level, p.mh.speed, True)
                self._seal_hit(fight, seal, (base + coef * p.spell_power) * self.damage_multiplier(seal, False))
        self._on_landed_melee(fight, spell)
        if outcome == "crit":
            self._vengeance(fight)

    def on_hit(self, fight, spell, amount, crit, frozen):
        if self.path != "ret" and self._on_hit_alt(fight, spell, amount, crit):
            return
        p, m, t = fight.p, fight.m, fight.t
        if crit and amount > 0 and spell.kind not in ("melee", "ranged", "heal"):   # a spell's crit (melee crits stack in on_swing)
            self._vengeance(fight)
        if spell.name in SEALS:   # a seal recast in combat (2026-09-30 fix: it never set the buff, so fights over 30 s recast it every GCD)
            p.buffs["Seal"] = {"until": t + 30.0, "name": spell.name}
            return
        if spell.name == "Judgement":
            sealb = p.buff("Seal", t)
            seal = self.spells.get(sealb["name"]) if sealb else None
            if seal is not None and getattr(seal, "judge", None):
                lo, hi = seal.judge
                if m.stunned(t) and getattr(seal, "judge_stunned", None):
                    lo, hi = seal.judge_stunned
                self._judge(fight, spell, lo, hi, seal.coef)
                # Sanctified Judgement (70425): 33/66/100% chance to return 20/40/60% of the judged seal's mana (60% at every rank until 2026-10-17)
                if self.rank("Sanctified Judgement") and fight.rng.random() < self.tv("Sanctified Judgement", 0) / 100:
                    p.mana = min(p.mana_max, p.mana + self.tv("Sanctified Judgement", 1) / 100 * self.mana_cost(seal))
        if spell.name == "Holy Strike" and self.rank("Sacred Arbiter"):
            pass
        if spell.name == "Hammer of Justice":
            m.stun_until = max(m.stun_until, t + spell.stun)
        if spell.name == "Divine Protection":
            p.buffs["Divine Protection"] = {"until": t + 8.0}
        if spell.name == "Lay on Hands":
            fight.heal(spell, p.hp_max)
            p.mana = 0.0
        if spell.kind == "heal" and crit and self.rank("Illumination"):
            p.mana = min(p.mana_max, p.mana + 0.5 * spell.cost * self.tv("Illumination", 0) / 100)

    def on_hit_taken(self, fight, dmg, crit=False):
        p, m, t = fight.p, fight.m, fight.t
        if crit:   # Reckoning: "a 20/40/60/80/100% chance after receiving a non-periodic critical strike" to store an extra attack
            self._reckoning_gain(fight, self.tv("Reckoning", 1) / 100)
        if crit and self.rank("Eye for an Eye") and dmg > 0:
            fight.deal(Spell("Eye for an Eye", "holy"), min(0.5 * p.hp_max, dmg * self.tv("Eye for an Eye", 0) / 100), False)

    def after_cast(self, fight, spell):
        if self.path != "ret":
            return self._after_cast_alt(fight, spell)
        p, t = fight.p, fight.t
        cd = spell.cooldown
        if spell.name == "Judgement":
            cd = max(GCD, cd - self.tv("Improved Judgement", 0))
        if spell.name == "Hammer of Justice":
            cd = max(10.0, cd - self.tv("Improved Hammer of Justice", 0))
        if spell.name in ("Divine Protection", "Divine Shield"):
            cd = max(60.0, cd - self.tv("Sacred Duty", 1))
        if cd > 0:
            p.cooldowns[spell.name] = t + cd
        if spell.name == "Holy Strike" and self.rank("Sacred Arbiter"):
            pass

    def after_fight(self, p, t):
        """Holy Light (or Flash of Light) back to 80% health between fights when mana allows; drinking follows the engine's threshold."""
        if self.path != "ret":
            return self._after_fight_alt(p, t)
        spent = 0.0
        hl, fl = self.spells.get("Holy Light"), self.spells.get("Flash of Light")
        for _ in range(3):
            if p.hp >= 0.80 * p.hp_max:
                break
            missing = p.hp_max - p.hp
            heal = fl if (fl is not None and missing < (fl.heal_min + fl.heal_max) / 2 * 1.5) else hl
            if heal is None or p.mana < self.mana_cost(heal):
                break
            p.mana -= self.mana_cost(heal)
            amount = ((heal.heal_min + heal.heal_max) / 2 + heal.heal_coef * p.spell_power) * self.heal_multiplier(heal)
            p.hp = min(p.hp_max, p.hp + amount)
            spent += max(GCD, heal.cast)
        return spent

    # ------------------------------------------------------------ priority list
    def decide(self, fight):
        if self.path != "ret":
            return self._decide_alt(fight)
        if fight.others():   # a pull of several mobs: the area priority first (engine.BaseModule.decide_aoe, AOE below)
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        judge, hs, cons, how, hoj, dp, loh, hl, fol = (sp.get(n) for n in ("Judgement", "Holy Strike", "Consecration", "Hammer of Wrath", "Hammer of Justice", "Divine Protection", "Lay on Hands", "Holy Light", "Flash of Light"))
        hp = m.hp
        seal = self.seal()
        # emergencies: Lay on Hands, bubble and heal
        if loh and can(loh) and p.hp < 0.15 * p.hp_max:
            return loh
        if p.hp < 0.35 * p.hp_max and hp > 0.25 * m.hp_max:
            if dp and can(dp) and not p.buff("Divine Protection", t):
                return dp
            if hl and can(hl) and (p.buff("Divine Protection", t) or m.stunned(t)):
                return hl
            if hoj and can(hoj) and not m.stunned(t):
                return hoj
            if fol and can(fol) and p.hp < 0.25 * p.hp_max:
                return fol
        # a casting mob: Hammer of Justice breaks the cast (it stands there casting until you reach it)
        if m.caster and m.casting(t) and hoj and can(hoj) and m.dist <= hoj.range and not m.stunned(t):
            return hoj
        if not in_melee:
            return "advance"
        # keep the seal up
        if seal is not None and not p.buff("Seal", t) and can(seal) and hp > 0.15 * m.hp_max:
            return seal
        if how and can(how) and hp <= 0.2 * m.hp_max:
            return how
        # Hammer of Justice into a doubled Seal of Command judgement
        if hoj and can(hoj) and judge and p.ready("Judgement", t) and seal is not None and getattr(seal, "judge_stunned", None) and hp > 0.3 * m.hp_max and not m.stunned(t):
            return hoj
        if judge and can(judge) and p.buff("Seal", t):
            return judge
        if hs and can(hs):
            return hs
        if cons and can(cons) and p.mana > 0.45 * p.mana_max and hp > 0.3 * m.hp_max and not fight.dot_active("Consecration"):
            return cons
        return None

    # ================================================================ Holy and Protection leveling (spec "holy..." / "prot...")
    def _init_alt(self, spec):
        """Holy: a two-hander (spec with "shield" in it: one-hander and shield), Seal of Righteousness (Seal of Fury with a shield),
        offensive Holy Shock, heals in combat. Protection: one-hander and shield, Seal of Fury, Holy Shield, Righteous Fury assumed
        always up (30 min buff cast between pulls; its mana is not charged)."""
        self.shield = self.path == "prot" or "shield" in spec
        self.weapon_kind = "1h" if self.shield else "2h"
        self.rf = self.path == "prot" and "Righteous Fury" in self.spells
        # rotation knobs (plain attributes, so run.apply_rotation's "knobs" can set them)
        # defaults from a hand sweep on the proposed holy-raid-healer / prot-tank builds (levels 30, 45, 60; 500 fights, seed 1; 2026-09-30):
        # Holy: Consecration never (its mana buys more as Holy Shock and less drinking), Holy Shock only above 70% mana, Blessing of
        # Wisdom, drink below 25%; Protection: Consecration above 60% mana, Blessing of Might, drink below 15%. Kings / Might / Wisdom
        # and the heal threshold are within ~2% of each other (in-combat heals almost never trigger against same-level mobs).
        holy = self.path == "holy"
        self.heal_below = 0.40 if holy else 0.35       # in-combat heal / emergency threshold (share of health)
        self.shock_mana = 0.70                         # offensive Holy Shock only above this mana share
        self.cons_mana = 1.10 if holy else 0.60        # Consecration only above this mana share (above 1 = never)
        self.blessing = "wisdom" if holy else "might"  # "might", "kings" or "wisdom" (one Blessing on yourself)
        self.drink_below = 0.25 if holy else 0.15      # rest threshold (a tuned rotation file overrides it)
        self.seal_pref = "fury" if self.shield else "righteousness"
        self._free_judge = False
        self._melee_pending = False
        self._sof_live = False
        self._bulwark_until = -1.0
        self._ss_ready = -1.0
        self._wisdom_tick = 0.0
        # heals resolved by this module (crit, Divine Favor, Illumination, Infusion of Light): copies of kind "buff"
        for name in ("Holy Light", "Flash of Light"):
            s = self.spells.get(name)
            if s is not None:
                c = copy.copy(s)
                c.kind, c.selfheal = "buff", True
                self.spells[name] = c
        shock = self.spells.get("Holy Shock")
        if shock is not None and getattr(shock, "shock_heal", (0, 0))[1] > 0:
            c = copy.copy(shock)
            c.name, c.kind, c.selfheal = "Holy Shock (heal)", "buff", True
            c.heal_min, c.heal_max = shock.shock_heal
            c.heal_coef = shock.shock_heal_coef
            c.dmg_min = c.dmg_max = 0.0
            self.spells[c.name] = c
        hsh = self.spells.get("Holy Shield")
        if hsh is not None:
            c = copy.copy(hsh)
            c.kind = "buff"
            self.spells["Holy Shield"] = c

    def _seal_alt(self):
        sp = self.spells
        if self.seal_pref == "fury" and sp.get("Seal of Fury") is not None:
            return sp["Seal of Fury"]
        return sp.get("Seal of Command") or sp.get("Seal of Righteousness")

    def _make_player_alt(self, level):
        base = class_base_stats("paladin", level)
        # caster gear row for a Holy-path build that casts Holy Shock (audit 2026-10-18 row 65); the Holy rotation's page builds without it
        # (holy-leveling, shockadin-open-leveling on 2026-10-18) melee and judge for 100% of their damage: the melee row is 4-5% faster at 60
        caster = self.path == "holy" and "Holy Shock" in self.spells
        g = gear_stats(level, self.gear, "paladin-caster" if caster else "paladin")
        kings = 1.10 if self.blessing == "kings" and self.book.get("Blessing of Kings") is not None else 1.0
        sh_armor = _interp(SHIELD_ARMOR, level) if self.shield else 0.0
        sh_sta = _interp(SHIELD_STAMINA, level) if self.shield else 0.0
        strength = (base["strength"] + g["strength"]) * (1 + self.tv("Divine Strength", 0) / 100) * kings
        agility = (base["agility"] + g["agility"]) * kings
        stamina = (base["stamina"] + g["stamina"] + sh_sta) * (1 + self.tv("Sacred Duty", 0) / 100) * kings
        intellect = (base["intellect"] + g["intellect"]) * (1 + self.tv("Divine Intellect", 0) / 100) * kings
        spirit = (base["spirit"] + g["spirit"]) * kings
        dev = self.book.get("Devotion Aura")
        armor = (g["armor"] + sh_armor) * (1 + self.tv("Toughness", 0) / 100) + (getattr(dev, "armor", 0.0) if dev else 0.0)
        bm = class_base_mana("paladin", level)
        might = self.book.get("Blessing of Might") if self.blessing == "might" else None
        self._cotl = intellect * self.tv("Champion of the Light", 0) / 100   # spell damage only (heal_multiplier takes it back out of heals)
        p = Player(level=level, hp_max=class_base_health("paladin", level) + 10 * stamina, hp=0.0, mana_max=bm + 15 * intellect, mana=0.0, base_mana=bm,
                   spirit=spirit, intellect=intellect, spell_power=g["spell_power"] + self._cotl, armor=armor,
                   spell_crit=class_spell_crit("paladin", level, intellect) + self.tv("Holy Power", 1) / 100, dodge=class_dodge("paladin", level, agility), ranged_crit=0.0)
        self._sp_total = p.spell_power
        self._reck = 0
        self._reck_block_ready = -1.0
        p.strength, p.agility, p.stamina = strength, agility, stamina
        p.attack_power = class_attack_power("paladin", level, strength, agility) + (getattr(might, "ap", 0.0) if might else 0.0)
        self.base_ap = p.attack_power
        p.melee_crit = class_melee_crit("paladin", level, agility) + self.tv("Conviction", 0) / 100
        p.hit_bonus = self.tv("Precision", 0) / 100
        defense = self.tv("Anticipation", 0) * DEFENSE_PER_POINT
        p.parry = 0.05 + self.tv("Deflection", 0) / 100 + defense
        p.dodge += defense
        kind = self.weapon_kind
        dps = weapon_dps(level, kind)
        p.mh = Weapon(dmg_min=dps * WEAPON_SPEED[kind] * 0.8, dmg_max=dps * WEAPON_SPEED[kind] * 1.2, speed=WEAPON_SPEED[kind], kind=kind)
        if self.shield:
            p.block = BASE_BLOCK + defense
            p.block_value = (SHIELD_BLOCK_PER_LEVEL * level + strength / 20.0) * (1 + self.tv("Shield Specialization", 0) / 100)
        bow = self.book.get("Blessing of Wisdom") if self.blessing == "wisdom" else None
        mp5 = re.search(r"restoring (\d+) mana every 5 seconds", getattr(bow, "text", "") or "") if bow else None
        self._wisdom_tick = float(mp5.group(1)) * 2.0 / 5.0 if mp5 else 0.0
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Reverence", 0) / 100
        return p

    def _crit_bonus_alt(self, spell):
        b = 0.0
        if spell.name == "Holy Strike":
            b += self.tv("Holy Power", 0) / 100
        if spell.name in ("Holy Shock", "Holy Shock (heal)"):
            b += (self.tv("Holy Power", 0) - self.tv("Holy Power", 1)) / 100   # 3%/rank instead of the 1%/rank already in spell crit
        f = self._fight
        if f is not None and f.p.buff("Divine Favor", f.t) and (spell.name == "Holy Shock" or getattr(spell, "selfheal", False)):
            b += 1.0
        return b

    def _damage_multiplier_alt(self, spell):
        m = (1 + self._weapon_spec(self.weapon_kind)) if spell.school == "physical" else 1.0
        f = self._fight
        if f:
            v = f.p.buff("Vengeance", f.t)
            if v:
                m *= 1 + 0.01 * self.rank("Vengeance") * v["stacks"]
        if spell.name in SEALS or spell.name == "Judgement":
            m *= 1 + self.tv("Improved Seals", 0) / 100
        if spell.name == "Holy Strike" and self.rank("Sacred Arbiter"):
            m *= 1.20
        return m * self._holy_marks(spell) * self._vind_factor(spell)

    # ---------------------------------------------------------------- shield block (engine hooks when the engine has them)
    def block_bonus(self, fight):
        if self.path == "ret":
            return 0.0
        p, t = fight.p, fight.t
        b = 0.0
        hs = p.buff("Holy Shield", t)
        if hs and hs["charges"] > 0:
            b += getattr(self.spells.get("Holy Shield"), "hs_block", 0.30)
        rd = p.buff("Redoubt", t)
        if rd and rd["charges"] > 0:
            b += self.tv("Redoubt", 1) / 100
        return b

    def on_block(self, fight):
        if self.path == "ret":
            return
        p, t = fight.p, fight.t
        fight.casts["Shield block"] = fight.casts.get("Shield block", 0) + 1
        hs = p.buff("Holy Shield", t)
        if hs and hs["charges"] > 0:
            hs["charges"] -= 1
            sp = Spell("Holy Shield", "holy")
            dmg = hs["dmg"] * self.damage_multiplier(sp, False)
            fight.deal(sp, dmg, False)
            fight.note(f"Holy Shield {dmg:.0f} -> mob {max(0, fight.m.hp):.0f}")
        rd = p.buff("Redoubt", t)
        if rd and rd["charges"] > 0:
            rd["charges"] -= 1
        if self.rank("Shield Specialization") and t >= self._ss_ready and fight.rng.random() < self.tv("Shield Specialization", 1) / 100:
            p.mana = min(p.mana_max, p.mana + self.tv("Shield Specialization", 2) / 100 * p.mana_max)
            self._ss_ready = t + 3.0
        self._reckoning_gain(fight, self.tv("Reckoning", 0) / 100)

    def _split_damage_taken_alt(self, fight, dmg):
        p, t = fight.p, fight.t
        melee, self._melee_pending = self._melee_pending, False
        if p.buff("Divine Protection", t):
            return 0.0
        if melee and self.shield:
            if not ENGINE_BLOCK and fight.rng.random() < p.block + self.block_bonus(fight):   # older engine: roll the block here
                blocked = min(dmg, p.block_value)
                dmg -= blocked
                fight.note(f"blocked {blocked:.0f}")
                self.on_block(fight)
            # 2%/rank (the client's talent curve; the fork reads it: talents_protection.go); the tooltip's 10% is rank 5's on every rank
            if self.rank("Redoubt") and fight.rng.random() < 0.02 * self.rank("Redoubt"):
                p.buffs["Redoubt"] = {"until": t + 10.0, "charges": 5}
        if self.rf:
            dmg *= 1 - self.tv("Improved Righteous Fury", 0) / 100
            if p.buff("Iron Creed", t):
                dmg *= 1 - self.tv("Iron Creed", 1) / 100
        if self._sof_live:   # Improved Seal of Fury: the seal's shield was used up
            if t >= p.absorb_until:
                self._sof_live = False
            elif p.absorb <= 1e-6:
                self._sof_live = False
                if self.rank("Improved Seal of Fury"):
                    p.mana = min(p.mana_max, p.mana + 60.0)
        return dmg

    # ---------------------------------------------------------------- events
    def _on_fight_start_alt(self, fight):
        self._fight = fight
        self._base_mana = fight.p.base_mana
        self._melee_pending = False
        p, t = fight.p, fight.t
        seal = self.seal()
        if seal is not None and p.mana >= self.mana_cost(seal) + 100:
            p.mana -= self.mana_cost(seal)
            p.fsr_until = t + 5.0
            p.buffs["Seal"] = {"until": t + 30.0, "name": seal.name}
            fight.casts[seal.name] = fight.casts.get(seal.name, 0) + 1

    def _on_swing_alt(self, fight, spell, outcome, amount, hand):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name == "Melee" and getattr(self, "_reck", 0):   # Reckoning's stored attacks go with the next auto attack, landed or not
            self._reckoning_release(fight)
        if outcome in ("miss", "dodge", "parry"):
            return
        sealb = p.buff("Seal", t)
        seal = self.spells.get(sealb["name"]) if sealb else None
        if seal is not None and spell.name == "Melee":
            if getattr(seal, "fury_hit", 0.0):
                dmg = (seal.fury_hit + seal.fury_coefs[1] * p.spell_power) * self.damage_multiplier(seal, False)
                if self._melee_roll(fight, False) == "crit":   # crit only on the melee table (the fork's seal_of_fury.go)
                    dmg *= 2.0
                    self._vengeance(fight)
                    fight.deal(Spell(seal.name, "holy"), dmg, True)
                else:
                    fight.deal(Spell(seal.name, "holy"), dmg, False)
                if self.shield:
                    shield = 0.5 * dmg
                    if t < self._bulwark_until:
                        p.absorb += shield
                    else:
                        p.absorb, p.absorb_until = shield, t + SOF_SHIELD_TIME
                        self._sof_live = True
            elif getattr(seal, "seal_pct", 0.0):
                self._soc_proc(fight, seal)
            elif getattr(seal, "seal_max", 0.0):
                # "slower weapons cause more Holy damage per swing": the client's per-hit rows by swing speed and hand (SOR_PER_HIT)
                base, coef = sor_hit(seal, self.level, p.mh.speed, self.weapon_kind == "2h")
                self._seal_hit(fight, seal, (base + coef * p.spell_power) * self.damage_multiplier(seal, False))
        self._on_landed_melee(fight, spell)
        if outcome == "crit":
            self._vengeance(fight)

    def _self_heal(self, fight, spell):
        p, t = fight.p, fight.t
        amount = (fight.rng.uniform(spell.heal_min, spell.heal_max) + spell.heal_coef * p.spell_power) * self.heal_multiplier(spell)
        crit = fight.rng.random() < p.spell_crit + self._crit_bonus_alt(spell)
        p.buffs.pop("Divine Favor", None)
        if spell.name == "Holy Light":
            p.buffs.pop("Infusion of Light", None)
        if crit:
            amount *= 1.5
            if self.rank("Illumination") and fight.rng.random() < self.tv("Illumination", 0) / 100:
                p.mana = min(p.mana_max, p.mana + 0.5 * spell.cost)
            if spell.name in ("Flash of Light", "Holy Shock (heal)") and self.rank("Infusion of Light"):
                p.buffs["Infusion of Light"] = {"until": t + 15.0}
        got = fight.heal(spell, amount, "player", crit)
        fight.note(f"{spell.name}{' CRIT' if crit else ''} heals {got:.0f}")

    def _on_hit_alt(self, fight, spell, amount, crit):
        p, m, t = fight.p, fight.m, fight.t
        name = spell.name
        if crit and amount > 0 and spell.kind not in ("melee", "ranged", "heal") and not getattr(spell, "selfheal", False):
            self._vengeance(fight)   # a spell's crit, Holy Shock's included (melee crits stack in on_swing)
        if name in SEALS:   # a seal recast in combat (the Retribution path leaves this to on_fight_start)
            p.buffs["Seal"] = {"until": t + 30.0, "name": name}
            return True
        if name == "Judgement":
            self._free_judge = False
            sealb = p.buff("Seal", t)
            seal = self.spells.get(sealb["name"]) if sealb else None
            if seal is None:
                return True
            if getattr(seal, "fury_hit", 0.0):
                (lo, hi), coef = seal.fury_judge, seal.fury_coefs[0]
            elif getattr(seal, "judge", None):
                lo, hi = seal.judge_stunned if (m.stunned(t) and getattr(seal, "judge_stunned", None)) else seal.judge
                coef = seal.coef
            else:
                return True
            self._judge(fight, spell, lo, hi, coef)
            if self.rank("Sanctified Judgement") and fight.rng.random() < self.tv("Sanctified Judgement", 0) / 100:
                p.mana = min(p.mana_max, p.mana + self.tv("Sanctified Judgement", 1) / 100 * self.mana_cost(seal))
            return True
        if name == "Holy Strike" and self.rf and self.rank("Iron Creed"):
            p.buffs["Iron Creed"] = {"until": t + 6.0}
        elif name == "Hammer of Justice":
            m.stun_until = max(m.stun_until, t + spell.stun)
        elif name == "Divine Protection":
            p.buffs["Divine Protection"] = {"until": t + 8.0}
            p.buffs["Forbearance"] = {"until": t + 60.0}
        elif name == "Templar's Bulwark":
            p.absorb, p.absorb_until = p.hp_max, t + 8.0
            self._bulwark_until = t + 8.0
            self._sof_live = False
            p.buffs["Forbearance"] = {"until": t + 60.0}
        elif name == "Lay on Hands":
            fight.heal(spell, p.hp_max)
            p.mana = 0.0
        elif name == "Holy Shield":
            p.buffs["Holy Shield"] = {"until": t + 10.0, "charges": HOLY_SHIELD_CHARGES, "dmg": getattr(spell, "hs_dmg", 0.0)}
        elif name == "Holy Shock":   # the offensive cast (resolve_spell rolled it)
            p.buffs.pop("Divine Favor", None)
            if crit and self.rank("Infusion of Light"):
                p.buffs["Infusion of Light"] = {"until": t + 15.0}
        elif getattr(spell, "selfheal", False):
            self._self_heal(fight, spell)
        return True

    def _after_cast_alt(self, fight, spell):
        p, t = fight.p, fight.t
        cd, name = spell.cooldown, spell.name
        if name == "Holy Shock (heal)":
            name = "Holy Shock"
        if name == "Judgement":
            cd = max(GCD, cd - self.tv("Improved Judgement", 0))
        if name == "Hammer of Justice":
            cd = max(10.0, cd - self.tv("Improved Hammer of Justice", 0))
        if name in ("Divine Protection", "Divine Shield", "Templar's Bulwark"):
            cd = max(60.0, cd - self.tv("Sacred Duty", 1))
        if cd > 0:
            p.cooldowns[name] = t + cd

    def _after_fight_alt(self, p, t):
        """Holy Light / Flash of Light back to 80% health between fights, with the expected crit and Illumination refund."""
        spent = 0.0
        hl, fl = self.spells.get("Holy Light"), self.spells.get("Flash of Light")
        cc = min(1.0, p.spell_crit)
        illum = self.tv("Illumination", 0) / 100
        for _ in range(3):
            if p.hp >= 0.80 * p.hp_max:
                break
            missing = p.hp_max - p.hp
            heal = fl if (fl is not None and missing < (fl.heal_min + fl.heal_max) / 2 * 1.5) else hl
            if heal is None or p.mana < self.mana_cost(heal):
                break
            p.mana -= self.mana_cost(heal)
            p.mana = min(p.mana_max, p.mana + cc * illum * 0.5 * heal.cost)
            amount = ((heal.heal_min + heal.heal_max) / 2 + heal.heal_coef * p.spell_power) * self.heal_multiplier(heal) * (1 + 0.5 * cc)
            p.hp = min(p.hp_max, p.hp + amount)
            spent += max(GCD, heal.cast)
        return spent

    def _off_gcd(self, fight, s):
        """Divine Favor and Swift Judgement: used off the global cooldown (assumption), paid and counted here."""
        p, t = fight.p, fight.t
        cost = self.mana_cost(s)
        if s is None or not p.ready(s.name, t) or p.mana < cost:
            return False
        p.mana -= cost
        if cost > 0:
            p.fsr_until = t + 5.0
        p.cooldowns[s.name] = t + s.cooldown
        fight.casts[s.name] = fight.casts.get(s.name, 0) + 1
        return True

    def _favor(self, fight):
        df = self.spells.get("Divine Favor")
        if df is not None and self._off_gcd(fight, df):
            fight.p.buffs["Divine Favor"] = {"until": fight.t + 60.0}

    # ---------------------------------------------------------------- priority list (Holy and Protection)
    def _decide_alt(self, fight):
        if fight.others():
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5

        def can(s):
            return s is not None and p.ready("Holy Shock" if s.name == "Holy Shock (heal)" else s.name, t) and fight.can_afford(s, self.mana_cost(s))

        (judge, hs, cons, how, hoj, dp, loh, hl, fol, shock, shock_h, hshield, bulwark, swift) = (sp.get(n) for n in (
            "Judgement", "Holy Strike", "Consecration", "Hammer of Wrath", "Hammer of Justice", "Divine Protection", "Lay on Hands", "Holy Light",
            "Flash of Light", "Holy Shock", "Holy Shock (heal)", "Holy Shield", "Templar's Bulwark", "Swift Judgement"))
        seal = self.seal()
        hpf = p.hp / p.hp_max
        forb = p.buff("Forbearance", t)
        # emergencies and in-combat heals
        if loh and can(loh) and hpf < 0.15:
            return loh
        if hpf < self.heal_below and m.hp > 0.2 * m.hp_max:
            if bulwark and can(bulwark) and not forb:
                return bulwark
            if shock_h and can(shock_h):
                self._favor(fight)
                return shock_h
            if dp and can(dp) and not forb and hpf < 0.30 and t >= self._bulwark_until:
                return dp
            if hoj and can(hoj) and not m.stunned(t) and m.dist <= hoj.range:
                return hoj
            safe = m.stunned(t) or p.buff("Divine Protection", t) or t < self._bulwark_until
            if hl and can(hl) and (safe or self.path == "holy"):
                self._favor(fight)
                return hl
            if fol and can(fol) and hpf < 0.25:
                self._favor(fight)
                return fol
        # a casting mob: Hammer of Justice breaks the cast
        if m.caster and m.casting(t) and hoj and can(hoj) and m.dist <= hoj.range and not m.stunned(t):
            return hoj
        # Holy Shock on the enemy (40 yd: also while the mob walks in)
        if shock and can(shock) and p.mana > self.shock_mana * p.mana_max and m.hp > 0.10 * m.hp_max:
            if hpf >= 0.70:
                self._favor(fight)
            return shock
        if not in_melee:
            return "advance"
        if seal is not None and not p.buff("Seal", t) and can(seal) and m.hp > 0.15 * m.hp_max:
            return seal
        if how and can(how) and m.hp <= 0.2 * m.hp_max:
            return how
        if hshield and can(hshield) and m.hp > 0.2 * m.hp_max:
            hb = p.buff("Holy Shield", t)
            if not hb or hb["charges"] <= 0:
                return hshield
        if hoj and can(hoj) and judge and p.ready("Judgement", t) and seal is not None and getattr(seal, "judge_stunned", None) and m.hp > 0.3 * m.hp_max and not m.stunned(t):
            return hoj
        if swift and judge and p.buff("Seal", t) and not p.ready("Judgement", t) and p.cooldowns.get("Judgement", 0.0) - t >= 3.0 and m.hp > 0.25 * m.hp_max:
            if self._off_gcd(fight, swift):
                p.cooldowns["Judgement"] = t
                self._free_judge = True
        if judge and can(judge) and p.buff("Seal", t):
            return judge
        if hs and can(hs):
            return hs
        if cons and can(cons) and p.mana > self.cons_mana * p.mana_max and m.hp > 0.3 * m.hp_max and not fight.dot_active("Consecration"):
            return cons
        return None
