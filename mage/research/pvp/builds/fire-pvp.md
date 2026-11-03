# Fire — PvP (derived) — 0/32/19

*[Mage](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/32/19 (Arcane / Fire / Frost) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fire PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Fire (model fire-leveling, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Fire builds agree with (6135 builds).

## Point allocation

### Arcane (0)

*No points.*

### Fire (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Flame Throwing** | 2/2 | unchanged | Increases the range of your Fire spells by 6 yards. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Impact** | 3/3 | changed | Gives your Fire spells a 10% chance to stun the target for 2 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 2/3 | changed | Your Scorch spell has a 67% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Blast Wave** | 1/1 | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 1/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 20%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

## Core talents (priority order)

1. **Ice Lance** — The scorer's value in this build: +39.2% of its score (model fire-leveling).
2. **Ignite** — The scorer's value in this build: +13.0% of its score (model fire-leveling).
3. **Fire Power** — The scorer's value in this build: +7.0% of its score (model fire-leveling).
4. **Combustion** — The scorer's value in this build: +6.9% of its score (model fire-leveling).
5. **Ice Block** — The scorer's value in this build: +6.4% of its score (model fire-leveling).
6. **Shatter** — The scorer's value in this build: +6.0% of its score (model fire-leveling).

## Notes

- Community tie-break moves: 1 point Arctic Reach -> Improved Scorch; 1 point Frost Warding -> Ice Shards; 2 points Improved Fireball -> Wake of Fire.
- Where we disagree with the community: most Fire builds take Master of Elements (83% take it), which the model values below this build's weakest point; this build takes Frostbite (11%), Improved Frost Nova (13%), Permafrost (7%), which few Fire builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Hot Streak 1 out; Heating Up 1 in; to be re-optimized.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 0/32/19 -> 0/32/19; Wake of Fire -> Improved Fire Blast (renamed); Fire Power 5 -> 3 (rank cap); +1 Improved Fireball (tier gating for Combustion); +1 Critical Mass (prerequisite of Combustion); +1 Critical Mass (prerequisite of Combustion); -1 Heating Up (over 51) (refill: the fire-raid model, pvp).
- 2026-10-22 (repair_builds.py, client build 70425 trees): 0/32/19 -> 0/32/19; Elemental Precision 5 -> 3 (rank cap); +1 Frost Warding (tier gating for Frostbite); +1 Frost Warding (tier gating for Frostbite) (refill: the fire-raid model, pvp).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 0/32/19 -> 0/32/19; Improved Fireball -> Accelerant (renamed); Critical Mass 5 -> 3 (rank cap); Elemental Precision -> Precision (renamed); +1 Accelerant (tier gating for Flame Throwing); refill +1 Heating Up (refill: the fire-raid model, pvp).

## Open questions (verify in the live game)

- A derived Fire PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
