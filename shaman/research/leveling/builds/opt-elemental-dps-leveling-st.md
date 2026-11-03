# Optimizer — Lightning Bolt 60%, Chain Lightning 15%, Earth Shock 10%, Flame Shock 8%, fire totem 7%; Lava Burst via talent (leveling-st) — 26/17/8

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 26/17/8 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `elemental-dps` and profile `leveling-st`: score +38.9% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Elemental (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt and Chain Lightning spells by 0.50 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Earthbound** | 1/1 | **NEW** | Your Earthbind Totem Immobilizes nearby targets for 5 sec when cast. |
| **Eye of the Storm** | 3/3 | changed | Gives your Lightning Bolt and Chain Lightning spells a 70% chance to not lose casting time when you take damage. |
| **Call of Thunder** | 1/1 | changed | Increases critical strike chance of Lightning Bolt and Chain Lightning by 5%. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 30% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 1/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 20%. |

### Enhancement (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ancestral Knowledge** | 2/5 | changed | Increases your Intellect by 4%. |
| **Earth's Grasp** | 2/2 | moved | Increases the health of your Stoneclaw Totem by 50% and the radius of your Earthbind Totem by 20%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Guardian Totems** | 2/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Anticipation** | 3/3 | changed | Increases your chance to dodge by an additional 6%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |

### Restoration (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |

## Core talents (priority order)

1. **Improved Ghost Wolf** — Removing it costs 3.0 points of score in this model.
2. **Mindfulness** — Removing it costs 3.0 points of score in this model.
3. **Elemental Alacrity** — Removing it costs 2.8 points of score in this model.
4. **Lava Burst** — Removing it costs 2.7 points of score in this model.
5. **Tidal Focus** — Removing it costs 2.4 points of score in this model.
6. **Elemental Fury** — Removing it costs 2.1 points of score in this model.
7. **Thundering Strikes** — Removing it costs 2.0 points of score in this model.
8. **Shamanistic Focus** — Removing it costs 1.9 points of score in this model.

## Leveling rotation (fight lab)

Elemental: Lightning Mastery on a fresh mob when ready, Lightning Bolts from range (the pull and while the mob walks in), then Flame Shock and Earth Shock on cooldown with Lightning Bolts between them while mana lasts (Chain Lightning on a single mob only as CL_SINGLE allows); a bolt in melee eats pushback (Eye of the Storm resists it); the weapon swings whenever nothing is cast. Lava Burst left the game on 2026-11-02 (it was cast on cooldown here).

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-20, on top of the priority below): drink below 15% mana; eat below 80% health. Together +1.2% time per kill saved for `opt-elemental-dps-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/elemental-dps.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Lightning Bolt | 3.5 | 4.8 | 4.8 | 4.4 | 4.4 | 34% |
| Melee | 1.4 | 2.1 | 2.1 | 2.1 | 2.5 | 9% |
| Earth Shock | 0.7 | 1.1 | 1.1 | 1.0 | 1.1 | 11% |
| Lava Burst | 0.0 | 0.0 | 0.0 | 0.9 | 1.0 | 11% |
| Flame Shock | 0.8 | 0.8 | 0.9 | 0.9 | 0.9 | 11% |
| Windfury | 0.0 | 0.7 | 0.7 | 0.8 | 0.9 | 4% |
| Lightning Shield | 0.6 | 0.7 | 0.8 | 0.8 | 0.8 | 14% |
| Searing Totem | 0.7 | 0.6 | 0.6 | 0.7 | 0.7 | 6% |
| Elemental Mastery | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 0% |
| Stoneclaw Totem | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: shaman/research/talents/forever/optimizer/elemental-dps-leveling-st.md
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 31/12/8 -> 26/17/8; Lava Burst 1 gone; Elemental Mastery -> Lightning Mastery (renamed); +1 Earth's Grasp (tier gating for Anticipation); +1 Ancestral Knowledge (tier gating for Anticipation); +1 Anticipation (tier gating for Improved Ghost Wolf); +1 Anticipation (tier gating for Improved Ghost Wolf); +1 Ancestral Knowledge (tier gating for Improved Ghost Wolf); +1 Call of Thunder (tier gating for Elemental Fury); -1 Lightning Mastery (over 51); -1 Elemental Fury (over 51); -1 Elemental Fury (over 51); -1 Elemental Fury (over 51); -1 Elemental Fury (over 51); order dropped (order_repair.py) (refill: the elemental-dps model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
