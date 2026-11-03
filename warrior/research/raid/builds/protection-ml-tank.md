# Protection — Raid tank (machine-learning search) — 17/3/31

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/3/31 (Arms / Fury / Protection) |
| **Role** | TANK — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Protection tank build the machine-learning talent search found in the community simulator on 2026-10-28 (raidsim/deep_tank.py: a random forest guiding a genetic search over every legal build of the spec, scored on tank value: threat per second and damage taken under boss melee; the rotation tuned with it; races on fresh seeds; every build one or two moves from the winner checked). The simulator's model of the beta, not an in-game measurement.

## Point allocation

### Arms (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Heroic Strike** | 3/3 | changed | Reduces the cost of your Heroic Strike ability by 3 Rage. |
| **Deflection** | 5/5 | unchanged | Increases your Parry chance by 5%. |
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Improved Overpower** | 1/2 | moved | Increases the critical strike chance of your Overpower ability by 25%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |
| **Impale** | 2/2 | changed | Increases the critical strike damage bonus of your abilities by 20%. |

### Fury (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 3/5 | changed | Improves your chance to get a critical strike with melee attacks by 3%. |

### Protection (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shield Specialization** | 5/5 | changed | Increases your chance to Block attacks with your shield by 5% and grants you a 100% chance to generate 5 Rage when you Block. |
| **Anticipation** | 5/5 | changed | Increases your Defense Skill by 20. |
| **Improved Revenge** | 3/3 | changed | Increases damage dealt by your Revenge ability by 60%. |
| **Master of Defense** | 2/2 | **NEW** | Grants you a 100% chance to generate 5 Rage when you Dodge or Parry while a shield is equipped. |
| **Defiance** | 3/3 | changed | Increases all threat generated in Defensive stance by an additional 20% while a shield is equipped. |
| **Improved Sunder Armor** | 3/3 | changed | Reduces the Rage cost of your Sunder Armor ability by 3. |
| **Concussion Blow** | 1/1 | changed | Stuns the target for 5 sec. |
| **Focused Rage** | 3/3 | **NEW** | Reduces the Rage cost of your offensive abilities by 3. |
| **Bastion** | 5/5 | **NEW** | Increases all damage you deal by 10% while a shield is equipped. |
| **Shield Slam** | 1/1 | changed | Slam the target with your shield, causing 421 to 439 damage, increased by your Block Value, and has a 50% chance of dispelling 1 magic effect on the target. Causes a very high amount of threat. |

## Rank among our builds and the community simulator's

**1 of 4** for `prot-tank` by tank value in the community simulator (wowsims/forever bac92db (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |
|---|---|---|---|---|---|---|---|
| 1 | **[`protection-ml-tank`](protection-ml-tank.md)** | ours: derived (ML search) | 17/3/31 | 1.016 | +0.0% | 1115 | 277 |
| 2 | *Protection* | community simulator | - | 1.009 | -0.7% | 1094 | 276 |
| 3 | [`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md) | ours: optimizer | 8/5/38 | 1.005 | -1.0% | 1087 | 276 |
| 4 | [`prot-raid-tank`](prot-raid-tank.md) | ours: hand draft | 14/5/32 | 1.000 | -1.6% | 1075 | 276 |

## Rotation (community simulator, raid setting)

- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-28, 9 changes to the base rotation; third-seed check: deep: tank 489 -> 523 DPS (+6.9%), protection-ml-tank 488 -> 521 DPS (+6.7%), sim preset: Protection 486 -> 512 DPS (+5.3%), prot-raid-tank 483 -> 498 DPS (+3.0%), opt-prot-tank-raid-tank 476 -> 503 DPS (+5.8%)):
  1. move down below 'cast Revenge': cast Shield Slam (+0.2%, pass 1)
  2. insert at the top: cast Shield Wall (+3.2%, pass 3)
  3. insert before the filler: if not Rend is on the target: cast Rend (+0.5%, pass 3)
  4. drop: cast Thunder Clap (+0.8%, pass 4)
  5. insert before the filler: cast Shield Bash (+0.2%, pass 4)
  6. drop: cast Shield Bash (+0.4%, pass 7)
  7. insert in the middle: if rage < 90: cast Bloodrage + threshold 45 -> 33.75: if rage ≥ 45: cast Heroic Strike (+0.2%, pass 7)
  8. insert at the top: if (rage ≥ 40 or auraIsInactive and time until Revenge is ready ≤ 1.5s): cast Shield Block (+8.4%, pass 9)
  9. drop the condition: if (rage ≥ 40 or auraIsInactive and time until Revenge is ready ≤ 1.5s): cast Shield Block (+2.2%, pass 9)

Before the pull: at -1s: cast Battle Shout.

| # | Priority (the first line whose condition holds is cast) | [`protection-ml-tank`](protection-ml-tank.md) casts/min |
|---|---|---|
| 1 | cast Shield Block | 11.8 |
| 2 | cast Shield Wall | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | cast Revenge | 10.9 |
| 5 | if rage < 90: cast Bloodrage | 1.0 |
| 6 | cast Shield Slam | 8.7 |
| 7 | if stacks of Sunder Armor < 5: cast Sunder Armor | 14.9 |
| 8 | if rage ≥ 33.75: cast Heroic Strike | 14.2 |
| 9 | if not Rend is on the target: cast Rend | 3.0 |
| 10 | cast Sunder Armor | 14.9 |

Lines of the simulator's rotation these builds never cast: cast Defensive Stance (its condition never held in these fights).

Damage by ability (threat for tanks):

| Ability | [`protection-ml-tank`](protection-ml-tank.md) |
|---|---|
| Revenge | 40% |
| Heroic Strike | 19% |
| Shield Slam | 13% |
| Auto Attack | 12% |
| Sunder Armor | 8% |
| Rend | 3% |
| Judgement of Light | 2% |
| OtherActionRageGain | 1% |
| Deep Wound | 1% |
| Retribution Aura | 1% |

## Notes

- Final race over 100,000 fights: tank value 1.129 ± 0.000 (relative to prot-raid-tank over 20,000 fights); protection-ml-tank 1.126, opt-prot-tank-raid-tank 1.115, prot-raid-tank 1.109.
- Independent runs agreeing in the last cycle: 3/3; two-move check: 193 one-move and 17,130 two-move builds, none better.

## Open questions (verify in the live game)

- A machine-searched Protection tank build: check its threat and survival against the community's tank builds at launch (the simulator models no threat from other players, taunts or tank swaps).

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
