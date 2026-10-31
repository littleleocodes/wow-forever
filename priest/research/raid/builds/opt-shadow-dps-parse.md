# Optimizer — Shadow leveling/raid: Shadow Word: Pain 28%, Mind Blast 27%, Mind Flay channel 30% (talent), wand 10%, Smite 5% before 20 (parse) — 17/1/33

*[Priest](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/1/33 (Discipline / Holy / Shadow) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `shadow-dps` and profile `parse`: score +201.6% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Discipline (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Mental Strength** | 5/5 | changed | Increases your total Intellect by 10%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Mental Agility** | 3/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Holy (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 1/3 | **NEW** | Gives you a 23% chance to avoid interruption caused by damage while casting any spell. |

### Shadow (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 5/5 | changed | Improves your chance to hit with Shadow spells by 5%. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |
| **Improved Mind Blast** | 5/5 | changed | Reduces the cooldown of your Mind Blast spell by 2.5 sec. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Each instance of damage of Mind Flay deals 20% more damage than its previous instance of damage. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Dark Inspiration** | 3/5 | moved | Your Mind Blast and fully channeled Mind Flay causes Dark Inspiration, increasing yours and your party's Spirit by 9% for 10 sec. |
| **Devouring Contagion** | 2/2 | **NEW** | Reduces the mana cost of your Devouring Plague by 50%.  Targets that die while Devouring Plague is active spreads it, jumping to 2 nearby enemies within 10 yds for the remaining duration. |
| **Silence** | 1/1 | changed | Silences the target, preventing them from casting spells for 5 sec and interrupting their spellcasts for 3 sec. |
| **Darkness** | 5/5 | changed | Increases your Shadow damage done by 10%. |
| **Early Demise** | 2/2 | **NEW** | Increases Shadow Word: Death's critical strike chance on targets at or below 20% health by 30%. |
| **Shadowform** | 1/1 | changed | Assume Shadowform, increasing your Shadow damage by 10%, reducing the Mana cost of all Shadow spells by 50%, increasing the critical strike damage bonus of your Shadow spells by 100%, and reducing Physical damage taken by you by 15%. However, you may not cast healing spells while in this form. |

## Core talents (priority order)

1. **Mind Flay** — Removing it costs 138.7 points of score in this model.
2. **Shadow Weaving** — Removing it costs 26.3 points of score in this model.
3. **Darkness** — Removing it costs 26.3 points of score in this model.
4. **Improved Mind Flay** — Removing it costs 25.6 points of score in this model.
5. **Shadowform** — Removing it costs 12.0 points of score in this model.
6. **Twin Disciplines** — Removing it costs 11.2 points of score in this model.
7. **Shadow Focus** — Removing it costs 10.3 points of score in this model.
8. **Improved Shadow Word: Pain** — Removing it costs 7.6 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: priest/research/talents/forever/optimizer/shadow-dps-parse.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/priest>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
