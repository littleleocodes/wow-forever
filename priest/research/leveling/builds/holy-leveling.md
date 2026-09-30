# Holy — Leveling (derived) — 2/30/19

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 2/30/19 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Holy build, 30+ points kept in Holy, playing the holy-leveling rotation; the talent order is the stats model's (shadow-dps). Holy is a healing spec: this is how to level while keeping it, compared with Shadow on the leveling page.

## Point allocation

### Discipline (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |

### Holy (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Renew** | 1/3 | unchanged | Increases the amount healed by your Renew spell by 5%. |
| **Holy Specialization** | 5/5 | unchanged | Increases the critical effect chance of your Holy spells by 5%. |
| **Spell Warding** | 5/5 | unchanged | Reduces all spell damage taken by 10%. |
| **Divine Fury** | 5/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.5 sec. |
| **Holy Nova** | 1/1 | changed | Causes an explosion of holy light around the caster, causing 26 to 30 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 49 to 57. These effects cause no threat. |
| **Blessed Recovery** | 1/3 | changed | After being struck by a melee or ranged critical hit, or suffering more than 30% of your maximum Health from a single attack, heal 8% of the damage taken over 6 sec. Refreshing this effect carries over any remaining healing. |
| **Inspiration** | 3/3 | changed | Your non-periodic critical heals increase your target's Armor by 25% for 15 sec. |
| **Holy Reach** | 1/2 | unchanged | Increases the range of your Smite and Holy Fire spells and the radius of your Prayer of Healing and Holy Nova spells by 10%. |
| **Spirit of Redemption** | 1/1 | changed | Upon death, the priest becomes the Spirit of Redemption for 15 sec. The Spirit of Redemption cannot move, attack, be attacked or targeted by any spells or effects. While in this form the priest can cast any healing spell free of cost. When the effect ends, the priest dies. |
| **Spiritual Guidance** | 5/5 | changed | Increases your spell healing by up to 25% of your total Spirit and your spell damage by up to 8% of your total Spirit. |
| **Searing Light** | 2/2 | changed | Increases your Holy damage done by 5%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana. |

### Shadow (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 3/5 | changed | Improves your chance to hit with Shadow spells by 3%. |
| **Blackout** | 3/5 | moved | Gives your Shadow damage spells a 6% chance to stun the target for 3 sec. |
| **Shadow Reach** | 2/2 | changed | Increases the range of your offensive Shadow spells by 20%. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Your Mind Flay now deals 20% more damage, gains 10 yards increased range, but slows the target's movement speed by 20%. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage you deal by 2% for 15 sec, stacking up to 5 times. |
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to gain a 100% bonus to your Spirit for 15 sec after killing a non-trivial target. For the duration, your Mana will regenerate at a 50% of normal rate while casting. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-12 | Shadow | Blackout | 3 | 0/0/3 |
| 13-14 | Shadow | Shadow Focus | 2 | 0/0/5 |
| 15-16 | Shadow | Shadow Reach | 2 | 0/0/7 |
| 17 | Shadow | Shadow Focus | 1 | 0/0/8 |
| 18-19 | Shadow | Spirit Tap | 2 | 0/0/10 |
| 20 | Shadow | Mind Flay | 1 | 0/0/11 |
| 21-22 | Shadow | Improved Mind Flay | 2 | 0/0/13 |
| 23-24 | Shadow | Spirit Tap | 2 | 0/0/15 |
| 25-27 | Shadow | Shadow Weaving | 3 | 0/0/18 |
| 28 | Holy | Improved Renew | 1 | 0/1/18 |
| 29-32 | Holy | Holy Specialization | 4 | 0/5/18 |
| 33-37 | Holy | Spell Warding | 5 | 0/10/18 |
| 38 | Holy | Holy Nova | 1 | 0/11/18 |
| 39 | Holy | Blessed Recovery | 1 | 0/12/18 |
| 40 | Holy | Holy Specialization | 1 | 0/13/18 |
| 41-45 | Holy | Divine Fury | 5 | 0/18/18 |
| 46-48 | Holy | Inspiration | 3 | 0/21/18 |
| 49 | Holy | Holy Reach | 1 | 0/22/18 |
| 50 | Holy | Spirit of Redemption | 1 | 0/23/18 |
| 51 | Shadow | Spirit Tap | 1 | 0/23/19 |
| 52-56 | Holy | Spiritual Guidance | 5 | 0/28/19 |
| 57-58 | Discipline | Wand Specialization | 2 | 2/28/19 |
| 59-60 | Holy | Searing Light | 2 | 2/30/19 |

## Core talents (priority order)

1. **Mind Flay** — The scorer's value in this build: +75.5% of its score (model shadow-dps).
2. **Shadow Weaving** — The scorer's value in this build: +6.8% of its score (model shadow-dps).
3. **Improved Mind Flay** — The scorer's value in this build: +6.6% of its score (model shadow-dps).
4. **Shadow Reach** — The scorer's value in this build: +2.0% of its score (model shadow-dps).
5. **Blackout** — The scorer's value in this build: +1.7% of its score (model shadow-dps).
6. **Shadow Focus** — The scorer's value in this build: +1.3% of its score (model shadow-dps).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Fight-lab talent search (fightlab/fl_talent_opt.py): start derived-holy-scorer, moves: 2 points Shadow Focus -> Spirit Tap; 2 points Blackout -> Spirit Tap; 3 points Twilight Focus -> Spiritual Guidance; 2 points Twin Disciplines -> Wand Specialization; 1 point Vampiric Embrace -> Spirit Tap; 2 points Improved Renew -> Spiritual Guidance; 2 points Blessed Recovery -> Searing Light. Race against derived-holy-scorer over levels 20-60 (seed 3, 3000 fights per level): +6.3% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- A derived Holy leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
