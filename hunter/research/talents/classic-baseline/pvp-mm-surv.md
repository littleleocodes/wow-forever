# Marksmanship / Survival (PvP, 0/31/20) — 0/31/20

*Hunter · Classic baseline*

| | |
|---|---|
| **Build** | 0/31/20 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — PvP |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Scatter Shot, Improved Concussive Shot stuns, Aimed Shot burst and Trueshot Aura from Marksmanship; Improved Wing Clip, Deterrence, Surefooted and Improved Feign Death from Survival for kiting.

## Point allocation

### Beast Mastery (0)

*No points.*

### Marksmanship (31)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Concussive Shot** | 5/5 | Gives your Concussive Shot a 20% chance to stun the target for 3 sec. |
| **Efficiency** | 2/5 | Reduces the Mana cost of your Shots and Stings by 4%. |
| **Lethal Shots** | 5/5 | Increases your critical strike chance with ranged weapons by 5%. |
| **Aimed Shot** | 1/1 | An aimed shot that increases ranged damage by 70. |
| **Hawk Eye** | 3/3 | Increases the range of your ranged weapons by 6 yards. |
| **Mortal Shots** | 5/5 | Increases your ranged weapon critical strike damage bonus by 30%. |
| **Scatter Shot** | 1/1 | A short-range shot that deals 50% weapon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used. |
| **Barrage** | 3/3 | Increases the damage done by your Multi-Shot and Volley spells by 15%. |
| **Ranged Weapon Specialization** | 5/5 | Increases the damage you deal with ranged weapons by 5%. |
| **Trueshot Aura** | 1/1 | Increases the attack power of party members within 45 yards by 50. Lasts 30 min. |

### Survival (20)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Humanoid Slaying** | 3/3 | Increases all damage caused against Humanoid targets by 3% and increases critical damage caused against Humanoid targets by an additional 3%. |
| **Monster Slaying** | 2/3 | Increases all damage caused against Beasts, Giants and Dragonkin targets by 2% and increases critical damage caused against Beasts, Giants and Dragonkin targets by an additional 2%. |
| **Improved Wing Clip** | 5/5 | Gives your Wing Clip ability a 20% chance to immobilize the target for 5 sec. |
| **Survivalist** | 4/5 | Increases total health by 8%. |
| **Deterrence** | 1/1 | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Surefooted** | 3/3 | Increases hit chance by 3% and increases the chance movement impairing effects will be resisted by an additional 15%. |
| **Improved Feign Death** | 2/2 | Reduces the chance your Feign Death ability will be resisted by 4%. |

## Core talents (priority order)

1. **Scatter Shot** — Instant 4s disorient — trap setup and Aimed Shot window.
2. **Improved Concussive Shot** — 20% chance to stun on Concussive Shot.
3. **Improved Wing Clip** — 20% root chance on Wing Clip — kite setup.
4. **Aimed Shot** — Big burst shot after Scatter Shot / a Wing Clip root (Classic Aimed Shot has no healing debuff).
5. **Deterrence** — +25% dodge/parry for 10s.
6. **Surefooted** — +3% hit and snare resistance.
7. **Humanoid Slaying** — +3% vs. players.
8. **Improved Feign Death** — Feign Death resisted less often.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 6 | Monster Slaying 2 + Survivalist 4 | Deflection, Savage Strikes, Entrapment | Filler to reach tier 2 and tier 4 of Survival; Survivalist's health is the least useless. |
| 2 | Efficiency | Improved Hunter's Mark | Marksmanship filler. |

## Notes

- Aimed Shot in Classic has no healing debuff (that is later expansions); its role here is burst after Scatter Shot.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Marksmanship | Improved Concussive Shot | 5 | unchanged | tier 1, max 5 |
| Marksmanship | Efficiency | 2 | changed | tier 2, max 5 — tooltip changed; was Marksmanship row 1, col 3 |
| Marksmanship | Lethal Shots | 5 | **REMOVED** | removed from Classic |
| Marksmanship | Aimed Shot | 1 | **REMOVED** | removed from Classic |
| Marksmanship | Hawk Eye | 3 | moved | tier 1, max 3 — was Marksmanship row 3, col 4 |
| Marksmanship | Mortal Shots | 5 | changed | tier 4, max 5 — tooltip changed |
| Marksmanship | Scatter Shot | 1 | moved | tier 5, max 1 — was Marksmanship row 5, col 1 |
| Marksmanship | Barrage | 3 | changed | tier 5, max 3 — tooltip changed; was Marksmanship row 5, col 2 |
| Marksmanship | Ranged Weapon Specialization | 5 | unchanged | tier 6, max 5 |
| Marksmanship | Trueshot Aura | 1 | changed | tier 4, max 1 — tooltip changed; was Marksmanship row 7, col 2; tooltip changed in build 1.60.1.70425 (ranks 1) |
| Survival | Humanoid Slaying | 3 | **REMOVED** | removed from Classic |
| Survival | Monster Slaying | 2 | **REMOVED** | removed from Classic |
| Survival | Improved Wing Clip | 5 | changed | tier 2, max 3 — max rank 5 → 3; tooltip changed; was Survival row 2, col 3 |
| Survival | Survivalist | 4 | changed | tier 2, max 5 — tooltip changed; was Survival row 3, col 2 |
| Survival | Deterrence | 1 | unchanged | tier 3, max 1 |
| Survival | Surefooted | 3 | changed | tier 3, max 3 — tooltip changed; was Survival row 4, col 2 |
| Survival | Improved Feign Death | 2 | **REMOVED** | removed from Classic |

**13 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/hunter/dps-pvp-arena>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
