# Holy — PvP (derived) — 0/35/16

*[Priest](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/35/16 (Discipline / Holy / Shadow) |
| **Role** | HEALER — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Holy (model holy-heal, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Holy builds agree with (5358 builds).

## Point allocation

### Discipline (0)

*No points.*

### Holy (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 3/3 | **NEW** | Gives you a 70% chance to avoid interruption caused by damage while casting any spell. |
| **Holy Specialization** | 3/5 | unchanged | Increases the critical effect chance of your Holy spells by 3%. |
| **Spell Warding** | 4/5 | unchanged | Reduces all spell damage taken by 8%. |
| **Divine Fury** | 5/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.5 sec. |
| **Holy Nova** | 1/1 | changed | Causes an explosion of holy light around the caster, causing 26 to 30 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 49 to 57. These effects cause no threat. |
| **Blessed Recovery** | 3/3 | changed | After being struck by a melee or ranged critical hit, or suffering more than 30% of your maximum Health from a single attack, heal 25% of the damage taken over 6 sec. Refreshing this effect carries over any remaining healing. |
| **Inspiration** | 3/3 | changed | Your non-periodic critical heals increase your target's Armor by 25% for 15 sec. |
| **Holy Reach** | 1/2 | unchanged | Increases the range of your Smite and Holy Fire spells and the radius of your Prayer of Healing and Holy Nova spells by 10%. |
| **Binding Heal** | 1/1 | **NEW** | Heals a friendly target and the caster for 236 to 284. Low threat. |
| **Litany of Light** | 1/2 | **NEW** | When you cast a healing spell, gain Mana equal to 5% of the base cost of the spell if your previous heal was a different spell. |
| **Spirit of Redemption** | 1/1 | changed | Upon death, the priest becomes the Spirit of Redemption for 15 sec. The Spirit of Redemption cannot move, attack, be attacked or targeted by any spells or effects. While in this form the priest can cast any healing spell free of cost. When the effect ends, the priest dies. |
| **Spiritual Guidance** | 5/5 | changed | Increases your spell healing by up to 25% of your total Spirit and your spell damage by up to 8% of your total Spirit. |
| **Spiritual Healing** | 3/3 | changed | Increases the amount healed by your spells by 10%. |
| **Prayer of Mending** | 1/1 | **NEW** | Places a spell on the target that heals them for 172 the next time they take damage or receive non-periodic healing. When the heal occurs, Prayer of Mending jumps to a party or raid member within 20 yards. Jumps up to 5 times and lasts 30 sec after each jump. This spell can only be placed on one target at a time per caster. |

### Shadow (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Blackout** | 5/5 | moved | Gives your Shadow damage spells a 10% chance to stun the target for 3 sec. |
| **Spirit Tap** | 1/5 | changed | Gives you a 20% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |
| **Shadow Reach** | 2/2 | changed | Increases the range of your offensive Shadow spells by 20%. |
| **Improved Psychic Scream** | 2/2 | moved | Reduces the cooldown of your Psychic Scream spell by 4 sec. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Each instance of damage of Mind Flay deals 20% more damage than its previous instance of damage. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |

## Core talents (priority order)

1. **Spiritual Guidance** — The scorer's value in this build: +21.2% of its score (model holy-heal).
2. **Divine Fury** — The scorer's value in this build: +12.9% of its score (model holy-heal).
3. **Prayer of Mending** — The scorer's value in this build: +11.2% of its score (model holy-heal).
4. **Vampiric Embrace** — The scorer's value in this build: +11.1% of its score (model holy-heal).
5. **Spiritual Healing** — The scorer's value in this build: +9.6% of its score (model holy-heal).
6. **Mind Flay** — The scorer's value in this build: +8.4% of its score (model holy-heal).

## Notes

- Community tie-break moves: 1 point Spell Warding -> Litany of Light; 1 point Holy Specialization -> Holy Reach; 1 point Shadow Focus -> Spirit Tap.
- Where we disagree with the community: most Holy builds take Meditation (91% take it), Twin Disciplines (86% take it), Inner Focus (84% take it), Improved Healing (83% take it), Improved Power Word: Shield (79% take it), Improved Renew (72% take it), which the model values below this build's weakest point; this build takes Blackout (2%), Improved Mind Flay (1%), Improved Psychic Scream (0%), Improved Shadow Word: Pain (2%), Mind Flay (1%), Shadow Reach (1%), Spell Warding (15%), Spirit Tap (13%), Vampiric Embrace (2%), which few Holy builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.

## Open questions (verify in the live game)

- A derived Holy PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
