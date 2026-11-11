# Destruction Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Destruction

**[Destruction — Raid](../research/raid/builds/destruction-ml-raid.md)** (9/11/31) — [open the talent tree](https://talentsforever.com/warlock/60/252-0050203001-055031500310035-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Destruction — Incinerate), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Shadow Bolt setup. The spec's best build for each other setup, in a full raid:

- Incinerate: [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-open-raid.md) (10/11/30, 793 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055030500310035-12)

## How to play

**Setup, before the pull:** **Summon Imp**, then **Demonic Sacrifice** it: you fight with its buff and no demon, which the rotation below assumes. Keep **Demon Armor** on you.

**Before the pull:** **Life Tap**.

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Conflagrate**
7. **Shadow Bolt** (rank 9)

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Before the pull: put on **Demon Armor**, summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours, worth about 10% of your damage in the simulator) and **Life Tap** once so you start full. In the fight Destruction is still a **Shadow Bolt** spec: keep **Immolate** on the boss so **Conflagrate** can go out every 10 seconds, and let **Shadow and Flame** turn each **Conflagrate** into 20% more Shadow damage for 20 seconds.

**Why it works**

- Before the pull: summon the Imp and use **Demonic Sacrifice** (summoning any demon ends it), then **Life Tap** once. Put a Spellstone (**Create Spellstone**) on your weapon on top of your wizard oil: Forever lets them stack, and the simulator measured about 3% more damage. **Demonic Embrace**, **Demonic Aegis** and **Fel Vitality** are the points that reach the sacrifice: **Demonic Aegis** makes **Demon Armor** 30% stronger and **Fel Vitality** adds 15% to your maximum mana. This build has no **Amplify Curse**.
- **Curse of the Elements** goes up first: 10% more damage from every magic school, Fire and Shadow alike, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana, and **Improved Life Tap** adds 20% to each tap.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (a 1.2-second cast with this build's 2 points in **Improved Corruption**) goes back up when it is about to run out, but not in the last 10 seconds.
- **Immolate** matters as much for **Conflagrate**, which needs it on the target, as for its own damage: start a new one when less than its cast (1.5 seconds with the **Bane** talent) is left on the old one, but not in the last 20 seconds.
- **Conflagrate** goes out whenever it is ready. With 5 points in **Shadow and Flame** it no longer eats your **Immolate** (each rank is a 20% chance not to), and each hit gives you 20% more Shadow damage for 20 seconds, twice its cooldown; **Fire and Brimstone** and **Ruin** make its crits frequent and big.
- **Shadow Bolt** is the filler: the sacrificed Imp, **Improved Shadow Bolt**, **Ruin** and **Shadow and Flame** all raise Shadow damage, so the filler is the one spell they all feed.

**Caveats**

- The last seconds belong to quick spells: with 3.5 seconds left the rotation casts **Searing Pain** (a 1.5-second cast) because a **Shadow Bolt** still casting when the boss dies does nothing. It does not belong earlier in the fight.
- With the Imp sacrificed you play without a demon: any summon ends the buff, so if you die, summon the Imp and sacrifice it again before the next pull.
- On the move, **Bane of Agony**, **Curse of the Elements**, **Conflagrate** and **Life Tap** are instant; **Corruption** still has a 1.2-second cast in this build.

**When to change it**

- In the last 20 seconds start no new **Immolate**, and in the last 10 no **Corruption**: cast **Shadow Bolt**, then **Searing Pain** in the last 3.5 seconds.
- The other setup listed on this page plays a different rotation: follow the list on its own page, not this one.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Affliction | 9 | Improved Life Tap 2, Suppression 5, Improved Corruption 2 |
| Demonology | 11 | Demonic Embrace 5, Demonic Aegis 2, Fel Vitality 3, Demonic Sacrifice 1 |
| Destruction | 31 | Improved Shadow Bolt 5, Bane 5, Cataclysm 3, Aftermath 1, Ruin 5, Agonizing Flames 3, Conflagrate 1, Fire and Brimstone 3, Shadow and Flame 5 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 815 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 771 | [10/11/30](https://talentsforever.com/warlock/60/253-0050203001-055030500310035-12) |
| Phase 1 BiS | 811 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 59.4; Phase 1 BiS 61.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [item 254013](https://www.wowhead.com/forever/item=254013)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [item 254013](https://www.wowhead.com/forever/item=254013)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Orb of the Forgotten Seer](https://www.wowhead.com/forever/item=7685) · *Bloodmage Thalnos, Scarlet Monastery* | [Mordresh's Lifeless Skull](https://www.wowhead.com/forever/item=10770) · *Mordresh Fire Eye, Razorfen Downs* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElV9oI1UUxnPu3GRuTrWZvat0OqsyBrLEwIQ7E8amRcjsPi0+FZ+EBd1kk5oETUImDysirGxFEc3KxpeNBf+u2wpq8aEWQaiFQuqD5MmXUixKUUSwiPRRZCaTKmkffEjZ83Bzcj5uzu+754aLDzFQQAUdknAFytCA6wCvA7wPsAzA7/NV4qlZ0D6ZYJIS1VyU2d1boO5PIGU3vgCk7Ld3vPXdvoIRtl1Tf55EmW3eAXVnEiW2WUPK9m8CRtifC94umX2zEVNvykhZ+3cFKfvuA0CJvf0CUrbWV1Bmf3wOau8sSuzVJ5CylaVY3FJ6leT3bRCHhfm3PoQ3gCxWbgE5LHQh/MuF9+7ApyDfXYLVS+3KKnxU3YPFykXm04MDX5NHLDtjCGELS2SEMA1h2yIjbCEyphAZu0ekPpn4iSxH8SwyLYKUHbQhLmMYJcN28QGUtTBKbOVyPIoyhg0zbbv8Ye0cnonH8P4vAZGyjdfmOVHC/m4vtzSBSX4ez6RiLMLJkyHN/z3Tdv0S5aQQlGbshEaRqCrvAH8m33j+2XqjpVvCetwwhSGsOf1qOV97rlTU6009XyyWinrhRb1VLunNeivfqtRrulvKN6+W9aRbKuluwWjmK0VjKBoDMV1167XHNPN/QmVFwvOsHBY41chcaGB3AH60LW37dr/qwElyJpBvvAn8pRFjYtawZsZqbBqV1CST/GONIEViJ4KhcdSOhsrjmo5TqQcZ5XLVk7+9rLEuCbLBB18aHYNHmx0r7RwKnsbp1BSjnFU9uB+3QIt2SZAem5BwtUA6GW/mlPF2/8XbPY5nBXi7W8CrI3TeHTbHSjeY5l8d4C+P9jINMd6TODe0OvxjWHbCa68sdk6wOvb2vlVlra8cXeKdLVClX0kPDoj1ihTyY9bpEoYRpDpxIP43iXrF0PUFZ7p724vt3KMLfvyQs/aISvVcap2E7km0nGF2qnH+s1PrM+uvT33sXAgKzhXvzbwN/pfQXi4lsfWpi/95WgVkwYFLMA9PQxkacA2ukX8GAI+ujik=); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElUFoI1UYx/O9ecm8fNVm9q3S6azKGMgSAxPeTBib9pLZPS2eingQFnSTTdYkSBIyEVZEWDGgiHYhcQ8bC4q6bFdQFg/rIgi1UEgRJCcvJViUonixB+mxyEwmUdIePKT4HV6+fP+8fL//fG94+AQDBVTQIQlXoAwNuAHwLsAnABsA/BFfJZ6aBW1jjklKVHsNZXa3A+r+HFJ21AGk7I8PvfWjgYIRtlNTf51HmW3dAXV3HiW2VUPK9m8Cymx4y98ms+82Y+pNGSn74RZM1gcDBSlrd71f/vkVqP2zKLHOC0jZvfVY3FL6leSPayAOC6sffArvAWlXOkAOCz0I/3bh4zvwBch31+H+pbXKffisugftykXm84MD35KnLNsyhLCFJTJCmIawbZExbSEyphAZu0+kAZn7hWxE8SwyLYKUHaxBXMYwSobt4mMoa2GU2L3L8SjKGDbMtO3yJ7VzeCYew0e/BkTKNt9Z5UQJ+7u93NIEJvl5PJOKsQgnz4U0//9M2/VLlJNCUFqyExpFoqq8C/ylfOPVl+uNlm4J61nDFIawVvSr5XztlVJRrzf1fLFYKuqF1/VWuaQ36618q1Kv6W4p37xa1pNuqaS7BaOZrxSNsWiMxHTVrdee0cz/CJUVCc+zcljgVCMroZHdEfhkW9r27X7ThZPkTCC//T7wN6aMiWXDWpqpsUVUUvNM8h9rBCkSOxEMjaM2GSqPazoupB5nlMtVT/7+ssZ6JMhGH3x9egwebXamtCsoeBoXUwuMclb14H7eBi3aI0F6bELC1QLpZLylU8Yb/oM3PI5nBXjDbeDVKTrvDJszpRtN868u8Dene5mGmO2TODe2On4xLDvhtVfa3ROszry9b1V5MFAmh3h3G1Tpd9KHA2K9JYX8WHZ6hGEEqU4ciB+RqFcM3bjmLPZue7GTe/qaHz/lrD2iUj2XekhC/0u0nHF2qnH+y1Prs+yvz3/uXAgKzhXv1rwN/pfQXi4lsYcLF/91uQrIggOXYBVehDI04DpcJ38PAKcfjrQ=).

## Other builds of this spec

- [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-raid.md) (9/11/31, 755 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/153-0050203001-0050245103101351-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

