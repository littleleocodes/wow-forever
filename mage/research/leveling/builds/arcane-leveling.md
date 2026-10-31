# Arcane — Leveling (derived) — 29/0/22

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/0/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Arcane build, 30+ points kept in Arcane, playing the arcane-leveling rotation; the talent order is the stats model's (frost-leveling).

## Point allocation

### Arcane (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 2/3 | changed | Increases your Armor by an amount equal to 100% of your Intellect. *(est. — extrapolated from rank 1)* |
| **Improved Channeling** | 1/5 | **NEW** | Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 1/2 | changed | Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Shielding** | 1/2 | **NEW** | Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 17% and increases the resistances granted by your Mage Armor spell by 25%. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Fire (0)

*No points.*

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Core talents (priority order)

1. **Ice Lance** — The scorer's value in this build: +21.2% of its score (model frost-leveling).
2. **Shatter** — The scorer's value in this build: +12.5% of its score (model frost-leveling).
3. **Ice Shards** — The scorer's value in this build: +8.5% of its score (model frost-leveling).
4. **Frostbite** — The scorer's value in this build: +6.4% of its score (model frost-leveling).
5. **Improved Frostbolt** — The scorer's value in this build: +3.1% of its score (model frost-leveling).
6. **Fingers of Frost** — The scorer's value in this build: +2.7% of its score (model frost-leveling).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Fight-lab talent search (fightlab/fl_talent_opt.py): start arcane-leveling, moves: 2 points Improved Counterspell -> Arcane Impact; 1 point Magic Absorption -> Arcane Impact. Race against arcane-leveling over levels 20-60 (seed 3, 3000 fights per level): +0.3% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.
- 2026-10-22 (repair_builds.py, client build 70425 trees): 30/0/21 -> 30/0/21; Piercing Ice 2 gone; +1 Elemental Precision (tier gating for Ice Block); +1 Elemental Precision (tier gating for Fingers of Frost); order dropped (order_repair.py) (refill: the frost-leveling model, leveling-st).
- 2026-10-22 (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the fastest of three the fight lab raced (the arcane-leveling rotation, seed 3, 3000 fights per level, levels 20-60 weighted by level): stats model 36.1 s per kill; own tree first 38.0 s; own tree last 36.1 s.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 30/0/21 -> 29/0/22; Arcane Focus 3 gone; Elemental Precision -> Precision (renamed); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Improved Channeling (tier gating for Arcane Concentration); refill +1 Fingers of Frost; order dropped (order_repair.py) (refill: the frost-leveling model, leveling-st).

## Open questions (verify in the live game)

- A derived Arcane leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
