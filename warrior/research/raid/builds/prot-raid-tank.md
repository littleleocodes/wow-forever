# Protection — Raid Tank (simulator winner adopted 2026-09-27) — 14/5/32

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/5/32 (Arms / Fury / Protection) |
| **Role** | TANK — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `prot-raid-tank` |

## Summary

Allocation adopted on 2026-09-27 from `opt-prot-tank-raid-tank`, the best build in the community simulator (+8.2% tank value vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Allocation adopted on 2026-09-26 from `opt-prot-tank-raid-tank`, the best build in the community simulator (+9.7% tank value vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: One-Handed Weapon Specialization, Improved Shield Block and Improved Taunt are gone, but Protection gained Bastion (+10% damage with a shield), Vitality (+10% Stamina/Strength), Master of Defense (rage on dodge/parry) and Vanguard (Charge in Defensive Stance). With Vanguard removing the reason to stance dance, the Classic Arms points (Tactical Mastery / Anger Management) are dropped and Protection is taken to 41.

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

1. **Shield Slam** — Raid sim (2026-09-27): removing it costs +15% tank value.
2. **Defiance** — Raid sim (2026-09-27): removing it costs +7% tank value.
3. **Deflection** — Raid sim (2026-09-26): removing it costs +4% tank value. Raid sim (2026-09-27): removing it costs +4% tank value.
4. **Bastion** — Raid sim (2026-09-27): removing it costs +4% tank value.
5. **Focused Rage** — Raid sim (2026-09-26): removing it costs +5% tank value. Raid sim (2026-09-27): removing it costs +3% tank value.
6. **Anticipation** — +4 Defense per rank (est. 20). Raid sim (2026-09-26): removing it costs +2% tank value. Raid sim (2026-09-27): removing it costs +2% tank value.
7. **Improved Thunder Clap** — Raid sim (2026-09-26): removing it costs +4% tank value. Raid sim (2026-09-27): removing it costs +2% tank value.
8. **Improved Revenge** — Raid sim (2026-09-26): removing it costs +3% tank value. Raid sim (2026-09-27): removing it costs +2% tank value.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Master of Defense | any utility talent legal at that tier | Measures +0.7% DPS in the community simulator (noise): these points are free to move. |
| 3 | Improved Heroic Strike | any utility talent legal at that tier | Measures +0.6% DPS in the community simulator (noise): these points are free to move. |
| 5 | Improved Tactical Mastery | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 1 | Vanguard | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 1 | Concussion Blow | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**1 of 4** for `prot-tank` by tank value in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |
|---|---|---|---|---|---|---|---|
| 1 | **[`prot-raid-tank`](prot-raid-tank.md)** | ours: hand draft | 14/5/32 | 1.000 | +0.0% | 650 | 1164 |
| 2 | [`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md) | ours: optimizer | 14/5/32 | 1.000 | +0.0% | 650 | 1164 |
| 3 | *Protection* | community simulator | - | 0.952 | -4.8% | 615 | 1217 |
| 4 | *Protection 1/0/50* | community simulator | - | 0.941 | -5.9% | 608 | 1229 |

## Rotation (community simulator, raid setting)

- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 3 changes to the base rotation; third-seed check: prot-raid-tank 416 -> 426 DPS (+2.4%), sim preset: Protection 394 -> 404 DPS (+2.5%)):
  1. move down below 'cast Revenge': cast Shield Slam (+0.2%, pass 1)
  2. insert at the top: cast Shield Wall (+3.2%, pass 3)
  3. insert before the filler: if not Rend is on the target: cast Rend (+0.5%, pass 3)

Before the pull: at -1s: cast Battle Shout.

| # | Priority (the first line whose condition holds is cast) | [`prot-raid-tank`](prot-raid-tank.md) casts/min |
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

| Ability | [`prot-raid-tank`](prot-raid-tank.md) |
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

- Adopted from the community simulator on 2026-09-27: opt-prot-tank-raid-tank beat the previous draft by +8.2% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Adopted from the community simulator on 2026-09-26: opt-prot-tank-raid-tank beat the previous draft by +9.7% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Improved Shield Block is gone: check whether Shield Block itself gained the extra charge baseline.
- Improved Thunder Clap moved into Protection (tier 2) — a dungeon/AoE tank can take it over Improved Bloodrage's partner Toughness.
- Beta client 1.60.1.69893 removed Vitality (5 points): re-spent as Focused Rage 3 (-3 Rage on offensive abilities) and Improved Revenge 2.

## Open questions (verify in the live game)

- Is Bastion's +10% damage worth more threat than Anger Management + Improved Tactical Mastery (the Classic Arms dip)?
- Does Shield Block still block an extra attack without Improved Shield Block?
- Vitality max rank (only rank 1 seen).

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
