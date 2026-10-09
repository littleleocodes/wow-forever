# Shadow — Leveling (open talent search) — 18/0/33

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/0/33 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow leveling build the open leveling search found on 2026-10-08: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the shadow-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). +1.0% faster per kill than leveling-shadow, the fastest of our leveling builds in that race.

## Point allocation

### Discipline (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 1/2 | changed | Increases your damage with Wands by 13%. |
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Holy Precision** | 1/3 | **NEW** | Improves your chance to hit with Holy spells by 6%. |
| **Improved Power Word: Shield** | 3/3 | changed | Increases the damage absorbed by your Power Word: Shield by 20%. |
| **Mental Agility** | 3/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Improved Inner Fire** | 1/3 | changed | Increases the Armor bonus of your Inner Fire spell by 15% and increases its total charges by 4. |

### Holy (0)

*No points.*

### Shadow (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 3/5 | changed | Improves your chance to hit with Shadow spells by 3%. |
| **Blackout** | 4/5 | moved | Gives your Shadow damage spells a 8% chance to stun the target for 3 sec. |
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Shadow Reach** | 2/2 | changed | Increases the range of your offensive Shadow spells by 20%. |
| **Improved Mind Blast** | 4/5 | changed | Reduces the cooldown of your Mind Blast spell by 2 sec. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Your Mind Flay now deals 20% more damage, gains 10 yards increased range, but slows the target's movement speed by 20%. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Shadow Weaving** | 2/3 | changed | Your Shadow damage spells have a 67% chance to increase the Shadow damage you deal by 2% for 15 sec, stacking up to 5 times. |
| **Devouring Contagion** | 2/2 | **NEW** | Reduces the mana cost of your Devouring Plague by 50%.  Targets that die while Devouring Plague is active spreads it, jumping to a nearby enemy within 10 yds for the remaining duration. |
| **Early Demise** | 1/2 | **NEW** | Increases Shadow Word: Death's critical strike chance on targets at or below 20% health by 15%. |
| **Darkness** | 5/5 | changed | Increases your Shadow damage done by 10%. |
| **Shadowform** | 1/1 | changed | Assume Shadowform, increasing your Shadow damage by 10%, reducing the Mana cost of all Shadow spells by 50%, increasing the critical strike damage bonus of your Shadow spells by 100%, and reducing Physical damage taken by you by 15%. However, you may not cast healing spells while in this form. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-13 | Shadow | Blackout | 4 | 0/0/4 |
| 14 | Shadow | Shadow Focus | 1 | 0/0/5 |
| 15-16 | Shadow | Shadow Reach | 2 | 0/0/7 |
| 17-18 | Shadow | Shadow Focus | 2 | 0/0/9 |
| 19 | Shadow | Spirit Tap | 1 | 0/0/10 |
| 20 | Shadow | Mind Flay | 1 | 0/0/11 |
| 21-22 | Shadow | Improved Mind Flay | 2 | 0/0/13 |
| 23-24 | Shadow | Improved Mind Blast | 2 | 0/0/15 |
| 25 | Shadow | Vampiric Embrace | 1 | 0/0/16 |
| 26-27 | Shadow | Shadow Weaving | 2 | 0/0/18 |
| 28-31 | Shadow | Spirit Tap | 4 | 0/0/22 |
| 32-33 | Shadow | Improved Mind Blast | 2 | 0/0/24 |
| 34 | Shadow | Devouring Contagion | 1 | 0/0/25 |
| 35 | Shadow | Early Demise | 1 | 0/0/26 |
| 36-39 | Shadow | Darkness | 4 | 0/0/30 |
| 40 | Shadow | Shadowform | 1 | 0/0/31 |
| 41 | Shadow | Darkness | 1 | 0/0/32 |
| 42-46 | Discipline | Twin Disciplines | 5 | 5/0/32 |
| 47-49 | Discipline | Improved Power Word: Shield | 3 | 8/0/32 |
| 50 | Discipline | Wand Specialization | 1 | 9/0/32 |
| 51 | Discipline | Holy Precision | 1 | 10/0/32 |
| 52 | Discipline | Inner Focus | 1 | 11/0/32 |
| 53-55 | Discipline | Mental Agility | 3 | 14/0/32 |
| 56 | Discipline | Meditation | 1 | 15/0/32 |
| 57 | Discipline | Improved Inner Fire | 1 | 16/0/32 |
| 58-59 | Discipline | Meditation | 2 | 18/0/32 |
| 60 | Shadow | Devouring Contagion | 1 | 18/0/33 |

## Core talents (priority order)

1. **Shadowform** — +11.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Mind Flay** — +7.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Spirit Tap** — +3.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Shadow Weaving** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Darkness** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Mind Flay** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
7. **Meditation** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Early Demise** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +1.0% faster than the hand draft leveling-shadow, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.57; leveling-shadow 25.83, opt-shadow-dps-leveling-aoe 28.63, opt-shadow-dps-leveling-st 29.49, opt-shadow-dps-solo-60 29.49. The search simulated 47,721 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shadow leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/01501303131--345002401201202151-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
