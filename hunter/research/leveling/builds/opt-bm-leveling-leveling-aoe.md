# Optimizer — Pet-first leveling (leveling-aoe) — 20/0/31

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/0/31 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `bm-leveling` and profile `leveling-aoe`: score +55.0% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Pathfinding** | 2/2 | moved | Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 6%. |
| **Improved Revive Pet** | 1/2 | unchanged | Revive Pet's casting time is reduced by 3 sec, mana cost is reduced by 20%, and increases the health your pet returns with by an additional 15%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Ferocity** | 4/5 | changed | Increases the critical strike chance of your pets and hawks by 8%. |

### Marksmanship (0)

*No points.*

### Survival (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 4/5 | unchanged | Increases your Parry chance by 4%. |
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Improved Wing Clip** | 3/3 | changed | Gives your Wing Clip ability a 20% chance to immobilize the target for 5 sec. |
| **Entrapment** | 3/5 | changed | When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 3 sec. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Counterattack** | 1/1 | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 10 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 10%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Beast Mastery | Deadly Aspects | 5 | 5/0/0 |
| 15-16 | Beast Mastery | Focused Fire | 2 | 7/0/0 |
| 17-18 | Beast Mastery | Pathfinding | 2 | 9/0/0 |
| 19 | Beast Mastery | Improved Revive Pet | 1 | 10/0/0 |
| 20-24 | Beast Mastery | Unleashed Fury | 5 | 15/0/0 |
| 25 | Beast Mastery | Summon Hawk | 1 | 16/0/0 |
| 26-29 | Beast Mastery | Ferocity | 4 | 20/0/0 |
| 30-33 | Survival | Deflection | 4 | 20/0/4 |
| 34 | Survival | Improved Tracking | 1 | 20/0/5 |
| 35-37 | Survival | Improved Wing Clip | 3 | 20/0/8 |
| 38-39 | Survival | Improved Tracking | 2 | 20/0/10 |
| 40-41 | Survival | Surefooted | 2 | 20/0/12 |
| 42 | Survival | Deterrence | 1 | 20/0/13 |
| 43-44 | Survival | Improved Tracking | 2 | 20/0/15 |
| 45 | Survival | Counterattack | 1 | 20/0/16 |
| 46 | Survival | Surefooted | 1 | 20/0/17 |
| 47-49 | Survival | Entrapment | 3 | 20/0/20 |
| 50 | Survival | Strider Kick | 1 | 20/0/21 |
| 51-52 | Survival | Expose Prey | 2 | 20/0/23 |
| 53-54 | Survival | Survivalist's Discipline | 2 | 20/0/25 |
| 55-59 | Survival | Lightning Reflexes | 5 | 20/0/30 |
| 60 | Survival | Lacerating Strikes | 1 | 20/0/31 |

## Core talents (priority order)

1. **Summon Hawk** — Removing it costs 8.2 points of score in this model.
2. **Strider Kick** — Removing it costs 6.6 points of score in this model.
3. **Unleashed Fury** — Removing it costs 4.3 points of score in this model.
4. **Improved Tracking** — Removing it costs 3.4 points of score in this model.
5. **Expose Prey** — Removing it costs 2.4 points of score in this model.
6. **Lacerating Strikes** — Removing it costs 2.3 points of score in this model.
7. **Lightning Reflexes** — Removing it costs 2.2 points of score in this model.
8. **Ferocity** — Removing it costs 2.0 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level with a cat: the pet runs in and meets the mob halfway, Growls every 5 s and holds it until your threat passes 130% of its own. You shoot from 35 yd: Hunter's Mark, Serpent Sting, Summon Hawk or Arcane Shot, Multi-Shot / Aimed Shot on their shared cooldown, Auto Shot in between (the bow cannot fire inside 8 yd); Bestial Wrath, Intimidation and Rapid Fire on the pull when ready; Mend Pet when the pet drops below 35%; Feign Death, Wing Clip and Raptor Strike when a mob reaches you. Between fights: 2 s loot, 6 s travel, Mend Pet below 70% pet health, water below 35% mana, food below 65% health, a 10 s Revive Pet after a pet death; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-09-28, on top of the priority below): never cast Multi-Shot; never cast Arcane Shot; drink below 15% mana; never cast Feign Death. Together +6.0% time per kill saved for `leveling-beast-mastery` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/bm-leveling-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Claw | 5.0 | 5.2 | 5.2 | 6.3 | 6% |
| Melee | 3.5 | 4.2 | 4.2 | 5.6 | 18% |
| Growl | 3.7 | 4.0 | 4.1 | 5.2 | 0% |
| Auto Shot | 3.3 | 3.9 | 5.3 | 4.7 | 17% |
| Volley | 0.0 | 1.3 | 1.4 | 1.6 | 11% |
| Serpent Sting | 1.9 | 1.7 | 1.7 | 1.6 | 16% |
| Mongoose Bite | 0.7 | 0.9 | 0.9 | 1.2 | 5% |
| Wing Clip | 0.4 | 0.5 | 0.7 | 0.8 | 0% |
| Bite | 0.4 | 0.5 | 0.5 | 0.5 | 1% |
| Raptor Strike | 1.1 | 0.5 | 0.3 | 0.3 | 1% |
| Hunter's Mark | 0.4 | 0.3 | 0.3 | 0.3 | 0% |
| Summon Hawk | 0.6 | 0.3 | 0.3 | 0.2 | 0% |
| Aimed Shot | 0.5 | 0.2 | 0.1 | 0.1 | 1% |

## Notes

- Allocation and order taken from cand-aoe-r7 on 2026-09-29: an earlier optimizer round beat the last export in the fight lab (56.3s vs 58.6s per kill, level-weighted).
- Report: hunter/talents/forever/optimizer/bm-leveling-leveling-aoe.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
