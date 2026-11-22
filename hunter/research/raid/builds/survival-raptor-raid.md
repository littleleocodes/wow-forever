# Survival — melee with a Raptor (the simulator's own build) — 16/4/31

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/4/31 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The official wowsims/forever simulator's own melee Survival build (SV Melee, 16/4/31): dual wield in melee with a Raptor out (Faster Attack II), Summon Hawk and the pet talents of Beast Mastery's first rows, Survival to Lacerating Strikes. Since 2026-11-20 it plays the simulator's own melee rotation (raidsim/apls/hunter/upstream/melee.apl.json): 914.9 DPS in a full raid, 3,000 fights (the play check of 2026-11-20), against the petless Beast-Survival's 863.6 in the melee-dps entry.

## Point allocation

### Beast Mastery (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |

### Marksmanship (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 4/5 | **NEW** | Increases your critical strike chance with all attacks by 4%. |

### Survival (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 15%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec |
| **Survivalist** | 3/5 | changed | Increases your total Health by 6%. |

## Core talents (priority order)

1. **Lacerating Strikes** — Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec
2. **Lightning Reflexes** — Increases your Agility by 15%
3. **Survivalist's Discipline** — Reduces the cooldown of your Trap and Deterrence abilities by 40%
4. **Strider Kick** — A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec
5. **Expose Prey** — Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite

## Rank among our builds and the community simulator's

**2 of 3** for `survival-pet-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 402 | +0.0% | 824 | -9.9% | 20 s |
| 2 | **[`survival-raptor-raid`](survival-raptor-raid.md)** | ours: derived (simulator preset) | 16/4/31 | 364 | -9.5% | 915 | +0.0% | 101 s |
| 3 | *SV Melee* | community simulator | - | 364 | -9.5% | 915 | +0.0% | 101 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/melee.apl.json`), untuned. The rotation search of 2026-09-29 to 2026-10-05 (9 changes, `survival-pet-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/melee.apl.json`), untuned. The rotation search of 2026-09-29 to 2026-11-10 (7 changes, `survival-pet-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: at -22s: cast Hunter's Mark; at -20s: cast Aspect of the Beast; at -19s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`survival-raptor-raid`](survival-raptor-raid.md) casts/min |
|---|---|---|
| 1 | if time into the fight ≥ 5s: use every other cooldown when ready | as ready |
| 2 | cast Raptor Strike | 3.0 |
| 3 | if not Hunter's Mark is on the target: cast Hunter's Mark | 0.7 |
| 4 | if Strider Kick is up and not Serpent Sting is on the target and mana % > 30%: move to “Shoot spot” yd | as ready |
| 5 | if unitDistance > “Melee range” and not Serpent Sting is on the target: cast Serpent Sting | 1.3 |
| 6 | if unitDistance > “Melee range”: cast Arcane Shot | 0.5 |
| 7 | if unitDistance > “Melee range”: cast Multi-Shot | 0.4 |
| 8 | if unitDistance > “Melee range” and not (Arcane Shot is in range and (“Windup close” or “Just shot”)): move to “Melee range” yd | as ready |
| 9 | if unitDistance > “Melee range”: wait inputDelay | as ready |
| 10 | cast Mongoose Bite | 4.7 |
| 11 | cast Strider Kick | 2.5 |
| 12 | cast Immolation Trap | 1.2 |
| 13 | if “Use Summon Hawk”: cast Summon Hawk | 2.2 |
| 14 | cast Wing Clip | 5.8 |

Damage by ability:

| Ability | [`survival-raptor-raid`](survival-raptor-raid.md) |
|---|---|
| Auto Attack | 35% |
| Pet: Auto Attack | 26% |
| Serpent Sting | 6% |
| Immolation Trap | 6% |
| Pet: Claw | 6% |
| Mongoose Bite | 6% |
| Raptor Strike | 3% |
| Auto Shot | 3% |
| Strider Kick | 3% |
| Summon Hawk | 1% |

## Notes

- The simulator's own build, credited (Simulator build first, 2026-11-20): the page starts from it; ours replaces it only when 0.5% ahead on two seeds and passing the spec's rules.
- Simulator numbers are the community's model of the game, not in-game measurements.
- 2026-11-20: the simulator's build with its filler points moved (3 points from Deflection to Survivalist): the same DPS bit for bit in a full raid and on the training dummy. The new talents follow the utility order (interrupt protection, threat, mana, range, survival; dodge, parry and block count for nothing in a damage dealer's raid), which the simulator cannot measure (deep-runs/credited_fillers_1120.py; the user's rule of 2026-11-08 that a page pick holds no talent that does nothing).

## Sources

- <https://github.com/wowsims/forever/blob/2e6e77d84/ui/specs/hunter/dps/builds/sv_melee.siml>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
