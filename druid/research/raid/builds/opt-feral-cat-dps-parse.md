# Optimizer — White 40%, Shred 30% (60 energy), Ferocious Bite 15%, Rip 10%, Claw/Rake 5% (parse) — 9/35/7

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/35/7 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `feral-cat-dps` and profile `parse`: score +102.7% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Ferocity** | 2/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 2 Rage or Energy. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Leap behind an enemy. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the critical strike chance of all party members within 45 yards by 3%, exclusive with Moonkin Aura. |
| **King of the Jungle** | 3/3 | **NEW** | Tiger's Fury now instantly grants you 60 Energy. |
| **Predatory Instincts** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20%. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |
| **Berserk** | 1/1 | **NEW** | Causes your Primal Bite ability to strike up to 3 targets, removes its cooldown, and increases the critical strike chance of your Combo Point-generating abilities by 100%. Clears and grants immunity to Fear effects for the duration. Lasts 15 sec. |

### Restoration (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when you shapeshift into Bear Form or Dire Bear Form. When you shift into Cat Form, you will regain 100% of the Energy you had when you were last in Cat Form, plus 10 Energy for each second you spent not in Bear Form, Cat Form, or Dire Bear Form, up to a maximum of 100 Energy. |
| **Naturalist** | 2/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.2 sec and increases all damage you deal by 2%. |

## Core talents (priority order)

1. **Shredding Attacks** — Removing it costs 34.5 points of score in this model.
2. **King of the Jungle** — Removing it costs 17.4 points of score in this model.
3. **Blood Frenzy** — Removing it costs 14.9 points of score in this model.
4. **Sharpened Claws** — Removing it costs 10.8 points of score in this model.
5. **Rend and Tear** — Removing it costs 10.1 points of score in this model.
6. **Berserk** — Removing it costs 7.2 points of score in this model.
7. **Predatory Strikes** — Removing it costs 6.5 points of score in this model.
8. **Predatory Instincts** — Removing it costs 6.2 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: druid/research/talents/forever/optimizer/feral-cat-dps-parse.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
