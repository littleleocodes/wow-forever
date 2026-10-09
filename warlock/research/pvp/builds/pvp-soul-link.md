# Soul Link / Shadow Mastery (PvP) — 30/21/0

*[Warlock](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/21/0 (Affliction / Demonology / Destruction) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `pvp-soul-link` |

## Summary

Soul Link moved to Demonology tier 5 (behind Demonic Sacrifice at tier 3), so a Soul Link warlock can now also reach Shadow Mastery, Siphon Life, Malevolence and Curse of Exhaustion: the Classic 20/31/0 becomes 30/21/0 with far more damage.

## Point allocation

### Affliction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Malediction** | 5/5 | **NEW** | Increases all periodic damage done by your Warlock spells by 5%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 3/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 3%. |
| **Nightfall** | 2/2 | changed | Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 4% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%. |
| **Curse of Exhaustion** | 1/1 | changed | Reduces the target's movement speed by 30% for 12 sec. Only one Curse per Warlock can be active on any one target. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Shadow Mastery** | 5/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 5%. |

### Demonology (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Unholy Power** | 1/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 2%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Master Summoner** | 2/2 | moved | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 4 sec and the Mana cost by 40%. |
| **Fel Domination** | 1/1 | changed | Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |

### Destruction (0)

*No points.*

## Core talents (priority order)

1. **Soul Link** — 30% of damage taken goes to the pet; now only 21 Demonology points.
2. **Shadow Mastery** — Shadow damage.
3. **Siphon Life** — Self-healing DoT.
4. **Curse of Exhaustion** — Snare curse (requires Amplify Curse).
5. **Nightfall** — Instant Shadow Bolt procs.
6. **Fel Domination** — Instant re-summon after the pet dies (requires Master Summoner 2).
7. **Improved Voidwalker** — Stronger Sacrifice shield and Consume Shadows.
8. **Pandemic** — DoT crit damage.
9. **Malevolence** — Shadow crit (3/5).
10. **Demonic Embrace** — Stamina.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Fel Vitality 3 + Demonic Aegis 2 + Demonic Energies (2) + Unholy Power 1 | Improved Health Funnel, Improved Imp | Nine Demonology filler points are needed between tier 1 and Soul Link; pick pet survivability. |
| 2 | Nightfall | Malevolence 5 | Procs vs. crit. |

## Notes

- Demonic Sacrifice is the Soul Link prerequisite in Forever but is not used — sacrificing the pet would remove the Soul Link partner.

## Open questions (verify in the live game)

- Whether Soul Link still requires the pet to be alive to work (demo wording implies yes).

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
