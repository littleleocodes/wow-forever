# Optimizer — Marksmanship raid DPS with a pet (Classic 20/31/0 style) (leveling-st) — 13/33/5

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 13/33/5 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `mm-raid` and profile `leveling-st`: score +26.8% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 1/5 | changed | Increases the Health and Armor of your pets by 3%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Revive Pet** | 2/2 | unchanged | Revive Pet's casting time is reduced by 6 sec, mana cost is reduced by 40%, and increases the health your pet returns with by an additional 30%. |
| **Bestial Swiftness** | 1/1 | changed | Increases the movement speed of your pets by 30%. |
| **Pathfinding** | 2/2 | moved | Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 6%. |

### Marksmanship (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Mortal Shots** | 1/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 6%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |
| **Barrage** | 2/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%. |
| **Rapid Recuperation** | 2/2 | **NEW** | Afflicting a target with Serpent Sting allows 50% of your Mana Regeneration to continue while casting for 15 sec, increased to 100% when Rapid Killing is consumed. |
| **Scatter Shot** | 1/1 | moved | A short-range shot that deals 50% weapon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |
| **Sniper Shot** | 1/1 | **NEW** | A long-range shot that deals ranged damage plus 160 and increases the range of your next 3 Shots by 10 yards for 10 sec. |

### Survival (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |

## Core talents (priority order)

1. **Careful Aim** — Removing it costs 2.7 points of score in this model.
2. **Deadly Aspects** — Removing it costs 2.3 points of score in this model.
3. **Sniper Shot** — Removing it costs 1.9 points of score in this model.
4. **Ranged Weapon Specialization** — Removing it costs 1.9 points of score in this model.
5. **Improved Tracking** — Removing it costs 1.9 points of score in this model.
6. **Efficiency** — Removing it costs 1.9 points of score in this model.
7. **Improved Stings** — Removing it costs 1.7 points of score in this model.
8. **Trueshot Aura** — Removing it costs 1.6 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level with a cat: the pet runs in and meets the mob halfway, Growls every 5 s and holds it until your threat passes 130% of its own. You shoot from 35 yd: Hunter's Mark, Serpent Sting, Summon Hawk or Arcane Shot, Multi-Shot / Aimed Shot on their shared cooldown, Auto Shot in between (the bow cannot fire inside 8 yd); Bestial Wrath, Intimidation and Rapid Fire on the pull when ready; Mend Pet when the pet drops below 35%; Feign Death, Wing Clip and Raptor Strike when a mob reaches you. Between fights: 2 s loot, 6 s travel, Mend Pet below 70% pet health, water below 35% mana, food below 65% health, a 10 s Revive Pet after a pet death; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-11-03, on top of the priority below): never cast Multi-Shot; Arcane Shot only when the mob is below 35% health; Feign Death only while the mob has more than 35% health; drink below 15% mana. Together +6.1% time per kill saved for `opt-mm-raid-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/mm-raid.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Auto Shot | 2.9 | 4.3 | 5.9 | 6.7 | 6.9 | 38% |
| Claw | 3.7 | 4.6 | 5.4 | 5.8 | 6.6 | 7% |
| Growl | 1.2 | 1.8 | 2.6 | 2.9 | 3.2 | 0% |
| Bite | 1.0 | 1.0 | 1.6 | 1.8 | 1.9 | 3% |
| Aimed Shot | 0.9 | 1.0 | 1.3 | 1.5 | 1.6 | 15% |
| Serpent Sting | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 17% |
| Hunter's Mark | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0% |
| Feign Death | 0.0 | 0.2 | 0.2 | 0.2 | 0.4 | 0% |
| Melee | 0.0 | 0.0 | 0.0 | 0.1 | 0.3 | 1% |
| Wing Clip | 0.0 | 0.0 | 0.0 | 0.1 | 0.2 | 0% |
| Raptor Strike | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | 1% |
| Mongoose Bite | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | 0% |
| Mend Pet | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: hunter/research/talents/forever/optimizer/mm-raid-leveling-st.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 12/34/5 -> 13/33/5; +1 Endurance Training (tier gating for Bestial Swiftness); -1 Mortal Shots (over 51); order dropped (order_repair.py) (refill: the mm-raid model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
