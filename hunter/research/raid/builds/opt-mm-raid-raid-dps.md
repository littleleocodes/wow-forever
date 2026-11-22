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

**1 of 9** for `mm-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md)** | ours: optimizer | 31/16/4 | 495 | +0.0% | 866 | -11.8% | 63 s |
| 2 | [`bm-mm-raid`](bm-mm-raid.md) | ours: hand draft | 22/29/0 | 489 | -1.4% | 905 | -7.8% | 58 s |
| 3 | *BM* | community simulator | - | 482 | -2.6% | 939 | -4.3% | 86 s |
| 4 | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) | ours: hand draft | 21/30/0 | 480 | -3.1% | 873 | -11.1% | 64 s |
| 5 | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) | ours: derived (ML search) | 7/39/5 | 472 | -4.8% | 981 | +0.0% | 96 s |
| 6 | *MM* | community simulator | - | 463 | -6.6% | 938 | -4.4% | 89 s |
| 7 | *SV Weave* | community simulator | - | 418 | -15.6% | 796 | -18.9% | 77 s |
| 8 | *SV* | community simulator | - | 418 | -15.7% | 813 | -17.1% | 83 s |
| 9 | *SV Melee* | community simulator | - | 396 | -20.1% | 792 | -19.3% | 86 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/turret.apl.json`), untuned. The rotation search of 2026-09-27 to 2026-10-09 (12 changes, `mm-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 19 passes, the last 2026-11-20, 22 changes to the base rotation; third-seed check: marksmanship-ml-raid 973 -> 981 DPS (+0.8%), sim preset: BM 899 -> 939 DPS (+4.5%), bm-mm-raid 863 -> 906 DPS (+5.0%), bm-mm-full-buffs-raid 872 -> 872 DPS (-0.0%), opt-mm-raid-raid-dps 865 -> 865 DPS (+0.0%)):
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
  17. drop: cast Major Mana Potion (+1.6%, pass 17)
  18. drop the condition: if “Use Summon Hawk” and not “Use Arcane Shot”: cast Summon Hawk (+0.9%, pass 18)
  19. only above 60% mana: cast Summon Hawk (+0.4%, pass 18)
  20. drop the condition: if “Use Summon Hawk” and “Use Arcane Shot”: sequence 'HHA': cast Summon Hawk; cast Summon Hawk; cast Arcane Shot (+0.2%, pass 18)
  21. drop '“Use Summon Hawk” and “Use Arcane Shot”' from the condition: if “Use Summon Hawk” and “Use Arcane Shot” and the sequence is complete: reset sequence 'HHA' (+1.0%, pass 18)
  22. insert at the end: cast Major Mana Potion (+0.4%, pass 18)

Before the pull: at -22s: cast Hunter's Mark; at -20s: cast Aspect of the Hawk; at -19s: move to “Pull range” yd; if “Use Sniper Shot”: cast Sniper Shot.

| # | Priority (the first line whose condition holds is cast) | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time into the fight ≥ 5s: use every other cooldown when ready | as ready |
| 2 | if not Hunter's Mark is on the target: cast Hunter's Mark | 0.7 |
| 3 | if not Serpent Sting is on the target: cast Serpent Sting | 2.9 |
| 4 | if “Use Arcane Shot” and not “Use Summon Hawk”: cast Arcane Shot | 8.5 |
| 5 | if “Use Aimed Shot”: cast Aimed Shot | 4.8 |
| 6 | if unitDistance ≠ “Shoot spot” and not (Arcane Shot is in range and (“Windup close” or “Just shot”)): move to “Shoot spot” yd | as ready |
| 7 | if unitDistance ≠ “Shoot spot”: wait inputDelay | as ready |

Lines of the simulator's rotation these builds never cast: reset sequence 'HHA', sequence 'HHA': cast Summon Hawk; cast Summon Hawk; cast Arcane Shot, cast Summon Hawk, cast Multi-Shot (a switch this rotation keeps off); cast Sniper Shot (needs the Sniper Shot talent).

Damage by ability:

| Ability | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) |
|---|---|
| Auto Shot | 34% |
| Pet: Auto Attack | 21% |
| Arcane Shot | 18% |
| Aimed Shot | 10% |
| Serpent Sting | 10% |
| Pet: Claw | 6% |
| Pet: Bite | 0% |

## Notes

- Report: hunter/research/talents/forever/optimizer/mm-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
