# Feral Combat — Shifting Power (the simulator's Feral Cat 9/35/7) — 9/35/7

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/35/7 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The community simulator's own Feral Cat preset (9/35/7), raced against our Feral builds in a full raid: 691 DPS against 594 for our best (+16.4%). It takes Shifting Power, Improved Shifting Power, Feral Charge and 5 Ferocity, which the raid rotation's powershifting (Furor) pays for, where our builds, optimized on the training dummy (368 against its 357 there), took Thick Hide, Reflection and 5 Naturalist.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Shifting Power** | 1/1 | **NEW** | Instantly convert 55% of base Mana into 40 Energy. Shifting Power's cost is reduced by effects that reduce the cost of Shapeshifting. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Improved Shifting Power** | 2/2 | **NEW** | Reduces the cooldown of your Shifting Power spell by 8 sec. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the critical strike chance of all party members within 45 yards by 3%, exclusive with Moonkin Aura. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |
| **Berserk** | 1/1 | **NEW** | Causes your Primal Bite ability to strike up to 3 targets, removes its cooldown, and increases the critical strike chance of your Combo Point-generating abilities by 100%. Clears and grants immunity to Fear effects for the duration. Lasts 15 sec. |

### Restoration (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per sec spent outside Cat Form, up to 100 Energy.  Bear Form and Dire Bear Form forfeit this Energy and halt its restoration while active. |
| **Naturalist** | 2/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.2 sec and increases all damage you deal by 2%. |

## Rank among our builds and the community simulator's

**2 of 5** for `feral-cat-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) | ours: optimizer | 9/31/11 | 368 | +0.0% | 594 | -14.1% | 0 s |
| 2 | **[`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md)** | ours: hand draft | 9/35/7 | 357 | -2.9% | 691 | +0.0% | 0 s |
| 3 | *Feral Cat 9/35/7* | community simulator | - | 357 | -2.9% | 691 | +0.0% | 0 s |
| 4 | [`feral-cat-dps`](feral-cat-dps.md) | ours: hand draft | 9/32/10 | 357 | -3.0% | 579 | -16.2% | 0 s |
| 5 | *Feral* | community simulator | - | 340 | -7.7% | 665 | -3.8% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-10-02, 9 changes to the base rotation; third-seed check: ml: Feral Combat 346 -> 371 DPS (+7.2%), sim preset: Feral Cat 9/35/7 346 -> 371 DPS (+7.2%)):
  1. drop: if combo points = 5.0 and not Clearcasting is up and (energy + 20.2) < (current cost + current cost): cast Ferocious Bite (+2.2%, pass 1)
  2. threshold 5 -> 3.75: if combo points ≥ 5 and not Rip is on the target: cast Rip (+1.6%, pass 1)
  3. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and (combo points < 5.0 and (energy + 20.2) < current cost or combo points = 5.0 and (energy + 20.2) < current cost or Clearcasting is known and Clearcasting is up and energy < 27.8): cancel Cat Form (+1.1%, pass 1)
  4. threshold 27.8 -> 13.9: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 27.8: cancel Cat Form (+0.4%, pass 1)
  5. drop the condition: if not Cat Form is up: cast Goblin Sapper Charge (+0.2%, pass 1)
  6. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 13.9: cancel Cat Form (+0.2%, pass 1)
  7. threshold 14.0s -> 28s: if Faerie Fire should be refreshed: cast Faerie Fire (+0.2%, pass 1)
  8. drop the condition: if Faerie Fire should be refreshed: cast Faerie Fire (+0.6%, pass 4)
  9. only with 6s or more of the fight left: cast Faerie Fire (+0.8%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-09, 6 changes to the base rotation; third-seed check: opt-feral-cat-dps-raid-dps 582 -> 593 DPS (+1.9%), sim preset: Feral Cat 9/35/7 680 -> 691 DPS (+1.6%), feral-cat-dps 570 -> 579 DPS (+1.5%)):
  1. drop: if combo points = 5.0 and not Clearcasting is up and (energy + 20.2) < (current cost + current cost): cast Ferocious Bite (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if combo points ≥ 5 and not Rip is on the target: cast Rip (+1.3%, pass 1)
  3. drop: if not Cat Form is up and mana % ≤ 40% and time left in the fight ≥ 20.0 and not (Demonic Rune is known and Demonic Rune is ready or Potion is known and Potion is ready): cast Innervate (+0.5%, pass 1)
  4. threshold 27.8 -> 13.9: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 27.8: cancel Cat Form (+0.2%, pass 1)
  5. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and (combo points < 5.0 and (energy + 20.2) < current cost or combo points = 5.0 and (energy + 20.2) < current cost or Clearcasting is known and Clearcasting is up and energy < 27.8): cancel Cat Form (+0.2%, pass 4)
  6. insert in the middle: if Shifting Power is known and energy ≤ 60: cast Shifting Power (+9.9%, pass 5)

Before the pull: at -1.0s: cast Faerie Fire; at -3.5s: cast Tiger's Fury.

| # | Priority (the first line whose condition holds is cast) | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) casts/min |
|---|---|---|
| 1 | cast Tiger's Fury | 2.3 |
| 2 | if Faerie Fire should be refreshed: cast Faerie Fire | 39.7 |
| 3 | if Cat Form is up: use every other cooldown when ready | as ready |
| 4 | if combo points ≥ 3.75 and not Rip is on the target: cast Rip | 4.7 |
| 5 | cast Shred | 14.8 |
| 6 | if time left in the fight ≥ 6s: cast Faerie Fire | 39.7 |
| 7 | cast Goblin Sapper Charge | as ready |
| 8 | if not Cat Form is up and (mana + 1500.0) ≤ (mana ÷ mana %): cast Demonic Rune | as ready |
| 9 | if not Cat Form is up and (mana + 2250.0) ≤ (mana ÷ mana %): cast Potion | as ready |
| 10 | if not Cat Form is up: cast Cat Form | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Haste, cast Metamorphosis Rune, cast Innervate (its condition never held in these fights).

Damage by ability:

| Ability | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) |
|---|---|
| Rip | 38% |
| Auto Attack | 32% |
| Shred | 27% |
| Goblin Sapper Charge | 2% |
| Dragonbreath Chili | 1% |

## Notes

- Raced 2026-10-09 in the feral-cat-dps entry (ElliotWood/Forever 2ce8265 with this project's patches, full raid, 180 s): sim preset Feral Cat 9/35/7 691.1, sim preset Feral 664.9, opt-feral-cat-dps-raid-dps 593.6, feral-cat-dps 579.1 DPS.
- Written by hand from the race until the druid's open talent search (the 70291 sweep) rebuilds the Feral raid pick; the hand draft feral-cat-dps stays as the alternative.
- Simulator numbers are the community's model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- Does powershifting work in Forever as the simulator plays it (Furor's energy on every Cat Form)? Check at launch.

## Sources

- <https://github.com/ElliotWood/Forever (ui/specs/druid/feral presets: Feral Cat 9/35/7)>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
