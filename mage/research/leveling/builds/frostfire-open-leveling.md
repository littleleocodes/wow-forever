# Frostfire — Leveling (open talent search) — 2/26/23

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 2/26/23 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frostfire (a Fire/Frost hybrid) leveling build the open leveling search found on 2026-11-21: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the frostfire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). 

## Point allocation

### Arcane (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |

### Fire (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Impact** | 1/3 | changed | Gives your Fire spells a 3% chance to stun the target for 2 sec. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |

### Frost (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 4/5 | changed | Reduces the casting time of your Frostbolt spell by 0.4 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 1/3 | moved | Gives your Chill effects a 5% chance to Freeze the target for 5 sec. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Frost | Precision | 2 | 0/0/2 |
| 12-14 | Frost | Improved Frostbolt | 3 | 0/0/5 |
| 15 | Frost | Frostbite | 1 | 0/0/6 |
| 16 | Frost | Improved Frostbolt | 1 | 0/0/7 |
| 17-19 | Frost | Ice Shards | 3 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-22 | Frost | Ice Shards | 2 | 0/0/13 |
| 23-24 | Frost | Frost Channeling | 2 | 0/0/15 |
| 25-27 | Frost | Shatter | 3 | 0/0/18 |
| 28 | Frost | Frost Channeling | 1 | 0/0/19 |
| 29 | Frost | Improved Frost Nova | 1 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32 | Arcane | Wand Specialization | 1 | 1/0/22 |
| 33-37 | Fire | Accelerant | 5 | 1/5/22 |
| 38-42 | Fire | Ignite | 5 | 1/10/22 |
| 43 | Fire | Pyroblast | 1 | 1/11/22 |
| 44 | Fire | Impact | 1 | 1/12/22 |
| 45-46 | Fire | Improved Fire Blast | 2 | 1/14/22 |
| 47 | Fire | Incineration | 1 | 1/15/22 |
| 48 | Fire | Heating Up | 1 | 1/16/22 |
| 49 | Fire | Incineration | 1 | 1/17/22 |
| 50-52 | Fire | Master of Elements | 3 | 1/20/22 |
| 53-54 | Fire | Incineration | 2 | 1/22/22 |
| 55 | Frost | Improved Frost Nova | 1 | 1/22/23 |
| 56-58 | Fire | Critical Mass | 3 | 1/25/23 |
| 59 | Fire | Incineration | 1 | 1/26/23 |
| 60 | Arcane | Wand Specialization | 1 | 2/26/23 |

## Core talents (priority order)

1. **Shatter** — +4.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Ice Lance** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
4. **Fingers of Frost** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
5. **Frost Channeling** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
6. **Precision** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
7. **Ignite** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
8. **Critical Mass** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-20: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Impact to Wand Specialization at 60 (tie-break: -0.2% seed 3, -0.1% seed 4, level-weighted time per kill); Frostbite to Improved Frostbolt at 16 (gate: -0.4% seed 3, -0.4% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 32.94; . The search simulated 75,576 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frostfire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/2-55501001200133-0425120301003002-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
