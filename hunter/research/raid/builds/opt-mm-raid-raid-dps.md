# Optimizer — Marksmanship raid DPS with a pet (Classic 20/31/0 style) (raid-dps) — 31/16/4

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/16/4 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `mm-raid` and profile `raid-dps`: score +56.0% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 4/5 | changed | Increases the Health and Armor of your pets by 12%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Bestial Swiftness** | 1/1 | changed | Increases the movement speed of your pets by 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Intimidation** | 1/1 | changed | Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 5/5 | unchanged | Gives your pet a 100% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |
| **Bestial Wrath** | 1/1 | unchanged | Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be stopped unless killed. |

### Marksmanship (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |

### Survival (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 4/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 4%. |

## Core talents (priority order)

1. **Frenzy** — Removing it costs 10.0 points of score in this model.
2. **Careful Aim** — Removing it costs 7.4 points of score in this model.
3. **Unleashed Fury** — Removing it costs 6.7 points of score in this model.
4. **Efficiency** — Removing it costs 6.5 points of score in this model.
5. **Lethal Attacks** — Removing it costs 6.4 points of score in this model.
6. **Deadly Aspects** — Removing it costs 5.9 points of score in this model.
7. **Bestial Discipline** — Removing it costs 5.8 points of score in this model.
8. **Ferocity** — Removing it costs 5.4 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 12** for `mm-raid` by training-dummy DPS in the community simulator (wowsims/forever 7c3453f (client 70755)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md)** | ours: optimizer | 31/16/4 | 530 | +0.0% | 937 | -7.0% | 38 s |
| 2 | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) | ours: derived (ML search) | 7/39/5 | 501 | -5.4% | 1004 | -0.4% | 46 s |
| 3 | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) | ours: hand draft | 21/30/0 | 499 | -5.9% | 916 | -9.2% | 32 s |
| 4 | [`marksmanship-with-a-pet-open-raid`](marksmanship-with-a-pet-open-raid.md) | ours: derived (open search) | 7/39/5 | 492 | -7.2% | 1008 | +0.0% | 54 s |
| 5 | *BM Weave* | community simulator | - | 489 | -7.8% | 956 | -5.1% | 46 s |
| 6 | *BM* | community simulator | - | 477 | -10.1% | 982 | -2.6% | 52 s |
| 7 | *MM* | community simulator | - | 471 | -11.1% | 969 | -3.9% | 50 s |
| 8 | [`bm-mm-raid`](bm-mm-raid.md) | ours: hand draft | 22/29/0 | 461 | -13.0% | 906 | -10.1% | 26 s |
| 9 | *SV* | community simulator | - | 434 | -18.2% | 838 | -16.9% | 47 s |
| 10 | *SV Weave* | community simulator | - | 429 | -19.0% | 827 | -18.0% | 47 s |
| 11 | *MM Weave* | community simulator | - | 415 | -21.8% | 834 | -17.2% | 53 s |
| 12 | *SV Melee* | community simulator | - | 388 | -26.8% | 814 | -19.2% | 51 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 10 passes, the last 2026-10-09, 12 changes to the base rotation; third-seed check: open winner 418 -> 452 DPS (+8.1%), bm-mm-full-buffs-raid 439 -> 473 DPS (+7.7%), sim preset: Marksmanship 417 -> 454 DPS (+8.9%), bm-mm-raid 443 -> 461 DPS (+3.9%)):
  1. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.3%, pass 1)
  2. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+1.7%, pass 1)
  3. threshold 0.5s -> 1s: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.6%, pass 1)
  4. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  5. only with 20s or more of the fight left: if time to the next auto attack > 1s: cast Aimed Shot (+0.2%, pass 2)
  6. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+6.4%, pass 5)
  7. only with 10s or more of the fight left: if auraIsInactive: cast Summon Hawk (+0.3%, pass 6)
  8. only above 25% mana: if time to the next auto attack > 1s and time left in the fight ≥ 20s: cast Aimed Shot (+0.3%, pass 6)
  9. threshold 25% -> 20%: if time to the next auto attack > 1s and time left in the fight ≥ 20s and mana % ≥ 25%: cast Aimed Shot (+0.2%, pass 9)
  10. threshold 10s -> 15s: if auraIsInactive and time left in the fight ≥ 10s: cast Summon Hawk + only above 10% mana: if time to the next auto attack > 1s: cast Multi-Shot (+0.2%, pass 9)
  11. insert in the middle: cast Intimidation + only above 60% mana: cast Intimidation (+0.3%, pass 9)
  12. threshold 20% -> 15%: if time to the next auto attack > 1s and time left in the fight ≥ 20s and mana % ≥ 20%: cast Aimed Shot (+0.2%, pass 10)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 16 passes, the last 2026-11-04, 16 changes to the base rotation; third-seed check: marksmanship-ml-raid 925 -> 1004 DPS (+8.6%), sim preset: BM 936 -> 981 DPS (+4.8%), bm-mm-raid 890 -> 905 DPS (+1.7%), bm-mm-full-buffs-raid 903 -> 916 DPS (+1.4%), opt-mm-raid-raid-dps 924 -> 937 DPS (+1.4%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.0%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  3. only with 6s or more of the fight left: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+0.2%, pass 1)
  4. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+1.3%, pass 5)
  5. insert in the middle: if time to the next auto attack > 1s: cast Aimed Shot (+0.8%, pass 6)
  6. only with 10s or more of the fight left: if auraIsInactive: cast Summon Hawk (+0.3%, pass 6)
  7. threshold 1s -> 0.5s: if time to the next auto attack > 1s: cast Aimed Shot (+0.3%, pass 6)
  8. insert before the filler: cast Intimidation (+0.2%, pass 6)
  9. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30% and time left in the fight ≥ 6s: cast Serpent Sting (+0.2%, pass 8)
  10. move to the top: cast Arcane Shot (+3.0%, pass 9)
  11. threshold 1 -> 3: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.7%, pass 12)
  12. move to the top: if time to the next auto attack > 0.5s: cast Aimed Shot (+0.5%, pass 12)
  13. drop 'time to the next auto attack > 1s' from the condition: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 3 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.5%, pass 12)
  14. insert at the end: cast Major Mana Potion (+0.2%, pass 13)
  15. threshold 1s -> 0.75s: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and time left in the fight ≥ 6s: cast Serpent Sting (+0.2%, pass 15)
  16. threshold 3 -> 2.25: if time until Aimed Shot is ready ≥ 3 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.2%, pass 16)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | cast Arcane Shot | 8.5 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if mana % ≥ 60%: cast Intimidation | 0.3 |
| 4 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 5 | if time to the next auto attack > 1s and time left in the fight ≥ 20s and mana % ≥ 15%: cast Aimed Shot | 3.9 |
| 6 | if time to the next auto attack > 1s and mana % ≥ 10%: cast Multi-Shot | 0.5 |
| 7 | if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.4 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent).

Damage by ability:

| Ability | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) |
|---|---|
| Pet: Auto Attack | 32% |
| Auto Shot | 31% |
| Arcane Shot | 17% |
| Serpent Sting | 9% |
| Aimed Shot | 7% |
| Pet: Bite | 2% |
| Pet: Claw | 2% |
| Multi-Shot | 1% |
| spell 1295633 | 0% |

## Notes

- Report: hunter/research/talents/forever/optimizer/mm-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
