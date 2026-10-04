# Optimizer — Raid Frostbolt with Ice Lance on Fingers of Frost charges (the ice_lance source, 2026-09-27) (raid-dps) — 22/0/29

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/0/29 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-raid` and profile `raid-dps`: score +76.6% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Wand Specialization** | 1/2 | moved | Increases your damage with Wands by 13%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Missile Barrage** | 1/1 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 1/5 | changed | Increases your Intellect by 2% and increases the critical strike damage bonus of your Arcane spells by 20%. |

### Fire (0)

*No points.*

### Frost (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Improved Cone of Cold** | 1/3 | changed | Increases the damage dealt by your Cone of Cold spell by 12%. |
| **Winter's Chill** | 4/5 | changed | Gives your Frost damage spells a 80% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 4 times. |

## Core talents (priority order)

1. **Improved Frostbolt** — Removing it costs 22.4 points of score in this model.
2. **Ice Shards** — Removing it costs 20.2 points of score in this model.
3. **Fingers of Frost** — Removing it costs 19.2 points of score in this model.
4. **Ice Lance** — Removing it costs 12.6 points of score in this model.
5. **Winter's Chill** — Removing it costs 11.4 points of score in this model.
6. **Shatter** — Removing it costs 10.8 points of score in this model.
7. **Piercing Ice** — Removing it costs 8.7 points of score in this model.
8. **Elemental Precision** — Removing it costs 8.6 points of score in this model.

## Rank among our builds and the community simulator's

**3 of 12** for `frost-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-ml-raid`](frost-ml-raid.md) | ours: hand draft | 21/0/30 | 617 | +0.0% | 705 | +0.0% | 0 s |
| 2 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 615 | -0.4% | 701 | -0.6% | 0 s |
| 3 | **[`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md)** | ours: optimizer | 22/0/29 | 614 | -0.6% | 701 | -0.7% | 1 s |
| 4 | *Frost DPS* | community simulator | - | 576 | -6.7% | 660 | -6.4% | 0 s |
| 5 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 32/0/19 | 575 | -6.8% | 660 | -6.5% | 0 s |
| 6 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 1/13/37 | 564 | -8.6% | 675 | -4.3% | 7 s |
| 7 | *Frost 14/0/37* | community simulator | - | 560 | -9.3% | 670 | -5.0% | 8 s |
| 8 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 548 | -11.1% | 626 | -11.2% | 0 s |
| 9 | *Arcane 35/0/16* | community simulator | - | 493 | -20.1% | 567 | -19.7% | 0 s |
| 10 | *Arcane DPS* | community simulator | - | 430 | -30.3% | 489 | -30.7% | 0 s |
| 11 | *Fire 0/35/16* | community simulator | - | 387 | -37.2% | 448 | -36.4% | 0 s |
| 12 | *Fire DPS* | community simulator | - | 324 | -47.5% | 369 | -47.7% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 2 passes, the last 2026-10-02, 3 changes to the base rotation; third-seed check: ):
  1. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.3%, pass 1)
  2. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  3. repair: insert before the filler: if mana % < 5% and time left in the fight > 25s: cast Evocation (every frost-raid build raced, 20,000 fights, seed 3: opt-frost-raid-raid-dps-extwc +6.6%, the others -0.02% to +0.00%) (+6.6%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 2 changes to the base rotation; third-seed check: ml: Frost 731 -> 737 DPS (+0.8%), ml: Hybrid Arcane/Frost 728 -> 735 DPS (+1.0%), frost-fingers-of-frost-raid 728 -> 735 DPS (+1.0%), sim preset: Frost DPS 687 -> 691 DPS (+0.6%), frost-arcane-power-raid 689 -> 693 DPS (+0.6%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%)

| # | Priority (the first line whose condition holds is cast) | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles | 3.6 |
| 4 | if Fingers of Frost is up: cast Ice Lance | 4.5 |
| 5 | cast Frostbolt | 17.8 |

Lines of the simulator's rotation these builds never cast: cast Evocation (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) |
|---|---|
| Frostbolt | 60% |
| Ice Lance | 21% |
| Arcane Missiles | 20% |

## Notes

- Allocation taken from cand-frost-raid-r1 on 2026-10-03: the optimizer's earlier round beat its last export in the community simulator (614 vs 584 DPS; the calibration moved the model past the better build).
- Report: mage/research/talents/forever/optimizer/frost-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
