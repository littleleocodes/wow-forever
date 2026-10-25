# Optimizer — AoE grinding: Frost Nova -> Blizzard -> Cone of Cold / Arcane Explosion on 5-10 mobs (leveling-aoe) — 5/3/43

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/3/43 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-aoe` and profile `leveling-aoe`: score +72.8% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 1/5 | changed | Improves your chance to hit with Arcane spells by 1%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, your Arcane Missile hits a 10% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |

### Fire (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |

### Frost (43)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 30%. In addition, gives your Frost Ward a 20% chance to reflect Frost spells and effects while active. |
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Improved Blizzard** | 3/3 | changed | Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 40% for 1.5 sec. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Improved Cone of Cold** | 3/3 | changed | Increases the damage dealt by your Cone of Cold spell by 35%. |
| **Winter's Chill** | 3/5 | changed | Gives your Frost damage spells a 60% chance to apply the Winter's Chill effect, which increases the damage done by your Cone of Cold spell to the target by 40%, stacking up to 5 times. |
| **Ice Barrier** | 1/1 | changed | Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10 | Frost | Frost Warding | 1 | 0/0/1 |
| 11 | Frost | Elemental Precision | 1 | 0/0/2 |
| 12 | Frost | Improved Frostbolt | 1 | 0/0/3 |
| 13 | Frost | Frost Warding | 1 | 0/0/4 |
| 14-15 | Frost | Elemental Precision | 2 | 0/0/6 |
| 16-18 | Frost | Permafrost | 3 | 0/0/9 |
| 19 | Frost | Improved Frostbolt | 1 | 0/0/10 |
| 20-22 | Frost | Improved Blizzard | 3 | 0/0/13 |
| 23 | Frost | Ice Lance | 1 | 0/0/14 |
| 24 | Frost | Frost Channeling | 1 | 0/0/15 |
| 25 | Frost | Ice Block | 1 | 0/0/16 |
| 26-27 | Frost | Shatter | 2 | 0/0/18 |
| 28 | Frost | Arctic Reach | 1 | 0/0/19 |
| 29 | Frost | Shatter | 1 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32 | Frost | Arctic Reach | 1 | 0/0/23 |
| 33-35 | Frost | Improved Cone of Cold | 3 | 0/0/26 |
| 36-38 | Frost | Ice Shards | 3 | 0/0/29 |
| 39 | Frost | Cold Snap | 1 | 0/0/30 |
| 40 | Frost | Ice Barrier | 1 | 0/0/31 |
| 41-42 | Frost | Ice Shards | 2 | 0/0/33 |
| 43-44 | Arcane | Missile Barrage | 2 | 2/0/33 |
| 45-47 | Frost | Winter's Chill | 3 | 2/0/36 |
| 48-50 | Frost | Improved Frostbolt | 3 | 2/0/39 |
| 51-52 | Frost | Frost Channeling | 2 | 2/0/41 |
| 53-55 | Fire | Incineration | 3 | 2/3/41 |
| 56 | Arcane | Arcane Focus | 1 | 3/3/41 |
| 57-58 | Arcane | Wand Specialization | 2 | 5/3/41 |
| 59-60 | Frost | Improved Frost Nova | 2 | 5/3/43 |

## Core talents (priority order)

1. **Improved Blizzard** — Removing it costs 8.2 points of score in this model.
2. **Shatter** — Removing it costs 6.8 points of score in this model.
3. **Fingers of Frost** — Removing it costs 5.1 points of score in this model.
4. **Ice Barrier** — Removing it costs 4.8 points of score in this model.
5. **Ice Lance** — Removing it costs 4.1 points of score in this model.
6. **Ice Block** — Removing it costs 3.1 points of score in this model.
7. **Elemental Precision** — Removing it costs 2.5 points of score in this model.
8. **Ice Shards** — Removing it costs 1.8 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level: pull at max range, the mob walks in at 7 yd/s (slowed by chills), swings every 2 s once in melee (pushing casts back), Frost Nova when it arrives, a 2-second step back, Ice Lance/Frostbolt into the freeze, Fire Blast and wand to finish without overkill. Between fights: 2 s loot, 6 s travel, Evocation when low, conjured water below 35% mana, food below 65% health; a death costs 90 s. Every hit, miss, crit, partial resist, chill, freeze, proc and pushback is rolled.

What this build casts per kill ([report](../fightlab/frost-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Wand | 0.7 | 1.6 | 2.3 | 1.9 | 4% |
| Blizzard | 0.7 | 0.8 | 0.8 | 0.7 | 55% |
| Arcane Explosion | 0.8 | 0.8 | 0.6 | 0.5 | 9% |
| Frostbolt | 0.6 | 0.6 | 0.6 | 0.5 | 7% |
| Frost Nova | 0.4 | 0.4 | 0.5 | 0.4 | 3% |
| Ice Lance | 0.2 | 0.4 | 0.5 | 0.3 | 5% |
| Cone of Cold | 0.4 | 0.4 | 0.3 | 0.3 | 13% |
| Fire Blast | 0.2 | 0.2 | 0.2 | 0.2 | 3% |
| Counterspell | 0.1 | 0.2 | 0.2 | 0.1 | 0% |

## Notes

- Allocation and order taken from cand-aoe-r8 on 2026-10-22: an earlier optimizer round beat the last export in the fight lab (31.8s vs 33.9s per kill, level-weighted).
- Report: mage/research/talents/forever/optimizer/frost-aoe-leveling-aoe.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
