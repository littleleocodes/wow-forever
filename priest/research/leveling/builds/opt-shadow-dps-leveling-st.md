# Optimizer — Shadow leveling/raid: Shadow Word: Pain 28%, Mind Blast 27%, Mind Flay channel 30% (talent), wand 10%, Smite 5% before 20 (leveling-st) — 7/11/33

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/11/33 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `shadow-dps` and profile `leveling-st`: score +74.4% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Discipline (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Improved Power Word: Shield** | 2/3 | changed | Increases the damage absorbed by your Power Word: Shield by 14%. |

### Holy (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 3/3 | **NEW** | Gives you a 70% chance to avoid interruption caused by damage while casting any spell. |
| **Improved Renew** | 2/3 | unchanged | Increases the amount healed by your Renew spell by 10%. |
| **Spell Warding** | 5/5 | unchanged | Reduces all spell damage taken by 10%. |
| **Holy Nova** | 1/1 | changed | Causes an explosion of holy light around the caster, causing 26 to 30 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 49 to 57. These effects cause no threat. |

### Shadow (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Blackout** | 5/5 | moved | Gives your Shadow damage spells a 10% chance to stun the target for 3 sec. |
| **Shadow Focus** | 5/5 | changed | Improves your chance to hit with Shadow spells by 5%. |
| **Spirit Tap** | 1/5 | changed | Gives you a 20% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Shadow Reach** | 2/2 | changed | Increases the range of your offensive Shadow spells by 20%. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Your Mind Flay now deals 20% more damage, gains 10 yards increased range, but slows the target's movement speed by 20%. |
| **Improved Mind Blast** | 5/5 | changed | Reduces the cooldown of your Mind Blast spell by 2.5 sec. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage you deal by 2% for 15 sec, stacking up to 5 times. |
| **Early Demise** | 2/2 | **NEW** | Increases Shadow Word: Death's critical strike chance on targets at or below 20% health by 30%. |
| **Darkness** | 5/5 | changed | Increases your Shadow damage done by 10%. |
| **Shadowform** | 1/1 | changed | Assume Shadowform, increasing your Shadow damage by 10%, reducing the Mana cost of all Shadow spells by 50%, increasing the critical strike damage bonus of your Shadow spells by 100%, and reducing Physical damage taken by you by 15%. However, you may not cast healing spells while in this form. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Shadow | Blackout | 5 | 0/0/5 |
| 15-16 | Shadow | Shadow Reach | 2 | 0/0/7 |
| 17-19 | Shadow | Shadow Focus | 3 | 0/0/10 |
| 20 | Shadow | Mind Flay | 1 | 0/0/11 |
| 21-22 | Shadow | Improved Mind Flay | 2 | 0/0/13 |
| 23-24 | Shadow | Shadow Focus | 2 | 0/0/15 |
| 25 | Shadow | Shadow Weaving | 1 | 0/0/16 |
| 26 | Shadow | Vampiric Embrace | 1 | 0/0/17 |
| 27-28 | Shadow | Shadow Weaving | 2 | 0/0/19 |
| 29-33 | Shadow | Improved Mind Blast | 5 | 0/0/24 |
| 34 | Shadow | Spirit Tap | 1 | 0/0/25 |
| 35-36 | Shadow | Early Demise | 2 | 0/0/27 |
| 37-39 | Shadow | Darkness | 3 | 0/0/30 |
| 40 | Shadow | Shadowform | 1 | 0/0/31 |
| 41-42 | Shadow | Darkness | 2 | 0/0/33 |
| 43-47 | Discipline | Twin Disciplines | 5 | 5/0/33 |
| 48-50 | Holy | Twilight Focus | 3 | 5/3/33 |
| 51-52 | Holy | Improved Renew | 2 | 5/5/33 |
| 53-57 | Holy | Spell Warding | 5 | 5/10/33 |
| 58 | Holy | Holy Nova | 1 | 5/11/33 |
| 59-60 | Discipline | Improved Power Word: Shield | 2 | 7/11/33 |

## Core talents (priority order)

1. **Mind Flay** — Removing it costs 23.7 points of score in this model.
2. **Shadowform** — Removing it costs 13.2 points of score in this model.
3. **Shadow Weaving** — Removing it costs 2.2 points of score in this model.
4. **Improved Mind Flay** — Removing it costs 2.1 points of score in this model.
5. **Darkness** — Removing it costs 1.5 points of score in this model.
6. **Shadow Focus** — Removing it costs 0.7 points of score in this model.
7. **Blackout** — Removing it costs 0.7 points of score in this model.
8. **Shadow Reach** — Removing it costs 0.6 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level: Power Word: Shield and Inner Fire before the pull, Mind Blast at 30 yd, Shadow Word: Pain, Mind Flay channels (50% slow) and Mind Blast on cooldown while the mob walks in and once it is on you (the shield stops pushback while it holds), Vampiric Embrace and Devouring Plague heal, Shadow Word: Death below 20%, wand to finish without overkill; Psychic Scream and Desperate Prayer when health runs low. Between fights: 2 s loot, 6 s travel, Renew (not in Shadowform), conjured water below 35% mana, food below 65% health; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-09-27, on top of the priority below): SHIELD_BELOW = 0.5; never cast Smite; drink below 15% mana. Together +13.3% time per kill saved for `leveling-shadow` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/shadow-dps.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Mind Flay | 2.9 | 3.7 | 2.6 | 2.4 | 2.3 | 37% |
| Mind Blast | 2.0 | 2.0 | 1.9 | 1.9 | 1.8 | 29% |
| Shadow Word: Pain | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 17% |
| Shadow Word: Death | 0.0 | 0.0 | 1.0 | 0.9 | 0.9 | 17% |
| Vampiric Embrace | 0.0 | 0.5 | 0.4 | 0.4 | 0.4 | 0% |
| Wand | 2.2 | 0.6 | 0.0 | 0.0 | 0.0 | 0% |
| Devouring Plague | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: priest/talents/forever/optimizer/shadow-dps-leveling-st.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/priest>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
