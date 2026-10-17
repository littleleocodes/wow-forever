# Optimizer — Starfire 55%, Wrath 20%, Moonfire 20% (8% direct, 12% DoT), Insect Swarm arrives as a talent effect (parse) — 33/5/13

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/5/13 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `balance-dps` and profile `parse`: score +96.6% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Moonglow** | 3/3 | changed | Reduces the Mana cost of your damaging spells by 25%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |
| **Improved Moonfire** | 2/2 | changed | Increases the damage and critical strike chance of your Moonfire spell by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |
| **Insect Swarm** | 1/1 | changed | The enemy target is swarmed by insects, decreasing their chance to hit with attacks by 2% and causing 48 Nature damage over 12 sec. |
| **Vengeance** | 5/5 | changed | Increases the critical strike damage bonus of your Arcane and Nature spells by 100%. |
| **Improved Starfire** | 5/5 | changed | Reduces the cast time of Starfire by 0.5 sec and Starfire has a 15% chance to stun its target for 3 sec. |
| **Nature's Grace** | 1/1 | changed | All non-periodic spell criticals grace you with a blessing of nature, increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec. |
| **Moonfury** | 5/5 | changed | Increases the damage done by your Arcane and Nature spells by 10%. |
| **Moonkin Form** | 1/1 | changed | Shapeshift into Moonkin Form, increasing Omen of Clarity's chance to trigger by 100%, Armor contribution from items by 360%, and all party or raid members within 45 yards have their spell Critical Strike chance increased by 3%. Also protects the caster from Polymorph effects and prevents the use of healing spells.  The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects. |

### Feral Combat (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |

### Restoration (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting Arcane and Nature spells. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

## Core talents (priority order)

1. **Vengeance** — Removing it costs 20.7 points of score in this model.
2. **Moonfury** — Removing it costs 16.6 points of score in this model.
3. **Insect Swarm** — Removing it costs 15.5 points of score in this model.
4. **Improved Starfire** — Removing it costs 11.2 points of score in this model.
5. **Moonglow** — Removing it costs 11.1 points of score in this model.
6. **Moonkin Form** — Removing it costs 10.9 points of score in this model.
7. **Naturalist** — Removing it costs 8.7 points of score in this model.
8. **Nature's Reach** — Removing it costs 8.5 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: druid/research/talents/forever/optimizer/balance-dps-parse.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
