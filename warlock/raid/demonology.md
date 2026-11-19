# Demonology Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Demonology

**✅ Recommended** for raid (the best warlock spec here, or within 3% of it).

**[Demonology — Raid](../research/raid/builds/demonology-ml-raid.md)** (2/31/18) — [open the talent tree](https://talentsforever.com/warlock/60/011-0025003031220301351-0550005003-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 850 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 749 | this build |
| Pre-BiS | 830 | this build |
| Raid BiS | 852 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 60.8; Pre-BiS 62.4; Raid BiS 64.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Shroud of the Nathrezim](https://www.wowhead.com/forever/item=18720) · *Balnazzar, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Amplifying Cloak](https://www.wowhead.com/forever/item=18350) · *Magister Kalendris, Dire Maul* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Highlander's Cloth Girdle](https://www.wowhead.com/forever/item=20047) · *sold by Samuel Hawke* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Leggings of Torment](https://www.wowhead.com/forever/item=22342) · *Lord Valthalak, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Don Mauricio's Band of Domination](https://www.wowhead.com/forever/item=22433) · *Darkmaster Gandling, Scholomance* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18467) · *quest: Harnessing Shadows* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Witchblade](https://www.wowhead.com/forever/item=13964) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Skul's Ghastly Touch](https://www.wowhead.com/forever/item=13396) · *Skul, Stratholme* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9II1ccx/N7M8m8/Gw1vlIcxxamASUNjLyZMGq8ZPQkpQfpqWBLTUxiEjQTkhz0ZtHSUqyKPRmE2mqxLfiHnqSneghkL/sHlr2IrOyy7B4XDx53l5lM2GXdw16C38Ob73zf7zfvM28GHn5CIQQyqBCBachBCZYAfgLYAfgLgH3gzhJndgSU4yAVQkGlhBLd3wT5SQeKdPkIUKQ7m854uA4o0XvrID/uRImeboB81okCrc+iSO9sAwboZdZpC9DDb+R1CUX6+xGgQF8mUaAb8yjS3Q2nanVebnyEAl36FgV6Pxc2Qo185PYa8KvU5C9/wM9AVvKbQK5SNfA/HfvtT/gHpP1tOJ5Yyx/DbuECVvLj1EUHC/4jYa7rGueGyXmMx3TD4DGux0xd46bJOXfiBhHuko5H5Ehinyp92B3uwg//BUSR/v/jJCMhvxLwvKFwjLAB7I520QAjX/gUCf0o6GbFjURGUl40bPYrIhJZZjFFf8+eId6v+FEIXaWYqJBRX5Om+dxWW2zQdGmWV4EtA8smS3Pf2aWqanBjSONxzRgZVWdyyeJsJq3aZTWZTmfSampRreYyatmuJqt5u6hWMsnyTE6NVDIZNZ2Zt4v2nD27qJWT+bTWKtKaRYOFil38XOnFULSTCu77BVBEYrqo9O8pFlZU7Il+TEUmFZzodEqhNeK55oXtvU2qc40bbSEdRc4GsTfaQ0VGC85WPayDEqwRz177DryieFM3i3n+GvP8OqbhYZ7Xgf1wDVPX+HBbMPtaHK1/1DD7HY7Qyq/Ayu/YrXhbMKizJj24/JKh58/qIAvPSAOeE+N7wecqbtUIIsUAFVRiQfgFCTqxbylr9da2HN1KfJZ19SBhXBBZVBPRE+K7EVWtlmurBg7atk7cHb/as8a8wJp2To8tcG98F4moQE96xt84ZDiMgAUTMAlfQw5KsAAL5NUAIvVOzA==); Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9II1ccx/N7M8m8/Gx1fKU4ji1MA0oaGHkzYdR4yehJSg/SU8FCTUw0CZoJSQ56s2hpKValLQXTQktr6R/wDy0U6akWLPGy5LQXkZVdZJdlYRcPXhaWZSYTdln3sJfg9/DmO9/f+837zJuBh29RkEEBDaIwDTkowTLA5wA/AvwGwF7zqsStjoD6V5gKclitoEQf74By3oEiXdkDFOn9b9zxu4aMIXpcVO50okQPN0E56USB/ldEkZ5vAEr0/12vLUR3P1I2JBTp+gMZRfptwx3/bsgo0M0FlOjDXVDqb6BI1zYABXoxHzHlej56Yx34ZXryy5/gCyCr+a+AXKZrELw79sMv8AdIv34P+xPr+X34uXAGq/lx6tGDDf+QCDcMnXPT4jzO44Zp8jg34pahc8vinLtxnQgN0nGb7EnsbbUPuyNd+PqfgCjSfz+bZEQOqiHfmyrHKBvA7lgXDTHyXkCVMIiCYVW8SGQk7UfDVr8qIlEUFleNV+wZ4v1qEAX5Ms1ElYwGmjTN57ba4oOWR7OyBmwF2GyqNP+xU6pqJjeHdJ7QzZFRbSaXKs5lM5pT1lKZTDajpZe0ai6rlZ1qqpp3ilolmyrP5LRoJZvVMtkFp+jMO3NLejmVz+itSXpz0mCh4hTfVXtRjnVSwXu/EIpILA+V/j7FIqqGPbE3qcikghsdTqm0RnzXvLDtF0kNrnOzLaSjyNkg9sZ6qMhowd2qW0eghmvEt1e+A6+oful6MU+fYZ5exTR9zNMjYJ9ewTR0PtwWzL4WR+sfNa1+l0Ne/RpY+SW7lWgLBnXXpDsX7zP0/ckRKMI9UodHxPxECHhK2DWCSDFEBY3YEHlCwm4cWJ61e2tbro6T78x6upk0z4giasnYAQlci6p2y7VVAzttWyfhjR9s22N+YE+7B8gWeDeBs2RMoAc948+dMxxGwIYJmIQPIQclWIRF8nQAA3FRhA==); Raid BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9IK1cUxnPuTDI3x1bHW4rj2MI0oKSBkTsTRo2bjK6kdCFdFSzUxESTYDMhyUJ3FlNaitWidWFaaGkt/QNaKaVIV7UgRArFVTcSKi3Sx9u8hws3D+Qxk8l7j+dbvE3wLM58851z5v7mzsDFVyjIoIAGUZiFHJRgBeAjgK8AvgdgL3hV4lbHQP0lTAU5rFZRog/2QLnoQpFebwKK9O5nbv78VMYQPSkq/3WjRI8+BeWsGwX6RxFFerEBKNHmtjcWovvvKBsSivTPbXiUfz2VUaS1Lbfx3j4ojZdQpGsbgAK9XIyYciMf/Wsd+FV6+pOv4WMgtfwmkKt0HYL/T3z5LfwI0ndfwMHUev4AvimcQy0/ST18sOE3EuGGoXNuWpzHedwwTR7nRtwydG5ZnHPXbhDhlHT9S36S2KvqAPZGevDFnwFRpL9/OM2IHFRDvjZVjlE2hL2xHhpi5I2AKmEQBcOqeJbISNq3Rq1BVUSiKCyuGs85M8IH1SAK8lWaiSoZD7RoWs9tj8WHLY9mdQ3YKrD5VGnxXadU1Uxujug8oZtj49pcLlVcyGY0p6ylMplsRksva9VcVis71VQ17xS1SjZVnstp0Uo2q2Wy7zlFZ9FZWNbLqXxGbzfprabhQsUpvq72oxzrpoL3fiEUkVgeKv1hhkVUDftiL1ORSQXXOppRaZ34qnVhu0+TGlznZkdIx5GzYeyP9VGR0YK7Vf8cgxquE1/e+A68ovql28VsPsZs3sQ0fczmMbAPbmAaOh/tCOZAm6P9j5rWoMsh17aAlZ+xW4mOYFB3Tbp3+SZDX58dgyLcIQ24T8z3hYAXCbtOECmGqKARGyLXJOzagZV5u7++48ZJ8rV5L/5OmudEEbVk7JAEbiWqdlt1NIb2OrZOwstv7doTvmHPuifIDng3gfNkTKCHfZNPHDQcxsCGKZiGtyEHJViCJfJwAKRPUcA=).

## Other builds of this spec

- [Demonology — Demonic Pact](../research/raid/builds/demonology-pact-raid.md) (2/31/18, 845 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/101-0035003021220301351-0550005003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

