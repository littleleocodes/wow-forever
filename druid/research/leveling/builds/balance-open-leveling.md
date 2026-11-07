# Balance — Leveling (open talent search) — 36/0/15

*[Druid](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 36/0/15 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Balance leveling build the open leveling search found on 2026-11-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the balance-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (balance-dps). 

## Point allocation

### Balance (36)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Wrath** | 5/5 | changed | Reduces the cast time of your Wrath spell by 0.5 sec and its Mana cost by 50%. |
| **Genesis** | 3/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 6%. |
| **Moonglow** | 3/3 | changed | Reduces the Mana cost of your damaging spells by 25%. |
| **Improved Moonfire** | 2/2 | changed | Increases the damage and critical strike chance of your Moonfire spell by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |
| **Vengeance** | 5/5 | changed | Increases the critical strike damage bonus of your Arcane and Nature spells by 100%. |
| **Improved Starfire** | 5/5 | changed | Reduces the cast time of Starfire by 0.5 sec and Starfire has a 15% chance to stun its target for 3 sec. |
| **Nature's Grace** | 1/1 | changed | All non-periodic spell criticals grace you with a blessing of nature, increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec. |
| **Eclipse** | 3/3 | **NEW** | Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.50 sec. Stores up to 4 charges. Lasts 15 sec. |
| **Moonfury** | 5/5 | changed | Increases the damage done by your Arcane and Nature spells by 10%. |
| **Moonkin Form** | 1/1 | changed | Shapeshift into Moonkin Form, increasing Omen of Clarity's chance to trigger by 100%, Armor contribution from items by 360%, and all party or raid members within 45 yards have their Critical Strike chance increased by 3%. Also protects the caster from Polymorph effects and prevents the use of healing spells.  The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects. |

### Feral Combat (0)

*No points.*

### Restoration (15)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives your Arcane and Nature spells a 70% chance to not lose casting time when you take damage. |
| **Heart of the Wild** | 1/5 | changed | Increases your Intellect by 2%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 4% and while in Cat Form your Strength is increased by 2%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Bloom** | 1/1 | **NEW** | When your Rejuvenation or Regrowth spell expires due to its duration, the target is instantly healed for an amount equal to 100% of your Spirit. If either spell expires due to being dispelled, the target is healed for 50% of your Spirit instead. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Balance | Improved Wrath | 5 | 5/0/0 |
| 15 | Balance | Moonglow | 1 | 6/0/0 |
| 16 | Balance | Improved Moonfire | 1 | 7/0/0 |
| 17 | Balance | Moonglow | 1 | 8/0/0 |
| 18 | Balance | Improved Moonfire | 1 | 9/0/0 |
| 19 | Balance | Moonglow | 1 | 10/0/0 |
| 20-21 | Balance | Nature's Majesty | 2 | 12/0/0 |
| 22 | Balance | Nature's Splendor | 1 | 13/0/0 |
| 23-24 | Balance | Genesis | 2 | 15/0/0 |
| 25-29 | Balance | Improved Starfire | 5 | 20/0/0 |
| 30-32 | Balance | Eclipse | 3 | 23/0/0 |
| 33 | Balance | Nature's Grace | 1 | 24/0/0 |
| 34 | Balance | Vengeance | 1 | 25/0/0 |
| 35-36 | Balance | Moonfury | 2 | 27/0/0 |
| 37 | Balance | Vengeance | 1 | 28/0/0 |
| 38 | Balance | Moonfury | 1 | 29/0/0 |
| 39 | Balance | Vengeance | 1 | 30/0/0 |
| 40 | Balance | Moonkin Form | 1 | 31/0/0 |
| 41-42 | Balance | Vengeance | 2 | 33/0/0 |
| 43-44 | Balance | Moonfury | 2 | 35/0/0 |
| 45 | Restoration | Heart of the Wild | 1 | 35/0/1 |
| 46-49 | Restoration | Nature's Focus | 4 | 35/0/5 |
| 50 | Restoration | Reflection | 1 | 35/0/6 |
| 51-55 | Restoration | Naturalist | 5 | 35/0/11 |
| 56-57 | Restoration | Reflection | 2 | 35/0/13 |
| 58 | Balance | Genesis | 1 | 36/0/13 |
| 59 | Restoration | Nature's Focus | 1 | 36/0/14 |
| 60 | Restoration | Bloom | 1 | 36/0/15 |

## Core talents (priority order)

1. **Eclipse** — +11.1 s per kill at level 60 without it (removal, 3,000 fights).
2. **Moonglow** — +3.3 s per kill at level 60 without it (removal, 3,000 fights).
3. **Moonkin Form** — +2.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Moonfury** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Naturalist** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Starfire** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Nature's Focus** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Wrath** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 37.25; opt-balance-dps-leveling-st 37.61. The search simulated 49,461 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Balance leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/druid>
- <https://talentsforever.com/druid/60/5332200105501351--51530001-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
