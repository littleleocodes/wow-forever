# Fire Mage — Leveling (solo)

[Mage](../README.md) > [Leveling (solo)](README.md) > Fire

**[Fire — Leveling](../research/leveling/builds/fire-leveling.md)** (0/32/19) — [open the talent tree](https://talentsforever.com/mage/60/-00550130130133151-00551030010013-6)

> 🔬 Derived build: searched in the fight lab (this project's leveling simulator) from the spec's builds and the stats model's best one; it beat the hand-made build (Fire (optimized)), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the fight:** **Frost Armor** (**Ice Armor** from level 30) and **Arcane Intellect** up; **Combustion** at the pull when it is ready. Pull from as far away as you can.

**In the fight**, top to bottom:

1. **Fireball** while the mob walks in, and whenever nothing below applies.
2. **Fire Blast** when the mob would reach you before a **Fireball** lands (**Scorch** if **Fire Blast** is on cooldown and there is time), once it is on you, or when it will kill.
3. **Frost Nova** when it reaches you, then step back; **Blast Wave** if **Frost Nova** is on cooldown.
4. **Ice Lance** while the mob is frozen; **Pyroblast** only at 3 stacks of **Heating Up**.
5. Mob on you and no control left: **Scorch** (a short cast, pushed back less). Finish a nearly dead mob with your wand.
6. **Counterspell** a mob that casts spells.

**Between fights:** Drink your conjured water below a third of your mana, **Evocation** when it is ready and you are under 40% mana, eat below two thirds of your health.

## Why this rotation

Fire levels with **Fireball** at range and **Fire Blast** up close, and borrows the Frost tree's freeze: **Frost Nova**, step back, and **Ice Lance** the frozen mob. **Ice Lance** into the freeze is this build's biggest damage source at level 60 in the fight lab (over a third), ahead of **Fireball**.

**Why it works**

- **Fireball** from as far away as you can: 3 seconds with **Improved Fireball** (levels 29-33). It is the filler whenever nothing else applies; the 2026-10-15 re-tune found no health or mana limit on **Fireball**, **Fire Blast** or **Scorch** that levels faster, so the earlier ones are gone.
- **Fire Blast** is your instant for when the mob would reach you before a **Fireball** lands, or is already on you, and to finish a mob it will kill; at range, **Fireball** comes first.
- **Frost Nova** when the mob reaches you, then step back. When Nova is on cooldown, **Blast Wave** dazes the mob (50% slower for 6 seconds) so you can get away.
- **Ice Lance** while the mob is frozen: this build takes **Ice Lance**, **Shatter**, **Frostbite** and **Ice Shards** from the Frost tree, so a frozen target takes 300% more damage with extra crit. That is over a third of your damage at level 60 in the fight lab.
- **Scorch** when the mob is on you and your control is down: its 1.5-second cast is pushed back less than a **Fireball**. It also covers the walk-in when **Fire Blast** is on cooldown and a **Fireball** would not land in time.
- **Combustion** goes at the pull. **Pyroblast** waits for 3 stacks of **Heating Up**, which almost never happens in a short leveling fight.

**Caveats**

- Mana: **Fireball** costs 410 at top rank against 290 for a **Frostbolt**. Drink below a third of your mana and use **Evocation** between fights when it is ready.
- **Impact** stuns the mob for 2 seconds on 10% of your Fire hits, and **Burning Soul** keeps 70% of your Fire casts from being pushed back: both help when a mob reaches you.
- Pulls of several mobs: **Blast Wave** and **Flamestrike** hit them all, but the fight lab only measured single pulls for Fire.

**When to change it**

- On a nearly dead mob, finish with the instant that will kill (**Fire Blast**, an **Ice Lance**, **Scorch**) or the wand rather than start a **Fireball**.
- If you run low on mana in a fight, keep **Fire Blast** and **Ice Lance** for the freeze and let the wand finish; the fight lab's rotation has no mana limit of its own and drinks below a third between fights.

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
*Generated by `_reference/data/render_modes.py` on 2026-10-16 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

