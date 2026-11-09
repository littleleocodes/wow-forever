# Restoration — Leveling into the raid build — 11/0/40

*[Druid](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/0/40 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Level with the talents of the Restoration raid build (restoration-ml-heal) so you arrive at 60 ready to heal; the order is the fastest of three the fight lab raced (stats model's order: 28 s per kill over levels 20-60, the feral-cat-dps rotation).

## Point allocation

### Balance (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Wrath** | 1/5 | changed | Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%. |
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Improved Moonfire** | 2/2 | changed | Increases the damage and critical strike chance of your Moonfire spell by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |

### Feral Combat (0)

*No points.*

### Restoration (40)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 3/5 | changed | Gives your Arcane and Nature spells a 42% chance to not lose casting time when you take damage. |
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Gift of Nature** | 5/5 | changed | Increases the effect of all your healing spells by 10%. |
| **Tranquil Spirit** | 5/5 | unchanged | Reduces the mana cost of your Healing Touch and Tranquility spells by 10%. |
| **Improved Rejuvenation** | 3/3 | moved | Increases the effect of your Rejuvenation spell by 15%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with your active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of the consumed spell. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell becomes an instant cast spell. |
| **Living Spirit** | 3/3 | **NEW** | Increases your Spirit by 15%. |
| **Improved Regrowth** | 5/5 | unchanged | Increases the critical effect chance of your Regrowth spell by 50%. |
| **Bloom** | 1/1 | **NEW** | When your Rejuvenation or Regrowth spell expires due to its duration, the target is instantly healed for an amount equal to 100% of your Spirit. If either spell expires due to being dispelled, the target is healed for 50% of your Spirit instead. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10 | Balance | Improved Wrath | 1 | 1/0/0 |
| 11-14 | Balance | Genesis | 4 | 5/0/0 |
| 15-16 | Balance | Improved Moonfire | 2 | 7/0/0 |
| 17-18 | Balance | Nature's Majesty | 2 | 9/0/0 |
| 19-23 | Restoration | Heart of the Wild | 5 | 9/0/5 |
| 24-28 | Restoration | Naturalist | 5 | 9/0/10 |
| 29 | Balance | Genesis | 1 | 10/0/10 |
| 30 | Balance | Nature's Splendor | 1 | 11/0/10 |
| 31-33 | Restoration | Nature's Focus | 3 | 11/0/13 |
| 34-35 | Restoration | Reflection | 2 | 11/0/15 |
| 36 | Restoration | Swiftmend | 1 | 11/0/16 |
| 37-41 | Restoration | Tranquil Spirit | 5 | 11/0/21 |
| 42-44 | Restoration | Living Spirit | 3 | 11/0/24 |
| 45 | Restoration | Reflection | 1 | 11/0/25 |
| 46-50 | Restoration | Gift of Nature | 5 | 11/0/30 |
| 51-53 | Restoration | Improved Rejuvenation | 3 | 11/0/33 |
| 54 | Restoration | Nature's Swiftness | 1 | 11/0/34 |
| 55-59 | Restoration | Improved Regrowth | 5 | 11/0/39 |
| 60 | Restoration | Bloom | 1 | 11/0/40 |

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-08 (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced (fight lab, seed 3, 3000 fights per level, level-weighted): stats model's order 28 s; own tree first 28 s; own tree last 28 s. First Restoration point at level 19.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- Check the Restoration leveling pace at launch; the raid build's talents may cost speed early.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
