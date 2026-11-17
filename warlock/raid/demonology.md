# Demonology Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Demonology

**✅ Recommended** for raid (the best warlock spec here, or within 3% of it).

**[Demonology — Raid](../research/raid/builds/demonology-ml-raid.md)** (2/31/18) — [open the talent tree](https://talentsforever.com/warlock/60/011-0025003031220301351-0550005003-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Setup, before the pull:** **Summon Succubus** and keep it out all fight. Keep **Demon Armor** on you.

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage), then summon your Succubus: Demonic Pact keeps the Imp's buff while another demon is out; **Soul Link**: turn it on with your demon out (it lasts while the demon lives).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Shadow Bolt** (rank 9)

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours, worth about 10% of your damage in the simulator), then summon the Succubus and turn on **Soul Link**. **Demonic Pact** keeps the sacrifice while she fights. In the fight keep **Curse of the Elements** and your dots up and cast **Shadow Bolt**.

**Why it works**

- Put your buffs, wizard oil and Spellstone (**Create Spellstone**) on first: in this project's model a demon copies its share of your spell damage when it is summoned. Then **Summon Imp**, **Demonic Sacrifice**, **Summon Succubus** (6 seconds with **Master Summoner**) and **Soul Link**. **Demonic Pact** keeps the sacrifice while a different demon is out, but summoning the Imp again cancels it.
- The Succubus earns her place: while she is out, **Master Demonologist** gives you and her 10% more Shadow damage, **Soul Link** 3% more damage and **Demonic Knowledge** 60 more spell damage at level 60. She takes 17% of your spell damage as attack power and 10% as spell damage, and her attacks and **Lash of Pain** add to your total.
- **Curse of the Elements** goes up first: 10% more damage from every magic school for 5 minutes, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana: every tap is a global cooldown with no damage, and the simulator measured tapping at 5% better than at 10%.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (a 1.6-second cast with this build's single point of **Improved Corruption**) goes back up when less time is left on it than its cast, but not in the last 10 seconds.
- **Immolate** is Fire, so the sacrifice and your other Shadow bonuses do not reach it, and it only just pays: the simulator measured this spec better without it when it was recast to the very end, and better with it when you stop 20 seconds before the end. Start it when less than its 1.5-second cast is left on the old one.
- **Shadow Bolt** is the filler because every bonus you stacked is Shadow: the sacrificed Imp, **Master Demonologist** and **Improved Shadow Bolt**'s 20% after your own crits. **Decimation** adds 6% to it once the boss is below 35% health.

**Caveats**

- **Searing Pain** has no cooldown: the rotation casts it only in the last 3.5 seconds, when its 1.5-second cast lands before the boss dies and a **Shadow Bolt** might not. So **Demonic Brand** and the **Soul Fire** half of **Decimation** do nothing here: they are points on the way to deeper talents, and the simulator found **Soul Fire** a loss wherever it tried it.
- If the Succubus dies, summon her again unless the boss is about to die and turn **Soul Link** back on: without a demon you lose **Master Demonologist**, **Soul Link**, **Demonic Knowledge** and her own damage. Never summon the Imp during the fight: that cancels your sacrifice even with **Demonic Pact**.
- Forever lets the Spellstone stack with the oil, and the simulator measured about 3% more damage from it.
- On the move, **Bane of Agony**, **Curse of the Elements** and **Life Tap** are instant; **Corruption** keeps a 1.6-second cast in this build, so put it back when you stand still.

**When to change it**

- In the last 20 seconds start no new **Immolate**, and in the last 10 no **Corruption**: cast **Shadow Bolt**, then **Searing Pain** in the last 3.5 seconds.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Affliction | 2 | Suppression 1, Improved Corruption 1 |
| Demonology | 31 | Demonic Embrace 2, Unholy Power 5, Fel Vitality 3, Improved Sayaad 3, Demonic Sacrifice 1, Master Summoner 2, Decimation 2, Demonic Brand 3, Soul Link 1, Demonic Knowledge 3, Master Demonologist 5, Demonic Pact 1 |
| Destruction | 18 | Improved Shadow Bolt 5, Bane 5, Ruin 5, Agonizing Flames 3 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 867 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 845 | this build |
| Phase 1 BiS | 867 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.5; Phase 1 BiS 64.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Leggings of Torment](https://www.wowhead.com/forever/item=22342) · *Lord Valthalak, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9II1ccx/N7M8m8/Gx1fKU4ji1MA0oaGHkzYdR4yehJSg/SU8FCTUw0CZoJSQ56s2hpKVZL24tpof+U/gH/0EKRnrqCS9zD4mkvIiu7yC7Lwi4evCwsy0wm7LLuYS/B7+HNd76/95v3mTcDD9+hIIMCGkRhEnJQgkWALwF+BvgDgL3hVYlbHQL1nzAV5LBaQYk+2QLlrA1FurQDKNIH37vjD0cyhuhhUbnbjhLd3wTluB0Ful9EkZ6tAUr0+rbXFqLbnyhrEop09aGMIr3xC6BAv5lDkf57JKNEH22DUn8LRbqy5lbOZyOmXM9Hb64Cv0iPf/0rfAVkOf8tkIt0DYL3Rn7ahL9A+v1H2B1bze/Cb4VTWM6PUo8ebPiPRLhh6JybFudxHjdMk8e5EbcMnVsW59yN60Q4Im13yI7E3lV7sDPSgW/+DYgi/f+LcUbkoBryvalyjLI+7Ix10BAjHwRUCYMoGFbFi0RG0n40aPWqIhJFYXHVeM2eAd6rBlGQL9JMVMlwoEHTeG6zLd5veTRLK8CWgE2nSrOfOqWqZnJzQOcJ3Rwa1qZyqeJMNqM5ZS2VyWQzWnpBq+ayWtmppqp5p6hVsqnyVE6LVrJZLZOdc4rOrDOzoJdT+YzenKQ3JvUXKk7xfbUb5Vg7Fbz3C6GIxPJQ6Z8TLKJq2BV7m4pMKrjRtQmV1ojvGhe28TKpwXVutoR0GDnrx+5YFxUZLbhbdfsA1HCN+PbSd+AV1S9dLebJc8yTy5imj3lyAOzzS5iGzgdbgtnT5Gj+o6bV63LIy98BK79itxItwaDumnTr/EOGvj8+AEW4T+rwmJifCQFPCbtGECmGqKARGyJPSdiNA4vTdndt3dVh8r1pT7eS5ilRRC0Z2yOBK1HVbrqWqm+rZeskvPGjDXvED+xJ9wBZB+8mcJqMCXSva/SFc4bDENgwBuPwMeSgBPMwT54NAE2DUZA=); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9IK1cUxnPuTDI3x1bHW4rj2MI0oKSBkTsTRo2bjK6kdCFdFSzUxESTYDMhyUJ3FlNailXQujAttLRK/4BWSinSVSsIkUJx1Y2ESou0dPMeLtw8kMdMJu89nm/xNsGzOPPNd86Z+5s7AxdfoSCDAhpEYRZyUIIVgI8AvgT4FoC94FWJWx0D9acwFeSwWkWJPtgH5bILRXqzCSjS/z9182dnMoboaVH5pxslerwHynk3CvS4iCK93ACUaHPbGwvRg3eUDQlF+vs2PMo/n8ko0tqW23jvAJTGSyjStQ1AgV4tRky5kY/+sQ78Oj39yVfwMZBafhPIdboOwX8nvtiD70H65nM4nFrPH8LXhQuo5Sephw82/EIi3DB0zk2L8ziPG6bJ49yIW4bOLYtz7toNIpyRrr/JDxJ7VR3A3kgPvvgjIIr01w+nGZGDasjXpsoxyoawN9ZDQ4y8EVAlDKJgWBXPEhlJ+9aoNaiKSBSFxVXjOWdG+KAaREG+TjNRJeOBFk3rue2x+LDl0ayuAVsFNp8qLb7rlKqayc0RnSd0c2xcm8uligvZjOaUtVQmk81o6WWtmstqZaeaquadolbJpspzOS1ayWa1TPY9p+gsOgvLejmVz+jtJr3VNFyoOMXX1X6UY91U8N4vhCISy0Ol382wiKphX+xlKjKp4Fq/zai0TnzVurDdp0kNrnOzI6TjyNkw9sf6qMhowd2qv05ADdeJL299B15R/dLdYjYfYzZvY5o+ZvME2Ae3MA2dj3YEc6DN0f5HTWvQ5ZBrW8DKz9itREcwqLsm3b96k6Gvz09AEf4jDbhPzPeFgBcJu04QKYaooBEbIjck7NqBlXm7v77jxmnytXkv/kyaF0QRtWTsiATuJKp2W3U0hvY7tk7Cy2/t2hO+Yc+6J8gOeDeBi2RMoEd9k08cNBzGwIYpmIa3IQclWIIl8nAALD1R1g==).

## Other builds of this spec

- [Demonology — Demonic Pact](../research/raid/builds/demonology-pact-raid.md) (2/31/18, 862 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/101-0035003021220301351-0550005003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-17 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

