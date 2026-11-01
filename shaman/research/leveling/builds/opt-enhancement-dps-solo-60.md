# Optimizer — One slow weapon: white 40%, Windfury extra attacks 20%, Earth Shock 12%, Lightning Bolt 8%, Flame Shock 5%, Lightning Shield 5%, Rockbiter/other 10%; Stormstrike via talent (solo-60) — 12/31/8

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 12/31/8 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Solo/farming |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `enhancement-dps` and profile `solo-60`: score +43.1% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Elemental (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Reverberation** | 5/5 | changed | Reduces the cooldown of your Shock spells by 1.0 sec. |
| **Call of Flame** | 1/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 5%, as well as increases the duration of your Flame Shock spell by 3 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |

### Enhancement (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Earth's Grasp** | 2/2 | moved | Increases the health of your Stoneclaw Totem by 50% and the radius of your Earthbind Totem by 20%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |
| **Improved Lightning Shield** | 3/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 15%. |
| **Guardian Totems** | 2/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Anticipation** | 3/3 | changed | Increases your chance to dodge by an additional 6%. |
| **Stormstrike** | 1/1 | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Flurry** | 5/5 | changed | Increases your attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Maelstrom Weapon** | 1/5 | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 4%. Stacks up to 5 times. Lasts 30 sec. |
| **Rage of the Farseer** | 1/1 | **NEW** | Increases your attack speed by 30% for 25 sec. |

### Restoration (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Enhancement | Thundering Strikes | 5 | 0/5/0 |
| 15-17 | Enhancement | Mental Dexterity | 3 | 0/8/0 |
| 18-19 | Enhancement | Improved Ghost Wolf | 2 | 0/10/0 |
| 20 | Enhancement | Shamanistic Focus | 1 | 0/11/0 |
| 21-23 | Enhancement | Improved Lightning Shield | 3 | 0/14/0 |
| 24 | Enhancement | Guardian Totems | 1 | 0/15/0 |
| 25 | Enhancement | Stormstrike | 1 | 0/16/0 |
| 26-30 | Restoration | Tidal Focus | 5 | 0/16/5 |
| 31 | Enhancement | Guardian Totems | 1 | 0/17/5 |
| 32-34 | Enhancement | Flurry | 3 | 0/20/5 |
| 35-36 | Enhancement | Mental Quickness | 2 | 0/22/5 |
| 37-39 | Restoration | Mindfulness | 3 | 0/22/8 |
| 40-41 | Enhancement | Flurry | 2 | 0/24/8 |
| 42-46 | Elemental | Concussion | 5 | 5/24/8 |
| 47-51 | Elemental | Reverberation | 5 | 10/24/8 |
| 52 | Elemental | Elemental Focus | 1 | 11/24/8 |
| 53-54 | Enhancement | Earth's Grasp | 2 | 11/26/8 |
| 55-57 | Enhancement | Anticipation | 3 | 11/29/8 |
| 58 | Enhancement | Maelstrom Weapon | 1 | 11/30/8 |
| 59 | Enhancement | Rage of the Farseer | 1 | 11/31/8 |
| 60 | Elemental | Call of Flame | 1 | 12/31/8 |

## Core talents (priority order)

1. **Stormstrike** — Removing it costs 6.7 points of score in this model.
2. **Shamanistic Focus** — Removing it costs 6.6 points of score in this model.
3. **Improved Ghost Wolf** — Removing it costs 3.0 points of score in this model.
4. **Mental Dexterity** — Removing it costs 3.0 points of score in this model.
5. **Tidal Focus** — Removing it costs 2.8 points of score in this model.
6. **Thundering Strikes** — Removing it costs 1.8 points of score in this model.
7. **Mental Quickness** — Removing it costs 1.5 points of score in this model.
8. **Reverberation** — Removing it costs 1.3 points of score in this model.

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Report: shaman/research/talents/forever/optimizer/enhancement-dps-solo-60.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
