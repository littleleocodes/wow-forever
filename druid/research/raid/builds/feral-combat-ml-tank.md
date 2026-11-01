# Feral Combat — Raid tank (machine-learning search) — 9/35/7

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/35/7 (Balance / Feral Combat / Restoration) |
| **Role** | TANK — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Feral Combat tank build the machine-learning talent search found in the community simulator on 2026-10-29 (raidsim/deep_tank.py: a random forest guiding a genetic search over every legal build of the spec, scored on tank value: threat per second and damage taken under boss melee; the rotation tuned with it; races on fresh seeds; every build one or two moves from the winner checked). The simulator's model of the beta, not an in-game measurement.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Wrath** | 5/5 | changed | Reduces the cast time of your Wrath spell by 0.5 sec and its Mana cost by 50%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Blood Frenzy** | 1/2 | changed | Gives you a 50% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 50% chance to add an additional Combo Point. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Natural Reaction** | 5/5 | **NEW** | Increases your dodge chance by 5%, and gives you a 100% chance to gain 5 Rage each time you dodge. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |

### Restoration (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 2/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.2 sec and increases all damage you deal by 4%. |

## Rank among our builds and the community simulator's

**3 of 5** for `feral-bear-tank` by tank value in the community simulator (wowsims/forever b90e2b9 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |
|---|---|---|---|---|---|---|---|
| 1 | [`opt-feral-bear-tank-raid-tank`](opt-feral-bear-tank-raid-tank.md) | ours: optimizer | 9/37/5 | 1.157 | +0.0% | 3627 | 370 |
| 2 | *Hybrid* | community simulator | - | 1.143 | -1.3% | 3749 | 396 |
| 3 | **[`feral-combat-ml-tank`](feral-combat-ml-tank.md)** | ours: derived (ML search) | 9/35/7 | 1.006 | -13.1% | 2917 | 390 |
| 4 | [`feral-bear-tank`](feral-bear-tank.md) | ours: hand draft | 7/35/9 | 1.000 | -13.6% | 2881 | 390 |
| 5 | *Bear* | community simulator | - | 0.984 | -15.0% | 2829 | 395 |

## Rotation (community simulator, raid setting)

- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 13 passes, the last 2026-10-29, 8 changes to the base rotation; third-seed check: deep: tank 542 -> 2610 DPS (+381.3%), opt-feral-bear-tank-raid-tank 594 -> 2554 DPS (+330.3%), sim preset: Hybrid 579 -> 1930 DPS (+233.2%), feral-bear-tank 513 -> 2349 DPS (+357.6%), feral-combat-ml-tank 542 -> 2608 DPS (+381.5%)):
  1. threshold 25 -> 50: if rage ≥ 25: cast Maul (+0.9%, pass 1)
  2. move down below 'if (stacks of Lacerate < 5 or time left on Lacerate ≤ 4.5s): cast Lacerate': cast Primal Bite (+0.6%, pass 1)
  3. insert before the filler: cast Barkskin (+2.2%, pass 3)
  4. only with 20s or more of the fight left: cast Lacerate (+1.2%, pass 11)
  5. drop the condition: if rage ≥ 50: cast Maul (+6.6%, pass 12)
  6. drop: cast Primal Bite (+2.2%, pass 12)
  7. insert before the filler: if rage < 20: cast Enrage (+1.2%, pass 12)
  8. drop 'stacks of Lacerate < 5' from the condition: if (stacks of Lacerate < 5 or time left on Lacerate ≤ 4.5s): cast Lacerate (+0.3%, pass 12)

| # | Priority (the first line whose condition holds is cast) | [`feral-combat-ml-tank`](feral-combat-ml-tank.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | cast Maul | 143.1 |
| 3 | cast Barkskin | 1.0 |
| 4 | if rage < 20: cast Enrage | 1.0 |

Lines of the simulator's rotation these builds never cast: cast Faerie Fire, cast Demoralizing Roar (its condition never held in these fights); cast Lacerate (needs the Lacerate talent).

Damage by ability (threat for tanks):

| Ability | [`feral-combat-ml-tank`](feral-combat-ml-tank.md) |
|---|---|
| Maul | 78% |
| Auto Attack | 18% |
| Judgement of Light | 2% |
| OtherActionRageGain | 1% |
| Retribution Aura | 0% |
| Thorns | 0% |

## Notes

- +5.5% tank value over the hand draft feral-bear-tank (over the 2% bar: the spec's tank pick; the hand draft stays as the alternative).
- Final race over 100,000 fights: tank value 1.055 ± 0.000 (relative to feral-bear-tank over 20,000 fights); feral-combat-ml-tank 1.055, opt-feral-bear-tank-raid-tank 1.044, feral-bear-tank 1.000.
- Independent runs agreeing in the last cycle: 3/3; two-move check: 350 one-move and 47,117 two-move builds, none better.
- 2026-10-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Genesis -> Improved Wrath (range); Genesis -> Improved Wrath (range); Genesis -> Improved Wrath (range); Genesis -> Improved Wrath (range); Genesis -> Improved Wrath (range). Net -0.03% on a third seed.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 9/35/7 -> 9/35/7; +1 Heart of the Wild (tier gating for Naturalist); +1 Heart of the Wild (tier gating for Naturalist); +1 Heart of the Wild (tier gating for Naturalist); +1 Heart of the Wild (tier gating for Naturalist); +1 Heart of the Wild (tier gating for Naturalist); -1 Feral Swiftness (over 51); -1 Feral Swiftness (over 51); -1 Savage Fury (over 51); -1 Savage Fury (over 51); -1 Blood Frenzy (over 51) (refill: the feral-bear-tank model, raid-dps).

## Open questions (verify in the live game)

- A machine-searched Feral Combat tank build: check its threat and survival against the community's tank builds at launch (the simulator models no threat from other players, taunts or tank swaps).

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
