# Enhancement — Raid (derived) — 11/31/9

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/31/9 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Enhancement raid damage build derived on 2026-09-30 (derive_raid.py): the community simulator's talent search (raidsim/talent_opt.py, entry enhancement-dps, training dummy) from the spec's best build opt-enhancement-dps-raid-dps, 30+ points kept in Enhancement.

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
| **Tidal Focus** | 1/5 | changed | Reduces the Mana cost of your healing spells by 1% and improves your chance to hit by 1%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |

## Rank among our builds and the community simulator's

**2 of 5** for `enhancement-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md) | ours: optimizer | 11/31/9 | 426 | +0.0% | 780 | +0.0% | 9 s |
| 2 | **[`enhancement-raid`](enhancement-raid.md)** | ours: hand draft | 11/31/9 | 424 | -0.4% | 770 | -1.2% | 0 s |
| 3 | *Level 60* | community simulator | - | 421 | -1.1% | 775 | -0.6% | 26 s |
| 4 | [`enhancement-raid-dps`](enhancement-raid-dps.md) | ours: hand draft | 11/31/9 | 420 | -1.3% | 770 | -1.3% | 9 s |
| 5 | *Enhancement 16/35/0* | community simulator | - | 388 | -8.9% | 761 | -2.3% | 81 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 3 changes to the base rotation; third-seed check: opt-enhancement-dps-raid-dps 406 -> 415 DPS (+2.3%), sim preset: Level 60 392 -> 400 DPS (+2.0%)):
  1. insert before the filler: if not Flame Shock is on the target: cast Flame Shock (+0.6%, pass 1)
  2. only above 60% mana: cast Earth Shock (+1.1%, pass 1)
  3. drop the condition: if mana % ≥ 60%: cast Earth Shock (+3.0%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 6 changes to the base rotation; third-seed check: opt-enhancement-dps-raid-dps 702 -> 774 DPS (+10.3%), sim preset: Level 60 690 -> 756 DPS (+9.7%)):
  1. insert in the middle: if not Flame Shock is on the target: cast Flame Shock (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.3%, pass 1)
  3. drop 'time left in the fight ≥ 20s' from the condition: if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem (+0.2%, pass 1)
  4. insert before the filler: cast Fire Nova (+7.3%, pass 2)
  5. move down below 'cast Stormstrike': if not Flame Shock is on the target: cast Flame Shock (+0.3%, pass 2)
  6. move down below 'cast Earth Shock': cast Fire Nova + only with 10s or more of the fight left: if not Flame Shock is on the target: cast Flame Shock (+0.2%, pass 2)

Before the pull: at -4.5s: cast Strength of Earth Totem; at -3s: cast Grace of Air Totem; at -1.5s: cast Searing Totem.

| # | Priority (the first line whose condition holds is cast) | [`enhancement-raid`](enhancement-raid.md) casts/min |
|---|---|---|
| 1 | if time left on the totem ≤ 0s: cast Strength of Earth Totem | 0.3 |
| 2 | if time left on the totem ≤ 0s: cast Grace of Air Totem | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | cast Stormstrike | 14.2 |
| 5 | if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt | 3.8 |
| 6 | if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem | 1.0 |
| 7 | if not Flame Shock is on the target: cast Flame Shock | 4.3 |
| 8 | cast Earth Shock | 5.1 |

Damage by ability:

| Ability | [`enhancement-raid`](enhancement-raid.md) |
|---|---|
| Auto Attack | 28% |
| Windfury Weapon | 19% |
| Stormstrike | 11% |
| Flame Shock | 11% |
| Earth Shock | 11% |
| Lightning Bolt | 8% |
| Attack | 6% |
| Elemental Sharpening Stone | 3% |
| Dragonbreath Chili | 3% |

## Notes

- About +3.1% over the hand draft enhancement-raid-dps (over the 2% replacement bar): this build is the spec's raid pick, the hand draft stays as the alternative.
- Simulator talent search from opt-enhancement-dps-raid-dps: 3 points Tidal Focus -> Mindfulness (+2.2% DPS on the search's third seed).
- Simulator numbers are the community's model of the beta (ElliotWood/Forever), not in-game measurements.

## Open questions (verify in the live game)

- A derived Enhancement raid build: check it against the community's Enhancement builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
