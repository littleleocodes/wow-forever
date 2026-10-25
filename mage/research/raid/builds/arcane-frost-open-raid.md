# Arcane-Frost — Raid (open talent search) — 29/0/22

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/0/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane-Frost (an Arcane/Frost hybrid) raid build the open talent search found on 2026-10-24: every legal 51-point build with no tree rule, searched in the community simulator's frost-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +0.6% over arcane-frost-open-raid, the best of our builds in that rotation.

## Point allocation

### Arcane (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Improved Channeling** | 5/5 | **NEW** | Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast or Arcane Wrath. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, your Arcane Missile hits a 10% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 15% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 15 sec from time of initial application. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Fire (0)

*No points.*

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 1/3 | moved | Gives your Chill effects a 5% chance to Freeze the target for 5 sec. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |

## Core talents (priority order)

1. **Fingers of Frost** — 310 DPS lost without it (45% of the build in a full raid; removal, 12,000 fights).
2. **Missile Barrage** — 121 DPS lost without it (18% of the build in a full raid; removal, 12,000 fights).
3. **Improved Frostbolt** — 69 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
4. **Arcane Blast** — 64 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
5. **Arcane Mind** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Arcane Instability** — 36 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Ice Shards** — 35 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Elemental Precision** — 23 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**3 of 11** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 587 | +0.0% | 680 | -1.8% | 9 s |
| 2 | *Arcane Frost* | community simulator | - | 582 | -0.9% | 693 | +0.0% | 8 s |
| 3 | **[`arcane-frost-open-raid`](arcane-frost-open-raid.md)** | ours: derived (open search) | 29/0/22 | 577 | -1.7% | 693 | -0.0% | 7 s |
| 4 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 35/0/16 | 577 | -1.7% | 676 | -2.4% | 5 s |
| 5 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 549 | -6.4% | 628 | -9.3% | 4 s |
| 6 | *Arcane Fire* | community simulator | - | 521 | -11.2% | 645 | -6.8% | 2 s |
| 7 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 484 | -17.5% | 547 | -21.0% | 0 s |
| 8 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 21/0/30 | 482 | -17.9% | 544 | -21.4% | 0 s |
| 9 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 441 | -24.8% | 501 | -27.7% | 0 s |
| 10 | *Fire* | community simulator | - | 439 | -25.2% | 504 | -27.2% | 8 s |
| 11 | *FFB* | community simulator | - | 387 | -34.1% | 443 | -36.1% | 2 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 7 passes, the last 2026-10-23, 6 changes to the base rotation; third-seed check: open winner 626 -> 691 DPS (+10.4%), opt-frost-raid-raid-dps-extwc 623 -> 680 DPS (+9.3%), sim preset: Arcane Frost 586 -> 693 DPS (+18.1%), frost-arcane-power-raid 585 -> 676 DPS (+15.6%), frost-winters-chill-raid 497 -> 501 DPS (+0.8%), frost-fingers-of-frost-raid 544 -> 547 DPS (+0.5%), opt-frost-raid-raid-dps 606 -> 663 DPS (+9.3%), frost-ml-raid 542 -> 545 DPS (+0.5%), arcane-frost-open-raid 622 -> 687 DPS (+10.5%)):
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
| 3 | if Fingers of Frost is up: cast Ice Lance | 2.1 |
| 4 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) | 5.3 |
| 5 | if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast | 7.3 |
| 6 | if Arcane Wrath is ready: cast Presence of Mind | 0.3 |
| 7 | if mana % < 5% and time left in the fight > 50s: cast Evocation | 0.3 |
| 8 | if time left in the fight ≥ 3s: cast Frostbolt (rank 10) | 11.9 |
| 9 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.2 |
| 10 | cast Arcane Blast | 7.3 |
| 11 | cast Robe of the Archmage | as ready |
| 12 | cast Frost Blast | 0.1 |

Damage by ability:

| Ability | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) |
|---|---|
| Frostbolt | 42% |
| Arcane Missiles | 35% |
| Arcane Blast | 13% |
| Ice Lance | 8% |
| Demonic Rune | 2% |
| Fire Blast | 0% |
| Frost Blast | 0% |

## Notes

- +2.3% over the best hand draft of the spec, frost-arcane-power-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (frost-raid, full raid): 29/0/22 (Arcane-Frost (an Arcane/Frost hybrid)) at 692.1 DPS; arcane-frost-open-raid 687.8, opt-frost-raid-raid-dps-extwc 680.3, frost-arcane-power-raid 676.5, opt-frost-raid-raid-dps 662.6, frost-fingers-of-frost-raid 546.6, frost-ml-raid 544.9, frost-winters-chill-raid 500.9 in the same fights; 4,517 builds simulated, 2 independent runs reached the top.
- The frost-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): fire-raid -41.2%, arcane-dps -13.5%, frostfire-raid -40.2%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Improved Channeling, Magic Absorption, Arcane Resilience, Arcane Shielding, Improved Counterspell, Improved Frost Nova.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements.
- 2026-10-24 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Concentration -> Improved Channeling (interrupt); Arcane Resilience -> Improved Channeling (interrupt); Arcane Shielding -> Improved Channeling (interrupt); Improved Counterspell -> Improved Channeling (interrupt); Improved Counterspell -> Magic Absorption (mana); Frostbite -> Arctic Reach (range); Improved Frost Nova -> Arctic Reach (range). Net +0.07% on a third seed.

## Open questions (verify in the live game)

- An open-search Arcane-Frost build: check it against the community's Arcane-Frost builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/mage/60/051221110311200153--0535210001003002-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
