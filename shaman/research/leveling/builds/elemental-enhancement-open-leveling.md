# Elemental-Enhancement — Leveling (open talent search) — 21/22/8

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/22/8 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental-Enhancement (an Elemental/Enhancement hybrid) leveling build the open leveling search found on 2026-10-10: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the elemental-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (elemental-dps). -0.3% faster per kill than elemental-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Elemental (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Elemental Devastation** | 1/3 | changed | Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 3% for 10 sec. |
| **Reverberation** | 2/5 | changed | Reduces the cooldown of your Shock spells by 0.4 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Lightning Overload** | 1/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 3% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |

### Enhancement (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Improved Lightning Shield** | 3/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 15%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Flurry** | 1/5 | changed | Increases your attack speed by 5% for your next 3 swings after dealing a melee critical strike. |
| **Toughness** | 2/5 | changed | Increases your Stamina by 4%. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |

### Restoration (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 2/3 | **NEW** | Allows 33% of your Mana regeneration to continue while casting. |
| **Totemic Focus** | 1/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 5%. |

## Core talents (priority order)

1. **Shamanistic Focus** — +5.2 s per kill at level 60 without it (removal, 3,000 fights).
2. **Mental Quickness** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
3. **Elemental Alacrity** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Thundering Strikes** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Convection** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Mindfulness** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Elemental Focus** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Call of Flame** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 38.16; elemental-open-leveling 38.04, opt-elemental-dps-leveling-st 39.20. The search simulated 30,700 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 22/22/7 -> 21/22/8; Call of Thunder 1 gone; +1 Tidal Focus (tier gating for Mindfulness); +1 Tidal Focus (tier gating for Mindfulness); +1 Tidal Focus (tier gating for Mindfulness); +1 Tidal Focus (tier gating for Mindfulness); +1 Tidal Focus (tier gating for Mindfulness); -1 Totemic Focus (over 51); -1 Totemic Focus (over 51); -1 Totemic Focus (over 51); -1 Totemic Focus (over 51); order dropped (order_repair.py) (refill: the elemental-dps model, leveling-st).

## Open questions (verify in the live game)

- An open-search Elemental-Enhancement leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/shaman/60/5502311300101-055030301021002-052-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
