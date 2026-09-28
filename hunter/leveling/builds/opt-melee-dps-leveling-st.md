# Optimizer — Melee hunter (Forever): dual-wield white swings under Aspect of the Beast, Raptor Strike on the next swing, Mongoose Bite after dodges and Expose Prey procs, Strider Kick on cooldown, Counterattack after parries, the Lacerating Strikes bleed, one Serpent Sting from the pull (the 8 yd minimum range stops every other shot in melee), and the pet unless Lone Wolf (leveling-st) — 7/13/31

*[Hunter](../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/13/31 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `melee-dps` and profile `leveling-st`: score +42.5% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |

### Marksmanship (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increased the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |

### Survival (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 4/5 | changed | Increases your Parry chance by 8%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee critical strike damage by 30% and your offhand weapon damage by 50%. |
| **Counterattack** | 1/1 | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the mana cost of your Trap abilities and melee abilities by 60%. In addition, your critical strikes have a 60% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 5 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 15%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Survival | Improved Tracking | 5 | 0/0/5 |
| 15-16 | Survival | Savage Strikes | 2 | 0/0/7 |
| 17-19 | Survival | Deflection | 3 | 0/0/10 |
| 20-22 | Survival | Surefooted | 3 | 0/0/13 |
| 23 | Survival | Deterrence | 1 | 0/0/14 |
| 24 | Survival | Deflection | 1 | 0/0/15 |
| 25-29 | Survival | Predator's Edge | 5 | 0/0/20 |
| 30 | Survival | Strider Kick | 1 | 0/0/21 |
| 31-32 | Survival | Resourcefulness | 2 | 0/0/23 |
| 33-35 | Marksmanship | Lethal Attacks | 3 | 0/3/23 |
| 36 | Survival | Counterattack | 1 | 0/3/24 |
| 37-38 | Marksmanship | Lethal Attacks | 2 | 0/5/24 |
| 39-40 | Survival | Expose Prey | 2 | 0/5/26 |
| 41-43 | Marksmanship | Improved Stings | 3 | 0/8/26 |
| 44-48 | Survival | Lightning Reflexes | 5 | 0/8/31 |
| 49-53 | Marksmanship | Careful Aim | 5 | 0/13/31 |
| 54-58 | Beast Mastery | Deadly Aspects | 5 | 5/13/31 |
| 59-60 | Beast Mastery | Focused Fire | 2 | 7/13/31 |

## Core talents (priority order)

1. **Strider Kick** — Removing it costs 7.0 points of score in this model.
2. **Predator's Edge** — Removing it costs 4.3 points of score in this model.
3. **Resourcefulness** — Removing it costs 3.9 points of score in this model.
4. **Lethal Attacks** — Removing it costs 3.5 points of score in this model.
5. **Lightning Reflexes** — Removing it costs 2.1 points of score in this model.
6. **Careful Aim** — Removing it costs 2.0 points of score in this model.
7. **Improved Tracking** — Removing it costs 1.7 points of score in this model.
8. **Surefooted** — Removing it costs 1.4 points of score in this model.

## Leveling rotation (fight lab)

The melee hunter: mark and sting from range, then stand and fight: Counterattack after a parry, Mongoose Bite when a dodge or Expose Prey activates it, Strider Kick on cooldown, Raptor Strike on the next swing; Deterrence when low; Mend Pet for the pet.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-09-28, on top of the priority below): never cast Hunter's Mark. Together +3.4% time per kill saved for `leveling-melee` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/melee-dps-opt.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Melee (off-hand) | 3.2 | 4.3 | 6.2 | 6.6 | 7.6 | 14% |
| Claw | 3.6 | 4.3 | 5.1 | 5.3 | 5.7 | 6% |
| Melee | 1.8 | 2.9 | 4.2 | 4.5 | 5.4 | 15% |
| Growl | 1.9 | 2.5 | 3.4 | 3.7 | 4.0 | 0% |
| Strider Kick | 0.0 | 1.8 | 2.4 | 2.5 | 2.7 | 10% |
| Raptor Strike | 1.4 | 1.4 | 2.0 | 2.1 | 2.3 | 12% |
| Auto Shot | 1.2 | 1.2 | 1.2 | 1.1 | 1.1 | 6% |
| Serpent Sting | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 17% |
| Bite | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 2% |
| Mongoose Bite | 0.0 | 0.0 | 0.1 | 0.2 | 0.5 | 2% |
| Counterattack | 0.0 | 0.0 | 0.1 | 0.2 | 0.4 | 1% |
| Mend Pet | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: hunter/talents/forever/optimizer/melee-dps-leveling-st.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
