# Optimizer — Raid Fireball spam with Scorch upkeep (raid-dps) — 13/33/5

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 13/33/5 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fire-raid` and profile `raid-dps`: score +183.0% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 4/5 | changed | Improves your chance to hit with Arcane spells by 4%. |
| **Wand Specialization** | 1/2 | moved | Increases your damage with Wands by 13%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Geometry** | 1/2 | **NEW** | Increases the range of your Arcane spells by 3 yards. |

### Fire (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 1/3 | changed | Gives your Fire spells a 23% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 10%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 5/5 | unchanged | Increases the critical strike chance of your Fire spells by 10%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |

## Core talents (priority order)

1. **Improved Scorch** — Removing it costs 96.8 points of score in this model.
2. **Fire Power** — Removing it costs 25.7 points of score in this model.
3. **Ignite** — Removing it costs 24.5 points of score in this model.
4. **Improved Fireball** — Removing it costs 22.5 points of score in this model.
5. **Critical Mass** — Removing it costs 16.8 points of score in this model.
6. **Elemental Precision** — Removing it costs 15.9 points of score in this model.
7. **Pyroblast** — Removing it costs 13.0 points of score in this model.
8. **Arcane Concentration** — Removing it costs 12.0 points of score in this model.

## Rank among our builds and the community simulator's

**3 of 8** for `fire-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Fire DPS* | community simulator | - | 518 | +0.0% | 661 | -3.4% | 1 s |
| 2 | [`fire-raid`](fire-raid.md) | ours: hand draft | 12/34/5 | 515 | -0.5% | 685 | +0.0% | 3 s |
| 3 | **[`opt-fire-raid-raid-dps`](opt-fire-raid-raid-dps.md)** | ours: optimizer | 14/32/5 | 515 | -0.5% | 685 | +0.0% | 3 s |
| 4 | *Fire 0/35/16* | community simulator | - | 472 | -8.8% | 638 | -6.8% | 6 s |
| 5 | *Arcane DPS* | community simulator | - | 415 | -19.8% | 506 | -26.1% | 0 s |
| 6 | *Arcane 35/0/16* | community simulator | - | 292 | -43.7% | 373 | -45.6% | 2 s |
| 7 | *Frost 14/0/37* | community simulator | - | 274 | -47.1% | 357 | -47.9% | 1 s |
| 8 | *Frost DPS* | community simulator | - | 271 | -47.7% | 356 | -48.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 4 passes, the last 2026-10-02, 7 changes to the base rotation; third-seed check: ml: Fire 568 -> 607 DPS (+6.9%), fire-raid 563 -> 598 DPS (+6.3%), sim preset: Fire DPS 537 -> 578 DPS (+7.6%)):
  1. move to the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+3.1%, pass 1)
  2. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+3.1%, pass 1)
  3. insert before the filler: if Missile Barrage is up: cast Arcane Missiles (+0.2%, pass 1)
  4. threshold 20% -> 10%: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.5%, pass 2)
  5. insert before the filler: cast Fireball (+0.3%, pass 4)
  6. threshold 5s -> 6s: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.3%, pass 4)
  7. only with 3s or more of the fight left: cast Fireball (+0.2%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 6 passes, the last 2026-10-09, 14 changes to the base rotation; third-seed check: fire-raid 680 -> 688 DPS (+1.2%), sim preset: Fire DPS 662 -> 665 DPS (+0.4%), opt-fire-raid-raid-dps 680 -> 688 DPS (+1.2%)):
  1. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+3.7%, pass 1)
  2. move to the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+2.5%, pass 1)
  3. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.2%, pass 1)
  4. only with 3s or more of the fight left: if mana % ≥ 10%: cast Fireball (+0.2%, pass 2)
  5. move to the top: cast Fire Blast (+0.2%, pass 2)
  6. threshold 5s -> 7.5s: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.4%, pass 2)
  7. insert before the filler: cast Blast Wave (+0.3%, pass 3)
  8. insert before the filler: cast Cone of Cold (+0.3%, pass 3)
  9. insert before the filler: cast Fireball (+0.3%, pass 4)
  10. insert in the middle: if stacks of Heating Up ≥ 2 and (time left in the fight < 6s or time left on Heating Up < 3.5s): cast Pyroblast (+0.2%, pass 5)
  11. drop: cast Fireball (+1.0%, pass 6)
  12. drop 'mana % ≥ 10%' from the condition: if mana % ≥ 10% and time left in the fight ≥ 3s: cast Fireball (+0.4%, pass 6)
  13. insert in the middle: cast Major Mana Potion (+0.3%, pass 6)
  14. move down below 'use every other cooldown when ready': if mana % ≤ 80%: cast Mana Ruby (mana gem) (+0.2%, pass 6)

| # | Priority (the first line whose condition holds is cast) | [`opt-fire-raid-raid-dps`](opt-fire-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s): cast Scorch | 4.4 |
| 2 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 5 | if stacks of Heating Up = 3: cast Pyroblast | 1.5 |
| 6 | cast Fire Blast | 7.0 |
| 7 | if mana % ≥ 10%: cast Fireball | 9.5 |
| 8 | if time left in the fight ≥ 3s: cast Fireball (rank 2) | 5.4 |
| 9 | cast Scorch (rank 1) | 0.2 |

Lines of the simulator's rotation these builds never cast: cast Arcane Missiles (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-fire-raid-raid-dps`](opt-fire-raid-raid-dps.md) |
|---|---|
| Fireball | 48% |
| Fire Blast | 21% |
| Ignite | 11% |
| Pyroblast | 11% |
| Scorch | 8% |

## Notes

- Allocation taken from cand-fire-raid-r1 on 2026-10-03: the optimizer's earlier round beat its last export in the community simulator (559 vs 527 DPS; the calibration moved the model past the better build).
- Report: mage/research/talents/forever/optimizer/fire-raid-raid-dps.md
- 2026-10-16 (repair_builds.py, client build 70425 trees): 14/32/5 -> 13/33/5; Wake of Fire -> Improved Fire Blast (renamed); Fire Power 5 -> 3 (rank cap); +1 Burning Soul (tier gating for Combustion); +1 Critical Mass (prerequisite of Combustion); +1 Critical Mass (prerequisite of Combustion); -1 Wand Specialization (over 51) (refill: the fire-raid model, raid-dps).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
