# Optimizer — One slow weapon: white 40%, Windfury extra attacks 20%, Earth Shock 12%, Lightning Bolt 8%, Flame Shock 5%, Lightning Shield 5%, Rockbiter/other 10%; Stormstrike via talent (leveling-st) — 12/31/8

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 12/31/8 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `enhancement-dps` and profile `leveling-st`: score +43.0% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Elemental (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Call of Flame** | 1/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 5%, as well as increases the duration of your Flame Shock spell by 3 sec. |
| **Reverberation** | 5/5 | changed | Reduces the cooldown of your Shock spells by 1.0 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |

### Enhancement (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Earth's Grasp** | 2/2 | moved | Increases the health of your Stoneclaw Totem by 50% and the radius of your Earthbind Totem by 20%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Guardian Totems** | 2/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Improved Lightning Shield** | 3/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 15%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 150% of your Intellect. |
| **Anticipation** | 3/3 | changed | Increases your chance to dodge by an additional 6%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Flurry** | 5/5 | changed | Increases your attack speed by 30% for your next 3 swings after dealing a melee critical strike. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |
| **Stormstrike** | 1/1 | changed | Instantly strike for 150% normalized weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Maelstrom Weapon** | 1/5 | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 4%. Stacks up to 5 times. Lasts 30 sec. |
| **Rage of the Farseer** | 1/1 | **NEW** | Increases your attack speed by 30% for 25 sec. |

### Restoration (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |

## Core talents (priority order)

1. **Shamanistic Focus** — Removing it costs 6.6 points of score in this model.
2. **Stormstrike** — Removing it costs 6.3 points of score in this model.
3. **Improved Ghost Wolf** — Removing it costs 3.0 points of score in this model.
4. **Mental Dexterity** — Removing it costs 3.0 points of score in this model.
5. **Tidal Focus** — Removing it costs 2.7 points of score in this model.
6. **Thundering Strikes** — Removing it costs 2.0 points of score in this model.
7. **Mental Quickness** — Removing it costs 1.6 points of score in this model.
8. **Reverberation** — Removing it costs 1.3 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level with a slow two-hander: Lightning Shield (Water Shield when talented and mana is low) and the weapon imbue up (Rockbiter's attack power until 30, Windfury's extra attacks from 30), Searing Totem dropped at the pull, a Lightning Bolt while the mob walks in, then Stormstrike, Earth Shock (buffed by Stormstrike), Flame Shock while mana allows and instant Maelstrom Lightning Bolts between white swings; Stoneclaw Totem and a Lesser Healing Wave when low, Nature's Swiftness + Healing Wave in an emergency; a death with Reincarnation ready costs 30 s instead of 90. Between fights: 2 s loot, 6 s travel, heals back to 80% health, water below 35% mana.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-20, on top of the priority below): Lightning Bolt only when the mob is below 35% health; drink below 15% mana; eat below 80% health. Together +11.7% time per kill saved for `leveling-enhancement` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/enhancement-dps.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Melee | 3.5 | 3.5 | 4.2 | 4.8 | 5.7 | 25% |
| Windfury | 0.0 | 1.8 | 2.2 | 2.3 | 2.8 | 16% |
| Earth Shock | 2.1 | 2.0 | 2.3 | 2.5 | 2.7 | 27% |
| Stormstrike | 0.0 | 1.7 | 1.9 | 2.2 | 2.4 | 11% |
| Lightning Shield | 0.6 | 0.7 | 0.8 | 0.8 | 0.9 | 15% |
| Searing Totem | 0.7 | 0.7 | 0.6 | 0.7 | 0.6 | 5% |
| Lightning Bolt | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: shaman/research/talents/forever/optimizer/enhancement-dps-leveling-st.md
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 12/31/8 -> 12/31/8; order dropped: a moved talent breaks it (order_repair.py) (refill: the enhancement-dps model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
