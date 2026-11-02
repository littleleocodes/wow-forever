# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-3550000123013303-2135000301113002-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Frostfire — Fingers of Frost / Ice Lance), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Pyroblast**.

**Talents with no line below:** **Ice Lance**: taken because Fingers of Frost requires it.

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

Frostfire is a Fire mage whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost damage, so both trees' talents apply, and its chill lights up **Fingers of Frost** for **Ice Lance**. The Fire side adds **Fire Blast**, **Scorch** upkeep and **Pyroblast** at full **Heating Up**.

**Why it works**

- **Ice Lance** on **Fingers of Frost** comes first. Each **Frostfire Bolt** chill has a 15% chance to treat your next 2 spells as if the target were frozen; a frozen target takes 300% more damage from **Ice Lance** and **Shatter** adds 50% crit, so spend both charges on **Ice Lance**.
- **Pyroblast** at 3 stacks of **Heating Up**: crits from **Frostfire Bolt**, **Fire Blast** and **Scorch** each take 25% off its 6-second cast, so 3 stacks make it 1.5 seconds. Unlike the Fire list, this one never casts it at 2 stacks; the simulator measured dropping that line 0.3% better.
- **Fire Blast** on cooldown (every 8 seconds: this build has no **Improved Fire Blast**): instant, and its crits feed **Heating Up** and **Ignite**. Using it without a mana condition was the biggest single gain of the full-raid rotation search, about 5%.
- **Scorch** keeps Fire Vulnerability (from **Improved Scorch**) at 5 stacks, +15% to your Fire damage, and **Frostfire Bolt** counts as Fire. This list refreshes it once 15 seconds or less of its 30 are left, a wider margin than the Fire list's 7.5.
- **Frostfire Bolt** is the main spell: 2.5 seconds with **Improved Fireball**, and one cast rolls for **Fingers of Frost**, **Heating Up** and **Ignite** at once. Below 30% mana the full rotation casts Rank 2 (285 mana against 370): the page's line "when your mana is below 30%". The simulator measured this about 2% better than the old rule of stopping at 10% mana.
- **Fireball** (Rank 2 in the full rotation) is last: a stopgap for when you cannot afford even a Rank 2 **Frostfire Bolt**. Forever gives ranks that far below your level only part of your spell power; keep your mana up with gems and a potion so it rarely comes up.

**Caveats**

- **Fingers of Frost** charges go to the next 2 spells you cast, whatever they are: do not let a **Frostfire Bolt** use one up.
- Mana: **Frostfire Bolt** costs 370 at top rank. The list uses both of your mana gems (from **Conjure Mana Ruby** and **Conjure Mana Citrine**), **Master of Elements** refunds 30% of the base cost on each Fire or Frost crit, and below 30% mana the cheaper Rank 2 stretches what is left.
- Moving: **Ice Lance** and **Fire Blast** are instant. For packs, **Flamestrike** and **Blizzard** are your area spells.
- **Frostfire Bolt** is new in Forever: its numbers here are the simulator's model of the beta tooltip, not yet checked in game.
- The full rotation also opens with **Arcane Power** for builds that take it; this build does not, so skip it.

**When to change it**

- Below 30% mana, switch to Rank 2 **Frostfire Bolt** rather than stop casting it; a **Fireball** is a weak stopgap only for when even that is out of reach.
- Against a target that resists Fire, **Frostfire Bolt** keeps working (it is checked against the lower of the target's Fire and Frost resistance), while **Fire Blast**, **Scorch** and **Pyroblast** lose damage.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 759 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 821 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-7) |
| Phase 1 BiS | 842 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-7) (ties this build) |

