# Frostfire — Leveling (open talent search) — 1/25/25

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 1/25/25 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frostfire (a Fire/Frost hybrid) leveling build the open leveling search found on 2026-10-23: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the frostfire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). 

## Point allocation

### Arcane (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 1/2 | moved | Increases your damage with Wands by 13%. |

### Fire (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Impact** | 1/3 | changed | Gives your Fire spells a 3% chance to stun the target for 2 sec. |
| **Burning Soul** | 1/3 | changed | Gives your Fire spells a 23% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 10%. |
| **Improved Fire Ward** | 2/2 | unchanged | Causes your Fire Ward to have a 20% chance to reflect Fire spells while active. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 5/5 | unchanged | Increases the critical strike chance of your Fire spells by 10%. |

### Frost (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 30%. In addition, gives your Frost Ward a 20% chance to reflect Frost spells and effects while active. |
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Improved Blizzard** | 2/3 | changed | Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 25% for 1.5 sec. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Improved Cone of Cold** | 1/3 | changed | Increases the damage dealt by your Cone of Cold spell by 12%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-12 | Frost | Elemental Precision | 3 | 0/0/3 |
| 13-14 | Frost | Frost Warding | 2 | 0/0/5 |
| 15-17 | Frost | Frostbite | 3 | 0/0/8 |
| 18-19 | Frost | Ice Shards | 2 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-23 | Frost | Frost Channeling | 3 | 0/0/14 |
| 24 | Frost | Ice Shards | 1 | 0/0/15 |
| 25-27 | Frost | Shatter | 3 | 0/0/18 |
| 28-29 | Frost | Ice Shards | 2 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32-33 | Frost | Improved Blizzard | 2 | 0/0/24 |
| 34 | Arcane | Wand Specialization | 1 | 1/0/24 |
| 35 | Frost | Improved Cone of Cold | 1 | 1/0/25 |
| 36-40 | Fire | Improved Fireball | 5 | 1/5/25 |
| 41-45 | Fire | Ignite | 5 | 1/10/25 |
| 46 | Fire | Burning Soul | 1 | 1/11/25 |
| 47 | Fire | Impact | 1 | 1/12/25 |
| 48-50 | Fire | Incineration | 3 | 1/15/25 |
| 51-53 | Fire | Master of Elements | 3 | 1/18/25 |
| 54-55 | Fire | Improved Fire Ward | 2 | 1/20/25 |
| 56-60 | Fire | Critical Mass | 5 | 1/25/25 |

## Core talents (priority order)

1. **Shatter** — +7.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Ice Lance** — +7.2 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +3.8 s per kill at level 60 without it (removal, 3,000 fights).
4. **Frostbite** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
5. **Frost Channeling** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Fingers of Frost** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Master of Elements** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Fireball** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 34.41; . The search simulated 76,952 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frostfire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/1-03550110002035-2035300321003102-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
