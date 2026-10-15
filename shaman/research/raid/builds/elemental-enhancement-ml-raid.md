# Elemental-Enhancement — Raid (machine-learning search) — 17/26/8

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/26/8 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental-Enhancement build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-15 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry enhancement-dps (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Elemental (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Reverberation** | 3/5 | changed | Reduces the cooldown of your Shock spells by 0.6 sec. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%. |
| **Elemental Devastation** | 3/3 | changed | Your offensive spell critical strikes will increase your chance to get a critical strike with melee attacks by 9% for 10 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Improved Fire Nova** | 2/2 | **NEW** | Increases the damage done by your Fire Nova spell by 20% and reduces its cooldown by 4 sec. |

### Enhancement (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Elemental Weapons** | 2/3 | moved | Increases the melee attack power bonus of your Rockbiter Weapon by 13%, your Windfury Weapon effect by 27% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 10%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Flurry** | 5/5 | changed | Increases your attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Stormstrike** | 1/1 | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Improved Stormstrike** | 2/2 | **NEW** | When you Stormstrike, you have a 100% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 100% chance to reset each time you Dodge or Parry. |

### Restoration (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |
| **Mindfulness** | 2/3 | **NEW** | Allows 33% of your Mana regeneration to continue while casting. |
| **Tidal Focus** | 1/5 | changed | Reduces the Mana cost of your healing spells by 1% and improves your chance to hit by 1%. |

## Rank among our builds and the community simulator's

**5 of 6** for `enhancement-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md) | ours: optimizer | 11/31/9 | 385 | +0.0% | 681 | -6.3% | 14 s |
| 2 | [`enhancement-ml-raid`](enhancement-ml-raid.md) | ours: hand draft | 19/32/0 | 383 | -0.4% | 727 | +0.0% | 30 s |
| 3 | [`enhancement-raid-dps`](enhancement-raid-dps.md) | ours: hand draft | 11/31/9 | 380 | -1.3% | 671 | -7.7% | 14 s |
| 4 | *Level 60* | community simulator | - | 379 | -1.6% | 684 | -5.8% | 32 s |
| 5 | **[`elemental-enhancement-ml-raid`](elemental-enhancement-ml-raid.md)** | ours: hand draft | 17/26/8 | 365 | -5.1% | 690 | -5.0% | 12 s |
| 6 | *Enhancement 16/35/0* | community simulator | - | 345 | -10.4% | 663 | -8.8% | 84 s |

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

| # | Priority (the first line whose condition holds is cast) | [`elemental-enhancement-ml-raid`](elemental-enhancement-ml-raid.md) casts/min |
|---|---|---|
| 1 | if time left on the totem ≤ 0s: cast Strength of Earth Totem | 0.3 |
| 2 | if time left on the totem ≤ 0s: cast Grace of Air Totem | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | cast Stormstrike | 14.2 |
| 5 | if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem | 1.3 |
| 6 | if not Flame Shock is on the target: cast Flame Shock | 3.8 |
| 7 | cast Earth Shock | 6.8 |
| 8 | if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem | 1.3 |

Lines of the simulator's rotation these builds never cast: cast Lightning Bolt (its condition never held in these fights).

Damage by ability:

| Ability | [`elemental-enhancement-ml-raid`](elemental-enhancement-ml-raid.md) |
|---|---|
| Auto Attack | 31% |
| spell 439440 | 20% |
| Earth Shock | 17% |
| Stormstrike | 12% |
| Flame Shock | 11% |
| Attack | 7% |
| Dragonbreath Chili | 3% |

## Notes

- Against the best hand draft elemental-raid-dps in a full raid, same gear and fights (100,000, one seed): +38.4% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow elemental-raid-dps: Reverberation → Ancestral Knowledge (within 0.03% of the search winner 18/25/8 on one seed, 30,000 fights).
- Search result (full raid): 18/25/8 at 718.6 ± 0.14 DPS over 100,000 fights; runner-up 18/25/8 (+0.09%; the winner takes Convection 5; the runner-up Concussion 1, Convection 4); 2,428 builds simulated; certificate: the neighbours ahead on the short run (of 200) did not hold on the longer one.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 17/25/9 at 690.8 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 29/22/0 at 379.9 DPS.

## Open questions (verify in the live game)

- A machine-searched Elemental-Enhancement build: check it against the community's Elemental-Enhancement builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
