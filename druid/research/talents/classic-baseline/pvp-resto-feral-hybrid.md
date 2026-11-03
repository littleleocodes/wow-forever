# Restoration / Balance — PvP Healer (14/0/37) — 14/0/37

*Druid · Classic baseline*

| | |
|---|---|
| **Build** | 14/0/37 (Balance / Feral Combat / Restoration) |
| **Role** | HEALER — PvP |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The flag-carrier / battleground healer: Nature's Swiftness, Swiftmend, Gift of Nature, Improved Regrowth and Furor from Restoration; Nature's Grasp, Improved Entangling Roots, Natural Shapeshifter and Nature's Reach from Balance. Shift, root, run.

## Point allocation

### Balance (14)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Nature's Grasp** | 1/1 | While active, any time an enemy strikes the caster they have a 35% chance to become afflicted by Entangling Roots (Rank 1). Only useable outdoors. 1 charge. Lasts 45 sec. |
| **Improved Nature's Grasp** | 4/4 | Increases the chance for your Nature's Grasp to entangle an enemy by 65%. |
| **Improved Entangling Roots** | 2/3 | Gives you a 70% chance to avoid interruption caused by damage while casting Entangling Roots. |
| **Natural Shapeshifter** | 3/3 | Reduces the mana cost of all shapeshifting by 30%. |
| **Improved Thorns** | 2/3 | Increases damage caused by your Thorns spell by 50%. |
| **Nature's Reach** | 2/2 | Increases the range of your Wrath, Entangling Roots, Faerie Fire, Moonfire, Starfire, and Hurricane spells by 20%. |

### Feral Combat (0)

*No points.*

### Restoration (37)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Furor** | 5/5 | Gives you 100% chance to gain 10 Rage when you shapeshift into Bear and Dire Bear Form or 40 Energy when you shapeshift into Cat Form. |
| **Improved Healing Touch** | 5/5 | Reduces the cast time of your Healing Touch spell by 0.5 sec. |
| **Nature's Focus** | 5/5 | Gives you a 70% chance to avoid interruption caused by damage while casting the Healing Touch, Regrowth and Tranquility spells. |
| **Reflection** | 3/3 | Allows 15% of your Mana regeneration to continue while casting. |
| **Insect Swarm** | 1/1 | The enemy target is swarmed by insects, decreasing their chance to hit by 2% and causing 66 Nature damage over 12 sec. |
| **Tranquil Spirit** | 5/5 | Reduces the mana cost of your Healing Touch and Tranquility spells by 10%. |
| **Improved Rejuvenation** | 1/3 | Increases the effect of your Rejuvenation spell by 5%. |
| **Nature's Swiftness** | 1/1 | When activated, your next Nature spell becomes an instant cast spell. |
| **Gift of Nature** | 5/5 | Increases the effect of all healing spells by 10%. |
| **Improved Regrowth** | 5/5 | Increases the critical effect chance of your Regrowth spell by 50%. |
| **Swiftmend** | 1/1 | Consumes a Rejuvenation or Regrowth effect on a friendly target to instantly heal them an amount equal to 12 sec. of Rejuvenation or 18 sec. of Regrowth. |

## Core talents (priority order)

1. **Nature's Swiftness** — Instant full Healing Touch.
2. **Swiftmend** — Instant heal from a HoT.
3. **Natural Shapeshifter** — Shift out of snares cheaply.
4. **Furor** — Instant Bash/Maul or a full energy bar when you shift.
5. **Nature's Grasp** — Roots on melee hit.
6. **Improved Entangling Roots** — Roots resist damage-breaks.
7. **Nature's Focus** — Heal through melee damage.
8. **Improved Regrowth** — Big Regrowth crits.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Improved Thorns | Improved Moonfire, Improved Wrath | Filler to reach 10 Balance points for Nature's Reach. |
| 5 | Tranquil Spirit | Subtlety, Improved Rejuvenation 3 + Subtlety 2 (no Swiftmend) | Prerequisite for Swiftmend. |

## Notes

- Feral 14/32/5 with Feral Charge is the other common Classic PvP druid; this build is the healer/flag-carrier.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Balance | Nature's Grasp | 1 | **REMOVED** | removed from Classic |
| Balance | Improved Nature's Grasp | 4 | **REMOVED** | removed from Classic |
| Balance | Improved Entangling Roots | 2 | changed | tier 3, max 3 — tooltip changed; was Balance row 2, col 1 |
| Balance | Natural Shapeshifter | 3 | moved-tree | now in Restoration, tier 2 |
| Balance | Improved Thorns | 2 | **REMOVED** | removed from Classic |
| Balance | Nature's Reach | 2 | changed | tier 2, max 2 — tooltip changed; was Balance row 3, col 4 |
| Restoration | Furor | 5 | moved-tree | now in Feral Combat, tier 1 |
| Restoration | Improved Healing Touch | 5 | **REMOVED** | removed from Classic |
| Restoration | Nature's Focus | 5 | changed | tier 1, max 5 — tooltip changed; was Restoration row 2, col 2; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3, 4, 5) |
| Restoration | Reflection | 3 | changed | tier 2, max 3 — tooltip changed; moved in build 1.60.1.70753: was row 3, col 2 |
| Restoration | Insect Swarm | 1 | moved-tree | now in Balance, tier 4 |
| Restoration | Tranquil Spirit | 5 | unchanged | tier 4, max 5 |
| Restoration | Improved Rejuvenation | 1 | moved | tier 4, max 3 — was Restoration row 4, col 4 |
| Restoration | Nature's Swiftness | 1 | unchanged | tier 5, max 1 |
| Restoration | Gift of Nature | 5 | changed | tier 3, max 5 — tooltip changed; was Restoration row 5, col 3 |
| Restoration | Improved Regrowth | 5 | unchanged | tier 6, max 5 |
| Restoration | Swiftmend | 1 | changed | tier 4, max 1 — tooltip changed; was Restoration row 7, col 2; tooltip changed in build 1.60.1.70753 (ranks 1) |

**12 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/druid/healer-pvp-arena>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
