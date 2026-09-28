# Fire (raid DPS, AQ40 / Naxxramas) — 17/31/3

*Mage · Classic baseline*

| | |
|---|---|
| **Build** | 17/31/3 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Once fire-immune bosses are behind you, Fire is the top damage: Ignite (40% of crit damage as a rolling DoT, shared across all fire mages), Improved Scorch (+15% fire damage taken), Critical Mass, Fire Power and Combustion. Arcane still supplies Clearcasting and Arcane Meditation; Elemental Precision is taken from Frost for hit.

## Point allocation

### Arcane (17)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Arcane Subtlety** | 2/2 | Reduces your target's resistance to all your spells by 10 and reduces the threat caused by your Arcane spells by 40%. |
| **Arcane Focus** | 3/5 | Reduces the chance that the opponent can resist your Arcane spells by 6%. |
| **Arcane Concentration** | 5/5 | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Improved Arcane Explosion** | 3/3 | Increases the critical strike chance of your Arcane Explosion spell by an additional 6%. |
| **Magic Attunement** | 2/2 | Increases the effect of your Amplify Magic and Dampen Magic spells by 50%. |
| **Arcane Meditation** | 2/3 | Allows 10% of your Mana regeneration to continue while casting. |

### Fire (31)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Fireball** | 5/5 | Reduces the casting time of your Fireball spell by 0.5 sec. |
| **Ignite** | 5/5 | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Flame Throwing** | 2/2 | Increases the range of your Fire spells by 6 yards. |
| **Incinerate** | 1/2 | Increases the critical strike chance of your Fire Blast and Scorch spells by 2%. |
| **Pyroblast** | 1/1 | Hurls an immense fiery boulder that causes 148 to 195 Fire damage and an additional 56 Fire damage over 12 sec. |
| **Burning Soul** | 2/2 | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Improved Scorch** | 3/3 | Your Scorch spells have a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases the Fire damage dealt to your target by 3% and lasts 30 sec. Stacks up to 5 times. |
| **Master of Elements** | 3/3 | Your Fire and Frost spell criticals will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 5/5 | Increases the damage done by your Fire spells by 10%. |
| **Combustion** | 1/1 | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 critical strikes with Fire spells. |

### Frost (3)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Elemental Precision** | 3/3 | Reduces the chance that the opponent can resist your Frost and Fire spells by 6%. |

## Core talents (priority order)

1. **Ignite** — Crits add a DoT worth 40% of the crit; with several fire mages the Ignite stack is the biggest damage source in the raid.
2. **Improved Scorch** — +15% Fire damage taken on the boss; one mage maintains it.
3. **Fire Power** — +10% Fire damage.
4. **Critical Mass** — +6% Fire crit.
5. **Improved Fireball** — -0.5s Fireball cast.
6. **Elemental Precision** — +6% hit.
7. **Combustion** — Guaranteed crits until three land — the burst cooldown.
8. **Master of Elements** — 30% mana back on crits.
9. **Arcane Concentration** — Clearcasting.
10. **Burning Soul** — -20% Fire threat and pushback resistance — fire mages pull threat.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Arcane Focus | Improved Arcane Missiles | Tier-1 Arcane filler; Arcane Focus only helps Arcane Explosion here. |
| 5 | Improved Arcane Explosion 3 + Magic Attunement 2 | Arcane Resilience + Magic Absorption | Reach Arcane Meditation. |
| 3 | Flame Throwing 2 + Incinerate 1 | Improved Fire Blast, Impact | Tier-2/3 Fire filler to unlock Improved Scorch and Master of Elements. |
| 2 | Arcane Meditation | Burning Soul (if dropped), Blast Wave | Trade mana regen against threat/AoE as gear improves. |

## Notes

- Scorch x5 to apply Improved Scorch, then Fireball; keep Fire Blast on cooldown only if movement forces it.
- Not usable in Molten Core; most of Blackwing Lair is fire-resistant as well.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Arcane | Arcane Subtlety | 2 | changed | tier 2, max 2 — tooltip changed; was Arcane row 1, col 1 |
| Arcane | Arcane Focus | 3 | changed | tier 1, max 5 — tooltip changed |
| Arcane | Arcane Concentration | 5 | unchanged | tier 2, max 5 |
| Arcane | Improved Arcane Explosion | 3 | **REMOVED** | removed from Classic |
| Arcane | Magic Attunement | 2 | **REMOVED** | removed from Classic |
| Arcane | Arcane Meditation | 2 | changed | tier 4, max 3 — tooltip changed; was Arcane row 4, col 4 |
| Fire | Improved Fireball | 5 | changed | tier 1, max 5 — tooltip changed; was Fire row 1, col 2 |
| Fire | Ignite | 5 | unchanged | tier 2, max 5 |
| Fire | Flame Throwing | 2 | unchanged | tier 2, max 2 |
| Fire | Incinerate | 1 | **REMOVED** | removed from Classic |
| Fire | Pyroblast | 1 | changed | tier 3, max 1 — tooltip changed; tooltip changed in build 1.60.1.70009 (ranks 1) |
| Fire | Burning Soul | 2 | changed | tier 3, max 3 — max rank 2 → 3; tooltip changed; was Fire row 3, col 4 |
| Fire | Improved Scorch | 3 | changed | tier 4, max 3 — tooltip changed |
| Fire | Master of Elements | 3 | changed | tier 4, max 3 — tooltip changed |
| Fire | Critical Mass | 3 | unchanged | tier 5, max 3 |
| Fire | Fire Power | 5 | unchanged | tier 6, max 5 |
| Fire | Combustion | 1 | changed | tier 7, max 1 — tooltip changed |
| Frost | Elemental Precision | 3 | changed | tier 1, max 5 — max rank 3 → 5; tooltip changed |

**6 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/mage-dps-pve-spec-builds-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
