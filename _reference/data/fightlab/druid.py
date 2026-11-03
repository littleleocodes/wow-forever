"""Druid module for the fight lab (Bear Form at 10-19, Cat Form from 20; Balance as a second spec model).

Spell ranks are read from `_reference/data/forever-spells/druid.json` (beta client build 1.60.1.70291); talent numbers from each
rank's tooltip in `_reference/data/forever-talents/druid.json`. Cat Form attacks once a second with a "paw" whose damage grows
like a one-hander by level (`tables.weapon_dps`), attack power from the client's base stats (2 AP per Strength, 1 per Agility)
plus Cat Form's 120 + Agility and Predatory Strikes.

Playstyle `feral-cat-dps` (the scorer's model id, used for leveling): prowl up behind the mob, open with Ravage from 32 (Shred from
22, Claw before; Pounce comes at 36, after Ravage), Rake once (no Tiger's Fury: removed, see TIGERS_FURY), Claw to five points,
Ferocious Bite whenever it kills (from 32), Rip at five points on a mob above half health (before Ferocious Bite: Rip at
RIP_EARLY_CP points on a mob above RIP_EARLY_HP of its health), Berserk on the pull when ready; shift out to Regrowth when low
(Nature's Swiftness + Healing Touch in an emergency) and shift back (Cat Form costs 55% of base mana; Furor carries a share of the
energy you left with plus some per second out of form). Between fights: Rejuvenation / Regrowth in caster form when hurt (only with
the mana to shift back), then Cat Form again; water below 35% mana (the tuned rule in rotations/ drinks lower).

Playstyle `balance-dps`: see decide_balance. Moonkin Form (40) blocks healing spells: an emergency heal leaves the form and going back
costs the form's mana; between fights a Moonkin stays in the form and eats.

2026-10-09 fixes (against the 70291 tooltips): Eclipse by rank (0.17/0.33/0.5 s, was 0.5 at any rank), Forever's Nature's Grace
(10% faster casts and global cooldown for 3 s, was Classic's 0.5 s off the next cast), Nature's Focus on every Arcane and Nature spell
(was heals only), Moonkin Form and healing, no wand (druids cannot use one), Rip before Ferocious Bite, Tiger's Fury (removed again on 2026-10-17), Furor's cat
energy (read the rage number: 10% at any rank), Heart of the Wild (cat Strength and bear Stamina were swapped), Blood Frenzy's cat
combo point, Nature's Splendor's longer damage and heals over time, Improved Moonfire's critical strike chance, Omen of Clarity at the
simulator's beta-log rate from attacks and spells (Wrath does not use Clearcasting), Rip's attack power share capped at 4 points,
Shifting Power in place of King of the Jungle (removed in 70170), and Entangling Roots, Hurricane and Lacerate parsed (Entangling Roots
had parsed to no root, so the Balance emergency cast it for nothing; now it roots and the druid steps out before the heal).
"""
import copy
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell, Weapon
from tables import (MOB_SWING, GCD, MELEE_RANGE, class_attack_power, class_base_health, class_base_mana, class_base_stats, class_dodge,
                    class_health_regen_tick, class_mana_regen_tick, class_melee_crit, class_spell_crit, gear_stats, weapon_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/druid.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/druid.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
PCT = re.compile(r"(\d+)% (?:normal )?damage plus (\d[\d,]*)")
RAKE = re.compile(r"for (\d[\d,]*) damage and an additional (\d[\d,]*) damage over (\d+) sec")
POUNCE = re.compile(r"stunning the target for (\d+) sec and causing (\d[\d,]*) damage over (\d+) sec")
FIVE = re.compile(r"5 points: (\d[\d,]*)(?:-(\d[\d,]*))? damage(?: over (\d+) sec)?")
ONE = re.compile(r"1 point : (\d[\d,]*)(?:-(\d[\d,]*))? damage(?: over (\d+) sec)?")
EXTRA = re.compile(r"each extra point of energy into ([\d.]+) additional damage")
HEAL = re.compile(r"Heals a friendly target for (\d[\d,]*) to (\d[\d,]*)(?: and another (\d[\d,]*) over (\d+) sec)?")
HOT = re.compile(r"Heals the target for (\d[\d,]*) over (\d+) sec")
DMG = re.compile(r"Causes (\d[\d,]*) to (\d[\d,]*) (\w+) damage")
MOONFIRE = re.compile(r"Burns the enemy for (\d[\d,]*) to (\d[\d,]*) Arcane damage and then an additional (\d[\d,]*) Arcane damage over (\d+) sec")
CP = re.compile(r"Awards (\d) combo point")
# 2026-10-18 (audit 2 row 3): Classic's "increasing melee attack power by"; 70425 says "increasing Attack Power by 120 plus Agility",
# "Armor contribution from items by 180%, and Health by 180", so all three had read nothing since 70170 (forms only, see FORMS)
FORM_AP = re.compile(r"increasing (?:melee )?attack power by (\d+)", re.I)
FORM_ARMOR = re.compile(r"armor contribution from items by (\d+)%", re.I)
FORM_HP = re.compile(r"and health by (\d[\d,]*)", re.I)
FORMS = {"Cat Form", "Bear Form", "Dire Bear Form"}
MAUL = re.compile(r"next attack by (\d+) damage")
SWARM = re.compile(r"causing (\d[\d,]*) Nature damage over (\d+) sec")
STARFIRE = re.compile(r"Causes (\d[\d,]*) to (\d[\d,]*) Arcane damage")
SWIPE = re.compile(r"inflicting (\d+) damage")
ROAR = re.compile(r"melee attack power by (\d+)\. Lasts (\d+) sec")
STUN = re.compile(r"Stuns the target for (\d+) sec")
COEF = re.compile(r"([\d.]+)% of spell power \((\w+(?: \w+)?)\)")
ROOTS = re.compile(r"Roots the target in place and causes (\d[\d,]*) Nature damage over (\d+) sec")
STORM = re.compile(r"causing (\d[\d,]*) Nature damage to enemies every (\d+) sec(?:.*?Lasts (\d+) sec)?")
LACERATE = re.compile(r"bleed for (\d[\d,]*) damage over (\d+) sec")
ENERGIZE = re.compile(r"into (\d+) Energy")

TALENT_SPELLS = {"Berserk": "Berserk", "Feral Charge": "Feral Charge", "Primal Bite": "Primal Bite", "Swiftmend": "Swiftmend", "Nature's Swiftness": "Nature's Swiftness",
                 "Insect Swarm": "Insect Swarm", "Moonkin Form": "Moonkin Form", "Wild Growth": "Wild Growth", "Leader of the Pack": "Leader of the Pack",
                 "Shifting Power": "Shifting Power"}
CAT = {"Claw", "Rake", "Shred", "Rip", "Ferocious Bite", "Tiger's Fury", "Pounce", "Ravage", "Cower", "Dash", "Prowl"}
BEAR = {"Maul", "Swipe", "Demoralizing Roar", "Enrage", "Bash", "Growl", "Primal Bite"}


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
                cost_txt = (r.get("cost") or "").replace(",", "")   # "1,185 Mana" had read 1 (audit 2 row 30)
                cost = _num(NUM.search(cost_txt).group(1)) if NUM.search(cost_txt) else 0.0
                cast_txt = (r.get("cast") or "").lower()
                cast = 0.0 if "instant" in cast_txt or not cast_txt or "channel" in cast_txt else _seconds(cast_txt)
                coefs = {k: float(v) / 100 for v, k in COEF.findall(r.get("coefficient") or "")}
                rm = re.search(r"(\d+) yd range", r.get("range") or "")
                name = sp["name"]
                resource = "energy" if "Energy" in cost_txt else ("rage" if "Rage" in cost_txt else ("mana" if "Mana" in cost_txt or "base mana" in cost_txt else "none"))
                s = Spell(name=name, school=(r.get("school") or "nature").lower(), rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")),
                          range=_num(rm.group(1)) if rm else 5.0, coef=coefs.get("direct", 0.0), resource=resource,
                          tags=("cost_pct",) if "base mana" in cost_txt else ())
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                pc, rk, po, fv, on, ex, he, ho, dm, mf, cp, fa = (rx.search(txt) for rx in (PCT, RAKE, POUNCE, FIVE, ONE, EXTRA, HEAL, HOT, DMG, MOONFIRE, CP, FORM_AP))
                if name in CAT:
                    s.kind, s.school = "melee", "physical"
                    if pc:
                        s.weapon_pct, s.dmg_min, s.dmg_max = float(pc.group(1)) / 100, _num(pc.group(2)), _num(pc.group(2))
                    if rk:
                        s.dmg_min = s.dmg_max = _num(rk.group(1))
                        s.dot, s.dot_dur, s.dot_ticks = _num(rk.group(2)), float(rk.group(3)), 3
                    if po:
                        s.stun, s.dot, s.dot_dur, s.dot_ticks = float(po.group(1)), _num(po.group(2)), float(po.group(3)), 6
                    if fv and on:
                        s.five = (_num(fv.group(1)), _num(fv.group(2)) if fv.group(2) else _num(fv.group(1)))
                        s.one = (_num(on.group(1)), _num(on.group(2)) if on.group(2) else _num(on.group(1)))
                        s.combo = -1
                        if fv.group(3):
                            s.dot_dur, s.dot_ticks = float(fv.group(3)), 6
                        else:
                            s.dmg_min, s.dmg_max = s.five
                    if ex:
                        s.extra_energy = float(ex.group(1))
                    if cp:
                        s.combo = int(cp.group(1))
                    if name in ("Tiger's Fury", "Prowl", "Dash", "Cower"):
                        s.kind = "buff"
                elif he:
                    s.kind, s.heal_min, s.heal_max, s.heal_coef = "heal", _num(he.group(1)), _num(he.group(2)), coefs.get("heal", 0.0)
                    if he.group(3):
                        s.hot, s.hot_dur = _num(he.group(3)), float(he.group(4))
                elif ho:
                    s.kind, s.hot, s.hot_dur, s.heal_coef = "heal", _num(ho.group(1)), float(ho.group(2)), coefs.get("per tick", 0.0)
                elif mf:
                    s.dmg_min, s.dmg_max = _num(mf.group(1)), _num(mf.group(2))
                    s.dot, s.dot_dur, s.dot_ticks, s.dot_coef = _num(mf.group(3)), float(mf.group(4)), 4, coefs.get("per tick", 0.0)
                elif name == "Insect Swarm" and SWARM.search(txt):
                    sw = SWARM.search(txt)
                    s.dot, s.dot_dur, s.dot_ticks, s.dot_coef = _num(sw.group(1)), float(sw.group(2)), 6, coefs.get("per tick", 0.0)
                elif dm:
                    s.dmg_min, s.dmg_max = _num(dm.group(1)), _num(dm.group(2))
                if fa and name in FORMS:
                    s.kind, s.form_ap = "buff", float(fa.group(1))
                    am, hm = FORM_ARMOR.search(txt), FORM_HP.search(txt)
                    s.form_armor_pct = float(am.group(1)) if am else 0.0
                    s.form_hp = _num(hm.group(1)) if hm else 0.0
                if name in BEAR:
                    s.school = "physical"
                    ma, sw, ro, st = MAUL.search(txt), SWIPE.search(txt), ROAR.search(txt), STUN.search(txt)
                    if name == "Maul" and ma:
                        s.kind, s.on_next_swing, s.weapon_pct, s.dmg_min, s.dmg_max = "melee", True, 1.0, _num(ma.group(1)), _num(ma.group(1))
                    elif name == "Swipe" and sw:
                        s.kind, s.dmg_min, s.dmg_max = "melee", _num(sw.group(1)), _num(sw.group(1))
                    elif name == "Primal Bite" and pc:
                        s.kind, s.weapon_pct, s.dmg_min, s.dmg_max = "melee", float(pc.group(1)) / 100, _num(pc.group(2)), _num(pc.group(2))
                    elif name == "Bash" and st:
                        s.kind, s.stun = "melee", float(st.group(1))
                    elif name == "Demoralizing Roar" and ro:
                        s.kind, s.roar_ap, s.roar_dur = "buff", float(ro.group(1)), float(ro.group(2))
                    else:
                        s.kind = "buff"
                if name in ("Mark of the Wild", "Thorns", "Nature's Swiftness", "Innervate", "Berserk", "Barkskin", "Omen of Clarity", "Faerie Fire", "Cat Form", "Bear Form", "Dire Bear Form", "Travel Form"):
                    s.kind = "buff"
                if name == "Feral Charge":
                    s.kind, s.charge, s.root, s.resource, s.cost = "buff", True, 4.0, "none", 0.0
                # 2026-10-09 (module_lint): these parsed to no damage, and Entangling Roots to no root, so casting it did nothing
                if name == "Entangling Roots" and ROOTS.search(txt):
                    er = ROOTS.search(txt)
                    s.dot, s.dot_dur = _num(er.group(1)), float(er.group(2))
                    s.dot_ticks, s.dot_coef, s.root = max(1, int(round(s.dot_dur / 3.0))), coefs.get("per tick", 0.0), s.dot_dur
                if name == "Hurricane" and STORM.search(txt):   # a channelled storm on the target's area (no druid rotation casts it)
                    hu = STORM.search(txt)
                    per, every = _num(hu.group(1)), float(hu.group(2))
                    dur = float(hu.group(3)) if hu.group(3) else 10.0
                    s.kind, s.channel, s.aoe = "channel", dur, True
                    s.dot, s.dot_dur, s.dot_ticks, s.dot_coef = per * dur / every, dur, max(1, int(dur / every)), coefs.get("per tick", 0.0)
                if name == "Lacerate" and LACERATE.search(txt):   # a bear bleed from 42 (the bear levels at 10-19 only): the base bleed, no stacks
                    la = LACERATE.search(txt)
                    s.kind, s.school = "melee", "physical"
                    s.dot, s.dot_dur = _num(la.group(1)), float(la.group(2))
                    s.dot_ticks = max(1, int(round(s.dot_dur / 3.0)))
                if name == "Shifting Power":   # a cat talent since 70170 (where King of the Jungle was): mana into energy
                    en = ENERGIZE.search(txt)
                    s.kind, s.energize = "buff", (float(en.group(1)) if en else 0.0)
                book.setdefault(name, []).append(s)
    for name in book:
        book[name].sort(key=lambda x: (x.level, x.rank))
    return book


BOOK = load_spellbook()

# Tiger's Fury: removed (settled 2026-10-17). Blizzard's beta notes of 1 Oct (t/2360696 post 4): "Tiger's Fury has been removed." The
# 70425 spellbook exports lack it and talentsforever.com's 70425 export lists it under "gone" ("In the spellbooks: Tiger's Fury is gone").
# In the client, SkillLineAbility moved spell 5217 from AcquireMethod 0 (trainer, build 69893) to 3 in 70170; in the 69893 table 3 marks
# spells never learned from the skill line: triggered effects (Pounce Bleed, Judgement of Righteousness), talent spells and the Season of
# Discovery runes this client carries unused (417045 Tiger's Fury, Mangle, Lacerate). The ElliotWood/Forever simulator reads 3 as "granted"
# and still casts it (sim/druid/tigers_fury.go). Until 2026-10-17 this module re-added it by hand (15% physical damage for 6 s, 30 s
# cooldown, the client's numbers for 5217); True restores that for a sensitivity run.
TIGERS_FURY = False
TIGERS_FURY_LEVEL, TIGERS_FURY_DURATION, TIGERS_FURY_COOLDOWN, TIGERS_FURY_BONUS = 24, 6.0, 30.0, 0.15
if TIGERS_FURY and "Tiger's Fury" not in BOOK:
    _tf = Spell(name="Tiger's Fury", school="physical", rank=1, level=TIGERS_FURY_LEVEL, cost=0.0, cast=0.0, cooldown=TIGERS_FURY_COOLDOWN,
                range=5.0, resource="none")
    _tf.kind = "buff"
    _tf.text = "Increases physical damage done by 15% for 6 sec."
    _tf.interrupt = parse_interrupt(_tf.text)
    BOOK["Tiger's Fury"] = [_tf]

# Blizzard's 2 Nov notes (client 70753): "Rip / Rake / Ferocious Bite / Pounce: Base points and attack power scaling increased by about
# 25%", "Starfire: Base damage points increased by about 40%". The client's tooltips (talentsforever's 70753 export, 2026-11-03) still
# carry the numbers they have had since 70291 (foreverchanges.pro lists them as what these spells "dealt"; the raid simulator's spell
# store the same), so the change is server-side: scale every rank by the notes' factor while the top rank still reads the old number
# (OLD_TOP). A data refresh that brings the new tooltips switches the scaling off by itself. "About": the factors are the notes' round
# numbers, an assumption until in-game numbers or client data confirm them.
BASE_70753 = {"Rip": 1.25, "Rake": 1.25, "Ferocious Bite": 1.25, "Pounce": 1.25, "Starfire": 1.40}
OLD_TOP = {"Rip": (243.0, 243.0), "Ferocious Bite": (199.0, 259.0), "Rake": (61.0, 61.0), "Pounce": (150.0, 150.0), "Starfire": (350.0, 412.0)}
# Attack power shares (never in a tooltip): the raid simulator's spell store before 70753 (Rip 1% a tick a combo point over 6 ticks, at
# most 4 points; Ferocious Bite 3% a combo point; Rake 5.5% a tick over 3 ticks, which this lab lacked until 2026-11-03; Pounce none), times
# the notes' 1.25.
RIP_AP_PER_CP = 0.06 * 1.25
BITE_AP_PER_CP = 0.03 * 1.25
RAKE_AP_PER_TICK = 0.055 * 1.25
# Poised (baseline passive from 32, client 70753): "When you are not in combat and have your maximum Energy, you will gain Poised. Poised
# reduces the Energy cost of your next Energy ability by 10." The druid starts a fight in Cat Form at full energy after resting: the opener
# costs 10 less (final_cost).
POISED_CUT = 10.0


def _apply_70753(book):
    for name, f in BASE_70753.items():
        ranks = book.get(name) or []
        if not ranks:
            continue
        top = ranks[-1]
        old = OLD_TOP[name]
        cur = getattr(top, "one", None) if name in ("Rip", "Ferocious Bite") else ((top.dot, top.dot) if name == "Pounce" else (top.dmg_min, top.dmg_max))
        if cur is None or (round(cur[0]), round(cur[1])) != (round(old[0]), round(old[1])):
            continue   # the tooltip moved: the data carries the change (or another one): no scaling
        for r in ranks:
            r.dmg_min, r.dmg_max, r.dot = r.dmg_min * f, r.dmg_max * f, r.dot * f
            if getattr(r, "one", None):
                r.one = (r.one[0] * f, r.one[1] * f)
            if getattr(r, "five", None):
                r.five = (r.five[0] * f, r.five[1] * f)
            r.scaled_70753 = f
    for r in book.get("Rake") or []:
        r.dot_coef = RAKE_AP_PER_TICK   # engine.apply_periodic: dot_coef x attack power x ticks for a melee dot


_apply_70753(BOOK)

# Rip before Ferocious Bite (levels 20-31): the only finisher, so it goes on at this many combo points while the mob has more than
# this share of its health left. The old rule (5 points above half health) never fired at 20 or 30. 2026-10-09 smoke test (1,500
# fights, seed 1, tuned drink rule): 2 points above 40% was the best of 1-5 points and 0-60% health, and against the old rule 3% faster
# per kill at 30 for leveling-feral (0.3% at 20, noise) and 6-7% at 20 and 30 for restoration-leveling. ROTATION_KNOBS lets
# rotation_opt.py tune both.
RIP_EARLY_CP = 2
RIP_EARLY_HP = 0.4
# Shifting Power only above this share of mana; 1.01 = never. 2026-10-09 smoke test (a leveling-feral variant with Shredding Attacks,
# Shifting Power and Improved Shifting Power, level 60, 1,500 fights): above 50% 38.1 s per kill, 65% 37.4, 80% 35.4, 95% 34.4, never
# 33.9: solo, the mana comes back as drinking time (about 600 mana a cast) and costs more than the 40 energy saves. A raid's mana
# buffs change that (the raid rotation casts it at 60 energy or less).
SHIFTING_POWER_ABOVE = 1.01
SHIFTING_POWER_CD = 8.0   # 70707 hotfix of 2026-10-30 (foreverchanges.pro, wowforever.be): 8 s, was 16 s
# Omen of Clarity: the client states no rate; the ElliotWood/Forever simulator fits beta logs at 2 procs a minute (4% a hit in Cat Form,
# 8% in Bear Form; spells by their cast time, instants by a 1.5 s global cooldown) outside the client's 10 s internal cooldown, which
# Moonkin Form halves (and doubles the chance: its tooltip). Clearcasting lasts 15 s.
OMEN_PPM = 2.0
OMEN_ICD = 10.0
OMEN_MOONKIN_ICD = 0.5
CLEARCASTING_DURATION = 15.0
THORNS_COEF = 0.06   # Thorns' spell power ratio (beta notes 2026-10-08: "reduced to 6% (was 13.3%)")


def talent_numbers():
    out = {}
    for tr in TREE["trees"]:
        for t in tr["talents"]:
            out[t["name"]] = [[float(x) for x in NUM.findall((rank or "").replace(",", ""))] for rank in t["ranks"]]
    return out


TNUM = talent_numbers()

MECHANICS = {
    "Ferocity": "-1 energy/rank on Claw and Rake, -1 rage/rank on Maul, Swipe and Primal Bite",
    "Heart of the Wild": "+2%/rank Intellect, +2%/rank Strength in Cat Form, +4%/rank Stamina in Bear Form",
    "Feral Swiftness": "+2%/rank dodge",
    "Feral Instinct": "+10%/rank Swipe (bear, not used single-target) and stealth: no effect here",
    "Brutal Impact": "+0.5 s/rank Pounce and Bash stun, -15 s/rank Bash cooldown",
    "Thick Hide": "+1 base armor per level per rank in Cat, Bear and Moonkin Form, times the form's armor multiplier",
    "Savage Fury": "+5%/rank Claw, Rake, Shred, Maul, Swipe",
    "Feral Charge": "cat / bear: charge that roots and interrupts a casting mob (4 s)",
    "Sharpened Claws": "+3%/rank crit in forms",
    "Shredding Attacks": "-6 energy/rank Shred (used only in the opener from behind)",
    "Primal Bite": "bear (levels 10-19): 100% weapon damage plus a bonus for 20 rage every 6 s",
    "Predatory Strikes": "+50%/rank of your level as attack power in forms",
    "Blood Frenzy": "bear: 50%/rank chance of 5 rage on a critical strike; cat: 50%/rank chance of an extra combo point on a critical Claw, Rake, Shred or Ravage",
    "Natural Instinct": "+10%/rank crit damage bonus on abilities; healing power +12/25% of Intellect",
    "Leader of the Pack": "+3% crit in forms",
    "Shifting Power": "cat: 40 energy for 55% of base mana (less with Natural Shapeshifter) every 8 s (the 70707 hotfix; 16 s before, Improved Shifting Power took 4 s a rank off until it was removed), at 60 energy or less, above "
                      "SHIFTING_POWER_ABOVE of mana (default never: solo its mana costs more drinking time than the energy saves) and "
                      "keeping the mana for an emergency heal and the way back (70170 put it where King of the Jungle was)",
    "Natural Reaction": "+1%/rank dodge",
    "Rend and Tear": "+3%/rank ability damage on a bleeding mob (Rake, Rip, Pounce; the tooltip's number, 3% a rank since client 70753)",
    "Genesis": "+1%/rank periodic damage (Rake, Rip, Pounce, Moonfire) and healing",
    "Nature's Majesty": "+2%/rank crit with spells and melee",
    "Nature's Reach": "+2%/rank hit",
    "Moonglow": "caster form only",
    "Improved Moonfire": "Balance: +5%/rank Moonfire damage and critical strike chance (cat: no Moonfire)",
    "Improved Wrath": "Balance: -0.1 s/rank Wrath cast, -10%/rank mana (cat: not used)",
    "Vengeance": "Balance: +20%/rank Arcane / Nature crit damage bonus",
    "Moonfury": "Balance: +2%/rank Arcane / Nature damage",
    "Nature's Grace": "Balance: a critical hit from a non-periodic damage spell gives 10% faster casts and a 10% shorter global cooldown for 3 s",
    "Insect Swarm": "Balance: a Nature DoT kept up",
    "Improved Starfire": "Balance: -0.1 s/rank Starfire cast, 3%/rank chance of a 3 s stun",
    "Eclipse": "Balance: each Wrath stores 2 charges (up to 4, 15 s); each charge takes 0.17/0.33/0.5 s (by rank) off one Starfire",
    "Moonkin Form": "Balance: +360% armor from items from 40, +3% spell crit while in the form, Omen of Clarity twice as likely; healing spells need you out of the form "
                    "(35% of base mana to go back); between fights a Moonkin eats instead of shifting out to heal",
    "Nature's Splendor": "Moonfire and Rejuvenation +3 s, Regrowth +6 s, Insect Swarm +2 s: one or two more ticks of the same size",
    "Furor": "Cat Form: back in with 20%/rank of the energy you left with plus 2/rank energy a second out of form (at most 20/rank); "
             "Bear Form: 20%/rank chance of 10 rage (expected value)",
    "Naturalist": "+1%/rank all damage, -0.1 s/rank Healing Touch",
    "Natural Shapeshifter": "-10%/rank shapeshift mana",
    "Reflection": "17%/rank mana regen while casting",
    "Gift of Nature": "+2%/rank heals",
    "Improved Rejuvenation": "+5%/rank Rejuvenation",
    "Tranquil Spirit": "-2%/rank Healing Touch mana",
    "Nature's Swiftness": "instant Healing Touch every 3 min when low",
    "Living Spirit": "+5%/rank Spirit",
    "Swiftmend": "instant heal of a running Rejuvenation / Regrowth",
    "Subtlety": "threat only",
    "Nature's Focus": "14%/rank chance to ignore pushback on Arcane and Nature spells (Wrath, Starfire, the heals)",
}
FIT = {
    "Ferocity": "scale", "Heart of the Wild": "scale", "Feral Swiftness": "scale", "Brutal Impact": "scale", "Thick Hide": "scale", "Savage Fury": "scale",
    "Sharpened Claws": "scale", "Shredding Attacks": "scale", "Predatory Strikes": "scale", "Natural Instinct": "scale", "Leader of the Pack": "scale",
    "Shifting Power": "scale", "Natural Reaction": "scale", "Rend and Tear": "scale", "Genesis": "scale", "Nature's Majesty": "scale",
    "Nature's Reach": "scale", "Furor": "scale", "Naturalist": "scale", "Natural Shapeshifter": "scale", "Reflection": "scale", "Gift of Nature": "scale",
    "Improved Rejuvenation": "scale", "Tranquil Spirit": "scale", "Nature's Swiftness": "scale", "Living Spirit": "scale", "Swiftmend": "scale", "Blood Frenzy": "scale",
    "Feral Charge": "scale", "Feral Instinct": "scale", "Moonglow": "scale", "Improved Moonfire": "scale", "Improved Wrath": "scale", "Nature's Focus": "scale",
}
SHARE_SOURCE = {"Melee": "white", "Shred": "shred", "Ferocious Bite": "ferocious_bite", "Rip": "rip", "Claw": "claw_rake", "Rake": "claw_rake", "Ravage": "shred",
                "Pounce": "claw_rake"}
NEW_SOURCES = {}
KEY_TALENTS = ["Predatory Strikes", "Savage Fury", "Sharpened Claws"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level. Levels 10-19 in Bear Form: walk up, Enrage, Demoralizing Roar, Maul on every swing "
               "the rage allows, Bash when low or against a casting mob. From 20 in Cat Form: prowl up behind the mob and open with Ravage from 32 (Shred from 22, "
               "Claw before; Pounce comes at 36, after Ravage), Rake once, Claw to five points (the mob faces you, so Shred is only for the "
               "opener), Ferocious Bite whenever it kills (from 32), Rip at five points on a mob above half health (before Ferocious Bite: Rip at "
               f"{RIP_EARLY_CP} points on a mob above {RIP_EARLY_HP:.0%} of its health), Berserk on the pull; when low, shift out for a Regrowth (Nature's Swiftness "
               "+ Healing Touch in an emergency) and shift back at 55% of base mana, Furor carrying the energy. Between fights: 2 s loot, 6 s travel, Rejuvenation / "
               "Regrowth in caster form when hurt (only with the mana to shift back) then Cat Form again, water below 35% mana (the tuned rule drinks lower).")
NOT_MODELLED = ("levels 1-9 (Wrath / Moonfire), Moonfire / Wrath pulls in bear levels, Faerie Fire, Swipe, Growl, Dash, Innervate, Barkskin, Hurricane, "
                "Lacerate's stacks, adds, gear upgrades within a level bracket.")
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'balance-dps', 'opt': 'opt-balance-dps-leveling-st', 'tag': 'bal', 'profile': 'leveling-st', 'lookahead': 16, 'sets': [],
                          'levels': '20,30,40,50,60', 'calibrate_levels': '30,60', 'label': 'Balance (its own rotation)', 'report': 'balance-dps-opt'}],
            "spec": "feral-cat-dps", "hand": "leveling-feral", "opt": "opt-feral-cat-dps-leveling-st", "tag": "cat", "lookahead": 16,
            "levels": "15,20,30,40,50,60", "calibrate_levels": "15,30,60",
            "extra_reports": [{"spec": "balance-dps", "build": "opt-balance-dps-leveling-st", "compare": ["opt-feral-cat-dps-leveling-st"]}]}


