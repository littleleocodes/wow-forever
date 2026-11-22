# Frost — Leveling (open talent search) — 18/1/32

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/1/32 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost leveling build the open leveling search found on 2026-11-21: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the frost-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). 

## Point allocation

### Arcane (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Improved Channeling** | 1/5 | **NEW** | Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage. |
| **Arcane Resilience** | 3/3 | changed | Increases your Armor by an amount equal to 75% of your Intellect. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 1/2 | changed | Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 1/2 | **NEW** | Gives your Arcane Blast spell a 20% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Fire (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 1/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 2%. |

### Frost (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 2/3 | moved | Gives your Chill effects a 10% chance to Freeze the target for 5 sec. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 1/3 | changed | Increases the duration of your Chill effects by 11% and reduces the target's speed by an additional 3%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Winter's Chill** | 2/5 | changed | Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 40% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times. |
| **Ice Barrier** | 1/1 | changed | Shield yourself, absorbing 447 damage and increasing your Frost damage by 15% for 1 min. While shielded, your Frost damage is increased by an additional 5% and you do not lose casting time when you take damage. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Frost | Precision | 2 | 0/0/2 |
| 12-16 | Frost | Improved Frostbolt | 5 | 0/0/7 |
| 17-19 | Frost | Ice Shards | 3 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-23 | Frost | Frost Channeling | 3 | 0/0/14 |
| 24 | Frost | Ice Shards | 1 | 0/0/15 |
| 25 | Frost | Shatter | 1 | 0/0/16 |
| 26 | Frost | Improved Frost Nova | 1 | 0/0/17 |
| 27 | Frost | Ice Shards | 1 | 0/0/18 |
| 28-29 | Frost | Shatter | 2 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32 | Frost | Arctic Reach | 1 | 0/0/23 |
| 33 | Frost | Frostbite | 1 | 0/0/24 |
| 34 | Frost | Permafrost | 1 | 0/0/25 |
| 35 | Frost | Arctic Reach | 1 | 0/0/26 |
| 36 | Frost | Frostbite | 1 | 0/0/27 |
| 37 | Frost | Cold Snap | 1 | 0/0/28 |
| 38-39 | Frost | Winter's Chill | 2 | 0/0/30 |
| 40 | Frost | Ice Barrier | 1 | 0/0/31 |
| 41 | Frost | Improved Frost Nova | 1 | 0/0/32 |
| 42-43 | Arcane | Wand Specialization | 2 | 2/0/32 |
| 44-45 | Arcane | Arcane Resilience | 2 | 4/0/32 |
| 46 | Arcane | Improved Channeling | 1 | 5/0/32 |
| 47-49 | Arcane | Arcane Concentration | 3 | 8/0/32 |
| 50 | Arcane | Arcane Subtlety | 1 | 9/0/32 |
| 51 | Arcane | Missile Barrage | 1 | 10/0/32 |
| 52 | Arcane | Arcane Resilience | 1 | 11/0/32 |
| 53-54 | Arcane | Arcane Concentration | 2 | 13/0/32 |
| 55 | Arcane | Arcane Subtlety | 1 | 14/0/32 |
| 56 | Arcane | Magic Absorption | 1 | 15/0/32 |
| 57 | Fire | Incineration | 1 | 15/1/32 |
| 58-60 | Arcane | Arcane Meditation | 3 | 18/1/32 |

## Core talents (priority order)

1. **Shatter** — +3.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Ice Lance** — +3.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ice Barrier** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Frostbolt** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
6. **Frost Channeling** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Arcane Meditation** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
8. **Fingers of Frost** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-21: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Arcane Blast to Magic Absorption at 56 (gate that did nothing, tie-break by utility (survival): +0.0% seed 3, +0.0% seed 4, level-weighted time per kill). Earlier: 2026-11-21: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Missile Barrage to Arcane Resilience at 52 (gate that did nothing, no loss: +0.0% seed 3, -0.0% seed 4, level-weighted time per kill).
- +3.6% faster than the hand draft leveling-frost, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 26.88; leveling-frost 27.86, opt-frost-aoe-leveling-aoe 30.54. The search simulated 66,618 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frost leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/2132151000003-1-052522130120301221-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
