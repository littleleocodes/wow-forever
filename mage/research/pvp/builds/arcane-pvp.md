# Arcane — PvP (derived) — 31/0/20

*[Mage](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/0/20 (Arcane / Fire / Frost) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Arcane (model frost-leveling, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Arcane builds agree with (5513 builds).

## Point allocation

### Arcane (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 2/3 | changed | Increases your Armor by an amount equal to 50% of your Intellect. |
| **Improved Channeling** | 1/5 | **NEW** | Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Missile Barrage** | 1/2 | **NEW** | Gives your Arcane Blast spell a 20% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Geometry** | 2/2 | **NEW** | Increases the range of your Arcane spells by 6 yards. |
| **Arcane Impact** | 1/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 2%. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Shielding** | 1/2 | **NEW** | Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 17% and increases the resistances granted by your Mage Armor spell by 25%. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Improved Counterspell** | 2/2 | changed | Your Counterspell also Silences the target for 4 sec. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |

### Fire (0)

*No points.*

### Frost (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

## Core talents (priority order)

1. **Ice Lance** — The scorer's value in this build: +27.9% of its score (model frost-leveling).
2. **Shatter** — The scorer's value in this build: +16.8% of its score (model frost-leveling).
3. **Ice Shards** — The scorer's value in this build: +14.5% of its score (model frost-leveling).
4. **Frostbite** — The scorer's value in this build: +13.4% of its score (model frost-leveling).
5. **Arcane Power** — The scorer's value in this build: +6.7% of its score (model frost-leveling).
6. **Ice Block** — The scorer's value in this build: +6.3% of its score (model frost-leveling).

## Notes

- Community tie-break moves: 1 point Arcane Shielding -> Missile Barrage; 1 point Arcane Mind -> Arcane Blast; 1 point Arcane Mind -> Arcane Impact.
- Where we disagree with the community: most Arcane builds take Arcane Mind (96% take it), Incineration (71% take it), which the model values below this build's weakest point; this build takes Frostbite (15%), Ice Block (20%), Ice Lance (19%), Improved Frost Nova (19%), Shatter (14%), which few Arcane builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- No Arcane model exists: scored with the Frost leveling model, whose damage is mostly Frostbolt, so talents that raise Arcane spells are under-valued (leveling: the fight lab plays Frost's priority list).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 31/0/20 -> 31/0/20; Arcane Focus 5 gone; +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Wand Specialization (tier gating for Arcane Concentration); +1 Wand Specialization (tier gating for Arcane Concentration); +1 Improved Channeling (tier gating for Arcane Concentration); +1 Arcane Wrath (tier gating for Arcane Power) (refill: the frost-raid model, pvp).

## Open questions (verify in the live game)

- A derived Arcane PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
