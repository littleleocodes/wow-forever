# Frost — Raid (machine-learning search) — 21/0/30

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-29 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry frost-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Arcane (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, Frost Blast, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Mind** | 1/5 | changed | Increases your Intellect by 2% and increases the critical strike damage bonus of your Arcane spells by 20%. |

### Fire (0)

*No points.*

### Frost (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Rank among our builds and the community simulator's

**6 of 13** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 54ceac6 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 552 | +0.0% | 661 | -1.5% | 5 s |
| 2 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 546 | -1.0% | 650 | -3.0% | 9 s |
| 3 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 32/3/16 | 544 | -1.4% | 659 | -1.7% | 7 s |
| 4 | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) | ours: derived (open search) | 28/10/13 | 525 | -4.9% | 671 | +0.0% | 4 s |
| 5 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 506 | -8.4% | 572 | -14.7% | 0 s |
| 6 | **[`frost-ml-raid`](frost-ml-raid.md)** | ours: derived (ML search) | 21/0/30 | 502 | -9.1% | 597 | -11.0% | 5 s |
| 7 | *Arcane Fire* | community simulator | - | 482 | -12.7% | 619 | -7.7% | 6 s |
| 8 | *Arcane* | community simulator | - | 482 | -12.7% | 631 | -5.9% | 6 s |
| 9 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 457 | -17.2% | 519 | -22.6% | 0 s |
| 10 | *Frost Incin* | community simulator | - | 454 | -17.9% | 544 | -18.9% | 4 s |
| 11 | *Frost Med* | community simulator | - | 444 | -19.6% | 539 | -19.5% | 9 s |
| 12 | *Fire* | community simulator | - | 408 | -26.0% | 487 | -27.4% | 8 s |
| 13 | *FFB* | community simulator | - | 387 | -30.0% | 447 | -33.4% | 2 s |

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

| # | Priority (the first line whose condition holds is cast) | [`frost-ml-raid`](frost-ml-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60% and mana % ≥ 60%: cast Mana Ruby | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Fingers of Frost is up: cast Ice Lance | 1.3 |
| 4 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) | 4.5 |
| 5 | if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast | 8.2 |
| 6 | if mana % < 5% and time left in the fight > 50s: cast Evocation | 0.3 |
| 7 | if time left in the fight ≥ 3s: cast Frostbolt (rank 10) | 12.3 |
| 8 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.1 |
| 9 | cast Arcane Blast | 8.2 |
| 10 | cast Robe of the Archmage | as ready |

Lines of the simulator's rotation these builds never cast: cast Presence of Mind (needs the Presence of Mind talent); cast spell 1326055 (its condition never held in these fights).

Damage by ability:

| Ability | [`frost-ml-raid`](frost-ml-raid.md) |
|---|---|
| Frostbolt | 46% |
| Arcane Missiles | 30% |
| Arcane Blast | 15% |
| Ice Lance | 7% |
| Demonic Rune | 2% |
| Fire Blast | 0% |

## Notes

- Against the best hand draft frost-winters-chill-raid in a full raid, same gear and fights (100,000, one seed): +18.7% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow frost-winters-chill-raid: Improved Blizzard → Winter's Chill (the same DPS as the search winner 21/0/30 on one seed, 30,000 fights).
- Search result (full raid): 21/0/30 at 593.6 ± 0.10 DPS over 100,000 fights; runner-up 21/0/30 (+0.16%; the winner takes Frostbite 3; the runner-up Frost Warding 1, Frostbite 2); 2,127 builds simulated; certificate: 1 confirmed move first, then none of its 261 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 21/0/30 at 579.4 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 21/0/30 at 514.9 DPS.
- 2026-10-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Meditation -> Improved Channeling (interrupt); Arcane Concentration -> Improved Channeling (interrupt); Arcane Concentration -> Improved Channeling (interrupt); Winter's Chill -> Frost Channeling (threat); Winter's Chill -> Arctic Reach (range); Winter's Chill -> Arctic Reach (range); Winter's Chill -> Frost Warding (survival); Winter's Chill -> Frost Warding (survival). Net -0.02% on a third seed.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 21/0/30 -> 21/0/30; Arcane Focus 5 gone; Elemental Precision -> Precision (renamed); +1 Missile Barrage (tier gating for Arcane Mind); +1 Arcane Concentration (tier gating for Arcane Mind); +1 Arcane Concentration (tier gating for Arcane Mind); +1 Magic Absorption (tier gating for Arcane Mind); +1 Magic Absorption (tier gating for Arcane Mind) (refill: the frost-raid model, raid-dps).

## Open questions (verify in the live game)

- A machine-searched Frost build: check it against the community's Frost builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
