# Frost — PvP (derived) — 19/0/32

*[Mage](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 19/0/32 (Arcane / Fire / Frost) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Frost (model frost-leveling, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Frost builds agree with (9200 builds).

## Point allocation

### Arcane (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 2/3 | changed | Increases your Armor by an amount equal to 50% of your Intellect. |
| **Improved Channeling** | 1/5 | **NEW** | Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Concentration** | 3/5 | unchanged | Gives you a 6% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, Frost Blast, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Geometry** | 2/2 | **NEW** | Increases the range of your Arcane spells by 6 yards. |
| **Arcane Shielding** | 1/2 | **NEW** | Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 17% and increases the resistances granted by your Mage Armor spell by 25%. |
| **Improved Counterspell** | 2/2 | changed | Your Counterspell also Silences the target for 4 sec. |

### Fire (0)

*No points.*

### Frost (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Frost Channeling** | 1/3 | moved | Reduces the mana cost of your Frost spells by 5% and reduces the threat caused by your Frost spells by 10%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Ice Barrier** | 1/1 | changed | Shield yourself, absorbing 447 damage and increasing your Frost damage by 15% for 1 min. While shielded, your Frost damage is increased by an additional 5% and you do not lose casting time when you take damage. |

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
- 2026-10-22 (repair_builds.py, client build 70425 trees): 18/0/33 -> 19/0/32; Piercing Ice 3 gone; +1 Elemental Precision (tier gating for Ice Barrier); refill +1 Missile Barrage, +1 Elemental Precision (refill: the frost-raid model, pvp).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 19/0/32 -> 19/0/32; Arcane Focus 5 gone; Elemental Precision -> Precision (renamed); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Wand Specialization (tier gating for Arcane Concentration); +1 Wand Specialization (tier gating for Arcane Concentration); +1 Improved Channeling (tier gating for Arcane Concentration); refill +1 Arcane Shielding (refill: the frost-raid model, pvp).

## Open questions (verify in the live game)

- A derived Frost PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
