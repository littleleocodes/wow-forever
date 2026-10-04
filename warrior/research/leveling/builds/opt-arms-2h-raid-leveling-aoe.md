# Optimizer — Two-handed Arms/raid or leveling: white ~45%, Heroic Strike, Overpower, Execute, Rend; Mortal Strike/Slam arrive as talent effects (leveling-aoe) — 19/32/0

*[Warrior](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 19/32/0 (Arms / Fury / Protection) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `arms-2h-raid` and profile `leveling-aoe`: score +54.5% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arms (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | unchanged | Increases your Parry chance by 5%. |
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Improved Tactical Mastery** | 2/5 | **NEW** | Tactical Mastery lets you retain up to an additional 6 Rage when you change stances. |
| **Improved Overpower** | 2/2 | moved | Increases the critical strike chance of your Overpower ability by 50%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |
| **Spearing Strike** | 1/1 | **NEW** | A brutal attack that deals 40% weapon damage, plus an additional 80% weapon damage against Giants, Dragonkin, and mounted targets. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 3%. |

### Fury (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Booming Voice** | 4/5 | changed | Increases the area of effect of your Shouts by 40% and reduces their Rage cost by 20%. |
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. |
| **Piercing Howl** | 1/1 | changed | Causes all enemies within 10 yds to be Dazed, reducing movement speed by 50% for 6 sec. |
| **Blood Craze** | 3/3 | changed | Regenerates 3% of your total Health over 6 sec after being the victim of a critical strike or suffering more than 20% of your maximum Health from a single attack. |
| **Enrage** | 5/5 | changed | Gives you a 30% chance to deal 10% increased Physical damage for 12 sec after being the victim of any damaging attack. |
| **Improved Execute** | 2/2 | changed | Reduces the Rage cost of your Execute ability by 5. |
| **Death Wish** | 1/1 | changed | When activated, increases your Physical damage done by 20% and makes you immune to Fear effects, but increases all damage you take by 5%. Lasts 30 sec. |
| **Flurry** | 5/5 | changed | Increases your melee attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Bloodthirst** | 1/1 | changed | Instantly attack the target causing damage equal to 45% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec. |

### Protection (0)

*No points.*

## Core talents (priority order)

1. **Enrage** — Removing it costs 5.4 points of score in this model.
2. **Cruelty** — Removing it costs 5.1 points of score in this model.
3. **Bloodthirst** — Removing it costs 4.6 points of score in this model.
4. **Flurry** — Removing it costs 4.2 points of score in this model.
5. **Precision** — Removing it costs 2.4 points of score in this model.
6. **Blood Craze** — Removing it costs 2.3 points of score in this model.
7. **Death Wish** — Removing it costs 1.9 points of score in this model.
8. **Improved Overpower** — Removing it costs 1.4 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level with a two-hander in Battle Stance: Bloodrage and Charge on the pull (the mob is stunned 1 s), Battle Shout kept up, Victory Rush after a kill, Mortal Strike on cooldown, Overpower after a dodge or a Bloodthrill proc, Rend once, Execute under 20% with all the rage, Heroic Strike with spare rage, white swings that generate rage by Classic's formula (the mob dodges 5%, parries 5%, 10% of swings glance for 95%). Between fights: 2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below 50%, rage decays; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-09-28, on top of the priority below): eat below 40% health. Together +2.9% time per kill saved for `leveling-arms` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/arms-2h-raid-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Melee | 4.7 | 5.9 | 6.3 | 6.8 | 43% |
| Thunder Clap | 1.3 | 1.1 | 1.2 | 1.5 | 6% |
| Rend | 1.0 | 1.1 | 1.1 | 1.1 | 8% |
| Execute | 0.8 | 1.0 | 1.1 | 1.1 | 13% |
| Whirlwind | 0.0 | 0.7 | 0.8 | 0.9 | 14% |
| Overpower | 0.4 | 0.4 | 0.5 | 0.5 | 6% |
| Bloodthirst | 0.0 | 0.4 | 0.4 | 0.4 | 2% |
| Charge | 0.3 | 0.3 | 0.4 | 0.4 | 0% |
| Bloodrage | 0.3 | 0.3 | 0.3 | 0.4 | 0% |
| Cleave | 0.4 | 0.2 | 0.2 | 0.3 | 4% |
| Victory Rush | 0.2 | 0.2 | 0.2 | 0.2 | 0% |
| Battle Shout | 0.2 | 0.2 | 0.2 | 0.2 | 0% |
| Heroic Strike | 0.3 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: warrior/talents/forever/optimizer/arms-2h-raid-leveling-aoe.md
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Boundless Rage 1, Precision 3 out; Booming Voice 4 in; to be re-optimized.

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
