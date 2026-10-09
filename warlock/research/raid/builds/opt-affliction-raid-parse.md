# Optimizer — Corruption 28%, Agony 18%, Shadow Bolt 30%, Drain Life 12%, Immolate 6%, Imp 6%; Siphon Life and Wrack arrive as talent effects (parse) — 30/0/21

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/0/21 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `affliction-raid` and profile `parse`: score +61.9% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Affliction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Malediction** | 2/5 | **NEW** | Increases all periodic damage done by your Warlock spells by 2%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Shadow Mastery** | 5/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 5%. |

### Demonology (0)

*No points.*

### Destruction (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Aftermath** | 3/5 | changed | Increases the initial damage of your Immolate spell by 30% and your Conflagrate spell has a 60% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Bane** — Removing it costs 14.4 points of score in this model.
2. **Agonizing Flames** — Removing it costs 9.5 points of score in this model.
3. **Improved Shadow Bolt** — Removing it costs 7.9 points of score in this model.
4. **Suppression** — Removing it costs 7.0 points of score in this model.
5. **Ruin** — Removing it costs 7.0 points of score in this model.
6. **Malevolence** — Removing it costs 6.5 points of score in this model.
7. **Shadow Mastery** — Removing it costs 6.4 points of score in this model.
8. **Improved Corruption** — Removing it costs 6.1 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: warlock/research/talents/forever/optimizer/affliction-raid-parse.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
