# Optimizer — Raid tank in Defensive Stance with a shield: threat sources are Heroic Strike, Sunder Armor, Revenge, white swings, Thunder Clap; Shield Slam arrives as a talent effect (raid-tank) — 14/5/32

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/5/32 (Arms / Fury / Protection) |
| **Role** | TANK — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `prot-tank` and profile `raid-tank`: score +58.5% (tank score: 0.5 x threat gain + 0.5 x mitigation gain + 0.1 x mana gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arms (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | unchanged | Increases your Parry chance by 5%. |
| **Improved Heroic Strike** | 3/3 | changed | Reduces the cost of your Heroic Strike ability by 3 Rage. |
| **Improved Tactical Mastery** | 5/5 | **NEW** | Tactical Mastery lets you retain up to an additional 15 Rage when you change stances. |
| **Anger Management** | 1/1 | changed | Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. |

### Fury (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |

### Protection (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Anticipation** | 5/5 | changed | Increases your Defense Skill by 20. |
| **Shield Specialization** | 5/5 | changed | Increases your chance to Block attacks with your shield by 5% and grants you a 100% chance to generate 5 Rage when you Block. |
| **Improved Thunder Clap** | 3/3 | changed | Reduces the Rage cost of your Thunder Clap ability by 6. |
| **Defiance** | 3/3 | changed | Increases all threat generated in Defensive stance by an additional 15% while a shield is equipped. |
| **Improved Revenge** | 3/3 | changed | Increases damage dealt by your Revenge ability by 60%. |
| **Master of Defense** | 2/2 | **NEW** | Grants you a 100% chance to generate 5 Rage when you Dodge or Parry while a shield is equipped. |
| **Vanguard** | 1/1 | **NEW** | Your Charge ability is now usable while in Defensive Stance. |
| **Concussion Blow** | 1/1 | changed | Stuns the target for 5 sec. |
| **Bastion** | 5/5 | **NEW** | Increases all damage you deal by 10% while a shield is equipped. |
| **Focused Rage** | 3/3 | **NEW** | Reduces the Rage cost of your offensive abilities by 3. |
| **Shield Slam** | 1/1 | changed | Slam the target with your shield, causing 421 to 439 damage, increased by your Block Value, and has a 50% chance of dispelling 1 magic effect on the target. Causes a very high amount of threat. |

## Core talents (priority order)

1. **Shield Slam** — Removing it costs 22.7 points of score in this model.
2. **Defiance** — Removing it costs 11.0 points of score in this model.
3. **Deflection** — Removing it costs 5.9 points of score in this model.
4. **Bastion** — Removing it costs 5.4 points of score in this model.
5. **Improved Revenge** — Removing it costs 4.5 points of score in this model.
6. **Focused Rage** — Removing it costs 4.0 points of score in this model.
7. **Anticipation** — Removing it costs 3.0 points of score in this model.
8. **Improved Thunder Clap** — Removing it costs 2.9 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 4** for `prot-tank` by tank value in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |
|---|---|---|---|---|---|---|---|
| 1 | [`prot-raid-tank`](prot-raid-tank.md) | ours: hand draft | 14/5/32 | 1.000 | +0.0% | 650 | 1164 |
| 2 | **[`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md)** | ours: optimizer | 14/5/32 | 1.000 | +0.0% | 650 | 1164 |
| 3 | *Protection* | community simulator | - | 0.952 | -4.8% | 615 | 1217 |
| 4 | *Protection 1/0/50* | community simulator | - | 0.941 | -5.9% | 608 | 1229 |

## Rotation (community simulator, raid setting)

- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 3 changes to the base rotation; third-seed check: prot-raid-tank 416 -> 426 DPS (+2.4%), sim preset: Protection 394 -> 404 DPS (+2.5%)):
  1. move down below 'cast Revenge': cast Shield Slam (+0.2%, pass 1)
  2. insert at the top: cast Shield Wall (+3.2%, pass 3)
  3. insert before the filler: if not Rend is on the target: cast Rend (+0.5%, pass 3)

Before the pull: at -1s: cast Battle Shout.

| # | Priority (the first line whose condition holds is cast) | [`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md) casts/min |
|---|---|---|
| 1 | cast Shield Wall | 0.3 |
| 2 | use every other cooldown when ready | as ready |
| 3 | cast Revenge | 6.1 |
| 4 | cast Shield Slam | 9.9 |
| 5 | cast Thunder Clap | 9.7 |
| 6 | if rage ≥ 45: cast Heroic Strike | 8.2 |
| 7 | if not Rend is on the target: cast Rend | 2.9 |

Lines of the simulator's rotation these builds never cast: cast Defensive Stance, cast Sunder Armor (its condition never held in these fights).

Damage by ability (threat for tanks):

| Ability | [`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md) |
|---|---|
| Shield Slam | 33% |
| Auto Attack | 23% |
| Heroic Strike | 16% |
| Revenge | 14% |
| Thunder Clap | 7% |
| Rend | 2% |
| Retribution Aura | 1% |
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
