# Beast Mastery — Full raid (parse) (machine-learning search) — 31/20/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/20/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast Mastery build the machine-learning talent search found in a full raid (every raid buff and debuff) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry bm-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

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
| **Efficiency** | 2/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 6%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |

### Survival (0)

*No points.*

## Rank among our builds and the community simulator's

**2 of 6** for `bm-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`beast-marks-open-raid`](beast-marks-open-raid.md) | ours: hand draft | 27/19/5 | 464 | +0.0% | 842 | +0.0% | 20 s |
| 2 | **[`beast-mastery-ml-parse`](beast-mastery-ml-parse.md)** | ours: parse build | 31/20/0 | 464 | -0.1% | 841 | -0.1% | 25 s |
| 3 | [`beast-mastery-raid`](beast-mastery-raid.md) | ours: hand draft | 30/21/0 | 461 | -0.7% | 810 | -3.9% | 6 s |
| 4 | [`beast-marks-ml-raid`](beast-marks-ml-raid.md) | ours: hand draft | 28/23/0 | 454 | -2.2% | 833 | -1.2% | 18 s |
| 5 | [`mm-hawk-raid`](mm-hawk-raid.md) | ours: hand draft | 22/29/0 | 446 | -4.0% | 805 | -4.5% | 13 s |
| 6 | *Beast Mastery 35/16/0* | community simulator | - | 439 | -5.4% | 790 | -6.3% | 14 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 10 passes, the last 2026-10-09, 15 changes to the base rotation; third-seed check: open winner 427 -> 473 DPS (+10.7%), beast-marks-open-raid 450 -> 490 DPS (+8.9%), sim preset: Beast Mastery 35/16/0 437 -> 463 DPS (+5.9%), mm-hawk-raid 438 -> 475 DPS (+8.5%), beast-mastery-raid 449 -> 487 DPS (+8.6%), beast-marks-ml-raid 443 -> 480 DPS (+8.3%)):
  1. drop: use every other cooldown when ready (+3.0%, pass 1)
  2. drop: if time to the next auto attack > 1s: cast Aimed Shot (+0.5%, pass 1)
  3. drop: if time to the next auto attack > 0.5s: cast Multi-Shot (+2.1%, pass 1)
  4. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and mana % ≥ 30%: cast Serpent Sting (+2.8%, pass 1)
  5. drop the condition: if time to the next auto attack > 1s: cast Summon Hawk (+0.8%, pass 1)
  6. move down below 'cast Summon Hawk': if time left on Serpent Sting < 1s: cast Serpent Sting (+0.9%, pass 1)
  7. insert before the filler: use every other cooldown when ready (+3.8%, pass 2)
  8. threshold 1s -> 2s: if time left on Serpent Sting < 1s: cast Serpent Sting (+0.4%, pass 2)
  9. threshold 2s -> 4s: if time left on Serpent Sting < 2s: cast Serpent Sting (+1.3%, pass 2)
  10. spell probe: insert at the end: if auraIsInactive: cast Intimidation (+0.5%, pass 5)
  11. only above 60% mana: if auraIsInactive: cast Intimidation (+0.2%, pass 7)
  12. threshold 60% -> 70%: if auraIsInactive and mana % ≥ 60%: cast Intimidation (+0.3%, pass 8)
  13. insert at the top: if time to the next auto attack > 0.5s and mana % ≥ 30%: cast Arcane Shot (+19.8%, pass 10)
  14. threshold 30% -> 10%: if time to the next auto attack > 0.5s and mana % ≥ 30%: cast Arcane Shot (+2.9%, pass 10)
  15. only with 3s or more of the fight left: if time left on Serpent Sting < 4s: cast Serpent Sting (+0.4%, pass 10)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 11 passes, the last 2026-10-09, 12 changes to the base rotation; third-seed check: open winner 718 -> 854 DPS (+18.9%), beast-marks-open-raid 805 -> 843 DPS (+4.7%), sim preset: Beast Mastery 35/16/0 761 -> 789 DPS (+3.7%), mm-hawk-raid 766 -> 807 DPS (+5.4%), beast-mastery-raid 776 -> 810 DPS (+4.5%), beast-mastery-ml-parse 805 -> 843 DPS (+4.6%), beast-marks-ml-raid 796 -> 833 DPS (+4.6%)):
  1. move to the top: if time to the next auto attack > 0.5s: cast Multi-Shot (+1.9%, pass 1)
  2. drop the condition: if time to the next auto attack > 1s: cast Summon Hawk (+0.4%, pass 1)
  3. threshold 1s -> 0.75s: if time left on Serpent Sting < 1s and mana % ≥ 30%: cast Serpent Sting (+0.2%, pass 2)
  4. threshold 0.75s -> 0.25s: if time left on Serpent Sting < 0.75s and mana % ≥ 30%: cast Serpent Sting + move to the top: if time left on Serpent Sting < 0.25s and mana % ≥ 30%: cast Serpent Sting (+0.3%, pass 3)
  5. drop: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.6%, pass 5)
  6. insert at the end: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.3%, pass 5)
  7. move down below 'cast Summon Hawk': if time to the next auto attack > 1s: cast Aimed Shot (+0.4%, pass 5)
  8. drop the condition: if time to the next auto attack > 1s: cast Aimed Shot (+0.2%, pass 5)
  9. insert at the top: if time to the next auto attack > 1s: cast Summon Hawk + insert in the middle: if time to the next auto attack > 0.5s and mana % ≥ 30%: cast Arcane Shot (+0.8%, pass 6)
  10. only with 10s or more of the fight left: if time to the next auto attack > 1s: cast Summon Hawk (+0.2%, pass 6)
  11. drop: if time to the next auto attack > 1s and time left in the fight ≥ 10s: cast Summon Hawk (+1.1%, pass 10)
  12. drop the condition: if time to the next auto attack > 0.5s and mana % ≥ 30%: cast Arcane Shot (+0.3%, pass 11)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`beast-mastery-ml-parse`](beast-mastery-ml-parse.md) casts/min |
|---|---|---|
| 1 | if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire | 0.3 |
| 2 | cast Summon Hawk | 9.7 |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left on Serpent Sting < 4s and time left in the fight ≥ 3s: cast Serpent Sting | 4.7 |
| 5 | if auraIsInactive and mana % ≥ 70%: cast Intimidation | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Arcane Shot (its condition never held in these fights).

Damage by ability:

| Ability | [`beast-mastery-ml-parse`](beast-mastery-ml-parse.md) |
|---|---|
| Auto Shot | 39% |
| Pet: Auto Attack | 21% |
| Serpent Sting | 19% |
| Summon Hawk | 14% |
| Pet: Claw | 7% |
| Pet: Bite | 0% |

## Notes

- In a full raid it does +3.2% over the training-dummy winner (812.2 vs 786.8 DPS, 100,000 fights, one seed, BiS gear).
- Search result: 31/20/0 at 812.0 ± 0.08 DPS over 100,000 fights; runner-up 31/20/0 (+0.21%; the winner takes Endurance Training 3, Frenzy 5; the runner-up Endurance Training 4, Frenzy 4); 1,723 builds simulated; certificate: 1 confirmed move first, then none of its 156 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.

## Open questions (verify in the live game)

- A machine-searched Beast Mastery build: check it against the community's Beast Mastery builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
