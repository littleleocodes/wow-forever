# Destruction — PvP (derived) — 21/0/30

*[Warlock](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Affliction / Demonology / Destruction) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Destruction PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Destruction (model affliction-leveling, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Destruction builds agree with (7592 builds).

## Point allocation

### Affliction (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Fel Concentration** | 3/3 | changed | Gives you a 70% chance to avoid interruption caused by damage while channeling or casting your Drain Life, Drain Mana, Drain Soul, or Wrack spells. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Nightfall** | 2/2 | changed | Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 4% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%. |
| **Curse of Exhaustion** | 1/1 | changed | Reduces the target's movement speed by 30% for 12 sec. Only one Curse per Warlock can be active on any one target. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |

### Demonology (0)

*No points.*

### Destruction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Destructive Reach** | 2/2 | changed | Increases the range of your damaging spells by 20%. |
| **Bane** | 3/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.3 sec and your Soul Fire spell by 1.2 sec. |
| **Molten Skin** | 5/5 | **NEW** | Reduces all damage taken by 10%. |
| **Aftermath** | 5/5 | changed | Increases the initial damage of your Immolate spell by 50% and your Conflagrate spell has a 100% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Shadowburn** | 1/1 | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. |
| **Intensity** | 3/3 | changed | Gives you a 70% chance to resist interruption caused by damage while casting or channeling any Destruction spell. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Conflagrate** | 1/1 | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. |
| **Pyroclasm** | 1/2 | changed | Gives your Soul Fire spell a 13% chance to Stun the target for 3 sec, and your Rain of Fire and Hellfire spells a 13% chance over their duration to Stun targets they damage for 3 sec. |
| **Bane of Havoc** | 1/1 | **NEW** | Afflicts the target for 5 min, causing 15% of all damage done by the Warlock to other targets to also be dealt to the cursed target. Bane of Havoc is limited to 1 target, and only one Bane per Warlock can be active on any one target. |

## Core talents (priority order)

1. **Siphon Life** — The scorer's value in this build: +21.2% of its score (model affliction-leveling).
2. **Improved Corruption** — The scorer's value in this build: +12.1% of its score (model affliction-leveling).
3. **Curse of Exhaustion** — The scorer's value in this build: +10.9% of its score (model affliction-leveling).
4. **Molten Skin** — The scorer's value in this build: +9.1% of its score (model affliction-leveling).
5. **Pandemic** — The scorer's value in this build: +6.4% of its score (model affliction-leveling).
6. **Suppression** — The scorer's value in this build: +5.8% of its score (model affliction-leveling).

## Notes

- Community tie-break moves: 1 point Pyroclasm -> Bane of Havoc; 3 points Cataclysm -> Agonizing Flames.
- Where we disagree with the community: most Destruction builds take Demonic Embrace (83% take it), Shadow and Flame (83% take it), Fire and Brimstone (82% take it), Demonic Aegis (75% take it), Demonic Sacrifice (74% take it), Fel Vitality (73% take it), which the model values below this build's weakest point; this build takes Amplify Curse (5%), Curse of Exhaustion (2%), Fel Concentration (1%), Nightfall (7%), Pandemic (8%), Pyroclasm (10%), Siphon Life (2%), which few Destruction builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- Scored with the Affliction leveling model (no Destruction leveling model): fire spells are under-valued.

## Open questions (verify in the live game)

- A derived Destruction PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
