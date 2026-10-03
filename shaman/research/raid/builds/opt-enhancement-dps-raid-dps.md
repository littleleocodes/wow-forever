# Optimizer — One slow weapon: white 40%, Windfury extra attacks 20%, Earth Shock 12%, Lightning Bolt 8%, Flame Shock 5%, Lightning Shield 5%, Rockbiter/other 10%; Stormstrike via talent (raid-dps) — 11/31/9

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/31/9 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `enhancement-dps` and profile `raid-dps`: score +123.8% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Elemental (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%. |
| **Elemental Devastation** | 2/3 | changed | Your offensive spell critical strikes will increase your chance to get a critical strike with melee attacks by 6% for 10 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |

### Enhancement (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Elemental Weapons** | 3/3 | moved | Increases the melee attack power bonus of your Rockbiter Weapon by 20%, your Windfury Weapon effect by 40% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 15%. |
| **Stormstrike** | 1/1 | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Flurry** | 5/5 | changed | Increases your attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Maelstrom Weapon** | 5/5 | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 20%. Stacks up to 5 times. Lasts 30 sec. |
| **Rage of the Farseer** | 1/1 | **NEW** | Increases your attack speed by 30% for 25 sec. |

### Restoration (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |
| **Tidal Focus** | 4/5 | changed | Reduces the Mana cost of your healing spells by 4% and improves your chance to hit by 4%. |

## Core talents (priority order)

1. **Stormstrike** — Removing it costs 41.3 points of score in this model.
2. **Maelstrom Weapon** — Removing it costs 27.8 points of score in this model.
3. **Shamanistic Focus** — Removing it costs 19.6 points of score in this model.
4. **Flurry** — Removing it costs 16.8 points of score in this model.
5. **Mental Dexterity** — Removing it costs 11.8 points of score in this model.
6. **Thundering Strikes** — Removing it costs 10.4 points of score in this model.
7. **Convection** — Removing it costs 7.6 points of score in this model.
8. **Mental Quickness** — Removing it costs 6.0 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 6** for `enhancement-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md)** | ours: optimizer | 11/31/9 | 413 | +0.0% | 755 | -5.6% | 14 s |
| 2 | [`enhancement-ml-raid`](enhancement-ml-raid.md) | ours: hand draft | 19/32/0 | 409 | -0.9% | 801 | +0.0% | 29 s |
| 3 | [`enhancement-raid-dps`](enhancement-raid-dps.md) | ours: hand draft | 11/31/9 | 408 | -1.4% | 745 | -6.9% | 14 s |
| 4 | *Level 60* | community simulator | - | 405 | -2.0% | 755 | -5.7% | 31 s |
| 5 | [`elemental-enhancement-ml-raid`](elemental-enhancement-ml-raid.md) | ours: hand draft | 22/29/0 | 387 | -6.3% | 764 | -4.6% | 34 s |
| 6 | *Enhancement 16/35/0* | community simulator | - | 367 | -11.2% | 734 | -8.4% | 84 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-03, 5 changes to the base rotation; third-seed check: deep: Enhancement (dummy) 400 -> 417 DPS (+4.2%), deep: Enhancement (raid) 395 -> 412 DPS (+4.4%), deep: Hybrid Elemental/Enhancement (raid) 342 -> 363 DPS (+6.1%), sim preset: Level 60 390 -> 405 DPS (+3.7%), enhancement-raid-dps 393 -> 407 DPS (+3.5%), opt-enhancement-dps-raid-dps 392 -> 413 DPS (+5.3%)):
  1. insert before the filler: if not Flame Shock is on the target: cast Flame Shock (+0.6%, pass 1)
  2. only above 60% mana: cast Earth Shock (+1.1%, pass 1)
  3. drop the condition: if mana % ≥ 60%: cast Earth Shock (+3.0%, pass 2)
  4. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.8%, pass 4)
  5. insert at the end: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.4%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-03, 7 changes to the base rotation; third-seed check: deep: Enhancement (dummy) 685 -> 773 DPS (+12.8%), deep: Enhancement (raid) 679 -> 802 DPS (+18.0%), deep: Hybrid Elemental/Enhancement (raid) 542 -> 679 DPS (+25.2%), sim preset: Level 60 669 -> 756 DPS (+13.0%), enhancement-raid-dps 666 -> 745 DPS (+11.7%), opt-enhancement-dps-raid-dps 662 -> 755 DPS (+14.1%), enhancement-ml-parse 663 -> 797 DPS (+20.2%)):
  1. insert in the middle: if not Flame Shock is on the target: cast Flame Shock (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.3%, pass 1)
  3. drop 'time left in the fight ≥ 20s' from the condition: if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem (+0.2%, pass 1)
  4. insert before the filler: cast Fire Nova (+7.3%, pass 2)
  5. move down below 'cast Stormstrike': if not Flame Shock is on the target: cast Flame Shock (+0.3%, pass 2)
  6. move down below 'cast Earth Shock': cast Fire Nova + only with 10s or more of the fight left: if not Flame Shock is on the target: cast Flame Shock (+0.2%, pass 2)
  7. threshold 3.75 -> 2.812: if stacks of Maelstrom Weapon ≥ 3.75: cast Lightning Bolt (+0.3%, pass 4)

Before the pull: at -4.5s: cast Strength of Earth Totem; at -3s: cast Grace of Air Totem; at -1.5s: cast Searing Totem.

| # | Priority (the first line whose condition holds is cast) | [`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time left on the totem ≤ 0s: cast Strength of Earth Totem | 0.3 |
| 2 | if time left on the totem ≤ 0s: cast Grace of Air Totem | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | cast Stormstrike | 14.1 |
| 5 | if stacks of Maelstrom Weapon ≥ 3.75: cast Lightning Bolt | 4.6 |
| 6 | if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem | 1.3 |
| 7 | if not Flame Shock is on the target: cast Flame Shock | 4.0 |
| 8 | cast Earth Shock | 4.8 |
| 9 | if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem | 1.3 |

Damage by ability:

| Ability | [`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md) |
|---|---|
| Auto Attack | 27% |
| Windfury Weapon | 18% |
| Flame Shock | 12% |
| Lightning Bolt | 12% |
| Earth Shock | 11% |
| Stormstrike | 10% |
| Attack | 7% |
| Dragonbreath Chili | 3% |

## Notes

- Report: shaman/research/talents/forever/optimizer/enhancement-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
