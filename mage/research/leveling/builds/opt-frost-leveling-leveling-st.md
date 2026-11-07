# Optimizer — Single-target Frostbolt leveling: Frostbolt ~70%, Fire Blast/Frost Nova instants, wand finishes (leveling-st) — 22/3/26

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/3/26 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-leveling` and profile `leveling-st`: score +57.1% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 2/3 | changed | Increases your Armor by an amount equal to 50% of your Intellect. |
| **Improved Channeling** | 1/5 | **NEW** | Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |

### Fire (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |

### Frost (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 1/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
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
| 26 | Frost | Ice Block | 1 | 0/0/17 |
| 27 | Frost | Ice Shards | 1 | 0/0/18 |
| 28-29 | Frost | Shatter | 2 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32-34 | Frost | Ice Shards | 3 | 0/0/25 |
| 35 | Frost | Arctic Reach | 1 | 0/0/26 |
| 36-37 | Arcane | Wand Specialization | 2 | 2/0/26 |
| 38-39 | Arcane | Arcane Resilience | 2 | 4/0/26 |
| 40 | Arcane | Improved Channeling | 1 | 5/0/26 |
| 41-43 | Arcane | Arcane Concentration | 3 | 8/0/26 |
| 44-45 | Arcane | Missile Barrage | 2 | 10/0/26 |
| 46-47 | Arcane | Arcane Concentration | 2 | 12/0/26 |
| 48-49 | Arcane | Arcane Subtlety | 2 | 14/0/26 |
| 50 | Arcane | Arcane Blast | 1 | 15/0/26 |
| 51 | Arcane | Arcane Wrath | 1 | 16/0/26 |
| 52-54 | Arcane | Arcane Meditation | 3 | 19/0/26 |
| 55 | Arcane | Magic Absorption | 1 | 20/0/26 |
| 56 | Arcane | Presence of Mind | 1 | 21/0/26 |
| 57-59 | Fire | Incineration | 3 | 21/3/26 |
| 60 | Arcane | Magic Absorption | 1 | 22/3/26 |

## Core talents (priority order)

1. **Ice Lance** — Removing it costs 11.4 points of score in this model.
2. **Shatter** — Removing it costs 8.1 points of score in this model.
3. **Ice Shards** — Removing it costs 4.4 points of score in this model.
4. **Frostbite** — Removing it costs 2.6 points of score in this model.
5. **Fingers of Frost** — Removing it costs 2.3 points of score in this model.
6. **Frost Channeling** — Removing it costs 1.8 points of score in this model.
7. **Arcane Concentration** — Removing it costs 1.5 points of score in this model.
8. **Improved Frostbolt** — Removing it costs 1.3 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level: pull at max range, the mob walks in at 7 yd/s (slowed by chills), swings every 2 s once in melee (pushing casts back), Frost Nova when it arrives, a 2-second step back, Ice Lance/Frostbolt into the freeze, Fire Blast and wand to finish without overkill. Between fights: 2 s loot, 6 s travel, Evocation when low, conjured water below 35% mana, food below 65% health; a death costs 90 s. Every hit, miss, crit, partial resist, chill, freeze, proc and pushback is rolled.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-11-03, on top of the priority below): Frostbolt only while the mob has more than 20% health; never cast Cone of Cold; Fire Blast only when the mob is below 20% health; drink below 15% mana; Fire Blast only while the mob has more than 10% health. Together +5.5% time per kill saved for `leveling-frost` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/frost-leveling.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Frostbolt | 3.9 | 4.1 | 4.1 | 3.4 | 3.2 | 52% |
| Wand | 0.8 | 1.2 | 1.7 | 1.6 | 1.7 | 4% |
| Ice Lance | 1.2 | 1.7 | 1.8 | 1.7 | 1.6 | 36% |
| Frost Nova | 0.5 | 0.8 | 0.8 | 0.7 | 0.6 | 1% |
| Fire Blast | 0.5 | 0.6 | 0.5 | 0.5 | 0.4 | 6% |
| Counterspell | 0.0 | 0.2 | 0.1 | 0.1 | 0.1 | 0% |

## Notes

- Report: mage/research/talents/forever/optimizer/frost-leveling-leveling-st.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 21/3/27 -> 22/3/26; Arcane Focus 1 gone; Elemental Precision -> Precision (renamed); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Improved Channeling (tier gating for Arcane Concentration); -1 Precision (over 51); order dropped (order_repair.py) (refill: the frost-leveling model, leveling-st).
- 2026-11-06 (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the fastest of three the fight lab raced (the frost-leveling rotation, seed 3, 3000 fights per level, levels 20-60 weighted by level): own tree first 31.2 s per kill; stats model 31.4 s; own tree last 37.9 s.

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
