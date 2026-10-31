# Feral Combat — Raid (open talent search) — 9/32/10

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/32/10 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Feral Combat raid build the open talent search found on 2026-10-26: every legal 51-point build with no tree rule, searched in the community simulator's feral-cat-dps rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). 

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Predatory Discipline** | 1/1 | **NEW** | Your Ferocious Bite ability no longer converts extra Energy into damage, but still deals extra damage based on your excess Energy. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the melee and ranged Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |
| **Shifting Power** | 1/1 | **NEW** | Instantly convert 55% of base Mana into 40 Energy. Shifting Power's cost is reduced by effects that reduce the cost of Shapeshifting. |

### Restoration (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |

## Core talents (priority order)

1. **Shifting Power** — 124 DPS lost without it (16% of the build in a full raid; removal, 12,000 fights).
2. **Shredding Attacks** — 70 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
3. **Improved Shifting Power** — 56 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
4. **Rend and Tear** — 41 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
5. **Sharpened Claws** — 34 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
6. **Natural Instinct** — 29 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
7. **Naturalist** — 28 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
8. **Savage Fury** — 25 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**2 of 6** for `feral-cat-dps` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) | ours: derived (simulator preset) | 9/35/7 | 361 | +0.0% | 743 | -1.5% | 66 s |
| 2 | **[`feral-combat-open-raid`](feral-combat-open-raid.md)** | ours: derived (open search) | 9/33/9 | 358 | -0.8% | 754 | +0.0% | 66 s |
| 3 | *Hybrid* | community simulator | - | 352 | -2.4% | 722 | -4.2% | 65 s |
| 4 | *Cat* | community simulator | - | 351 | -2.7% | 736 | -2.5% | 66 s |
| 5 | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) | ours: optimizer | 9/31/11 | 334 | -7.3% | 643 | -14.7% | 0 s |
| 6 | [`feral-cat-dps`](feral-cat-dps.md) | ours: hand draft | 9/32/10 | 325 | -10.0% | 630 | -16.5% | 0 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 8 passes, the last 2026-10-26, 9 changes to the base rotation; third-seed check: feral-combat-open-raid 757 -> 754 DPS (-0.4%), feral-combat-shifting-power-raid 750 -> 743 DPS (-0.9%), feral-cat-dps 635 -> 630 DPS (-0.7%), opt-feral-cat-dps-raid-dps 644 -> 643 DPS (-0.1%)):
  1. drop: if combo points = 5.0 and not Clearcasting is up and (energy + 20.2) < (current cost + current cost): cast Ferocious Bite (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if combo points ≥ 5 and not Rip is on the target: cast Rip (+1.3%, pass 1)
  3. drop: if not Cat Form is up and mana % ≤ 40% and time left in the fight ≥ 20.0 and not (Demonic Rune is known and Demonic Rune is ready or Potion is known and Potion is ready): cast Innervate (+0.5%, pass 1)
  4. threshold 27.8 -> 13.9: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 27.8: cancel Cat Form (+0.2%, pass 1)
  5. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and (combo points < 5.0 and (energy + 20.2) < current cost or combo points = 5.0 and (energy + 20.2) < current cost or Clearcasting is known and Clearcasting is up and energy < 27.8): cancel Cat Form (+0.2%, pass 4)
  6. insert in the middle: if Shifting Power is known and energy ≤ 60: cast Shifting Power (+9.9%, pass 5)
  7. insert at the top: if combo points < 5 and not Rake is on the target and time left in the fight > 6s: cast Rake (+7.5%, pass 7)
  8. drop 'combo points < 5' from the condition: if combo points < 5 and not Rake is on the target and time left in the fight > 6s: cast Rake (+0.5%, pass 7)
  9. insert at the top: if (combo points ≥ 5 and not time left in the fight ≥ 10s or combo points ≥ 3 and time left in the fight < 3s): cast Ferocious Bite (rank 4) (+0.2%, pass 8)

Before the pull: at -1.0s: cast Faerie Fire; at -3.5s: cast Tiger's Fury.

| # | Priority (the first line whose condition holds is cast) | [`feral-combat-open-raid`](feral-combat-open-raid.md) casts/min |
|---|---|---|
| 1 | if Faerie Fire should be refreshed: cast Faerie Fire | 8.9 |
| 2 | if Cat Form is up: use every other cooldown when ready | as ready |
| 3 | if combo points ≥ 3.75 and not Rip is on the target: cast Rip | 4.6 |
| 4 | cast Shred | 17.6 |
| 5 | if Shifting Power is known and energy ≤ 60: cast Shifting Power | 3.3 |
| 6 | if time left in the fight ≥ 6s: cast Faerie Fire | 8.9 |
| 7 | cast Goblin Sapper Charge | as ready |
| 8 | if not Cat Form is up and (mana + 1500.0) ≤ (mana ÷ mana %): cast Demonic Rune | as ready |
| 9 | if not Cat Form is up and (mana + 2250.0) ≤ (mana ÷ mana %): cast Potion | as ready |
| 10 | if not Cat Form is up: cast Cat Form | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Tiger's Fury, cast Haste, cast Metamorphosis Rune, cast Innervate (its condition never held in these fights).

Damage by ability:

| Ability | [`feral-combat-open-raid`](feral-combat-open-raid.md) |
|---|---|
| Rip | 36% |
| Shred | 32% |
| Auto Attack | 31% |
| Goblin Sapper Charge | 2% |

## Notes

- +19.7% over the best hand draft of the spec, feral-cat-dps, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (feral-cat-dps, full raid): 9/33/9 (Feral Combat) at 753.7 DPS; feral-combat-shifting-power-raid 743.2, opt-feral-cat-dps-raid-dps 643.1, feral-cat-dps 629.8 in the same fights; 4,989 builds simulated, 2 independent runs reached the top.
- Sibling rotations tried on it (10,000 fights): balance-dps -65.6%; none adopted.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 9/33/9 -> 9/32/10; Improved Shifting Power 2 gone; Berserk 1 gone; +1 Blood Frenzy (tier gating for Rend and Tear); +1 Predatory Discipline (prerequisite of Shifting Power); refill +1 Naturalist (refill: the feral-cat-dps model, raid-dps).

## Open questions (verify in the live game)

- An open-search Feral Combat build: check it against the community's Feral Combat builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/druid/60/050022-55000032021031212051-054-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
