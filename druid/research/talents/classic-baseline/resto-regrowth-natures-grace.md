# Restoration — Regrowth / Nature's Grace (21/0/30) — 21/0/30

*Druid · Classic baseline*

| | |
|---|---|
| **Build** | 21/0/30 (Balance / Feral Combat / Restoration) |
| **Role** | HEALER — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The endgame Regrowth build: Nature's Grace (-0.5s cast after a crit) chained with Improved Regrowth's +50% crit means near-permanent fast Regrowths, with Gift of Nature and Reflection behind it. Gives up Swiftmend, Nature's Swiftness, Tranquil Spirit and Improved Rejuvenation for 20 points of Balance utility.

## Point allocation

### Balance (21)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Wrath** | 5/5 | Reduces the cast time of your Wrath spell by 0.5 sec. |
| **Nature's Grasp** | 1/1 | While active, any time an enemy strikes the caster they have a 35% chance to become afflicted by Entangling Roots (Rank 1). Only useable outdoors. 1 charge. Lasts 45 sec. |
| **Improved Nature's Grasp** | 4/4 | Increases the chance for your Nature's Grasp to entangle an enemy by 65%. |
| **Improved Entangling Roots** | 2/3 | Gives you a 70% chance to avoid interruption caused by damage while casting Entangling Roots. |
| **Natural Shapeshifter** | 3/3 | Reduces the mana cost of all shapeshifting by 30%. |
| **Improved Thorns** | 3/3 | Increases damage caused by your Thorns spell by 75%. |
| **Nature's Reach** | 2/2 | Increases the range of your Wrath, Entangling Roots, Faerie Fire, Moonfire, Starfire, and Hurricane spells by 20%. |
| **Nature's Grace** | 1/1 | All spell criticals grace you with a blessing of nature, reducing the casting time of your next spell by 0.5 sec. |

### Feral Combat (0)

*No points.*

### Restoration (30)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Mark of the Wild** | 5/5 | Increases the effects of your Mark of the Wild and Gift of the Wild spells by 35%. |
| **Improved Healing Touch** | 5/5 | Reduces the cast time of your Healing Touch spell by 0.5 sec. |
| **Nature's Focus** | 5/5 | Gives you a 70% chance to avoid interruption caused by damage while casting the Healing Touch, Regrowth and Tranquility spells. |
| **Reflection** | 3/3 | Allows 15% of your Mana regeneration to continue while casting. |
| **Insect Swarm** | 1/1 | The enemy target is swarmed by insects, decreasing their chance to hit by 2% and causing 66 Nature damage over 12 sec. |
| **Improved Rejuvenation** | 1/3 | Increases the effect of your Rejuvenation spell by 5%. |
| **Gift of Nature** | 5/5 | Increases the effect of all healing spells by 10%. |
| **Improved Regrowth** | 5/5 | Increases the critical effect chance of your Regrowth spell by 50%. |

## Core talents (priority order)

1. **Nature's Grace** — Every crit makes the next spell 0.5s faster — with Improved Regrowth it is up constantly.
2. **Improved Regrowth** — +50% Regrowth crit chance.
3. **Gift of Nature** — +10% healing.
4. **Reflection** — Mana regen while casting.
5. **Improved Healing Touch** — Healing Touch cast time for the big heals.
6. **Natural Shapeshifter** — -30% shapeshift cost — bear/travel emergencies cost less.
7. **Nature's Reach** — +20% range on Balance spells (Roots, Moonfire, Hibernate).

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 1 | Improved Rejuvenation | Subtlety | Twentieth Restoration point to unlock Gift of Nature. |

## Notes

- Regrowth spam on the tank and raid; Healing Touch when Nature's Grace is up and the tank is low.
- Icy Veins also lists a Moonglow variant (24/0/27) for mana-starved raids: same Balance path plus Moonglow 3/3, dropping Improved Regrowth.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Balance | Improved Wrath | 5 | changed | tier 1, max 5 — tooltip changed; was Balance row 1, col 1 |
| Balance | Nature's Grasp | 1 | **REMOVED** | removed from Classic |
| Balance | Improved Nature's Grasp | 4 | **REMOVED** | removed from Classic |
| Balance | Improved Entangling Roots | 2 | changed | tier 3, max 3 — tooltip changed; was Balance row 2, col 1 |
| Balance | Natural Shapeshifter | 3 | moved-tree | now in Restoration, tier 2 |
| Balance | Improved Thorns | 3 | **REMOVED** | removed from Classic |
| Balance | Nature's Reach | 2 | changed | tier 2, max 2 — tooltip changed; was Balance row 3, col 4 |
| Balance | Nature's Grace | 1 | changed | tier 5, max 1 — tooltip changed |
| Restoration | Improved Mark of the Wild | 5 | **REMOVED** | removed from Classic |
| Restoration | Improved Healing Touch | 5 | **REMOVED** | removed from Classic |
| Restoration | Nature's Focus | 5 | changed | tier 1, max 5 — tooltip changed; was Restoration row 2, col 2; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3, 4, 5) |
| Restoration | Reflection | 3 | changed | tier 2, max 3 — tooltip changed; moved in build 1.60.1.70753: was row 3, col 2 |
| Restoration | Insect Swarm | 1 | moved-tree | now in Balance, tier 4 |
| Restoration | Improved Rejuvenation | 1 | moved | tier 4, max 3 — was Restoration row 4, col 4 |
| Restoration | Gift of Nature | 5 | changed | tier 3, max 5 — tooltip changed; was Restoration row 5, col 3 |
| Restoration | Improved Regrowth | 5 | unchanged | tier 6, max 5 |

**18 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/restoration-druid-healer-pve-spec-builds-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
