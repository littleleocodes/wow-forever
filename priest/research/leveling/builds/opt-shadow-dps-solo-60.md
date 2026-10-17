# Optimizer — Shadow leveling/raid: Shadow Word: Pain 28%, Mind Blast 27%, Mind Flay channel 30% (talent), wand 10%, Smite 5% before 20 (solo-60) — 7/11/33

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/11/33 (Discipline / Holy / Shadow) |
| **Role** | DPS — Solo/farming |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `shadow-dps` and profile `solo-60`: score +74.4% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Discipline (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Mental Strength** | 2/5 | changed | Increases your total Intellect by 4%. |

### Holy (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Renew** | 2/3 | unchanged | Increases the amount healed by your Renew spell by 10%. |
| **Twilight Focus** | 3/3 | **NEW** | Gives you a 70% chance to avoid interruption caused by damage while casting any spell. |
| **Spell Warding** | 5/5 | unchanged | Reduces all spell damage taken by 10%. |
| **Holy Nova** | 1/1 | changed | Causes an explosion of holy light around the caster, causing 26 to 30 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 49 to 57. These effects cause no threat. |

### Shadow (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Blackout** | 5/5 | moved | Gives your Shadow damage spells a 10% chance to stun the target for 3 sec. |
| **Shadow Focus** | 5/5 | changed | Improves your chance to hit with Shadow spells by 5%. |
| **Spirit Tap** | 1/5 | changed | Gives you a 20% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Mind Blast** | 5/5 | changed | Reduces the cooldown of your Mind Blast spell by 2.5 sec. |
| **Shadow Reach** | 2/2 | changed | Increases the range of your offensive Shadow spells by 20%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Each instance of damage of Mind Flay deals 20% more damage than its previous instance of damage. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Darkness** | 5/5 | changed | Increases your Shadow damage done by 10%. |
| **Early Demise** | 2/2 | **NEW** | Increases Shadow Word: Death's critical strike chance on targets at or below 20% health by 30%. |
| **Shadowform** | 1/1 | changed | Assume Shadowform, increasing your Shadow damage by 10%, reducing the Mana cost of all Shadow spells by 50%, increasing the critical strike damage bonus of your Shadow spells by 100%, and reducing Physical damage taken by you by 15%. However, you may not cast healing spells while in this form. |

## Core talents (priority order)

1. **Mind Flay** — Removing it costs 23.7 points of score in this model.
2. **Shadowform** — Removing it costs 13.2 points of score in this model.
3. **Shadow Weaving** — Removing it costs 2.2 points of score in this model.
4. **Improved Mind Flay** — Removing it costs 2.1 points of score in this model.
5. **Darkness** — Removing it costs 1.5 points of score in this model.
6. **Shadow Focus** — Removing it costs 0.7 points of score in this model.
7. **Blackout** — Removing it costs 0.7 points of score in this model.
8. **Shadow Reach** — Removing it costs 0.6 points of score in this model.

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Report: priest/talents/forever/optimizer/shadow-dps-solo-60.md
- 2026-10-16 (repair_builds.py, client build 70425 trees): 7/11/33 -> 7/11/33; +1 Mental Strength (tier gating for Improved Power Word: Shield); +1 Mental Strength (tier gating for Improved Power Word: Shield); +1 Mental Strength (tier gating for Improved Power Word: Shield); +1 Mental Strength (tier gating for Improved Power Word: Shield); +1 Mental Strength (tier gating for Improved Power Word: Shield); -1 Improved Power Word: Shield (over 51); -1 Improved Power Word: Shield (over 51); -1 Mental Strength (over 51); -1 Mental Strength (over 51); -1 Mental Strength (over 51); order dropped (order_repair.py) (refill: the shadow-dps model, solo-60).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/priest>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
