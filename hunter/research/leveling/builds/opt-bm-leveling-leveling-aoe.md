# Optimizer — Pet-first leveling (leveling-aoe) — 7/12/32

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/12/32 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `bm-leveling` and profile `leveling-aoe`: score +32.2% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Pathfinding** | 2/2 | moved | Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 6%. |

### Marksmanship (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Hawk Eye** | 3/3 | moved | Increases the range of your ranged weapons by 6 yards. |
| **Improved Concussive Shot** | 1/5 | unchanged | Gives your Concussive Shot a 4% chance to stun the target for 3 sec. |
| **Efficiency** | 1/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 3%. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |

### Survival (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Improved Wing Clip** | 3/3 | changed | Gives your Wing Clip ability a 20% chance to immobilize the target for 5 sec. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Entrapment** | 4/5 | changed | When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 4 sec. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Counterattack** | 1/1 | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. |
| **Survival Tactics** | 2/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 10%. |
| **Expose Prey** | 2/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 10%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Survival | Improved Tracking | 5 | 0/0/5 |
| 15-17 | Survival | Improved Wing Clip | 3 | 0/0/8 |
| 18-19 | Survival | Savage Strikes | 2 | 0/0/10 |
| 20 | Survival | Deterrence | 1 | 0/0/11 |
| 21-23 | Survival | Surefooted | 3 | 0/0/14 |
| 24 | Survival | Entrapment | 1 | 0/0/15 |
| 25 | Survival | Counterattack | 1 | 0/0/16 |
| 26-27 | Survival | Survival Tactics | 2 | 0/0/18 |
| 28-29 | Survival | Entrapment | 2 | 0/0/20 |
| 30 | Survival | Strider Kick | 1 | 0/0/21 |
| 31-32 | Survival | Expose Prey | 2 | 0/0/23 |
| 33-34 | Survival | Survivalist's Discipline | 2 | 0/0/25 |
| 35-39 | Survival | Lightning Reflexes | 5 | 0/0/30 |
| 40 | Survival | Lacerating Strikes | 1 | 0/0/31 |
| 41-45 | Marksmanship | Lethal Attacks | 5 | 0/5/31 |
| 46-48 | Marksmanship | Hawk Eye | 3 | 0/8/31 |
| 49 | Marksmanship | Efficiency | 1 | 0/9/31 |
| 50 | Marksmanship | Improved Concussive Shot | 1 | 0/10/31 |
| 51-52 | Marksmanship | Rapid Killing | 2 | 0/12/31 |
| 53-57 | Beast Mastery | Deadly Aspects | 5 | 5/12/31 |
| 58-59 | Beast Mastery | Pathfinding | 2 | 7/12/31 |
| 60 | Survival | Entrapment | 1 | 7/12/32 |

## Core talents (priority order)

1. **Strider Kick** — Removing it costs 7.5 points of score in this model.
2. **Efficiency** — Removing it costs 3.5 points of score in this model.
3. **Expose Prey** — Removing it costs 2.8 points of score in this model.
4. **Lacerating Strikes** — Removing it costs 2.6 points of score in this model.
5. **Surefooted** — Removing it costs 2.6 points of score in this model.
6. **Deadly Aspects** — Removing it costs 2.3 points of score in this model.
7. **Improved Wing Clip** — Removing it costs 1.5 points of score in this model.
8. **Rapid Killing** — Removing it costs 1.3 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level with a cat: the pet runs in and meets the mob halfway, Growls every 5 s and holds it until your threat passes 130% of its own. You shoot from 35 yd: Hunter's Mark, Serpent Sting, Summon Hawk or Arcane Shot, Multi-Shot / Aimed Shot on their shared cooldown, Auto Shot in between (the bow cannot fire inside 8 yd); Bestial Wrath, Intimidation and Rapid Fire on the pull when ready; Mend Pet when the pet drops below 35%; Feign Death, Wing Clip and Raptor Strike when a mob reaches you. Between fights: 2 s loot, 6 s travel, Mend Pet below 70% pet health, water below 35% mana, food below 65% health, a 10 s Revive Pet after a pet death; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-18, on top of the priority below): never cast Multi-Shot; never cast Arcane Shot; never cast Summon Hawk; drink below 15% mana. Together +8.2% time per kill saved for `leveling-beast-mastery` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/bm-leveling-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Claw | 5.3 | 6.9 | 5.5 | 5.8 | 6% |
| Melee | 3.8 | 4.7 | 3.0 | 3.6 | 14% |
| Growl | 2.4 | 3.6 | 2.8 | 3.1 | 0% |
| Auto Shot | 2.6 | 2.8 | 3.2 | 2.5 | 11% |
| Serpent Sting | 2.0 | 1.7 | 1.6 | 1.3 | 14% |
| Bite | 1.2 | 1.6 | 1.3 | 1.3 | 2% |
| Volley | 0.0 | 0.9 | 1.0 | 1.1 | 33% |
| Feign Death | 0.3 | 0.4 | 0.4 | 0.4 | 0% |
| Mongoose Bite | 0.3 | 0.4 | 0.3 | 0.3 | 2% |
| Wing Clip | 0.2 | 0.2 | 0.2 | 0.3 | 0% |
| Aimed Shot | 0.7 | 0.3 | 0.3 | 0.1 | 1% |
| Raptor Strike | 0.4 | 0.2 | 0.1 | 0.1 | 1% |
| Hunter's Mark | 0.4 | 0.2 | 0.2 | 0.1 | 0% |

## Notes

- Allocation and order taken from cand-aoe-r2 on 2026-10-18: an earlier optimizer round beat the last export in the fight lab (40.0s vs 49.3s per kill, level-weighted).
- Report: hunter/research/talents/forever/optimizer/bm-leveling-leveling-aoe.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
