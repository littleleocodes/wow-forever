# Destruction Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Destruction

**[Destruction — Raid](../research/raid/builds/destruction-ml-raid.md)** (9/11/31) — [open the talent tree](https://talentsforever.com/warlock/60/252-0050203001-055031500310035-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Destruction — Incinerate), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Shadow Bolt setup. The spec's best build for each other setup, in a full raid:

- Incinerate: [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-open-raid.md) (10/11/30, 789 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055030500310035-12)

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 811 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 771 | [10/11/30](https://talentsforever.com/warlock/60/253-0050203001-055030500310035-12) |
| Phase 1 BiS | 811 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 60.1; Phase 1 BiS 62.6; each item opens its Wowhead page, with where it drops and its enchant):

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
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) · *sold by Gaelden Hammersmith* | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) · *sold by Gaelden Hammersmith* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9oK1UUxnPu3GRuztN23n1Kp+MfxkAfMTDhzoSxSTeZ91bFVXElFLRJk5oESUImSMVNxYJWNFUjSmNBUYu2IhYXtrhRC4V0U7pyYSmWSlHERUHpUmQm0yptFy5S3lncnJxvztzfN+fCxYcZKKCCDnGYghLUYQ7gNYCPAD4H4Pf5KvHUNGhryCQlqr2AMltbAPX4BlJ29D4gZb+/6627bwFG2E5V/WUAZba1Aur+AEpsq4qUHS8CyuyLXpvMvloAdVFGyn5a8TpbfyhI2Td73vr2dwrK7IMNULu3kLI/3/MeWF0ejFlKtxzfbYE4zU+8+TG8DmS+/A6Q03wHwr/e+XAF1kD+bBnWx1vldfikcgjz5bvMNwAOfEsetWzLEMIWlkgJYRrCtkXKtIVImUKk7C6R9siNI7LK8BYyLYKUnbQgJmMYJcN28QGUtTBKbHUyFkUZw4aZtF3+iPYQ3owN4v1fAyJl3786wYkS9ru93NIExvltvJkYZBFOngxp/vtM2/VLlJN8UBq1RzSKRFV5G/gzufrzz9bqTd0S1hOGKQxhjenTpVz1uWJBrzX0XKFQLOj5F/Vmqag3as1cs1yr6m4x15gu6XG3WNTdvNHIlQvGmWj0xGTFrVUf18z/CZUWI55n5TTPqUbGQj27PfDztqTt291ow1VyKpBfeQP4SxeMiYxhjfbV2DAqiQEm+Z81ghSJPRIMjaN2PlQe03QcSjzIKJcrnvzDpMY6JMh6P3z54hg82nRfacdQ8CQOJ4YY5aziwf28DVq0Q4L00oSEqwXS1Xij14x38C/ewWU8K8A72AZeuUDnnWGzr3S9af7VvnqvTP/3UubbcH6K9rdBlX4jXTgh1stSyI+M0yEMI0h14kDsbxL1iqG5GWe4s+TFTvaxGT9+zFqHRKV6NrFJQvckms5Zdq1x+8tr2yfjr0996twJCs6Ud28tgf8ndJhNSGxz6O5/rjcBaXBgHCbgaShBHWZhlvwzAKbxaeE=); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9oK1UUxnPuTDI3p9pOb5VOxz+MgZYYmHBnwtikm0y7Kq6KK6GgTZrUJEgSMkEqbipGtKItNCo0FhS1aCticWGLKy0UUgTpyk0pFqUorgpKl0VmMs17tF28Rco7izNnzsed+/vmXLj4JAUZFNAgCnNQgCosAbwL8BnA1wDsEU8lrpoEdRupIIfV11Ci28ugnPWhSC/XAEX6z4duPnt7EEP0sKz82Y8S3d8E5bgfBbpfdrVVQIl+01km0e+WQVmVUKS/fATd3Gi6+YcjGSX6yS4o7SEU6b8fu82tjYGIKbeL0V9XgF9kZz74HN4D0iiuAbnItiD41+Snm7AN0lcbsDO9UtyBL0qn0ChOUc8A2PAjedq0TJ1zi5s8wbmhc8viCcPiPGFwnrDaRDgifX+QLYpDSNUQivR8BSISBlHQLQcfQ0kNokC3ZiNhlDCoG3HLYU+pT+BgZAAf/R4QRfrTOzOMyEFvtVubKscoG8PB2AANMfJ8QPW+Z1iO1xIZyfqtcWtUFZEoCmsCeylTffXlSrWumdx8Tje4zs0Jbb6QKb+Sz2mVmpbJ5fI5Lfu6Vi/ktVqlnqkXK2XNyWdq8wUt6uTzmpPVa5liTr8S9Y4YLzmV8rOq8YBQST7qepYvskxUyUSgY7cD3l0Wtzy7u024TU748lvvA3vjmjGe0s3xnhobQTnWTwXvt4ZQRGKN+kNjqHaHyiKqhsOxx6nIpJIr/zyr0hbxq86DbVwfg0ub7CntBHIWx5HYMBUZLblwvx+AGm4Rv7wxIe6ovnQ73vgd453cwzu5iWf6eCcHwErX6NwzbPSUrjPN/5q375Xq/V5yowndU3R8AIrwN2nDOTHfFAJepOwWoRhCUSM2RC5J2G0Glhbskda6G4fpZxa8+C1tnhJF1NKxPRJ4KFG3r6o7jbFv72yflJdf+NKe9Bv2nHtvrYP3EjhNxwS6Nzx13/XGIQk2TMMMvAgFqMIiLJL/BwBaTmmE).

## Other builds of this spec

- [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-raid.md) (9/11/31, 750 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/153-0050203001-0050245103101351-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-09 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

