# Optimizer — White 40%, Shred 30% (60 energy), Ferocious Bite 15%, Rip 10%, Claw/Rake 5% (raid-dps) — 9/31/11

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/31/11 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `feral-cat-dps` and profile `raid-dps`: score +91.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Ferocity** | 2/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 2 Rage or Energy. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the critical strike chance of all party members within 45 yards by 3%, exclusive with Moonkin Aura. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |
| **Berserk** | 1/1 | **NEW** | Causes your Primal Bite ability to strike up to 3 targets, removes its cooldown, and increases the critical strike chance of your Combo Point-generating abilities by 100%. Clears and grants immunity to Fear effects for the duration. Lasts 15 sec. |

### Restoration (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per sec spent outside Cat Form, up to 100 Energy.  Bear Form and Dire Bear Form forfeit this Energy and halt its restoration while active. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Reflection** | 1/3 | changed | Allows 17% of your Mana regeneration to continue while casting. |

## Core talents (priority order)

1. **Shredding Attacks** — Removing it costs 29.9 points of score in this model.
2. **Blood Frenzy** — Removing it costs 14.4 points of score in this model.
3. **Sharpened Claws** — Removing it costs 9.8 points of score in this model.
4. **Rend and Tear** — Removing it costs 9.5 points of score in this model.
5. **Naturalist** — Removing it costs 9.1 points of score in this model.
6. **Predatory Strikes** — Removing it costs 6.1 points of score in this model.
7. **Natural Instinct** — Removing it costs 5.9 points of score in this model.
8. **Nature's Reach** — Removing it costs 5.6 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 5** for `feral-cat-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md)** | ours: optimizer | 9/31/11 | 368 | +0.0% | 594 | -14.1% | 0 s |
| 2 | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) | ours: hand draft | 9/35/7 | 357 | -2.9% | 691 | +0.0% | 0 s |
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

| # | Priority (the first line whose condition holds is cast) | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) casts/min |
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

| Ability | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) |
|---|---|
| Rip | 38% |
| Auto Attack | 32% |
| Shred | 27% |
| Goblin Sapper Charge | 2% |
| Dragonbreath Chili | 1% |

## Notes

- Report: druid/research/talents/forever/optimizer/feral-cat-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
