# Enhancement — Raid (open talent search) — 17/31/3

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/31/3 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Enhancement raid build the open talent search found on 2026-10-26: every legal 51-point build with no tree rule, searched in the community simulator's enhancement-dps rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.5% over enhancement-ml-raid, the best of our builds in that rotation.

## Point allocation

### Elemental (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Elemental Devastation** | 3/3 | changed | Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 9% for 10 sec. |
| **Reverberation** | 3/5 | changed | Reduces the cooldown of your Shock spells by 0.6 sec. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Trial by Fire** | 2/2 | **NEW** | Increases the damage done by your Fire Nova spell by 20% and reduces its cooldown by 4 sec, and increases the duration of your Magma Totem by 20 sec. |

### Enhancement (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 3/5 | changed | Increases your Intellect by 6%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Elemental Weapons** | 3/3 | moved | Increases the melee attack power bonus of your Rockbiter Weapon by 20%, your Windfury Weapon effect by 40% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 15%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Flurry** | 5/5 | changed | Increases your attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Stormstrike** | 1/1 | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Improved Stormstrike** | 2/2 | **NEW** | When you Stormstrike, you have a 100% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 100% chance to reset each time you Dodge or Parry. |
| **Maelstrom Weapon** | 5/5 | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 20%. Stacks up to 5 times. Lasts 30 sec. |
| **Rage of the Farseer** | 1/1 | **NEW** | Increases your attack speed by 30% for 25 sec. |

### Restoration (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 3/5 | changed | Reduces the Mana cost of your healing spells by 3% and improves your chance to hit by 3%. |

## Core talents (priority order)

1. **Maelstrom Weapon** — 292 DPS lost without it (40% of the build in a full raid; removal, 12,000 fights).
2. **Stormstrike** — 153 DPS lost without it (21% of the build in a full raid; removal, 12,000 fights).
3. **Flurry** — 61 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Shamanistic Focus** — 53 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
5. **Mental Dexterity** — 42 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Thundering Strikes** — 34 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Call of Flame** — 31 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
8. **Improved Stormstrike** — 30 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 6** for `enhancement-dps` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`enhancement-open-raid`](enhancement-open-raid.md)** | ours: derived (open search) | 17/31/3 | 402 | +0.0% | 734 | +0.0% | 10 s |
| 2 | [`enhancement-ml-raid`](enhancement-ml-raid.md) | ours: derived (ML search) | 19/32/0 | 398 | -1.0% | 722 | -1.6% | 5 s |
| 3 | *Standard* | community simulator | - | 396 | -1.5% | 726 | -1.1% | 13 s |
| 4 | [`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md) | ours: optimizer | 14/31/6 | 386 | -4.0% | 672 | -8.4% | 18 s |
| 5 | [`enhancement-raid-dps`](enhancement-raid-dps.md) | ours: hand draft | 11/31/9 | 373 | -7.3% | 668 | -8.9% | 12 s |
| 6 | [`elemental-enhancement-ml-raid`](elemental-enhancement-ml-raid.md) | ours: derived (ML search) | 15/24/12 | 255 | -36.7% | 437 | -40.4% | 29 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-03, 5 changes to the base rotation; third-seed check: deep: Enhancement (dummy) 400 -> 417 DPS (+4.2%), deep: Enhancement (raid) 395 -> 412 DPS (+4.4%), deep: Hybrid Elemental/Enhancement (raid) 342 -> 363 DPS (+6.1%), sim preset: Level 60 390 -> 405 DPS (+3.7%), enhancement-raid-dps 393 -> 407 DPS (+3.5%), opt-enhancement-dps-raid-dps 392 -> 413 DPS (+5.3%)):
  1. insert before the filler: if not Flame Shock is on the target: cast Flame Shock (+0.6%, pass 1)
  2. only above 60% mana: cast Earth Shock (+1.1%, pass 1)
  3. drop the condition: if mana % ≥ 60%: cast Earth Shock (+3.0%, pass 2)
  4. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.8%, pass 4)
  5. insert at the end: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.4%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 11 passes, the last 2026-10-26, 11 changes to the base rotation; third-seed check: open winner 661 -> 734 DPS (+11.0%), enhancement-ml-raid 647 -> 722 DPS (+11.6%), sim preset: Standard 652 -> 725 DPS (+11.2%), enhancement-raid-dps 615 -> 668 DPS (+8.6%), opt-enhancement-dps-raid-dps 619 -> 671 DPS (+8.3%), elemental-enhancement-ml-raid 345 -> 437 DPS (+26.8%)):
  1. insert in the middle: if not Flame Shock is on the target: cast Flame Shock (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.3%, pass 1)
  3. drop 'time left in the fight ≥ 20s' from the condition: if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem (+0.2%, pass 1)
  4. insert before the filler: cast Fire Nova (+7.3%, pass 2)
  5. move down below 'cast Stormstrike': if not Flame Shock is on the target: cast Flame Shock (+0.3%, pass 2)
  6. move down below 'cast Earth Shock': cast Fire Nova + only with 10s or more of the fight left: if not Flame Shock is on the target: cast Flame Shock (+0.2%, pass 2)
  7. threshold 3.75 -> 2.812: if stacks of Maelstrom Weapon ≥ 3.75: cast Lightning Bolt (+0.3%, pass 4)
  8. threshold 2.812 -> 4.218: if stacks of Maelstrom Weapon ≥ 2.812: cast Lightning Bolt (+5.1%, pass 8)
  9. insert at the end: if auraIsInactive: cast Rockbiter Weapon (+3.5%, pass 10)
  10. insert in the middle: if auraIsInactive: cast Magma Totem (+1.4%, pass 10)
  11. only above 25% mana: if auraIsInactive: cast Magma Totem (+0.2%, pass 10)

Before the pull: at -4.5s: cast Strength of Earth Totem; at -3s: cast Grace of Air Totem; at -1.5s: cast Searing Totem.

| # | Priority (the first line whose condition holds is cast) | [`enhancement-open-raid`](enhancement-open-raid.md) casts/min |
|---|---|---|
| 1 | if time left on the totem ≤ 0s: cast Strength of Earth Totem | 0.3 |
| 2 | if time left on the totem ≤ 0s: cast Grace of Air Totem | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | cast Stormstrike | 7.4 |
| 5 | if stacks of Maelstrom Weapon ≥ 3.75: cast Lightning Bolt | 4.6 |
| 6 | if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem | 1.3 |
| 7 | if not Flame Shock is on the target: cast Flame Shock | 2.8 |
| 8 | cast Earth Shock | 6.9 |
| 9 | if number of targets = 1 and time left on the totem ≤ 0s: cast Searing Totem | 1.3 |

Damage by ability:

| Ability | [`enhancement-open-raid`](enhancement-open-raid.md) |
|---|---|
| Auto Attack | 42% |
| Earth Shock | 16% |
| Lightning Bolt | 13% |
| Flame Shock | 12% |
| Stormstrike | 10% |
| Searing Totem | 7% |

## Notes

- +9.9% over the best hand draft of the spec, enhancement-raid-dps, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (enhancement-dps, full raid): 17/31/3 (Enhancement) at 733.5 DPS; enhancement-ml-raid 722.4, opt-enhancement-dps-raid-dps 670.8, enhancement-raid-dps 667.7, elemental-enhancement-ml-raid 437.2 in the same fights; 2,330 builds simulated, 1 independent runs reached the top.
- The enhancement-dps raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): elemental-dps -54.4%, stormcaller-dps -55.0%; none adopted.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Enhancement build: check it against the community's Enhancement builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/shaman/60/053303102-053030031005102251-03-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
