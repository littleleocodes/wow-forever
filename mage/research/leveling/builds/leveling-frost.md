# Leveling — Frost (Ice Lance at 20, Shatter at 25, Ice Barrier at 40) — 17/0/34

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/0/34 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-30 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `leveling-frost` |

## Summary

Classic Frost leveling was Frostbolt/Ice Shards early, Shatter at 30, Ice Block at 34 and Ice Barrier at 43. Forever pulls the burst forward: Ice Lance arrives at 20 (Frost Nova -> step back -> Ice Lance, 4x damage on a Frozen target and ~60% of all leveling damage in the fight lab), Shatter at 25-27, Fingers of Frost at 30, Ice Block at 32 and Ice Barrier at 40. Ends in the Forever Fingers of Frost raid build (12/0/39) — no respec.

## Point allocation

### Arcane (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 2/3 | changed | Increases your Armor by an amount equal to 50% of your Intellect. |
| **Improved Channeling** | 1/5 | **NEW** | Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, Frost Blast, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 15% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 15 sec from time of initial application. |
| **Arcane Meditation** | 1/3 | changed | Allows 17% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |

### Fire (0)

*No points.*

### Frost (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Arctic Reach** | 1/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, Ice Lance and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Winter's Chill** | 5/5 | changed | Gives your Frostbolt, Frost Blast, and Fingers of Frost empowered Ice Lance spells a 100% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times. |
| **Ice Barrier** | 1/1 | changed | Shield yourself, absorbing 447 damage and increasing your Frost damage by 15% for 1 min. While shielded, your Frost damage is increased by an additional 5% and you do not lose casting time when you take damage. |

## Core talents (priority order)

1. **Improved Frostbolt** — Still 5/5 but no longer the opening points: the fight lab values it at ~3% per kill once Ice Lance carries the damage, so it comes at 44-48 after Ice Barrier.
2. **Ice Shards** — Unchanged +100% Frost crit damage.
3. **Ice Lance** — New at 20: instant, 300% damage on Frozen targets — Frost Nova -> Ice Lance replaces the Classic Nova -> Frostbolt burst and needs no cast.
4. **Ice Block** — The 16-point talent, taken at 32 after Shatter and Fingers of Frost: the sim has no bad pulls to block, and Shatter is worth ~20% per kill.
5. **Shatter** — 3 ranks for est. +51% crit vs. Frozen — 2 points cheaper than Classic.
6. **Fingers of Frost** — New: chills grant a 'Frozen' cast (est. 30% at 2/2) — Shatter-crit Frostbolts on mobs that are not novaed.
7. **Frostbite** — Random freezes from chills (est. 15%) feed Shatter and Ice Lance; more valuable in Forever than in Classic.
8. **Cold Snap** — Second Ice Block/Nova; Ice Barrier prerequisite (moved to tier 5).
9. **Ice Barrier** — Level-40 milestone; requires Cold Snap now.
10. **Elemental Precision** — Hit; 5 ranks now, so it is spread across 37-47 rather than taken in one go.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Winter's Chill (41-45) | Improved Blizzard 3 + Permafrost 2 (AoE grinding) | Winter's Chill only buffs Frostbolt/Ice Lance crit in Forever and its stack count is unclear; AoE grinders should take Improved Blizzard/Permafrost here instead and respec at 60. |
| 3 | Frost Channeling | Permafrost | Mana vs. longer slows. |

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level: pull at max range, the mob walks in at 7 yd/s (slowed by chills), swings every 2 s once in melee (pushing casts back), Frost Nova when it arrives, a 2-second step back, Ice Lance/Frostbolt into the freeze, Fire Blast and wand to finish without overkill. Between fights: 2 s loot, 6 s travel, Evocation when low, conjured water below 35% mana, food below 65% health; a death costs 90 s. Every hit, miss, crit, partial resist, chill, freeze, proc and pushback is rolled.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-22, on top of the priority below): never cast Cone of Cold; Frostbolt only while the mob has more than 20% health; Fire Blast only while the mob has more than 10% health. Together +3.7% time per kill saved for `leveling-frost` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/frost-leveling.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Ice Lance | 2.7 | 3.5 | 4.1 | 3.4 | 3.3 | 55% |
| Frostbolt | 2.7 | 2.0 | 2.1 | 2.0 | 1.9 | 27% |
| Fire Blast | 0.9 | 1.6 | 1.5 | 1.2 | 1.2 | 14% |
| Wand | 0.3 | 0.7 | 1.3 | 0.9 | 0.9 | 2% |
| Frost Nova | 0.5 | 0.8 | 0.8 | 0.7 | 0.6 | 1% |
| Counterspell | 0.0 | 0.2 | 0.1 | 0.1 | 0.1 | 0% |

