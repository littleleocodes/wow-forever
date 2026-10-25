# Frost — Leveling (open talent search) — 18/3/30

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/3/30 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost leveling build the open leveling search found on 2026-10-23: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the frost-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). 

## Point allocation

### Arcane (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Focus** | 2/5 | changed | Improves your chance to hit with Arcane spells by 2%. |
| **Improved Channeling** | 1/5 | **NEW** | Gives you a 20% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 14% chance while casting Arcane Blast or Arcane Wrath. |
| **Arcane Subtlety** | 1/2 | changed | Reduces your target's resistance to all your spells by 8 and reduces the threat caused by your Arcane spells by 15%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Resilience** | 2/2 | changed | Increases your Armor by an amount equal to 50% of your Intellect. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Fire (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |

### Frost (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 1/2 | changed | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 15%. In addition, gives your Frost Ward a 10% chance to reflect Frost spells and effects while active. |
| **Improved Frostbolt** | 3/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.3 sec. |
| **Elemental Precision** | 2/3 | changed | Improves your chance to hit with Frost and Fire spells by 4%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 2/3 | changed | Increases the duration of your Chill effects by 22% and reduces the target's speed by an additional 7%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Winter's Chill** | 1/5 | changed | Gives your Frost damage spells a 20% chance to apply the Winter's Chill effect, which increases the damage done by your Cone of Cold spell to the target by 40%, stacking up to 5 times. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-12 | Frost | Improved Frostbolt | 3 | 0/0/3 |
| 13-14 | Frost | Elemental Precision | 2 | 0/0/5 |
| 15-17 | Frost | Frostbite | 3 | 0/0/8 |
| 18-19 | Frost | Ice Shards | 2 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-23 | Frost | Frost Channeling | 3 | 0/0/14 |
| 24 | Frost | Ice Shards | 1 | 0/0/15 |
| 25 | Frost | Shatter | 1 | 0/0/16 |
| 26-27 | Frost | Ice Shards | 2 | 0/0/18 |
| 28-29 | Frost | Shatter | 2 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32-33 | Arcane | Wand Specialization | 2 | 2/0/22 |
| 34-35 | Arcane | Arcane Focus | 2 | 4/0/22 |
| 36 | Arcane | Improved Channeling | 1 | 5/0/22 |
| 37-41 | Arcane | Arcane Concentration | 5 | 10/0/22 |
| 42 | Arcane | Arcane Subtlety | 1 | 11/0/22 |
| 43-44 | Arcane | Magic Absorption | 2 | 13/0/22 |
| 45-46 | Arcane | Arcane Resilience | 2 | 15/0/22 |
| 47-49 | Arcane | Arcane Meditation | 3 | 18/0/22 |
| 50-52 | Fire | Incineration | 3 | 18/3/22 |
| 53-54 | Frost | Arctic Reach | 2 | 18/3/24 |
| 55-56 | Frost | Improved Frost Nova | 2 | 18/3/26 |
| 57 | Frost | Frost Warding | 1 | 18/3/27 |
| 58-59 | Frost | Permafrost | 2 | 18/3/29 |
| 60 | Frost | Winter's Chill | 1 | 18/3/30 |

## Core talents (priority order)

1. **Ice Lance** — +5.6 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +4.2 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
4. **Frostbite** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Frost Channeling** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Arcane Meditation** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Fingers of Frost** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Arcane Concentration** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +4.0% faster than the hand draft leveling-frost, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 30.24; leveling-frost 31.44, opt-frost-aoe-leveling-aoe 34.85. The search simulated 48,237 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frost leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/22101252000003-03-13253223012030021-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
