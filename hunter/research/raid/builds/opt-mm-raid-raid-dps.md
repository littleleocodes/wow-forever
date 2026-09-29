# Optimizer — Marksmanship raid DPS with a pet (Classic 20/31/0 style) (raid-dps) — 22/29/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/29/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `mm-raid` and profile `raid-dps`: score +55.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |

### Marksmanship (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Stings** | 3/3 | **NEW** | Increased the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Improved Arcane Shot** | 1/5 | changed | Reduces the cooldown of your Arcane Shot by 0.3 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yards by 30. Lasts 30 min. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Ranged Weapon Specialization** | 4/5 | unchanged | Increases the damage you deal with ranged weapons by 4%. |

### Survival (0)

*No points.*

## Core talents (priority order)

1. **Bestial Discipline** — Removing it costs 9.6 points of score in this model.
2. **Efficiency** — Removing it costs 8.6 points of score in this model.
3. **Mortal Shots** — Removing it costs 7.1 points of score in this model.
4. **Lethal Attacks** — Removing it costs 7.1 points of score in this model.
5. **Deadly Aspects** — Removing it costs 6.9 points of score in this model.
6. **Careful Aim** — Removing it costs 5.9 points of score in this model.
7. **Ranged Weapon Specialization** — Removing it costs 5.0 points of score in this model.
8. **Trueshot Aura** — Removing it costs 3.5 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 7** for `mm-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md)** | ours: optimizer | 22/29/0 | 415 | +0.0% | 761 | -3.4% | 78 s |
| 2 | [`bm-mm-raid`](bm-mm-raid.md) | ours: hand draft | 22/29/0 | 413 | -0.5% | 758 | -3.8% | 76 s |
| 3 | *Marksmanship* | community simulator | - | 388 | -6.4% | 788 | +0.0% | 99 s |
| 4 | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) | ours: hand draft | 20/31/0 | 386 | -7.0% | 784 | -0.5% | 93 s |
| 5 | *Beast Mastery 35/16/0* | community simulator | - | 370 | -10.7% | 691 | -12.4% | 92 s |
| 6 | *Marksmanship 0/39/12* | community simulator | - | 356 | -14.3% | 719 | -8.8% | 94 s |
| 7 | *Survival 0/15/36* | community simulator | - | 335 | -19.2% | 640 | -18.8% | 91 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 4 passes, the last 2026-09-29, 5 changes to the base rotation; third-seed check: opt-mm-raid-raid-dps 395 -> 428 DPS (+8.5%), sim preset: Marksmanship 360 -> 399 DPS (+10.9%)):
  1. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.3%, pass 1)
  2. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+1.7%, pass 1)
  3. threshold 0.5s -> 1s: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.6%, pass 1)
  4. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  5. only with 20s or more of the fight left: if time to the next auto attack > 1s: cast Aimed Shot (+0.2%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 4 passes, the last 2026-09-29, 3 changes to the base rotation; third-seed check: opt-mm-raid-raid-dps 644 -> 766 DPS (+19.0%), sim preset: Marksmanship 681 -> 817 DPS (+20.0%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.0%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  3. only with 6s or more of the fight left: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+0.2%, pass 1)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | cast Arcane Shot | 8.6 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 4 | if time to the next auto attack > 1s and time left in the fight ≥ 20s: cast Aimed Shot | 4.0 |
| 5 | if time to the next auto attack > 1s: cast Multi-Shot | 0.6 |
| 6 | if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.3 |

Damage by ability:

| Ability | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) |
|---|---|
| Auto Shot | 46% |
| Arcane Shot | 20% |
| Serpent Sting | 13% |
| Aimed Shot | 8% |
| Pet: Auto Attack | 8% |
| Pet: Claw | 2% |
| Pet: Bite | 1% |
| Multi-Shot | 1% |

## Notes

- Report: hunter/research/talents/forever/optimizer/mm-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
