# Elemental-Enhancement Shaman — Leveling (solo)

[Shaman](../README.md) > [Leveling (solo)](README.md) > Elemental-Enhancement

*A Lightning Bolt caster (Call of Thunder, Lightning Overload) that dips Enhancement for its passive bonuses.* (a hybrid: Elemental/Enhancement).

**[Elemental-Enhancement — Leveling](../research/leveling/builds/elemental-enhancement-open-leveling.md)** (22/22/7) — [open the talent tree](https://talentsforever.com/shaman/60/5502311300101-055030301021002-052-6)

> 🔬 Derived build: found by this project's open leveling search (every legal build, no tree rule, in the fight lab, this project's leveling simulator; the winner picked by a race at levels 20-60). A model of the beta, to check at launch.

## How to play

**Not in this build:** **Lava Burst** is a talent this build does not take: skip the lines that use it. The fight lab played the build without it.

**Before the fight:** **Lightning Shield** up, **Rockbiter Weapon** on your weapon (**Windfury Weapon** from 30): you swing it whenever nothing else is ready. Drop **Searing Totem** as you pull while you have more than half your mana, and pull from range with **Lightning Bolt**.

**In the fight**, top to bottom:

1. **Lightning Bolt** while the mob walks in, as long as the cast ends before it reaches you.
2. **Earth Shock** when it would kill the mob, or to interrupt a caster.
3. **Flame Shock** while it is not on the mob and the mob has more than 30% health.
4. **Lava Burst** whenever it is ready (20% more damage with **Flame Shock** on the mob).
5. **Earth Shock** whenever the shock cooldown is free.
6. **Lightning Bolt** in between while you keep the mana for the next **Earth Shock** and **Flame Shock**; otherwise let your weapon swing.
7. Low on health at any point: under 30% drop **Stoneclaw Totem**, under 40% cast **Lesser Healing Wave**.

**Between fights:** Heal back to 80% health (eat if you cannot), drink below a third of your mana.

## Why this rotation

Elemental-Enhancement levels with the Elemental list: **Lightning Bolt** while the mob walks in, then the shocks on cooldown and bolts between them while your mana holds. The Enhancement half turns your Intellect into spell damage and attack power (**Mental Quickness**, **Mental Dexterity**), so your spells and your weapon both hit harder. It has no **Lava Burst** and no **Eye of the Storm**.

**Why it works**

- **Shamanistic Focus** (level 35) makes your shocks and **Lightning Shield** 45% cheaper: at 60 the fight lab measured 5.2 seconds per kill without it, the build's most valuable talent.
- **Lightning Bolt** while the mob walks in, as long as the cast ends before it reaches you; **Elemental Alacrity** (levels 21-23) cuts its cast by half a second. Once the mob hits you each hit pushes a cast back, and this build has no **Eye of the Storm**: bolt in melee only while you keep the mana for the next shocks.
- The shocks share one cooldown: **Flame Shock** while it is not ticking and the mob is above 30% health, **Earth Shock** on every other free shock and first whenever it would kill. **Reverberation** (levels 57-58) shortens the shared cooldown by 0.4 seconds.
- **Mental Quickness** (levels 48-49) adds 30% of your Intellect as spell damage and **Mental Dexterity** (39-41) all of it as attack power; without Mental Quickness the fight lab measured 2.0 seconds more per kill at 60.
- Before every pull: **Lightning Shield** (**Improved Lightning Shield** from 42), **Rockbiter Weapon** (**Windfury Weapon** from 30), and **Searing Totem** while you have more than half your mana.

**Caveats**

- No **Lava Burst**: skip the step that names it.
- In the fight lab it takes 38 seconds per kill (levels 20-60): about a fifth slower than Enhancement (32) and level with Elemental (39).
- This list is for one mob at a time; the fight lab does not model area pulls for this rotation.

**When to change it**

- A nearly dead mob: an instant **Earth Shock** finishes it before another bolt could land.
- A caster mob that stays back: **Earth Shock** interrupts it and locks that school for 2 seconds, which brings it to you.
- A bad pull (you under 30% health): **Stoneclaw Totem** taunts the mob onto itself, then heal with **Lesser Healing Wave**.
- A mob that flees: **Frost Shock** slows it by 50% for 8 seconds (it shares the shock cooldown).

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10-14 | Convection (Elemental) | 5 |
| 15-17 | Call of Flame (Elemental) | 3 |
| 18-19 | Concussion (Elemental) | 2 |
| 20 | Elemental Focus (Elemental) | 1 |
| 21-23 | Elemental Alacrity (Elemental) | 3 |
| 24-28 | Thundering Strikes (Enhancement) | 5 |
| 29-30 | Ancestral Knowledge (Enhancement) | 2 |
| 31 | Totemic Focus (Restoration) | 1 |
| 32-34 | Ancestral Knowledge (Enhancement) | 3 |
| 35 | Shamanistic Focus (Enhancement) | 1 |
| 36-38 | Concussion (Elemental) | 3 |
| 39-41 | Mental Dexterity (Enhancement) | 3 |
| 42 | Improved Lightning Shield (Enhancement) | 1 |
| 43-44 | Toughness (Enhancement) | 2 |
| 45-46 | Improved Lightning Shield (Enhancement) | 2 |
| 47 | Flurry (Enhancement) | 1 |
| 48-49 | Mental Quickness (Enhancement) | 2 |
| 50-53 | Totemic Focus (Restoration) | 4 |
| 54-55 | Mindfulness (Restoration) | 2 |
| 56 | Call of Thunder (Elemental) | 1 |
| 57-58 | Reverberation (Elemental) | 2 |
| 59 | Lightning Overload (Elemental) | 1 |
| 60 | Elemental Devastation (Elemental) | 1 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 28 |
| 30 | 38 |
| 40 | 39 |
| 50 | 40 |
| 60 | 39 |

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

