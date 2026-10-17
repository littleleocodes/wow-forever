# Optimizer — Lightning Bolt 60%, Chain Lightning 15%, Earth Shock 10%, Flame Shock 8%, fire totem 7%; Lava Burst via talent (parse) — 30/8/13

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/8/13 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `elemental-dps` and profile `parse`: score +71.0% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Elemental (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Eye of the Storm** | 3/3 | changed | Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 70%. |
| **Elemental Reach** | 1/2 | **NEW** | Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 3 yards and reduces the cooldown of Totemic Projection by 10 sec. |
| **Lava Burst** | 1/1 | **NEW** | You hurl molten lava at the target, dealing 113 to 145 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 5/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 100%. |

### Enhancement (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ancestral Knowledge** | 3/5 | changed | Increases your Intellect by 6%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |

### Restoration (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |

## Core talents (priority order)

1. **Elemental Alacrity** — Removing it costs 29.1 points of score in this model.
2. **Elemental Fury** — Removing it costs 16.8 points of score in this model.
3. **Tidal Focus** — Removing it costs 8.9 points of score in this model.
4. **Concussion** — Removing it costs 6.7 points of score in this model.
5. **Thundering Strikes** — Removing it costs 6.7 points of score in this model.
6. **Call of Flame** — Removing it costs 6.0 points of score in this model.
7. **Lightning Overload** — Removing it costs 4.8 points of score in this model.
8. **Lava Burst** — Removing it costs 4.4 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: shaman/research/talents/forever/optimizer/elemental-dps-parse.md
- 2026-10-16 (repair_builds.py, client build 70425 trees): 31/7/13 -> 30/8/13; Call of Thunder 1 gone; refill +1 Ancestral Knowledge (refill: the elemental-dps model, raid-dps).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
