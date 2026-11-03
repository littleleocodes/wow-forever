# Optimizer — Melee hunter (Forever): dual-wield white swings under Aspect of the Beast, Raptor Strike on the next swing, Mongoose Bite after dodges and Expose Prey procs, Strider Kick on cooldown, Counterattack after parries, the Lacerating Strikes bleed, one Serpent Sting from the pull (the 8 yd minimum range stops every other shot in melee), and the pet unless Lone Wolf (solo-60) — 15/10/26

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 15/10/26 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Solo/farming |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `melee-dps` and profile `solo-60`: score +42.5% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (15)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 1/5 | changed | Increases the Health and Armor of your pets by 3%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Revive Pet** | 2/2 | unchanged | Revive Pet's casting time is reduced by 6 sec, mana cost is reduced by 40%, and increases the health your pet returns with by an additional 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |

### Marksmanship (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |

### Survival (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 4/5 | unchanged | Increases your Parry chance by 4%. |
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Survivalist's Discipline** | 1/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 20%. |

## Core talents (priority order)

1. **Strider Kick** — Removing it costs 6.0 points of score in this model.
2. **Predator's Edge** — Removing it costs 5.0 points of score in this model.
3. **Resourcefulness** — Removing it costs 4.4 points of score in this model.
4. **Expose Prey** — Removing it costs 4.3 points of score in this model.
5. **Lethal Attacks** — Removing it costs 3.7 points of score in this model.
6. **Unleashed Fury** — Removing it costs 1.8 points of score in this model.
7. **Careful Aim** — Removing it costs 1.8 points of score in this model.
8. **Improved Tracking** — Removing it costs 1.3 points of score in this model.

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Report: hunter/research/talents/forever/optimizer/melee-dps-solo-60.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 15/10/26 -> 15/10/26; +1 Improved Revive Pet (tier gating for Pathfinding); +1 Endurance Training (tier gating for Pathfinding); -1 Pathfinding (over 51); -1 Pathfinding (over 51); order dropped (order_repair.py) (refill: the melee-dps model, solo-60).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
