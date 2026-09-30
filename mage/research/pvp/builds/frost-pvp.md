# Frost — PvP (derived) — 18/0/33

*[Mage](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/0/33 (Arcane / Fire / Frost) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Frost (model frost-leveling, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Frost builds agree with (9200 builds).

## Point allocation

### Arcane (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Concentration** | 3/5 | unchanged | Gives you a 6% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Resilience** | 1/2 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |
| **Arcane Geometry** | 2/2 | **NEW** | Increases the range of your Arcane spells by 6 yards. |
| **Improved Counterspell** | 2/2 | changed | Your Counterspell also Silences the target for 4 sec. |
| **Missile Barrage** | 1/1 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |

### Fire (0)

*No points.*

### Frost (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 1/3 | moved | Reduces the mana cost of your Frost spells by 5% and reduces the threat caused by your Frost spells by 10%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Ice Barrier** | 1/1 | changed | Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage. |

## Core talents (priority order)

1. **Ice Lance** — The scorer's value in this build: +23.0% of its score (model frost-leveling).
2. **Shatter** — The scorer's value in this build: +19.3% of its score (model frost-leveling).
3. **Ice Barrier** — The scorer's value in this build: +14.6% of its score (model frost-leveling).
4. **Ice Shards** — The scorer's value in this build: +11.9% of its score (model frost-leveling).
5. **Frostbite** — The scorer's value in this build: +11.0% of its score (model frost-leveling).
6. **Fingers of Frost** — The scorer's value in this build: +10.0% of its score (model frost-leveling).

## Notes

- Scores +13.3% of the optimum's talent value above the hand draft pvp-frost, over the 2% replacement bar: this build is the spec's PvP pick, the hand draft stays as the alternative.
- Community tie-break moves: 1 point Elemental Precision -> Missile Barrage; 1 point Elemental Precision -> Frost Channeling.
- Where we disagree with the community: most Frost builds take none, which the model values below this build's weakest point; this build takes none, which few Frost builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.

## Open questions (verify in the live game)

- A derived Frost PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
