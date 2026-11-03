# Arcane-Frost — Raid (open talent search) — 28/10/13

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 28/10/13 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane-Frost (an Arcane/Frost hybrid) raid build the open talent search found on 2026-11-01: every legal 51-point build with no tree rule, searched in the community simulator's frost-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.5% over opt-frost-raid-raid-dps, the best of our builds in that rotation.

## Point allocation

### Arcane (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 2/5 | **NEW** | Gives your Arcane Missiles spell a 40% chance and your Arcane Blast and Arcane Wrath spells a 28% chance to not lose casting time when you take damage. |
| **Arcane Resilience** | 3/3 | changed | Increases your Armor by an amount equal to 75% of your Intellect. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 4/5 | unchanged | Gives you a 8% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |

### Fire (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |

### Frost (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |

## Core talents (priority order)

1. **Missile Barrage** — 107 DPS lost without it (16% of the build in a full raid; removal, 12,000 fights).
2. **Arcane Blast** — 70 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
3. **Arcane Mind** — 58 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
4. **Precision** — 44 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
5. **Improved Frostbolt** — 37 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Arcane Instability** — 35 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Arcane Wrath** — 32 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Arcane Impact** — 22 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**4 of 13** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever bac92db (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 552 | +0.0% | 661 | -1.5% | 5 s |
| 2 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 546 | -1.0% | 650 | -3.0% | 9 s |
| 3 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 32/3/16 | 544 | -1.4% | 660 | -1.6% | 7 s |
| 4 | **[`arcane-frost-open-raid`](arcane-frost-open-raid.md)** | ours: derived (open search) | 28/10/13 | 525 | -4.9% | 670 | +0.0% | 4 s |
| 5 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 506 | -8.4% | 572 | -14.7% | 0 s |
| 6 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 21/0/30 | 502 | -9.1% | 597 | -10.9% | 5 s |
| 7 | *Arcane Fire* | community simulator | - | 482 | -12.7% | 619 | -7.7% | 6 s |
| 8 | *Arcane* | community simulator | - | 482 | -12.7% | 631 | -5.9% | 6 s |
| 9 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 457 | -17.2% | 519 | -22.6% | 0 s |
| 10 | *Frost Incin* | community simulator | - | 454 | -17.9% | 544 | -18.9% | 4 s |
| 11 | *Frost Med* | community simulator | - | 444 | -19.6% | 540 | -19.5% | 9 s |
| 12 | *Fire* | community simulator | - | 408 | -26.0% | 487 | -27.4% | 8 s |
| 13 | *FFB* | community simulator | - | 387 | -30.0% | 446 | -33.4% | 2 s |

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

| # | Priority (the first line whose condition holds is cast) | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60% and mana % ≥ 60%: cast Mana Ruby | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) | 4.5 |
| 4 | if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast | 8.3 |
| 5 | if mana % < 5% and time left in the fight > 50s: cast Evocation | 0.3 |
| 6 | if time left in the fight ≥ 3s: cast Frostbolt (rank 10) | 12.9 |
| 7 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.1 |
| 8 | cast Arcane Blast | 8.3 |
| 9 | cast Robe of the Archmage | as ready |

Lines of the simulator's rotation these builds never cast: cast Ice Lance (needs the Ice Lance talent); cast Presence of Mind (needs the Presence of Mind talent); cast spell 1326055 (its condition never held in these fights).

Damage by ability:

| Ability | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) |
|---|---|
| Frostbolt | 48% |
| Arcane Missiles | 32% |
| Arcane Blast | 18% |
| Demonic Rune | 2% |
| Fire Blast | 0% |

## Notes

- +1.6% over the best hand draft of the spec, frost-arcane-power-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (frost-raid, full raid): 28/10/13 (Arcane-Frost (an Arcane/Frost hybrid)) at 670.9 DPS; opt-frost-raid-raid-dps 661.1, arcane-frost-open-raid 660.9, frost-arcane-power-raid 660.5, opt-frost-raid-raid-dps-extwc 649.1, frost-ml-raid 597.5, frost-fingers-of-frost-raid 573.0, frost-winters-chill-raid 519.7 in the same fights; 2,665 builds simulated, 1 independent runs reached the top.
- The frost-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): fire-raid -36.8%, arcane-dps -0.3%, frostfire-raid -35.4%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Improved Channeling, Arcane Resilience, Arcane Geometry, Improved Counterspell.
- Simulator numbers are the community's model of the beta (wowsims/forever 54ceac6 (client 70707) with this project's patches), not in-game measurements.
- 2026-11-01 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Geometry -> Magic Absorption (mana); Improved Counterspell -> Magic Absorption (mana); Improved Channeling -> Arcane Resilience (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Arcane-Frost build: check it against the community's Arcane-Frost builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/mage/60/03220421310101053-55-0535-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
