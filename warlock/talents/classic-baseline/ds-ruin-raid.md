# DS/Ruin — Demonic Sacrifice + Ruin (raid DPS) — 7/21/23

*Warlock · Classic baseline*

| | |
|---|---|
| **Build** | 7/21/23 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The most popular Classic raiding build: sacrifice the Succubus for +15% Shadow damage, take Ruin for 200% crits, Improved Shadow Bolt for the 20% shadow vulnerability debuff, and Suppression/Improved Life Tap from Affliction for hit on Curses and mana.

## Point allocation

### Affliction (7)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Suppression** | 5/5 | Reduces the chance for enemies to resist your Affliction spells by 10%. |
| **Improved Life Tap** | 2/2 | Increases the amount of Mana awarded by your Life Tap spell by 20%. |

### Demonology (21)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Healthstone** | 2/2 | Increases the amount of Health restored by your Healthstone by 20%. |
| **Demonic Embrace** | 5/5 | Increases your total Stamina by 15% but reduces your total Spirit by 5%. |
| **Fel Intellect** | 5/5 | Increases the maximum Mana of your Imp, Voidwalker, Succubus, and Felhunter by 15%. |
| **Fel Domination** | 1/1 | Your next Imp, Voidwalker, Succubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%. |
| **Fel Stamina** | 5/5 | Increases the maximum Health of your Imp, Voidwalker, Succubus, and Felhunter by 15%. |
| **Master Summoner** | 2/2 | Reduces the casting time of your Imp, Voidwalker, Succubus, and Felhunter Summoning spells by 4 sec and the Mana cost by 40%. |
| **Demonic Sacrifice** | 1/1 | When activated, sacrifices your summoned demon to grant you an effect that lasts 30 min. The effect is canceled if any Demon is summoned.Imp: Increases your Fire damage by 15%.Voidwalker: Restores 3% of total Health every 4 sec.Succubus: Increases your Shadow damage by 15%.Felhunter: Restores 2% of total Mana every 4 sec. |

### Destruction (23)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Shadow Bolt** | 5/5 | Your Shadow Bolt critical strikes increase Shadow damage dealt to the target by 20% until 4 non-periodic damage sources are applied. Effect lasts a maximum of 12 sec. |
| **Cataclysm** | 4/5 | Reduces the Mana cost of your Destruction spells by 4%. |
| **Bane** | 5/5 | Reduces the casting time of your Shadow Bolt and Immolate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Devastation** | 5/5 | Increases the critical strike chance of your Destruction spells by 5%. |
| **Shadowburn** | 1/1 | Instantly blasts the target for 91 to 104 Shadow damage. If the target dies within 5 sec of Shadowburn, and yields experience or honor, the caster gains a Soul Shard. |
| **Destructive Reach** | 2/2 | Increases the range of your Destruction spells by 20%. |
| **Ruin** | 1/1 | Increases the critical strike damage bonus of your Destruction spells by 100%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — Succubus sacrifice = +15% Shadow damage for 30 minutes.
2. **Ruin** — Shadow Bolt crits deal 200% instead of 150%.
3. **Improved Shadow Bolt** — Crits apply +20% Shadow damage taken (4 charges) — helps every shadow caster.
4. **Bane** — -0.5s Shadow Bolt cast time.
5. **Devastation** — +5% Destruction crit; prerequisite for Ruin.
6. **Improved Life Tap** — +20% mana from Life Tap — your only mana source in a long fight.
7. **Suppression** — +10% hit on Affliction spells (your assigned Curse and Corruption).
8. **Demonic Embrace** — +15% Stamina; you Life Tap health into mana.
9. **Destructive Reach** — +20% range and -10% threat on Destruction spells.
10. **Fel Domination** — Instant re-summon to sacrifice a Voidwalker for the shield in an emergency.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 10 | Fel Intellect 5 + Fel Stamina 5 | Improved Imp, Improved Voidwalker, Improved Health Funnel | Nothing in Demonology tiers 2-3 matters after the pet is sacrificed; these are the least useless fillers (mana/health while the pet is out). |
| 4 | Cataclysm | Improved Firebolt, Improved Searing Pain | -4% Destruction mana cost. |
| 2 | Improved Healthstone | Improved Imp | Bigger Healthstones for the raid. |
| 2 | Master Summoner | Unholy Power | Faster, cheaper re-summons to sacrifice again after a death. |

## Notes

- Shadow Bolt spam with your assigned Curse (usually Curse of Recklessness / Elements / Shadow). Corruption is added only if the raid allows the debuff slot.
- Shadowburn is an execute/instant while moving; Curse of Doom on long fights where allowed.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Affliction | Suppression | 5 | changed | tier 1, max 5 — tooltip changed |
| Affliction | Improved Life Tap | 2 | moved | tier 1, max 2 — was Affliction row 2, col 3 |
| Demonology | Improved Healthstone | 2 | **REMOVED** | removed from Classic |
| Demonology | Demonic Embrace | 5 | changed | tier 1, max 5 — tooltip changed |
| Demonology | Fel Intellect | 5 | **REMOVED** | removed from Classic |
| Demonology | Fel Domination | 1 | changed | tier 4, max 1 — tooltip changed; was Demonology row 3, col 2 |
| Demonology | Fel Stamina | 5 | **REMOVED** | removed from Classic |
| Demonology | Master Summoner | 2 | moved | tier 3, max 2 — was Demonology row 4, col 2 |
| Demonology | Demonic Sacrifice | 1 | changed | tier 3, max 1 — tooltip changed; was Demonology row 5, col 2; tooltip changed in build 1.60.1.70009 (ranks 1) |
| Destruction | Improved Shadow Bolt | 5 | changed | tier 1, max 5 — tooltip changed |
| Destruction | Cataclysm | 4 | changed | tier 2, max 3 — max rank 5 → 3; tooltip changed; was Destruction row 1, col 3 |
| Destruction | Bane | 5 | changed | tier 1, max 5 — tooltip changed; was Destruction row 2, col 2 |
| Destruction | Devastation | 5 | **REMOVED** | removed from Classic |
| Destruction | Shadowburn | 1 | changed | tier 3, max 1 — tooltip changed; was Destruction row 3, col 4; tooltip changed in build 1.60.1.70009 (ranks 1) |
| Destruction | Destructive Reach | 2 | changed | tier 1, max 2 — tooltip changed; was Destruction row 4, col 2 |
| Destruction | Ruin | 1 | changed | tier 3, max 5 — max rank 1 → 5; tooltip changed; was Destruction row 5, col 3 |

**17 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/warlock-dps-pve-spec-builds-talents>
- <https://www.wowhead.com/classic/guide/classes/warlock/dps-talent-builds-pve>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
