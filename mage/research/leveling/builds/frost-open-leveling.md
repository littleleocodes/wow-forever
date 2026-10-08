# Frost — Leveling (open talent search) — 18/2/31

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/2/31 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost leveling build the open leveling search found on 2026-10-08: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the frost-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). +2.0% faster per kill than leveling-frost, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Improved Channeling** | 2/5 | **NEW** | Gives you a 40% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 28% chance while casting Arcane Blast. |
| **Arcane Subtlety** | 1/2 | changed | Reduces your target's resistance to all your spells by 8 and reduces the threat caused by your Arcane spells by 15%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Fire (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 2/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 4%. |

### Frost (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 1/2 | changed | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 15%. In addition, gives your Frost Ward a 10% chance to reflect Frost spells and effects while active. |
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 3/5 | changed | Improves your chance to hit with Frost and Fire spells by 3%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Ice Barrier** | 1/1 | changed | Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Frost | Improved Frostbolt | 5 | 0/0/5 |
| 15-17 | Frost | Frostbite | 3 | 0/0/8 |
| 18-19 | Frost | Elemental Precision | 2 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-23 | Frost | Frost Channeling | 3 | 0/0/14 |
| 24 | Frost | Piercing Ice | 1 | 0/0/15 |
| 25-26 | Frost | Shatter | 2 | 0/0/17 |
| 27-28 | Frost | Ice Shards | 2 | 0/0/19 |
| 29 | Frost | Shatter | 1 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32-34 | Frost | Ice Shards | 3 | 0/0/25 |
| 35-36 | Frost | Piercing Ice | 2 | 0/0/27 |
| 37 | Frost | Elemental Precision | 1 | 0/0/28 |
| 38 | Frost | Frost Warding | 1 | 0/0/29 |
| 39 | Frost | Cold Snap | 1 | 0/0/30 |
| 40 | Frost | Ice Barrier | 1 | 0/0/31 |
| 41-42 | Fire | Incineration | 2 | 0/2/31 |
| 43-44 | Arcane | Wand Specialization | 2 | 2/2/31 |
| 45-47 | Arcane | Arcane Focus | 3 | 5/2/31 |
| 48-50 | Arcane | Arcane Concentration | 3 | 8/2/31 |
| 51 | Arcane | Arcane Subtlety | 1 | 9/2/31 |
| 52-53 | Arcane | Arcane Concentration | 2 | 11/2/31 |
| 54-55 | Arcane | Arcane Focus | 2 | 13/2/31 |
| 56-57 | Arcane | Improved Channeling | 2 | 15/2/31 |
| 58-60 | Arcane | Arcane Meditation | 3 | 18/2/31 |

## Core talents (priority order)

1. **Ice Lance** — +8.4 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +5.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +3.9 s per kill at level 60 without it (removal, 3,000 fights).
4. **Fingers of Frost** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Frostbite** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
6. **Frost Channeling** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Arcane Meditation** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
8. **Piercing Ice** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +2.0% faster than the hand draft leveling-frost, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.75; leveling-frost 26.26, opt-frost-leveling-leveling-st 26.26, opt-frost-aoe-leveling-aoe 30.80. The search simulated 88,874 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frost leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/2521050000003-02-1535003331000301201-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
