# Fire — PvP (derived) — 0/32/19

*[Mage](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/32/19 (Arcane / Fire / Frost) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fire PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Fire (model fire-leveling, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Fire builds agree with (6135 builds).

## Point allocation

### Arcane (0)

*No points.*

### Fire (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wake of Fire** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec. Killing a non-trivial target increases the critical strike chance of your next Fire Blast cast within 30 sec by 50%. |
| **Improved Fireball** | 3/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.3 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Flame Throwing** | 2/2 | unchanged | Increases the range of your Fire spells by 6 yards. |
| **Impact** | 3/3 | changed | Gives your Fire spells a 10% chance to stun the target for 2 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Scorch** | 2/3 | changed | Your Scorch spell has a 67% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Hot Streak** | 1/1 | **NEW** | Your non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch grant Hot Streak for 20 sec. Hot Streak reduces the cast time of Pyroblast by 25%, stacking up to 3 times. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Blast Wave** | 1/1 | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. |
| **Fire Power** | 5/5 | unchanged | Increases the damage done by your Fire spells by 10%. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 4 non-periodic critical strikes with Fire spells. |

### Frost (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 1/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 20%. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
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

## Open questions (verify in the live game)

- A derived Fire PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
