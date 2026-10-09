# Marksmanship — Summon Hawk (raid) — 22/29/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/29/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Our Marksmanship raid draft's tree split with Summon Hawk, a Forever Beast Mastery talent: every 6 seconds (a cooldown shared with Arcane Shot) a hawk dive-bombs the target and keeps attacking for 18 seconds, two hawks at a time, and Unleashed Fury and Ferocity buff hawks as they buff pets. Beast Mastery for the hawk, Unleashed Fury, Ferocity, Focused Fire and Deadly Aspects; Marksmanship for Lethal Attacks, Efficiency, Careful Aim, Mortal Shots, Ranged Weapon Specialization, Improved Stings and Trueshot Aura. Found by the simulator talent search from bm-mm-raid under the Beast Mastery entry's rotation (Summon Hawk on cooldown, Serpent Sting kept up, the cooldowns, Auto Shot between): its first move, one point into Summon Hawk, was worth +47% on the training dummy (2026-09-28). A deeper Beast Mastery version (31/20/0, from the simulator's Beast Mastery preset) lands 0.3% lower on the dummy and 1.6% lower in a raid. Its lead rests on the simulator's guess at the hawks' follow-up attacks (open questions).

## Point allocation

### Beast Mastery (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Bestial Discipline** | 1/2 | changed | Increases the Focus regeneration of your pets by 10% and allows 25% of your Mana regeneration to continue while casting. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |

### Marksmanship (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yds by 30. |
| **Ranged Weapon Specialization** | 4/5 | unchanged | Increases the damage you deal with ranged weapons by 4%. |
| **Hawk Eye** | 1/3 | moved | Increases the range of your ranged weapons by 2 yards. |

### Survival (0)

*No points.*

## Core talents (priority order)

1. **Summon Hawk** — The build's engine: a dive bomb every 6 s and hawks that keep attacking for 18 s. Simulator removal run (2026-09-28): the build loses 47.6% of its DPS on the training dummy without it.
2. **Unleashed Fury** — +15% pet and hawk damage. Simulator removal run (2026-09-28): the build loses 5.2% of its DPS on the training dummy without it.
3. **Deadly Aspects** — Auto Shot procs +30% ranged attack speed under Aspect of the Hawk. Simulator removal run (2026-09-28): the build loses 4.6% of its DPS on the training dummy without it.
4. **Lethal Attacks** — +5% crit on every attack. Simulator removal run (2026-09-28): the build loses 4.4% of its DPS on the training dummy without it.
5. **Improved Stings** — +20% Serpent Sting damage, and the rotation keeps Serpent Sting up. Simulator removal run (2026-09-28): the build loses 3.5% of its DPS on the training dummy without it.
6. **Ferocity** — +10% pet and hawk crit. Simulator removal run (2026-09-28): the build loses 3.3% of its DPS on the training dummy without it.
7. **Mortal Shots** — +30% ranged crit damage. Simulator removal run (2026-09-28): the build loses 3.1% of its DPS on the training dummy without it.
8. **Careful Aim** — Attack power from Intellect. Simulator removal run (2026-09-28): the build loses 2.6% of its DPS on the training dummy without it.
9. **Efficiency** — -15% mana on shots and stings: the training dummy runs a hunter dry. Simulator removal run (2026-09-28): the build loses 2.2% of its DPS on the training dummy without it.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 1 | Bestial Discipline | any talent legal at that tier | Worth 0.7% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 3 | Endurance Training | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 1 | Hawk Eye | Barrage, any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |

## Rank among our builds and the community simulator's

**5 of 6** for `bm-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`beast-marks-open-raid`](beast-marks-open-raid.md) | ours: hand draft | 27/19/5 | 464 | +0.0% | 842 | +0.0% | 20 s |
| 2 | [`beast-mastery-ml-parse`](beast-mastery-ml-parse.md) | ours: parse build | 31/20/0 | 464 | -0.1% | 841 | -0.1% | 25 s |
| 3 | [`beast-mastery-raid`](beast-mastery-raid.md) | ours: hand draft | 30/21/0 | 461 | -0.7% | 810 | -3.9% | 6 s |
| 4 | [`beast-marks-ml-raid`](beast-marks-ml-raid.md) | ours: hand draft | 28/23/0 | 454 | -2.2% | 833 | -1.2% | 18 s |
| 5 | **[`mm-hawk-raid`](mm-hawk-raid.md)** | ours: hand draft | 22/29/0 | 446 | -4.0% | 805 | -4.5% | 13 s |
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

| # | Priority (the first line whose condition holds is cast) | [`mm-hawk-raid`](mm-hawk-raid.md) casts/min |
|---|---|---|
| 1 | if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire | 0.3 |
| 2 | cast Summon Hawk | 10.0 |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left on Serpent Sting < 4s and time left in the fight ≥ 3s: cast Serpent Sting | 4.7 |

Lines of the simulator's rotation these builds never cast: cast Arcane Shot (its condition never held in these fights); cast Intimidation (needs the Intimidation talent).

Damage by ability:

| Ability | [`mm-hawk-raid`](mm-hawk-raid.md) |
|---|---|
| Auto Shot | 44% |
| Serpent Sting | 20% |
| Pet: Auto Attack | 16% |
| Summon Hawk | 15% |
| Pet: Claw | 6% |
| Pet: Bite | 0% |

## Notes

- Talents from the simulator talent search (raidsim/talent_opt.py, 2026-09-28) from `bm-mm-raid`: 1 point Improved Mend Pet -> Summon Hawk, 1 point Barrage -> Improved Stings, 1 point Improved Mend Pet -> Ferocity, 1 point Bestial Discipline -> Ferocity.
- New-builds survey (2026-09-28, user request): see _reference/new-builds-survey.md. A simulator-searched build: no scorer model covers it, so it is raced and ranked, not optimized or audited.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Barrage -> Hawk Eye (range). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- How hard do the hawks hit after the dive bomb? The client does not describe the hawk's swings; the simulator (and the fight lab, which follows it) assumes the dive bomb's base damage (108 at rank 4) every 3 s for 18 s, two hawks at once. Those follow-up attacks are 22% of this build's damage on the training dummy and 13% in a raid (2026-09-28): at half that, the build only matches the best builds without the hawk.
- Do Unleashed Fury, Ferocity and Focused Fire apply to hawks in the game? The first two tooltips name hawks; the simulator applies all three.
- Summon Hawk shares its cooldown with Arcane Shot: the rotation gives up Arcane Shot for it.

## Sources

- <https://github.com/ElliotWood/Forever/blob/master/ui/specs/hunter/dps/presets.ts>
- <https://github.com/ElliotWood/Forever/blob/master/sim/hunter/summon_hawk.go>
- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
