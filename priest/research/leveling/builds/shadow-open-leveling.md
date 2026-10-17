# Shadow — Leveling (open talent search) — 17/2/32

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/2/32 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the shadow-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). +0.6% faster per kill than shadow-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Discipline (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Wand Specialization** | 1/2 | changed | Increases your damage with Wands by 13%. |
| **Holy Precision** | 1/3 | **NEW** | Improves your chance to hit with Holy spells by 6%. |
| **Martyrdom** | 2/2 | changed | Gives you a 100% chance to gain Focused Casting for 6 sec after being the victim of a melee or ranged critical strike. The Focused Casting effect prevents you from losing casting time when taking damage and increases your resistance to Interrupt effects by 20%. |
| **Mental Strength** | 1/5 | changed | Increases your total Intellect by 2%. |
| **Improved Power Word: Shield** | 1/3 | changed | Increases the damage absorbed by your Power Word: Shield by 7%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Mental Agility** | 2/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 7%. |

### Holy (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 2/3 | **NEW** | Gives you a 47% chance to avoid interruption caused by damage while casting any spell. |

### Shadow (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Blackout** | 4/5 | moved | Gives your Shadow damage spells a 8% chance to stun the target for 3 sec. |
| **Shadow Focus** | 3/5 | changed | Improves your chance to hit with Shadow spells by 3%. |
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Mind Blast** | 4/5 | changed | Reduces the cooldown of your Mind Blast spell by 2 sec. |
| **Shadow Reach** | 1/2 | changed | Increases the range of your offensive Shadow spells by 10%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Each instance of damage of Mind Flay deals 20% more damage than its previous instance of damage. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Shadow Weaving** | 2/3 | changed | Your Shadow damage spells have a 67% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Devouring Contagion** | 2/2 | **NEW** | Reduces the mana cost of your Devouring Plague by 50%.  Targets that die while Devouring Plague is active spreads it, jumping to 2 nearby enemies within 10 yds for the remaining duration. |
| **Darkness** | 5/5 | changed | Increases your Shadow damage done by 10%. |
| **Early Demise** | 1/2 | **NEW** | Increases Shadow Word: Death's critical strike chance on targets at or below 20% health by 15%. |
| **Shadowform** | 1/1 | changed | Assume Shadowform, increasing your Shadow damage by 10%, reducing the Mana cost of all Shadow spells by 50%, increasing the critical strike damage bonus of your Shadow spells by 100%, and reducing Physical damage taken by you by 15%. However, you may not cast healing spells while in this form. |

## Core talents (priority order)

1. **Shadowform** — +11.8 s per kill at level 60 without it (removal, 3,000 fights).
2. **Mind Flay** — +6.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Spirit Tap** — +3.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Shadow Weaving** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Darkness** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Mind Flay** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
7. **Meditation** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Vampiric Embrace** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +1.0% faster than the hand draft leveling-shadow, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.45; shadow-open-leveling 25.60, leveling-shadow 25.71, opt-shadow-dps-leveling-aoe 28.55, opt-shadow-dps-leveling-st 29.52, opt-shadow-dps-solo-60 29.52. The search simulated 49,778 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 17/2/32 -> 17/2/32; +1 Mental Strength (tier gating for Improved Power Word: Shield); -1 Mental Agility (over 51); order dropped (order_repair.py) (refill: the shadow-dps model, leveling-st).

## Open questions (verify in the live game)

- An open-search Shadow leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/0150112313-2-345001401201202151-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
