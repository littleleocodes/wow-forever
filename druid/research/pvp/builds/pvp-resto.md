# Restoration / Balance — PvP Healer (14/0/37) — 14/0/37

*[Druid](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/0/37 (Balance / Feral Combat / Restoration) |
| **Role** | HEALER — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `pvp-resto-feral-hybrid` |

## Summary

Nature's Grasp is gone (likely baseline), so the Balance dip is Genesis, Nature's Majesty, Nature's Reach, Moonglow and Improved Entangling Roots; Restoration keeps Furor, Natural Shapeshifter, Swiftmend, Nature's Swiftness and Improved Regrowth, adds Naturalist and Gift of the Earthmother.

## Point allocation

### Balance (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Moonglow** | 1/3 | changed | Reduces the Mana cost of your damaging spells by 8%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |
| **Improved Entangling Roots** | 3/3 | changed | Increases the damage done by your Entangling Roots spell by 75%, and its victims can take up to 75% more damage without interrupting the effect. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |

### Feral Combat (0)

*No points.*

### Restoration (37)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting Arcane and Nature spells. |
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when you shapeshift into Bear Form or Dire Bear Form. When you shift into Cat Form, you will regain 100% of the Energy you had when you were last in Cat Form, plus 10 Energy for each second you spent not in Bear Form, Cat Form, or Dire Bear Form, up to a maximum of 100 Energy. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Natural Shapeshifter** | 3/3 | moved | Reduces the mana cost of all shapeshifting by 30%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Gift of Nature** | 5/5 | changed | Increases the effect of all your healing spells by 10%. |
| **Gift of the Earthmother** | 1/1 | **NEW** | Reduces the global cooldown by 0.5 seconds on your Rejuvenation, Swiftmend, and Wild Growth spells. |
| **Improved Rejuvenation** | 3/3 | moved | Increases the effect of your Rejuvenation spell by 15%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell becomes an instant cast spell. |
| **Improved Regrowth** | 5/5 | unchanged | Increases the critical effect chance of your Regrowth spell by 50%. |

## Core talents (priority order)

1. **Nature's Swiftness** — Instant Healing Touch.
2. **Swiftmend** — Instant heal from a HoT; cheap at 16 points.
3. **Natural Shapeshifter** — Cheaper shifting out of snares.
4. **Furor** — Rage/energy on shift.
5. **Improved Entangling Roots** — Roots resist damage breaks.
6. **Improved Regrowth** — Regrowth crits.
7. **Nature's Focus** — Heal through damage.
8. **Gift of the Earthmother** — Faster Rejuvenation/Swiftmend globals.
9. **Nature's Splendor** — +3 s Rejuvenation and +6 s Regrowth: more healing per cast while being trained.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Moonglow 2 | Improved Moonfire | Balance tier-2 filler. |

## Notes

- Nature's Grasp and Improved Nature's Grasp are not in the demo tree — presumably baseline.
- 2026-09-27 scenario audit: Moonglow 1 -> Nature's Splendor 1. Moonglow (beta) only cheapens damaging spells, which a Restoration druid rarely casts in PvP; its first rank stays as the Balance tier filler. Nature's Splendor lengthens Rejuvenation by 3 s and Regrowth by 6 s: more healing per global cooldown under pressure (PvP profile +0.9 points).

## Open questions (verify in the live game)

- Nature's Grasp availability.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
