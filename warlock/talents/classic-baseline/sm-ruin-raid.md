# SM/Ruin — Shadow Mastery + Ruin (raid DPS) — 30/0/21

*Warlock · Classic baseline*

| | |
|---|---|
| **Build** | 30/0/21 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Keeps the pet (Imp with Blood Pact for the tank group) and takes +10% Shadow damage from Shadow Mastery instead of the +15% from Demonic Sacrifice. Slightly less Shadow Bolt damage than DS/Ruin but better DoT damage (Improved Corruption, Nightfall) and much better for solo/PvP.

## Point allocation

### Affliction (30)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Suppression** | 5/5 | Reduces the chance for enemies to resist your Affliction spells by 10%. |
| **Improved Corruption** | 5/5 | Reduces the casting time of your Corruption spell by 2 sec. |
| **Improved Life Tap** | 2/2 | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Improved Drain Soul** | 2/2 | Gives you a 100% chance to get a 100% increase to your Mana regeneration for 10 sec if the target is killed by you while you drain its soul. In addition your Mana may continue to regenerate while casting at 50% of normal. |
| **Improved Curse of Agony** | 3/3 | Increases the damage done by your Curse of Agony by 6%. |
| **Amplify Curse** | 1/1 | Increases the effect of your next Curse of Weakness or Curse of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Nightfall** | 2/2 | Gives your Corruption and Drain Life spells a 4% chance to cause you to enter a Shadow Trance state after damaging the opponent. The Shadow Trance state reduces the casting time of your next Shadow Bolt spell by 100%. |
| **Grim Reach** | 2/2 | Increases the range of your Affliction spells by 20%. |
| **Siphon Life** | 1/1 | Transfers 15 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Improved Curse of Weakness** | 2/3 | Increases the effect of your Curse of Weakness by 13%. |
| **Shadow Mastery** | 5/5 | Increases the damage dealt or life drained by your Shadow spells by 10%. |

### Demonology (0)

*No points.*

### Destruction (21)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Shadow Bolt** | 5/5 | Your Shadow Bolt critical strikes increase Shadow damage dealt to the target by 20% until 4 non-periodic damage sources are applied. Effect lasts a maximum of 12 sec. |
| **Cataclysm** | 2/5 | Reduces the Mana cost of your Destruction spells by 2%. |
| **Bane** | 5/5 | Reduces the casting time of your Shadow Bolt and Immolate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Devastation** | 5/5 | Increases the critical strike chance of your Destruction spells by 5%. |
| **Shadowburn** | 1/1 | Instantly blasts the target for 91 to 104 Shadow damage. If the target dies within 5 sec of Shadowburn, and yields experience or honor, the caster gains a Soul Shard. |
| **Destructive Reach** | 2/2 | Increases the range of your Destruction spells by 20%. |
| **Ruin** | 1/1 | Increases the critical strike damage bonus of your Destruction spells by 100%. |

## Core talents (priority order)

1. **Shadow Mastery** — +10% Shadow damage without sacrificing the pet.
2. **Ruin** — 200% crits.
3. **Improved Shadow Bolt** — Shadow vulnerability debuff.
4. **Improved Corruption** — Instant Corruption — free damage between Shadow Bolts.
5. **Nightfall** — Corruption ticks proc an instant Shadow Bolt.
6. **Bane** — Cast time.
7. **Improved Life Tap** — Mana.
8. **Suppression** — Affliction hit.
9. **Siphon Life** — Prerequisite for Shadow Mastery; small self-heal DoT.
10. **Grim Reach** — +20% Affliction range.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 4 | Improved Drain Soul 2 + Improved Curse of Weakness 2 | Fel Concentration, Improved Drain Life | Four filler points are needed to reach 25 for Shadow Mastery; none of the options matter in a raid. |
| 3 | Improved Curse of Agony | Fel Concentration | Only if you are assigned Curse of Agony; otherwise filler. |
| 2 | Cataclysm | Aftermath, Intensity | Reach 20 points for Ruin. |

## Notes

- At least one SM/Ruin lock per raid keeps an Imp for Blood Pact in the tank group.
- Improved Firebolt is worth taking instead of Cataclysm if the Imp is out and attacking.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Affliction | Suppression | 5 | changed | tier 1, max 5 — tooltip changed |
| Affliction | Improved Corruption | 5 | changed | tier 1, max 5 — tooltip changed |
| Affliction | Improved Life Tap | 2 | moved | tier 1, max 2 — was Affliction row 2, col 3 |
| Affliction | Improved Drain Soul | 2 | **REMOVED** | removed from Classic |
| Affliction | Improved Curse of Agony | 3 | **REMOVED** | removed from Classic |
| Affliction | Amplify Curse | 1 | changed | tier 3, max 1 — tooltip changed |
| Affliction | Nightfall | 2 | changed | tier 4, max 2 — tooltip changed |
| Affliction | Grim Reach | 2 | **REMOVED** | removed from Classic |
| Affliction | Siphon Life | 1 | changed | tier 5, max 1 — tooltip changed |
| Affliction | Improved Curse of Weakness | 2 | **REMOVED** | removed from Classic |
| Affliction | Shadow Mastery | 5 | changed | tier 6, max 5 — tooltip changed; was Affliction row 6, col 2 |
| Destruction | Improved Shadow Bolt | 5 | changed | tier 1, max 5 — tooltip changed |
| Destruction | Cataclysm | 2 | changed | tier 2, max 3 — max rank 5 → 3; tooltip changed; was Destruction row 1, col 3 |
| Destruction | Bane | 5 | changed | tier 1, max 5 — tooltip changed; was Destruction row 2, col 2 |
| Destruction | Devastation | 5 | **REMOVED** | removed from Classic |
| Destruction | Shadowburn | 1 | changed | tier 3, max 1 — tooltip changed; was Destruction row 3, col 4; tooltip changed in build 1.60.1.70009 (ranks 1) |
| Destruction | Destructive Reach | 2 | changed | tier 1, max 2 — tooltip changed; was Destruction row 4, col 2 |
| Destruction | Ruin | 1 | changed | tier 3, max 5 — max rank 1 → 5; tooltip changed; was Destruction row 5, col 3 |

**14 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/warlock-dps-pve-spec-builds-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
