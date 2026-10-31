# Optimizer — AoE grinding: Frost Nova -> Blizzard -> Cone of Cold / Arcane Explosion on 5-10 mobs (leveling-aoe) — 7/3/41

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/3/41 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-aoe` and profile `leveling-aoe`: score +72.8% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 2/3 | changed | Increases your Armor by an amount equal to 100% of your Intellect. *(est. — extrapolated from rank 1)* |
| **Improved Channeling** | 1/5 | **NEW** | Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, Frost Blast, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |

### Fire (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |

### Frost (41)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Improved Frostbolt** | 4/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.4 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
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
| **Winter's Chill** | 3/5 | changed | Gives your Frostbolt, Frost Blast, and Fingers of Frost empowered Ice Lance spells a 60% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 5% and it gains an additional 7% of your spell damage, stacking up to 5 times. |
| **Ice Barrier** | 1/1 | changed | Shield yourself, absorbing 447 damage and increasing your Frost damage by 3% for 1 min. While shielded, your Frost damage is increased by an additional 3% and you do not lose casting time when you take damage. |

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
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 5/3/43 -> 7/3/41; Arcane Focus 1 gone; Elemental Precision -> Precision (renamed); +1 Arcane Resilience (tier gating for Missile Barrage); +1 Arcane Resilience (tier gating for Missile Barrage); +1 Improved Channeling (tier gating for Missile Barrage); -1 Precision (over 51); -1 Improved Frostbolt (over 51); order dropped (order_repair.py) (refill: the frost-aoe model, leveling-aoe).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
