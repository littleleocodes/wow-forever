# Elemental Shaman — Leveling (solo)

[Shaman](../README.md) > [Leveling (solo)](README.md) > Elemental

**Leveling from level 1?** [The rotation level by level](elemental-by-level.md): what to press as each spell and talent arrives. [Your keys and macros](keybinds.md).

**[Elemental — Leveling](../research/leveling/builds/elemental-open-leveling.md)** (32/11/8) — [open the talent tree](https://talentsforever.com/shaman/60/540333100301135-05003201-053-12)

> 🔬 Derived build: found by this project's open leveling search (every legal build, no tree rule, in the fight lab, this project's leveling simulator; the winner picked by a race at levels 20-60). A model of the beta, to check at launch.

**Signature spells:** 75% of the damage at level 60 in the fight lab comes from the spec's core spells (Lightning Bolt, Earth Shock, Flame Shock; this build never casts Chain Lightning) (the spec's rule: at least 60%; **Lightning Bolt** cast at level 60).

## How to play

**Before the fight:** **Lightning Shield** up, **Rockbiter Weapon** on your weapon (**Windfury Weapon** from 30): you swing it whenever nothing else is ready. Drop **Searing Totem** as you pull while you have more than half your mana, and pull from range with **Lightning Bolt**.

**In the fight**, top to bottom:

1. **Lightning Bolt** while the mob walks in, as long as the cast ends before it reaches you.
2. **Earth Shock** when it would kill the mob, or to interrupt a caster.
3. **Flame Shock** while it is not on the mob and the mob has more than 30% health.
4. **Earth Shock** whenever the shock cooldown is free.
5. **Lightning Bolt** in between while you keep the mana for the next **Earth Shock** and **Flame Shock**; otherwise let your weapon swing.
6. Low on health at any point: under 30% drop **Stoneclaw Totem**, under 40% cast **Lesser Healing Wave**.

**Between fights:** Heal back to 80% health with **Lesser Healing Wave** (eat if you cannot), drink below 15% of your mana.

## Why this rotation

Kill as much as you can with **Lightning Bolt** before the mob reaches you, then use your shocks whenever they are ready and bolt between them while your mana holds. Mana is the limit: about a third of each kill is drinking in the fight lab.

**Why it works**

- **Lightning Shield** before each pull: it strikes a mob each time it hits you, one ball every few seconds; about 14% of your damage at 60 in the fight lab. **Shamanistic Focus** (level 28) makes it and your shocks 45% cheaper: the build's most valuable talent at 60 (about 3 seconds per kill without it).
- **Lightning Bolt** while the mob walks in: nothing pushes those casts back. Once the mob hits you, each hit pushes a cast back (about 3 times per kill in the fight lab); **Eye of the Storm** (levels 44-46) cuts that by 70%. **Elemental Alacrity** (34-36) takes half a second off the cast.
- The shocks share one cooldown and cannot be pushed back. **Flame Shock** goes first while it is not ticking and the mob is above 30% health (**Call of Flame**, 37-38, strengthens it and makes it last longer); **Earth Shock** takes every other shock, and comes first whenever it would kill. **Convection** (29-33) makes shocks and bolts 10% cheaper.
- **Elemental Fury** (levels 54-58) doubles the crit bonus of your spells and **Searing Totem**.
- Bolt between shocks only while you keep the mana for the next **Earth Shock** and **Flame Shock**; otherwise let your weapon swing. The fight lab keeps **Rockbiter Weapon** (from 30, **Windfury Weapon**) on, and your weapon does about an eighth of your damage at 60.
- Drop **Searing Totem** at each pull while you have more than half your mana: it does about 6% of your damage at 60.

**Caveats**

- From 39, **Elemental Focus** sometimes makes your next damage spell free: nothing to change, the next spell in the list takes it.
- This list is for one mob at a time; the fight lab does not model area pulls for Elemental. **Chain Lightning** hits up to 3 targets if you pull more.
- Levels 10-17 go into Restoration (**Tidal Focus**: 5% more chance to hit; **Mindfulness**: half your mana regeneration continues while you cast) and 18-28 into Enhancement (**Thundering Strikes**: 5% crit with spells and attacks; **Improved Lightning Shield** (23-24): more damage from **Lightning Shield**; **Mental Dexterity**, which mostly opens the tier of **Shamanistic Focus** at 28). From 29 every point goes to Elemental.
- Drink only below 15% mana and heal or eat back to 80% health between pulls: the tuned rules the fight lab plays.

**When to change it**

- A nearly dead mob: an instant **Earth Shock** finishes it before another bolt could land.
- A caster mob that stays back: **Earth Shock** interrupts it and locks that school for 2 seconds, which brings it to you.
- A bad pull (you under 30% health): **Stoneclaw Totem** taunts the mob onto itself, then heal with **Lesser Healing Wave**; the fight lab does this for every shaman.
- A mob that flees: **Frost Shock** slows it by 50% for 8 seconds (it shares the shock cooldown).

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10-14 | Tidal Focus (Restoration) | 5 |
| 15-17 | Mindfulness (Restoration) | 3 |
| 18-22 | Thundering Strikes (Enhancement) | 5 |
| 23-24 | Improved Lightning Shield (Enhancement) | 2 |
| 25-27 | Mental Dexterity (Enhancement) | 3 |
| 28 | Shamanistic Focus (Enhancement) | 1 |
| 29-33 | Convection (Elemental) | 5 |
| 34-36 | Elemental Alacrity (Elemental) | 3 |
| 37-38 | Call of Flame (Elemental) | 2 |
| 39 | Elemental Focus (Elemental) | 1 |
| 40-43 | Concussion (Elemental) | 4 |
| 44-46 | Eye of the Storm (Elemental) | 3 |
| 47-48 | Reverberation (Elemental) | 2 |
| 49 | Call of Thunder (Elemental) | 1 |
| 50-52 | Lightning Overload (Elemental) | 3 |
| 53 | Reverberation (Elemental) | 1 |
| 54-58 | Elemental Fury (Elemental) | 5 |
| 59 | Elemental Reach (Elemental) | 1 |
| 60 | Call of Flame (Elemental) | 1 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 27 |
| 30 | 30 |
| 40 | 30 |
| 50 | 30 |
| 60 | 28 |

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753). Simulations, not in-game measurements. Do not hand-edit.*

