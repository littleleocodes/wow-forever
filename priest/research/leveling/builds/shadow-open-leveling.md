# Shadow — Leveling (open talent search) — 16/3/32

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/3/32 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow leveling build the open leveling search found on 2026-10-21: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the shadow-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). +1.4% faster per kill than shadow-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Discipline (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Power in Light** | 2/5 | **NEW** | Your Smite and Penance spells deal 4% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain. |
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Mental Strength** | 3/5 | changed | Increases your total Intellect by 6%. |
| **Mental Agility** | 2/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 7%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Holy (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 3/3 | **NEW** | Gives you a 70% chance to avoid interruption caused by damage while casting any spell. |

### Shadow (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 4/5 | changed | Improves your chance to hit with Shadow spells by 4%. |
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Mind Blast** | 5/5 | changed | Reduces the cooldown of your Mind Blast spell by 2.5 sec. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Each instance of damage of Mind Flay deals 20% more damage than its previous instance of damage. |
| **Dark Inspiration** | 4/5 | moved | Your Mind Blast and fully channeled Mind Flay causes Dark Inspiration, increasing yours and your party's Spirit by 12% for 10 sec. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |
| **Early Demise** | 1/2 | **NEW** | Increases Shadow Word: Death's critical strike chance on targets at or below 20% health by 15%. |
| **Darkness** | 5/5 | changed | Increases your Shadow damage done by 10%. |
| **Shadowform** | 1/1 | changed | Assume Shadowform, increasing your Shadow damage by 10%, reducing the Mana cost of all Shadow spells by 50%, increasing the critical strike damage bonus of your Shadow spells by 100%, and reducing Physical damage taken by you by 15%. However, you may not cast healing spells while in this form. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Shadow | Spirit Tap | 5 | 0/0/5 |
| 15-18 | Shadow | Shadow Focus | 4 | 0/0/9 |
| 19 | Shadow | Improved Mind Blast | 1 | 0/0/10 |
| 20 | Shadow | Mind Flay | 1 | 0/0/11 |
| 21-22 | Shadow | Improved Mind Flay | 2 | 0/0/13 |
| 23-24 | Shadow | Improved Mind Blast | 2 | 0/0/15 |
| 25-27 | Shadow | Dark Inspiration | 3 | 0/0/18 |
| 28 | Shadow | Vampiric Embrace | 1 | 0/0/19 |
| 29-31 | Shadow | Shadow Weaving | 3 | 0/0/22 |
| 32-33 | Shadow | Improved Mind Blast | 2 | 0/0/24 |
| 34 | Shadow | Dark Inspiration | 1 | 0/0/25 |
| 35 | Shadow | Early Demise | 1 | 0/0/26 |
| 36-39 | Shadow | Darkness | 4 | 0/0/30 |
| 40 | Shadow | Shadowform | 1 | 0/0/31 |
| 41 | Shadow | Darkness | 1 | 0/0/32 |
| 42-46 | Discipline | Twin Disciplines | 5 | 5/0/32 |
| 47-49 | Holy | Twilight Focus | 3 | 5/3/32 |
| 50-52 | Discipline | Mental Strength | 3 | 8/3/32 |
| 53-54 | Discipline | Power in Light | 2 | 10/3/32 |
| 55 | Discipline | Inner Focus | 1 | 11/3/32 |
| 56-57 | Discipline | Mental Agility | 2 | 13/3/32 |
| 58-60 | Discipline | Meditation | 3 | 16/3/32 |

## Core talents (priority order)

1. **Shadowform** — +11.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Mind Flay** — +5.2 s per kill at level 60 without it (removal, 3,000 fights).
3. **Spirit Tap** — +3.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Darkness** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Mind Flay** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Vampiric Embrace** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Meditation** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Mind Blast** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +4.0% faster than the hand draft leveling-shadow, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 24.47; shadow-open-leveling 24.82, opt-shadow-dps-solo-60 24.97, leveling-shadow 25.46, opt-shadow-dps-leveling-aoe 28.67, opt-shadow-dps-leveling-st 30.44. The search simulated 48,045 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shadow leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/20500302103-3-40550001241300151-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
