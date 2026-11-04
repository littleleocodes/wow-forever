# Elemental-Enhancement Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Elemental-Enhancement

*A melee shaman: Enhancement's Stormstrike and Flurry with Elemental's shock and Fire Nova talents.* (a hybrid: Elemental/Enhancement).

**[Elemental-Enhancement — Raid](../research/raid/builds/elemental-enhancement-ml-raid.md)** (17/29/5) — [open the talent tree](https://talentsforever.com/shaman/60/503303102-05303031005100224-05-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Strength of Earth Totem**, **Grace of Air Totem**, **Searing Totem**.

**Keep up all fight:** **Strength of Earth Totem**, **Grace of Air Totem**, **Magma Totem**, **Searing Totem**.

**Then press the first one that is ready**, top to bottom:

1. **Flame Shock**: keep it on the target, until the last 10 seconds of the fight
2. **Stormstrike**
3. **Lightning Bolt** when Maelstrom Weapon has 5 or more stacks
4. **Earth Shock**
5. **Fire Nova** when you have at least 10% mana
6. **Rockbiter Weapon**

**Rockbiter Weapon** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

This hybrid is a melee shaman: Enhancement's **Stormstrike** and **Flurry** with Elemental's shock and **Fire Nova** talents. It plays the Enhancement raid list without its **Maelstrom Weapon** bolt: **Stormstrike**, **Flame Shock**, **Earth Shock** and **Fire Nova** between your swings, which with **Windfury Weapon** do about half the damage.

**Why it works**

- Before the pull, drop **Strength of Earth Totem**, **Grace of Air Totem** and **Searing Totem**; the first two last 5 minutes, so one cast covers the fight.
- **Stormstrike** first: 125 mana, a weapon hit and 20% more on your next **Earth Shock**; with **Improved Stormstrike** each one keeps half your mana regeneration going while you cast for 15 seconds.
- **Flame Shock** whenever the burn is off the target, **Earth Shock** on every other free shock. Your Elemental points shape them: 3 points in **Reverberation** bring the shared cooldown to 5.4 seconds, **Convection** and **Shamanistic Focus** cut their cost, and **Call of Flame** adds 15% to **Flame Shock**, **Fire Nova** and **Searing Totem**.
- **Fire Nova** last: it erupts around your Fire totem, so keep **Searing Totem** within 10 yards of the boss and replace it when it expires. **Trial by Fire** makes it 20% stronger on a 6-second cooldown; adding Fire Nova to this list measured about 7% more damage in the rotation search.
- **Elemental Devastation** turns every spell crit into 9% more melee crit chance for 10 seconds, which feeds **Flurry**: another reason to keep a shock going between swings.
- Put **Windfury Weapon** on your weapon with a sharpening stone on top: in Forever an imbue and a stone stack.

**Caveats**

- No **Maelstrom Weapon** and no **Rage of the Farseer** (26 Enhancement points): the list's **Lightning Bolt** line never fires for this build. Use your trinkets and potion at the pull.
- Mana: **Improved Stormstrike**, **Mindfulness** and **Totemic Focus** pay for the shocks; with only your own buffs the simulator's build is out of mana for about 12 seconds of a 3-minute fight. Use a mana potion when low, and do not hold shocks back.
- Several targets: **Fire Nova** hits every enemy within 10 yards of your Fire totem.
- For a **Lightning Bolt** caster, play Elemental: this split is a melee build.

**When to change it**

- In the last 10 seconds, skip **Flame Shock** (its burn would not finish) and use **Earth Shock**.
- In a party of warriors and rogues, ask whether they want **Windfury Totem** instead of **Grace of Air Totem**: a party gets only one, and it does nothing for you while you use **Windfury Weapon**.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 893 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 726 | this build |
| Phase 1 BiS | 755 | [17/29/5](https://talentsforever.com/shaman/60/053303102-05303031005100224-05-7) (ties this build) |

**The gear** (average item level: Pre-BiS 65.8; Phase 1 BiS 65.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) · *quest: Falrin's Vendetta* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Warlord's Mail Spaulders](https://www.wowhead.com/forever/item=16580) · *sold by Lady Palanseer* | [Warlord's Mail Spaulders](https://www.wowhead.com/forever/item=16580) · *sold by Lady Palanseer* |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear* | [Sergeant Major's Cape](https://www.wowhead.com/forever/item=16337) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009) · *quest: Saving the Best for Last*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Onyxia Scale Breastplate](https://www.wowhead.com/forever/item=15141) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [General's Mail Gauntlets](https://www.wowhead.com/forever/item=16574) · *sold by Lady Palanseer*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [General's Mail Gauntlets](https://www.wowhead.com/forever/item=16574) · *sold by Lady Palanseer*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) · *quest: A Collection of Heads* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673) · *sold by Kelm Hargunth*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Premier Centurion's Mail Boots](https://www.wowhead.com/forever/item=273336)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Premier Centurion's Mail Boots](https://www.wowhead.com/forever/item=273336)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) · *sold by Gaelden Hammersmith* | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) · *quest: The Qiraji Conqueror* | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) · *sold by Gaelden Hammersmith* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Grand Marshal's Demolisher](https://www.wowhead.com/forever/item=23455) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Demolisher](https://www.wowhead.com/forever/item=23455) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzEVU1MK1UU7rkz7dweCZQLxHFEHUowWJ3mzrQlhU0LK+MKWLGTgQ62/rQN0yiugATREIWwwUA0mCjRKJi4IKJBTdA0uGOhmECMBDVh4UKNUXzJe3m50/aFB29b3lmcnHvOd3O/c86XXGynEAIVdOiGUchCEWYA3gB4D+AjANbgVYmoJkH7K0gDIUV7BRX61XaTevoAynR+C1Cm380K/+0GoEL//wTUXxtRoXsboP4sgq9nQV1XUKbn7wrA8mcg7ip056eQ+ksjyvTmirj+44bw2wchlOnyNyFU6PrnoP7RiD6U6fo2hJ8M7ee6/35h8HARRv4ZXQAyl1uDwPv2pn3U/zEE38x9+A78bi7mTmAuN0A96pCGL8mjCR6L8ZjJLYMnYjzGRcwTJresuMET+wQOiHRKzhVsQ6oFxPNlCAdRQb8RjyZcbKmml8oQVtCPkhFzsRUVzY8SLQ9VoWY04bK3gU3YxRefLRRLusWtHoP3GlayTx/P2vnnnIxemNTtTMbJ6GOv6qWso08WSnYpV8jrrmNPjmf1btdxdCeftfPjzktOvmRkiq5RAxkVUPR5t5B/QjOwk3VgQxiRWoL05m+AzZEmGmDkGZ/m8TS5q1VL7DHtEWyJNFOZ+RckQkEUkFQBy+UrAHIXYKkMTNZIn4+hVhnGD68DW7ncrckNq6cu3T5V6fYoEESJHg8zEpJr3Y5Vu7USXd5GjofZW/cgxnvrQqwTtYhKAyy4B2IsX/ynap4e4lHLTHp8zl5m89cni/aLS5TuLFEQKQ+xoFZR7adD7LUrMzINHq8Lp4cvr8rkXYIZXf1XZdPXpqG2mn52p4V+vEHsTqvSGdmHP4k1K/k8a03fgIAmI6EQvkWCIuWbmUg/tLYq7PtUx4RnhynrhKiynorsEN99sVK6FtXVHt+q2zu9nh/+IN1fTaRHxfezCt7Bd5KKSHTnwYELvxSHJKThaRiEEchCEaZgitweAKKScEE=); Phase 1 BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzEVV9ILGUU3/PN7My3J9H1U2marMYVw7Zm+WZ2V1ZfdvUpelKffMvRHdvtz+7ibGJPq6AVUi4iGEpgUFKE9ZRkYT1ILPZmEAZKJKbgQ1BEVARdLjO7e/HqfV3vefg4c85vZn6/c37wYSeFICigQS+MQwYKMAfwNsAHAJ8AsCavS9xuAtTfA1QKyurrKNNvdlqUs0dQpOdlQJF+Nw8o0B9KKNGtGeXXZpTp/hYoP7vJt/OgbMoo0osyoEwrX3hvynT3p6DySzOKdHHV/cT/a+65cxhEkS6susjNL0H5rRl9KNLNHQg9GzzI9v75yvDRMoz9Nb4EZCG7AdKH1rZ1PPgpBN7Jfvw+XBjL2VNYyA5Rjzik4GvyJI9HozxqcFPn8SiPcjfncYObZkzn8QMCh0Q4I//K2IFUlVCkKxUIBVBGvx6LxB1sq5XLFQjJ6EdBjzrYjrLqR4FWRmpQIxJ32HvApqzCqy/mC0XN5Gafzvt1MzGgTWas3Et2WstPa1Y6bae1iTe0YsbWpvNFq5jN5zTHtqYnM1qvY9uanctYuUn7NTtX1NMFR6+D9Coo8rKTzz2j6tjNurAphEhNl/T2OWBruIVKjLzgUz2eBnfUWos9pT6BbeFWKjL/kkAouA0kNcBK5QaA3AcoV4CJKhnwMVSrw/jxLWBr19UaXDf7GqL2uaraYymAAj0ZZSQo1tVO1NSa8R5vIyej7N0HEOP9DSHWjWpYoRIL7IM7lq/+UVTPD7GIaSQ8Ppcz7M3bs0Xn1SUK95boEqmMsIBade3nI2zxxowMnccawunx66syeI/LjK7/rbDSrXmoo+6fvZLrH28QeyVFuCQH8Acx5wWfF+2p/0BSRSQUQndIwC355qZSj22su/F9smvKi6OkeUoUUUuGd4nvoUQxVc8aGk9/1rD/9Hvn6EepwVohNe5ePuvgPfhOk2GB7j46dOWO4pCAFDwPwzAGGSjALMySuwMAq4lvUw==).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 7c3453f (client 1.60.1.70755)). Simulations, not in-game measurements. Do not hand-edit.*

