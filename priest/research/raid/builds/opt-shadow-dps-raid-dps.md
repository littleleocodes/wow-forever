# Optimizer — Shadow leveling/raid: Shadow Word: Pain 28%, Mind Blast 27%, Mind Flay channel 30% (talent), wand 10%, Smite 5% before 20 (raid-dps) — 20/0/31

*[Priest](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/0/31 (Discipline / Holy / Shadow) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `shadow-dps` and profile `raid-dps`: score +685.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Discipline (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Power in Light** | 5/5 | **NEW** | Your Smite and Penance spells deal 10% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain. |
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |
| **Mental Strength** | 5/5 | changed | Increases your total Intellect by 10%. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Holy (0)

*No points.*

### Shadow (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 5/5 | changed | Improves your chance to hit with Shadow spells by 5%. |
| **Improved Mind Blast** | 5/5 | changed | Reduces the cooldown of your Mind Blast spell by 2.5 sec. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |
| **Shadow Reach** | 1/2 | changed | Increases the range of your offensive Shadow spells by 10%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Each instance of damage of Mind Flay deals 20% more damage than its previous instance of damage. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Dark Inspiration** | 3/5 | moved | Your Mind Blast and fully channeled Mind Flay causes Dark Inspiration, increasing yours and your party's Spirit by 9% for 10 sec. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Devouring Contagion** | 2/2 | **NEW** | Reduces the mana cost of your Devouring Plague by 50%.  Targets that die while Devouring Plague is active spreads it, jumping to 2 nearby enemies within 10 yds for the remaining duration. |
| **Darkness** | 5/5 | changed | Increases your Shadow damage done by 10%. |
| **Shadowform** | 1/1 | changed | Assume Shadowform, increasing your Shadow damage by 10%, reducing the Mana cost of all Shadow spells by 50%, increasing the critical strike damage bonus of your Shadow spells by 100%, and reducing Physical damage taken by you by 15%. However, you may not cast healing spells while in this form. |

## Core talents (priority order)

1. **Shadowform** — Removing it costs 478.5 points of score in this model.
2. **Mind Flay** — Removing it costs 376.5 points of score in this model.
3. **Shadow Weaving** — Removing it costs 71.4 points of score in this model.
4. **Darkness** — Removing it costs 71.4 points of score in this model.
5. **Improved Mind Flay** — Removing it costs 69.5 points of score in this model.
6. **Twin Disciplines** — Removing it costs 30.5 points of score in this model.
7. **Shadow Focus** — Removing it costs 28.1 points of score in this model.
8. **Improved Shadow Word: Pain** — Removing it costs 21.8 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 4** for `shadow-dps` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-shadow-dps-raid-dps`](opt-shadow-dps-raid-dps.md)** | ours: optimizer | 20/0/31 | 665 | +0.0% | 761 | -0.5% | 0 s |
| 2 | *Standard* | community simulator | - | 620 | -6.7% | 760 | -0.5% | 0 s |
| 3 | [`shadow-ml-raid`](shadow-ml-raid.md) | ours: derived (ML search) | 16/0/35 | 603 | -9.4% | 764 | +0.0% | 11 s |
| 4 | *Smite* | community simulator | - | 225 | -66.1% | 302 | -60.5% | 3 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 4 passes, the last 2026-10-02, 3 changes to the base rotation; third-seed check: ml: Shadow 633 -> 634 DPS (+0.2%), opt-shadow-dps-raid-dps 631 -> 632 DPS (+0.1%), sim preset: Shadow 618 -> 618 DPS (+0.1%)):
  1. always rank 2 instead of rank 4: cast Shadow Word: Death (+1.7%, pass 1)
  2. move down below 'cast Shadow Word: Death': cast Mind Blast (+0.3%, pass 1)
  3. insert in the middle: cast Shadow Word: Death (+1.1%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 8 passes, the last 2026-11-02, 4 changes to the base rotation; third-seed check: opt-shadow-dps-raid-dps 782 -> 783 DPS (+0.2%), sim preset: Standard 780 -> 782 DPS (+0.3%)):
  1. move down below 'cast Shadow Word: Death': cast Mind Blast (+0.4%, pass 1)
  2. insert before the filler: cast Devouring Plague (+2.5%, pass 5)
  3. insert at the end: cast Dark Sacrifice (+0.3%, pass 5)
  4. move to the top: cast Mind Blast (+0.3%, pass 8)

Before the pull: at -1s: cast Shadowform.

| # | Priority (the first line whose condition holds is cast) | [`opt-shadow-dps-raid-dps`](opt-shadow-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain | 2.6 |
| 3 | strict sequence: cast Inner Focus; cast Devouring Plague | 2.6 |
| 4 | cast Shadow Word: Death | 3.3 |
| 5 | cast Mind Blast | 7.0 |
| 6 | channel Mind Flay | as ready |

Lines of the simulator's rotation these builds never cast: Death (rank 2) (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-shadow-dps-raid-dps`](opt-shadow-dps-raid-dps.md) |
|---|---|
| Mind Flay | 40% |
| Shadow Word: Pain | 19% |
| Mind Blast | 19% |
| Devouring Plague | 12% |
| Shadow Word: Death | 9% |
| Demonic Rune | 2% |

## Notes

- Allocation taken from cand-shadow-dps-r3 on 2026-10-29: the optimizer's earlier round beat its last export in the community simulator (695 vs 656 DPS; the calibration moved the model past the better build).
- Report: priest/research/talents/forever/optimizer/shadow-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/priest>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
