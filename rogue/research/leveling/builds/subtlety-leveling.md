# Subtlety — Leveling (derived) — 5/16/30

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/16/30 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Subtlety leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Subtlety build, 30+ points kept in Subtlety, playing the subtlety-leveling rotation; the talent order is the stats model's (combat-swords-raid).

## Point allocation

### Assassination (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 3/5 | changed | Increases your critical strike chance with all attacks and Poisons by 3%. |
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |

### Combat (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |

### Subtlety (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 3/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 12%. |
| **Setup** | 3/3 | changed | Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Camouflage** | 3/3 | changed | Grants 15% increased movement speed in stealth and reduces stealth's cooldown by 6 seconds. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |
| **Heightened Senses** | 2/2 | changed | Increases your Stealth detection as if you were 3 levels higher and reduces your chance to be hit by spells and ranged attacks by 4%. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |

## Core talents (priority order)

1. **Riposte** — The scorer's value in this build: +11.5% of its score (model combat-swords-raid).
2. **Improved Sinister Strike** — The scorer's value in this build: +7.6% of its score (model combat-swords-raid).
3. **Serrated Blades** — The scorer's value in this build: +7.4% of its score (model combat-swords-raid).
4. **Flawless Execution** — The scorer's value in this build: +7.4% of its score (model combat-swords-raid).
5. **Precision** — The scorer's value in this build: +7.1% of its score (model combat-swords-raid).
6. **Remorseless Attacks** — The scorer's value in this build: +7.0% of its score (model combat-swords-raid).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Fight-lab talent search (fightlab/fl_talent_opt.py): start subtlety-leveling, moves: none (the start was already the best the search found). Race against subtlety-leveling over levels 20-60 (seed 3, 3000 fights per level): +0.0% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 5/16/30 -> 5/16/30; Improved Eviscerate -> Coup de Grace (renamed); Improved Sinister Strike -> Efficient Strikes (renamed); Quietus 5 gone; +1 Improved Ambush (back into Subtlety); +1 Improved Ambush (back into Subtlety); +1 Improved Ambush (back into Subtlety); +1 Camouflage (back into Subtlety); +1 Opportunity (back into Subtlety); order dropped (order_repair.py) (refill: the combat-daggers-raid model, leveling-st).

## Open questions (verify in the live game)

- A derived Subtlety leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
