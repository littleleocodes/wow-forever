# Arcane-Frost — Raid (open talent search) — 28/0/23

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 28/0/23 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane-Frost (an Arcane/Frost hybrid) raid build the open talent search found on 2026-10-09: every legal 51-point build with no tree rule, searched in the community simulator's frost-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.4% over frost-ml-raid, the best of our builds in that rotation.

## Point allocation

### Arcane (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Improved Channeling** | 5/5 | **NEW** | Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast. |
| **Arcane Concentration** | 3/5 | unchanged | Gives you a 6% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 57 to 65 Arcane damage. Each time you cast Arcane Blast, the damage of all your other spells is increased by 10% and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 8 sec or until any other damage spell is cast. |
| **Missile Barrage** | 1/1 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |

### Fire (0)

*No points.*

### Frost (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 4/5 | changed | Improves your chance to hit with Frost and Fire spells by 4%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Core talents (priority order)

1. **Improved Frostbolt** — 91 DPS lost without it (13% of the build in a full raid; removal, 12,000 fights).
2. **Fingers of Frost** — 72 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
3. **Missile Barrage** — 66 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
4. **Ice Shards** — 63 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
5. **Shatter** — 52 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
6. **Arcane Instability** — 35 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Piercing Ice** — 30 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
8. **Elemental Precision** — 29 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**4 of 13** for `frost-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 21/0/30 | 602 | +0.0% | 680 | -1.0% | 0 s |
| 2 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 598 | -0.5% | 676 | -1.6% | 0 s |
| 3 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 22/0/29 | 597 | -0.8% | 676 | -1.6% | 1 s |
| 4 | **[`arcane-frost-open-raid`](arcane-frost-open-raid.md)** | ours: derived (open search) | 28/0/23 | 589 | -2.1% | 687 | +0.0% | 5 s |
| 5 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 32/0/19 | 566 | -5.9% | 643 | -6.4% | 0 s |
| 6 | *Frost DPS* | community simulator | - | 557 | -7.5% | 632 | -8.0% | 0 s |
| 7 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 1/13/37 | 546 | -9.3% | 646 | -6.0% | 7 s |
| 8 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 541 | -10.0% | 612 | -10.9% | 0 s |
| 9 | *Frost 14/0/37* | community simulator | - | 540 | -10.2% | 641 | -6.7% | 8 s |
| 10 | *Arcane 35/0/16* | community simulator | - | 487 | -19.1% | 553 | -19.5% | 0 s |
| 11 | *Arcane DPS* | community simulator | - | 420 | -30.1% | 472 | -31.2% | 0 s |
| 12 | *Fire 0/35/16* | community simulator | - | 385 | -36.0% | 438 | -36.2% | 0 s |
| 13 | *Fire DPS* | community simulator | - | 323 | -46.3% | 362 | -47.3% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 4 passes, the last 2026-10-09, 7 changes to the base rotation; third-seed check: open winner 576 -> 605 DPS (+5.1%), frost-ml-raid 591 -> 604 DPS (+2.2%), sim preset: Frost DPS 551 -> 561 DPS (+1.7%), frost-arcane-power-raid 567 -> 572 DPS (+0.8%), frost-winters-chill-raid 544 -> 547 DPS (+0.6%), frost-fingers-of-frost-raid 588 -> 602 DPS (+2.4%), opt-frost-raid-raid-dps 580 -> 600 DPS (+3.4%), opt-frost-raid-raid-dps-extwc 545 -> 549 DPS (+0.8%)):
  1. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.3%, pass 1)
  2. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  3. repair: insert before the filler: if mana % < 5% and time left in the fight > 25s: cast Evocation (every frost-raid build raced, 20,000 fights, seed 3: opt-frost-raid-raid-dps-extwc +6.6%, the others -0.02% to +0.00%) (+6.6%, pass 2)
  4. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast (+0.6%, pass 3)
  5. threshold 80% -> 60%: if mana % ≤ 80%: cast Mana Ruby (mana gem) (+0.2%, pass 4)
  6. threshold 25s -> 50s: if mana % < 5% and time left in the fight > 25s: cast Evocation (+0.2%, pass 4)
  7. insert at the end: cast Arcane Blast (+0.2%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 4 passes, the last 2026-10-09, 2 changes to the base rotation; third-seed check: open winner 676 -> 693 DPS (+2.4%), frost-ml-raid 673 -> 683 DPS (+1.5%), sim preset: Frost DPS 631 -> 635 DPS (+0.7%), frost-arcane-power-raid 646 -> 650 DPS (+0.6%), frost-winters-chill-raid 616 -> 620 DPS (+0.6%), frost-fingers-of-frost-raid 669 -> 680 DPS (+1.7%), opt-frost-raid-raid-dps 669 -> 680 DPS (+1.7%), opt-frost-raid-raid-dps-extwc 645 -> 650 DPS (+0.7%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60%: cast Mana Ruby (mana gem) | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles | 3.2 |
| 4 | if Fingers of Frost is up: cast Ice Lance | 4.3 |
| 5 | if mana % < 5% and time left in the fight > 50s: cast Evocation | 0.1 |
| 6 | if time left in the fight ≥ 3s: cast Frostbolt | 17.2 |
| 7 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.2 |
| 8 | cast Arcane Blast | 0.2 |

Damage by ability:

| Ability | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) |
|---|---|
| Frostbolt | 59% |
| Arcane Missiles | 22% |
| Ice Lance | 18% |
| Arcane Blast | 1% |
| Fire Blast | 0% |

## Notes

- +1.9% over the best hand draft of the spec, frost-fingers-of-frost-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (frost-raid, full raid): 28/0/23 (Arcane-Frost (an Arcane/Frost hybrid)) at 692.9 DPS; frost-ml-raid 683.3, opt-frost-raid-raid-dps 679.9, frost-fingers-of-frost-raid 679.8, opt-frost-raid-raid-dps-extwc 650.1, frost-arcane-power-raid 649.5, frost-winters-chill-raid 619.1 in the same fights; 4,617 builds simulated, 2 independent runs reached the top.
- The frost-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): fire-raid -46.4%, arcane-dps -6.9%, frostfire-raid -36.5%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Improved Channeling, Arcane Subtlety, Arcane Geometry, Arcane Blast.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements.
- 2026-10-09 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Geometry -> Improved Channeling (interrupt); Arcane Subtlety -> Improved Channeling (interrupt); Arcane Subtlety -> Improved Channeling (interrupt); Arcane Meditation -> Improved Channeling (interrupt); Arcane Concentration -> Arcane Subtlety (threat); Arcane Concentration -> Arcane Subtlety (threat). Net +0.04% on a third seed.

## Open questions (verify in the live game)

- An open-search Arcane-Frost build: check it against the community's Arcane-Frost builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/mage/60/05120501310011053--05450003010003002-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
