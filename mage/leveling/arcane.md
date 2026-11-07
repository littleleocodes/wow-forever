# Arcane Mage — Leveling (solo)

[Mage](../README.md) > [Leveling (solo)](README.md) > Arcane

**[Arcane — Leveling](../research/leveling/builds/arcane-open-leveling.md)** (30/0/21) — [open the talent tree](https://talentsforever.com/mage/60/05100520310031153--2323013031200001-12)

> 🔬 Derived build: found by this project's open leveling search (every legal build, no tree rule, in the fight lab, this project's leveling simulator; the winner picked by a race at levels 20-60). A model of the beta, to check at launch.

*Signature spells (**Arcane Blast**): not checked for this build in its rotation yet (fightlab/signature_audit.py).*

## How to play

**Not in this build:** **Arcane Power** is a talent this build does not take: skip the lines that use it. The fight lab played the build without it.

**Before the fight:** **Frost Armor** (**Ice Armor** from level 30) and **Arcane Intellect** up. Pull from as far away as you can; **Presence of Mind** at the pull (your first cast goes out instantly), and **Arcane Power** too while you have more than half your mana.

**In the fight**, top to bottom:

1. With **Arcane Wrath**: cast it first on the pull if it will land before the mob reaches you, and again whenever it is ready and there is time.
2. **Arcane Blast** while the mob walks in: at most two in a row, only if the cast ends before the mob reaches you and costs no more than a quarter of your mana. Each stack gives all your spells spell damage (12% of your Intellect) for 18 seconds.
3. **Arcane Missiles** as your channel, also once the mob is on you (with **Improved Channeling**, hits do not cut it short), and at once when **Missile Barrage** lights up (after your two stacks, or when the mob is on you).
4. No Frost Nova: let the mob come and keep channeling. **Cone of Cold** only when the mob is on you and below a fifth of its health, then step back; **Ice Lance** if the mob is frozen.
5. When you cannot afford **Arcane Missiles**: **Fire Blast** if the mob is on you, else **Frostbolt**; finish with a **Fire Blast** that will kill, or your wand.
6. **Counterspell** a mob that casts spells.

**Between fights:** Drink your conjured water below a third of your mana, **Evocation** when it is ready and you are under 40% mana, eat below 40% of your health.

## Why this rotation

Arcane levels on its own spells: **Arcane Wrath** to open, two **Arcane Blast** stacks while the mob walks in, then **Arcane Missiles**, which you keep channeling when the mob reaches you; the tuned rules never cast **Frost Nova**. In the fight lab at level 60 (2026-11-04 run), **Arcane Missiles** is about 67% of this build's damage, **Arcane Blast** 14%, **Fire Blast** 7%, **Ice Lance** 7% and **Arcane Wrath** 4%; a kill takes about 32 seconds level-weighted with the talents taken in the page's order (Arcane first, Frost from level 40) and 30 at 60.

**Why it works**

- **Presence of Mind** (level 30) at the pull makes your first cast instant (the opening **Arcane Wrath** in the fight lab). This build has no **Arcane Power**: skip its line of the list.
- **Arcane Wrath** opens when its cast (3.5 seconds) lands before the mob arrives, then goes out whenever it is ready (6-second cooldown) and the cast fits. It gains spell damage equal to 5% of your maximum mana, and each cast has a 20% chance to light up **Missile Barrage**.
- **Arcane Blast** twice while the mob walks in: each cast gives you 12% of your Intellect as spell damage for 18 seconds and doubles the next cast's cost, so the fight lab stops at two and starts one only while it costs at most a quarter of your mana and will finish before the mob reaches you. Each cast rolls 40% for **Missile Barrage**. Without **Arcane Blast** a kill at 60 takes about 2 seconds longer in the fight lab.
- **Arcane Missiles** is the main spell, at range and in melee: **Improved Channeling** at 5 points gives a 100% chance that hits do not interrupt the channel. **Missile Barrage** makes the next one free, 2.5 seconds long and twice as dense: cast it at once after your two stacks, or when the mob is on you. Without **Missile Barrage** a kill at 60 takes about 4.1 seconds longer, without **Improved Channeling** 2.4; **Arcane Mind** (1.7), **Arcane Instability** (1.3), **Arcane Meditation** and **Arcane Concentration** (about 1.2 each) follow.
- No **Frost Nova**: the tuned rules measured kills faster without it. With hits unable to stop the Missiles, the global cooldown and the step back cost more than the hits do.
- When the mob is on you and below a fifth of its health, **Cone of Cold** and a step back (a tuned rule); **Fire Blast** finishes a mob it will kill. The 21 Frost points come last, from level 40: **Precision** for hit, **Improved Frostbolt**, **Frostbite** and **Ice Shards**, **Ice Lance** at 50, **Permafrost** and one point of **Fingers of Frost** at 60. With no **Frost Nova** in the list a freeze only comes from a chill (**Frostbite**, or **Fingers of Frost**): **Frost Armor** chilling a mob that hits you, or a **Frostbolt** cast when the Missiles are unaffordable. So **Ice Lance** is about 7% of the damage at 60 in the fight lab: cast it into a freeze when one happens.

