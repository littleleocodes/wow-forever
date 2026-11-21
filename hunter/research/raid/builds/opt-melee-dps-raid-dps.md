# Optimizer — Melee hunter (Forever): dual-wield white swings under Aspect of the Beast, Raptor Strike on the next swing, Mongoose Bite after dodges and Expose Prey procs, Strider Kick on cooldown, Counterattack after parries, the Lacerating Strikes bleed, one Serpent Sting from the pull (the 8 yd minimum range stops every other shot in melee), and the pet unless Lone Wolf (raid-dps) — 5/15/31

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/15/31 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `melee-dps` and profile `raid-dps`: score +126.0% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (15)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Efficiency** | 4/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 12%. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |

### Survival (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 5/5 | changed | Increases your total Health by 10%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 15%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec |

## Core talents (priority order)

1. **Expose Prey** — Removing it costs 30.7 points of score in this model.
2. **Lone Wolf** — Removing it costs 19.8 points of score in this model.
3. **Deadly Aspects** — Removing it costs 19.4 points of score in this model.
4. **Predator's Edge** — Removing it costs 17.5 points of score in this model.
5. **Resourcefulness** — Removing it costs 15.6 points of score in this model.
6. **Careful Aim** — Removing it costs 11.8 points of score in this model.
7. **Strider Kick** — Removing it costs 10.7 points of score in this model.
8. **Improved Tracking** — Removing it costs 9.9 points of score in this model.

## Rank among our builds and the community simulator's

**3 of 6** for `melee-dps` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`survival-raid`](survival-raid.md) | ours: derived (simulator search) | 5/16/30 | 398 | +0.0% | 799 | -7.5% | 1 s |
| 2 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 394 | -1.0% | 836 | -3.2% | 20 s |
| 3 | **[`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md)** | ours: optimizer | 5/15/31 | 377 | -5.1% | 789 | -8.6% | 1 s |
| 4 | [`beast-survival-open-raid`](beast-survival-open-raid.md) | ours: derived (open search) | 16/11/24 | 303 | -23.9% | 864 | +0.0% | 100 s |
| 5 | [`survival-ml-parse`](survival-ml-parse.md) | ours: derived (ML search) | 5/14/32 | 300 | -24.6% | 793 | -8.1% | 86 s |
| 6 | *SV Melee* | community simulator | - | 256 | -35.7% | 734 | -15.1% | 101 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/melee.apl.json`), untuned. The rotation search of 2026-09-29 to 2026-10-05 (9 changes, `melee-dps-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/hunter/upstream/melee.apl.json`), untuned. The rotation search of 2026-09-29 to 2026-11-10 (7 changes, `melee-dps-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: at -22s: cast Hunter's Mark; at -20s: cast Aspect of the Beast; at -19s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time into the fight ≥ 5s: use every other cooldown when ready | as ready |
| 2 | cast Raptor Strike | 8.2 |
| 3 | if not Hunter's Mark is on the target: cast Hunter's Mark | 0.7 |
| 4 | if Strider Kick is up and not Serpent Sting is on the target and mana % > 30%: move to “Shoot spot” yd | as ready |
| 5 | if unitDistance > “Melee range” and not Serpent Sting is on the target: cast Serpent Sting (rank 8) | 2.2 |
| 6 | if unitDistance > “Melee range”: cast Arcane Shot | 0.7 |
| 7 | if unitDistance > “Melee range”: cast Multi-Shot | 0.3 |
| 8 | if unitDistance > “Melee range” and not (Arcane Shot is in range and (“Windup close” or “Just shot”)): move to “Melee range” yd | as ready |
| 9 | if unitDistance > “Melee range”: wait inputDelay | as ready |
| 10 | cast Mongoose Bite | 6.3 |
| 11 | cast Strider Kick | 6.5 |
| 12 | cast Immolation Trap | 2.0 |
| 13 | cast Wing Clip | 21.3 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent).

Damage by ability:

| Ability | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) |
|---|---|
| Auto Attack | 37% |
| Serpent Sting | 12% |
| Raptor Strike | 11% |
| Mongoose Bite | 9% |
| Immolation Trap | 9% |
| Strider Kick | 8% |
| Auto Shot | 5% |
| Wing Clip | 4% |
| Arcane Shot | 2% |
| Lacerating Strikes | 2% |

## Notes

- Report: hunter/research/talents/forever/optimizer/melee-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
