# Optimizer — Lightning Bolt 60%, Chain Lightning 15%, Earth Shock 10%, Flame Shock 8%, fire totem 7%; Lava Burst via talent (leveling-st) — 30/12/9

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/12/9 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `elemental-dps` and profile `leveling-st`: score +33.5% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Elemental (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Earthbound** | 1/1 | **NEW** | Your Earthbind Totem Immobilizes nearby targets for 5 sec when cast. |
| **Eye of the Storm** | 3/3 | changed | Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 70%. |
| **Lava Burst** | 1/1 | **NEW** | You hurl molten lava at the target, dealing 113 to 145 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 5/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 100%. |

### Enhancement (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Earth's Grasp** | 1/2 | moved | Increases the health of your Stoneclaw Totem by 25% and the radius of your Earthbind Totem by 10%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Guardian Totems** | 2/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |
| **Anticipation** | 1/3 | changed | Increases your chance to dodge by an additional 2%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |

### Restoration (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |
| **Totemic Focus** | 1/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 5%. |

## Core talents (priority order)

1. **Mindfulness** — Removing it costs 3.0 points of score in this model.
2. **Improved Ghost Wolf** — Removing it costs 3.0 points of score in this model.
3. **Lava Burst** — Removing it costs 2.6 points of score in this model.
4. **Shamanistic Focus** — Removing it costs 1.9 points of score in this model.
5. **Thundering Strikes** — Removing it costs 1.9 points of score in this model.
6. **Convection** — Removing it costs 1.8 points of score in this model.
7. **Elemental Alacrity** — Removing it costs 1.8 points of score in this model.
8. **Call of Flame** — Removing it costs 1.8 points of score in this model.

## Leveling rotation (fight lab)

Elemental: Lightning Bolts from range (the pull and while the mob walks in), then Flame Shock, Earth Shock and Lava Burst on cooldown with Lightning Bolts between them while mana lasts; a bolt in melee eats pushback (Eye of the Storm resists it); the weapon swings whenever nothing is cast.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-09, on top of the priority below): eat below 80% health. Together +1.9% time per kill saved for `opt-elemental-dps-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/elemental-dps.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Lightning Bolt | 3.1 | 4.1 | 4.6 | 5.0 | 4.2 | 26% |
| Melee | 1.8 | 2.8 | 2.9 | 3.3 | 3.9 | 15% |
| Earth Shock | 0.3 | 0.8 | 1.0 | 1.2 | 1.3 | 11% |
| Windfury | 0.0 | 0.9 | 1.0 | 1.1 | 1.3 | 7% |
| Lava Burst | 0.0 | 0.0 | 0.0 | 0.0 | 1.2 | 10% |
| Flame Shock | 0.8 | 0.9 | 0.9 | 0.9 | 1.0 | 10% |
| Lightning Shield | 0.5 | 0.7 | 0.7 | 0.8 | 0.9 | 13% |
| Searing Totem | 0.8 | 0.9 | 0.8 | 0.8 | 0.8 | 8% |
| Stoneclaw Totem | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: shaman/research/talents/forever/optimizer/elemental-dps-leveling-st.md
- 2026-10-16 (repair_builds.py, client build 70425 trees): 31/12/8 -> 30/12/9; Call of Thunder 1 gone; +1 Tidal Focus (tier gating for Mindfulness); +1 Tidal Focus (tier gating for Mindfulness); +1 Tidal Focus (tier gating for Mindfulness); +1 Tidal Focus (tier gating for Mindfulness); +1 Tidal Focus (tier gating for Mindfulness); -1 Totemic Focus (over 51); -1 Totemic Focus (over 51); -1 Totemic Focus (over 51); -1 Totemic Focus (over 51); order dropped (order_repair.py) (refill: the elemental-dps model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
