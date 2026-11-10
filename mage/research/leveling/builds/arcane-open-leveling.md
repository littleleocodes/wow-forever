# Arcane — Leveling (open talent search) — 31/0/20

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/0/20 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane leveling build the open leveling search found on 2026-11-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the arcane-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). -0.1% faster per kill than arcane-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage. |
| **Arcane Resilience** | 1/3 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |

### Fire (0)

*No points.*

### Frost (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Improved Frostbolt** | 3/5 | changed | Reduces the casting time of your Frostbolt spell by 0.3 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Ice Shards** | 3/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 60%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 2/3 | changed | Increases the duration of your Chill effects by 22% and reduces the target's speed by an additional 7%. |
| **Improved Blizzard** | 2/3 | changed | Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 25% for 1.5 sec. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10 | Arcane | Arcane Resilience | 1 | 1/0/0 |
| 11-14 | Arcane | Improved Channeling | 4 | 5/0/0 |
| 15-19 | Arcane | Arcane Concentration | 5 | 10/0/0 |
| 20 | Arcane | Arcane Blast | 1 | 11/0/0 |
| 21-22 | Arcane | Missile Barrage | 2 | 13/0/0 |
| 23 | Arcane | Improved Channeling | 1 | 14/0/0 |
| 24 | Arcane | Arcane Impact | 1 | 15/0/0 |
| 25 | Arcane | Arcane Wrath | 1 | 16/0/0 |
| 26-28 | Arcane | Arcane Meditation | 3 | 19/0/0 |
| 29 | Arcane | Arcane Impact | 1 | 20/0/0 |
| 30 | Arcane | Presence of Mind | 1 | 21/0/0 |
| 31 | Arcane | Arcane Impact | 1 | 22/0/0 |
| 32-34 | Arcane | Arcane Mind | 3 | 25/0/0 |
| 35-37 | Arcane | Arcane Instability | 3 | 28/0/0 |
| 38-39 | Arcane | Arcane Mind | 2 | 30/0/0 |
| 40-41 | Frost | Precision | 2 | 30/0/2 |
| 42-44 | Frost | Improved Frostbolt | 3 | 30/0/5 |
| 45-47 | Frost | Ice Shards | 3 | 30/0/8 |
| 48 | Frost | Improved Frost Nova | 1 | 30/0/9 |
| 49 | Frost | Frost Warding | 1 | 30/0/10 |
| 50 | Frost | Ice Lance | 1 | 30/0/11 |
| 51 | Frost | Frost Warding | 1 | 30/0/12 |
| 52-53 | Frost | Improved Blizzard | 2 | 30/0/14 |
| 54 | Frost | Improved Frost Nova | 1 | 30/0/15 |
| 55-56 | Frost | Shatter | 2 | 30/0/17 |
| 57-58 | Frost | Permafrost | 2 | 30/0/19 |
| 59 | Arcane | Arcane Power | 1 | 31/0/19 |
| 60 | Frost | Shatter | 1 | 31/0/20 |

## Core talents (priority order)

1. **Missile Barrage** — +4.6 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Channeling** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
3. **Arcane Blast** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
4. **Arcane Mind** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Arcane Meditation** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
6. **Arcane Instability** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Precision** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
8. **Arcane Concentration** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-09: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Fingers of Frost to Shatter at 60 (tie-break: -0.2% seed 3, -0.1% seed 4, level-weighted time per kill); Permafrost to Arcane Power at 59 (tie-break: -0.2% seed 3, -0.2% seed 4, level-weighted time per kill); Arctic Reach to Shatter at 56 (tie-break: -0.2% seed 3, -0.3% seed 4, level-weighted time per kill); Arctic Reach to Shatter at 55 (measured: -0.4% seed 3, -0.4% seed 4, level-weighted time per kill); Improved Blizzard to Improved Frost Nova at 54 (gate: -0.2% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 31.16; arcane-open-leveling 31.12, arcane-leveling 38.63. The search simulated 53,708 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Arcane leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/05100520310031153--2323013031200001-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
