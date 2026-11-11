# Optimizer — Raid Frostbolt with Ice Lance on Fingers of Frost charges (the ice_lance source, 2026-09-27) (raid-dps) — 29/0/22

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/0/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-raid` and profile `raid-dps`: score +70.0% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Fire (0)

*No points.*

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 2/3 | moved | Reduces the mana cost of your Frost spells by 10% and reduces the threat caused by your Frost spells by 20%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Core talents (priority order)

1. **Improved Frostbolt** — Removing it costs 18.6 points of score in this model.
2. **Fingers of Frost** — Removing it costs 11.4 points of score in this model.
3. **Ice Shards** — Removing it costs 11.3 points of score in this model.
4. **Arcane Mind** — Removing it costs 10.5 points of score in this model.
5. **Missile Barrage** — Removing it costs 9.6 points of score in this model.
6. **Arcane Instability** — Removing it costs 9.0 points of score in this model.
7. **Ice Lance** — Removing it costs 8.6 points of score in this model.

## Rank among our builds and the community simulator's

**3 of 15** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 564 | +0.0% | 659 | -3.3% | 7 s |
| 2 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 32/3/16 | 561 | -0.6% | 670 | -1.7% | 3 s |
| 3 | **[`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md)** | ours: optimizer | 29/0/22 | 559 | -0.9% | 666 | -2.3% | 7 s |
| 4 | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) | ours: derived (open search) | 28/10/13 | 529 | -6.2% | 682 | +0.0% | 5 s |
| 5 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 21/0/30 | 506 | -10.3% | 601 | -11.9% | 8 s |
| 6 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 503 | -10.9% | 568 | -16.8% | 0 s |
| 7 | *Arcane Fire* | community simulator | - | 493 | -12.5% | 629 | -7.7% | 2 s |
| 8 | *Arcane* | community simulator | - | 493 | -12.6% | 643 | -5.7% | 2 s |
| 9 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 451 | -20.1% | 514 | -24.7% | 0 s |
| 10 | *Frost Med* | community simulator | - | 451 | -20.1% | 536 | -21.5% | 7 s |
| 11 | *Frost Incin* | community simulator | - | 443 | -21.4% | 540 | -20.8% | 9 s |
| 12 | *Fire Skyborne GT 180* | community simulator | - | 422 | -25.3% | 488 | -28.5% | 5 s |
| 13 | *Fire Skyborne LT 180* | community simulator | - | 418 | -25.9% | 490 | -28.2% | 7 s |
| 14 | *Fire* | community simulator | - | 416 | -26.2% | 488 | -28.5% | 7 s |
| 15 | *FFB* | community simulator | - | 390 | -30.9% | 443 | -35.1% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 5 passes, the last 2026-10-23, 12 changes to the base rotation; third-seed check: open winner 528 -> 577 DPS (+9.3%), opt-frost-raid-raid-dps-extwc 549 -> 586 DPS (+6.8%), sim preset: Arcane Frost 516 -> 582 DPS (+12.8%), frost-arcane-power-raid 515 -> 577 DPS (+12.2%), frost-winters-chill-raid 436 -> 441 DPS (+1.1%), frost-fingers-of-frost-raid 480 -> 484 DPS (+0.8%), opt-frost-raid-raid-dps 532 -> 566 DPS (+6.4%), frost-ml-raid 478 -> 482 DPS (+0.8%), arcane-frost-open-raid 543 -> 576 DPS (+6.2%)):
  1. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.3%, pass 1)
  2. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  3. repair: insert before the filler: if mana % < 5% and time left in the fight > 25s: cast Evocation (every frost-raid build raced, 20,000 fights, seed 3: opt-frost-raid-raid-dps-extwc +6.6%, the others -0.02% to +0.00%) (+6.6%, pass 2)
  4. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast (+0.6%, pass 3)
  5. threshold 80% -> 60%: if mana % ≤ 80%: cast Mana Ruby (mana gem) (+0.2%, pass 4)
  6. threshold 25s -> 50s: if mana % < 5% and time left in the fight > 25s: cast Evocation (+0.2%, pass 4)
  7. insert at the end: cast Arcane Blast (+0.2%, pass 4)
  8. insert in the middle: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+10.2%, pass 5)
  9. insert at the end: cast Robe of the Archmage (+0.9%, pass 5)
  10. insert in the middle: if Arcane Wrath is ready: cast Presence of Mind (+0.7%, pass 5)
  11. move down below 'if Fingers of Frost is up: cast Ice Lance': if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) (+0.2%, pass 5)
  12. only above 60% mana: if mana % ≤ 60%: cast Mana Ruby + insert at the end: cast Frost Blast (+0.2%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 10 passes, the last 2026-10-31, 6 changes to the base rotation; third-seed check: arcane-frost-open-raid 558 -> 671 DPS (+20.3%), sim preset: Arcane 464 -> 632 DPS (+36.3%), frost-arcane-power-raid 575 -> 660 DPS (+14.7%), frost-winters-chill-raid 515 -> 520 DPS (+0.8%), frost-fingers-of-frost-raid 574 -> 573 DPS (-0.3%), opt-frost-raid-raid-dps 618 -> 661 DPS (+6.9%), opt-frost-raid-raid-dps-extwc 616 -> 650 DPS (+5.5%), frost-ml-raid 569 -> 597 DPS (+5.0%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%, pass 1)
  3. spell probe: insert in the middle: cast Arcane Wrath (+1.0%, pass 6)
  4. insert at the top: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+6.1%, pass 7)
  5. move to the top: if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) (+2.2%, pass 7)
  6. only with 20s or more of the fight left: cast Arcane Wrath (+0.4%, pass 7)

| # | Priority (the first line whose condition holds is cast) | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60% and mana % ≥ 60%: cast Mana Ruby | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Fingers of Frost is up: cast Ice Lance | 1.3 |
| 4 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) | 4.5 |
| 5 | if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast | 8.2 |
| 6 | if mana % < 5% and time left in the fight > 50s: cast Evocation | 0.1 |
| 7 | if time left in the fight ≥ 3s: cast Frostbolt (rank 10) | 12.4 |
| 8 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.1 |
| 9 | cast Arcane Blast | 8.2 |
| 10 | cast Robe of the Archmage | as ready |

Lines of the simulator's rotation these builds never cast: cast Presence of Mind, cast spell 1326055 (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) |
|---|---|
| Frostbolt | 45% |
| Arcane Missiles | 31% |
| Arcane Blast | 16% |
| Ice Lance | 7% |
| Demonic Rune | 2% |
| Fire Blast | 0% |

## Notes

- Report: mage/research/talents/forever/optimizer/frost-raid-raid-dps.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 29/0/22 -> 29/0/22; Arcane Focus 5 gone; Elemental Precision -> Precision (renamed); +1 Arcane Concentration (tier gating for Arcane Mind); +1 Arcane Concentration (tier gating for Arcane Mind); +1 Arcane Concentration (tier gating for Arcane Mind); +1 Arcane Concentration (tier gating for Arcane Mind); +1 Arcane Blast (tier gating for Arcane Mind) (refill: the frost-raid model, raid-dps).
- 2026-11-09 page audit: core entries for talents the allocation no longer holds removed (Elemental Precision; a tree change or a repair took them out).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
