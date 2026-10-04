# Marksmanship / Survival — Surefooted (raid DPS, 0/31/20) — 0/31/20

*Hunter · Classic baseline*

| | |
|---|---|
| **Build** | 0/31/20 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The same Marksmanship core with 20 points in Survival for Surefooted (+3% hit) and the slaying talents. Only worth running while you are below ~6% hit from gear; once hit comes from gear, go back to 20/31/0.

## Point allocation

### Beast Mastery (0)

*No points.*

### Marksmanship (31)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Efficiency** | 5/5 | Reduces the Mana cost of your Shots and Stings by 10%. |
| **Improved Hunter's Mark** | 3/5 | Increases the Ranged Attack Power bonus of your Hunter's Mark spell by 9%. |
| **Lethal Shots** | 5/5 | Increases your critical strike chance with ranged weapons by 5%. |
| **Aimed Shot** | 1/1 | An aimed shot that increases ranged damage by 70. |
| **Hawk Eye** | 3/3 | Increases the range of your ranged weapons by 6 yards. |
| **Mortal Shots** | 5/5 | Increases your ranged weapon critical strike damage bonus by 30%. |
| **Barrage** | 3/3 | Increases the damage done by your Multi-Shot and Volley spells by 15%. |
| **Ranged Weapon Specialization** | 5/5 | Increases the damage you deal with ranged weapons by 5%. |
| **Trueshot Aura** | 1/1 | Increases the attack power of party members within 45 yards by 50. Lasts 30 min. |

### Survival (20)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Monster Slaying** | 3/3 | Increases all damage caused against Beasts, Giants and Dragonkin targets by 3% and increases critical damage caused against Beasts, Giants and Dragonkin targets by an additional 3%. |
| **Humanoid Slaying** | 3/3 | Increases all damage caused against Humanoid targets by 3% and increases critical damage caused against Humanoid targets by an additional 3%. |
| **Deflection** | 5/5 | Increases your Parry chance by 5%. |
| **Survivalist** | 5/5 | Increases total health by 10%. |
| **Deterrence** | 1/1 | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Surefooted** | 3/3 | Increases hit chance by 3% and increases the chance movement impairing effects will be resisted by an additional 15%. |

## Core talents (priority order)

1. **Surefooted** — +3% hit and +15% snare resistance.
2. **Monster Slaying** — +3% damage and crit damage vs. Beasts, Giants, Dragonkin — most raid bosses.
3. **Humanoid Slaying** — +3% vs. Humanoids (many trash packs, some bosses).
4. **Trueshot Aura** — Group attack power.
5. **Lethal Shots** — Crit.
6. **Mortal Shots** — Crit damage.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 10 | Deflection 5 + Survivalist 5 | Savage Strikes + Improved Wing Clip, Entrapment | Pure filler to unlock Surefooted; Survivalist's +10% health is the least useless. |
| 1 | Deterrence | Clever Traps | Melee/PvP survival button. |

## Notes

- Loses Improved Aspect of the Hawk and pet damage — roughly a wash at 6% hit, worse above.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Marksmanship | Efficiency | 5 | changed | tier 2, max 5 — tooltip changed; was Marksmanship row 1, col 3 |
| Marksmanship | Improved Hunter's Mark | 3 | **REMOVED** | removed from Classic |
| Marksmanship | Lethal Shots | 5 | **REMOVED** | removed from Classic |
| Marksmanship | Aimed Shot | 1 | **REMOVED** | removed from Classic |
| Marksmanship | Hawk Eye | 3 | moved | tier 1, max 3 — was Marksmanship row 3, col 4 |
| Marksmanship | Mortal Shots | 5 | changed | tier 4, max 5 — tooltip changed |
| Marksmanship | Barrage | 3 | changed | tier 5, max 3 — tooltip changed; was Marksmanship row 5, col 2 |
| Marksmanship | Ranged Weapon Specialization | 5 | unchanged | tier 6, max 5 |
| Marksmanship | Trueshot Aura | 1 | changed | tier 4, max 1 — tooltip changed; was Marksmanship row 7, col 2; tooltip changed in build 1.60.1.70170 (ranks 1) |
| Survival | Monster Slaying | 3 | **REMOVED** | removed from Classic |
| Survival | Humanoid Slaying | 3 | **REMOVED** | removed from Classic |
| Survival | Deflection | 5 | changed | tier 1, max 5 — tooltip changed; tooltip changed in build 1.60.1.70170 (ranks 1, 2, 3, 4, 5) |
| Survival | Survivalist | 5 | changed | tier 2, max 5 — tooltip changed; was Survival row 3, col 2 |
| Survival | Deterrence | 1 | unchanged | tier 3, max 1 |
| Survival | Surefooted | 3 | changed | tier 3, max 3 — tooltip changed; was Survival row 4, col 2 |

**15 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/hunter-dps-pve-spec-builds-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
