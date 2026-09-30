# Restoration — Leveling into the raid build — 11/5/35

*[Druid](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/5/35 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Level with the talents of the Restoration raid build (resto-raid-healer) so you arrive at 60 ready to heal; the order is the fastest of three the fight lab raced (stats model's order: 33 s per kill over levels 20-60, the feral-cat-dps rotation).

## Point allocation

### Balance (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Moonglow** | 3/3 | changed | Reduces the Mana cost of your damaging spells by 25%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |

### Feral Combat (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |

### Restoration (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting Arcane and Nature spells. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Gift of Nature** | 5/5 | changed | Increases the effect of all your healing spells by 10%. |
| **Gift of the Earthmother** | 1/1 | **NEW** | Reduces the global cooldown by 0.5 seconds on your Rejuvenation, Swiftmend, and Wild Growth spells. |
| **Tranquil Spirit** | 5/5 | unchanged | Reduces the mana cost of your Healing Touch and Tranquility spells by 10%. |
| **Improved Rejuvenation** | 3/3 | moved | Increases the effect of your Rejuvenation spell by 15%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell becomes an instant cast spell. |
| **Living Spirit** | 3/3 | **NEW** | Increases your Spirit by 15%. |
| **Improved Regrowth** | 2/5 | unchanged | Increases the critical effect chance of your Regrowth spell by 20%. |
| **Wild Growth** | 1/1 | **NEW** | Heals the target and their party for 336 over 7 sec. Party members must be within 43 yards of target. The amount healed is applied quickly at first, and slows down as Wild Growth reaches its full duration. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Restoration | Nature's Focus | 5 | 0/0/5 |
| 15-19 | Restoration | Naturalist | 5 | 0/0/10 |
| 20-24 | Balance | Genesis | 5 | 5/0/10 |
| 25-26 | Balance | Nature's Majesty | 2 | 7/0/10 |
| 27-31 | Feral Combat | Heart of the Wild | 5 | 7/5/10 |
| 32-34 | Restoration | Reflection | 3 | 7/5/13 |
| 35-36 | Restoration | Gift of Nature | 2 | 7/5/15 |
| 37 | Restoration | Swiftmend | 1 | 7/5/16 |
| 38-40 | Balance | Moonglow | 3 | 10/5/16 |
| 41 | Balance | Nature's Splendor | 1 | 11/5/16 |
| 42-46 | Restoration | Tranquil Spirit | 5 | 11/5/21 |
| 47-49 | Restoration | Living Spirit | 3 | 11/5/24 |
| 50-52 | Restoration | Gift of Nature | 3 | 11/5/27 |
| 53 | Restoration | Gift of the Earthmother | 1 | 11/5/28 |
| 54-56 | Restoration | Improved Rejuvenation | 3 | 11/5/31 |
| 57 | Restoration | Nature's Swiftness | 1 | 11/5/32 |
| 58-59 | Restoration | Improved Regrowth | 2 | 11/5/34 |
| 60 | Restoration | Wild Growth | 1 | 11/5/35 |

## Core talents (priority order)

1. **Reflection** — Regen while casting (17%/rank est. 51%). Healer lab (2026-09-28): removing it costs +38% healing capacity.
2. **Moonglow** — -9% mana on all spells (est.). Healer lab (2026-09-28): removing it costs +30% healing capacity.
3. **Tranquil Spirit** — Healer lab (2026-09-28): removing it costs +9% healing capacity.
4. **Gift of Nature** — +10% healing (est.). Healer lab (2026-09-28): removing it costs +6% healing capacity.
5. **Living Spirit** — +15% Spirit (est.); Wild Growth prerequisite. Healer lab (2026-09-28): removing it costs +6% healing capacity.
6. **Nature's Splendor** — +3s Rejuvenation/Moonfire, +6s Regrowth. Healer lab (2026-09-28): removing it costs +2% healing capacity.
7. **Swiftmend** — Now a 16-point talent; per the reveal it no longer consumes the HoT. Healer lab (2026-09-28): removing it costs +2% healing capacity.
8. **Genesis** — New: +5% periodic healing (est.) — Rejuvenation, Regrowth HoT, Wild Growth. Healer lab (2026-09-28): removing it costs +2% healing capacity.

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-09-30 (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced (fight lab, seed 3, 3000 fights per level, level-weighted): stats model's order 33 s; own tree first 33 s; own tree last 33 s. First Restoration point at level 10.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- Check the Restoration leveling pace at launch; the raid build's talents may cost speed early.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
