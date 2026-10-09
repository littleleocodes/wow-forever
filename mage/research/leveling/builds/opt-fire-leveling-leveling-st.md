# Optimizer — Single-target Fireball leveling: Fireball ~60%, Fire Blast, Scorch (22+), wand (leveling-st) — 0/33/18

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/33/18 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fire-leveling` and profile `leveling-st`: score +64.6% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (0)

*No points.*

### Fire (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Flame Throwing** | 2/2 | unchanged | Increases the range of your Fire spells by 6 yards. |
| **Impact** | 3/3 | changed | Gives your Fire spells a 10% chance to stun the target for 2 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Blast Wave** | 1/1 | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. |
| **Fire Power** | 5/5 | unchanged | Increases the damage done by your Fire spells by 10%. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Permafrost** | 1/3 | changed | Increases the duration of your Chill effects by 11% and reduces the target's speed by an additional 3%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 2/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 33%. |

## Core talents (priority order)

1. **Ice Lance** — Removing it costs 24.3 points of score in this model.
2. **Ignite** — Removing it costs 6.7 points of score in this model.
3. **Fire Power** — Removing it costs 3.2 points of score in this model.
4. **Combustion** — Removing it costs 2.3 points of score in this model.
5. **Elemental Precision** — Removing it costs 1.3 points of score in this model.
6. **Ice Block** — Removing it costs 1.1 points of score in this model.
7. **Burning Soul** — Removing it costs 1.0 points of score in this model.
8. **Shatter** — Removing it costs 0.7 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level: pull at max range, the mob walks in at 7 yd/s (slowed by chills), swings every 2 s once in melee (pushing casts back), Frost Nova when it arrives, a 2-second step back, Ice Lance/Frostbolt into the freeze, Fire Blast and wand to finish without overkill. Between fights: 2 s loot, 6 s travel, Evocation when low, conjured water below 35% mana, food below 65% health; a death costs 90 s. Every hit, miss, crit, partial resist, chill, freeze, proc and pushback is rolled.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-09-27, on top of the priority below): Fireball only while the mob has more than 20% health; Fire Blast only while the mob has more than 10% health; Scorch only above 50% mana. Together +0.8% time per kill saved for `opt-fire-leveling-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/fire-leveling.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Ice Lance | 1.1 | 1.6 | 2.3 | 2.0 | 2.0 | 42% |
| Fireball | 2.3 | 1.8 | 1.9 | 1.8 | 1.8 | 28% |
| Fire Blast | 1.0 | 1.1 | 1.4 | 1.2 | 1.2 | 16% |
| Frost Nova | 0.4 | 0.6 | 0.7 | 0.7 | 0.7 | 1% |
| Wand | 0.6 | 0.2 | 0.4 | 0.3 | 0.3 | 0% |
| Blast Wave | 0.0 | 0.2 | 0.3 | 0.3 | 0.3 | 4% |
| Scorch | 0.0 | 0.2 | 0.3 | 0.2 | 0.2 | 1% |
| Counterspell | 0.0 | 0.1 | 0.1 | 0.1 | 0.1 | 0% |

## Notes

- Report: mage/talents/forever/optimizer/fire-leveling-leveling-st.md
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Hot Streak 1 out; Heating Up 1 in; to be re-optimized.

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
