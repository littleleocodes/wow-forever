# Soul Link / Nightfall (PvP) — 20/31/0

*Warlock · Classic baseline*

| | |
|---|---|
| **Build** | 20/31/0 (Affliction / Demonology / Destruction) |
| **Role** | DPS — PvP |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The durable PvP warlock: Soul Link splits 30% of damage taken to the pet, Fel Domination + Master Summoner re-summon instantly, Nightfall gives instant Shadow Bolts, Improved Corruption/Curse of Agony/Amplify Curse do the DoT work. Very hard to kill; damage is steady rather than bursty.

## Point allocation

### Affliction (20)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Suppression** | 5/5 | Reduces the chance for enemies to resist your Affliction spells by 10%. |
| **Improved Corruption** | 5/5 | Reduces the casting time of your Corruption spell by 2 sec. |
| **Improved Life Tap** | 2/2 | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Improved Curse of Agony** | 3/3 | Increases the damage done by your Curse of Agony by 6%. |
| **Amplify Curse** | 1/1 | Increases the effect of your next Curse of Weakness or Curse of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Nightfall** | 2/2 | Gives your Corruption and Drain Life spells a 4% chance to cause you to enter a Shadow Trance state after damaging the opponent. The Shadow Trance state reduces the casting time of your next Shadow Bolt spell by 100%. |
| **Grim Reach** | 2/2 | Increases the range of your Affliction spells by 20%. |

### Demonology (31)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Healthstone** | 2/2 | Increases the amount of Health restored by your Healthstone by 20%. |
| **Demonic Embrace** | 5/5 | Increases your total Stamina by 15% but reduces your total Spirit by 5%. |
| **Fel Intellect** | 5/5 | Increases the maximum Mana of your Imp, Voidwalker, Succubus, and Felhunter by 15%. |
| **Fel Stamina** | 5/5 | Increases the maximum Health of your Imp, Voidwalker, Succubus, and Felhunter by 15%. |
| **Fel Domination** | 1/1 | Your next Imp, Voidwalker, Succubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%. |
| **Unholy Power** | 5/5 | Increases the damage done by your Voidwalker, Succubus, and Felhunter's melee attacks by 20%. |
| **Master Summoner** | 1/2 | Reduces the casting time of your Imp, Voidwalker, Succubus, and Felhunter Summoning spells by 2 sec and the Mana cost by 20%. |
| **Demonic Sacrifice** | 1/1 | When activated, sacrifices your summoned demon to grant you an effect that lasts 30 min. The effect is canceled if any Demon is summoned.Imp: Increases your Fire damage by 15%.Voidwalker: Restores 3% of total Health every 4 sec.Succubus: Increases your Shadow damage by 15%.Felhunter: Restores 2% of total Mana every 4 sec. |
| **Master Demonologist** | 5/5 | Grants both the Warlock and the summoned demon an effect as long as that demon is active.Imp - Reduces threat caused by 20%.Voidwalker - Reduces physical damage taken by 10%.Succubus - Increases all damage caused by 10%.Felhunter - Increases all resistances by 1 per level. |
| **Soul Link** | 1/1 | When active, 0% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, or Felhunter demon instead. In addition, both the demon and master will inflict 3% more damage. Lasts as long as the demon is active. |

### Destruction (0)

*No points.*

## Core talents (priority order)

1. **Soul Link** — 30% of damage redirected to the pet, +3% damage.
2. **Master Demonologist** — Pet-dependent buffs: Voidwalker -10% physical damage taken, Succubus +10% damage, Felhunter resistances.
3. **Fel Domination** — Instant re-summon after the pet dies.
4. **Nightfall** — Instant Shadow Bolt procs from Corruption.
5. **Improved Corruption** — Instant Corruption.
6. **Amplify Curse** — Big Curse of Agony/Exhaustion every 3 minutes.
7. **Demonic Embrace** — +15% Stamina.
8. **Unholy Power** — +20% pet melee damage; prerequisite for Master Demonologist.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 10 | Fel Intellect 5 + Fel Stamina 5 | Improved Voidwalker 3 + Improved Health Funnel 2 + Improved Imp | Improved Voidwalker is a fine swap when the Voidwalker is the PvP pet. |
| 5 | Suppression | Improved Drain Life, Fel Concentration | Hit on DoTs matters in PvP too, but Fel Concentration for Drain Life kiting is popular. |

## Notes

- Siphon Life is not reachable with Soul Link at 31 Demonology; SM/Ruin (above) is the higher-damage PvP alternative without Soul Link.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Affliction | Suppression | 5 | changed | tier 1, max 5 — tooltip changed |
| Affliction | Improved Corruption | 5 | changed | tier 1, max 5 — tooltip changed |
| Affliction | Improved Life Tap | 2 | moved | tier 1, max 2 — was Affliction row 2, col 3 |
| Affliction | Improved Curse of Agony | 3 | **REMOVED** | removed from Classic |
| Affliction | Amplify Curse | 1 | changed | tier 3, max 1 — tooltip changed |
| Affliction | Nightfall | 2 | changed | tier 4, max 2 — tooltip changed |
| Affliction | Grim Reach | 2 | new | tier 2, max 2 — renamed from Malediction in build 1.60.1.70707; max rank 5 -> 2 in build 1.60.1.70707; tooltip changed in build 1.60.1.70707 (ranks 1, 2) |
| Demonology | Improved Healthstone | 2 | **REMOVED** | removed from Classic |
| Demonology | Demonic Embrace | 5 | changed | tier 1, max 5 — tooltip changed |
| Demonology | Fel Intellect | 5 | **REMOVED** | removed from Classic |
| Demonology | Fel Stamina | 5 | **REMOVED** | removed from Classic |
| Demonology | Fel Domination | 1 | changed | tier 4, max 1 — tooltip changed; was Demonology row 3, col 2 |
| Demonology | Unholy Power | 5 | changed | tier 1, max 5 — tooltip changed; was Demonology row 4, col 3 |
| Demonology | Master Summoner | 1 | moved | tier 3, max 2 — was Demonology row 4, col 2 |
| Demonology | Demonic Sacrifice | 1 | changed | tier 3, max 1 — tooltip changed; was Demonology row 5, col 2; tooltip changed in build 1.60.1.70707 (ranks 1) |
| Demonology | Master Demonologist | 5 | changed | tier 6, max 5 — tooltip changed |
| Demonology | Soul Link | 1 | changed | tier 5, max 1 — tooltip changed; was Demonology row 7, col 2 |

**15 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/warlock/dps-pvp-arena>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
