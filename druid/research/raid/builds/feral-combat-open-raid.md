# Feral Combat — Raid (open talent search) — 9/32/10

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/32/10 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Feral Combat raid build the open talent search found on 2026-11-01: every legal 51-point build with no tree rule, searched in the community simulator's feral-cat-dps rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). 

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Furor** | 2/5 | changed | Gives you a 40% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 40% of the Energy you had when last in Cat Form, plus 4 Energy per second spent outside Bear Form or Dire Bear Form, up to 40 Energy. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Predatory Discipline** | 1/1 | **NEW** | Your Ferocious Bite ability no longer converts extra Energy into damage, but still deals extra damage based on your excess Energy. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 15%. |
| **Shifting Power** | 1/1 | **NEW** | Instantly convert 55% of base Mana into 40 Energy. Shifting Power's cost is reduced by effects that reduce the cost of Shapeshifting. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |

### Restoration (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |

## Core talents (priority order)

1. **Shifting Power** — 120 DPS lost without it (16% of the build in a full raid; removal, 12,000 fights).
2. **Naturalist** — 68 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
3. **Shredding Attacks** — 64 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Rend and Tear** — 42 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
5. **Sharpened Claws** — 38 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
6. **Natural Instinct** — 28 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
7. **Genesis** — 25 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
8. **Nature's Majesty** — 25 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**3 of 6** for `feral-cat-dps` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Cat* | community simulator | - | 549 | +0.0% | 924 | -1.2% | 37 s |
| 2 | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) | ours: derived (simulator preset) | 9/33/9 | 545 | -0.7% | 918 | -1.8% | 37 s |
| 3 | **[`feral-combat-open-raid`](feral-combat-open-raid.md)** | ours: derived (open search) | 9/32/10 | 537 | -2.1% | 935 | +0.0% | 38 s |
| 4 | *Hybrid* | community simulator | - | 501 | -8.6% | 864 | -7.6% | 42 s |
| 5 | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) | ours: optimizer | 9/30/12 | 475 | -13.4% | 772 | -17.4% | 0 s |
| 6 | [`feral-cat-dps`](feral-cat-dps.md) | ours: hand draft | 9/32/10 | 466 | -15.0% | 758 | -18.9% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/druid/upstream/adaptive.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-10-10 (10 changes, `feral-cat-dps-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/druid/upstream/adaptive.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-11-02 (10 changes, `feral-cat-dps-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: at -33s: if Manual Crowd Pummeler is known: swap to the Swap1 item set; at -1s: cast Prowl; at -0.01s: if not activeItemSwapSet: swap to the Main item set; at -0.01s: cast Dash.

| # | Priority (the first line whose condition holds is cast) | [`feral-combat-open-raid`](feral-combat-open-raid.md) casts/min |
|---|---|---|
| 1 | if “Ready to return to the main weapon”: swap to the Main item set | as ready |
| 2 | if “Drop Prowl for this opener”: cancel Prowl | as ready |
| 3 | if Faerie Fire is known and Faerie Fire should be refreshed: cast Faerie Fire | 1.9 |
| 4 | if unitDistance > 5: move to 5 yd | as ready |
| 5 | if unitDistance > 5: wait until not (unitDistance > 5) | as ready |
| 6 | if “Ready to activate MCP”: cast Manual Crowd Pummeler | as ready |
| 7 | if not Cat Form is up: cast Cat Form | 0.3 |
| 8 | if “Final-global Bite”: cast Ferocious Bite (rank 5) | 0.6 |
| 9 | use every other cooldown when ready | as ready |
| 10 | if “Mana potion fits and is needed”: cast ResourcePotion on self | as ready |
| 11 | if number of targets = 2 and “Use Shred cleave tuning” and time until the global cooldown is ready ≤ 0s and “2 targets: Shred: next target is worth switching to”: change target | as ready |
| 12 | if number of targets = 2 and “Use Shred cleave tuning” and “2 targets: Shred: Midfight Bite is worthwhile” and not “2 targets: Shred: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.6 |
| 13 | if number of targets = 2 and “Use Shred cleave tuning” and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 14 | if number of targets = 2 and “Use Shred cleave tuning” and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 15 | if number of targets = 2 and “Use Shred cleave tuning” and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 16 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up: cast OffensivePotion | as ready |
| 17 | if number of targets = 2 and “Use Shred cleave tuning” and “Cleave 2: Fight-end Bite is worthwhile” and not “2 targets: Shred: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.6 |
| 18 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and Clearcasting is up and not “2 targets: Shred: Pool energy for Bite” and not “2 targets: Shred: leave this global for the target switch”: cast Shred | 14.4 |
| 19 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 2: 2 targets: Shred: Rip due” and not “2 targets: Shred: leave this global for the target switch”: cast Rip | 4.7 |
| 20 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 2: Rake due”: cast Rake | 6.2 |
| 21 | if number of targets = 2 and “Use Shred cleave tuning” and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 2: 2 targets: Shred: Paid builder fits the energy pool” and not “2 targets: Shred: leave this global for the target switch”: cast Shred | 14.4 |
| 22 | if number of targets = 2 and “Use Shred cleave tuning” and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 23 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 24 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 25 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 26 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up: cast OffensivePotion | as ready |
| 27 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Cleave 2: Fight-end Bite is worthwhile” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.6 |
| 28 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “2 targets: Hybrid with Blood Frenzy: next target is worth switching to”: change target | as ready |
| 29 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and Clearcasting is up and not “2 targets: Hybrid: Pool energy for Bite” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 14.4 |
| 30 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and “Blood Frenzy: Cleave 2: Rip due” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Rip | 4.7 |
| 31 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and “Blood Frenzy: Cleave 2: Rake due”: cast Rake | 6.2 |
| 32 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 2: 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 14.4 |
| 33 | if number of targets = 2 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 34 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 35 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 36 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 37 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up: cast OffensivePotion | as ready |
| 38 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Cleave 2: Fight-end Bite is worthwhile” and not “2 targets: Hybrid: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.6 |
| 39 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “2 targets: Hybrid: next target is worth switching to”: change target | as ready |
| 40 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and Clearcasting is up and not “2 targets: Hybrid: Pool energy for Bite” and not “2 targets: Hybrid: leave this global for the target switch”: cast Shred | 14.4 |
| 41 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and “Cleave 2: Rip due” and not “2 targets: Hybrid: leave this global for the target switch”: cast Rip | 4.7 |
| 42 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and “Cleave 2: Rake due”: cast Rake | 6.2 |
| 43 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 2: 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid: leave this global for the target switch”: cast Shred | 14.4 |
| 44 | if number of targets = 2 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 45 | if number of targets = 3 and “Use Shred cleave tuning” and time until the global cooldown is ready ≤ 0s and “3 targets: Shred: next target is worth switching to”: change target | as ready |
| 46 | if number of targets = 3 and “Use Shred cleave tuning” and time until the global cooldown is ready ≤ 0s and “3 targets: Shred: previous target is worth switching to”: change target | as ready |
| 47 | if number of targets = 3 and “Use Shred cleave tuning” and “3 targets: Shred: Midfight Bite is worthwhile” and not “3 targets: Shred: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.6 |
| 48 | if number of targets = 3 and “Use Shred cleave tuning” and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 49 | if number of targets = 3 and “Use Shred cleave tuning” and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 50 | if number of targets = 3 and “Use Shred cleave tuning” and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 51 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up: cast OffensivePotion | as ready |
| 52 | if number of targets = 3 and “Use Shred cleave tuning” and “Cleave 3: Fight-end Bite is worthwhile” and not “3 targets: Shred: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.6 |
| 53 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and Clearcasting is up and not “3 targets: Shred: Pool energy for Bite” and not “3 targets: Shred: leave this global for the target switch”: cast Shred | 14.4 |
| 54 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 3: 3 targets: Shred: Rip due” and not “3 targets: Shred: leave this global for the target switch”: cast Rip | 4.7 |
| 55 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and “Cleave 3: Rake due”: cast Rake | 6.2 |
| 56 | if number of targets = 3 and “Use Shred cleave tuning” and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 3: 3 targets: Shred: Paid builder fits the energy pool” and not “3 targets: Shred: leave this global for the target switch”: cast Shred | 14.4 |
| 57 | if number of targets = 3 and “Use Shred cleave tuning” and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 58 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 59 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 60 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 61 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up: cast OffensivePotion | as ready |
| 62 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Blood Frenzy: Cleave 3: Fight-end Bite is worthwhile” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.6 |
| 63 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid with Blood Frenzy: next target is worth switching to”: change target | as ready |
| 64 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid with Blood Frenzy: previous target is worth switching to”: change target | as ready |
| 65 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and Clearcasting is up and not “Blood Frenzy: 3 targets: Hybrid: Pool energy for Bite” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 14.4 |
| 66 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and “Cleave 3: Rip due” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Rip | 4.7 |
| 67 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and “Blood Frenzy: Cleave 3: Rake due”: cast Rake | 6.2 |
| 68 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Blood Frenzy: Cleave 3: 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Shred | 14.4 |
| 69 | if number of targets = 3 and not “Use Shred cleave tuning” and Blood Frenzy is taken and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 70 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and combo points ≥ 4 and time left on Rip ≥ 2s and (Clearcasting is up and energy ≥ 30 or energy ≥ 50) and not “3 targets: Hybrid: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.6 |
| 71 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 72 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 73 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 74 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up: cast OffensivePotion | as ready |
| 75 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Cleave 3: Fight-end Bite is worthwhile” and not “3 targets: Hybrid: leave this global for the target switch”: cast Ferocious Bite (rank 5) | 0.6 |
| 76 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid: next target is worth switching to”: change target | as ready |
| 77 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and time until the global cooldown is ready ≤ 0s and “3 targets: Hybrid: previous target is worth switching to”: change target | as ready |
| 78 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and Clearcasting is up and not “3 targets: Hybrid: Pool energy for Bite” and not “3 targets: Hybrid: leave this global for the target switch”: cast Shred | 14.4 |
| 79 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and “Cleave 3: Rip due” and not “3 targets: Hybrid: leave this global for the target switch”: cast Rip | 4.7 |
| 80 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and “Cleave 3: Rake due”: cast Rake | 6.2 |
| 81 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Cleave 3: 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid: leave this global for the target switch”: cast Shred | 14.4 |
| 82 | if number of targets = 3 and not “Use Shred cleave tuning” and not Blood Frenzy is taken and “Innervate can restore needed mana”: cast Innervate | 0.3 |
| 83 | if not (number of targets = 2 or number of targets = 3) and “Midfight Bite is worthwhile”: cast Ferocious Bite (rank 5) | 0.6 |
| 84 | if not (number of targets = 2 or number of targets = 3) and “Shifting Power ready”: cast Shifting Power | 5.5 |
| 85 | if not (number of targets = 2 or number of targets = 3) and “Tea is selected and energy is low”: cast Thistle Tea | as ready |
| 86 | if not (number of targets = 2 or number of targets = 3) and “Rune can restore mana after Tea”: cast Demonic Rune | as ready |
| 87 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up: cast OffensivePotion | as ready |
| 88 | if not (number of targets = 2 or number of targets = 3) and “Fight-end Bite is worthwhile”: cast Ferocious Bite (rank 5) | 0.6 |
| 89 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and Clearcasting is up and not “Pool energy for Bite”: cast Shred | 14.4 |
| 90 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and “Rip due”: cast Rip | 4.7 |
| 91 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and “Rake due”: cast Rake | 6.2 |
| 92 | if not (number of targets = 2 or number of targets = 3) and Cat Form is up and not “Use Claw for paid builders” and energy ≥ current cost and “Paid builder fits the energy pool”: cast Shred | 14.4 |
| 93 | if not (number of targets = 2 or number of targets = 3) and “Innervate can restore needed mana”: cast Innervate | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Ravage, cast Elune's Light, 2 targets: Shred: Paid builder fits the energy pool” and not “2 targets: Shred: leave this global for the target switch”: cast Claw, Shred: Pool energy for Bite” and not “2 targets: Shred: leave this global for the target switch”: cast Claw, 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, Hybrid: Pool energy for Bite” and not “2 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, 2 targets: Hybrid: Paid builder fits the energy pool” and not “2 targets: Hybrid: leave this global for the target switch”: cast Claw, Hybrid: Pool energy for Bite” and not “2 targets: Hybrid: leave this global for the target switch”: cast Claw, 3 targets: Shred: Paid builder fits the energy pool” and not “3 targets: Shred: leave this global for the target switch”: cast Claw, Shred: Pool energy for Bite” and not “3 targets: Shred: leave this global for the target switch”: cast Claw, Cleave 3: 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, 3 targets: Hybrid: Pool energy for Bite” and not “3 targets: Hybrid with Blood Frenzy: leave this global for the target switch”: cast Claw, 3 targets: Hybrid: Paid builder fits the energy pool” and not “3 targets: Hybrid: leave this global for the target switch”: cast Claw, Hybrid: Pool energy for Bite” and not “3 targets: Hybrid: leave this global for the target switch”: cast Claw, cast Claw (its condition never held in these fights).

Damage by ability:

| Ability | [`feral-combat-open-raid`](feral-combat-open-raid.md) |
|---|---|
| Rip | 35% |
| Shred | 22% |
| Auto Attack | 20% |
| Rake | 19% |
| Ferocious Bite | 2% |
| Goblin Sapper Charge | 1% |
| spell 18211 | 0% |

## Notes

- +20.8% over the best hand draft of the spec, feral-cat-dps, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (feral-cat-dps, full raid): 9/32/10 (Feral Combat) at 767.7 DPS; feral-combat-shifting-power-raid 754.3, opt-feral-cat-dps-raid-dps 642.6, feral-cat-dps 635.3 in the same fights; 4,174 builds simulated, 2 independent runs reached the top.
- Sibling rotations tried on it (10,000 fights): balance-dps -66.1%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Leader of the Pack.
- Simulator numbers are the community's model of the beta (wowsims/forever 54ceac6 (client 70707) with this project's patches), not in-game measurements.
- 2026-11-01 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Leader of the Pack -> Feral Charge (interrupt); Furor -> Thick Hide (survival); Furor -> Thick Hide (survival); Furor -> Thick Hide (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Feral Combat build: check it against the community's Feral Combat builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/druid/60/050022-55000032023012125001-055-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
