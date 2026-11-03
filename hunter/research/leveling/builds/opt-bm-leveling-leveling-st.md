# Optimizer — Pet-first leveling (leveling-st) — 20/31/0

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/31/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `bm-leveling` and profile `leveling-st`: score +27.3% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |

### Marksmanship (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |
| **Barrage** | 1/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 5%. |
| **Rapid Recuperation** | 2/2 | **NEW** | Afflicting a target with Serpent Sting allows 50% of your Mana Regeneration to continue while casting for 15 sec, increased to 100% when Rapid Killing is consumed. |
| **Scatter Shot** | 1/1 | moved | A short-range shot that deals 50% weapon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |
| **Sniper Shot** | 1/1 | **NEW** | A long-range shot that deals ranged damage plus 160 and increases the range of your next 3 Shots by 10 yards for 10 sec. |

### Survival (0)

*No points.*

## Core talents (priority order)

1. **Unleashed Fury** — Removing it costs 3.5 points of score in this model.
2. **Sniper Shot** — Removing it costs 2.7 points of score in this model.
3. **Efficiency** — Removing it costs 2.5 points of score in this model.
4. **Ranged Weapon Specialization** — Removing it costs 2.3 points of score in this model.
5. **Deadly Aspects** — Removing it costs 1.7 points of score in this model.
6. **Ferocity** — Removing it costs 1.6 points of score in this model.
7. **Rapid Recuperation** — Removing it costs 1.5 points of score in this model.
8. **Improved Stings** — Removing it costs 1.3 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level with a cat: the pet runs in and meets the mob halfway, Growls every 5 s and holds it until your threat passes 130% of its own. You shoot from 35 yd: Hunter's Mark, Serpent Sting, Summon Hawk or Arcane Shot, Multi-Shot / Aimed Shot on their shared cooldown, Auto Shot in between (the bow cannot fire inside 8 yd); Bestial Wrath, Intimidation and Rapid Fire on the pull when ready; Mend Pet when the pet drops below 35%; Feign Death, Wing Clip and Raptor Strike when a mob reaches you. Between fights: 2 s loot, 6 s travel, Mend Pet below 70% pet health, water below 35% mana, food below 65% health, a 10 s Revive Pet after a pet death; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-11-02, on top of the priority below): never cast Multi-Shot; never cast Arcane Shot; drink below 15% mana. Together +8.3% time per kill saved for `opt-mm-raid-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/mm-raid.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Auto Shot | 2.7 | 4.0 | 5.6 | 6.5 | 7.0 | 37% |
| Claw | 3.6 | 4.6 | 5.4 | 5.8 | 6.3 | 8% |
| Growl | 1.1 | 1.8 | 2.5 | 2.9 | 3.2 | 0% |
| Bite | 1.0 | 1.0 | 1.5 | 1.7 | 1.9 | 4% |
| Aimed Shot | 0.9 | 1.0 | 1.2 | 1.5 | 1.6 | 14% |
| Serpent Sting | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 16% |
| Hunter's Mark | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0% |
| Feign Death | 0.0 | 0.1 | 0.1 | 0.1 | 0.2 | 0% |
| Melee | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Wing Clip | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Raptor Strike | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Mongoose Bite | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: hunter/research/talents/forever/optimizer/bm-leveling-leveling-st.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 20/31/0 -> 20/31/0; +1 Endurance Training (tier gating for Pathfinding); +1 Endurance Training (tier gating for Pathfinding); -1 Pathfinding (over 51); -1 Pathfinding (over 51); order dropped (order_repair.py) (refill: the bm-leveling model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
