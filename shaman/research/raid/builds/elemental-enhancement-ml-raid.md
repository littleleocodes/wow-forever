# Elemental-Enhancement — Raid (machine-learning search) — 17/29/5

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/29/5 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental-Enhancement build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-29 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry enhancement-dps (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Elemental (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Elemental Devastation** | 3/3 | changed | Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 9% for 10 sec. |
| **Reverberation** | 3/5 | changed | Reduces the cooldown of your Shock spells by 0.6 sec. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Trial by Fire** | 2/2 | **NEW** | Increases the damage done by your Fire Nova spell by 20% and reduces its cooldown by 4 sec, and increases the duration of your Magma Totem by 20 sec. |

### Enhancement (29)

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
| **Maelstrom Weapon** | 4/5 | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 16%. Stacks up to 5 times. Lasts 30 sec. |

### Restoration (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |

## Rank among our builds and the community simulator's

**5 of 6** for `enhancement-dps` by training-dummy DPS in the community simulator (wowsims/forever 54ceac6 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`enhancement-open-raid`](enhancement-open-raid.md) | ours: derived (open search) | 17/31/3 | 394 | +0.0% | 720 | +0.0% | 12 s |
| 2 | *Standard* | community simulator | - | 394 | +0.0% | 720 | +0.0% | 12 s |
| 3 | [`enhancement-ml-raid`](enhancement-ml-raid.md) | ours: derived (ML search) | 19/32/0 | 387 | -1.9% | 704 | -2.2% | 7 s |
| 4 | [`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md) | ours: optimizer | 14/31/6 | 378 | -4.0% | 658 | -8.6% | 20 s |
| 5 | **[`elemental-enhancement-ml-raid`](elemental-enhancement-ml-raid.md)** | ours: derived (ML search) | 17/29/5 | 378 | -4.2% | 682 | -5.3% | 11 s |
| 6 | [`enhancement-raid-dps`](enhancement-raid-dps.md) | ours: hand draft | 11/31/9 | 365 | -7.4% | 655 | -9.0% | 14 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-03, 5 changes to the base rotation; third-seed check: deep: Enhancement (dummy) 400 -> 417 DPS (+4.2%), deep: Enhancement (raid) 395 -> 412 DPS (+4.4%), deep: Hybrid Elemental/Enhancement (raid) 342 -> 363 DPS (+6.1%), sim preset: Level 60 390 -> 405 DPS (+3.7%), enhancement-raid-dps 393 -> 407 DPS (+3.5%), opt-enhancement-dps-raid-dps 392 -> 413 DPS (+5.3%)):
  1. insert before the filler: if not Flame Shock is on the target: cast Flame Shock (+0.6%, pass 1)
  2. only above 60% mana: cast Earth Shock (+1.1%, pass 1)
  3. drop the condition: if mana % ≥ 60%: cast Earth Shock (+3.0%, pass 2)
  4. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.8%, pass 4)
  5. insert at the end: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.4%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 12 passes, the last 2026-11-02, 11 changes to the base rotation; third-seed check: enhancement-open-raid 648 -> 720 DPS (+11.1%), sim preset: Standard 634 -> 705 DPS (+11.2%), enhancement-raid-dps 603 -> 656 DPS (+8.7%), opt-enhancement-dps-raid-dps 607 -> 658 DPS (+8.3%), enhancement-ml-raid 629 -> 703 DPS (+11.8%), elemental-enhancement-ml-raid 605 -> 681 DPS (+12.5%)):
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

| # | Priority (the first line whose condition holds is cast) | [`elemental-enhancement-ml-raid`](elemental-enhancement-ml-raid.md) casts/min |
|---|---|---|
| 1 | if time left on the totem ≤ 0s: cast Strength of Earth Totem | 0.3 |
| 2 | if time left on the totem ≤ 0s: cast Grace of Air Totem | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | cast Stormstrike | 7.3 |
| 5 | if stacks of Maelstrom Weapon ≥ 3.75: cast Lightning Bolt | 4.3 |
| 6 | if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem | 1.3 |
| 7 | if not Flame Shock is on the target: cast Flame Shock | 2.8 |
| 8 | cast Earth Shock | 6.9 |
| 9 | if number of targets = 1 and time left on the totem ≤ 0s: cast Searing Totem | 1.3 |

Damage by ability:

| Ability | [`elemental-enhancement-ml-raid`](elemental-enhancement-ml-raid.md) |
|---|---|
| Auto Attack | 41% |
| Earth Shock | 17% |
| Flame Shock | 12% |
| Lightning Bolt | 12% |
| Stormstrike | 10% |
| Searing Totem | 7% |

## Notes

- Search result (full raid): 17/29/5 at 711.8 ± 0.12 DPS over 100,000 fights; runner-up 17/29/5 (+0.02%; the winner takes Concussion 4, Convection 1; the runner-up Concussion 2, Convection 3); 1,660 builds simulated; certificate: none of its 250 one-move and chain-move neighbours was 0.1% ahead.
- Where the simulator measured no difference, the points follow elemental-enhancement-ml-raid: Concussion → Convection (4 points) (within 0.02% of the search winner 17/29/5 on one seed, 30,000 fights).
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 17/29/5 at 697.9 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 16/29/6 at 391.7 DPS.

## Open questions (verify in the live game)

- A machine-searched Elemental-Enhancement build: check it against the community's Elemental-Enhancement builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
