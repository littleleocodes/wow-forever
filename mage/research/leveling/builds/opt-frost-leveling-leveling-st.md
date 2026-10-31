# Optimizer — Single-target Frostbolt leveling: Frostbolt ~70%, Fire Blast/Frost Nova instants, wand finishes (leveling-st) — 22/3/26

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/3/26 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-leveling` and profile `leveling-st`: score +57.1% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 2/3 | changed | Increases your Armor by an amount equal to 100% of your Intellect. *(est. — extrapolated from rank 1)* |
| **Improved Channeling** | 1/5 | **NEW** | Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, Frost Blast, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 15% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 15 sec from time of initial application. |
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
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Arctic Reach** | 1/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

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

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-22, on top of the priority below): never cast Cone of Cold; Frostbolt only while the mob has more than 20% health; Fire Blast only while the mob has more than 10% health. Together +3.7% time per kill saved for `leveling-frost` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/frost-leveling.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Ice Lance | 2.7 | 3.5 | 4.2 | 3.5 | 3.2 | 55% |
| Frostbolt | 2.7 | 2.0 | 1.8 | 1.8 | 1.9 | 28% |
| Fire Blast | 0.9 | 1.6 | 1.6 | 1.3 | 1.1 | 14% |
| Wand | 0.3 | 0.7 | 1.0 | 0.7 | 0.9 | 2% |
| Frost Nova | 0.5 | 0.8 | 0.8 | 0.7 | 0.6 | 1% |
| Counterspell | 0.0 | 0.2 | 0.1 | 0.1 | 0.1 | 0% |

## Notes

- Report: mage/research/talents/forever/optimizer/frost-leveling-leveling-st.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 21/3/27 -> 22/3/26; Arcane Focus 1 gone; Elemental Precision -> Precision (renamed); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Improved Channeling (tier gating for Arcane Concentration); -1 Precision (over 51); order dropped (order_repair.py) (refill: the frost-leveling model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
