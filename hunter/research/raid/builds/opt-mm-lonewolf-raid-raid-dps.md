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

**3 of 9** for `mm-lonewolf-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`marksmanship-lone-wolf-sim-raid`](marksmanship-lone-wolf-sim-raid.md) | ours: derived (simulator preset) | 5/41/5 | 479 | +0.0% | 990 | -0.6% | 89 s |
| 2 | *MM* | community simulator | - | 479 | +0.0% | 990 | -0.6% | 89 s |
| 3 | **[`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md)** | ours: optimizer | 7/41/3 | 473 | -1.3% | 936 | -6.0% | 78 s |
| 4 | [`mm-lone-wolf-raid`](mm-lone-wolf-raid.md) | ours: hand draft | 5/41/5 | 472 | -1.4% | 996 | +0.0% | 93 s |
| 5 | *SV* | community simulator | - | 424 | -11.4% | 843 | -15.4% | 83 s |
| 6 | *SV Weave* | community simulator | - | 424 | -11.5% | 820 | -17.7% | 77 s |
| 7 | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) | ours: derived (ML search) | 7/39/5 | 387 | -19.1% | 826 | -17.1% | 96 s |
| 8 | *BM* | community simulator | - | 345 | -28.0% | 659 | -33.9% | 77 s |
| 9 | *SV Melee* | community simulator | - | 302 | -36.9% | 596 | -40.2% | 86 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/turret.apl.json`), untuned. The rotation search of 2026-09-27 to 2026-10-07 (9 changes, `mm-lonewolf-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/turret.apl.json`), untuned. The rotation search of 2026-09-27 to 2026-11-10 (14 changes, `mm-lonewolf-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: at -22s: cast Hunter's Mark; at -20s: cast Aspect of the Hawk; at -19s: move to “Pull range” yd; if “Use Sniper Shot”: cast Sniper Shot.

| # | Priority (the first line whose condition holds is cast) | [`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time into the fight ≥ 5s: use every other cooldown when ready | as ready |
| 2 | if not Hunter's Mark is on the target: cast Hunter's Mark | 0.7 |
| 3 | if not Serpent Sting is on the target: cast Serpent Sting | 2.3 |
| 4 | if “Use Arcane Shot” and not “Use Summon Hawk”: cast Arcane Shot | 7.4 |
| 5 | if “Use Aimed Shot”: cast Aimed Shot | 3.9 |
| 6 | if “Use Sniper Shot”: cast Sniper Shot | 2.0 |
| 7 | if unitDistance ≠ “Shoot spot” and not (Arcane Shot is in range and (“Windup close” or “Just shot”)): move to “Shoot spot” yd | as ready |
| 8 | if unitDistance ≠ “Shoot spot”: wait inputDelay | as ready |

Lines of the simulator's rotation these builds never cast: reset sequence 'HHA', sequence 'HHA': cast Summon Hawk; cast Summon Hawk; cast Arcane Shot, cast Summon Hawk, cast Multi-Shot (a switch this rotation keeps off).

Damage by ability:

| Ability | [`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md) |
|---|---|
| Auto Shot | 45% |
| Arcane Shot | 21% |
| Serpent Sting | 14% |
| Aimed Shot | 13% |
| Sniper Shot | 7% |

## Notes

- Allocation taken from cand-mm-lonewolf-raid-r1 on 2026-10-22: the optimizer's earlier round beat its last export in the community simulator (361 vs 358 DPS; the calibration moved the model past the better build).
- Report: hunter/research/talents/forever/optimizer/mm-lonewolf-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
