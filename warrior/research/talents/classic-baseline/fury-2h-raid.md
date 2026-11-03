# Fury — Two-Handed / Improved Slam (raid DPS) — 17/34/0

*Warrior · Classic baseline*

| | |
|---|---|
| **Build** | 17/34/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Identical to the dual-wield build except Dual Wield Specialization is swapped for Improved Slam. Better than dual wield until you have the hit and weapon skill to make two weapons connect, and always strong for Horde with Windfury Totem.

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
| **Improved Execute** | 2/2 | Reduces the Rage cost of your Execute ability by 5. |
| **Enrage** | 5/5 | Gives you a 25% melee damage bonus for 12 sec up to a maximum of 12 swings after being the victim of a critical strike. |
| **Improved Slam** | 5/5 | Decreases the casting time of your Slam ability by 0.5 sec. |
| **Death Wish** | 1/1 | When activated, increases your physical damage by 20% and makes you immune to Fear effects, but lowers your armor and all resistances by 20%. Lasts 30 sec. |
| **Flurry** | 5/5 | Increases your attack speed by 30% for your next 3 swings after dealing a melee critical strike. |
| **Bloodthirst** | 1/1 | Instantly attack the target causing damage equal to 45% of your attack power. In addition, the next 5 successful melee attacks will restore 10 health. This effect lasts 8 sec. |

### Protection (0)

*No points.*

## Core talents (priority order)

1. **Improved Slam** — Cuts Slam to a 1.0s cast so it fits between auto-attacks — the entire point of the 2H variant.
2. **Bloodthirst** — Still the primary rage dump.
3. **Flurry** — Haste on crit.
4. **Death Wish** — Burst cooldown.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Improved Battle Shout | Booming Voice, Piercing Howl + Improved Cleave | Same as the dual-wield build. |

## Notes

- Slam must be timed immediately after a white swing so it does not reset the swing timer — a swing-timer addon is mandatory for this build.

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
| Fury | Unbridled Wrath | 5 | changed | tier 2, max 5 — tooltip changed; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3, 4, 5) |
| Fury | Improved Battle Shout | 5 | **REMOVED** | removed from Classic |
| Fury | Improved Execute | 2 | changed | tier 4, max 2 — tooltip changed; was Fury row 4, col 2 |
| Fury | Enrage | 5 | changed | tier 3, max 5 — tooltip changed; moved in build 1.60.1.70753: was row 4, col 3 |
| Fury | Improved Slam | 5 | moved-tree | now in Arms, tier 6 |
| Fury | Death Wish | 1 | changed | tier 5, max 1 — tooltip changed |
| Fury | Flurry | 5 | changed | tier 6, max 3 — tooltip changed; moved in build 1.60.1.70753: was row 6, col 3; max rank 5 -> 3 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3); prerequisite changed in build 1.60.1.70753: was enrage |
| Fury | Bloodthirst | 1 | changed | tier 7, max 1 — tooltip changed; tooltip changed in build 1.60.1.70753 (ranks 1) |

**10 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/warrior-dps-pve-spec-builds-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
