# Combat Swords (raid DPS) — 19/32/0

*Rogue · Classic baseline*

| | |
|---|---|
| **Build** | 19/32/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The default Classic raid rogue: Sinister Strike + Slice and Dice with Sword Specialization extra attacks, Blade Flurry and Adrenaline Rush. Weapon Expertise takes you to 305 sword skill against level-63 bosses, which is why Combat is mandatory. Assassination adds Malice, Ruthlessness, Relentless Strikes and Improved Slice and Dice for the finisher cycle.

## Point allocation

### Assassination (19)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Eviscerate** | 3/3 | Increases the damage done by your Eviscerate ability by 15%. |
| **Malice** | 5/5 | Increases your critical strike chance by 5%. |
| **Ruthlessness** | 3/3 | Gives your finishing moves a 60% chance to add a combo point to your target. |
| **Murder** | 2/2 | Increases all damage caused against Humanoid, Giant, Beast and Dragonkin targets by 2%. |
| **Improved Slice and Dice** | 3/3 | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | Your finishing moves have a 20% chance per combo point to restore 25 energy. |
| **Lethality** | 2/5 | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Ghostly Strike, and Hemorrhage abilities by 12%. |

### Combat (32)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Sinister Strike** | 2/2 | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 4/5 | Increases your Dodge chance by 4%. |
| **Precision** | 5/5 | Increases your chance to hit with melee weapons by 5%. |
| **Endurance** | 2/2 | Reduces the cooldown of your Sprint and Evasion abilities by 1.5 min. |
| **Improved Sprint** | 2/2 | Gives a 100% chance to remove all movement impairing effects when you activate your Sprint ability. |
| **Dual Wield Specialization** | 5/5 | Increases the damage done by your offhand weapon by 50%. |
| **Blade Flurry** | 1/1 | Increases your attack speed by 20%. In addition, attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Sword Specialization** | 5/5 | Gives you a 5% chance to get an extra attack on the same target after dealing damage with your Sword. |
| **Weapon Expertise** | 2/2 | Increases your skill with Sword, Fist and Dagger weapons by 5. |
| **Aggression** | 3/3 | Increases the damage of your Sinister Strike and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Weapon Expertise** — +5 sword/dagger/fist skill: removes most glancing-blow penalty and adds hit/crit against level 63 bosses. Non-negotiable.
2. **Sword Specialization** — 5% chance per hit for an extra attack — scales with every white and yellow hit.
3. **Dual Wield Specialization** — +50% off-hand damage.
4. **Precision** — +5% hit; rogues need a lot of hit for the off-hand.
5. **Blade Flurry** — +20% haste and a cleave for 15s — used every cooldown.
6. **Adrenaline Rush** — Doubled energy regeneration for 15s.
7. **Improved Sinister Strike** — -5 energy on the main builder.
8. **Malice** — +5% crit.
9. **Improved Slice and Dice** — +45% duration; lets you keep SnD up with 1-2 point finishers.
10. **Relentless Strikes** — Energy refund on finishers.
11. **Ruthlessness** — Free combo point after finishers.
12. **Aggression** — +6% Sinister Strike and Eviscerate damage.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 4 | Lightning Reflexes | Improved Gouge | Filler to reach tier 2 of Combat; Improved Gouge is better if you bandage in dungeons. |
| 4 | Endurance 2 + Improved Sprint 2 | Improved Kick, Riposte (needs Deflection 5) | Filler to reach 15 points for Dual Wield Specialization. |
| 2 | Lethality | Improved Eviscerate (already 3/3), Improved Expose Armor | Crit damage on Sinister Strike. |
| 2 | Murder | Remorseless Attacks | +2% damage to Humanoids/Giants/Beasts/Dragonkin covers most raid bosses. |

## Notes

- Rotation: Sinister Strike to 2-3 combo points -> Slice and Dice, then Sinister Strike to 5 -> Eviscerate (or Rupture on non-armored targets late).
- One rogue per raid maintains Expose Armor only if there is no Improved Sunder Armor warrior; otherwise Sunder is better.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Assassination | Improved Eviscerate | 3 | unknown | not found in Forever data |
| Assassination | Malice | 5 | changed | tier 1, max 5 — tooltip changed |
| Assassination | Ruthlessness | 3 | unchanged | tier 2, max 3 |
| Assassination | Murder | 2 | unknown | not found in Forever data |
| Assassination | Improved Slice and Dice | 3 | unchanged | tier 2, max 3 |
| Assassination | Relentless Strikes | 1 | unchanged | tier 5, max 5 — moved in build 1.60.1.70753: was row 3, col 1; max rank 1 -> 5 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3, 4, 5) |
| Assassination | Lethality | 2 | changed | tier 3, max 2 — tooltip changed; max rank 5 -> 2 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2) |
| Combat | Improved Sinister Strike | 2 | unknown | not found in Forever data |
| Combat | Lightning Reflexes | 4 | unchanged | tier 1, max 5 |
| Combat | Precision | 5 | changed | tier 2, max 3 — max rank 5 → 3; tooltip changed |
| Combat | Endurance | 2 | changed | tier 3, max 2 — tooltip changed |
| Combat | Improved Sprint | 2 | unchanged | tier 2, max 2 — moved in build 1.60.1.70753: was row 3, col 4 |
| Combat | Dual Wield Specialization | 5 | changed | tier 5, max 2 — tooltip changed; moved in build 1.60.1.70753: was row 4, col 3; max rank 5 -> 2 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2) |
| Combat | Blade Flurry | 1 | changed | tier 5, max 1 — tooltip changed |
| Combat | Sword Specialization | 5 | **REMOVED** | removed from Classic |
| Combat | Weapon Expertise | 2 | changed | tier 4, max 2 — tooltip changed; moved in build 1.60.1.70753: was row 6, col 2; prerequisite changed in build 1.60.1.70753: was blade flurry |
| Combat | Aggression | 3 | changed | tier 4, max 3 — tooltip changed; moved in build 1.60.1.70753: was row 6, col 3; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3) |
| Combat | Adrenaline Rush | 1 | unchanged | tier 7, max 1 |

**5 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/rogue-dps-pve-spec-builds-talents>
- <https://www.wowhead.com/classic/guide/classes/rogue/dps-talent-builds-pve>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
