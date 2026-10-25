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
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Shroud of Arcane Mastery](https://www.wowhead.com/forever/item=22330) · *Blackrock Depths* | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Netherwind Pants](https://www.wowhead.com/forever/item=16915) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Elemental Attuned Blade](https://www.wowhead.com/forever/item=20698) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMlM1PE10UxnvuDJ3D4ePtO8Q4jC6uJJLaOOZOyxhgM4WV0YWYuHClTOlAa7Bt2i5wJSgmhgUadYNxA4lRE0DiCln6lcFUwwZN0Bg/YnThgqBh48bMUOw/oMYnmcy5z7kn93dPcg81IkRAAw5REKC2/loxAZ2QhD44AQUYBdBXZcQI6kVS8MccaJ8aSMYL94BkfPetiWRcmgcKo5fTPjaTgg9vgfa6mSR8MkQyvt1sojBuDPpVCi7MgnZZIRkfzfvlz6aBJDzvkoRXzpCCa9OgeS0k44N5P7Ex3LYfx7MRL8tv34Toi0kQm6m+mccwAWw8exXYZuoOfO5ZhNkJWIHJbC/VbrTEdsUtIYQlRMI0/c9KmIaZMC1DWJbHYIU1fGDvmSrrrDukJnSTomo7/R/7DyWVpUK6QnUkmdbewKpT2eGqFRclvY4kvHZS3aG3UP19CJOM39eY7v/HnoJ6TnWcwvCpfKHM4yJ+0DCFITq7+UDGyQ25aZ4vcieddtM8dZaXMy4v5stOOZvP8ZLrFAcyPFpyXe4UB5yca6QLJWM7b2zlD5wu5XP7dD3gCte4Oqpcr47+LYBIrLkKECaZWKIUdOD66hG1XleqLJr0hXmwzuJjUihQR3LGbxgxhLa7Ur1vhUYHk603pnwt23sGA7204+tMk7kd81jon1I5uR39UbXP/fZzup5XKpXG/oVkT9VI9sMlgCnI5tcvLh9ftbsCN7Ri9/g7K5Wv9rGt4I0dk3BxZ+/u2vvamhGHgimRgQKMwIj6cwC6GsoL); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMVM9LFFEc3++b0Xl+NdtGonHq8BKSbWnizawT6mVGT1GHDDp0Kmfd0Z2QnWVnAzulsUJ4MNA8GF0SogIV6WSdol+stJUX+33oB1GHDlLhJYiYcc1/oKIPvPe+7/N5Pz7vC++LDRTioACDBHCQm3/PCId2sKEHjkMehgHUFyKlcaqeRon+mAPlYz2K9OcEoEjfftuCIn15BVCiS1OgfGhEid69CsrrRhTogwEU6Z2pUJwsRfskujALygUJRfpoKjzg3nzYlyYBBXrORYk+HQWl3IQivTUfcl8HW/bRkhcve+zaZUg8GQe+lu6ZuQ9jQEreBJC19HX41LUIs2OwDONeN24+6jbZaZicc5PzlK6HzUzpmp7STY2bZpnAMql/T94RWVRJZ0xOqTom5FbcltxKBZmkY6qENSjo5p6IqpHJoSpl8ECtQYFOnpC3q01YdxNqUaTfXxE1HEcegnxWdpz84Ek/X2QGNw5oOtd4eyfryzq5ATfD/AJzMhk3w9JnWDHrsoJfdIqen2OB6xT6siwRuC5zCn1OztUy+UDb0LV1ff+pwM/tVdXIV+2mr7aqr+dH/pWBeLKxaqAWRSSpIMrAxZXDcp0qVb0owmdShlVijAixCG32TJgwJBRabgh1IRUb7rebL02HWLJ290d4ZhmrRBGZlSyT2H+For0R/VW0zv3xezoeVyqVht4Fu6tK2L1wHmAaPH91dOnYitURsbFlqytcWal8sY6uB2+spEAXd3Tv2vxf62XiYFQospCHIRiSfw0AHX3Jyw==).

## Other builds of this spec

- [Arcane — Arcane Blast](../research/raid/builds/arcane-blast-raid.md) (36/11/4, 671 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0552205003100301531-2305001-013-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-25 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

