# Fury — Dual Wield (raid DPS) — 17/34/0

*Warrior · Classic baseline*

| | |
|---|---|
| **Build** | 17/34/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The standard Classic raid DPS build. Everything is bent toward Bloodthirst, Dual Wield Specialization, Flurry and Death Wish, with Arms taken only as far as Impale (crit damage) and Anger Management (sustained rage). Highest sustained damage once hit and weapon skill are handled by gear.

## Point allocation

### Arms (17)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Heroic Strike** | 3/3 | Reduces the cost of your Heroic Strike ability by 3 rage points. |
| **Improved Rend** | 3/3 | Increases the bleed damage done by your Rend ability by 35%. |
| **Tactical Mastery** | 5/5 | You retain up to 25 of your rage points when you change stances. |
| **Anger Management** | 1/1 | Increases the time required for your rage to decay while out of combat by 30%. |
| **Deep Wounds** | 3/3 | Your critical strikes cause the opponent to bleed, dealing 60% of your melee weapon's average damage over 12 sec. |
| **Impale** | 2/2 | Increases the critical strike damage bonus of your abilities in Battle, Defensive, and Berserker stance by 20%. |

### Fury (34)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Cruelty** | 5/5 | Increases your chance to get a critical strike with melee weapons by 5%. |
| **Unbridled Wrath** | 5/5 | Gives you a 40% chance to generate an additional Rage point when you deal melee damage with a weapon. |
| **Improved Battle Shout** | 5/5 | Increases the melee attack power bonus of your Battle Shout by 25%. |
| **Dual Wield Specialization** | 5/5 | Increases the damage done by your offhand weapon by 25%. |
| **Improved Execute** | 2/2 | Reduces the Rage cost of your Execute ability by 5. |
| **Enrage** | 5/5 | Gives you a 25% melee damage bonus for 12 sec up to a maximum of 12 swings after being the victim of a critical strike. |
| **Death Wish** | 1/1 | When activated, increases your physical damage by 20% and makes you immune to Fear effects, but lowers your armor and all resistances by 20%. Lasts 30 sec. |
| **Flurry** | 5/5 | Increases your attack speed by 30% for your next 3 swings after dealing a melee critical strike. |
| **Bloodthirst** | 1/1 | Instantly attack the target causing damage equal to 45% of your attack power. In addition, the next 5 successful melee attacks will restore 10 health. This effect lasts 8 sec. |

### Protection (0)

*No points.*

## Core talents (priority order)

1. **Bloodthirst** — Main rage dump; scales with attack power and heals on hit. The reason to be 34 deep in Fury.
2. **Dual Wield Specialization** — +25% off-hand damage — the single biggest throughput talent for a dual-wielder.
3. **Flurry** — 30% haste after a crit; with raid crit levels it is up almost permanently.
4. **Cruelty** — +5% crit feeds Flurry, Deep Wounds and Impale.
5. **Death Wish** — +20% damage cooldown, also a fear break.
6. **Impale** — +20% crit damage on abilities.
7. **Enrage** — +25% damage after being crit; required for Flurry.
8. **Anger Management** — 1 rage / 3 sec keeps the rotation alive on low-rage pulls. Requires Tactical Mastery 5/5, which also makes stance dancing for Overpower/Whirlwind free.
9. **Deep Wounds** — Bleed on every crit; requires Improved Rend 3/3 in Classic.
10. **Unbridled Wrath** — Free rage on white hits; dual wield doubles the proc opportunities.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Improved Battle Shout | Booming Voice, Piercing Howl + Improved Cleave | Only one warrior per group needs Improved Battle Shout. Others can take Booming Voice or utility. |
| 3 | Improved Heroic Strike | Improved Overpower, Improved Charge | Heroic Strike is the rage dump when rage-capped; the cost reduction is a real DPS gain in good gear. |
| 2 | Improved Execute | Improved Berserker Rage | Cheaper Executes in the sub-20% phase. |

## Notes

- Requires roughly 9% hit (with 300 weapon skill) before dual wield out-damages a two-hander; use the 2H variant until then.
- Stance dance: Battle Stance for Overpower after a dodge, Berserker Stance otherwise. Tactical Mastery makes this free.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Arms | Improved Heroic Strike | 3 | changed | tier 1, max 3 — tooltip changed |
| Arms | Improved Rend | 3 | changed | tier 1, max 3 — tooltip changed |
| Arms | Tactical Mastery | 5 | **REMOVED** | removed from Classic |
| Arms | Anger Management | 1 | changed | tier 3, max 1 — tooltip changed |
| Arms | Deep Wounds | 3 | changed | tier 3, max 3 — tooltip changed |
| Arms | Impale | 2 | changed | tier 4, max 2 — tooltip changed |
| Fury | Cruelty | 5 | changed | tier 1, max 5 — tooltip changed |
| Fury | Unbridled Wrath | 5 | changed | tier 2, max 5 — tooltip changed; tooltip changed in build 1.60.1.70170 (ranks 1, 2, 3, 4, 5) |
| Fury | Improved Battle Shout | 5 | **REMOVED** | removed from Classic |
| Fury | Dual Wield Specialization | 5 | changed | tier 4, max 5 — tooltip changed; tooltip changed in build 1.60.1.70170 (ranks 1, 2, 3, 4, 5) |
| Fury | Improved Execute | 2 | changed | tier 4, max 2 — tooltip changed; was Fury row 4, col 2 |
| Fury | Enrage | 5 | changed | tier 4, max 5 — tooltip changed |
| Fury | Death Wish | 1 | changed | tier 5, max 1 — tooltip changed |
| Fury | Flurry | 5 | changed | tier 6, max 5 — tooltip changed; moved in build 1.60.1.70170: was row 6, col 3; prerequisite changed in build 1.60.1.70170: was enrage |
| Fury | Bloodthirst | 1 | changed | tier 7, max 1 — tooltip changed; tooltip changed in build 1.60.1.70170 (ranks 1); prerequisite changed in build 1.60.1.70170: was death wish |

**10 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/warrior-dps-pve-spec-builds-talents>
- <https://www.wowhead.com/classic/guide/classes/warrior/fury/dps-talent-builds-pve>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
