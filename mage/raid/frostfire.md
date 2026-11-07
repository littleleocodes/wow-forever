# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-3550000123013303-2135000301113002-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Frostfire — Fingers of Frost / Ice Lance), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Pyroblast**.

**Then press the first one that is ready**, top to bottom:

1. **Scorch** when either the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 10 seconds left and the target has fewer than 4 stacks of Fire Vulnerability
2. **Pyroblast** when Heating Up has 3 stacks
3. **Fire Blast** when the target has fewer than 2 stacks of Fingers of Frost
4. **Frostfire Bolt**

**Frostfire Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Scorch**: in the last 3 seconds of the fight, when there is no time left for another **Frostfire Bolt**
- **Evocation**: when you run low on mana (about 1 time a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frostfire is a Fire list whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost, so both trees' talents apply, its chill rolls **Fingers of Frost**, and its crits stack **Heating Up** for a 1.5-second **Pyroblast**. **Scorch** keeps Fire Vulnerability at 5 stacks and **Fire Blast** fills between casts. **Ice Lance** is in the build only because **Fingers of Frost** requires it: the list never casts it. 759 DPS in a full raid, 8% behind the Fire page.

**Why it works**

- **Scorch** keeps Fire Vulnerability at 5 stacks (**Improved Scorch**: 3% more Fire damage per stack for 30 seconds, and **Frostfire Bolt** counts as Fire) and refreshes it under 10 seconds left, a wider margin than the Fire list's 5 (+2.2% in the search), between casts unless the stacks are under 4. About 14 casts and 7% of the damage. Trinkets and the other cooldowns wait for the fifth stack.
- **Pyroblast** at 3 stacks of **Heating Up** (12 casts, 22%, and most of **Ignite**'s 13%): crits from **Frostfire Bolt**, **Fire Blast** and **Scorch** cut its cast by 25% each and **Fire Blast** adds a stack on every hit. One hard cast before the pull.
- **Fire Blast** (21 casts, 17%) every 6 seconds with **Improved Fire Blast**, but only while fewer than 2 **Fingers of Frost** charges are up. A proc treats your next 2 spells as cast on a frozen target, where **Shatter** adds 50% crit chance: the list spends both charges on **Frostfire Bolt**, whose crit starts **Ignite** and a **Heating Up** stack, and holds **Fire Blast** until a charge is gone.
- **Frostfire Bolt** fills everything else (40 casts, 41%): 2.5 seconds with **Accelerant**, 370 mana less **Frost Channeling**'s 15%, a 40% slow, **Ice Shards**' doubled crit bonus and **Critical Mass**'s 6% crit, and one cast rolls for **Fingers of Frost**, **Heating Up**, **Ignite** and **Master of Elements**' refund at once. It is checked against the lower of the target's Fire and Frost resistance.
- **Ice Lance** has no line: on the same **Fingers of Frost** charge a **Frostfire Bolt** is worth more than its 136-160 damage, and the search dropped the **Ice Lance** line in its last passes. The talent is the one point **Fingers of Frost** requires.
- **Fire Power** adds 3% Fire damage per Fire effect of yours on the target, up to 12%: Fire Vulnerability, **Ignite** and **Pyroblast**'s burn count; **Frostfire Bolt**'s own burn, a mixed school, does not.
- Mana: your mana gem (from **Conjure Mana Citrine**) whenever it is ready, two mana potions, a Demonic Rune, **Master of Elements**, and **Evocation** once a fight (an 8-minute cooldown). In a 6-minute fight the simulator's DPS falls to 306: this list is the mage's most front-loaded.

**Caveats**

- **Fingers of Frost** charges go to the next 2 spells you cast, whatever they are: do not spend one on a **Scorch** refresh if a **Frostfire Bolt** fits.
- Moving: **Fire Blast** and the 1.5-second **Scorch**. For packs, **Flamestrike** and **Blizzard**.
- **Frostfire Bolt** is new in Forever: its numbers are the simulator's model of the tooltip, not checked in game.
- The simulator's boss resists nothing. Against Fire resistance **Frostfire Bolt** keeps working (the lower of the two resistances), while **Fire Blast**, **Scorch** and **Pyroblast** lose damage.

**When to change it**

- In the last 3 seconds, **Scorch** instead of starting a **Frostfire Bolt**.
- Out of mana with the fight going on: **Evocation** if it is back, else **Scorch** (150 mana) keeps the stacks and **Heating Up** moving until a gem or potion returns.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 759 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 821 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-12) |
| Phase 1 BiS | 842 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-12) (ties this build) |

