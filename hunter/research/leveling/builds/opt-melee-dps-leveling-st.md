# Optimizer — Melee hunter (Forever): dual-wield white swings under Aspect of the Beast, Raptor Strike on the next swing, Mongoose Bite after dodges and Expose Prey procs, Strider Kick on cooldown, Counterattack after parries, the Lacerating Strikes bleed, one Serpent Sting from the pull (the 8 yd minimum range stops every other shot in melee), and the pet unless Lone Wolf (leveling-st) — 9/13/29

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/13/29 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `melee-dps` and profile `leveling-st`: score +40.7% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Pathfinding** | 2/2 | moved | Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 6%. |

### Marksmanship (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |

### Survival (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 4/5 | unchanged | Increases your Parry chance by 4%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Counterattack** | 1/1 | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the mana cost of your Trap abilities and melee abilities by 60%. In addition, your critical strikes have a 60% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 10 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Lightning Reflexes** | 1/5 | changed | Increases your Agility by 2%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Survival | Improved Tracking | 5 | 0/0/5 |
| 15-16 | Survival | Savage Strikes | 2 | 0/0/7 |
| 17-19 | Survival | Deflection | 3 | 0/0/10 |
| 20-22 | Survival | Surefooted | 3 | 0/0/13 |
| 23 | Survival | Deterrence | 1 | 0/0/14 |
| 24 | Survival | Deflection | 1 | 0/0/15 |
| 25 | Survival | Counterattack | 1 | 0/0/16 |
| 26-29 | Survival | Predator's Edge | 4 | 0/0/20 |
| 30 | Survival | Strider Kick | 1 | 0/0/21 |
| 31-32 | Survival | Resourcefulness | 2 | 0/0/23 |
| 33-34 | Survival | Expose Prey | 2 | 0/0/25 |
| 35 | Survival | Predator's Edge | 1 | 0/0/26 |
| 36-40 | Marksmanship | Lethal Attacks | 5 | 0/5/26 |
| 41-43 | Marksmanship | Improved Stings | 3 | 0/8/26 |
| 44-48 | Marksmanship | Careful Aim | 5 | 0/13/26 |
| 49-50 | Survival | Survivalist's Discipline | 2 | 0/13/28 |
| 51-55 | Beast Mastery | Deadly Aspects | 5 | 5/13/28 |
| 56-57 | Beast Mastery | Focused Fire | 2 | 7/13/28 |
| 58-59 | Beast Mastery | Pathfinding | 2 | 9/13/28 |
| 60 | Survival | Lightning Reflexes | 1 | 9/13/29 |

## Core talents (priority order)

1. **Resourcefulness** — Removing it costs 7.1 points of score in this model.
2. **Strider Kick** — Removing it costs 6.0 points of score in this model.
3. **Predator's Edge** — Removing it costs 3.4 points of score in this model.
4. **Lethal Attacks** — Removing it costs 2.9 points of score in this model.
5. **Savage Strikes** — Removing it costs 1.7 points of score in this model.
6. **Careful Aim** — Removing it costs 1.7 points of score in this model.
7. **Expose Prey** — Removing it costs 1.5 points of score in this model.
8. **Improved Tracking** — Removing it costs 1.4 points of score in this model.

## Leveling rotation (fight lab)

The melee hunter: Serpent Sting from range, then stand and fight beside the pet: Raptor Strike queued on the next swing whenever it is ready, Deterrence when low, Counterattack after a parry, Mongoose Bite when a dodge or Expose Prey activates it, Strider Kick on cooldown, Immolation Trap at your feet, then (with Expose Prey) Hunter's Mark in a free global cooldown; Mend Pet for the pet.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-09, on top of the priority below): never cast Serpent Sting. Together +1.7% time per kill saved for `leveling-melee` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/melee-dps-opt.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Melee (off-hand) | 3.1 | 4.2 | 5.8 | 5.8 | 6.5 | 11% |
| Claw | 3.5 | 4.3 | 4.9 | 5.0 | 5.2 | 5% |
| Melee | 1.9 | 3.0 | 4.0 | 4.2 | 4.8 | 13% |
| Growl | 1.9 | 2.5 | 3.2 | 3.3 | 3.5 | 0% |
| Strider Kick | 0.0 | 1.8 | 2.2 | 2.2 | 2.3 | 8% |
| Raptor Strike | 1.2 | 1.3 | 1.8 | 1.7 | 1.9 | 9% |
| Auto Shot | 1.2 | 1.2 | 1.2 | 1.2 | 1.1 | 5% |
| Serpent Sting | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 17% |
| Bite | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 2% |
| Immolation Trap | 0.4 | 0.1 | 0.4 | 0.7 | 0.8 | 12% |
| Counterattack | 0.0 | 0.0 | 0.1 | 0.3 | 0.5 | 1% |
| Mongoose Bite | 0.0 | 0.0 | 0.1 | 0.3 | 0.5 | 2% |
| Mend Pet | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: hunter/talents/forever/optimizer/melee-dps-leveling-st.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
