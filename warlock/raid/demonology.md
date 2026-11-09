# Demonology Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Demonology

**✅ Recommended** for raid (the best warlock spec here, or within 3% of it).

**[Demonology — Raid](../research/raid/builds/demonology-ml-raid.md)** (2/31/18) — [open the talent tree](https://talentsforever.com/warlock/60/011-0025003031220301351-0550005003-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Setup, before the pull:** **Summon Succubus** and keep it out all fight. Keep **Demon Armor** on you.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 857 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 820 | this build |
| Phase 1 BiS | 856 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 60.8; Phase 1 BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Coronal](https://www.wowhead.com/forever/item=17578) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Field Marshal's Coronal](https://www.wowhead.com/forever/item=17578) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Fel Cape](https://www.wowhead.com/forever/item=279269) · *Tailoring* |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Marshal's Dreadweave Leggings](https://www.wowhead.com/forever/item=17579) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Marshal's Dreadweave Leggings](https://www.wowhead.com/forever/item=17579) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Marshal's Dreadweave Boots](https://www.wowhead.com/forever/item=17583) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Marshal's Dreadweave Boots](https://www.wowhead.com/forever/item=17583) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) · *sold by Gaelden Hammersmith* | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) · *sold by Gaelden Hammersmith* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElUFII2cUx/O+mWS+PFszfqU4TluYBpQ0MPLNhLHGS0ZPUnqQngoeamKiSbCZkISiN4tCa2m1tKXFKLRYpdUilR5a6akVhHgRTz1UZMVFdln2sOyCt12WmYzssu5hL1nf4eWf/3tv3u+bOXz4JgUZFNAgBmOQhzLMAnwO8BPArwDsFa9K3Go/qGthKshh9ROU6NYCKOdtKNKzHwBFeuc7Nx9+DRiiByXlZjtKdG8DlON2FOheCUV6vgQo0d+aYxL9fQGUJQlF+v+GO7l4V0aR/nnk5oerEZToyl+gNF5DkT743m3YXI1ETblRiB0uAr/IjHy1Bl8AmS98A+QiU4fgrcEfN2ALpF9WYWd4sbADPxdPYb4wRL0DgA1/kyg3DJ1z0+I8wROGafIENxKWoXPL4py7doMIR6TtjKxI7C31DeyIRvDVPwBRpP98NsKIHFRDvjZVjjHWgx3xCA0x8l5AlTCIgmFVPUtkJONb71rdqohEUVhCNV5wpo93q0EU5IsME1UyEGjSNJ97OZbotTyauS+BzQGbSJenPnLKNc3kZp/Ok7rZP6CN59OlyVxWcypaOpvNZbXMjFbL57SKU0vXCk5Jq+bSlfG8Fqvmclo297FTcqacyRm9ki5k9csmvdnUW6w6pXfULpTj7VTwzhdCEYnlodLNURZVNeyMv05FJhVd699RldaJr5o/bP1ZUoPr3GwJ6QBy1otd8U4qMlp0X9WNfVDDdeLLK9+BV1W/dL2YJ08wT65imj7myT6wynMoky2hpO5Oef7bl76Tbt9/n6Gvj/dBEW6TBtwj5qdCwIukXSeIFENU0IgN0Uck7NqB2Qm7q77sxkHq7Qkv/kuZp0QRtVR8lwSuJWr2pWpp9Gy3bE/Syx+s24O+YY+598UyeH8Cp6m4QHc7h566Vjj0gw3DMAIfQh7KMA3T5PEAFS9QJw==); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElUFIFG0Yx/d5Z3bn3dfv0/H9+HCcCqYFZVsYeXeWMdfLjp4kOkinwEPuuqu7i+0su0vozXCjjFLQClyFwpTSkKRDSacShJUgPHURSQopOkWBR4mZHSuyQ5fN5/DMf/7P+8zze+c9vOQ4BhEkUMAPvZCELIwAXAO4B/AQgP5jV5FVbQN5zos50StfIgJeGgNpt4bweH8SCI8/3bLy7pV64sEbGel9LRHw2gJIW7WEw2sZqzYBRMCPKm0CfjwG0oRAePzqNnzPxSkrP90UiYBnnoFU/o/w+Osdy1ycrfNpYjnlfz0ObC/WfXMOrgMqpiYB7cVK4P7QcXcBlkB4MAsrXeOpFbif3oFiqhPbGwADniMfY5rKmKYzFmKhoKaxEAuG9KDKdJ0xZtllxG2imndoRqAn5GOk3ldH/n0ChPD4xdVuikS37HG0JjPip82kPlCHPRSdcckCcRMuqOdti6co5lin9SaZJ0iSaEgO/mFPK2uS3YQT92KUl1G7q0JT+e5BW6hFt2lGbwAdBdofzQ5eMLMFRWNaq8rCqtbWrvQlo5mBRFwxc0o0Hk/EldiwUkgmlJxZiBZSZkbJJ6K5vqTizycSSjxx0cyYg+bAsJqLpuLqwSK1sqglnTczp+RGIgZqMWfvz0N4gnQbFS/2UJ+skIbA/5inQtqyXvbIuIQcVXnQ+V9Jg0xlWlVI2wmjLaQx0IB5itPWr3q7DrK3hBx56BxYXnZKR4u5/QNz+zCm5mBurwPN/YYyXBVKbM0Ui1N/fSZe/nKWEkdvrYPEfURl+Iy0y5zLjrBRQoRg4sGcggzw7SOvZbtG+o3G0rQVG5GT/Xa8iWg7SOKVSGAVuY4kCsaBqmo0L1dtTtjO5+aNDscweq37YhrsF9dOJMDh1YbOn64VBm1gQBd0w3lIQhaGYAh9GwBRkE+C).

## Other builds of this spec

- [Demonology — Demonic Pact](../research/raid/builds/demonology-pact-raid.md) (2/31/18, 852 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/101-0035003021220301351-0550005003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-09 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

