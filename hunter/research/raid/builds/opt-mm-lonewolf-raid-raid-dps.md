# Optimizer — Marksmanship without a pet (Forever Lone Wolf) (raid-dps) — 7/41/3

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/41/3 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `mm-lonewolf-raid` and profile `raid-dps`: score +83.7% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Improved Revive Pet** | 2/2 | unchanged | Revive Pet's casting time is reduced by 6 sec, mana cost is reduced by 40%, and increases the health your pet returns with by an additional 30%. |

### Marksmanship (41)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Hawk Eye** | 3/3 | moved | Increases the range of your ranged weapons by 6 yards. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Rapid Recuperation** | 2/2 | **NEW** | Afflicting a target with Serpent Sting allows 50% of your Mana Regeneration to continue while casting for 15 sec, increased to 100% when Rapid Killing is consumed. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 15%. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |
| **Sniper Shot** | 1/1 | **NEW** | A long-range shot that deals ranged damage plus 160 and increases the range of your next 3 Shots by 10 yards for 10 sec. |

### Survival (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 3/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 3%. |

## Core talents (priority order)

1. **Lone Wolf** — Removing it costs 30.4 points of score in this model.
2. **Efficiency** — Removing it costs 11.7 points of score in this model.
3. **Careful Aim** — Removing it costs 11.0 points of score in this model.
4. **Lethal Attacks** — Removing it costs 9.6 points of score in this model.
5. **Improved Tracking** — Removing it costs 8.7 points of score in this model.
6. **Ranged Weapon Specialization** — Removing it costs 8.7 points of score in this model.
7. **Deadly Aspects** — Removing it costs 8.7 points of score in this model.
8. **Mortal Shots** — Removing it costs 7.8 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 10** for `mm-lonewolf-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *MM* | community simulator | - | 486 | +0.0% | 996 | -0.7% | 41 s |
| 2 | **[`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md)** | ours: optimizer | 7/41/3 | 478 | -1.6% | 929 | -7.3% | 24 s |
| 3 | [`mm-lone-wolf-raid`](mm-lone-wolf-raid.md) | ours: hand draft | 5/41/5 | 475 | -2.2% | 1003 | +0.0% | 47 s |
| 4 | *SV* | community simulator | - | 427 | -12.1% | 824 | -17.8% | 38 s |
| 5 | *SV Weave* | community simulator | - | 421 | -13.2% | 818 | -18.4% | 38 s |
| 6 | *MM Weave* | community simulator | - | 412 | -15.1% | 826 | -17.6% | 45 s |
| 7 | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) | ours: derived (ML search) | 7/39/5 | 407 | -16.1% | 810 | -19.2% | 29 s |
| 8 | *BM Weave* | community simulator | - | 309 | -36.3% | 632 | -37.0% | 26 s |
| 9 | *BM* | community simulator | - | 300 | -38.3% | 643 | -35.8% | 31 s |
| 10 | *SV Melee* | community simulator | - | 269 | -44.7% | 597 | -40.5% | 45 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 9 passes, the last 2026-10-07, 9 changes to the base rotation; third-seed check: open winner 396 -> 444 DPS (+12.2%), opt-mm-lonewolf-raid-raid-dps 422 -> 463 DPS (+9.5%), sim preset: Beast Mastery 35/16/0 298 -> 381 DPS (+27.8%), mm-lone-wolf-raid 405 -> 457 DPS (+12.8%), marksmanship-ml-raid 403 -> 444 DPS (+10.3%)):
  1. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+3.3%, pass 1)
  2. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.4%, pass 1)
  3. threshold 1s -> 0.5s: if time to the next auto attack > 1s: cast Aimed Shot (+0.7%, pass 1)
  4. threshold 1s -> 2s: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting (+0.2%, pass 1)
  5. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 2)
  6. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+5.5%, pass 4)
  7. move down below 'cast Arcane Shot': if time to the next auto attack > 0.5s: cast Aimed Shot (+0.4%, pass 6)
  8. only with 10s or more of the fight left: if auraIsInactive: cast Summon Hawk (+0.2%, pass 6)
  9. drop: if time to the next auto attack > 0.5s: cast Multi-Shot + only above 10% mana: if time to the next auto attack > 0.5s: cast Aimed Shot (+0.2%, pass 7)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 18 passes, the last 2026-11-10, 14 changes to the base rotation; third-seed check: mm-lone-wolf-raid 870 -> 965 DPS (+10.8%), sim preset: MM 866 -> 958 DPS (+10.6%), opt-mm-lonewolf-raid-raid-dps 858 -> 896 DPS (+4.5%), marksmanship-ml-raid 699 -> 752 DPS (+7.6%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.7%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 1)
  3. drop 'time to the next auto attack > 1s' from the condition: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.3%, pass 1)
  4. drop the condition: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.2%, pass 1)
  5. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+2.3%, pass 4)
  6. insert at the top: if time to the next auto attack > 1s: cast Aimed Shot (+2.7%, pass 5)
  7. drop the condition: if time to the next auto attack > 1s: cast Aimed Shot (+1.5%, pass 5)
  8. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+0.9%, pass 5)
  9. move down below 'if auraIsInactive: cast Summon Hawk': cast Aimed Shot (+0.3%, pass 6)
  10. drop: if auraIsInactive: cast Summon Hawk (+0.7%, pass 10)
  11. insert at the top: if time to the next auto attack > 1s: cast Summon Hawk (+0.3%, pass 10)
  12. only with 20s or more of the fight left: if time to the next auto attack > 1s: cast Summon Hawk (+0.2%, pass 10)
  13. insert at the end: cast Major Mana Potion (+0.6%, pass 13)
  14. threshold 1 -> 2: if time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.5%, pass 13)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 3 | cast Arcane Shot | 8.7 |
| 4 | if time to the next auto attack > 0.5s and mana % ≥ 10%: cast Aimed Shot | 5.0 |
| 5 | if time left on Serpent Sting < 2s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.8 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent).

Damage by ability:

| Ability | [`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md) |
|---|---|
| Auto Shot | 44% |
| Arcane Shot | 24% |
| Serpent Sting | 17% |
| Aimed Shot | 15% |

## Notes

- Allocation taken from cand-mm-lonewolf-raid-r1 on 2026-10-22: the optimizer's earlier round beat its last export in the community simulator (361 vs 358 DPS; the calibration moved the model past the better build).
- Report: hunter/research/talents/forever/optimizer/mm-lonewolf-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
