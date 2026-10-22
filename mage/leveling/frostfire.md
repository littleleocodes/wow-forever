# Frostfire Mage — Leveling (solo)

[Mage](../README.md) > [Leveling (solo)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Leveling](../research/leveling/builds/frostfire-open-leveling.md)** (0/26/25) — [open the talent tree](https://talentsforever.com/mage/60/-03550030100135-00550221310013002-7)

> 🔬 Derived build: found by this project's open leveling search (every legal build, no tree rule, in the fight lab, this project's leveling simulator; the winner picked by a race at levels 20-60). A model of the beta, to check at launch.

## How to play

**Not in this build:** **Blast Wave**, **Combustion** are talents this build does not take: skip the lines that use them. The fight lab played the build without them.

**Before the fight:** **Frost Armor** (**Ice Armor** from level 30) and **Arcane Intellect** up; **Combustion** at the pull when it is ready. Pull from as far away as you can.

**In the fight**, top to bottom:

1. **Fireball** while the mob walks in, and whenever nothing below applies, while the mob has more than about a third (35%) of its health.
2. **Fire Blast** when the mob would reach you before a **Fireball** lands (**Scorch** if **Fire Blast** is on cooldown and there is time), once it is on you, or when it will kill; never on a mob below a tenth of its health.
3. **Frost Nova** when it reaches you, then step back; **Blast Wave** if **Frost Nova** is on cooldown.
4. **Ice Lance** while the mob is frozen; **Pyroblast** only at 3 stacks of **Heating Up**.
5. Mob on you and no control left: **Scorch** (a short cast, pushed back less), while the mob has more than about a third of its health.
6. Below about a third of the mob's health, no **Fireball** or **Scorch**: finish with **Fire Blast** (not below a tenth), an **Ice Lance** or your wand.
7. **Counterspell** a mob that casts spells.

**Between fights:** Drink your conjured water below a third of your mana, **Evocation** when it is ready and you are under 40% mana, eat below two thirds of your health.

## Why this rotation

The Frostfire leveling build plays the Fire leveling list: **Fireball** at range, **Frost Nova** and a step back when the mob arrives, **Ice Lance** into the frozen mob. Its first 25 points (levels 10-34) go into Frost, so the freeze carries the build; the Fire talents arrive from level 35. **Ice Lance** is almost half of its damage at level 60 in the fight lab.

**Why it works**

- **Ice Lance** (level 20) and **Shatter** (25-27) are the build's two most valuable talents in the fight lab at level 60 (without them a kill takes about 6 and 4 seconds longer): a frozen mob takes 200% more damage from **Ice Lance**, with 50% more crit chance and **Ice Shards**' bigger crits.
- **Frostbite** (levels 15-16) and **Fingers of Frost** (30-31) work on chills, and **Fireball** does not chill: here they come from **Frost Armor** (**Ice Armor** from 30) chilling a mob that hits you. **Improved Frost Nova** (17-18) brings **Frost Nova** back sooner, and **Frost Channeling** (32-34) makes your Frost spells cheaper.
- **Fireball** from as far away as you can, while the mob has more than 35% health; **Improved Fireball** (35-39) cuts it to 3 seconds. Below that, **Fire Blast** (not below a tenth of the mob's health), an **Ice Lance** or the wand finish it without overkill.
- **Heating Up** (level 50): crits with **Fireball**, **Fire Blast** and **Scorch**, and every **Fire Blast** hit, stack it; at 3 stacks cast **Pyroblast**, which then comes out fast. **Incineration** adds crit to **Fire Blast**, **Ice Lance** and **Scorch**, and **Master of Elements** (51-53) refunds 30% of a spell's base cost on each Fire or Frost crit, which **Shatter** makes common.

**Caveats**

- This build takes neither **Combustion** nor **Blast Wave**: skip those lines. When **Frost Nova** is on cooldown and the mob is on you, **Fire Blast**, then **Scorch** (above a third of the mob's health).
- **Frostfire Bolt** (trained at level 40) is not in this list: the fight lab plays this build with **Fireball**, and in the Frostfire leveling rotation the tuned rules switch **Frostfire Bolt** off for this same build (2026-10-22: 3.6% faster per kill with **Frostbolt** instead).
- Mana: **Fireball** costs 410 at top rank. Drink below a third of your mana and use **Evocation** between fights when it is ready and you are under 40% mana.

**When to change it**

- On a nearly dead mob, finish with a **Fire Blast** or **Ice Lance** that will kill, or the wand, rather than start a **Fireball**.
- Mob on you with **Frost Nova** down: **Fire Blast**, then **Scorch**; its 1.5-second cast is pushed back less than a **Fireball**.

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10-14 | Elemental Precision (Frost) | 5 |
| 15-16 | Frostbite (Frost) | 2 |
| 17-18 | Improved Frost Nova (Frost) | 2 |
| 19 | Ice Shards (Frost) | 1 |
| 20 | Ice Lance (Frost) | 1 |
| 21 | Piercing Ice (Frost) | 1 |
| 22-24 | Ice Shards (Frost) | 3 |
| 25-27 | Shatter (Frost) | 3 |
| 28 | Ice Block (Frost) | 1 |
| 29 | Ice Shards (Frost) | 1 |
| 30-31 | Fingers of Frost (Frost) | 2 |
| 32-34 | Frost Channeling (Frost) | 3 |
| 35-39 | Improved Fireball (Fire) | 5 |
| 40-44 | Ignite (Fire) | 5 |
| 45-47 | Burning Soul (Fire) | 3 |
| 48 | Pyroblast (Fire) | 1 |
| 49 | Incineration (Fire) | 1 |
| 50 | Heating Up (Fire) | 1 |
| 51-53 | Master of Elements (Fire) | 3 |
| 54 | Incineration (Fire) | 1 |
| 55-59 | Critical Mass (Fire) | 5 |
| 60 | Incineration (Fire) | 1 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 30 |
| 30 | 34 |
| 40 | 40 |
| 50 | 34 |
| 60 | 30 |

---
*Generated by `_reference/data/render_modes.py` on 2026-10-22 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70425). Simulations, not in-game measurements. Do not hand-edit.*

