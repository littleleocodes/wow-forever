# Optimizer — White 40%, Shred 30% (60 energy), Ferocious Bite 15%, Rip 10%, Claw/Rake 5% (raid-dps) — 9/30/12

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/30/12 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `feral-cat-dps` and profile `raid-dps`: score +90.8% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 2/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 2 Rage or Energy. |
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 15%. |

### Restoration (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |
| **Reflection** | 2/3 | changed | Allows 33% of your Mana regeneration to continue while casting. |

## Core talents (priority order)

1. **Shredding Attacks** — Removing it costs 28.9 points of score in this model.
2. **Blood Frenzy** — Removing it costs 14.3 points of score in this model.
3. **Sharpened Claws** — Removing it costs 9.9 points of score in this model.
4. **Rend and Tear** — Removing it costs 9.5 points of score in this model.
5. **Naturalist** — Removing it costs 9.1 points of score in this model.
6. **Predatory Strikes** — Removing it costs 6.1 points of score in this model.
7. **Natural Instinct** — Removing it costs 6.0 points of score in this model.
8. **Nature's Reach** — Removing it costs 5.6 points of score in this model.

## Rank among our builds and the community simulator's

**5 of 6** for `feral-cat-dps` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Cat* | community simulator | - | 549 | +0.0% | 924 | -1.2% | 37 s |
| 2 | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) | ours: derived (simulator preset) | 9/33/9 | 545 | -0.7% | 918 | -1.8% | 37 s |
| 3 | [`feral-combat-open-raid`](feral-combat-open-raid.md) | ours: derived (open search) | 9/32/10 | 537 | -2.1% | 935 | +0.0% | 38 s |
| 4 | *Hybrid* | community simulator | - | 501 | -8.6% | 864 | -7.6% | 42 s |
| 5 | **[`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md)** | ours: optimizer | 9/30/12 | 475 | -13.4% | 772 | -17.4% | 0 s |
| 6 | [`feral-cat-dps`](feral-cat-dps.md) | ours: hand draft | 9/32/10 | 466 | -15.0% | 758 | -18.9% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/druid/upstream/adaptive.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-10-10 (10 changes, `feral-cat-dps-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/druid/upstream/adaptive.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-11-02 (10 changes, `feral-cat-dps-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: at -33s: if Manual Crowd Pummeler is known: swap to the Swap1 item set; at -1s: cast Prowl; at -0.01s: if not activeItemSwapSet: swap to the Main item set; at -0.01s: cast Dash.

| # | Priority (the first line whose condition holds is cast) | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if “Ready to return to the main weapon”: swap to the Main item set | as ready |
| 2 | if “Drop Prowl for this opener”: cancel Prowl | as ready |
| 3 | if Faerie Fire is known and Faerie Fire should be refreshed: cast Faerie Fire | 1.9 |
| 4 | if unitDistance > 5: move to 5 yd | as ready |
| 5 | if unitDistance > 5: wait until not (unitDistance > 5) | as ready |
| 6 | if “Ready to activate MCP”: cast Manual Crowd Pummeler | as ready |
| 7 | if “Final-global Bite”: cast Ferocious Bite | 0.3 |
| 8 | use every other cooldown when ready | as ready |
| 9 | if “Mana potion fits and is needed”: cast ResourcePotion on self | as ready |
| 10 | if number of targets = 2 and “Use Shred cleave tuning” and time until the global cooldown is ready ≤ 0s and “2 targets: Shred: next target is worth switching to”: change target | as ready |
| 11 | if number of targets = 2 and “Use Shred cleave tuning” and “2 targets: Shred: Midfight Bite is worthwhile” and not “2 targets: Shred: leave this global for the target switch”: cast Ferocious Bite | 0.3 |
| 12 | if number of targets = 2 and “Use Shred cleave tuning” and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 13 | if number of targets = 2 and “Use Shred cleave tuning” and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 14 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up: cast OffensivePotion | as ready |
| 15 | if number of targets = 2 and “Use Shred cleave tuning” and “Cleave 2: Fight-end Bite is worthwhile” and not “2 targets: Shred: leave this global for the target switch”: cast Ferocious Bite | 0.3 |
| 16 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and Clearcasting is up and not “2 targets: Shred: Pool energy for Bite” and not “2 targets: Shred: leave this global for the target switch”: cast Shred | 9.0 |
| 17 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 2: 2 targets: Shred: Rip due” and not “2 targets: Shred: leave this global for the target switch”: cast Rip | 4.4 |
| 18 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 2: Rake due”: cast Rake | 6.1 |
| 19 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 2: 2 targets: Shred: Paid builder fits the energy pool” and not “2 targets: Shred: leave this global for the target switch”: cast Shred | 9.0 |
| 20 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 21 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 22 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up: cast OffensivePotion | as ready |
| 23 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Cleave 2: Fight-end Bite is worthwhile” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Ferocious Bite | 0.3 |
| 24 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “2 targets: Hybrid with Blood Frenzy: next target is worth switching to”: change target | as ready |
| 25 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and Clearcasting is up and not “2 targets: Hybrid: Pool energy for Bite” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 9.0 |
| 26 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and “Blood Frenzy: Cleave 2: Rip due” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Rip | 4.4 |
| 27 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and “Blood Frenzy: Cleave 2: Rake due”: cast Rake | 6.1 |
| 28 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 2: 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 9.0 |
| 29 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 30 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 31 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up: cast OffensivePotion | as ready |
| 32 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Cleave 2: Fight-end Bite is worthwhile” and not “2 targets: Hybrid: leave this global for the target switch”: cast Ferocious Bite | 0.3 |
| 33 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “2 targets: Hybrid: next target is worth switching to”: change target | as ready |
| 34 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and Clearcasting is up and not “2 targets: Hybrid: Pool energy for Bite” and not “2 targets: Hybrid: leave this global for the target switch”: cast Shred | 9.0 |
| 35 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and “Cleave 2: Rip due” and not “2 targets: Hybrid: leave this global for the target switch”: cast Rip | 4.4 |
| 36 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and “Cleave 2: Rake due”: cast Rake | 6.1 |
| 37 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 2: 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid: leave this global for the target switch”: cast Shred | 9.0 |
| 38 | if number of targets = 3 and “Use Shred cleave tuning” and time until the global cooldown is ready ≤ 0s and “3 targets: Shred: next target is worth switching to”: change target | as ready |
| 39 | if number of targets = 3 and “Use Shred cleave tuning” and time until the global cooldown is ready ≤ 0s and “3 targets: Shred: previous target is worth switching to”: change target | as ready |
| 40 | if number of targets = 3 and “Use Shred cleave tuning” and “3 targets: Shred: Midfight Bite is worthwhile” and not “3 targets: Shred: leave this global for the target switch”: cast Ferocious Bite | 0.3 |
| 41 | if number of targets = 3 and “Use Shred cleave tuning” and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 42 | if number of targets = 3 and “Use Shred cleave tuning” and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 43 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up: cast OffensivePotion | as ready |
| 44 | if number of targets = 3 and “Use Shred cleave tuning” and “Cleave 3: Fight-end Bite is worthwhile” and not “3 targets: Shred: leave this global for the target switch”: cast Ferocious Bite | 0.3 |
| 45 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and Clearcasting is up and not “3 targets: Shred: Pool energy for Bite” and not “3 targets: Shred: leave this global for the target switch”: cast Shred | 9.0 |
| 46 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 3: 3 targets: Shred: Rip due” and not “3 targets: Shred: leave this global for the target switch”: cast Rip | 4.4 |
| 47 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 3: Rake due”: cast Rake | 6.1 |
| 48 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 3: 3 targets: Shred: Paid builder fits the energy pool” and not “3 targets: Shred: leave this global for the target switch”: cast Shred | 9.0 |
| 49 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 50 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 51 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up: cast OffensivePotion | as ready |
| 52 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Blood Frenzy: Cleave 3: Fight-end Bite is worthwhile” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Ferocious Bite | 0.3 |
| 53 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid with Blood Frenzy: next target is worth switching to”: change target | as ready |
| 54 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid with Blood Frenzy: previous target is worth switching to”: change target | as ready |
| 55 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and Clearcasting is up and not “Blood Frenzy: 3 targets: Hybrid: Pool energy for Bite” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 9.0 |
| 56 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and “Cleave 3: Rip due” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Rip | 4.4 |
| 57 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and “Blood Frenzy: Cleave 3: Rake due”: cast Rake | 6.1 |
| 58 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Blood Frenzy: Cleave 3: 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 9.0 |
| 59 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and combo points ≥ 4 and time left on Rip ≥ 2s and (Clearcasting is up and energy ≥ 30 or energy ≥ 50) and not “3 targets: Hybrid: leave this global for the target switch”: cast Ferocious Bite | 0.3 |
| 60 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 61 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 62 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up: cast OffensivePotion | as ready |
| 63 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Cleave 3: Fight-end Bite is worthwhile” and not “3 targets: Hybrid: leave this global for the target switch”: cast Ferocious Bite | 0.3 |
| 64 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid: next target is worth switching to”: change target | as ready |
| 65 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid: previous target is worth switching to”: change target | as ready |
| 66 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and Clearcasting is up and not “3 targets: Hybrid: Pool energy for Bite” and not “3 targets: Hybrid: leave this global for the target switch”: cast Shred | 9.0 |
| 67 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and “Cleave 3: Rip due” and not “3 targets: Hybrid: leave this global for the target switch”: cast Rip | 4.4 |
| 68 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and “Cleave 3: Rake due”: cast Rake | 6.1 |
| 69 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 3: 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid: leave this global for the target switch”: cast Shred | 9.0 |
| 70 | if not (number of targets = 2 or number of targets = 3) and “Midfight Bite is worthwhile”: cast Ferocious Bite | 0.3 |
| 71 | if not (number of targets = 2 or number of targets = 3) and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 72 | if not (number of targets = 2 or number of targets = 3) and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 73 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up: cast OffensivePotion | as ready |
| 74 | if not (number of targets = 2 or number of targets = 3) and “Fight-end Bite is worthwhile”: cast Ferocious Bite | 0.3 |
| 75 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and Clearcasting is up and not “Pool energy for Bite”: cast Shred | 9.0 |
| 76 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and “Rip due”: cast Rip | 4.4 |
| 77 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and “Rake due”: cast Rake | 6.1 |
| 78 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Paid builder fits the energy pool”: cast Shred | 9.0 |

Lines of the simulator's rotation these builds never cast: cast Ravage, cast Cat Form, cast Elune's Light, 2 targets: Shred: Paid builder fits the energy pool” and not “2 targets: Shred: leave this global for the target switch”: cast Claw, Shred: Pool energy for Bite” and not “2 targets: Shred: leave this global for the target switch”: cast Claw, cast Innervate, 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, Hybrid: Pool energy for Bite” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid: leave this global for the target switch”: cast Claw, Hybrid: Pool energy for Bite” and not “2 targets: Hybrid: leave this global for the target switch”: cast Claw, 3 targets: Shred: Paid builder fits the energy pool” and not “3 targets: Shred: leave this global for the target switch”: cast Claw, Shred: Pool energy for Bite” and not “3 targets: Shred: leave this global for the target switch”: cast Claw, Cleave 3: 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, 3 targets: Hybrid: Pool energy for Bite” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid: leave this global for the target switch”: cast Claw, Hybrid: Pool energy for Bite” and not “3 targets: Hybrid: leave this global for the target switch”: cast Claw, cast Claw (its condition never held in these fights); cast Shifting Power (needs the Shifting Power talent).

Damage by ability:

| Ability | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) |
|---|---|
| Rip | 36% |
| Auto Attack | 24% |
| Rake | 22% |
| Shred | 16% |
| Goblin Sapper Charge | 1% |
| Ferocious Bite | 1% |
| spell 18211 | 0% |

## Notes

- Report: druid/research/talents/forever/optimizer/feral-cat-dps-raid-dps.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 9/31/11 -> 9/30/12; Berserk 1 gone; refill +1 Reflection (refill: the feral-cat-dps model, raid-dps).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
