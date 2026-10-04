# Shadow (PvP) — 7/0/44

*Priest · Classic baseline*

| | |
|---|---|
| **Build** | 7/0/44 (Discipline / Holy / Shadow) |
| **Role** | DPS — PvP |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Shadowform, Silence, Vampiric Embrace, Improved Psychic Scream and Blackout stuns, with Unbreakable Will and Improved Power Word: Shield from Discipline. The standard Classic PvP priest.

## Point allocation

### Discipline (7)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Unbreakable Will** | 5/5 | Increases your chance to resist Stun, Fear, and Silence effects by an additional 15%. |
| **Improved Power Word: Shield** | 2/3 | Increases the damage absorbed by your Power Word: Shield by 10%. |

### Holy (0)

*No points.*

### Shadow (44)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Spirit Tap** | 5/5 | Gives you a 100% chance to gain a 100% bonus to your Spirit after killing a target that yields experience. For the duration, your Mana will regenerate at a 50% rate while casting. Lasts 15 sec. |
| **Blackout** | 5/5 | Gives your Shadow damage spells a 10% chance to stun the target for 3 sec. |
| **Improved Shadow Word: Pain** | 2/2 | Increases the duration of your Shadow Word: Pain spell by 6 sec. |
| **Shadow Focus** | 5/5 | Reduces your target's chance to resist your Shadow spells by 10%. |
| **Improved Psychic Scream** | 2/2 | Reduces the cooldown of your Psychic Scream spell by 4 sec. |
| **Improved Mind Blast** | 5/5 | Reduces the cooldown of your Mind Blast spell by 2.5 sec. |
| **Mind Flay** | 1/1 | Assault the target's mind with Shadow energy, causing 75 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Improved Fade** | 1/2 | Decreases the cooldown of your Fade ability by 3 sec. |
| **Shadow Reach** | 3/3 | Increases the range of your Shadow damage spells by 20%. |
| **Shadow Weaving** | 5/5 | Your Shadow damage spells have a 100% chance to cause your target to be vulnerable to Shadow damage. This vulnerability increases the Shadow damage dealt to your target by 3% and lasts 15 sec. Stacks up to 5 times. |
| **Silence** | 1/1 | Silences the target, preventing them from casting spells for 5 sec. |
| **Vampiric Embrace** | 1/1 | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 1 min. |
| **Improved Vampiric Embrace** | 2/2 | Increases the percentage healed by Vampiric Embrace by an additional 10%. |
| **Darkness** | 5/5 | Increases your Shadow spell damage by 10%. |
| **Shadowform** | 1/1 | Assume a Shadowform, increasing your Shadow damage by 15% and reducing Physical damage done to you by 15%. However, you may not cast Holy spells while in this form. |

## Core talents (priority order)

1. **Shadowform** — +15% Shadow damage, -15% physical damage taken.
2. **Silence** — 5s silence — the anti-caster tool.
3. **Blackout** — 10% stun chance on Shadow damage (every DoT tick rolls).
4. **Vampiric Embrace** — Self-healing from Shadow damage.
5. **Improved Psychic Scream** — -4s Psychic Scream cooldown; prerequisite for Silence.
6. **Shadow Weaving** — Stacking +15% Shadow damage taken debuff.
7. **Darkness** — +10% Shadow damage.
8. **Improved Mind Blast** — -2.5s Mind Blast cooldown.
9. **Unbreakable Will** — +15% resist to stun/fear/silence.
10. **Spirit Tap** — Mana after kills — long battleground fights.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Improved Vampiric Embrace 2 + Improved Fade 1 | Shadow Affinity, Improved Fade 2 | Last points in Shadow. |
| 2 | Improved Power Word: Shield | Martyrdom, Wand Specialization | Bigger shields. |

## Notes

- Shadow priests are not used as raid DPS in Classic Era (mana and the 16-debuff limit); this build is PvP and world content only.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Discipline | Unbreakable Will | 5 | **REMOVED** | removed from Classic |
| Discipline | Improved Power Word: Shield | 2 | changed | tier 2, max 3 — tooltip changed |
| Shadow | Spirit Tap | 5 | changed | tier 1, max 5 — tooltip changed; was Shadow row 1, col 2; tooltip changed in build 1.60.1.70170 (ranks 1, 2, 3, 4, 5) |
| Shadow | Blackout | 5 | moved | tier 1, max 5 — was Shadow row 1, col 3 |
| Shadow | Improved Shadow Word: Pain | 2 | moved | tier 2, max 2 — was Shadow row 2, col 2 |
| Shadow | Shadow Focus | 5 | changed | tier 1, max 5 — tooltip changed; was Shadow row 2, col 3 |
| Shadow | Improved Psychic Scream | 2 | moved | tier 3, max 2 — was Shadow row 3, col 1 |
| Shadow | Improved Mind Blast | 5 | changed | tier 3, max 5 — tooltip changed; was Shadow row 3, col 2 |
| Shadow | Mind Flay | 1 | changed | tier 3, max 1 — tooltip changed |
| Shadow | Improved Fade | 1 | moved | tier 4, max 2 — was Shadow row 4, col 2 |
| Shadow | Shadow Reach | 3 | changed | tier 2, max 2 — max rank 3 → 2; tooltip changed; was Shadow row 4, col 3 |
| Shadow | Shadow Weaving | 5 | changed | tier 4, max 3 — max rank 5 → 3; tooltip changed; was Shadow row 4, col 4 |
| Shadow | Silence | 1 | changed | tier 5, max 1 — tooltip changed |
| Shadow | Vampiric Embrace | 1 | changed | tier 4, max 1 — tooltip changed; was Shadow row 5, col 2; tooltip changed in build 1.60.1.70170 (ranks 1) |
| Shadow | Improved Vampiric Embrace | 2 | **REMOVED** | removed from Classic |
| Shadow | Darkness | 5 | changed | tier 6, max 5 — tooltip changed |
| Shadow | Shadowform | 1 | changed | tier 7, max 1 — tooltip changed |

**7 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/priest/dps-pvp-arena>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
