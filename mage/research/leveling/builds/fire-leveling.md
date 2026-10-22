# Fire — Leveling (derived) — 0/32/19

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/32/19 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fire leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Fire build, 30+ points kept in Fire, playing the fire-leveling rotation; the talent order is the stats model's (fire-leveling).

## Point allocation

### Arcane (0)

*No points.*

### Fire (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fire Blast** | 1/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 1 sec and increases its range by 8 yards. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Impact** | 1/3 | changed | Gives your Fire spells a 3% chance to stun the target for 2 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Blast Wave** | 1/1 | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. |
| **Critical Mass** | 5/5 | unchanged | Increases the critical strike chance of your Fire spells by 10%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Permafrost** | 1/3 | changed | Increases the duration of your Chill effects by 11% and reduces the target's speed by an additional 3%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Frost | Elemental Precision | 5 | 0/0/5 |
| 15 | Frost | Permafrost | 1 | 0/0/6 |
| 16-18 | Frost | Frostbite | 3 | 0/0/9 |
| 19 | Frost | Ice Shards | 1 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-24 | Frost | Ice Shards | 4 | 0/0/15 |
| 25 | Frost | Ice Block | 1 | 0/0/16 |
| 26-28 | Frost | Shatter | 3 | 0/0/19 |
| 29 | Fire | Improved Fire Blast | 1 | 0/1/19 |
| 30-33 | Fire | Improved Fireball | 4 | 0/5/19 |
| 34-38 | Fire | Ignite | 5 | 0/10/19 |
| 39-41 | Fire | Burning Soul | 3 | 0/13/19 |
| 42 | Fire | Impact | 1 | 0/14/19 |
| 43 | Fire | Improved Fireball | 1 | 0/15/19 |
| 44-46 | Fire | Improved Scorch | 3 | 0/18/19 |
| 47-48 | Fire | Master of Elements | 2 | 0/20/19 |
| 49 | Fire | Blast Wave | 1 | 0/21/19 |
| 50 | Fire | Master of Elements | 1 | 0/22/19 |
| 51-52 | Fire | Critical Mass | 2 | 0/24/19 |
| 53 | Fire | Pyroblast | 1 | 0/25/19 |
| 54-56 | Fire | Fire Power | 3 | 0/28/19 |
| 57-59 | Fire | Critical Mass | 3 | 0/31/19 |
| 60 | Fire | Combustion | 1 | 0/32/19 |

## Core talents (priority order)

1. **Ice Lance** — The scorer's value in this build: +38.5% of its score (model fire-leveling).
2. **Ignite** — The scorer's value in this build: +10.5% of its score (model fire-leveling).
3. **Fire Power** — The scorer's value in this build: +5.0% of its score (model fire-leveling).
4. **Combustion** — The scorer's value in this build: +3.6% of its score (model fire-leveling).
5. **Elemental Precision** — The scorer's value in this build: +2.1% of its score (model fire-leveling).
6. **Ice Block** — The scorer's value in this build: +1.7% of its score (model fire-leveling).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +2.9% faster than the hand draft opt-fire-leveling-leveling-st, over the 2% replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Fight-lab talent search (fightlab/fl_talent_opt.py): start opt-fire-leveling-leveling-st, moves: 1 point Flame Throwing -> Shatter; 3 points Impact -> Master of Elements; 1 point Flame Throwing -> Impact. Race against opt-fire-leveling-leveling-st over levels 20-60 (seed 3, 3000 fights per level): +2.9% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Hot Streak 1 out; Heating Up 1 in; to be re-optimized.
- 2026-10-15 (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the fastest of three the fight lab raced (the fire-leveling rotation, seed 3, 3000 fights per level, levels 20-60 weighted by level): own tree last 34.4 s per kill; stats model 36.4 s; own tree first 39.7 s.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 0/32/19 -> 0/32/19; Fire Power 5 -> 3 (rank cap); +1 Improved Fire Blast (tier gating for Combustion); +1 Critical Mass (prerequisite of Combustion); +1 Critical Mass (prerequisite of Combustion); -1 Heating Up (over 51); order dropped (order_repair.py) (refill: the fire-leveling model, leveling-st).
- 2026-10-17 (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the fastest of three the fight lab raced (the fire-leveling rotation, seed 3, 3000 fights per level, levels 20-60 weighted by level): own tree last 37.9 s per kill; stats model 40.1 s; own tree first 42.2 s.

## Open questions (verify in the live game)

- A derived Fire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
