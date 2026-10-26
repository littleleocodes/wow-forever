# Demonology Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Demonology

**✅ Recommended** for raid (the best warlock spec here, or within 3% of it).

**[Demonology — Raid](../research/raid/builds/demonology-ml-raid.md)** (2/31/18) — [open the talent tree](https://talentsforever.com/warlock/60/011-0025003031220301351-0550005003-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage), then summon your Succubus: Demonic Pact keeps the Imp's buff while another demon is out; **Soul Link**: turn it on with your demon out (it lasts while the demon lives).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Shadow Bolt**

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Demonology in a raid is a **Shadow Bolt** caster with two demons' worth of bonuses: you sacrifice the Imp for 15% more Shadow damage, and **Demonic Pact** keeps that buff while your Succubus fights. Then you keep **Curse of the Elements** and your dots up and cast **Shadow Bolt**.

**Why it works**

- Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours), then summon the Succubus and turn on **Soul Link**. **Demonic Pact** keeps the sacrifice while a different demon is out, but summoning the Imp again cancels it; the simulator measured about 10% less damage without the sacrifice.
- The Succubus earns her place: while she is out, **Master Demonologist** gives you and her 10% more Shadow damage, **Soul Link** 3% more damage and **Demonic Knowledge** 60 more spell damage at level 60. She takes 17% of your spell damage as attack power and 10% as spell damage, and her attacks and **Lash of Pain** add about 9% of your damage.
- **Curse of the Elements** goes up first: 10% more damage from every magic school for 5 minutes, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana: every tap is a global cooldown with no damage, and the simulator measured tapping at 5% about 0.5% better than at 10%.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (a 1.6-second cast with this build's single point of **Improved Corruption**) goes back up when less time is left on it than its cast, but not in the last 10 seconds.
- **Immolate** is Fire, so none of your Shadow bonuses reach it, and it only just pays: the simulator measured this spec better without it when it was recast to the very end, and better with it when you stop 20 seconds before the end. Start it when less than its 1.5-second cast is left on the old one.
- **Shadow Bolt** is the filler because every bonus you stacked is Shadow: the sacrificed Imp, **Master Demonologist** and **Improved Shadow Bolt**'s 20% after your own crits. **Decimation** adds 6% to it once the boss is below 35% health.

**Caveats**

- **Searing Pain** has no cooldown: the rotation casts it only in the last 3.5 seconds, when its 1.5-second cast lands before the boss dies and a **Shadow Bolt** might not. So **Demonic Brand** and the **Soul Fire** half of **Decimation** do nothing here: they are points on the way to deeper talents, and the simulator found **Soul Fire** a loss wherever it tried it.
- If the Succubus dies, summon her again unless the boss is about to die (6 seconds with **Master Summoner**) and turn **Soul Link** back on: without a demon you lose **Master Demonologist**, **Soul Link**, **Demonic Knowledge** and her own damage. Never summon the Imp during the fight: that cancels your sacrifice even with **Demonic Pact**.
- Summon her after your buffs, wizard oil and Spellstone (**Create Spellstone**) are on: in this project's model a demon copies its share of your spell damage when it is summoned. Forever lets the Spellstone stack with the oil, and the simulator measured about 3% more damage from it.
- On the move, **Bane of Agony**, **Curse of the Elements** and **Life Tap** are instant; **Corruption** keeps a 1.6-second cast in this build, so put it back when you stand still.

**When to change it**

- In the last 20 seconds start no new **Immolate**, and in the last 10 no **Corruption**: cast **Shadow Bolt**, then **Searing Pain** in the last 3.5 seconds.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 822 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, ElliotWood/Forever fork 2ce8265 (client 70291); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 801 | [2/31/18](https://talentsforever.com/warlock/60/011-0005203031220301351-0550005003-7) |
| Phase 1 BiS | 839 | [2/31/18](https://talentsforever.com/warlock/60/011-0005203031220301351-0550005003-7) (ties this build) |

**The gear** (average item level: Pre-BiS 62.4; Phase 1 BiS 63.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ghostweave Pants](https://www.wowhead.com/forever/item=14144) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Brilliant Watcher's Signet](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9II2cYxvN+M8l8ebU6fqU4TluYBpQ0MPLNhLHGS0ZPUnqQngoeamKiSbCZkOSgN4tCS2mV/qHFKFhapbXUIj0sspd1BSFeFk97WJEVF9llWdhlFzwuy0xGXNY97CXre/i+Z573fef9fTOHDz+gIIMCGkRhDHJQglmAbwF+B/gbgLV6WeJm+0FdC1NBDqtVDNHVonLagiI9+Q1QpA9/cdflAxlDdL+o3GtDie6ug3LYhgLdLaJITxcBQ3TH65Lo1r+gLEoo0jvrbuPCIxlFeu3AXX+8IaNEH/8HSv1dFOmzX92CjZX2iCnX89FbC8DP0iM//AHfAZnP/wTkLF2D4P3B1XX4B6S/VmBreCG/BX8WjmE+P9R6cTgbrpMINwydc26ZPM7jhuluRtwydG5Zrs15vE6EA9JyQpYl9qH6PnZE2vGd/wFRpDvfjDAiB9WQr02VY5T1YEesnYYY+TSgShhEwbAqniUykvatT6xuVUSiKCyuGm/Y08e71SAK8lmaiSoZCDRoGu89b4v3Wh7N3PfA5oBNpEpTXzqlqmZys0/nCd3sH9DGc6niZDajOWUtlclkM1p6RqvmslrZqaaqeaeoVbKp8nhOi1ayWS2T/copOlPO5IxeTuUz+nmR3ijqLVSc4sdqF8qxNip45wuhiMTyUOnGKIuoGnbG3qMikwqudXNUpTXiq8bG1l4lNbjOzaaQDiBnvdgV66QiowX3U93dAzVcI7689B94RfVTV4t5dIF5dBnT9DGP9oCVX0OZaAoldWfK8z+/9Zl08+lnDH19uAeK8IDU4QkxvxYCXiTsGkGkGKKCRmyIPCdh1w7MTthdtSU39pMfTXhxO2keE0XUkrFtEriSqNrnqqnRs9m0OQlv/XzNHvQNe8y9MZbAewgcJ2MC3e4ceuli4dAPNgzDCHwBOSjBNEyTFwMA/GRQiA==); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElUFII1cYx/O9mWRePq2OrxTHaQvTgJIGRt5MGGu8ZPQkpQfpqeChJiaaBJsJSQp6sxhoKa2C1oJRsLRKa6lFeijSUysIkULx1IuESou09LLLLniUZSbjuqx72EvW7/Def/7f9833ezOHh69RkEEBDaIwBTkowSLAJwBfAXwHwDq9LHGzw6Duhqkgh9UPMUS3i8pFB4r0ahVQpP9/4a6bpzKG6ElR+acLJXq0C8pZFwr0qIgivVgBlGhzHdw2iR78AMqKhCL9fR0erz+fyijS2ppbee9HUBovo0gffumm9ra6I6bcyEf/WAZ+mZ74/Gv4FEgtvwrkMl2H4L+j27vwPUjfbsHB+HL+AL4pnEMtP9Z5czobfiERbhg659wyeZzHDdPdjLhl6NyyXJvzeIMIp6Tjb7IpsdfVV7En0o0v/QSIIv314wlG5KAa8rWpcoyyAeyJddMQI28HVAmDKBhWxbNERtK+9ZbVr4pIFIXFVeM5e4Z4vxpEQb5MM1ElI4EWTeu9123xQcujWfoM2BKwmVRp7n2nVNVMbg7pPKGbwyPadC5VnM1mNKespTKZbEZLL2jVXFYrO9VUNe8UtUo2VZ7OadFKNqtlsh84RWfOmV3Qy6l8Rr8u0ltFg4WKU3xT7UM51kUF73whFJFYHirdm2QRVcPe2CtUZFLBtX6bVGmd+Kq1sZ2nSQ2uc7MtpCPI2SD2xXqpyGjB/VR/HYMarhNf3voPvKL6qbvFbN5gNm9jmj5m8xhY+RmUibZQUnemXFt74TPp/oN3GPr67BgU4T/SgPvE/EgIeJGw6wSRYogKGrEhckXCrh1YnLH76htunCTfmPHiz6R5ThRRS8YOSeBOompfq7bGwH7b5iS89d0de9Q37Cn3ytgA7yFwnowJ9LB37ImbhcMw2DAOE/Ae5KAE8zBPHg0A/9FQVw==).

## Other builds of this spec

- [Demonology — Demonic Pact](../research/raid/builds/demonology-pact-raid.md) (2/31/18, 816 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/101-0035003021220301351-0550005003-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)). Simulations, not in-game measurements. Do not hand-edit.*

