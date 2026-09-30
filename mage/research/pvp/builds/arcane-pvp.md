# Arcane — PvP (generated) — 31/0/20

*[Mage](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/0/20 (Arcane / Fire / Frost) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The best Arcane pvp build with at least 30 points in Arcane, generated on 2026-09-29 by spec_builds.py: the stats model's optimum (frost-leveling, profile pvp). No hand draft exists for this spec and mode yet; treat it as a starting point.

## Point allocation

### Arcane (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Resilience** | 1/2 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |
| **Arcane Geometry** | 2/2 | **NEW** | Increases the range of your Arcane spells by 6 yards. |
| **Arcane Shielding** | 2/2 | **NEW** | Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 33% and increases the resistances granted by your Mage Armor spell by 50%. |
| **Improved Counterspell** | 2/2 | changed | Your Counterspell also Silences the target for 4 sec. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 2/5 | changed | Increases your Intellect by 4% and increases the critical strike damage bonus of your Arcane spells by 40%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |

### Fire (0)

*No points.*

### Frost (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

## Core talents (priority order)

1. **Ice Lance** — The scorer's value in this build: +27.7% of its score (model frost-leveling).
2. **Shatter** — The scorer's value in this build: +16.7% of its score (model frost-leveling).
3. **Ice Shards** — The scorer's value in this build: +14.4% of its score (model frost-leveling).
4. **Frostbite** — The scorer's value in this build: +13.3% of its score (model frost-leveling).
5. **Arcane Power** — The scorer's value in this build: +6.7% of its score (model frost-leveling).
6. **Ice Block** — The scorer's value in this build: +6.3% of its score (model frost-leveling).

## Notes

- Generated 2026-09-29 (spec_builds.py) so every spec has a pvp build; model frost-leveling, profile pvp. PvP values are assumptions: no simulator plays PvP.
- No Arcane model exists: scored with the Frost leveling model, whose damage is mostly Frostbolt, so talents that raise Arcane spells are under-valued (leveling: the fight lab plays Frost's priority list).

## Open questions (verify in the live game)

- A generated Arcane build: check it against the community's Arcane builds at launch.

## Sources

- <https://talentsforever.com/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