## Notes

- Rotation: Frostbolt -> Frost Nova when the mob reaches you -> Ice Lance (x2 if Fingers of Frost procs) -> Frostbolt; Cone of Cold to re-snare.
- Arcane Concentration and the Arcane fillers are left for 49-60 because nothing in Arcane speeds up a kill.
- Order revised 2026-09-26 from the fight lab (fightlab/candidates/cand-hand-revised.json raced against the old order with the same seeds): Elemental Precision, Frostbite and Ice Shards first so that Ice Lance lands at 20 and Shatter at 25-27 — 7% faster per kill at 20, 13% at 25, 6% at 30, the same from 40 on. Improved Frostbolt first instead (cand-hand-revised-2) ties within noise.
- The optimizer's opt-frost-leveling-leveling-st (12/3/36, same Arcane points) ends 2-3% faster at 50-60 in the sim by swapping Arctic Reach and four Winter's Chill points for Incineration and Improved Cone of Cold, and is 6% slower at 30 because its order buys Frost Channeling before Ice Shards.
- 2026-10-22 (repair_builds.py, client build 70425 trees): 12/0/39 -> 17/0/34; Elemental Precision 5 -> 3 (rank cap); Piercing Ice 3 gone; refill +1 Arcane Blast, +2 Missile Barrage, +1 Arcane Wrath, +1 Arcane Meditation; order dropped (order_repair.py) (refill: the frost-leveling model, leveling-st).
- 2026-10-22 (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the fastest of three the fight lab raced (the frost-leveling rotation, seed 3, 3000 fights per level, levels 20-60 weighted by level): own tree first 31.2 s per kill; stats model 31.6 s; own tree last 37.2 s.
- Fight lab (leveling/fightlab/frost-leveling.md, 2026-10-30, generated by render_fightlab_sections.py): time per kill at L20/30/40/50/60 = 27/34/36/31/29 s with Classic 1.12 creature stats and quest greens; the optimizer's opt-frost-leveling-leveling-st is -4% at 60 and +0% at 30 (negative = faster); race winner over the leveling: cand-frost-r4; top talents at 60: Ice Lance +16%, Shatter +16%, Ice Shards +8%, Frostbite +6%; about zero: Arcane Blast, Arcane Focus, Arcane Resilience, Arcane Subtlety, Arcane Wrath, Ice Block. See the Fight lab section of leveling/README.md.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 17/0/34 -> 17/0/34; Arcane Focus 3 gone; Elemental Precision -> Precision (renamed); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Improved Channeling (tier gating for Arcane Concentration); order dropped (order_repair.py) (refill: the frost-leveling model, leveling-st).

## Open questions (verify in the live game)

- Fingers of Frost proc rate at rank 2 (extrapolated) and whether it triggers off Frostbolt's own chill.
- Ice Lance base damage at each rank (demo shows 28-33 at level 38 — low; its value is the 300% Frozen multiplier).
- Fight lab (2026-09-25, beta numbers): Ice Lance on a Frozen target (Frost Nova, Frostbite, Fingers of Frost) is 4x damage for an instant, so Nova -> step back -> Ice Lance x2 makes Ice Lance ~40-55% of all leveling damage from 30 on and Shatter/Fingers of Frost/Frostbite the best talents; testable at the level-20 cap now: does Ice Lance rank 1 hit a Frost-Nova'd mob for ~120 (4 x 28-32) and how often do the first two Ice Lances break the root?

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
