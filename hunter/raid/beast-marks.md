# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Marksmanship's shots (Trueshot Aura, Barrage, Sniper Shot) with a few Beast Mastery points: the classic raid hunter split.* (a hybrid: Beast Mastery/Marksmanship).

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Beast-Marks — Raid](../research/raid/builds/beast-marks-ml-raid.md)** (28/21/2) — [open the talent tree](https://talentsforever.com/hunter/60/532000150510123-00530503005-2-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Marksmanship — Summon Hawk), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** The spec's best build for each other setup, in a full raid:

- With a pet: [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 719 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--7)

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target
2. **Arcane Shot**
3. **Rapid Fire**
4. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast-Marks puts Beast Mastery's pet talents on a Marksmanship shot core and plays the same short list as Beast Mastery: keep **Serpent Sting** up, fire **Arcane Shot** and **Aimed Shot** each time they are ready, and let **Auto Shot** and the pet do the rest.

**Why it works**

- **Serpent Sting** first so it never drops, 20% stronger with **Improved Stings**. Recast it only as it runs out (a new sting replaces the old one), and the full rotation does so only while you have 30% mana or more.
- **Arcane Shot** every time it is ready: 3 points in **Improved Arcane Shot** bring its cooldown to 5.1 seconds, about 34 casts in a 3-minute fight. **Summon Hawk** would share that timer, and in a full raid the simulator measured **Arcane Shot** as the better use of it, so this build skips the hawk.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown.
- **Aimed Shot** is listed last but goes out almost every time it can: a 2-second cast, then its 6-second cooldown. The simulator measured it slightly better below the instants; **Multi-Shot** shares its cooldown and never comes up on one target.
- The pet half: **Unleashed Fury** (+15% pet damage), **Ferocity** (+10% pet crit on top of your own crit, which Forever pets inherit), **Frenzy** (2 points) and **Focused Fire** (+2% to you and the pet while it is out). There is no **Bestial Wrath** here, so there is nothing to time but **Rapid Fire**, trinkets and a potion.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator drops **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** goes first when you run low.
- Keep the pet alive with **Mend Pet**: it is about a quarter of your damage and takes no stat buffs from players in Forever. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; measured by players only at levels 20 and 30).
- Track the boss's creature type: **Improved Tracking** (3 points here) counts only against the tracked type.
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant. The simulator starts **Aimed Shot** 2.5 seconds before the pull; in a real raid, wait for your tank.
- Watch your ranks: in the beta client (build 70425) **Hunter's Mark** rank 4 gives +71 ranged attack power against rank 3's +98, and **Trueshot Aura** rank 5 +50 against rank 4's +75 (if your build has it); cast the stronger lower rank from your spellbook until Blizzard fixes the numbers. **Aspect of the Hawk** rank 7 (+120) is the best at 60. The simulator's numbers use **Hunter's Mark** rank 4, so they read about 0.3% low (estimate).

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown (up to 3 targets for weapon damage each, against 166 extra on one). For a pack, **Volley**: a 6-second channel with no cooldown in Forever.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds.
- Inside 8 yards your shots and **Auto Shot** stop: step back out at once; the pet keeps attacking meanwhile.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 763 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 799 | [28/20/3](https://talentsforever.com/hunter/60/532000151500123-00520503005-3-7) |
| Phase 1 BiS | 798 | this build |

**The gear** (average item level: Pre-BiS 66.2; Phase 1 BiS 67.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Chain Helm](https://www.wowhead.com/forever/item=16465)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Field Marshal's Chain Helm](https://www.wowhead.com/forever/item=16465)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Field Marshal's Chain Breastplate](https://www.wowhead.com/forever/item=16466)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Field Marshal's Chain Breastplate](https://www.wowhead.com/forever/item=16466)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Marshal's Chain Bracers](https://www.wowhead.com/forever/item=16461)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Marshal's Chain Bracers](https://www.wowhead.com/forever/item=16461)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Marshal's Chain Grips](https://www.wowhead.com/forever/item=16463)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Marshal's Chain Grips](https://www.wowhead.com/forever/item=16463)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marshal's Chain Girdle](https://www.wowhead.com/forever/item=16464) | [Molten Belt](https://www.wowhead.com/forever/item=19163) · *Leatherworking* |
| Legs | [Marshal's Chain Legguards](https://www.wowhead.com/forever/item=16467)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Marshal's Chain Legguards](https://www.wowhead.com/forever/item=16467)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Marshal's Chain Boots](https://www.wowhead.com/forever/item=16462)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Marshal's Chain Boots](https://www.wowhead.com/forever/item=16462)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Trinket | [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Main hand | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Grand Marshal's Bullseye](https://www.wowhead.com/forever/item=18833)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIFG0Y3veb2Z1v3/9Pt09tx6Fi2kDWhVm+mW1EjdjVU6eQTp3K0V3bkXKX3T3oIZjAIESiiCIlMNgkkYKO0iUwBINqNamgjMQMOnTwFgVFzLgLkR2VnsPLO8/DfM/zzny8uJ9CCGRQIQq9kIU8OACXAe4AzACw/z2VuGo7KOsSpSFBuYASXXZA3vgPRVq+BSjSlWchlGjlKsjLAZToSwfkj3Uo0ecOyO/dpuKA/KEORbrkAEp0Zet1ib6o8a+m3XN+3HTrwxtuffLYPfPrdL38pQ59KNFr10F+1xBpCS3a0Y0pGAMyak9CsGzdt1a7pqZhFqRx+95tuGKvwajdTb3skIJH5ICZMDjnuqmbnOtGQuPcNLjJE5ybWmKRiEuErpNVPzYiVQJuygWIUAygqOm8iE1VdqYMkSBK6NeMuFlkl4CdtvLnzuTyJdXgRpumc01v61T7s9bQ2UxazRVUK53OpNW+EbWUzaiFXMkq2bkhtZixCv1ZNVrMZNS+81rBstNaTdS2xPhgMTfUqhzG5liYCowOuqkqC6B4/jxumEWlSjFRIZ0+Zm8Pwzt2NIyk+FGglRwb+cvcR3bUKox73gYQRTrv9DASEr1Z3f6YchQNxrExxqjA/POEUL8ioR8FHtdRju2jAgvOQvVv1RTTS/4pzAb/SM47NKN9R5Nv3ZQ3305s89K5xo1d8JopA1OVg9gUa6D+2ifxLi+Pm0Vv8pVGWfhMFmGTGBcFn4doagwacC/Wh76Pgxxo9XnYTEZ+kqDb+ZyBVPPkhIunyUMDHl4njTUii2oyNkd8/wSlVK3bVbQ82DWfDq+evJvqqhKpXnffToD34FtLxgQ6F+7+bS1zaIcUHIceOAVZyMMwDJNfAwDiAivy); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIFFEY3v/N7M7bv9Ltqe04VEwbyLowy5vZRtSIXT11CunUqRzdtR0pd9ndgx6CCQxCpCIQUgIDk0QKugTSURAMql2TCtJIzKBDB29Rh4gZdyGyo9J3GL75PuZ93z/v8fAohRDIoEIUeiELeXAAbgI8AJgDYAc9l7huOyibEqUhQbmGEl1xQN46gCLdug0o0tWXIZRo+Q7IKwGU6BsH5M91KNFXDsgfXVJ2QP5UhyJdmwCU6OrO5xJ9XdPfzrrr3KuEUKRPJ1z+rOKu+X22Xv5Whz6U6ORdkNcaIi2hZTu6NQ1jQEbtKQjOWI+t9a7pWZgHadx+dB9u2RswandTrzuk4Dk5ZiYMzrluclPnupHQODcT3OQJzk3NWCZihdBNsu7HRqRKAEVaWYIIxQCKms6L2FRV52YgEkQJ/ZoRN4vsBrCLVv7KpVy+pBrcaNN0rultnWp/1hq6nEmruYJqpdOZtNo3opayGbWQK1klOzekFjNWoT+rRouZjNp3VStYdlqrmdqOGR8s5oZalZPYHAtTgdFBt1V5CRQvn8cNs6hUJSYqpNPH7N1leMeelpEUPwq0nGMj/5j71J5GhfHQhwCiSBedHkZCojery88op9FgHBtjjArMv0gI9SsS+lHgcR3l2BEqsOA8VHer5phe8y9hNvhXc96hGe172nznpLz/cW5Xls41buxD1twMMFU5jk2xBuqv/RLv8PK4WfQmX22Uha9kGbaJcV3weYimxqABD2N96Oc4yIFWn4ftZOQXCbrM5wykmqcmXbxInhjw8C5pbBBZVJOxBeL7Lyilamxf0fJk33I6vOf5h6muqpDqde/bSfBefBvJmEAXwt1/XMsc2iEFZ6EHLkAW8jAMw+T3AF6ELDg=).

## Other builds of this spec

- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 721 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

