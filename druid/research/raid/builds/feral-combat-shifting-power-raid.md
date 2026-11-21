# Feral Combat — Shifting Power (the simulator's Feral Cat 9/35/7) — 9/33/9

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/33/9 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The community simulator's own Feral Cat preset (9/35/7), raced against our Feral builds in a full raid: 691 DPS against 594 for our best (+16.4%). It takes Shifting Power, Improved Shifting Power, Feral Charge and 5 Ferocity, which the raid rotation's powershifting (Furor) pays for, where our builds, optimized on the training dummy (368 against its 357 there), took Thick Hide, Reflection and 5 Naturalist.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Predatory Discipline** | 1/1 | **NEW** | Your Ferocious Bite ability no longer converts extra Energy into damage, but still deals extra damage based on your excess Energy. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 15%. |
| **Shifting Power** | 1/1 | **NEW** | Instantly convert 55% of base Mana into 40 Energy. Shifting Power's cost is reduced by effects that reduce the cost of Shapeshifting. |

### Restoration (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 4/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.4 sec and increases all damage you deal by 8%. |

## Rank among our builds and the community simulator's

**2 of 6** for `feral-cat-dps` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Cat* | community simulator | - | 549 | +0.0% | 924 | -1.2% | 37 s |
| 2 | **[`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md)** | ours: derived (simulator preset) | 9/33/9 | 545 | -0.7% | 918 | -1.8% | 37 s |
| 3 | [`feral-combat-open-raid`](feral-combat-open-raid.md) | ours: derived (open search) | 9/32/10 | 537 | -2.1% | 935 | +0.0% | 38 s |
| 4 | *Hybrid* | community simulator | - | 501 | -8.6% | 864 | -7.6% | 42 s |
| 5 | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) | ours: optimizer | 9/30/12 | 475 | -13.4% | 772 | -17.4% | 0 s |
| 6 | [`feral-cat-dps`](feral-cat-dps.md) | ours: hand draft | 9/32/10 | 466 | -15.0% | 758 | -18.9% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-10, 10 changes to the base rotation; third-seed check: open winner 368 -> 390 DPS (+5.9%), opt-feral-cat-dps-raid-dps 346 -> 368 DPS (+6.4%), sim preset: Feral Cat 9/35/7 368 -> 394 DPS (+7.2%), feral-cat-dps 337 -> 357 DPS (+5.9%)):
  1. drop: if combo points = 5.0 and not Clearcasting is up and (energy + 20.2) < (current cost + current cost): cast Ferocious Bite (+2.2%, pass 1)
  2. threshold 5 -> 3.75: if combo points ≥ 5 and not Rip is on the target: cast Rip (+1.6%, pass 1)
  3. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and (combo points < 5.0 and (energy + 20.2) < current cost or combo points = 5.0 and (energy + 20.2) < current cost or Clearcasting is known and Clearcasting is up and energy < 27.8): cancel Cat Form (+1.1%, pass 1)
  4. threshold 27.8 -> 13.9: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 27.8: cancel Cat Form (+0.4%, pass 1)
  5. drop the condition: if not Cat Form is up: cast Goblin Sapper Charge (+0.2%, pass 1)
  6. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 13.9: cancel Cat Form (+0.2%, pass 1)
  7. threshold 14.0s -> 28s: if Faerie Fire should be refreshed: cast Faerie Fire (+0.2%, pass 1)
  8. drop the condition: if Faerie Fire should be refreshed: cast Faerie Fire (+0.6%, pass 4)
  9. only with 6s or more of the fight left: cast Faerie Fire (+0.8%, pass 4)
  10. insert in the middle: if Shifting Power is known and energy ≤ 60: cast Shifting Power (+11.8%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 12 passes, the last 2026-11-02, 10 changes to the base rotation; third-seed check: feral-combat-open-raid 758 -> 758 DPS (+0.0%), sim preset: Cat 750 -> 750 DPS (+0.0%), feral-cat-dps 620 -> 620 DPS (+0.0%), opt-feral-cat-dps-raid-dps 630 -> 630 DPS (+0.0%), feral-combat-shifting-power-raid 745 -> 745 DPS (+0.0%)):
  1. drop: if combo points = 5.0 and not Clearcasting is up and (energy + 20.2) < (current cost + current cost): cast Ferocious Bite (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if combo points ≥ 5 and not Rip is on the target: cast Rip (+1.3%, pass 1)
  3. drop: if not Cat Form is up and mana % ≤ 40% and time left in the fight ≥ 20.0 and not (Demonic Rune is known and Demonic Rune is ready or Potion is known and Potion is ready): cast Innervate (+0.5%, pass 1)
  4. threshold 27.8 -> 13.9: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 27.8: cancel Cat Form (+0.2%, pass 1)
  5. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and (combo points < 5.0 and (energy + 20.2) < current cost or combo points = 5.0 and (energy + 20.2) < current cost or Clearcasting is known and Clearcasting is up and energy < 27.8): cancel Cat Form (+0.2%, pass 4)
  6. insert in the middle: if Shifting Power is known and energy ≤ 60: cast Shifting Power (+9.9%, pass 5)
  7. insert at the top: if combo points < 5 and not Rake is on the target and time left in the fight > 6s: cast Rake (+7.5%, pass 7)
  8. drop 'combo points < 5' from the condition: if combo points < 5 and not Rake is on the target and time left in the fight > 6s: cast Rake (+0.5%, pass 7)
  9. insert at the top: if (combo points ≥ 5 and not time left in the fight ≥ 10s or combo points ≥ 3 and time left in the fight < 3s): cast Ferocious Bite (rank 4) (+0.2%, pass 8)
  10. rotation replaced by the official simulator's adaptive.apl.json at 54ceac638 (rotation-lag audit after the re-pin) (+1.0%, pass 10)

Before the pull: at -33s: if Manual Crowd Pummeler is known: swap to the Swap1 item set; at -1s: cast Prowl; at -0.01s: if not activeItemSwapSet: swap to the Main item set; at -0.01s: cast Dash.

| # | Priority (the first line whose condition holds is cast) | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) casts/min |
|---|---|---|
| 1 | if “Ready to return to the main weapon”: swap to the Main item set | as ready |
| 2 | if “Drop Prowl for this opener”: cancel Prowl | as ready |
| 3 | if Faerie Fire is known and Faerie Fire should be refreshed: cast Faerie Fire | 1.9 |
| 4 | if unitDistance > 5: move to 5 yd | as ready |
| 5 | if unitDistance > 5: wait until not unitDistance > 5 | as ready |
| 6 | if “Ready to activate MCP”: cast Manual Crowd Pummeler | as ready |
| 7 | if not Cat Form is up: cast Cat Form | 0.3 |
| 8 | if “Final-global Bite”: cast Ferocious Bite (rank 5) | 0.7 |
| 9 | use every other cooldown when ready | as ready |
| 10 | if “Mana potion fits and is needed”: cast ResourcePotion on self | as ready |
| 11 | if number of targets = 2 and “Use Shred cleave tuning” and time until the global cooldown is ready ≤ 0s and “2 targets: Shred: next target is worth switching to”: change target | as ready |
| 12 | if number of targets = 2 and “Use Shred cleave tuning” and “2 targets: Shred: Midfight Bite is worthwhile” and not “2 targets: Shred: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.7 |
| 13 | if number of targets = 2 and “Use Shred cleave tuning” and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 14 | if number of targets = 2 and “Use Shred cleave tuning” and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 15 | if number of targets = 2 and “Use Shred cleave tuning” and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 16 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up: cast OffensivePotion | as ready |
| 17 | if number of targets = 2 and “Use Shred cleave tuning” and “Cleave 2: Fight-end Bite is worthwhile” and not “2 targets: Shred: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.7 |
| 18 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and Clearcasting is up and not “2 targets: Shred: Pool energy for Bite” and not “2 targets: Shred: leave this global for the target switch”: cast Shred | 14.5 |
| 19 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 2: 2 targets: Shred: Rip due” and not “2 targets: Shred: leave this global for the target switch”: cast Rip | 4.7 |
| 20 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 2: Rake due”: cast Rake | 6.2 |
| 21 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 2: 2 targets: Shred: Paid builder fits the energy pool” and not “2 targets: Shred: leave this global for the target switch”: cast Shred | 14.5 |
| 22 | if number of targets = 2 and “Use Shred cleave tuning” and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 23 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 24 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 25 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 26 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up: cast OffensivePotion | as ready |
| 27 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and “Cleave 2: Fight-end Bite is worthwhile” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.7 |
| 28 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and time until the global cooldown is ready ≤ 0s and “2 targets: Hybrid with Blood Frenzy: next target is worth switching to”: change target | as ready |
| 29 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up and Clearcasting is up and not “2 targets: Hybrid: Pool energy for Bite” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 14.5 |
| 30 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up and “Blood Frenzy: Cleave 2: Rip due” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Rip | 4.7 |
| 31 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up and “Blood Frenzy: Cleave 2: Rake due”: cast Rake | 6.2 |
| 32 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 2: 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 14.5 |
| 33 | if number of targets = 2 and not “Use Shred cleave tuning” and talentIsKnown and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 34 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 35 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 36 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 37 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up: cast OffensivePotion | as ready |
| 38 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and “Cleave 2: Fight-end Bite is worthwhile” and not “2 targets: Hybrid: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.7 |
| 39 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and time until the global cooldown is ready ≤ 0s and “2 targets: Hybrid: next target is worth switching to”: change target | as ready |
| 40 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up and Clearcasting is up and not “2 targets: Hybrid: Pool energy for Bite” and not “2 targets: Hybrid: leave this global for the target switch”: cast Shred | 14.5 |
| 41 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up and “Cleave 2: Rip due” and not “2 targets: Hybrid: leave this global for the target switch”: cast Rip | 4.7 |
| 42 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up and “Cleave 2: Rake due”: cast Rake | 6.2 |
| 43 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 2: 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid: leave this global for the target switch”: cast Shred | 14.5 |
| 44 | if number of targets = 2 and not “Use Shred cleave tuning” and not talentIsKnown and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 45 | if number of targets = 3 and “Use Shred cleave tuning” and time until the global cooldown is ready ≤ 0s and “3 targets: Shred: next target is worth switching to”: change target | as ready |
| 46 | if number of targets = 3 and “Use Shred cleave tuning” and time until the global cooldown is ready ≤ 0s and “3 targets: Shred: previous target is worth switching to”: change target | as ready |
| 47 | if number of targets = 3 and “Use Shred cleave tuning” and “3 targets: Shred: Midfight Bite is worthwhile” and not “3 targets: Shred: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.7 |
| 48 | if number of targets = 3 and “Use Shred cleave tuning” and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 49 | if number of targets = 3 and “Use Shred cleave tuning” and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 50 | if number of targets = 3 and “Use Shred cleave tuning” and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 51 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up: cast OffensivePotion | as ready |
| 52 | if number of targets = 3 and “Use Shred cleave tuning” and “Cleave 3: Fight-end Bite is worthwhile” and not “3 targets: Shred: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.7 |
| 53 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and Clearcasting is up and not “3 targets: Shred: Pool energy for Bite” and not “3 targets: Shred: leave this global for the target switch”: cast Shred | 14.5 |
| 54 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 3: 3 targets: Shred: Rip due” and not “3 targets: Shred: leave this global for the target switch”: cast Rip | 4.7 |
| 55 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 3: Rake due”: cast Rake | 6.2 |
| 56 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 3: 3 targets: Shred: Paid builder fits the energy pool” and not “3 targets: Shred: leave this global for the target switch”: cast Shred | 14.5 |
| 57 | if number of targets = 3 and “Use Shred cleave tuning” and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 58 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 59 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 60 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 61 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up: cast OffensivePotion | as ready |
| 62 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and “Blood Frenzy: Cleave 3: Fight-end Bite is worthwhile” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.7 |
| 63 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid with Blood Frenzy: next target is worth switching to”: change target | as ready |
| 64 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid with Blood Frenzy: previous target is worth switching to”: change target | as ready |
| 65 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up and Clearcasting is up and not “Blood Frenzy: 3 targets: Hybrid: Pool energy for Bite” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 14.5 |
| 66 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up and “Cleave 3: Rip due” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Rip | 4.7 |
| 67 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up and “Blood Frenzy: Cleave 3: Rake due”: cast Rake | 6.2 |
| 68 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Blood Frenzy: Cleave 3: 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 14.5 |
| 69 | if number of targets = 3 and not “Use Shred cleave tuning” and talentIsKnown and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 70 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and combo points ≥ 4 and time left on Rip ≥ 2s and (Clearcasting is up and energy ≥ 30 or energy ≥ 50) and not “3 targets: Hybrid: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.7 |
| 71 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 72 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 73 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 74 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up: cast OffensivePotion | as ready |
| 75 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and “Cleave 3: Fight-end Bite is worthwhile” and not “3 targets: Hybrid: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.7 |
| 76 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid: next target is worth switching to”: change target | as ready |
| 77 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid: previous target is worth switching to”: change target | as ready |
| 78 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up and Clearcasting is up and not “3 targets: Hybrid: Pool energy for Bite” and not “3 targets: Hybrid: leave this global for the target switch”: cast Shred | 14.5 |
| 79 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up and “Cleave 3: Rip due” and not “3 targets: Hybrid: leave this global for the target switch”: cast Rip | 4.7 |
| 80 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up and “Cleave 3: Rake due”: cast Rake | 6.2 |
| 81 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 3: 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid: leave this global for the target switch”: cast Shred | 14.5 |
| 82 | if number of targets = 3 and not “Use Shred cleave tuning” and not talentIsKnown and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 83 | if not (number of targets = 2 or number of targets = 3) and “Midfight Bite is worthwhile”: cast Ferocious Bite (rank 5) | 0.7 |
| 84 | if not (number of targets = 2 or number of targets = 3) and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 85 | if not (number of targets = 2 or number of targets = 3) and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 86 | if not (number of targets = 2 or number of targets = 3) and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 87 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up: cast OffensivePotion | as ready |
| 88 | if not (number of targets = 2 or number of targets = 3) and “Fight-end Bite is worthwhile”: cast Ferocious Bite (rank 5) | 0.7 |
| 89 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and Clearcasting is up and not “Pool energy for Bite”: cast Shred | 14.5 |
| 90 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and “Rip due”: cast Rip | 4.7 |
| 91 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and “Rake due”: cast Rake | 6.2 |
| 92 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Paid builder fits the energy pool”: cast Shred | 14.5 |
| 93 | if not (number of targets = 2 or number of targets = 3) and “Innervate can restore needed mana”: cast Innervate | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Ravage, cast Elune's Light, 2 targets: Shred: Paid builder fits the energy pool” and not “2 targets: Shred: leave this global for the target switch”: cast Claw, Shred: Pool energy for Bite” and not “2 targets: Shred: leave this global for the target switch”: cast Claw, 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, Hybrid: Pool energy for Bite” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid: leave this global for the target switch”: cast Claw, Hybrid: Pool energy for Bite” and not “2 targets: Hybrid: leave this global for the target switch”: cast Claw, 3 targets: Shred: Paid builder fits the energy pool” and not “3 targets: Shred: leave this global for the target switch”: cast Claw, Shred: Pool energy for Bite” and not “3 targets: Shred: leave this global for the target switch”: cast Claw, Cleave 3: 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, 3 targets: Hybrid: Pool energy for Bite” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid: leave this global for the target switch”: cast Claw, Hybrid: Pool energy for Bite” and not “3 targets: Hybrid: leave this global for the target switch”: cast Claw, cast Claw (its condition never held in these fights).

Damage by ability:

| Ability | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) |
|---|---|
| Rip | 35% |
| Shred | 22% |
| Auto Attack | 20% |
| Rake | 19% |
| Ferocious Bite | 2% |
| Goblin Sapper Charge | 1% |
| spell 18211 | 0% |

## Notes

- Raced 2026-10-09 in the feral-cat-dps entry (ElliotWood/Forever 2ce8265 with this project's patches, full raid, 180 s): sim preset Feral Cat 9/35/7 691.1, sim preset Feral 664.9, opt-feral-cat-dps-raid-dps 593.6, feral-cat-dps 579.1 DPS.
- Written by hand from the race until the druid's open talent search (the 70291 sweep) rebuilds the Feral raid pick; the hand draft feral-cat-dps stays as the alternative.
- Simulator numbers are the community's model of the beta, not in-game measurements.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 9/35/7 -> 9/33/9; Improved Shifting Power 2 gone; Berserk 1 gone; +1 Predatory Discipline (prerequisite of Shifting Power); refill +2 Naturalist (refill: the feral-cat-dps model, raid-dps).

## Open questions (verify in the live game)

- Does powershifting work in Forever as the simulator plays it (Furor's energy on every Cat Form)? Check at launch.

## Sources

- <https://github.com/ElliotWood/Forever (ui/specs/druid/feral presets: Feral Cat 9/35/7)>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
