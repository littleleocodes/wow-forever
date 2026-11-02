# Arcane Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Arcane

**[Arcane — Raid](../research/raid/builds/arcane-open-raid.md)** (31/17/3) — [open the talent tree](https://talentsforever.com/mage/60/023205203100211531-554000011001-003-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Arcane — Arcane Blast), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Arcane Missiles** (rank 7) when Missile Barrage is active
2. **Arcane Wrath** until the last 10 seconds of the fight
3. **Arcane Blast**: keep it on the target
4. **Pyroblast** when Heating Up has 3 stacks
5. **Fire Blast** until the last 40 seconds of the fight
6. **Arcane Blast** when you have at least 25% mana
7. **Fireball** (rank 11)

**Fireball** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Presence of Mind**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Arcane Power**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Evocation**: when you run low on mana (about 1 time a fight)
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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 742 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 800 | [32/16/3](https://talentsforever.com/mage/60/023205203100311531-553000011001-003-7) |
| Phase 1 BiS | 817 | [32/16/3](https://talentsforever.com/mage/60/023205203100311531-553000011001-003-7) (ties this build) |

**The gear** (average item level: Pre-BiS 67.3; Phase 1 BiS 68.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Coronet](https://www.wowhead.com/forever/item=16441)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Field Marshal's Coronet](https://www.wowhead.com/forever/item=16441)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Beads of Ogre Mojo](https://www.wowhead.com/forever/item=22149) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Field Marshal's Silk Spaulders](https://www.wowhead.com/forever/item=16444) | [Field Marshal's Silk Spaulders](https://www.wowhead.com/forever/item=16444) |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Marshal's Silk Leggings](https://www.wowhead.com/forever/item=16442)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Marshal's Silk Leggings](https://www.wowhead.com/forever/item=16442)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Marshal's Silk Footwraps](https://www.wowhead.com/forever/item=16437)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Marshal's Silk Footwraps](https://www.wowhead.com/forever/item=16437)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Grand Marshal's Tome of Power](https://www.wowhead.com/forever/item=23452) | [Grand Marshal's Tome of Power](https://www.wowhead.com/forever/item=23452) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzE1k1MG0cUAGC/2cU7fi7gTlG7nfawpaWAW1ezuzaiHGrDpX8HrPbSW1ljU7uitmVbFT3VrajUIhUQqqri+tCiItoqXCIlYBQuXOJECuKSRCIXlASRY5IDSQ6Jol1shAiKcgDnHd6M52k034x3pMHXKfhABQ26YAiSkIUiwM8AfwH8C8BecKrErvYCn2ym1Ef5t6jQShHUbS/K9KdFQJmeK9p5fRrQTatp9UYLKnRtHtRrLSjRtTTKdHsKUKEre9MUeqYI6pSCMt2ct2de/NvOZzd8KNOH5VZU6J9LoFZfQpmWl+zSf+XW9nd91VTX+iSI3Vj01zmYADKemgGyGysB2en/H+hCGU5NwGRqC8ZTA9ShQwRWyJvCMA0RMoSpC2HqesjUA6GQKYQQui6EHhDCrBLYIN7rZNrLZE76XKyNM/ScBjfK9FJF5U0o0ZuDrAjMsrKjX2ayBc0QRk9AFwEj2KcNJ630V4m4lslpVjyeiGux77RCMqHlMgWrkMqktXzCyg0nta58IqFZuWErnQjEs/lAvR7Yq7/3dT6T7uav4Yv+Vupm5BMXV7AJJV3kuS358X6UlRpCCOE7vBu9m26KMl2tqCog96tUYp4V50xWKyr3lIjd/e3yp7zWsl+OwJn6cePeeibLckMsn+PH7EPs4cGnmfBlfxuVmWdtv9aEEoKBze1e9NyFw/Q/GkI3sZt1OjSo0+7UaeZB2oMZ4LWWff+kTPQet4wfvgBBkbdd9Oog+70h37+OnawDff6WmsKNMhIzX3fFai4j1LH/p3m4UjeOHkE0j5u4t9rCIPumEQdCnX3u3Is2cHO+8x+o0i1ShdvE+EFyORGMzNnXBQmF9kfEYw+5iiORV0uzdlwIvzHixJWwsUVUWQv7l4nruUQhUu+daLy9eGLrvO/kz/6J9NcGIkP222AWnB+urbBfosuvDBx4QgjohQh8BFH4ApKQhTEYI48HAMs+/GI=); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzE1j9MW0cYAHB/9x5+588F3CtqX68dXmkp4NbVvfdsRBlqw9J/A1a7dCvP2NSuqG3ZVkWnuhVDi1RAtKqKy5CgIJIoWSIlYBQWljiRgliSSGRBSRAZkwwkWVD0HjZCBEUZwPmG78736XS/O7+TDt+l4AMVNOiAAUhCFooAfwCcADgNwF5zqsSudgMfb6TUR/nPqNByEdRNL8p0ZwpQppeLdl6dBHTTSlq924QKXZkD9XYTSnQljTLdnABU6NLuNIVeLII6oaBM1+fsmddO2nn0bztfWvOhQv9fALXyBsp0ZsEePDPT3Pqxr5LqWB0HsR2L/jULY0BGU1NAtmMlIFu9Z4HOz8C5MRhPbcBoqo86dIjAEnlfGKYhQoYwdSFMXQ+ZeiAUMoUQQteF0ANCmBUCa8R7h0x6mcxJj4u1cIaeC+BGmV4vq7wBJXqvnxWBWVZ2+PtMtqAZwugK6CJgBHu0waSV/iER1zI5zYrHE3Et9otWSCa0XKZgFVKZtJZPWLnBpNaRTyQ0KzdopROBeDYfqNUDu/VPfsxn0p38HXzd30zdjHzl4go2oKSLPLclvz+JslJdCCH8iHeid91NUabLZVUF5H6VSsyz5JzJclnlnhKxu//c+JpXW/bnIThTP2rcBy9lWayL5Vv8kn2OXTz4IhO+6W+hMvOs7NUaUEIwsLHVi55HcJD+X13oJnaydocGNdrDGs3cT3s6Bbzasl+fl4nuo5bxgxcgKPK2i97qZ//W5fvXsZ21oc/fVFW4UUZi5muuWNVlhNr2/jQPV2rG4UOI5lETd1eb72c/1eNAqLPPrcfROm7Od+UzVbpPKvCAGL9JLieCkVn7uiCh0LpDPPaQqzgUebs0bcfV8HtDTtwMGxtElbWwf5G4XkkUIrXescaH549tnU+d/M2pSG91IDJgvw2mwfnh2gj7Jbr4Vt++J4SAbojAFxCF7yAJWRiBEfJsAF/3/DA=).

## Other builds of this spec

- [Arcane — Arcane Blast](../research/raid/builds/arcane-blast-raid.md) (31/13/7, 657 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/050205203100301531-505001002-043-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

