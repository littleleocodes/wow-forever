# Optimizer — Raid Combat swords: white ~43% (MH 30 / OH 13), Sinister Strike ~30%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (parse) — 19/32/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 19/32/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-swords-raid` and profile `parse`: score +66.2% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 5/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 20%. |

### Combat (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Deflection** | 2/3 | changed | Increases your Parry chance by 4%. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Relentless Strikes** — Removing it costs 12.5 points of score in this model.
2. **Improved Sinister Strike** — Removing it costs 9.5 points of score in this model.
3. **Improved Slice and Dice** — Removing it costs 9.2 points of score in this model.
4. **Malice** — Removing it costs 7.9 points of score in this model.
5. **Ruthlessness** — Removing it costs 7.8 points of score in this model.
6. **Dual Wield Specialization** — Removing it costs 7.7 points of score in this model.
7. **Adrenaline Rush** — Removing it costs 7.3 points of score in this model.
8. **Precision** — Removing it costs 5.8 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: rogue/research/talents/forever/optimizer/combat-swords-raid-parse.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
