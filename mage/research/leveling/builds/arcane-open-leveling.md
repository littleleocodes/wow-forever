# Arcane — Leveling (open talent search) — 34/17/0

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 34/17/0 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the arcane-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). +31.0% faster per kill than arcane-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 4/? | ? |  |
| **Improved Channeling** | 5/5 | **NEW** | Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, Frost Blast, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |

### Fire (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 4/? | ? |  |
| **Flame Throwing** | 2/2 | unchanged | Increases the range of your Fire spells by 6 yards. |
| **Impact** | 3/3 | changed | Gives your Fire spells a 10% chance to stun the target for 2 sec. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Master of Elements** | 2/3 | changed | Your Fire and Frost critical strikes will refund 20% of their base mana cost. |

### Frost (0)

*No points.*

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Arcane | Missile Barrage | 2 | 2/0/0 |
| 12-14 | Arcane | Arcane Focus | 3 | 5/0/0 |
| 15-19 | Arcane | Arcane Concentration | 5 | 10/0/0 |
| 20 | Arcane | Arcane Blast | 1 | 11/0/0 |
| 21 | Arcane | Arcane Focus | 1 | 12/0/0 |
| 22-24 | Arcane | Improved Channeling | 3 | 15/0/0 |
| 25 | Arcane | Arcane Wrath | 1 | 16/0/0 |
| 26-28 | Arcane | Arcane Meditation | 3 | 19/0/0 |
| 29 | Arcane | Improved Channeling | 1 | 20/0/0 |
| 30 | Arcane | Presence of Mind | 1 | 21/0/0 |
| 31 | Arcane | Improved Channeling | 1 | 22/0/0 |
| 32-34 | Arcane | Arcane Impact | 3 | 25/0/0 |
| 35-37 | Arcane | Arcane Instability | 3 | 28/0/0 |
| 38-39 | Arcane | Arcane Mind | 2 | 30/0/0 |
| 40 | Arcane | Arcane Power | 1 | 31/0/0 |
| 41-43 | Arcane | Arcane Mind | 3 | 34/0/0 |
| 44-45 | Fire | Improved Fire Blast | 2 | 34/2/0 |
| 46-48 | Fire | Incineration | 3 | 34/5/0 |
| 49-52 | Fire | Improved Fireball | 4 | 34/9/0 |
| 53-54 | Fire | Flame Throwing | 2 | 34/11/0 |
| 55-57 | Fire | Impact | 3 | 34/14/0 |
| 58 | Fire | Pyroblast | 1 | 34/15/0 |
| 59-60 | Fire | Master of Elements | 2 | 34/17/0 |

## Core talents (priority order)

1. **Missile Barrage** — +4.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Arcane Blast** — +4.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Channeling** — +2.9 s per kill at level 60 without it (removal, 3,000 fights).
4. **Arcane Mind** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
5. **Arcane Concentration** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
6. **Arcane Instability** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Arcane Impact** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
8. **Arcane Meditation** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 32.45; arcane-leveling 42.52. The search simulated 55,377 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Arcane leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/0452005003100311531-2340230010002--7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
