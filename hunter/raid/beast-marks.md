# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Marksmanship's shots (Trueshot Aura, Barrage, Sniper Shot) with a few Beast Mastery points: the classic raid hunter split.* (a hybrid: Beast Mastery/Marksmanship).

**[Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md)** (22/29/0) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--7)

**Other setups of this spec.** The spec's best build for each other setup, in a full raid:

- With a pet: [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 714 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--7)

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Talents with no line below:** **Trueshot Aura**: turn it on before the pull.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 715 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 748 | [28/20/3](https://talentsforever.com/hunter/60/502300151500123-00520503005-3-7) |
| Phase 1 BiS | 762 | [28/20/3](https://talentsforever.com/hunter/60/502301151500023-00500505005-3-7) |

**The gear** (average item level: Pre-BiS 62.5; Phase 1 BiS 63.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Beaststalker's Gloves](https://www.wowhead.com/forever/item=16676) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Beaststalker's Boots](https://www.wowhead.com/forever/item=16675) · *Nerub'enkan, Stratholme*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Beaststalker's Boots](https://www.wowhead.com/forever/item=16675) · *Nerub'enkan, Stratholme*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Trinket | [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) | [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) |
| Main hand | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIFFEY3v/N7M7bP3OnUdtxqJg2kHVhljezjagRu3rqFNKpUzm6aztS7rK7Bz0EVgYhEnUoUgSDTRIpKCiQIAJFMFhQkwrKSMqiQwdvUYeIGXcpsqPSdxi++T/mfd837/FwHwURZFAhDJ2QhiwMAlwBuA0wBSBVuSpx1GZQPguUipxyHgX69HFAXt+FPC3eAuTpSklEgS5eA3nZhwKdexSQP1ajQC+NgvzOIaWSKL+vRp6WxgEFev0hOJ8LtHgRNucvJ511bi6JyNMHNxw+98xZ89tkQP5ajR4U6ItlUX5bE2oQF+zw+gQMAxmyx8BftO5Zq20TkzANwoh9dxyu2mswZLdX/W6WgCdkv8mMGGO6qZuM6UZMY8w0mMlijJlabIHwS4R+IKterEWq+JCnS/MQouhDXtNZHuvK06kihPwooFczomZeugzSKSt79nQmW1ANZjRpOtP0pla1O231nUkl1UxOtZLJVFLtGlAL6ZSayxSsgp3pU/MpK9edVsP5VErtOqflLDupVURtU4z25jN9jcohrI8EKSfRXifV4jworj+LGmZeKY8kXiGtHsneGoa1bGsYQfEiRxcz0sA/eh/eVqsg7n7jQ+Tp7GCHRETe7erwo8oRNCSGtRGJcpJ3lhDqVQT0IseiOsqRvZST/NNQ3q2KYrrJPwWl3r+SsxbNaN7W5Jsn5fX341u8dKYxYwe8poogqcoBrIvUUG/ll7iHl0XNvNt8pVbmvpAF2CDGBc7jIpwYhhrcgwHxxwjIvkaPi4146CfxO8wz2JOoHxt18Dx+sMfFq7ixRmRejUdmiOe/oJCosB1Fw/0d82lxnyfuJNrKg0Snc+eOgvviWYtHODoTbP/jambQDAk4Bh1wEtKQhX7oJ78GALUrLRs=); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVF9IFF8U3nNndufu+flzt6u241AxbSDrwix3xkbUiF196imkp57K0V3bkXKX3X3Qh8DKIET6Bz2sCAarJFJQUCBBBIpgIGhIBWUkZdFDD75FPUTMuEuRPSp9DIdvzsfc7ztzLxf3UQiCDCpEoAvSkIUhgCsAtwGmAViVqxJHbQHlk0RpUFDOo0SfPArIG/+hSDeuAYp0dSmIEl2+DvJzH0p0/mFA/lCNEr1UBPmtQyYvgvyuGkW6NA4o0RsPwPlcoqVKf+6Ws86LKafed/n8U2fNr1MB+Us1elCixZsgv6kJNwQX7cjGBIwAGbbHwF+y7lpr7RNTMAPSqH1nHK7a6zBsd1T9miwBj8l+kxtNXNdN3eScG00a56bzOEVrWiTiCqHvyZoXa5EqPhTpygKEKfpQ1HSex7pyd7oEYT9K6NWMmJlnl4GdsrJnT2eyBdXgRrOmc01vblN70lb/mVRSzeRUK5lMJdXuQbWQTqm5TMEq2Jl+NZ+ycj1pNZJPpdTuc1rOspNaRdS2xFhfPtPfqBzC+miICoz2OamWF0Bx/XnMMPNKucVEhbR5mL09DG/d0TCS4kWBLmfY4F/mPryjViH8/7UPUaRzQ52MBEV3VocfVY6gwTjWRhkVmHeOEOpVJPSiwGM6ytG9VGD+GSjvVkUx3eQfQ6zvj+S8VTNadjT51kl59e34Ni+da9zYBa/pEjBVOYB10RrqrfwS9/DymJl3J1+tlYXPZBE2iXFB8LiIJEagBvdgIPh9FGRfo8fFZjz8g/gd5hnqTdSPFR08ix/sdfEybqwTWVTj0Vni+ScoJCpsV9Fwb9d8Wt16YjLRXm4kupw7twjui2c9HhXobKjjt6uZQwsk4Bh0wklIQxYGYID8HADzACwt).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

