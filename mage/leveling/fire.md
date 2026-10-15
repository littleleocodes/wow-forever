# Fire Mage — Leveling (solo)

[Mage](../README.md) > [Leveling (solo)](README.md) > Fire

**[Fire — Leveling](../research/leveling/builds/fire-leveling.md)** (0/32/19) — [open the talent tree](https://talentsforever.com/mage/60/-00550130130133151-00551030010013-6)

> 🔬 Derived build: searched in the fight lab (this project's leveling simulator) from the spec's builds and the stats model's best one; it beat the hand-made build (Fire (optimized)), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the fight:** **Frost Armor** (**Ice Armor** from level 30) and **Arcane Intellect** up; **Combustion** at the pull when it is ready. Pull from as far away as you can.

**In the fight**, top to bottom:

1. **Fireball** while the mob walks in and while it has more than a fifth of its health.
2. **Fire Blast** when the mob would reach you before a **Fireball** lands, or once it is on you (not below a tenth of its health).
3. **Frost Nova** when it reaches you, then step back; **Blast Wave** if **Frost Nova** is on cooldown.
4. **Ice Lance** while the mob is frozen; **Pyroblast** only at 3 stacks of **Heating Up**.
5. Mob on you and no control left: **Scorch**, only above half your mana. Finish a nearly dead mob with your wand.
6. **Counterspell** a mob that casts spells.

**Between fights:** Drink your conjured water below a third of your mana, **Evocation** when it is ready and you are under 40% mana, eat below two thirds of your health.

## Why this rotation

Fire levels with **Fireball** at range and **Fire Blast** up close, and borrows the Frost tree's freeze: **Frost Nova**, step back, and **Ice Lance** the frozen mob. **Ice Lance** into the freeze is this build's biggest damage source at level 60 in the fight lab (about 40%), ahead of **Fireball**.

**Why it works**

- **Fireball** from as far away as you can (**Flame Throwing** adds 6 yards): 3 seconds with **Improved Fireball**. Stop starting it below a fifth of the mob's health, where it overkills; the fight lab measured that faster.
- **Fire Blast** is your instant for when the mob would reach you before a **Fireball** lands, or is already on you; at range, **Fireball** comes first. Leave the last 10% of the mob's health to the wand.
- **Frost Nova** when the mob reaches you, then step back. When Nova is on cooldown, **Blast Wave** dazes the mob (50% slower for 6 seconds) so you can get away.
- **Ice Lance** while the mob is frozen: this build takes **Ice Lance**, **Shatter**, **Frostbite** and **Ice Shards** from the Frost tree, so a frozen target takes 300% more damage with extra crit. That is about 40% of your damage at level 60 in the fight lab.
- **Scorch** only above half your mana (tuned): when the mob is on you and your control is down, its 1.5-second cast is pushed back less than a **Fireball**.
- **Combustion** goes at the pull. **Pyroblast** waits for 3 stacks of **Heating Up**, which almost never happens in a short leveling fight.

**Caveats**

- Mana: **Fireball** costs 410 at top rank against 290 for a **Frostbolt**. Drink below a third of your mana and use **Evocation** between fights when it is ready.
- **Impact** stuns the mob for 2 seconds on 10% of your Fire hits, and **Burning Soul** keeps 70% of your Fire casts from being pushed back: both help when a mob reaches you.
- Pulls of several mobs: **Blast Wave** and **Flamestrike** hit them all, but the fight lab only measured single pulls for Fire.

**When to change it**

- On a nearly dead mob, let the wand finish it rather than start a **Fireball** (below 20% health) or spend a **Fire Blast** (below 10%).
- If you run low on mana in a fight, skip **Scorch** and keep **Fire Blast** and **Ice Lance** for the freeze; the fight lab casts **Scorch** only above half your mana.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10-14 | Elemental Precision (Frost) | 5 |
| 15 | Permafrost (Frost) | 1 |
| 16-18 | Frostbite (Frost) | 3 |
| 19 | Ice Shards (Frost) | 1 |
| 20 | Ice Lance (Frost) | 1 |
| 21-24 | Ice Shards (Frost) | 4 |
| 25 | Ice Block (Frost) | 1 |
| 26-28 | Shatter (Frost) | 3 |
| 29-33 | Improved Fireball (Fire) | 5 |
| 34-38 | Ignite (Fire) | 5 |
| 39-41 | Burning Soul (Fire) | 3 |
| 42 | Impact (Fire) | 1 |
| 43 | Pyroblast (Fire) | 1 |
| 44-46 | Improved Scorch (Fire) | 3 |
| 47-48 | Master of Elements (Fire) | 2 |
| 49 | Blast Wave (Fire) | 1 |
| 50 | Master of Elements (Fire) | 1 |
| 51-53 | Critical Mass (Fire) | 3 |
| 54-58 | Fire Power (Fire) | 5 |
| 59 | Combustion (Fire) | 1 |
| 60 | Heating Up (Fire) | 1 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 37 |
| 30 | 38 |
| 40 | 43 |
| 50 | 36 |
| 60 | 29 |

## Other builds of this spec

- [Fire (optimized)](../research/leveling/builds/opt-fire-leveling-leveling-st.md) (0/33/18, 37 s per kill, level-weighted) — [open the talent tree](https://talentsforever.com/mage/60/-00552330130103151-00551030010012-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

