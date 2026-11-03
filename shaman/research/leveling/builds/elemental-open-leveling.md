# Elemental — Leveling (open talent search) — 26/17/8

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 26/17/8 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the elemental-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (elemental-dps). +2.1% faster per kill than opt-elemental-dps-leveling-st, the fastest of our leveling builds in that race.

## Point allocation

### Elemental (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 3/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 3%. |
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt and Chain Lightning spells by 0.50 sec. |
| **Reverberation** | 3/5 | changed | Reduces the cooldown of your Shock spells by 0.6 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Eye of the Storm** | 3/3 | changed | Gives your Lightning Bolt and Chain Lightning spells a 70% chance to not lose casting time when you take damage. |
| **Elemental Reach** | 1/2 | **NEW** | Increases the range of your Lightning Bolt, Chain Lightning, and Fire Nova spells by 3 yards. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 30% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 1/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 20%. |

### Enhancement (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Guardian Totems** | 2/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Improved Lightning Shield** | 1/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 5%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 150% of your Intellect. |
| **Anticipation** | 3/3 | changed | Increases your chance to dodge by an additional 6%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |

### Restoration (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |

## Core talents (priority order)

1. **Shamanistic Focus** — +4.1 s per kill at level 60 without it (removal, 3,000 fights).
2. **Elemental Alacrity** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Mindfulness** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
4. **Convection** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Tidal Focus** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Thundering Strikes** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Call of Flame** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
8. **Elemental Focus** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 35.87; opt-elemental-dps-leveling-st 36.61. The search simulated 24,342 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 31/12/8 -> 26/17/8; Lava Burst 1 gone; +1 Guardian Totems (tier gating for Shamanistic Focus); +1 Guardian Totems (tier gating for Improved Ghost Wolf); +1 Anticipation (tier gating for Improved Ghost Wolf); +1 Anticipation (tier gating for Improved Ghost Wolf); +1 Anticipation (tier gating for Improved Ghost Wolf); -1 Elemental Fury (over 51); -1 Elemental Fury (over 51); -1 Elemental Fury (over 51); -1 Elemental Fury (over 51); order dropped (order_repair.py) (refill: the elemental-dps model, leveling-st).

## Open questions (verify in the live game)

- An open-search Elemental leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/shaman/60/530333100301135-050032101-053-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
