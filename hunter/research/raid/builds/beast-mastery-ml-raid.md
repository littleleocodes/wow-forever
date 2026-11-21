# Beast Mastery — Raid (machine-learning search) — 31/20/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/20/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast Mastery build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-16 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry bm-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Beast Mastery (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Bestial Swiftness** | 1/1 | changed | Increases the movement speed of your pets by 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Intimidation** | 1/1 | changed | Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 5/5 | unchanged | Gives your pet a 100% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |
| **Bestial Wrath** | 1/1 | unchanged | Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be stopped unless killed. |

### Marksmanship (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Arcane Shot** | 2/5 | changed | Reduces the cooldown of your Arcane Shot by 0.6 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |

### Survival (0)

*No points.*

## Rank among our builds and the community simulator's

**3 of 4** for `bm-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *BM* | community simulator | - | 491 | +0.0% | 940 | -0.6% | 82 s |
| 2 | [`mm-hawk-raid`](mm-hawk-raid.md) | ours: hand draft | 22/29/0 | 482 | -1.8% | 905 | -4.3% | 64 s |
| 3 | **[`beast-mastery-ml-raid`](beast-mastery-ml-raid.md)** | ours: derived (ML search) | 31/20/0 | 480 | -2.2% | 946 | +0.0% | 82 s |
| 4 | [`beast-marks-ml-raid`](beast-marks-ml-raid.md) | ours: derived (ML search) | 27/22/2 | 477 | -2.8% | 942 | -0.4% | 73 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/turret_hawk.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-10-09 (15 changes, `bm-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/turret_hawk.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-11-20 (15 changes, `bm-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: at -22s: cast Hunter's Mark; at -20s: cast Aspect of the Hawk (rank 6); at -19s: move to “Pull range” yd.

| # | Priority (the first line whose condition holds is cast) | [`beast-mastery-ml-raid`](beast-mastery-ml-raid.md) casts/min |
|---|---|---|
| 1 | if time into the fight ≥ 5s: use every other cooldown when ready | as ready |
| 2 | if not Hunter's Mark is on the target: cast Hunter's Mark | 0.7 |
| 3 | if not Serpent Sting is on the target: cast Serpent Sting (rank 8) | 2.4 |
| 4 | if “Use Summon Hawk” and “Use Arcane Shot” and the sequence is complete: reset sequence 'HHA' | as ready |
| 5 | if “Use Summon Hawk” and “Use Arcane Shot”: sequence 'HHA': cast Summon Hawk; cast Summon Hawk; cast Arcane Shot | 13.2 |
| 6 | if “Use Aimed Shot”: cast Aimed Shot | 4.0 |
| 7 | if unitDistance ≠ “Shoot spot” and not (Arcane Shot is in range and (“Windup close” or “Just shot”)): move to “Shoot spot” yd | as ready |
| 8 | if unitDistance ≠ “Shoot spot”: wait inputDelay | as ready |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk, cast Arcane Shot, cast Multi-Shot (a switch this rotation keeps off).

Damage by ability:

| Ability | [`beast-mastery-ml-raid`](beast-mastery-ml-raid.md) |
|---|---|
| Auto Shot | 34% |
| Pet: Auto Attack | 32% |
| Serpent Sting | 11% |
| Aimed Shot | 9% |
| Pet: Claw | 6% |
| Arcane Shot | 5% |
| Summon Hawk | 3% |
| Pet: Bite | 0% |

## Notes

- Search result (full raid): 31/20/0 at 841.9 ± 0.08 DPS over 100,000 fights; runner-up 31/20/0 (+0.00%; the winner takes Endurance Training 3, Spirit Bond 1; the runner-up Endurance Training 1, Improved Mend Pet 1, Improved Revive Pet 2); 1,770 builds simulated; certificate: none of its 164 one-move and chain-move neighbours was 0.1% ahead.
- Where the simulator measured no difference, the points follow beast-mastery-ml-parse: Spirit Bond → Frenzy (the same DPS as the search winner 31/20/0 on one seed, 30,000 fights).
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 31/20/0 at 803.7 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 31/17/3 at 487.8 DPS.

## Open questions (verify in the live game)

- A machine-searched Beast Mastery build: check it against the community's Beast Mastery builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