**Caveats**

- This build takes **Ice Lance** only at level 50: before that, skip its line of the list.
- Mana: **Arcane Missiles** costs 655 at top rank, every **Arcane Blast** stack makes the next one dearer and **Arcane Power** adds 30%. **Frostbolt** (290) is for when you cannot afford the Missiles. Drink below a third of your mana and use **Evocation** between fights when it is ready and you are under 40% mana.
- The tuned rules eat below 40% of your health, not two thirds: the fight lab measured kills slightly faster that way, with no deaths in its tuning runs.
- Single pulls only: with several mobs on you, **Frost Nova** and **Arcane Explosion** are back in play.
- This is the 2026-11-03 search's winner (30/0/21, Frost as the second tree), written on 2026-11-04 in place of the earlier 31/17/3 build with Fire points and **Arcane Power**; the search's race had the two within 0.1% at levels 20-60, a tie, and the list is the same but for **Ice Lance**.

**When to change it**

- If the mob would reach you before an **Arcane Blast** or **Arcane Wrath** finishes, do not start it: channel **Arcane Missiles** instead (an instant cast with **Presence of Mind** is the exception).
- A mob that hits harder than a normal same-level mob is still worth a **Frost Nova**: the rule only says it costs time against the mobs the fight lab models.
- Against a caster mob, **Counterspell** it when it starts a cast, as every mage list in the fight lab does.

*This guide was written for the rotation of 2026-11-04; the list above was re-tuned since, so follow the list where the two differ.*

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10 | Arcane Resilience (Arcane) | 1 |
| 11-14 | Improved Channeling (Arcane) | 4 |
| 15-19 | Arcane Concentration (Arcane) | 5 |
| 20 | Arcane Blast (Arcane) | 1 |
| 21-22 | Missile Barrage (Arcane) | 2 |
| 23 | Improved Channeling (Arcane) | 1 |
| 24 | Arcane Impact (Arcane) | 1 |
| 25 | Arcane Wrath (Arcane) | 1 |
| 26-28 | Arcane Meditation (Arcane) | 3 |
| 29 | Arcane Impact (Arcane) | 1 |
| 30 | Presence of Mind (Arcane) | 1 |
| 31 | Arcane Impact (Arcane) | 1 |
| 32-34 | Arcane Mind (Arcane) | 3 |
| 35-37 | Arcane Instability (Arcane) | 3 |
| 38-39 | Arcane Mind (Arcane) | 2 |
| 40-41 | Precision (Frost) | 2 |
| 42-44 | Improved Frostbolt (Frost) | 3 |
| 45-47 | Ice Shards (Frost) | 3 |
| 48 | Improved Frost Nova (Frost) | 1 |
| 49 | Frost Warding (Frost) | 1 |
| 50 | Ice Lance (Frost) | 1 |
| 51 | Frost Warding (Frost) | 1 |
| 52-54 | Improved Blizzard (Frost) | 3 |
| 55-56 | Arctic Reach (Frost) | 2 |
| 57-59 | Permafrost (Frost) | 3 |
| 60 | Fingers of Frost (Frost) | 1 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 35 |
| 30 | 33 |
| 40 | 32 |
| 50 | 31 |
| 60 | 29 |

## Other builds of this spec

- [Arcane — Leveling](../research/leveling/builds/arcane-leveling.md) (29/0/22, 39 s per kill, level-weighted) — [open the talent tree](https://talentsforever.com/mage/60/21221500301030153--0525300001013002-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-07 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753). Simulations, not in-game measurements. Do not hand-edit.*

