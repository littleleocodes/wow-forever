# Destruction — Leveling (open talent search) — 6/9/36

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 6/9/36 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Destruction leveling build the open leveling search found on 2026-11-22: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the destruction-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +0.8% faster per kill than destruction-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (6)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 4/5 | changed | Improves your chance to hit by 4% and reduces all threat you generate by 16%. |

### Demonology (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Improved Voidwalker** | 1/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 10%. |
| **Fel Vitality** | 1/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 5%, and increases your maximum Mana by 5%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |

### Destruction (36)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Destructive Reach** | 2/2 | changed | Increases the range of your Destruction spells by 20%. |
| **Improved Shadow Bolt** | 1/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Aftermath** | 5/5 | changed | Increases the initial damage of your Immolate spell by 50% and your Conflagrate spell has a 100% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Shadowburn** | 1/1 | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Conflagrate** | 1/1 | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. |
| **Bane of Havoc** | 1/1 | **NEW** | Afflicts the target for 5 min, causing 15% of all damage done by the Warlock to other targets to also be dealt to the cursed target. Bane of Havoc is limited to 1 target, and only one Bane per Warlock can be active on any one target. |
| **Fire and Brimstone** | 3/3 | **NEW** | Increases the critical strike chance of your Conflagrate spell by 25%. |
| **Shadow and Flame** | 5/5 | **NEW** | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 20% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 20% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard. |
| **Incinerate** | 1/1 | **NEW** | Deals 99 to 113 Fire damage to your target and an additional 25% damage if the target is afflicted by Immolate. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Destruction | Bane | 5 | 0/0/5 |
| 15-16 | Destruction | Destructive Reach | 2 | 0/0/7 |
| 17-19 | Destruction | Cataclysm | 3 | 0/0/10 |
| 20-24 | Destruction | Ruin | 5 | 0/0/15 |
| 25-27 | Destruction | Agonizing Flames | 3 | 0/0/18 |
| 28 | Destruction | Improved Shadow Bolt | 1 | 0/0/19 |
| 29 | Destruction | Shadowburn | 1 | 0/0/20 |
| 30 | Destruction | Bane of Havoc | 1 | 0/0/21 |
| 31 | Destruction | Conflagrate | 1 | 0/0/22 |
| 32-34 | Destruction | Fire and Brimstone | 3 | 0/0/25 |
| 35-39 | Destruction | Shadow and Flame | 5 | 0/0/30 |
| 40 | Destruction | Incinerate | 1 | 0/0/31 |
| 41 | Destruction | Aftermath | 1 | 0/0/32 |
| 42-45 | Affliction | Suppression | 4 | 4/0/32 |
| 46-49 | Destruction | Aftermath | 4 | 4/0/36 |
| 50-54 | Demonology | Unholy Power | 5 | 4/5/36 |
| 55 | Demonology | Improved Voidwalker | 1 | 4/6/36 |
| 56-57 | Demonology | Demonic Energies | 2 | 4/8/36 |
| 58 | Demonology | Fel Vitality | 1 | 4/9/36 |
| 59-60 | Affliction | Improved Life Tap | 2 | 6/9/36 |

## Core talents (priority order)

1. **Conflagrate** — +4.4 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shadow and Flame** — +4.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Shadowburn** — +3.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Agonizing Flames** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Fire and Brimstone** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Demonic Energies** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Cataclysm** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Ruin** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-22: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Improved Voidwalker to Improved Life Tap at 60 (tie-break: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill); Improved Voidwalker to Improved Life Tap at 59 (tie-break: -0.1% seed 3, -0.2% seed 4, level-weighted time per kill); Intensity to Improved Shadow Bolt at 28 (gate that did nothing, no loss: -0.0% seed 3, -0.0% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 35.45; destruction-open-leveling 35.75, destruction-leveling 39.62. The search simulated 36,382 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Destruction leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/04-00050312-2050355113101351-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
