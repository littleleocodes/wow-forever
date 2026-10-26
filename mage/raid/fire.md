# Fire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Fire

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Fire — Raid](../research/raid/builds/fire-open-raid.md)** (17/31/3) — [open the talent tree](https://talentsforever.com/mage/60/05122050000002-23550000130125031-003-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Fire — Ignite / Heating Up), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Pyroblast** when Heating Up has 3 stacks
2. **Fire Blast**
3. **Scorch** when the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 7.5 seconds left
4. **Arcane Missiles** (rank 7) when Missile Barrage is active
5. **Pyroblast** when Heating Up has 2 or more stacks and Heating Up has under 3.5 seconds left
6. **Fireball**

**Fireball** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Scorch**: in the last 3 seconds of the fight, when there is no time left for another **Fireball**
- **Combustion**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fire keeps its own **Improved Scorch** debuff at 5 stacks, fires **Fire Blast** on cooldown and casts **Fireball** in between. Crits build **Heating Up**; at 3 stacks **Pyroblast** becomes a 1.5-second cast.

**Why it works**

- **Fire Blast** first whenever it is ready: every 6 seconds with **Improved Fire Blast**, instant, and **Incineration** and **Critical Mass** make it crit often, feeding **Heating Up** and **Ignite**. The simulator measured using it on cooldown, with no mana saving, 3.7% better than the rule it replaced.
- **Scorch** keeps Fire Vulnerability at 5 stacks. In Forever **Improved Scorch** is your own debuff: +3% to your Fire damage per stack, for 30 seconds. Build 5 stacks, then refresh it once 7.5 seconds or less are left so a long cast cannot let it drop; the list shows only the stack count, but the early refresh is part of the rule (the simulator measured 7.5 seconds 0.4% better than 5).
- **Pyroblast** waits for 3 stacks of **Heating Up**. Each crit from **Fireball**, **Fire Blast** or **Scorch** takes 25% off your next **Pyroblast**'s 6-second cast, so 3 stacks make it 1.5 seconds: your biggest hit for its cast time. The list's 2-stack line is a last-chance rule: cast a 3-second **Pyroblast** at 2 stacks only if **Heating Up** has under 3.5 seconds left or the boss dies within 6 seconds.
- **Fireball** fills everything else: 3 seconds with **Improved Fireball**, about half your damage, and each crit also starts **Ignite**. The list stops starting it with under 3 seconds left, when it would land too late.
- **Combustion** at the pull and whenever it is back (3 minutes): each Fire hit adds 10% crit until you land 3 crits, which fills **Heating Up** fast. It shares its cooldown with **Presence of Mind** (client data), so a build with both gets only one of the two every 3 minutes.

**Caveats**

- Mana: Fire runs short even in a full raid. The simulator uses your mana gem (from **Conjure Mana Ruby**) at 80% mana and a mana potion whenever it is ready, and still runs dry now and then; **Master of Elements** refunds 30% of a spell's base cost on each crit.
- The raid list has no **Evocation**: in a 3-minute fight with raid buffs the simulator measured it slightly better without (0.2%). In a longer fight or without mana buffs, channel it when nearly empty with plenty of fight left; the simulator's list for playing without raid buffs does so below 10% mana with more than 25 seconds to go.
- Several targets: the simulator's own Fire list adds **Blast Wave** and **Flamestrike** at 3 or more targets; this build has no **Blast Wave**, so use **Flamestrike**.
- The simulator's boss resists nothing. Against an enemy that resists or ignores Fire, every spell here loses damage, and **Frostbolt** is your fallback.

**When to change it**

- In the last 3 seconds a **Fireball** would land too late: cast **Scorch**. The simulator's list uses Rank 1 there, the same line it falls back on when you cannot afford a **Fireball**; Forever gives ranks that low only part of your spell power and fewer talent procs, so use your top **Scorch** whenever you have the 150 mana.
- With 2 stacks of **Heating Up** and the boss dying within 6 seconds, cast **Pyroblast** now: the third crit may never come.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 850 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 837 | [17/31/3](https://talentsforever.com/mage/60/05022050010002-23550000130125031-003-7) |
| Phase 1 BiS | 857 | [17/31/3](https://talentsforever.com/mage/60/05022050010002-23550000130125031-003-7) |

**The gear** (average item level: Pre-BiS 63.0; Phase 1 BiS 64.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVU1oK1UUzrkzzZycvNeO14dvOiqMRaWOzPPOjPP6I5q0C/FnkSIIrrRJk5pRSUISpC6UKl2IYAtVKq1dSLFUi1pRkDbLrOJC6UpBFw3VorhREQouFLnT1mrbZdp3Fpd773cv3zdzv49DtyHoYIAF/TAORajANMDrAO8BfADAL0Uok+ggmLtJRB3NF0nDxmtg7CVJxd13gFT85W05vrutUxxbJeOHbtKwuQrG992kYLNEKu7NAWm4cXBNw08/AmNOIxUXtnVS8btVef+LaP7Xcg9p+OsnYLRuJhX/WJDQh8s9fffqrbD/61kQ+7mxN1fgDWAz4Tyw/dwSsJ9G1kFbW4Y9dzZsw0w4eun4u9LQYHeKQHieCIRwhRCe4/lBIIQQri9cLxC+6wjhtxhss+Quayd4n2nRLfYVBJ5oQpxU/H3LMLtIIfBNufxzHvjzfDxbeeGZcqVuecK77oghxxsYtiaK2dKzhbxVrlrZfL6Qt3IvWfViwaqW69l6WC5ZtUK2OlG0+muFgjUZVgtONRvmnSPYOYCvPVcrl+4xNUmK32b4OpzBNthhtofpQfMBMm0DFX65CUQqbnwOnOldUgZBQLfbt6LKLzf+hyHFSR24FtTkKdzJcNVkwzH+ygnFrnA8v8OKTbrJ7kGVs1zM1KiLlIHgLqlCbz3Epy6A/wolPwMkFb/aMgyQzPhj5pQzXOGIoQ4zR87QZ0K+ddIZkq3TzniSHuePRomIn0qER/eZDul2NyqcPRaT+SB2vUa99lVUeKLx7+nIJ770yVGEXr6AH9UbSYsfS/MPfLqW4YnDfO2c+WQdN0tEprdKF5iM+HEyXBElA9962lB+Zi34jXmvKrGo7k+vyEcihtD3N0vIrdj0ZLp3aVHWl6k7JqP6JuW1maFaKXuTxW5I1dNHs3Otuz8+N56haHzi/fTI4UZ6XPbbRYgWsXbKVnDz6uh/2rKAQUjDIzAGT0ERKjAFU+yfAQABSMTh); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVU9oI1UYz/dmmvnyZbc7Phd3OiqMRaWOzPpmxtm2K5rsHsQ/hyyC4EmbbFIzKklIgtSDUiUHEWyhlUJrD1Is1aJWFKTNMad4UHJS0ENDtSheVISClyJv2lpte0y73+Hx3vd7j99v5v1+PLoLQQcDLBiCMShCBSYB3gb4AOAjAH4uQplER8DcSiLqaL5KGjbfAmM7SSruzgCp+Nt7cny/o1Mc2yXjp37SsLUMxo/9pGCrRCpuTwNpuLZ3TMPPPwFjWiMVf1iWJ+c6OqnYmJXzrzo6afj7Z2C0bycV/5qTzY8XLww+qLfDoW+nQOzkbry7BO8Aa4QzwHZyC8B+ubYK2soibLtTYRca4fVzh9+Vhia7VwTC80QghCuE8BzPDwIhhHB94XqB8F1HCL/NoMOSW6yb4IOmRXfYFxF4ogVxUvHPDcPsI4XAN+Xy7xngL/OxbOWVF8qVuuUJ74ojRh1v+Kp1s5gtvVjIW+Wqlc3nC3kr95pVLxasarmerYflklUrZKs3i9ZQrVCwxsNqwalmw7xzADt78OWXauXSA6YmSfH7DF+FE9hGesz2OD1qPkKmbaDCz7eASMW1L4EzvU/KIAjobvtOVPn55v8wpDipw5eDmtyFmxmumuxqjL9xRLErHM/vsWKTbrMvoMpZLmZq1EfKcHCfVKG3H+MTZ8B/kZJfAJKK32wYBkhm/DlzzBmucMRoj5kjZ+iNkG8cdYZk67UznqWn+ZNRIuLHEuHRQ6ZDut2PCmdPxWQ+iF2p0YB9CRWeaP67O/KJL31yEKHXz+BHDUTS4ofS/D2frmR4Yj9fmydeWc/NEpHp7dIZJiN+mAxXRMnA2ecN5VfWhj+Y96YSi+rh9JK8JGIIg7ssIVuxyfH0wMK8rK9T94xH9V3K6zJDtVL2OovdkqqnD2anWvd/emo8o9H4zIfpa/uN9Jh8b+chWsS6KVvB9UvX//MsCxiBNDwBN+A5KEIFJmCC/TMApdjEaA==).

## Other builds of this spec

- [Fire — Ignite / Heating Up](../research/raid/builds/fire-raid.md) (14/34/3, 830 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0052205-23550020130135031-003-7)
- [Fire (optimized)](../research/raid/builds/opt-fire-raid-raid-dps.md) (18/31/2, 815 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/00522150000003-13550000130135031-002-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

