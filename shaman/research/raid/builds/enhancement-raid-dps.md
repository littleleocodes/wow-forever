# Enhancement — Stormstrike / Maelstrom Weapon (simulator winner adopted 2026-09-27) — 11/31/9

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/31/9 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `enhancement-raid-support` |

## Summary

Allocation adopted on 2026-09-27 from `opt-enhancement-dps-raid-dps`, the best build in the community simulator (+2.8% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Improved Weapon Totems, Enhancing Totems and Weapon Mastery are gone, so Enhancement stops being a totem-support spec and becomes a melee DPS: Stormstrike at 16 points, Flurry, Mental Dexterity (AP from Intellect), Elemental Weapons, Spirit Weapons (parry + threat control), Mental Quickness, Improved Stormstrike, Maelstrom Weapon (instant Lightning Bolts) and the Rage of the Farseer capstone (+30% attack and cast speed). Concussion/Reverberation for shocks, Tidal Focus for hit.

## Point allocation

### Elemental (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Concussion** | 2/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 2%. |
| **Elemental Devastation** | 3/3 | changed | Your offensive spell critical strikes will increase your chance to get a critical strike with melee attacks by 9% for 10 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |

### Enhancement (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Elemental Weapons** | 3/3 | moved | Increases the melee attack power bonus of your Rockbiter Weapon by 20%, your Windfury Weapon effect by 40% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 15%. |
| **Stormstrike** | 1/1 | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Flurry** | 5/5 | changed | Increases your attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Maelstrom Weapon** | 5/5 | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 20%. Stacks up to 5 times. Lasts 30 sec. |
| **Rage of the Farseer** | 1/1 | **NEW** | Increases your attack speed by 30% for 25 sec. |

### Restoration (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |
| **Tidal Focus** | 4/5 | changed | Reduces the Mana cost of your healing spells by 4% and improves your chance to hit by 4%. |

## Core talents (priority order)

1. **Maelstrom Weapon** — New: melee hits stack -4%/rank cast time and mana on the next Lightning Bolt (5 stacks) — instant Lightning Bolts between swings. Raid sim (2026-09-27): the simulator's rotation reads this talent's own proc, so its removal run breaks the rotation and is not its value.
2. **Stormstrike** — Now the 16-point talent: weapon strike + 20% Nature damage taken for 12s. Raid sim (2026-09-27): removing it costs +19% DPS.
3. **Flurry** — Haste after crits (demo rank 1 = 5%); requires Mental Dexterity 3. Raid sim (2026-09-27): removing it costs +10% DPS.
4. **Thundering Strikes** — +5% crit with all spells and attacks. Raid sim (2026-09-27): removing it costs +5% DPS.
5. **Shamanistic Focus** — -45% shock/Lightning Shield mana. Raid sim (2026-09-27): removing it costs +5% DPS.
6. **Rage of the Farseer** — Capstone: +30% melee and casting speed for 25s every 3 minutes. Raid sim (2026-09-27): removing it costs +4% DPS.
7. **Mental Dexterity** — New: attack power from Intellect (33%/rank read). Raid sim (2026-09-27): removing it costs +4% DPS.
8. **Convection** — Raid sim (2026-09-27): removing it costs +3% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Concussion | any utility talent legal at that tier | Measures +0.3% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**4 of 5** for `enhancement-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md) | ours: optimizer | 11/31/9 | 426 | +0.0% | 780 | +0.0% | 9 s |
| 2 | [`enhancement-raid`](enhancement-raid.md) | ours: hand draft | 11/31/9 | 424 | -0.4% | 770 | -1.2% | 0 s |
| 3 | *Level 60* | community simulator | - | 421 | -1.1% | 775 | -0.6% | 26 s |
| 4 | **[`enhancement-raid-dps`](enhancement-raid-dps.md)** | ours: hand draft | 11/31/9 | 420 | -1.3% | 770 | -1.3% | 9 s |
| 5 | *Enhancement 16/35/0* | community simulator | - | 388 | -8.9% | 761 | -2.3% | 81 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 3 changes to the base rotation; third-seed check: opt-enhancement-dps-raid-dps 406 -> 415 DPS (+2.3%), sim preset: Level 60 392 -> 400 DPS (+2.0%)):
  1. insert before the filler: if not Flame Shock is on the target: cast Flame Shock (+0.6%, pass 1)
  2. only above 60% mana: cast Earth Shock (+1.1%, pass 1)
  3. drop the condition: if mana % ≥ 60%: cast Earth Shock (+3.0%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 6 changes to the base rotation; third-seed check: opt-enhancement-dps-raid-dps 702 -> 774 DPS (+10.3%), sim preset: Level 60 690 -> 756 DPS (+9.7%)):
  1. insert in the middle: if not Flame Shock is on the target: cast Flame Shock (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.3%, pass 1)
  3. drop 'time left in the fight ≥ 20s' from the condition: if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem (+0.2%, pass 1)
  4. insert before the filler: cast Fire Nova (+7.3%, pass 2)
  5. move down below 'cast Stormstrike': if not Flame Shock is on the target: cast Flame Shock (+0.3%, pass 2)
  6. move down below 'cast Earth Shock': cast Fire Nova + only with 10s or more of the fight left: if not Flame Shock is on the target: cast Flame Shock (+0.2%, pass 2)

Before the pull: at -4.5s: cast Strength of Earth Totem; at -3s: cast Grace of Air Totem; at -1.5s: cast Searing Totem.

| # | Priority (the first line whose condition holds is cast) | [`enhancement-raid-dps`](enhancement-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time left on the totem ≤ 0s: cast Strength of Earth Totem | 0.3 |
| 2 | if time left on the totem ≤ 0s: cast Grace of Air Totem | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | cast Stormstrike | 14.1 |
| 5 | if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt | 3.8 |
| 6 | if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem | 1.0 |
| 7 | if not Flame Shock is on the target: cast Flame Shock | 4.2 |
| 8 | cast Earth Shock | 5.0 |

Damage by ability:

| Ability | [`enhancement-raid-dps`](enhancement-raid-dps.md) |
|---|---|
| Auto Attack | 29% |
| Windfury Weapon | 19% |
| Stormstrike | 12% |
| Earth Shock | 11% |
| Flame Shock | 10% |
| Lightning Bolt | 9% |
| Attack | 5% |
| Elemental Sharpening Stone | 3% |
| Dragonbreath Chili | 3% |

## Notes

- Adopted from the community simulator on 2026-09-27: `opt-enhancement-dps-raid-dps` beat the previous draft by +2.8% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Two-Handed Axes and Maces is no longer a talent — check whether shamans can still use two-handers baseline; this build assumes dual wield or a two-hander with Windfury either way.
- Windfury Totem can no longer be improved — the melee-group support reason for bringing an Enhancement shaman is gone; the spec must stand on its own DPS.
- Beta client: Tidal Mastery is a tier-4 talent now, so the Restoration dip is Totemic Focus 5 (tier 1) plus Tidal Focus 5.
- 2026-09-27 scenario audit: Improved Stormstrike 2 -> Elemental Devastation 2. Improved Stormstrike resets Stormstrike when you dodge or parry and adds regen while casting: behind a raid boss you are never attacked, and the simulator measures 0.0%. Elemental Devastation turns Flame Shock and Earth Shock crits into +9% melee crit for 10 s (simulator +3.1% on the optimizer build).

## Open questions (verify in the live game)

- Dual wield for shamans (implied by Predator's Edge-style talents elsewhere, not confirmed here).
- Maelstrom Weapon proc rate; Mental Dexterity/Quickness scaling at max rank.
- Flurry max rank (5% at rank 1).

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
