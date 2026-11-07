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

**3 of 6** for `feral-cat-dps` by training-dummy DPS in the community simulator (wowsims/forever bac92db (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Cat* | community simulator | - | 372 | +0.0% | 750 | -1.1% | 61 s |
| 2 | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) | ours: derived (simulator preset) | 9/33/9 | 369 | -0.8% | 745 | -1.8% | 61 s |
| 3 | **[`feral-combat-open-raid`](feral-combat-open-raid.md)** | ours: derived (open search) | 9/32/10 | 365 | -1.9% | 758 | +0.0% | 61 s |
| 4 | *Hybrid* | community simulator | - | 339 | -8.9% | 711 | -6.3% | 62 s |
| 5 | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) | ours: optimizer | 9/30/12 | 335 | -9.9% | 630 | -16.9% | 0 s |
| 6 | [`feral-cat-dps`](feral-cat-dps.md) | ours: hand draft | 9/32/10 | 328 | -11.7% | 619 | -18.3% | 0 s |

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

Before the pull: at -1.0s: cast Faerie Fire; at -3.5s: cast Tiger's Fury.

| # | Priority (the first line whose condition holds is cast) | [`feral-combat-open-raid`](feral-combat-open-raid.md) casts/min |
|---|---|---|
| 1 | if Faerie Fire should be refreshed: cast Faerie Fire | 8.8 |
| 2 | if Cat Form is up: use every other cooldown when ready | as ready |
| 3 | if combo points ≥ 3.75 and not Rip is on the target: cast Rip | 4.7 |
| 4 | cast Shred | 17.8 |
| 5 | if Shifting Power is known and energy ≤ 60: cast Shifting Power | 3.7 |
| 6 | if time left in the fight ≥ 6s: cast Faerie Fire | 8.8 |
| 7 | cast Goblin Sapper Charge | as ready |
| 8 | if not Cat Form is up and (mana + 1500.0) ≤ (mana ÷ mana %): cast Demonic Rune | as ready |
| 9 | if not Cat Form is up and (mana + 2250.0) ≤ (mana ÷ mana %): cast Potion | as ready |

Lines of the simulator's rotation these builds never cast: cast Tiger's Fury, cast Haste, cast Metamorphosis Rune, cast Innervate, cast Cat Form (its condition never held in these fights).

Damage by ability:

| Ability | [`feral-combat-open-raid`](feral-combat-open-raid.md) |
|---|---|
| Rip | 39% |
| Auto Attack | 30% |
| Shred | 30% |
| Goblin Sapper Charge | 2% |

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
- <https://talentsforever.com/druid/60/050022-55000032023012125001-055-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
