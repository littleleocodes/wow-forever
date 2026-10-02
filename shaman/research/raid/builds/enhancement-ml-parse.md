# Enhancement — Full raid (parse) (machine-learning search) — 18/33/0

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/33/0 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Enhancement build the machine-learning talent search found in a full raid (every raid buff and debuff) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry enhancement-dps (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Elemental (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Concussion** | 2/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 2%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%. |
| **Elemental Devastation** | 3/3 | changed | Your offensive spell critical strikes will increase your chance to get a critical strike with melee attacks by 9% for 10 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Elemental Alacrity** | 2/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.33 sec. |
| **Improved Fire Nova** | 2/2 | **NEW** | Increases the damage done by your Fire Nova spell by 20% and reduces its cooldown by 4 sec. |

### Enhancement (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Elemental Weapons** | 3/3 | moved | Increases the melee attack power bonus of your Rockbiter Weapon by 20%, your Windfury Weapon effect by 40% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 15%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Flurry** | 5/5 | changed | Increases your attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Stormstrike** | 1/1 | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Improved Stormstrike** | 2/2 | **NEW** | When you Stormstrike, you have a 100% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 100% chance to reset each time you Dodge or Parry. |
| **Maelstrom Weapon** | 5/5 | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 20%. Stacks up to 5 times. Lasts 30 sec. |
| **Rage of the Farseer** | 1/1 | **NEW** | Increases your attack speed by 30% for 25 sec. |

### Restoration (0)

*No points.*

## Rank among our builds and the community simulator's

**3 of 6** for `enhancement-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`enhancement-ml-raid`](enhancement-ml-raid.md) | ours: hand draft | 20/31/0 | 414 | +0.0% | 774 | -3.0% | 27 s |
| 2 | [`opt-enhancement-dps-raid-dps`](opt-enhancement-dps-raid-dps.md) | ours: optimizer | 11/31/9 | 413 | -0.2% | 755 | -5.3% | 14 s |
| 3 | **[`enhancement-ml-parse`](enhancement-ml-parse.md)** | ours: parse build | 18/33/0 | 408 | -1.4% | 798 | +0.0% | 17 s |
| 4 | [`enhancement-raid-dps`](enhancement-raid-dps.md) | ours: hand draft | 11/31/9 | 408 | -1.6% | 745 | -6.6% | 14 s |
| 5 | *Level 60* | community simulator | - | 405 | -2.2% | 755 | -5.4% | 31 s |
| 6 | *Enhancement 16/35/0* | community simulator | - | 367 | -11.4% | 734 | -8.1% | 84 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-10-02, 5 changes to the base rotation; third-seed check: ml: Enhancement 400 -> 417 DPS (+4.3%), opt-enhancement-dps-raid-dps 392 -> 413 DPS (+5.3%), sim preset: Level 60 390 -> 405 DPS (+3.7%)):
  1. insert before the filler: if not Flame Shock is on the target: cast Flame Shock (+0.6%, pass 1)
  2. only above 60% mana: cast Earth Shock (+1.1%, pass 1)
  3. drop the condition: if mana % ≥ 60%: cast Earth Shock (+3.0%, pass 2)
  4. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.8%, pass 4)
  5. insert at the end: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.4%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-10-02, 7 changes to the base rotation; third-seed check: ml: Enhancement 684 -> 772 DPS (+12.8%), opt-enhancement-dps-raid-dps 662 -> 755 DPS (+14.1%), sim preset: Level 60 669 -> 756 DPS (+13.0%)):
  1. insert in the middle: if not Flame Shock is on the target: cast Flame Shock (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if stacks of Maelstrom Weapon ≥ 5: cast Lightning Bolt (+0.3%, pass 1)
  3. drop 'time left in the fight ≥ 20s' from the condition: if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem (+0.2%, pass 1)
  4. insert before the filler: cast Fire Nova (+7.3%, pass 2)
  5. move down below 'cast Stormstrike': if not Flame Shock is on the target: cast Flame Shock (+0.3%, pass 2)
  6. move down below 'cast Earth Shock': cast Fire Nova + only with 10s or more of the fight left: if not Flame Shock is on the target: cast Flame Shock (+0.2%, pass 2)
  7. threshold 3.75 -> 2.812: if stacks of Maelstrom Weapon ≥ 3.75: cast Lightning Bolt (+0.3%, pass 4)

Before the pull: at -4.5s: cast Strength of Earth Totem; at -3s: cast Grace of Air Totem; at -1.5s: cast Searing Totem.

| # | Priority (the first line whose condition holds is cast) | [`enhancement-ml-parse`](enhancement-ml-parse.md) casts/min |
|---|---|---|
| 1 | if time left on the totem ≤ 0s: cast Strength of Earth Totem | 0.3 |
| 2 | if time left on the totem ≤ 0s: cast Grace of Air Totem | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | cast Stormstrike | 14.0 |
| 5 | if stacks of Maelstrom Weapon ≥ 3.75: cast Lightning Bolt | 4.6 |
| 6 | if time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem | 1.3 |
| 7 | if not Flame Shock is on the target: cast Flame Shock | 4.0 |
| 8 | cast Earth Shock | 4.6 |
| 9 | if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem | 1.3 |

Damage by ability:

| Ability | [`enhancement-ml-parse`](enhancement-ml-parse.md) |
|---|---|
| Auto Attack | 28% |
| Windfury Weapon | 18% |
| Flame Shock | 12% |
| Lightning Bolt | 12% |
| Earth Shock | 11% |
| Stormstrike | 10% |
| Attack | 7% |
| Dragonbreath Chili | 3% |

## Notes

- In a full raid it does +3.1% over the training-dummy winner (796.1 vs 772.4 DPS, 100,000 fights, one seed, BiS gear).
- Search result: 18/33/0 at 796.2 ± 0.16 DPS over 100,000 fights; runner-up 18/33/0 (+0.01%; the winner takes Concussion 2, Elemental Alacrity 2; the runner-up Concussion 1, Elemental Alacrity 3); 2,027 builds simulated; certificate: the neighbours ahead on the short run (of 429) did not hold on the longer one.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.

## Open questions (verify in the live game)

- A machine-searched Enhancement build: check it against the community's Enhancement builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