**The gear** (average item level: Pre-BiS 65.4; Phase 1 BiS 66.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Coronet](https://www.wowhead.com/forever/item=16441) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Field Marshal's Coronet](https://www.wowhead.com/forever/item=16441) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Marshal's Silk Leggings](https://www.wowhead.com/forever/item=16442) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Marshal's Silk Leggings](https://www.wowhead.com/forever/item=16442) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Marshal's Silk Footwraps](https://www.wowhead.com/forever/item=16437) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Marshal's Silk Footwraps](https://www.wowhead.com/forever/item=16437) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) · *sold by Gaelden Hammersmith* | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) · *sold by Gaelden Hammersmith* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG0UU9pvdxOOXNHGmULbbHKaGkGQTJ/uTVEmQiFsJUUpRKk6IA3Tt3Y0XHK/l3UTtLUAPqBIpLVWrhCKhiAqKQEhFQJMLwhfMpao4gASHREEVCHEgQarEBaFZJ2249NZwyJM8s/PefO/NfO95ZrCTQhoU4NADJ6EIFZgFeBPgfYCPAFhrbCXCOgLq+Q5K01SdwSRdmgXldgvKdO0yoEx/vyjam28DNtN6WfmlDZO0dhWUn9tQorUyyvT2OcAkXW7AkvSLWVDOJVGmP10VyLk/0ijTL2+J9vzXaUzSd78Cpb4XZfrXJTHh2pX2TH+67vfcnAP9Tv7EW4twFsgZ/wKQO/kFIL8e/hjoh1fgk7Mw56/CGf8IjZcOOVgmmezQ8LCu67phWvHPypqGJTSWbhiGpetmncAt0rJGLrbjY0jVZpTp3xcgo1wnD1OJpRbIpkZYkGQNVmGuXSm9HFQiburmoayhZy1jjBeKdnnSdXhQ5bbjuA7Pn+ZR0eXVILIjPyjz0LWrhSLvCV2Xe9UgjDy/6martu9kt+ZkG3MGXgmDcq+aVJtQSn/7JJsnbB22xxJ+A8/zC75d4qE/NV2yo6DaHfIpe9IddCrhoF0phYOelx+wK6XYHbcjPjxUcO3CIWuE205QiVyH99yNXLInuT3t+BG3vcitNpbuZit+eYz3mQN6F/eChtYtR9XT3SHPu2HE89N+yeF+mdvcmy6VuNhOP+8zBowuHgUCaTaQfhTykh+KoDEm7OeG3q/rOvf8yWIU8pgh1wm5ye2yw61e9VHcq3VQiZEXE2pqQ9rMwxq0YOqpmaAQs8pWYKfSMYNT7FV8Qh1FVVOoxPbUAFGmn30OjKSJyBXCMB7Q9gvb8n9scekYOvar2n3AQ9iaQaQb0IQSXZkQHunKBLu0O7PPsVNTKbD2GrTeY0qBTaLHEuza7iTGwl7Wjfu0hyiwVA3E32J9SWnQYuGeTAumNmDboSV6dnl3cnUQFW0flVhLDSjK9L1lZauATNHRHyfYGzt2gKiY1tpoMyPHEiIvSKxQ9PSb2rM7fKnQlQlF0hZh+0H6jPo0djK1UUDX4wJarj+Hqe9l8bm0ftzs3rwel9aP44HXQUGJvvOS2qG1iz3lE2oSm1AaHe1ix9Sj2Kf2NlzdxTeGi7A1vBfkPr5+I3X4k5ivSYlYhnIxHgmFzD8kJVSJWS+3f2FeyHfjB71Yfhg3V4ki83HtBkn8LxLltr4eqDz+6QOLMxq3z3+QO7ypyJ0Uz8N5iAeJ1XFNojceObLtFanDCOTgKJyAF6AIFTgFp8i/AwD3I4ZR); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk9MHFUY3+/NwL79oLC8ap1OObyuIjCwMH+gAUxk28RYaw2NJ+NBO7szw44uO5udgbQ3VA6miW2ktQasiSE2WqMxqVELN9eDa0xM40EPHiA1jcaTYNLES2PeLFC89FY88CX73rzve7/ve+/3ffvew04KaVCAQw+chiJUYBbgTYAPAD4GYK2xlQjrCKhvd1CapuoMJunyLCi3W1Cmd+cBZfrnJdF+exWwmdbLym9tmKS1q6D82oYSrZVRprcvACbpSgOWpF/OgnIhiTL94R3Ybr+6mUaZzl0UM9/7GpT6fpTp35eF6dqV9kx/uu73/Hge9Dv5U28twTkgc/48kDv5RSC/H/0E6EdX4NNzcN5fgzn/GI2XDjlYIZns0PCwruu6YVrxz8qahiU0lm4YhqXrZp3ATdJyi1xqx8eQqs0o03/mIaNcJw9TiaUWyaZGWJBkDVZhrl0pvRxUIm7q5pGsoWctY4wXinZ50nV4UOW247gOz5/lUdHl1SCyIz8o89C1q4Ui7wldl3vVIIw8v+pmq7bvZLfmZBtzBl4Jg3KvmlSbUEp/9yRbIGwddsYSfgPP8wu+XeKhPzVdsqOg2h3yKXvSHXQq4aBdKYWDnpcfsCul2B23Iz48VHDtwhFrhNtOUIlch/dsRy7Zk9yedvyI217kVhtLd7MVvzzG+8wBvYt7QUPrlqPq2e6Q590w4vlpv+Rwv8xt7k2XSlxsp5/3GQNGF48CgTQbSD8KeckPRdAYE/ZzQ+/XdZ17/mQxCnnMkOuE3OR22eFWr/oo7tc6qMTIiwk1tSFt5uEWtGDqqZmgELPKVmG30jGDU+xVfEIdRVVTqMT21QBRpp9/AYykicgVwjAe0g4K28p/bHHpGDr2q9p9wEPYmkGkG9CEEl2dEB7p6gS7vDezz7FTUymw9hq03mNKgU2ixxLs2t4kxsJe1o0HtIcosFQNxN9ifVlp0GLhvkwLpjZgx6Elevbu3uTqMCraASqxlhpQlOn7K8pWAZmio79MsDd27QBRMa210WZGTiREXpBYoejpN7Vnd/lSoasTiqQtwc6D9Bn1aexkaqOArscFtFJ/DlM/yeJzef2k2b15PS6vn8RDr4OCEr34ktqhtYs95RNqEptQGh3tYifU49in9jZcbeMbwyXYGt4Lch9ff5A6/EXM16RELEO5GI+EQuYuSQlVYtbLHVxcEPL9+GEvlp/HzTWiyHxcu0ES/4tEua2vByqPf/bA4ozG7fMf5o5uKnKnxfNwAeJBYm1ck+iNR47teEXqMAI5OA6n4AUoQgXOwBny7wC7KYXi).

## Other builds of this spec

- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 751 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-3551000113013303-2135000301113002-12)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (7/31/13, 694 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0410011-32510301230133031-20350003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 5ad0894 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

