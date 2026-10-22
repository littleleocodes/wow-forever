# Optimizer — Raid Fireball spam with Scorch upkeep (parse) — 14/34/3

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/34/3 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fire-raid` and profile `parse`: score +161.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast or Arcane Wrath. |
| **Missile Barrage** | 1/2 | **NEW** | Gives your Arcane Blast spell a 20% chance, your Arcane Missile hits a 5% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 1/2 | changed | Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec. |

### Fire (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 2/3 | changed | Gives your Fire spells a 47% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 20%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 5/5 | unchanged | Increases the critical strike chance of your Fire spells by 10%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |

## Core talents (priority order)

1. **Improved Scorch** — Removing it costs 88.8 points of score in this model.
2. **Fire Power** — Removing it costs 23.6 points of score in this model.
3. **Ignite** — Removing it costs 22.3 points of score in this model.
4. **Improved Fireball** — Removing it costs 20.7 points of score in this model.
5. **Critical Mass** — Removing it costs 15.2 points of score in this model.
6. **Elemental Precision** — Removing it costs 14.6 points of score in this model.
7. **Pyroblast** — Removing it costs 11.9 points of score in this model.
8. **Combustion** — Removing it costs 9.6 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: mage/research/talents/forever/optimizer/fire-raid-parse.md
- 2026-10-16 (repair_builds.py, client build 70425 trees): 13/33/5 -> 13/33/5; Wake of Fire -> Improved Fire Blast (renamed); Fire Power 5 -> 3 (rank cap); +1 Critical Mass (prerequisite of Combustion); +1 Critical Mass (prerequisite of Combustion) (refill: the fire-raid model, raid-dps).
- 2026-10-22 (repair_builds.py, client build 70425 trees): 13/33/5 -> 14/34/3; Elemental Precision 5 -> 3 (rank cap); refill +1 Heating Up, +1 Missile Barrage (refill: the fire-raid model, raid-dps).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