**The gear** (average item level: Pre-BiS 65.4; Phase 1 BiS 66.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Coronet](https://www.wowhead.com/forever/item=16441)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Field Marshal's Coronet](https://www.wowhead.com/forever/item=16441)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Marshal's Silk Leggings](https://www.wowhead.com/forever/item=16442)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Marshal's Silk Leggings](https://www.wowhead.com/forever/item=16442)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Marshal's Silk Footwraps](https://www.wowhead.com/forever/item=16437)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Marshal's Silk Footwraps](https://www.wowhead.com/forever/item=16437)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG0UU9pvdxOOXNHGmULbbHKaGkGQTJ/uTVEmQiFsJUUpRKk6IA3Tt3Y0XHK/l3UTtLUAPqBIpLVWrhCKhiAqKQEhFQJMLwhfMpao4gASHREEVCHEgQarEBaFZJ2249NZwyJM8s/PefO/NfO95ZrCTQhoU4NADJ6EIFZgFeBPgfYCPAFhrbCXCOgLq+Q5K01SdwSRdmgXldgvKdO0yoEx/vyjam28DNtN6WfmlDZO0dhWUn9tQorUyyvT2OcAkXW7AkvSLWVDOJVGmP10VyLk/0ijTL2+J9vzXaUzSd78Cpb4XZfrXJTHh2pX2TH+67vfcnAP9Tv7EW4twFsgZ/wKQO/kFIL8e/hjoh1fgk7Mw56/CGf8IjZcOOVgmmezQ8LCu67phWvHPypqGJTSWbhiGpetmncAt0rJGLrbjY0jVZpTp3xcgo1wnD1OJpRbIpkZYkGQNVmGuXSm9HFQiburmoayhZy1jjBeKdnnSdXhQ5bbjuA7Pn+ZR0eXVILIjPyjz0LWrhSLvCV2Xe9UgjDy/6martu9kt+ZkG3MGXgmDcq+aVJtQSn/7JJsnbB22xxJ+A8/zC75d4qE/NV2yo6DaHfIpe9IddCrhoF0phYOelx+wK6XYHbcjPjxUcO3CIWuE205QiVyH99yNXLInuT3t+BG3vcitNpbuZit+eYz3mQN6F/eChtYtR9XT3SHPu2HE89N+yeF+mdvcmy6VuNhOP+8zBowuHgUCaTaQfhTykh+KoDEm7OeG3q/rOvf8yWIU8pgh1wm5ye2yw61e9VHcq3VQiZEXE2pqQ9rMwxq0YOqpmaAQs8pWYKfSMYNT7FV8Qh1FVVOoxPbUAFGmn30OjKSJyBXCMB7Q9gvb8n9scekYOvar2n3AQ9iaQaQb0IQSXZkQHunKBLu0O7PPsVNTKbD2GrTeY0qBTaLHEuza7iTGwl7Wjfu0hyiwVA3E32J9SWnQYuGeTAumNmDboSV6dnl3cnUQFW0flVhLDSjK9L1lZauATNHRHyfYGzt2gKiY1tpoMyPHEiIvSKxQ9PSb2rM7fKnQlQlF0hZh+0H6jPo0djK1UUDX4wJarj+Hqe9l8bm0ftzs3rwel9aP44HXQUGJvvOS2qG1iz3lE2oSm1AaHe1ix9Sj2Kf2NlzdxTeGi7A1vBfkPr5+I3X4k5ivSYlYhnIxHgmFzD8kJVSJWS+3f2FeyHfjB71Yfhg3V4ki83HtBkn8LxLltr4eqDz+6QOLMxq3z3+QO7ypyJ0Uz8N5iAeJ1XFNojceObLtFanDCOTgKJyAF6AIFTgFp8i/AwD3I4ZR); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk9MHFUY3+/NwL79oLC8ap1OObyuIjCwMH+gAUxk28RYaw2NJ+NBO7szw44uO5udgbQ3VA6miW2ktQasiSE2WqMxqVELN9eDa0xM40EPHiA1jcaTYNLES2PeLFC89FY88CX73rzve7/ve+/3ffvew04KaVCAQw+chiJUYBbgTYAPAD4GYK2xlQjrCKhvd1CapuoMJunyLCi3W1Cmd+cBZfrnJdF+exWwmdbLym9tmKS1q6D82oYSrZVRprcvACbpSgOWpF/OgnIhiTL94R3Ybr+6mUaZzl0UM9/7GpT6fpTp35eF6dqV9kx/uu73/Hge9Dv5U28twTkgc/48kDv5RSC/H/0E6EdX4NNzcN5fgzn/GI2XDjlYIZns0PCwruu6YVrxz8qahiU0lm4YhqXrZp3ATdJyi1xqx8eQqs0o03/mIaNcJw9TiaUWyaZGWJBkDVZhrl0pvRxUIm7q5pGsoWctY4wXinZ50nV4UOW247gOz5/lUdHl1SCyIz8o89C1q4Ui7wldl3vVIIw8v+pmq7bvZLfmZBtzBl4Jg3KvmlSbUEp/9yRbIGwddsYSfgPP8wu+XeKhPzVdsqOg2h3yKXvSHXQq4aBdKYWDnpcfsCul2B23Iz48VHDtwhFrhNtOUIlch/dsRy7Zk9yedvyI217kVhtLd7MVvzzG+8wBvYt7QUPrlqPq2e6Q590w4vlpv+Rwv8xt7k2XSlxsp5/3GQNGF48CgTQbSD8KeckPRdAYE/ZzQ+/XdZ17/mQxCnnMkOuE3OR22eFWr/oo7tc6qMTIiwk1tSFt5uEWtGDqqZmgELPKVmG30jGDU+xVfEIdRVVTqMT21QBRpp9/AYykicgVwjAe0g4K28p/bHHpGDr2q9p9wEPYmkGkG9CEEl2dEB7p6gS7vDezz7FTUymw9hq03mNKgU2ixxLs2t4kxsJe1o0HtIcosFQNxN9ifVlp0GLhvkwLpjZgx6Elevbu3uTqMCraASqxlhpQlOn7K8pWAZmio79MsDd27QBRMa210WZGTiREXpBYoejpN7Vnd/lSoasTiqQtwc6D9Bn1aexkaqOArscFtFJ/DlM/yeJzef2k2b15PS6vn8RDr4OCEr34ktqhtYs95RNqEptQGh3tYifU49in9jZcbeMbwyXYGt4Lch9ff5A6/EXM16RELEO5GI+EQuYuSQlVYtbLHVxcEPL9+GEvlp/HzTWiyHxcu0ES/4tEua2vByqPf/bA4ozG7fMf5o5uKnKnxfNwAeJBYm1ck+iNR47teEXqMAI5OA6n4AUoQgXOwBny7wC7KYXi).

## Other builds of this spec

- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 751 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-3551000113013303-2135000301113002-7)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (7/31/13, 695 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0410011-32510301230133031-20350003-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

