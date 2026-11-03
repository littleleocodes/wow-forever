# Optimizer — One slow weapon: white 40%, Windfury extra attacks 20%, Earth Shock 12%, Lightning Bolt 8%, Flame Shock 5%, Lightning Shield 5%, Rockbiter/other 10%; Stormstrike via talent (leveling-aoe) — 29/22/0

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/22/0 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `enhancement-dps` and profile `leveling-aoe`: score +53.6% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Elemental (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt and Chain Lightning spells by 0.50 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Elemental Warding** | 3/3 | changed | Reduces damage taken from Fire, Frost, and Nature effects by 10%. |
| **Trial by Fire** | 2/2 | **NEW** | Increases the damage done by your Fire Nova spell by 20% and reduces its cooldown by 4 sec, and increases the duration of your Magma Totem by 20 sec. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 30% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 4/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 80%. |

### Enhancement (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Earth's Grasp** | 1/2 | moved | Increases the health of your Stoneclaw Totem by 25% and the radius of your Earthbind Totem by 10%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Guardian Totems** | 2/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Improved Lightning Shield** | 3/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 15%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 150% of your Intellect. |
| **Anticipation** | 3/3 | changed | Increases your chance to dodge by an additional 6%. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |
| **Stormstrike** | 1/1 | changed | Instantly strike for 150% normalized weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |

### Restoration (0)

*No points.*

## Core talents (priority order)

1. **Call of Flame** — Removing it costs 13.9 points of score in this model.
2. **Thundering Strikes** — Removing it costs 3.2 points of score in this model.
3. **Mental Quickness** — Removing it costs 2.5 points of score in this model.
4. **Trial by Fire** — Removing it costs 2.5 points of score in this model.
5. **Mental Dexterity** — Removing it costs 2.3 points of score in this model.
6. **Tidal Focus** — Removing it costs 2.2 points of score in this model.
7. **Stormstrike** — Removing it costs 2.1 points of score in this model.
8. **Flurry** — Removing it costs 1.1 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level with a slow two-hander: Lightning Shield (Water Shield when talented and mana is low) and the weapon imbue up (Rockbiter's attack power until 30, Windfury's extra attacks from 30), Searing Totem dropped at the pull, a Lightning Bolt while the mob walks in, then Stormstrike, Earth Shock (buffed by Stormstrike), Flame Shock while mana allows and instant Maelstrom Lightning Bolts between white swings; Stoneclaw Totem and a Lesser Healing Wave when low, Nature's Swiftness + Healing Wave in an emergency; a death with Reincarnation ready costs 30 s instead of 90. Between fights: 2 s loot, 6 s travel, heals back to 80% health, water below 35% mana.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-20, on top of the priority below): Lightning Bolt only when the mob is below 35% health; drink below 15% mana; eat below 80% health. Together +11.7% time per kill saved for `leveling-enhancement` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/enhancement-dps-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Melee | 4.7 | 7.3 | 6.1 | 6.3 | 20% |
| Windfury | 1.6 | 3.2 | 2.7 | 2.6 | 10% |
| Stormstrike | 0.0 | 2.5 | 1.8 | 1.7 | 5% |
| Chain Lightning | 0.0 | 1.2 | 1.0 | 1.1 | 8% |
| Flame Shock | 1.4 | 1.1 | 1.1 | 1.0 | 9% |
| Fire Nova | 1.0 | 1.0 | 0.9 | 1.0 | 18% |
| Magma Totem | 0.7 | 0.5 | 0.5 | 0.5 | 23% |
| Lightning Shield | 0.4 | 0.5 | 0.5 | 0.5 | 7% |
| Stoneclaw Totem | 0.0 | 0.1 | 0.1 | 0.1 | 0% |
| Lightning Bolt | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Earth Shock | 0.4 | 0.0 | 0.0 | 0.0 | 0% |
| Lesser Healing Wave | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Allocation and order taken from cand-aoe-r9 on 2026-10-20: an earlier optimizer round beat the last export in the fight lab (54.1s vs 60.2s per kill, level-weighted).
- Report: shaman/research/talents/forever/optimizer/enhancement-dps-leveling-aoe.md
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 29/22/0 -> 29/22/0; order dropped: a moved talent breaks it (order_repair.py) (refill: the enhancement-dps model, leveling-aoe).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
