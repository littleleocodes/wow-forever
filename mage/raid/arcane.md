# Arcane Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Arcane

**[Arcane — Raid](../research/raid/builds/arcane-open-raid.md)** (35/13/3) — [open the talent tree](https://talentsforever.com/mage/60/0532205003100311531-0355-003-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Arcane — Arcane Blast), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Arcane Missiles** (rank 7) when Missile Barrage is active
2. **Arcane Wrath** until the last 10 seconds of the fight
3. **Arcane Blast**: keep it on the target
4. **Fire Blast** until the last 40 seconds of the fight
5. **Arcane Blast** when you have at least 25% mana
6. **Fireball** (rank 11)
7. **Frost Blast**

**Frost Blast** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Presence of Mind**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Arcane Power**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Evocation**: when you run out of mana (needed in about 3 of 10 fights)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Arcane in a raid builds **Arcane Blast** stacks and spends them. Each **Arcane Blast** makes your next other spell stronger and the next **Arcane Blast** much dearer, so free **Arcane Missiles** from **Missile Barrage** and a **Fire Blast** every 6 seconds spend the stacks before the cost runs away.

**Why it works**

- **Arcane Blast** is the filler: a 2.5-second cast that adds a stack each time (up to 4, for 8 seconds). Each stack adds 10% to the damage of your other spells (15% to **Arcane Missiles**, fitted to beta logs) and 175% to the next **Arcane Blast**'s mana cost; casting any other damage spell spends them all.
- **Arcane Missiles** on **Missile Barrage** comes first. Each **Arcane Blast** that lands has a 40% chance to make your next Missiles free and twice as fast, and the Missiles spend your stacks at 15% each: about a third of your damage in the simulator.
- **Fire Blast** whenever it is ready is why this Arcane build spends 11 points in Fire: **Improved Fire Blast** brings it back every 6 seconds and **Incineration** adds crit. It is instant, it takes your stacks' bonus, and it puts **Arcane Blast** back to its base cost. Adding it was the biggest gain of the rotation search, about 8% over three steps.
- **Arcane Power** and **Presence of Mind** go at the pull: 30% more damage for 15 seconds (at 30% more mana cost) and one instant spell. Both have 3-minute cooldowns, so a 3-minute fight gets one of each.
- Mana: **Evocation** only below 15% mana with more than 20 seconds left. With a raid's mana buffs, your mana gems and a mana potion, the simulator almost never needed it.

**Caveats**

- Without a raid's mana buffs you run dry sooner. The simulator's list for playing without them also spends two stacks on a **Frostbolt** when **Fire Blast** is not ready, which keeps **Arcane Blast** cheap.
- Moving: **Arcane Blast** and **Arcane Missiles** both need you to stand. **Fire Blast** is your instant, and **Presence of Mind** makes one **Arcane Blast** instant.
- Threat: **Arcane Subtlety** cuts your Arcane threat by 30%, but the simulator ignores threat, and **Arcane Power** at the pull is when you are most likely to pull the boss.
- Several targets: this list is for one boss. **Arcane Explosion** hits everything within 10 yards.

**When to change it**

- In the last 40 seconds, stop resetting with **Fire Blast** and keep casting **Arcane Blast**. Its cost climbs, but mana left when the boss dies is wasted and your free Missiles spend bigger stacks; the simulator measured these end-of-fight rules about 1% better together.
- In the last 3 seconds an **Arcane Blast** cannot finish: cast the **Fire Blast** you saved.
- In a fight longer than 3 minutes, use **Arcane Power** and **Presence of Mind** again when they are back, and channel **Evocation** below 15% mana while more than 20 seconds remain.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 717 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 720 | [34/13/4](https://talentsforever.com/mage/60/0502205203100311531-0355-013-7) |
| Phase 1 BiS | 735 | [33/14/4](https://talentsforever.com/mage/60/0502205103100311531-1355-013-7) |

**The gear** (average item level: Pre-BiS 62.2; Phase 1 BiS 63.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Red Mageweave Headband](https://www.wowhead.com/forever/item=10033) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElU9ME1sUxnvuTNvbUwJ988h78+axmEcCr1Rr7kw7pLKwAyujiTSuXClTWmwNtk1bE1yJhIUhERIlGCoLJRLU4N+FARI2bKwmGjZqghuCEtQNJiboRmNmaMGocQX1W5y5c77c3N859yQX6yh4QAQZvNABCchAL8A5gCsA1wGEKsslphsC6a2bUg+VTqGD3jskrriRp8uXAHn6btiMlxc86KDFlPiqGp10fgLEl9XI0fkU8nRlCNBJ7/SBuc1J706BOOREni5OmDsfXzXjgwUP8vTzWA066dptEIt/Ik8/jJjWjbGa+t2eYtL7dBDYejRyfhwGgPQnLwBZjxaArLbeBDo5BlMDMJhcgv5kW9VWXTrMkjqmMVVlmsoCCmMBRdECip8FNM3PlECRwAJxL5M1l8BLpMUm1EoCuu6DA3n6ZEaU7MjR1+1CLwiGkek+ls7kZZWpzX6F+dVgi9yZMFLH4zE5nZWNWCwek6On5XwiLmfTeSOfTKfkXNzIdiZkby4el41sp5GK+2OZnL/s+zf8PSdy6VST9C/+4auhDoEcsElOtCOnsJxkkvR9iggjFUFQ0Cs0WhicQKJlDK3BStm3yEIsZ/Xm4lGhUBEwDXdJTehedFDk6dyMKAJKPpFygmvWuqy5GVFyFYi5HH52UCp9hYmKwOnYLAV/xYN/+WpNb37TsyOHoG5ynvkRk4W2G1P6fr6CpVt80V6x8fpfaECPr7pE4UAeSSBX5ioPnKo1bHbGJTnLjN0/QQxsN+LGaZPtwslKNIRada5+jFSwOM/DfSL3hhThPVHPcjZLQX3cHE0kFOq/EJeZsvV26f8URk09Cv/XZel5WF0iIi+HfdPE9luU18urHVXjrR07Z68VD1/TW0sJvcN8dkfB+rEthX0cnf677ZvXmUEIdNgPETgCCchAD/SQrwMAvmHLQw==); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElU9ME1sUxnvuTDu3pwT65pH35t3HYh4JvNL3+jIz7ZA+Fq8Dqxdd0LhypUxpsTXYNm1jcCUSFoZESABJqCwMkaAG/8SFARI2bKwxGjZqohuiEgwbTEzQFTEztMWocQX1W5y5c77c3N859yQXmyh4QQIZfNADScjCIMBFgKsA1wHEOtsllhsGtuWh1EvZWRTo8hBIGx7k6e44IE+3Jq14Zc2LLlpKS6/rUaCrcyC9rEeOrqaRpxtjgAK9s7dNoHcXQBoTkKePLkM1Dk9Y8f6aFwW6fRuk0s/I0/dTVvLGTEPz395SyvdkFJSdWPTSLIwAGU6NA9mJFYFsdt4EOj8DCyMwmlqH4VRX3X5hBiyTJkVXNE3RVSWoKkpQVfWgGlCDuh5Q1GCJwBrxvCLbbpFnpMMhNjIR3ffAhTx9vCQxJ3L0Tbc4CKJpZvtPZrIFWVO09oCqBLRQh9ybNNOnEnE5k5PNeDwRl2Pn5EIyIecyBbOQyqTlfMLM9SZlXz6RkM1cr5lOBOLZfKDiB/b8f07nM+k29jv+5G+gLpEccTABncipSp5ZJEMfo+JUTRBU9ImtNgYnklgFQ2+xU859srCSt3szcUIs1gRMx79YG3peuCjydGVJkgCZX6Kc6F62L2tlSWLuIrGWk0+PsvJXnKsJnIHtLPQ9HvzF32h5q1XPiRyCVuU8/zWmEj5oTPblfIXKt/i8u2bj9afYgl5/fZnChTySYL7CVRk4TW+pdsbNhApj/zcQgweNuHfafLd4phYNoXadmx+iNSzO++A/iXtLSvCOaBc4h62QMWuNJhIKzbvEbaUcg33Gb8VpSw8jf/TZehbR1onEyxH/InH8EBWMyupQ1Xrr0M75147Hrhmd5YTRY72702D/ONYjfo4u/tr12fOsQBgM+B+icBySkIUBGCCfBgAgOsrh).

## Other builds of this spec

- [Arcane — Arcane Blast](../research/raid/builds/arcane-blast-raid.md) (36/11/4, 671 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0552205003100301531-2305001-013-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

