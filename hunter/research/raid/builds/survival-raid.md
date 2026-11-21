# Survival — Raid (derived) — 5/16/30

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/16/30 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Survival raid damage build derived on 2026-09-30 (derive_raid.py): the community simulator's talent search (raidsim/talent_opt.py, entry melee-dps, training dummy) from the spec's best build opt-melee-dps-raid-dps, 30+ points kept in Survival.

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |

### Survival (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 3/5 | changed | Increases your total Health by 6%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 3/5 | changed | Increases your Agility by 9%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |

## Rank among our builds and the community simulator's

**1 of 6** for `melee-dps` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`survival-raid`](survival-raid.md)** | ours: derived (simulator search) | 5/16/30 | 398 | +0.0% | 799 | -7.5% | 1 s |
| 2 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 394 | -1.0% | 836 | -3.2% | 20 s |
| 3 | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) | ours: optimizer | 5/15/31 | 377 | -5.1% | 789 | -8.6% | 1 s |
| 4 | [`beast-survival-open-raid`](beast-survival-open-raid.md) | ours: derived (open search) | 16/11/24 | 303 | -23.9% | 864 | +0.0% | 100 s |
| 5 | [`survival-ml-parse`](survival-ml-parse.md) | ours: derived (ML search) | 5/14/32 | 300 | -24.6% | 793 | -8.1% | 86 s |
| 6 | *SV Melee* | community simulator | - | 256 | -35.7% | 734 | -15.1% | 101 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/melee.apl.json`), untuned. The rotation search of 2026-09-29 to 2026-10-05 (9 changes, `melee-dps-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/melee.apl.json`), untuned. The rotation search of 2026-09-29 to 2026-11-10 (7 changes, `melee-dps-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: at -22s: cast Hunter's Mark; at -20s: cast Aspect of the Beast; at -19s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`survival-raid`](survival-raid.md) casts/min |
|---|---|---|
| 1 | if time into the fight ≥ 5s: use every other cooldown when ready | as ready |
| 2 | cast Raptor Strike | 8.2 |
| 3 | if not Hunter's Mark is on the target: cast Hunter's Mark | 0.7 |
| 4 | if Strider Kick is up and not Serpent Sting is on the target and mana % > 30%: move to “Shoot spot” yd | as ready |
| 5 | if unitDistance > “Melee range” and not Serpent Sting is on the target: cast Serpent Sting (rank 8) | 2.1 |
| 6 | if unitDistance > “Melee range”: cast Arcane Shot | 0.7 |
| 7 | if unitDistance > “Melee range”: cast Multi-Shot | 0.3 |
| 8 | if unitDistance > “Melee range” and not (Arcane Shot is in range and (“Windup close” or “Just shot”)): move to “Melee range” yd | as ready |
| 9 | if unitDistance > “Melee range”: wait inputDelay | as ready |
| 10 | cast Mongoose Bite | 6.3 |
| 11 | cast Strider Kick | 6.5 |
| 12 | cast Immolation Trap | 3.2 |
| 13 | cast Wing Clip | 20.1 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent).

Damage by ability:

| Ability | [`survival-raid`](survival-raid.md) |
|---|---|
| Auto Attack | 34% |
| Immolation Trap | 17% |
| Serpent Sting | 11% |
| Raptor Strike | 10% |
| Mongoose Bite | 9% |
| Strider Kick | 7% |
| Auto Shot | 4% |
| Wing Clip | 4% |
| Arcane Shot | 2% |
| Multi-Shot | 1% |

## Notes

- About +3.3% over the hand draft melee-survival-raid (over the 2% replacement bar): this build is the spec's raid pick, the hand draft stays as the alternative.
- Simulator talent search from opt-melee-dps-raid-dps: 2 points Survivalist -> Clever Traps; 1 point Lacerating Strikes -> Efficiency; 2 points Lightning Reflexes -> Survivalist's Discipline (+3.2% DPS on the search's third seed).
- Simulator numbers are the community's model of the beta (ElliotWood/Forever), not in-game measurements.

## Open questions (verify in the live game)

- A derived Survival raid build: check it against the community's Survival builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
