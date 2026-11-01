# Destruction — Leveling (open talent search) — 6/11/34

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 6/11/34 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Destruction leveling build the open leveling search found on 2026-10-26: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the destruction-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +11.1% faster per kill than destruction-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (6)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 1/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 10%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 1/5 | changed | Increases your total Stamina by 3%. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Fel Vitality** | 2/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 10%, and increases your maximum Mana by 10%. |

### Destruction (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Aftermath** | 2/5 | changed | Increases the initial damage of your Immolate spell by 20% and your Conflagrate spell has a 40% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Shadowburn** | 1/1 | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. |
| **Intensity** | 3/3 | changed | Gives your Destruction spells a 70% chance to not lose casting time when you take damage. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Conflagrate** | 1/1 | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. |
| **Pyroclasm** | 1/2 | changed | Gives your Soul Fire spell a 13% chance to Stun the target for 3 sec, and your Rain of Fire and Hellfire spells a 13% chance over their duration to Stun targets they damage for 3 sec. |
| **Bane of Havoc** | 1/1 | **NEW** | Afflicts the target for 5 min, causing 15% of all damage done by the Warlock to other targets to also be dealt to the cursed target. Bane of Havoc is limited to 1 target, and only one Bane per Warlock can be active on any one target. |
| **Fire and Brimstone** | 3/3 | **NEW** | Increases the critical strike chance of your Conflagrate spell by 25%. |
| **Shadow and Flame** | 5/5 | **NEW** | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 10% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 10% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard. |
| **Incinerate** | 1/1 | **NEW** | Deals 99 to 113 Fire damage to your target and an additional 25% damage if the target is afflicted by Immolate. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Destruction | Bane | 5 | 0/0/5 |
| 15-16 | Destruction | Aftermath | 2 | 0/0/7 |
| 17-19 | Destruction | Cataclysm | 3 | 0/0/10 |
| 20-24 | Destruction | Ruin | 5 | 0/0/15 |
| 25-27 | Destruction | Agonizing Flames | 3 | 0/0/18 |
| 28 | Destruction | Shadowburn | 1 | 0/0/19 |
| 29-31 | Destruction | Intensity | 3 | 0/0/22 |
| 32 | Destruction | Conflagrate | 1 | 0/0/23 |
| 33 | Destruction | Pyroclasm | 1 | 0/0/24 |
| 34 | Destruction | Bane of Havoc | 1 | 0/0/25 |
| 35-39 | Destruction | Shadow and Flame | 5 | 0/0/30 |
| 40 | Destruction | Incinerate | 1 | 0/0/31 |
| 41-43 | Destruction | Fire and Brimstone | 3 | 0/0/34 |
| 44 | Affliction | Improved Life Tap | 1 | 1/0/34 |
| 45-48 | Affliction | Suppression | 4 | 5/0/34 |
| 49-53 | Demonology | Unholy Power | 5 | 5/5/34 |
| 54-56 | Demonology | Improved Voidwalker | 3 | 5/8/34 |
| 57 | Affliction | Suppression | 1 | 6/8/34 |
| 58 | Demonology | Demonic Embrace | 1 | 6/9/34 |
| 59-60 | Demonology | Fel Vitality | 2 | 6/11/34 |

## Core talents (priority order)

1. **Suppression** — +3.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Conflagrate** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Shadow and Flame** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Agonizing Flames** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Voidwalker** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Cataclysm** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Shadowburn** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
8. **Incinerate** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 45.74; destruction-leveling 50.82. The search simulated 26,746 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Destruction leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/15-0015032-0050325133111351-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
