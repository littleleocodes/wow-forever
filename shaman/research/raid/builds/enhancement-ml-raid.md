# Enhancement — Raid (machine-learning search) — 19/32/0

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 19/32/0 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Enhancement build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-03 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry enhancement-dps (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Elemental (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Devastation** | 3/3 | changed | Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 9% for 10 sec. |
| **Reverberation** | 5/5 | changed | Reduces the cooldown of your Shock spells by 1.0 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Trial by Fire** | 2/2 | **NEW** | Increases the damage done by your Fire Nova spell by 20% and reduces its cooldown by 4 sec, and increases the duration of your Magma Totem by 20 sec. |

### Enhancement (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Elemental Weapons** | 2/3 | moved | Increases the melee attack power bonus of your Rockbiter Weapon by 13%, your Windfury Weapon effect by 27% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 10%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Flurry** | 5/5 | changed | Increases your attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Stormstrike** | 1/1 | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Improved Stormstrike** | 2/2 | **NEW** | When you Stormstrike, you have a 100% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 100% chance to reset each time you Dodge or Parry. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Maelstrom Weapon** | 5/5 | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 20%. Stacks up to 5 times. Lasts 30 sec. |
| **Rage of the Farseer** | 1/1 | **NEW** | Increases your attack speed by 30% for 25 sec. |

### Restoration (0)

*No points.*

## Rank among our builds and the community simulator's

**1 of 6** for `enhancement-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`enhancement-ml-raid`](enhancement-ml-raid.md)** | ours: derived (ML search) | 19/32/0 | 405 | +0.0% | 754 | +0.0% | 18 s |
| 2 | [`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md) | ours: optimizer | 11/31/9 | 404 | -0.2% | 704 | -6.6% | 4 s |
| 3 | *Level 60* | community simulator | - | 399 | -1.3% | 704 | -6.6% | 21 s |
| 4 | [`enhancement-raid-dps`](enhancement-raid-dps.md) | ours: hand draft | 11/31/9 | 399 | -1.3% | 694 | -7.9% | 4 s |
| 5 | [`elemental-enhancement-ml-raid`](elemental-enhancement-ml-raid.md) | ours: derived (ML search) | 17/26/8 | 381 | -6.0% | 713 | -5.4% | 2 s |
| 6 | *Enhancement 16/35/0* | community simulator | - | 362 | -10.6% | 691 | -8.3% | 79 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-03, 5 changes to the base rotation; third-seed check: deep: Enhancement (dummy) 400 -> 417 DPS (+4.2%), deep: Enhancement (raid) 395 -> 412 DPS (+4.4%), deep: Hybrid Elemental/Enhancement (raid) 342 -> 363 DPS (+6.1%), sim preset: Level 60 390 -> 405 DPS (+3.7%), enhancement-raid-dps 393 -> 407 DPS (+3.5%), opt-enhancement-dps-raid-dps 392 -> 413 DPS (+5.3%)):
  1. insert before the filler: if not Flame Shock is on the target: cast Flame Shock (+0.6%, pass 1)
  2. only above 60% mana: cast Earth Shock (+1.1%, pass 1)
  3. drop the condition: if mana % ≥ 60%: cast Earth Shock (+3.0%, pass 2)
  4. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.8%, pass 4)
  5. insert at the end: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.4%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-09, 8 changes to the base rotation; third-seed check: enhancement-ml-raid 715 -> 739 DPS (+3.4%), sim preset: Level 60 675 -> 696 DPS (+3.1%), enhancement-raid-dps 673 -> 683 DPS (+1.5%), opt-enhancement-dps-raid-dps 676 -> 693 DPS (+2.5%), elemental-enhancement-ml-raid 668 -> 690 DPS (+3.3%)):
  1. insert in the middle: if not Flame Shock is on the target: cast Flame Shock (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.3%, pass 1)
  3. drop 'time left in the fight ≥ 20s' from the condition: if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem (+0.2%, pass 1)
  4. insert before the filler: cast Fire Nova (+7.3%, pass 2)
  5. move down below 'cast Stormstrike': if not Flame Shock is on the target: cast Flame Shock (+0.3%, pass 2)
  6. move down below 'cast Earth Shock': cast Fire Nova + only with 10s or more of the fight left: if not Flame Shock is on the target: cast Flame Shock (+0.2%, pass 2)
  7. threshold 3.75 -> 2.812: if stacks of Maelstrom Weapon ≥ 3.75: cast Lightning Bolt (+0.3%, pass 4)
  8. threshold 2.812 -> 4.218: if stacks of Maelstrom Weapon ≥ 2.812: cast Lightning Bolt (+5.1%, pass 8)

Before the pull: at -4.5s: cast Strength of Earth Totem; at -3s: cast Grace of Air Totem; at -1.5s: cast Searing Totem.

| # | Priority (the first line whose condition holds is cast) | [`enhancement-ml-raid`](enhancement-ml-raid.md) casts/min |
|---|---|---|
| 1 | if time left on the totem ≤ 0s: cast Strength of Earth Totem | 0.3 |
| 2 | if time left on the totem ≤ 0s: cast Grace of Air Totem | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | cast Stormstrike | 14.6 |
| 5 | if stacks of Maelstrom Weapon ≥ 3.75: cast Lightning Bolt | 4.6 |
| 6 | if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem | 1.3 |
| 7 | if not Flame Shock is on the target: cast Flame Shock | 3.9 |
| 8 | cast Earth Shock | 6.0 |
| 9 | if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem | 1.3 |

Damage by ability:

| Ability | [`enhancement-ml-raid`](enhancement-ml-raid.md) |
|---|---|
| Auto Attack | 28% |
| Windfury Weapon | 19% |
| Earth Shock | 13% |
| Stormstrike | 11% |
| Flame Shock | 10% |
| Lightning Bolt | 10% |
| Attack | 6% |
| Dragonbreath Chili | 3% |

## Notes

- Against the best hand draft enhancement-raid-dps in a full raid, same gear and fights (100,000, one seed): +7.9% (over the 2% bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Search result (full raid): 19/32/0 at 801.3 ± 0.12 DPS over 200,000 fights; runner-up 19/32/0 (+0.05%; the winner takes Ancestral Knowledge 5, Elemental Weapons 2; the runner-up Ancestral Knowledge 4, Elemental Weapons 3); 7,070 builds simulated; certificate: none of its 322 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 19/32/0 at 781.7 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 20/31/0 at 416.9 DPS.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Enhancement: its full-raid winner is +0.00% against it, under the 0.5% bar for a new build.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 19/32/0 -> 19/32/0; Improved Fire Nova -> Trial by Fire (renamed) (refill: the enhancement-dps model, raid-dps).

## Open questions (verify in the live game)

- A machine-searched Enhancement build: check it against the community's Enhancement builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
