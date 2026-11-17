# Frost — Leveling (open talent search) — 18/3/30

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/3/30 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost leveling build the open leveling search found on 2026-11-16: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the frost-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). 

## Point allocation

### Arcane (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Improved Channeling** | 3/5 | **NEW** | Gives your Arcane Missiles spell a 60% chance and your Arcane Blast and Arcane Wrath spells a 42% chance to not lose casting time when you take damage. |
| **Arcane Resilience** | 3/3 | changed | Increases your Armor by an amount equal to 75% of your Intellect. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Fire (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |

### Frost (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 2/3 | changed | Increases the duration of your Chill effects by 22% and reduces the target's speed by an additional 7%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Frost | Precision | 2 | 0/0/2 |
| 12-14 | Frost | Improved Frostbolt | 3 | 0/0/5 |
| 15-17 | Frost | Frostbite | 3 | 0/0/8 |
| 18-19 | Frost | Improved Frostbolt | 2 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-23 | Frost | Frost Channeling | 3 | 0/0/14 |
| 24 | Frost | Ice Shards | 1 | 0/0/15 |
| 25 | Frost | Shatter | 1 | 0/0/16 |
| 26-27 | Frost | Ice Shards | 2 | 0/0/18 |
| 28-29 | Frost | Shatter | 2 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32-33 | Frost | Ice Shards | 2 | 0/0/24 |
| 34-35 | Frost | Arctic Reach | 2 | 0/0/26 |
| 36-37 | Frost | Improved Frost Nova | 2 | 0/0/28 |
| 38-39 | Frost | Permafrost | 2 | 0/0/30 |
| 40-41 | Arcane | Wand Specialization | 2 | 2/0/30 |
| 42-43 | Arcane | Arcane Resilience | 2 | 4/0/30 |
| 44 | Arcane | Improved Channeling | 1 | 5/0/30 |
| 45-49 | Arcane | Arcane Concentration | 5 | 10/0/30 |
| 50-51 | Arcane | Arcane Subtlety | 2 | 12/0/30 |
| 52-53 | Arcane | Improved Channeling | 2 | 14/0/30 |
| 54 | Arcane | Arcane Resilience | 1 | 15/0/30 |
| 55-57 | Arcane | Arcane Meditation | 3 | 18/0/30 |
| 58-60 | Fire | Incineration | 3 | 18/3/30 |

## Core talents (priority order)

1. **Shatter** — +4.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Ice Lance** — +3.0 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Improved Frostbolt** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Precision** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Frost Channeling** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
7. **Arcane Meditation** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
8. **Frostbite** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +3.5% faster than the hand draft leveling-frost, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 28.88; leveling-frost 29.89, opt-frost-aoe-leveling-aoe 33.95. The search simulated 66,618 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frost leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/2332050000003-3-0525322301203002-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
