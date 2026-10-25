# Optimizer — Raid tank in Defensive Stance with a shield: threat sources are Heroic Strike, Sunder Armor, Revenge, white swings, Thunder Clap; Shield Slam arrives as a talent effect (raid-tank) — 14/5/32

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/5/32 (Arms / Fury / Protection) |
| **Role** | TANK — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `prot-tank` and profile `raid-tank`: score +58.4% (tank score: 0.5 x threat gain + 0.5 x mitigation gain + 0.1 x mana gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arms (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | unchanged | Increases your Parry chance by 5%. |
| **Improved Heroic Strike** | 3/3 | changed | Reduces the cost of your Heroic Strike ability by 3 Rage. |
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |

### Fury (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |

### Protection (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shield Specialization** | 5/5 | changed | Increases your chance to Block attacks with your shield by 5% and grants you a 100% chance to generate 5 Rage when you Block. |
| **Improved Revenge** | 3/3 | changed | Increases damage dealt by your Revenge ability by 60%. |
| **Anticipation** | 5/5 | changed | Increases your Defense Skill by 20. |
| **Improved Thunder Clap** | 3/3 | changed | Reduces the Rage cost of your Thunder Clap ability by 6. |
| **Defiance** | 3/3 | changed | Increases all threat generated in Defensive stance by an additional 15% while a shield is equipped. |
| **Master of Defense** | 2/2 | **NEW** | Grants you a 100% chance to generate 5 Rage when you Dodge or Parry while a shield is equipped. |
| **Vanguard** | 1/1 | **NEW** | Your Charge ability is now usable while in Defensive Stance. |
| **Concussion Blow** | 1/1 | changed | Stuns the target for 5 sec. |
| **Focused Rage** | 3/3 | **NEW** | Reduces the Rage cost of your offensive abilities by 3. |
| **Bastion** | 5/5 | **NEW** | Increases all damage you deal by 10% while a shield is equipped. |
| **Shield Slam** | 1/1 | changed | Slam the target with your shield, causing 421 to 439 damage, increased by your Block Value, and has a 50% chance of dispelling 1 magic effect on the target. Causes a very high amount of threat. |

## Core talents (priority order)

1. **Shield Slam** — Removing it costs 22.7 points of score in this model.
2. **Defiance** — Removing it costs 10.9 points of score in this model.
3. **Deflection** — Removing it costs 5.9 points of score in this model.
4. **Bastion** — Removing it costs 5.4 points of score in this model.
5. **Improved Revenge** — Removing it costs 4.8 points of score in this model.
6. **Focused Rage** — Removing it costs 4.2 points of score in this model.
7. **Anticipation** — Removing it costs 3.0 points of score in this model.
8. **Shield Specialization** — Removing it costs 2.9 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 5** for `prot-tank` by tank value in the community simulator (ElliotWood/Forever fork 2ce8265 (client 70291)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |
|---|---|---|---|---|---|---|---|
| 1 | [`protection-ml-tank`](protection-ml-tank.md) | ours: derived (ML search) | 17/3/31 | 1.011 | +0.0% | 700 | 672 |
| 2 | **[`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md)** | ours: optimizer | 14/5/32 | 1.005 | -0.6% | 694 | 675 |
| 3 | [`prot-raid-tank`](prot-raid-tank.md) | ours: hand draft | 14/5/32 | 1.000 | -1.1% | 685 | 673 |
| 4 | *Protection* | community simulator | - | 0.948 | -6.3% | 646 | 706 |
| 5 | *Protection 1/0/50* | community simulator | - | 0.931 | -7.9% | 631 | 714 |

## Rotation (community simulator, raid setting)

- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 8 passes, the last 2026-10-15, 7 changes to the base rotation; third-seed check: deep: tank 485 -> 518 DPS (+6.8%), opt-prot-tank-raid-tank 493 -> 514 DPS (+4.1%), sim preset: Protection 455 -> 468 DPS (+2.9%), prot-raid-tank 486 -> 500 DPS (+2.9%)):
  1. move down below 'cast Revenge': cast Shield Slam (+0.2%, pass 1)
  2. insert at the top: cast Shield Wall (+3.2%, pass 3)
  3. insert before the filler: if not Rend is on the target: cast Rend (+0.5%, pass 3)
  4. drop: cast Thunder Clap (+0.8%, pass 4)
  5. insert before the filler: cast Shield Bash (+0.2%, pass 4)
  6. drop: cast Shield Bash (+0.4%, pass 7)
  7. insert in the middle: if rage < 90: cast Bloodrage + threshold 45 -> 33.75: if rage ≥ 45: cast Heroic Strike (+0.2%, pass 7)

Before the pull: at -1s: cast Battle Shout.

| # | Priority (the first line whose condition holds is cast) | [`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md) casts/min |
|---|---|---|
| 1 | cast Shield Wall | 0.3 |
| 2 | use every other cooldown when ready | as ready |
| 3 | cast Revenge | 6.3 |
| 4 | if rage < 90: cast Bloodrage | 1.0 |
| 5 | cast Shield Slam | 9.9 |
| 6 | if rage ≥ 33.75: cast Heroic Strike | 20.2 |
| 7 | if not Rend is on the target: cast Rend | 3.1 |

Lines of the simulator's rotation these builds never cast: cast Defensive Stance, cast Sunder Armor (its condition never held in these fights).

Damage by ability (threat for tanks):

| Ability | [`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md) |
|---|---|
| Heroic Strike | 35% |
| Shield Slam | 29% |
| Revenge | 15% |
| Auto Attack | 10% |
| Rend | 4% |
| Retribution Aura | 2% |
| Deep Wound | 2% |
| Thorns | 1% |
| OtherActionRageGain | 1% |
| Dragonbreath Chili | 0% |

## Notes

- Report: warrior/research/talents/forever/optimizer/prot-tank-raid-tank.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