class DruidModule(BaseModule):
    resource = "energy"
    melee = True
    RIP_EARLY_CP = RIP_EARLY_CP   # Rip before Ferocious Bite: at this many combo points ...
    RIP_EARLY_HP = RIP_EARLY_HP   # ... while the mob has more than this share of its health
    SHIFTING_POWER_ABOVE = SHIFTING_POWER_ABOVE   # Shifting Power only above this share of mana (1.01: never; see the module constant)
    ROTATION_KNOBS = {"RIP_EARLY_CP": [2, 3, 4, 5], "RIP_EARLY_HP": [0.0, 0.25, 0.4, 0.5],
                      "SHIFTING_POWER_ABOVE": [0.5, 0.65, 0.8, 0.95, 1.01]}   # tuned by rotation_opt.py (1.01: never)

    def __init__(self, talents, level, spec="feral-cat-dps", gear="leveling"):
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
        self.balance = spec.startswith("balance")
        self.form = "caster" if self.balance else ("cat" if "Cat Form" in self.spells else ("bear" if "Bear Form" in self.spells else "caster"))
        self.form_spell = self.spells.get("Cat Form") if self.form == "cat" else self.spells.get("Bear Form")
        self.in_cat = self.form != "caster"     # "in form" (cat or bear); the name is historical
        self.moonkin = self.balance and "Moonkin Form" in self.spells
        self.resource = "rage" if self.form == "bear" else ("mana" if self.balance else "energy")
        self.opened = False
        self.armor_spell_used = {"cat": "Cat Form", "bear": "Bear Form"}.get(self.form, "caster")
        self.in_moonkin = self.moonkin       # Moonkin Form is up from the first pull; an emergency heal leaves it
        self._moonkin_armor = 0.0
        self._cat_exit = None                # (time, energy) when Cat Form was last left: Furor
        self._omen_ready = 0.0               # Omen of Clarity's internal cooldown
        self._apply_splendor()

    def _apply_splendor(self):
        """Nature's Splendor: Moonfire, Rejuvenation, Regrowth and Insect Swarm last longer; the extra time adds ticks of the same size
        (this module's own copies: BOOK is shared)."""
        if not self.rank("Nature's Splendor"):
            return
        text = next((t["ranks"][0] for tr in TREE["trees"] for t in tr["talents"] if t["name"] == "Nature's Splendor"), "")
        for name in ("Moonfire", "Rejuvenation", "Regrowth", "Insect Swarm"):
            mt = re.search(rf"{name}(?: and [A-Z][\w' ]+?)? spells? by ([\d.]+) sec", text)
            s = self.spells.get(name)
            if not mt or s is None:
                continue
            extra = float(mt.group(1))
            s = copy.copy(s)
            if s.dot > 0 and s.dot_ticks > 0 and s.dot_dur > 0:
                every = s.dot_dur / s.dot_ticks
                n = max(1, int(round(extra / every)))
                s.dot += s.dot / s.dot_ticks * n
                s.dot_ticks += n
                s.dot_dur += n * every
            if s.hot > 0 and s.hot_dur > 0:
                s.hot *= (s.hot_dur + extra) / s.hot_dur
                s.hot_dur += extra
            self.spells[name] = s
            self.book[name] = s

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
        return sorted(n for n in self.t if n not in MECHANICS)

    def rank_at(self, name):
        ranks = [s for s in BOOK.get(name, []) if s.level <= self.level]
        return self.scale_rank(ranks[-1]) if ranks else None   # the rank at this level (row 8)

    # ------------------------------------------------------------ character
    def make_player(self, level):
        base = class_base_stats("druid", level)
        g = gear_stats(level, self.gear, "druid-caster" if self.balance else "druid")   # caster row for Balance (audit 2026-10-18 row 65)
        # Mark of the Wild, self-cast and kept up (an hour: recast between pulls, its mana not counted) like its armor before: "armor by 385,
        # all attributes by 16" at rank 7. Until 2026-10-18 only the armor counted (audit 2 row 4: about +8% cat attack power at 60).
        motw = self.book.get("Mark of the Wild")
        mm = re.search(r"armor by (\d+)", motw.text) if motw else None
        ma = re.search(r"all attributes by (\d+)", motw.text) if motw else None
        attr = _num(ma.group(1)) if ma else 0.0
        # Heart of the Wild's tooltip: Intellect, then Stamina in Bear Form, then Strength in Cat Form (numbers 0, 1, 2)
        strength = (base["strength"] + g["strength"] + attr) * (1 + self.tv("Heart of the Wild", 2) / 100 if self.form == "cat" else 1.0)
        agility = base["agility"] + g["agility"] + attr
        stamina = (base["stamina"] + g["stamina"] + attr) * (1 + self.tv("Heart of the Wild", 1) / 100 if self.form == "bear" else 1.0)
        intellect = (base["intellect"] + g["intellect"] + attr) * (1 + self.tv("Heart of the Wild", 0) / 100)
        spirit = (base["spirit"] + g["spirit"] + attr) * (1 + self.tv("Living Spirit", 0) / 100)
        # the animal form's own numbers (a Balance druid's form_spell is Bear Form, never used: no form stats; they had read 0 until 2026-10-18)
        form = self.form_spell if self.form in ("cat", "bear") else None
        moonkin_pct = self.tv("Moonkin Form", 1) / 100 if self.moonkin else 0.0   # "Armor contribution from items by 360%"
        # Thick Hide (70425): "While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 1/2/3 additional base Armor per level
        # ... further increased by multipliers from those forms": inside the form's multiplier, nothing in caster form (until 2026-10-18 it
        # counted in caster form too and outside the multiplier: audit 2 row 24). The defense-skill half is 0 (no defense above 5 x level).
        in_form = self.moonkin if self.balance else self.form in ("cat", "bear")
        thick = level * self.tv("Thick Hide", 0) if in_form else 0.0
        self._moonkin_armor = (g["armor"] + thick) * moonkin_pct + thick if self.moonkin else 0.0   # what leaving Moonkin Form takes away
        self.in_moonkin = self.moonkin           # a new session (its clock starts again): fresh state
        self._cat_exit = None
        self._omen_ready = 0.0
        self._intellect, self._spell_power = intellect, g["spell_power"]   # Natural Instinct's healing (heal_multiplier)
        armor = (g["armor"] + thick) * (1 + (moonkin_pct if self.moonkin else getattr(form, "form_armor_pct", 0.0) / 100)) + (_num(mm.group(1)) if mm else 0.0)
        bm = class_base_mana("druid", level)
        cat = self.book.get("Cat Form")
        p = Player(level=level, hp_max=class_base_health("druid", level) + 10 * stamina + getattr(form, "form_hp", 0.0), hp=0.0, mana_max=bm + 15 * intellect, mana=0.0, base_mana=bm,
                   spirit=spirit, intellect=intellect, spell_power=g["spell_power"], armor=armor, spell_crit=class_spell_crit("druid", level, intellect),
                   dodge=class_dodge("druid", level, agility) + self.tv("Feral Swiftness", 1) / 100 + self.tv("Natural Reaction", 0) / 100, ranged_crit=0.0)
        p.strength, p.agility, p.stamina = strength, agility, stamina
        # Attack power (2026-10-18, audit 2 row 3): Agility gives a druid none outside Cat Form (client ChrClasses AttackPowerPerAgility 0;
        # tables.AP_PER_AGI had 1, so Cat Form counted it twice), and the forms' "Attack Power by 120" (Cat, Bear) / 180 (Dire Bear) is the
        # level-60 value of 2 / 3 x level (the ElliotWood/Forever simulator's forms.go: 2 x level for Cat Form, 3 x level for Dire Bear).
        # Before, the form numbers read 0 (FORM_AP), so a cat had +Agility - 2 x level and a bear no form attack power, armor or health.
        p.attack_power = class_attack_power("druid", level, strength, 0.0) + level * self.tv("Predatory Strikes", 0) / 100
        if self.form == "cat":
            p.attack_power += getattr(cat, "form_ap", 0.0) * level / 60 + agility
        elif self.form == "bear":
            p.attack_power += getattr(form, "form_ap", 0.0) * level / 60
        p.melee_crit = class_melee_crit("druid", level, agility) + self.tv("Sharpened Claws", 0) / 100 + (0.03 if self.rank("Leader of the Pack") else 0.0) + self.tv("Nature's Majesty", 0) / 100
        p.hit_bonus = self.tv("Nature's Reach", 1) / 100
        dps = weapon_dps(level, "2h") * 0.85   # a cat's paws: assumed 85% of a quest-green two-hander's dps at a 1.0 s swing (a bear's at 2.5 s)
        if self.form == "bear":
            self.paw = Weapon(dmg_min=dps * 2.5 * 0.8, dmg_max=dps * 2.5 * 1.2, speed=2.5, kind="paw")
            p.rage_max, p.rage = 100.0, 0.0
            p.energy_max = 0.0
        else:
            self.paw = Weapon(dmg_min=dps * 1.0 * 0.8, dmg_max=dps * 1.0 * 1.2, speed=1.0, kind="paw")
            p.energy_max = 100.0
            p.energy = p.energy_max
        p.mh = self.paw if self.form != "caster" else None
        if self.balance:
            p.energy_max = 0.0
            p.spell_crit += self.tv("Nature's Majesty", 0) / 100
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Reflection", 0) / 100
        self.in_cat = self.form != "caster"
        return p

    def pull_range(self):
        return 30.0 if self.balance else 20.0

    def shift_cost(self, p):
        form = self.form_spell
        return (form.cost / 100 * p.base_mana if form else 0.0) * (1 - self.tv("Natural Shapeshifter", 0) / 100)

    # Moonkin Form "prevents the use of healing spells": a heal leaves the form (free), going back costs the form's mana
    def moonkin_cost(self, p):
        mk = self.spells.get("Moonkin Form")
        if mk is None:
            return 0.0
        cost = mk.cost / 100 * p.base_mana if "cost_pct" in mk.tags else mk.cost
        return cost * (1 - self.tv("Natural Shapeshifter", 0) / 100)

    def leave_moonkin(self, fight):
        if self.in_moonkin:
            self.in_moonkin = False
            fight.note("leaves Moonkin Form to heal")

    def enter_moonkin(self, fight_or_none, p, t):
        cost = self.moonkin_cost(p)
        if p.mana < cost:
            return False
        p.mana -= cost
        p.fsr_until = t + 5.0
        self.in_moonkin = True
        if fight_or_none is not None:
            fight_or_none.note("Moonkin Form")
            fight_or_none.casts["Moonkin Form"] = fight_or_none.casts.get("Moonkin Form", 0) + 1
        return True

    def eclipse_charges(self, fight):
        e = fight.p.buff("Eclipse", fight.t) if fight else None
        return e.get("charges", 0) if e else 0

    def omen_roll(self, fight, seconds):
        """Omen of Clarity (from 20): a chance at Clearcasting on a landed attack or spell, OMEN_PPM procs a minute by the swing or cast
        time, outside the internal cooldown; Moonkin Form doubles the chance (its tooltip) and halves the cooldown (the client)."""
        if "Omen of Clarity" not in self.spells or fight.t < self._omen_ready:
            return
        moonkin = self.balance and self.in_moonkin
        chance = OMEN_PPM * seconds / 60.0 * ((1 + self.tv("Moonkin Form", 0) / 100) if moonkin else 1.0)
        if fight.rng.random() < chance:
            fight.p.buffs["Clearcasting"] = {"until": fight.t + CLEARCASTING_DURATION}
            self._omen_ready = fight.t + OMEN_ICD * (OMEN_MOONKIN_ICD if moonkin else 1.0)

    def base_cast(self, spell):
        """The cast time with the talents' flat cuts only (no haste, no Eclipse): what Omen of Clarity's rate reads."""
        c = spell.cast
        if spell.name == "Healing Touch":
            c = max(GCD, c - self.tv("Naturalist", 0))
        elif spell.name == "Wrath":
            c = max(GCD, c - self.tv("Improved Wrath", 0))
        elif spell.name == "Starfire":
            c = max(GCD, c - self.tv("Improved Starfire", 0))
        return c

    # ------------------------------------------------------------ engine hooks: numbers
    def mana_cost(self, spell):
        cost = spell.cost
        if "cost_pct" in spell.tags:
            cost = cost / 100 * self._base_mana
        if spell.name == "Wrath":
            cost *= 1 - self.tv("Improved Wrath", 1) / 100
        if spell.kind == "spell" and spell.school in ("arcane", "nature") and spell.dmg_max + spell.dot > 0:
            cost *= 1 - self.tv("Moonglow", 0) / 100
        if spell.name in ("Claw", "Rake", "Maul", "Swipe", "Primal Bite"):
            cost = max(0.0, cost - self.rank("Ferocity"))
        if spell.name == "Shred":
            cost = max(0.0, cost - 6.0 * self.rank("Shredding Attacks"))
        if spell.name == "Healing Touch":
            cost *= 1 - self.tv("Tranquil Spirit", 0) / 100
        if spell.name == "Shifting Power":   # "cost is reduced by effects that reduce the cost of Shapeshifting"
            cost *= 1 - self.tv("Natural Shapeshifter", 0) / 100
        return cost

    def final_cost(self, fight, spell, cost):
        # Clearcasting: the next ability or spell that costs something is free; "Clearcasting is not consumed by Wrath" (Forever)
        if fight.p.buff("Clearcasting", fight.t) and spell.kind in ("melee", "heal", "spell") and cost > 0 and spell.name != "Wrath":
            del fight.p.buffs["Clearcasting"]
            return 0.0
        if spell.resource == "energy" and cost > 0 and fight.p.buffs.pop("Poised", None) is not None:
            return max(0.0, cost - POISED_CUT)
        return cost

    def cast_time(self, spell):
        """Stateless (the engine also calls it for pushback): flat talent cuts, Eclipse's cut by rank while it holds charges, Nature's
        Swiftness, then Nature's Grace's haste (10%, floored at its 10% shorter global cooldown)."""
        f = self._fight
        c = self.base_cast(spell)
        if spell.name == "Starfire" and self.rank("Eclipse") and self.eclipse_charges(f) > 0:
            c = max(GCD, c - self.tv("Eclipse", 1))
        if c > 0 and f and f.p.buff("Nature's Swiftness", f.t) and spell.school == "nature":
            return 0.0
        if c > 0 and f and self.rank("Nature's Grace") and f.p.buff("Nature's Grace", f.t):
            ng = self.tv("Nature's Grace", 0) / 100
            c = max(GCD * (1 - ng), c / (1 + ng))
        return c

    def crit_bonus(self, spell, frozen):
        f = self._fight
        bonus = 0.0
        if f and spell.combo > 0 and f.p.buff("Berserk", f.t):
            bonus += 1.0
        if spell.name == "Moonfire":
            bonus += self.tv("Improved Moonfire", 0) / 100   # "damage and critical strike chance of your Moonfire spell"
        if self.balance and self.in_moonkin and spell.kind == "spell":   # Moonkin Form's aura: "spell Critical Strike chance increased by 3%" (until 2026-10-17 left out)
            bonus += self.tv("Moonkin Form", 3) / 100
        return bonus

    def crit_damage_bonus(self, spell):
        if spell.kind == "melee" and spell.name != "Melee":
            return self.tv("Natural Instinct", 0) / 100
        if spell.kind == "spell" and spell.school in ("arcane", "nature"):
            return self.tv("Vengeance", 0) / 100 * 0.5   # +100% of the 50% crit bonus = +50% damage on a crit
        return 0.0

    def damage_multiplier(self, spell, frozen):
        m = 1 + self.tv("Naturalist", 1) / 100
        if spell.kind == "spell" and spell.school in ("arcane", "nature"):
            m *= 1 + self.tv("Moonfury", 0) / 100
            if spell.name == "Moonfire":
                m *= 1 + self.tv("Improved Moonfire", 0) / 100
        f = self._fight
        if f and spell.school == "physical" and f.p.buff("Tiger's Fury", f.t):
            m *= 1 + TIGERS_FURY_BONUS
        if spell.name in ("Claw", "Rake", "Shred", "Maul", "Swipe"):
            m *= 1 + self.tv("Savage Fury", 0) / 100
        if spell.kind == "melee" and spell.name != "Melee" and f and (f.dot_active("Rake") or f.dot_active("Rip") or f.dot_active("Pounce")):
            m *= 1 + self.tv("Rend and Tear", 0) / 100
        if spell.name == "Ferocious Bite" and f:
            cp = max(1, f.last_combo)
            lo1, hi1 = spell.one
            lo5, hi5 = spell.five
            avg = (lo1 + hi1) / 2 + ((lo5 + hi5) / 2 - (lo1 + hi1) / 2) * (cp - 1) / 4 + BITE_AP_PER_CP * cp * f.p.attack_power + getattr(spell, "extra_energy", 0.0) * getattr(f, "_bite_extra", 0.0)
            m *= avg / ((lo5 + hi5) / 2)
        return m

    def periodic_multiplier(self, spell):
        return self.damage_multiplier(spell, False) * (1 + self.tv("Genesis", 0) / 100)

    def heal_multiplier(self, spell):
        m = (1 + self.tv("Gift of Nature", 0) / 100) * (1 + self.tv("Genesis", 0) / 100 if spell.hot > 0 else 1.0)
        if spell.name == "Rejuvenation":
            m *= 1 + self.tv("Improved Rejuvenation", 0) / 100
        # Natural Instinct's second half (70425): "increases your spell healing by 12/25% of your Intellect": healing power the engine has
        # no slot for, so the heal's mean is scaled by its gain (until 2026-10-18 left out: audit 2 row 24)
        ni = self.tv("Natural Instinct", 1) / 100 * getattr(self, "_intellect", 0.0)
        if ni > 0 and spell.heal_coef > 0:
            sp = getattr(self, "_spell_power", 0.0)
            ticks = max(1, int(spell.hot_dur / 3.0)) if spell.hot > 0 else 0
            direct = 1 if spell.heal_max > 0 else 0
            mean = direct * ((spell.heal_min + spell.heal_max) / 2 + spell.heal_coef * sp) + (spell.hot + spell.heal_coef * sp * ticks if ticks else 0.0)
            if mean > 0:
                m *= 1 + spell.heal_coef * ni * (direct + ticks) / mean
        return m

    def periodic_can_crit(self, spell):
        return True

    def mana_regen(self, p, t):
        return class_mana_regen_tick("druid", p.spirit)

    def health_regen(self, p):
        return class_health_regen_tick("druid", p.spirit)

    def pushback_resisted(self, fight, spell):
        # Nature's Focus (Forever): "avoid interruption caused by damage while casting Arcane and Nature spells", damage spells included
        if self.rank("Nature's Focus") and spell.school in ("arcane", "nature") and spell.kind in ("spell", "heal", "channel"):
            return fight.rng.random() < self.tv("Nature's Focus", 0) / 100
        return False

    def attacks_from_front(self):
        return self.opened or self.balance

    def on_hit_taken(self, fight, dmg, crit=False):
        # Thorns (2026-10-18, audit 2 row 4): self-cast and kept up (10 min; its mana not counted), "causing 18 Nature damage to attackers
        # when hit" at rank 6 plus 6% of spell power (Blizzard's beta notes of 8 Oct; the ElliotWood/Forever simulator's
        # ThornsSpellPowerCoefficient); melee hits only (a caster mob's bolt at range does not trigger it), no crit
        th = self.book.get("Thorns")
        m = fight.m
        if th is None or not m.in_melee or m.hp <= 0:
            return
        val = re.search(r"causing (\d+) Nature damage", th.text)
        if val:
            spell = Spell("Thorns", "nature")
            fight.deal(spell, (float(val.group(1)) + THORNS_COEF * fight.p.spell_power) * self.damage_multiplier(spell, False))

    # ------------------------------------------------------------ forms
    def shift_out(self, fight):
        p = fight.p
        if self.form == "cat" and self.in_cat:
            self._cat_exit = (fight.t, p.energy)
            p.buffs.pop("Tiger's Fury", None)   # leaving Cat Form ends Tiger's Fury
        self.in_cat = False
        p.mh = None
        fight.note(f"shifts out of {self.form_spell.name if self.form_spell else 'form'}")

    def armor_bonus(self):
        f = self._fight
        bonus = 0.0
        if f and self.form == "bear" and f.p.buff("Enrage", f.t):
            bonus -= 0.27 * f.p.armor
        if self.moonkin and not self.in_moonkin:
            bonus -= self._moonkin_armor   # out of Moonkin Form after a heal: no armor bonus from the form
        return bonus

    def furor_energy(self, p, t):
        """Energy on entering Cat Form (Forever's Furor): a share of the energy you left the form with plus some per second out of it,
        up to a cap (20%, 2 a second and 20 a rank: tooltip numbers 2, 3 and 4; number 1 is the bear's 10 rage). None without Furor."""
        if not self.rank("Furor"):
            return 0.0
        left_t, left_e = self._cat_exit if self._cat_exit else (t, p.energy)
        carry = left_e * self.tv("Furor", 2) / 100 + self.tv("Furor", 3) * max(0.0, t - left_t)
        return min(self.tv("Furor", 4), carry, p.energy_max)

    def on_regen_tick(self, fight, p, t):
        en = p.buff("Enrage", t)
        if en and en.get("left", 0) > 0:
            gain = min(4.0, en["left"])
            en["left"] -= gain
            p.rage = min(p.rage_max, p.rage + gain)

    def shift_in(self, fight_or_none, p, t):
        cost = self.shift_cost(p)
        if p.mana < cost:
            return False
        p.mana -= cost
        p.fsr_until = t + 5.0
        if self.form == "bear":
            p.rage = min(p.rage_max, p.rage + self.tv("Furor", 1) * self.tv("Furor", 0) / 100)   # expected value of the rage chance
        else:
            p.energy = self.furor_energy(p, t)
        self.in_cat = True
        p.mh = self.paw
        name = self.form_spell.name if self.form_spell else "form"
        if fight_or_none is not None:
            fight_or_none.note(name)
            fight_or_none.casts[name] = fight_or_none.casts.get(name, 0) + 1
        return True

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        self._base_mana = fight.p.base_mana
        p, m, t = fight.p, fight.m, fight.t
        self.opened = False
        if self.balance:
            if self.moonkin and not self.in_moonkin:
                self.enter_moonkin(fight, p, t)   # back into Moonkin Form before the pull when the mana allows
            return
        if not self.in_cat:
            if not self.shift_in(fight, p, t):
                self.in_cat = False
        p.buffs.pop("Poised", None)
        if self.in_cat and self.form == "cat" and self.book.get("Poised") is not None and p.energy >= p.energy_max > 0:
            p.buffs["Poised"] = {"until": t + 3600.0}   # rested to full energy out of combat: the opener costs 10 less
        if self.in_cat and self.form == "cat":
            m.dist = MELEE_RANGE          # prowled up behind the mob
            m.in_melee = True
            m.swing_at = t + 1.5
            p.swing_mh = t + 0.5
        elif self.form == "bear":
            self.opened = True            # no stealth opener: the bear walks up
        bs = self.spells.get("Berserk")
        if bs is not None and p.ready("Berserk", t) and self.in_cat:
            p.buffs["Berserk"] = {"until": t + 15.0}
            p.cooldowns["Berserk"] = t + bs.cooldown

    def on_swing(self, fight, spell, outcome, amount, hand):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name in ("Ravage", "Pounce", "Shred", "Claw") and not self.opened:
            self.opened = True
        if outcome in ("miss", "dodge", "parry"):
            return
        if p.mh is not None:
            self.omen_roll(fight, p.mh.speed)   # white hits and abilities alike, by the form's swing
        if outcome == "crit" and self.form == "bear" and self.rank("Blood Frenzy") and fight.rng.random() < self.tv("Blood Frenzy", 0) / 100:
            p.rage = min(p.rage_max, p.rage + self.tv("Blood Frenzy", 1))
        # Blood Frenzy's cat half: "your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 50%/100%
        # chance to add an additional Combo Point"
        if (outcome == "crit" and self.form == "cat" and spell.combo > 0 and amount > 0 and self.rank("Blood Frenzy")
                and fight.rng.random() < self.tv("Blood Frenzy", 2) / 100):
            p.combo = min(5, p.combo + 1)
        if spell.name == "Rip" and amount == 0:
            cp = max(1, fight.last_combo)
            lo1, _ = spell.one
            lo5, _ = spell.five
            # attack power: 1% a combo point a tick over 6 ticks, no more above 4 points (Classic's rule, as the raid simulator has it), x1.25
            # since the 2 Nov notes (RIP_AP_PER_CP)
            total = (lo1 + (lo5 - lo1) * (cp - 1) / 4 + RIP_AP_PER_CP * min(cp, 4) * p.attack_power) * self.periodic_multiplier(spell)
            fight.refresh_dot("Rip", total, 6, spell.dot_dur / 6.0, p.melee_crit, 2.0)

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        if spell.kind in ("spell", "heal"):
            self.omen_roll(fight, self.base_cast(spell) or GCD)   # spells by their cast time, instants by the global cooldown
        if self.balance and spell.kind == "spell":
            # Nature's Grace (Forever): any critical non-periodic damage spell, 10% faster casts and global cooldown for 3 s
            if crit and amount > 0 and self.rank("Nature's Grace"):
                p.buffs["Nature's Grace"] = {"until": t + self.tv("Nature's Grace", 1)}
            if spell.name == "Starfire" and self.rank("Improved Starfire") and fight.rng.random() < self.tv("Improved Starfire", 1) / 100:
                m.stun_until = max(m.stun_until, t + self.tv("Improved Starfire", 2))
        if spell.name == "Tiger's Fury":
            p.buffs["Tiger's Fury"] = {"until": t + TIGERS_FURY_DURATION}
        if spell.name == "Shifting Power":
            p.energy = min(p.energy_max, p.energy + getattr(spell, "energize", 0.0))
        if spell.name == "Nature's Swiftness":
            p.buffs["Nature's Swiftness"] = {"until": t + 60.0}
        if spell.kind == "heal" and spell.cast > 0 and p.buff("Nature's Swiftness", t):
            del p.buffs["Nature's Swiftness"]
        if spell.name in ("Pounce", "Bash") and spell.stun > 0:
            m.stun_until = max(m.stun_until, t + spell.stun + 0.5 * self.rank("Brutal Impact"))
        if spell.name == "Demoralizing Roar":
            m.dmg_reduction = spell.roar_ap / 14.0 * MOB_SWING
            m.dmg_reduction_until = t + spell.roar_dur
            m.debuffs["Demoralizing Roar"] = {"until": t + spell.roar_dur}
        if spell.name == "Enrage":
            p.rage = min(p.rage_max, p.rage + 10.0)
            p.buffs["Enrage"] = {"until": t + 10.0, "left": 20.0}

    def after_cast(self, fight, spell):
        p, t = fight.p, fight.t
        if spell.cooldown > 0 or spell.name == "Shifting Power":
            cd = SHIFTING_POWER_CD if spell.name == "Shifting Power" else spell.cooldown
            cut = 15.0 * self.rank("Brutal Impact") if spell.name == "Bash" else 0.0
            p.cooldowns[spell.name] = t + cd - cut
        if spell.name in ("Cat Form", "Bear Form"):
            self.shift_in(fight, p, t)
        if self.balance and self.rank("Eclipse"):
            # Eclipse: a completed Wrath stores 2 charges (up to 4, 15 s); a completed Starfire spends one (its cast time read the charge)
            e = p.buff("Eclipse", t)
            if spell.name == "Wrath":
                charges = min(int(self.tv("Eclipse", 2)), (e.get("charges", 0) if e else 0) + int(self.tv("Eclipse", 0)))
                p.buffs["Eclipse"] = {"until": t + self.tv("Eclipse", 3), "charges": charges}
            elif spell.name == "Starfire" and e and e.get("charges", 0) > 0:
                e["charges"] -= 1
        if self.balance and spell.kind in ("spell", "heal"):
            # global cooldown: an instant's was set just now (t + GCD) and is 10% shorter under Nature's Grace; a cast spell's started
            # with the cast and ends with it at the latest (Nature's Grace can haste a cast below 1.5 s)
            if p.gcd_until - t < GCD - 1e-6:
                p.gcd_until = min(p.gcd_until, t)
            elif self.rank("Nature's Grace") and p.buff("Nature's Grace", t):
                p.gcd_until = min(p.gcd_until, t + GCD * (1 - self.tv("Nature's Grace", 0) / 100))

    def after_fight(self, p, t):
        """Heal in caster form when hurt (Rejuvenation, Regrowth), then Cat Form again if the mana allows. A Moonkin stays in its form
        and eats (healing spells would need the form dropped and 35% of base mana to go back); out of it after an emergency heal, it
        heals here and shifts back."""
        spent = 0.0
        if self.balance:
            if self.in_moonkin:
                return 0.0
            rj, rg = self.spells.get("Rejuvenation"), self.spells.get("Regrowth")
            for heal in (rj, rg):
                if heal is None or p.hp >= 0.85 * p.hp_max or p.hp >= 0.70 * p.hp_max and heal is rg or p.mana < self.mana_cost(heal):
                    continue
                p.mana -= self.mana_cost(heal)
                total = ((heal.heal_min + heal.heal_max) / 2 + heal.heal_coef * p.spell_power + heal.hot) * self.heal_multiplier(heal)
                p.hp = min(p.hp_max, p.hp + total)
                spent += max(GCD, heal.cast)
            if self.moonkin and not self.in_moonkin and self.enter_moonkin(None, p, t):
                spent += GCD
            return spent
        rj, rg = self.spells.get("Rejuvenation"), self.spells.get("Regrowth")
        cheapest = min((self.mana_cost(h) for h in (rj, rg) if h is not None), default=0.0)
        # shift out to heal only with the mana for a heal and the way back (out of form already: heal with what there is)
        if p.hp < 0.70 * p.hp_max and (rj or rg) and self.form != "caster" and (not self.in_cat or p.mana >= self.shift_cost(p) + cheapest):
            if self.in_cat:
                if self.form == "cat":
                    self._cat_exit = (t, p.energy)
                self.in_cat = False
                p.mh = None
            for heal in (rj, rg):
                if heal is None or p.hp >= 0.85 * p.hp_max or p.mana < self.mana_cost(heal) + self.shift_cost(p):
                    continue
                p.mana -= self.mana_cost(heal)
                total = ((heal.heal_min + heal.heal_max) / 2 + heal.heal_coef * p.spell_power + heal.hot) * self.heal_multiplier(heal)
                p.hp = min(p.hp_max, p.hp + total)
                spent += max(GCD, heal.cast)
        if not self.in_cat:
            if not self.shift_in(None, p, t):
                pass   # no mana to shift: the engine drinks, the next fight starts with the shift
            else:
                spent += GCD
        return spent

    # ------------------------------------------------------------ priority list: bear (levels 10-19)
    def decide_bear(self, fight, can):
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        maul, roar, enrage, bash, bite = (sp.get(n) for n in ("Maul", "Demoralizing Roar", "Enrage", "Bash", "Primal Bite"))
        hp = m.hp
        if enrage and can(enrage) and not p.buff("Enrage", t) and hp > 0.4 * m.hp_max:
            return enrage
        if bash and can(bash) and not m.stunned(t) and ((m.caster and m.casting(t)) or p.hp < 0.40 * p.hp_max) and hp > 0.15 * m.hp_max:
            return bash
        if roar and can(roar) and not (m.debuffs.get("Demoralizing Roar", {}).get("until", 0) > t) and hp > 0.35 * m.hp_max:
            return roar
        if bite and can(bite) and p.rage >= self.mana_cost(bite) + (self.mana_cost(maul) if maul else 0.0):
            return bite
        if maul and fight.queued_swing is None and p.rage >= self.mana_cost(maul):
            return maul
        return None

    def decide_balance(self, fight, can, in_melee):
        """Balance: Moonfire and Insect Swarm up, Wrath while the mob walks in (Eclipse charges), Starfire on Eclipse charges
        or when the mob is rooted / stunned, Wrath otherwise (pushback in melee), Regrowth below 35% health with Nature's
        Swiftness when it is up; Entangling Roots when low and the mob is not rooted. A heal leaves Moonkin Form; the druid goes
        back in while the mob still has half its health (else after the fight). Out of mana it waits: druids cannot use wands."""
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        wrath, mf, sf, swarm, roots, rg, ns, ht = (sp.get(n) for n in ("Wrath", "Moonfire", "Starfire", "Insect Swarm", "Entangling Roots", "Regrowth", "Nature's Swiftness", "Healing Touch"))
        hp = m.hp

        def avg(s):
            return ((s.dmg_min + s.dmg_max) / 2 + s.coef * p.spell_power) * self.damage_multiplier(s, False) if s else 0.0

        if p.hp < 0.35 * p.hp_max and hp > 0.15 * m.hp_max:
            if ns and can(ns) and ht and not p.buff("Nature's Swiftness", t):
                return ns
            if ht and can(ht) and p.buff("Nature's Swiftness", t):
                self.leave_moonkin(fight)
                return ht
            if roots and can(roots) and in_melee and not m.rooted(t) and hp > 0.3 * m.hp_max:
                return roots
            if m.rooted(t) and in_melee and not m.stunned(t):
                return "retreat"   # a rooted mob still swings at you in melee range: step out before the heal
            if rg and can(rg) and (m.rooted(t) or m.stunned(t) or not in_melee):
                self.leave_moonkin(fight)
                return rg
        if self.moonkin and not self.in_moonkin and p.hp >= 0.5 * p.hp_max and hp > 0.5 * m.hp_max:
            reserve = 2 * self.mana_cost(sf) if sf else 0.0   # keep the mana for two Starfires
            if p.mana >= self.moonkin_cost(p) + reserve and self.enter_moonkin(fight, p, t):
                p.gcd_until = t + GCD
                return None
        if mf and can(mf) and hp <= avg(mf) * 0.9:
            return mf
        if wrath and can(wrath) and hp <= avg(wrath) * 0.9:
            return wrath
        if mf and can(mf) and not fight.dot_active("Moonfire") and hp > 0.35 * m.hp_max:
            return mf
        if swarm and can(swarm) and not fight.dot_active("Insect Swarm") and hp > 0.4 * m.hp_max:
            return swarm
        eclipse = self.rank("Eclipse") and self.eclipse_charges(fight) > 0
        if sf and can(sf) and (eclipse or m.rooted(t) or m.stunned(t)) and hp > avg(sf) * 0.5:
            return sf
        if wrath and can(wrath) and hp > avg(wrath) * 0.5:
            return wrath
        if sf and can(sf):
            return sf
        if wrath and can(wrath):
            return wrath
        return None   # out of mana: wait for regeneration (druids cannot use a wand)

    def decide(self, fight):
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        if self.balance:
            return self.decide_balance(fight, can, in_melee)

        claw, rake, shred, rip, bite, tf, pounce, ravage, rg, ht, ns, cat = (sp.get(n) for n in ("Claw", "Rake", "Shred", "Rip", "Ferocious Bite", "Tiger's Fury", "Pounce", "Ravage", "Regrowth", "Healing Touch", "Nature's Swiftness", "Cat Form"))
        hp = m.hp
        # caster form: heal and shift back
        if not self.in_cat:
            if p.hp < 0.55 * p.hp_max and hp > 0.15 * m.hp_max:
                if ns and can(ns) and ht and not p.buff("Nature's Swiftness", t):
                    return ns
                if ht and can(ht) and p.buff("Nature's Swiftness", t):
                    return ht
                if rg and can(rg) and p.mana >= self.mana_cost(rg) + self.shift_cost(p):
                    return rg
            if p.mana >= self.shift_cost(p):
                if self.shift_in(fight, p, t):
                    p.gcd_until = t + GCD
                    return None
            return None
        # emergency: shift out to heal
        if p.hp < 0.30 * p.hp_max and hp > 0.25 * m.hp_max and (rg or ht) and p.mana >= self.shift_cost(p) + (self.mana_cost(rg) if rg else 0.0):
            self.shift_out(fight)
            p.gcd_until = t + GCD
            return None
        if not in_melee:
            fc = sp.get("Feral Charge")
            if m.caster and m.casting(t) and fc and can(fc) and 8.0 <= m.dist <= 25.0:
                return fc
            return "advance"
        if self.form == "bear":
            return self.decide_bear(fight, can)
        # opener from prowl
        if not self.opened:
            if ravage and can(ravage):
                return ravage
            if pounce and can(pounce):
                return pounce
            if shred and can(shred):
                return shred
            self.opened = True
        if tf and can(tf) and not p.buff("Tiger's Fury", t) and hp > 0.3 * m.hp_max:
            return tf
        # finishers
        if bite and can(bite) and p.combo >= 1:
            lo1, hi1 = bite.one
            lo5, hi5 = bite.five
            est = ((lo1 + hi1) / 2 + ((lo5 + hi5) / 2 - (lo1 + hi1) / 2) * (p.combo - 1) / 4 + 0.03 * p.combo * p.attack_power) * self.damage_multiplier(Spell("x", "physical"), False) * 0.65
            if hp <= est * 0.95:
                fight._bite_extra = max(0.0, p.energy - self.mana_cost(bite))
                return bite
        # before Ferocious Bite (levels 20-31) Rip is the only finisher: spend the points on it while the mob will live through some ticks
        if bite is None and rip and can(rip) and not fight.dot_active("Rip") and p.combo >= self.RIP_EARLY_CP and hp > self.RIP_EARLY_HP * m.hp_max:
            return rip
        if p.combo >= 5:
            if rip and can(rip) and hp > 0.5 * m.hp_max and not fight.dot_active("Rip"):
                return rip
            if bite and can(bite):
                fight._bite_extra = max(0.0, p.energy - self.mana_cost(bite))
                return bite
        # Shifting Power: 40 energy for mana, at 60 energy or less (nothing spills over the cap) on a mob worth it, keeping the mana for
        # an emergency Regrowth and the shift back
        spw = sp.get("Shifting Power")
        if (spw and can(spw) and p.energy <= p.energy_max - getattr(spw, "energize", 0.0) and hp > 0.3 * m.hp_max
                and p.mana >= self.SHIFTING_POWER_ABOVE * p.mana_max
                and p.mana - self.mana_cost(spw) >= self.shift_cost(p) + (self.mana_cost(rg) if rg else 0.0)):
            return spw
        if rake and can(rake) and not fight.dot_active("Rake") and hp > 0.3 * m.hp_max:
            return rake
        if claw and can(claw):
            return claw
        return None
