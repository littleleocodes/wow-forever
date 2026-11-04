# Frostfire Mage — Leveling (solo)

[Mage](../README.md) > [Leveling (solo)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Leveling](../research/leveling/builds/frostfire-open-leveling.md)** (1/25/25) — [open the talent tree](https://talentsforever.com/mage/60/1-35501101002133-2035300321003102-7)

> 🔬 Derived build: found by this project's open leveling search (every legal build, no tree rule, in the fight lab, this project's leveling simulator; the winner picked by a race at levels 20-60). A model of the beta, to check at launch.

> **Signature spells: this build fails the check** in the fight lab (Frostfire Bolt 0.00/kill at 40 (needs 0.50); Frostfire Bolt 0.00/kill at 50 (needs 0.50); Frostfire Bolt 0.00/kill at 60 (needs 0.50); core share 0% < 30%). Frostfire is defined by **Frostfire Bolt** cast in every fight and Frostfire Bolt carrying 30% of the damage at level 60. No leveling build of this spec passes yet; it stays on the page until one does (the leveling searches since 2026-10-22 look only for such builds).

## How to play

**Not in this build:** **Cold Snap**, **Ice Barrier** are talents this build does not take: skip the lines that use them. The fight lab played the build without them.

**Before the fight:** **Frost Armor** (**Ice Armor** from level 30) and **Arcane Intellect** up; **Ice Barrier** before each pull once you have it. Pull from as far away as you can.

**In the fight**, top to bottom:

1. **Frostbolt** while the mob walks in (it slows it) and whenever nothing below applies, but only while the mob has more than a fifth of its health; if the mob would reach you before the cast ends, **Fire Blast** it instead (or wand it until it arrives if **Fire Blast** is on cooldown and **Frost Nova** is ready).
2. **Frost Nova** when it reaches you, then step back out of melee; **Cold Snap** resets **Frost Nova** if it has more than 8 seconds of cooldown left and the mob still has 40% of its health; with both down, **Fire Blast**.
3. **Ice Lance** again and again while the mob is frozen (**Frost Nova**, **Frostbite** or **Fingers of Frost**).
4. Below a fifth of the mob's health: **Fire Blast** (not below a tenth), an **Ice Lance** that will kill, or your wand. No Cone of Cold at all.
5. **Counterspell** a mob that casts spells.

**Between fights:** Drink your conjured water below a third of your mana, **Evocation** when it is ready and you are under 40% mana, eat below two thirds of your health.

## Why this rotation

The Frostfire leveling build is a Frost mage whose bolt changes at level 40: **Frostbolt** before, **Frostfire Bolt** after, with **Frost Nova**, a step back and **Ice Lance** into the freeze throughout. In the fight lab at level 60, **Ice Lance** is about 60% of its damage and **Frostfire Bolt** about 31% (its burn included).

**Why it works**

- **Frostfire Bolt** (trained at level 40) counts as Frost and Fire, so both trees' talents apply, and it slows like **Frostbolt** (40%), so its chill rolls **Frostbite** (15% to freeze) and **Fingers of Frost** (15%: your next 2 spells count as cast on a frozen target). **Improved Fireball** (levels 36-40) cuts its 3-second cast to 2.5. The tuned rules (2026-10-22) cast it down to a tenth of the mob's health.
- Before level 40, **Frostbolt** does the same job, but only while the mob has more than 35% of its health; below that, an **Ice Lance** into a freeze or the wand.
- **Ice Lance** (level 20) and **Shatter** (25-27) are the build's two most valuable talents in the fight lab at level 60 (without either a kill takes about 7 seconds longer): a frozen mob takes 200% more damage from **Ice Lance**, with 50% more crit chance and **Ice Shards**' bigger crits.
- **Frost Nova** when the mob reaches you, then step back out of melee.
- **Fire Blast** is a small part here (about 3% of the damage): the tuned rules cast it only while the mob is between a tenth and a fifth of its health and you have more than 30% of your mana.
- **Master of Elements** (levels 51-53) refunds 30% of a spell's base cost on each Fire or Frost crit, which **Shatter** makes common; **Critical Mass** (56-60) adds 10% crit chance to your Fire spells.

**Caveats**

- This build takes neither **Heating Up** nor **Pyroblast**, and the tuned rules never cast **Pyroblast** with this list.
- The signature rule: the Frostfire spec must do at least 30% of its damage with **Frostfire Bolt**. Two tuned rules serve that floor: **Ice Lance** only above 30% of your mana, and the narrow **Fire Blast** window. They keep the bolt at about 30% and cost a little time: the fight lab measured the whole rule set 0.4% slower per kill than the plain list.
- **Cone of Cold** stays out of single pulls (the tuned rules never cast it); **Improved Blizzard**, **Improved Cone of Cold** and **Improved Fire Ward** do nothing on single pulls.
- Mana: **Frostfire Bolt** costs 370 at top rank. Drink below a third of your mana and use **Evocation** between fights when it is ready and you are under 40% mana.
- Level 40 is the slow spot: about 44 seconds per kill in the fight lab, against 33 at level 30 and 35 at level 50.

**When to change it**

- On a nearly dead mob (below a tenth of its health), start no bolt: an **Ice Lance** that will kill, or the wand.
- Mob on you with **Frost Nova** down: keep casting the bolt (**Burning Soul** sometimes keeps a hit from pushing it back); **Fire Blast** only inside its window.

*This guide was written for the rotation of 2026-10-25; the list above was re-tuned since, so follow the list where the two differ.*

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753). Simulations, not in-game measurements. Do not hand-edit.*

