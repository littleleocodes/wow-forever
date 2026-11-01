# Optimizer — Shadow leveling/raid: Shadow Word: Pain 28%, Mind Blast 27%, Mind Flay channel 30% (talent), wand 10%, Smite 5% before 20 (solo-60) — 16/2/33

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/2/33 (Discipline / Holy / Shadow) |
| **Role** | DPS — Solo/farming |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `shadow-dps` and profile `solo-60`: score +55.3% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Discipline (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Mental Strength** | 3/5 | changed | Increases your total Intellect by 6%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Mental Agility** | 2/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 7%. |

### Holy (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 2/3 | **NEW** | Gives your spells a 47% chance to not lose casting time when you take damage. |

### Shadow (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Shadow Focus** | 5/5 | changed | Improves your chance to hit with Shadow spells by 5%. |
| **Blackout** | 5/5 | moved | Gives your Shadow damage spells a 10% chance to stun the target for 3 sec. |
| **Improved Mind Blast** | 1/5 | changed | Reduces the cooldown of your Mind Blast spell by 0.5 sec. |
| **Shadow Reach** | 2/2 | changed | Increases the range of your offensive Shadow spells by 20%. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Each instance of damage of Mind Flay deals 20% more damage than its previous instance of damage. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |
| **Early Demise** | 2/2 | **NEW** | Increases Shadow Word: Death's critical strike chance on targets at or below 20% health by 30%. |
| **Darkness** | 5/5 | changed | Increases your Shadow damage done by 10%. |
| **Shadowform** | 1/1 | changed | Assume Shadowform, increasing your Shadow damage by 10%, reducing the Mana cost of all Shadow spells by 50%, increasing the critical strike damage bonus of your Shadow spells by 100%, and reducing Physical damage taken by you by 15%. However, you may not cast healing spells while in this form. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Shadow | Spirit Tap | 5 | 0/0/5 |
| 15-19 | Shadow | Shadow Focus | 5 | 0/0/10 |
| 20 | Shadow | Mind Flay | 1 | 0/0/11 |
| 21-22 | Shadow | Improved Mind Flay | 2 | 0/0/13 |
| 23-24 | Shadow | Shadow Reach | 2 | 0/0/15 |
| 25-27 | Shadow | Shadow Weaving | 3 | 0/0/18 |
| 28-32 | Shadow | Blackout | 5 | 0/0/23 |
| 33 | Shadow | Improved Mind Blast | 1 | 0/0/24 |
| 34 | Shadow | Vampiric Embrace | 1 | 0/0/25 |
| 35-36 | Shadow | Early Demise | 2 | 0/0/27 |
| 37-39 | Shadow | Darkness | 3 | 0/0/30 |
| 40 | Shadow | Shadowform | 1 | 0/0/31 |
| 41-42 | Shadow | Darkness | 2 | 0/0/33 |
| 43-47 | Discipline | Twin Disciplines | 5 | 5/0/33 |
| 48-49 | Discipline | Wand Specialization | 2 | 7/0/33 |
| 50-52 | Discipline | Mental Strength | 3 | 10/0/33 |
| 53 | Discipline | Inner Focus | 1 | 11/0/33 |
| 54-55 | Discipline | Mental Agility | 2 | 13/0/33 |
| 56-58 | Discipline | Meditation | 3 | 16/0/33 |
| 59-60 | Holy | Twilight Focus | 2 | 16/2/33 |

## Core talents (priority order)

1. **Shadowform** — Removing it costs 17.0 points of score in this model.
2. **Improved Mind Flay** — Removing it costs 2.8 points of score in this model.
3. **Darkness** — Removing it costs 2.6 points of score in this model.
4. **Mind Flay** — Removing it costs 2.2 points of score in this model.
5. **Shadow Weaving** — Removing it costs 2.0 points of score in this model.
6. **Spirit Tap** — Removing it costs 1.3 points of score in this model.
7. **Shadow Focus** — Removing it costs 1.3 points of score in this model.
8. **Early Demise** — Removing it costs 1.1 points of score in this model.

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Report: priest/research/talents/forever/optimizer/shadow-dps-solo-60.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/priest>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
