# Restoration — Regrowth / Nature's Grace, with a Balance dip (21/0/30) — 21/0/30

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Balance / Feral Combat / Restoration) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `resto-regrowth-natures-grace` |

## Summary

The Classic endgame Regrowth build, adapted: Nature's Grace (now +10% cast speed for 3s after a crit) still pairs with Improved Regrowth, and the first 20 Balance points now include genuinely useful healer talents (Genesis, Nature's Majesty, Moonglow, Nature's Splendor, Insect Swarm). Probably weaker than 11/0/40 now that Wild Growth exists — kept for comparison.

## Point allocation

### Balance (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Improved Wrath** | 1/5 | changed | Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%. |
| **Improved Moonfire** | 2/2 | changed | Increases the damage and critical strike chance of your Moonfire spell by 10%. |
| **Moonglow** | 3/3 | changed | Reduces the Mana cost of your damaging spells by 25%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |
| **Improved Entangling Roots** | 3/3 | changed | Increases the damage done by your Entangling Roots spell by 75%, and its victims can take up to 75% more damage without interrupting the effect. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |
| **Insect Swarm** | 1/1 | changed | The enemy target is swarmed by insects, decreasing their chance to hit with attacks by 2% and causing 48 Nature damage over 12 sec. |
| **Nature's Grace** | 1/1 | changed | All non-periodic spell criticals grace you with a blessing of nature, increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec. |

### Feral Combat (0)

*No points.*

### Restoration (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives your Arcane and Nature spells a 70% chance to not lose casting time when you take damage. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Gift of Nature** | 5/5 | changed | Increases the effect of all your healing spells by 10%. |
| **Improved Rejuvenation** | 3/3 | moved | Increases the effect of your Rejuvenation spell by 15%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with your active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of the consumed spell. |
| **Living Spirit** | 2/3 | **NEW** | Increases your Spirit by 10%. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell becomes an instant cast spell. |
| **Improved Regrowth** | 5/5 | unchanged | Increases the critical effect chance of your Regrowth spell by 50%. |

## Core talents (priority order)

1. **Nature's Grace** — +10% cast speed and shorter GCD for 3s after any crit (reworked).
2. **Improved Regrowth** — +50% Regrowth crit.
3. **Gift of Nature** — Healing.
4. **Genesis** — Periodic healing.
5. **Nature's Splendor** — Longer Regrowth/Rejuvenation.
6. **Swiftmend** — Reachable at 16 points now — the Classic build had to give it up.
7. **Nature's Swiftness** — Instant Healing Touch.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 9 | Improved Moonfire 2 + Nature's Reach 2 + Improved Entangling Roots 3 + Balance of Nature 1 + Insect Swarm 1 | Improved Wrath, Eclipse path | Balance gating fillers between tier 2 and Nature's Grace. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- Loses Wild Growth, Living Spirit 3 and Tranquil Spirit versus the deep Restoration build.
- Beta client 1.60.1.69893 removed Balance of Nature: its 1 gating point moved to Improved Wrath.
- 2026-09-30: renamed from "Restoration / Balance — Regrowth / Nature's Grace (21/0/30)" so the name matches the spec the pages file it under (the point split decides the spec, spec_modes.py).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 21/0/30 -> 21/0/30; Gift of the Earthmother 1 gone; +1 Living Spirit (tier gating for Improved Regrowth) (refill: the resto-heal model, raid-heal).

## Open questions (verify in the live game)

- Whether the reworked Nature's Grace (3s haste window) is worth 21 Balance points at all.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
