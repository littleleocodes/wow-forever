# Frost — Raid (machine-learning search) — 15/5/31

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 15/5/31 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-11-19 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry frost-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Arcane (15)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 2/5 | **NEW** | Gives your Arcane Missiles spell a 40% chance and your Arcane Blast and Arcane Wrath spells a 28% chance to not lose casting time when you take damage. |
| **Arcane Resilience** | 3/3 | changed | Increases your Armor by an amount equal to 75% of your Intellect. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 2/5 | unchanged | Gives you a 4% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Magic Absorption** | 1/2 | changed | Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec. |

### Fire (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |

### Frost (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 1/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 15%, gives your Frost Ward a 10% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 10%. |
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Winter's Chill** | 3/5 | changed | Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 60% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times. |
| **Ice Barrier** | 1/1 | changed | Shield yourself, absorbing 447 damage and increasing your Frost damage by 15% for 1 min. While shielded, your Frost damage is increased by an additional 5% and you do not lose casting time when you take damage. |

## Rank among our builds and the community simulator's

**2 of 15** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 579 | +0.0% | 673 | -3.1% | 5 s |
| 2 | **[`frost-ml-raid`](frost-ml-raid.md)** | ours: derived (ML search) | 15/5/31 | 578 | -0.1% | 652 | -6.1% | 2 s |
| 3 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 32/3/16 | 573 | -1.1% | 684 | -1.5% | 2 s |
| 4 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 572 | -1.3% | 679 | -2.2% | 7 s |
| 5 | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) | ours: derived (open search) | 28/10/13 | 538 | -7.0% | 695 | +0.0% | 5 s |
| 6 | *Frost Incin* | community simulator | - | 534 | -7.8% | 647 | -6.8% | 6 s |
| 7 | *Frost Med* | community simulator | - | 534 | -7.8% | 642 | -7.6% | 10 s |
| 8 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 513 | -11.5% | 579 | -16.6% | 0 s |
| 9 | *Arcane Fire* | community simulator | - | 504 | -13.0% | 642 | -7.5% | 1 s |
| 10 | *Arcane* | community simulator | - | 504 | -13.0% | 657 | -5.5% | 1 s |
| 11 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 459 | -20.7% | 523 | -24.7% | 0 s |
| 12 | *Fire Skyborne GT 180* | community simulator | - | 434 | -25.1% | 500 | -28.1% | 4 s |
| 13 | *Fire Skyborne LT 180* | community simulator | - | 430 | -25.7% | 502 | -27.7% | 6 s |
| 14 | *Fire* | community simulator | - | 428 | -26.0% | 500 | -28.1% | 6 s |
| 15 | *FFB* | community simulator | - | 397 | -31.4% | 450 | -35.1% | 0 s |

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

Before the pull: at -2s: cast Ice Barrier.

| # | Priority (the first line whose condition holds is cast) | [`frost-ml-raid`](frost-ml-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Frigid Power < 2s: cast Ice Barrier | 1.3 |
| 2 | if mana % ≤ 60% and mana % ≥ 60%: cast Mana Ruby | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if Fingers of Frost is up: cast Ice Lance | 2.0 |
| 5 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) | 3.2 |
| 6 | if time left in the fight ≥ 3s: cast Frostbolt (rank 10) | 18.7 |
| 7 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.1 |
| 8 | cast Robe of the Archmage | as ready |

Lines of the simulator's rotation these builds never cast: cast Arcane Blast (needs the Arcane Blast talent); cast Presence of Mind (needs the Presence of Mind talent); cast Evocation, cast spell 1326055 (its condition never held in these fights).

Damage by ability:

| Ability | [`frost-ml-raid`](frost-ml-raid.md) |
|---|---|
| Frostbolt | 70% |
| Arcane Missiles | 18% |
| Ice Lance | 11% |
| Fire Blast | 0% |
| Demonic Rune | 0% |

## Notes

- Against the best hand draft frost-winters-chill-raid in a full raid, same gear and fights (100,000, one seed): +24.5% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow frost-winters-chill-raid: Flame Throwing → Arcane Concentration, Wand Specialization → Improved Channeling (2 points), Arcane Resilience → Improved Channeling (2 points), Permafrost → Arctic Reach, Improved Cone of Cold → Arctic Reach, Improved Cone of Cold → Ice Block, Improved Cone of Cold → Winter's Chill (within 0.00% of the search winner 14/6/31 on one seed, 30,000 fights).
- Search result (full raid): 14/6/31 at 671.0 ± 0.12 DPS over 100,000 fights; runner-up 13/6/32 (+0.01%; the winner takes Arcane Concentration 2, Frost Warding 2, Permafrost 1; the runner-up Arctic Reach 2, Frost Warding 1, Improved Blizzard 1, Improved Channeling 1); 1,910 builds simulated; certificate: the neighbours ahead on the short run (of 293) did not hold on the longer one.
- Simulator numbers are the community's model of the beta (wowsims/forever 2e6e77d (client 70938) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 13/6/32 at 646.4 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 19/1/31 at 595.3 DPS.
- 2026-11-19 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Concentration -> Frost Channeling (threat); Arctic Reach -> Magic Absorption (mana); Frost Warding -> Arctic Reach (range); Improved Channeling -> Arcane Resilience (survival); Improved Channeling -> Arcane Resilience (survival). Net +0.04% on a third seed.

## Open questions (verify in the live game)

- A machine-searched Frost build: check it against the community's Frost builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
