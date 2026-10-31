# Optimizer — Marksmanship raid DPS with a pet (Classic 20/31/0 style) (raid-dps) — 31/16/4

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/16/4 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

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
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 15. |

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

**1 of 11** for `mm-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md)** | ours: optimizer | 31/16/4 | 417 | +0.0% | 731 | -6.4% | 36 s |
| 2 | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) | ours: hand draft | 21/30/0 | 395 | -5.2% | 715 | -8.5% | 27 s |
| 3 | *BM Weave* | community simulator | - | 395 | -5.2% | 744 | -4.7% | 41 s |
| 4 | *BM* | community simulator | - | 395 | -5.2% | 744 | -4.7% | 41 s |
| 5 | [`marksmanship-open-raid`](marksmanship-open-raid.md) | ours: derived (open search) | 7/39/5 | 389 | -6.7% | 781 | +0.0% | 49 s |
| 6 | *MM* | community simulator | - | 376 | -9.8% | 707 | -9.5% | 43 s |
| 7 | [`bm-mm-raid`](bm-mm-raid.md) | ours: hand draft | 22/29/0 | 376 | -9.8% | 714 | -8.6% | 21 s |
| 8 | *SV* | community simulator | - | 340 | -18.3% | 648 | -17.0% | 34 s |
| 9 | *SV Weave* | community simulator | - | 338 | -18.9% | 647 | -17.2% | 41 s |
| 10 | *MM Weave* | community simulator | - | 330 | -20.8% | 629 | -19.5% | 49 s |
| 11 | *SV Melee* | community simulator | - | 322 | -22.7% | 640 | -18.1% | 46 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 12 passes, the last 2026-10-22, 13 changes to the base rotation; third-seed check: marksmanship-with-a-pet-open-raid 729 -> 780 DPS (+7.0%), sim preset: Marksmanship 708 -> 757 DPS (+6.9%), bm-mm-raid 699 -> 714 DPS (+2.1%), bm-mm-full-buffs-raid 705 -> 715 DPS (+1.5%), opt-mm-raid-raid-dps 725 -> 735 DPS (+1.4%)):
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

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | cast Arcane Shot | 8.8 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 4 | if time to the next auto attack > 1s and time left in the fight ≥ 20s and mana % ≥ 15%: cast Aimed Shot | 3.7 |
| 5 | if time to the next auto attack > 1s and mana % ≥ 10%: cast Multi-Shot | 0.8 |
| 6 | if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.6 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Intimidation (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) |
|---|---|
| Auto Shot | 33% |
| Pet: Auto Attack | 30% |
| Arcane Shot | 16% |
| Serpent Sting | 8% |
| Aimed Shot | 6% |
| Pet: Bite | 2% |
| Pet: Claw | 2% |
| Multi-Shot | 1% |
| spell 1295633 | 1% |

## Notes

- Report: hunter/research/talents/forever/optimizer/mm-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
