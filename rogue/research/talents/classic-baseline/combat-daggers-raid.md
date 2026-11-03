# Combat Daggers (raid DPS) — 15/31/5

*Rogue · Classic baseline*

| | |
|---|---|
| **Build** | 15/31/5 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Same Combat backbone (Precision, Dual Wield Specialization, Blade Flurry, Weapon Expertise, Adrenaline Rush) but Backstab replaces Sinister Strike, so Improved Backstab, Dagger Specialization and Opportunity are taken instead of Sword Specialization and Aggression. Requires standing behind the target; used when your best weapons are daggers.

## Point allocation

### Assassination (15)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Eviscerate** | 1/3 | Increases the damage done by your Eviscerate ability by 5%. |
| **Malice** | 5/5 | Increases your critical strike chance by 5%. |
| **Ruthlessness** | 3/3 | Gives your finishing moves a 60% chance to add a combo point to your target. |
| **Murder** | 2/2 | Increases all damage caused against Humanoid, Giant, Beast and Dragonkin targets by 2%. |
| **Improved Slice and Dice** | 3/3 | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | Your finishing moves have a 20% chance per combo point to restore 25 energy. |

### Combat (31)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Gouge** | 3/3 | Increases the effect duration of your Gouge ability by 1.5 sec. |
| **Lightning Reflexes** | 2/5 | Increases your Dodge chance by 2%. |
| **Improved Backstab** | 3/3 | Increases the critical strike chance of your Backstab ability by 30%. |
| **Precision** | 5/5 | Increases your chance to hit with melee weapons by 5%. |
| **Improved Sprint** | 2/2 | Gives a 100% chance to remove all movement impairing effects when you activate your Sprint ability. |
| **Dagger Specialization** | 5/5 | Increases your chance to get a critical strike with Daggers by 5%. |
| **Dual Wield Specialization** | 5/5 | Increases the damage done by your offhand weapon by 50%. |
| **Blade Flurry** | 1/1 | Increases your attack speed by 20%. In addition, attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Weapon Expertise** | 2/2 | Increases your skill with Sword, Fist and Dagger weapons by 5. |
| **Aggression** | 2/3 | Increases the damage of your Sinister Strike and Eviscerate abilities by 4%. |
| **Adrenaline Rush** | 1/1 | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (5)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Opportunity** | 5/5 | Increases the damage dealt when striking from behind with your Backstab, Garrote, or Ambush abilities by 20%. |

## Core talents (priority order)

1. **Improved Backstab** — +30% Backstab crit chance — the whole build revolves around Backstab crits.
2. **Dagger Specialization** — +5% crit with daggers.
3. **Opportunity** — +20% Backstab/Ambush damage.
4. **Weapon Expertise** — +5 dagger skill vs. level 63 bosses.
5. **Dual Wield Specialization** — +50% off-hand damage.
6. **Precision** — +5% hit.
7. **Blade Flurry** — Haste + cleave cooldown.
8. **Adrenaline Rush** — Energy cooldown.
9. **Relentless Strikes** — Energy on finishers.
10. **Improved Slice and Dice** — Longer SnD uptime.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Improved Gouge 3 + Lightning Reflexes 2 | Improved Sinister Strike + Lightning Reflexes | Tier-1 Combat filler; nothing there helps a Backstab rogue. |
| 2 | Aggression | Aggression 3 with Improved Eviscerate 0, Improved Kick | Aggression only affects Eviscerate for this build, so it is a filler at 2/3. |

## Notes

- Backstab requires being behind the target; on bosses that turn or cleave, the swords build is safer.
- Slower main-hand dagger (1.8) is best for Backstab; the off-hand should be fast for poison procs.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Assassination | Improved Eviscerate | 1 | unknown | not found in Forever data |
| Assassination | Malice | 5 | changed | tier 1, max 5 — tooltip changed |
| Assassination | Ruthlessness | 3 | unchanged | tier 2, max 3 |
| Assassination | Murder | 2 | unknown | not found in Forever data |
| Assassination | Improved Slice and Dice | 3 | unchanged | tier 2, max 3 |
| Assassination | Relentless Strikes | 1 | unchanged | tier 5, max 5 — moved in build 1.60.1.70753: was row 3, col 1; max rank 1 -> 5 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3, 4, 5) |
| Combat | Improved Gouge | 3 | moved-tree | now in Assassination, tier 1 |
| Combat | Lightning Reflexes | 2 | unchanged | tier 1, max 5 |
| Combat | Improved Backstab | 3 | **REMOVED** | removed from Classic |
| Combat | Precision | 5 | changed | tier 2, max 3 — max rank 5 → 3; tooltip changed |
| Combat | Improved Sprint | 2 | unchanged | tier 2, max 2 — moved in build 1.60.1.70753: was row 3, col 4 |
| Combat | Dagger Specialization | 5 | **REMOVED** | removed from Classic |
| Combat | Dual Wield Specialization | 5 | changed | tier 5, max 2 — tooltip changed; moved in build 1.60.1.70753: was row 4, col 3; max rank 5 -> 2 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2) |
| Combat | Blade Flurry | 1 | changed | tier 5, max 1 — tooltip changed |
| Combat | Weapon Expertise | 2 | changed | tier 4, max 2 — tooltip changed; moved in build 1.60.1.70753: was row 6, col 2; prerequisite changed in build 1.60.1.70753: was blade flurry |
| Combat | Aggression | 2 | changed | tier 4, max 3 — tooltip changed; moved in build 1.60.1.70753: was row 6, col 3; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3) |
| Combat | Adrenaline Rush | 1 | unchanged | tier 7, max 1 |
| Subtlety | Opportunity | 5 | changed | tier 1, max 5 — max rank 5 → 2; tooltip changed; max rank 2 -> 5 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3, 4, 5) |

**8 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/rogue-dps-pve-spec-builds-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
