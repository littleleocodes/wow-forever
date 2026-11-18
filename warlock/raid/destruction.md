# Destruction Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Destruction

**[Destruction — Raid](../research/raid/builds/destruction-ml-raid.md)** (9/11/31) — [open the talent tree](https://talentsforever.com/warlock/60/252-0050203001-055031500310035-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Destruction — Incinerate), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Shadow Bolt setup. The spec's best build for each other setup, in a full raid:

- Incinerate: [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-open-raid.md) (10/11/30, 802 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055030500310035-12)

## How to play

**Setup, before the pull:** **Summon Imp**, then **Demonic Sacrifice** it: you fight with its buff and no demon, which the rotation below assumes. Keep **Demon Armor** on you.

**Before the pull:** **Life Tap**.

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage for 2 hours; summoning any demon cancels it).

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 826 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 793 | [10/11/30](https://talentsforever.com/warlock/60/253-0050203001-055030500310035-12) |
| Phase 1 BiS | 825 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.3; Phase 1 BiS 64.2; each item opens its Wowhead page, with where it drops and its enchant):

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
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElUFoI1UYx/O9ecm8fNXu7Ful01mVMZAlBia8mTA27SWze1o8FU/Cim6ySU3CmoRMDisirGxBkTUVI0JjQVGLVWgtHmrxpIVCepGcvJRiUYoigqVIL4LITCZV0h48pOx3ePny/Xn5fv/3vfDwMQYKqKBDAm5CCepwF+BNgI8AVgD4Q75KPDUD2vIYk5So1kCZ/bUK6sEYUnbvS0DKfnvPWz/oKRhhO1X153GU2dYyqLvjKLGtKlJ2sAAYYUdz3q4IW3teXZCRstbvClL2fs9bN3oKSuydl1Fmf6yB2r2ElN1fAJTY0e2YpXTLie9bII7zs29/DG8BmS+/C+Q434HwL1c/XIYvQP5sCdavt8rr8EllH+bL15gPDw58Q56w7LQhhC0skRbCNIRti7SwhUibQqTtLpF6ZOwnshLFS8i0CFJ22IKYjGGUDNvFR1DWwiixz2/Eoihj2DBTtssf1y7jxdgFfPgrQKTs2zdmOVHC/m4vtzSBCX4FLyYvsAgnz4Q0//dM2/VLlJN8UJqy4xpFoqq8DfyFXP32i7V6U7eE9bRhCkNYM/qtUq76UrGg1xp6rlAoFvT8K3qzVNQbtWauWa5VdbeYa9wq6Qm3WNTdvNHIlQvGQDT6Yqri1qpPaeb/hMqIuOdZOc5zqpGZUN9uH/xkW8r27X7dhrPkdCDfuw/81SFjYtqwpkZqbBKV5DiT/GONIEVix4OhcdROhspjmo4TyUcZ5XLFk7+7obEOCbL+B18aHoNHmxkp7QwKnsLJ5ASjnFU8uB+3QYt2SJCempBwtUA6G2/qnPH2/sXbO41nBXh728ArQ3TeHTZHStef5p9t4K8N9zINMdqTuDywOvhjWHbca6/Mt8+wOvL2vlVlo6ecXOLdbVClX0kXDon1uhTyY9rpEIYRpDpxIPY3iXrF0N05Z7Kz6MVO9sk5P37IWvtEpXo2uUlCDySaziA717iyem59pv312U+dq0HBuek9mYvgfwntZ5MS25y49p+XVUAGHLgOs/AclKAOd+AO+WcA8Y+Ogg==); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElUFoI1UYx/O9ecm8fNXu7Ful01mVMZAlBia8mTA27SWze1o8FU/Cim6yyZqEJQmZHFZEWDGgyNrCxj1sXFDUpVVoKR5q8aSFQoogOXkpwaIUxYtFpBehyEwmUdIePKT4HV6+fP+8fL//fG94+BQDBVTQIQHXoQR1uAPwLsDHAKsA/DFfJZ6aAW1liklKVGuizP5aA/VgCik7vgdI2W8feOuHPQUjbLeq/jyNMtt+BOreNEpsu4qUHSwDyqx/398WYesvq8syUvbdfRitmz0FKWu1vR/+vg5q9wJSdncZUGJ/3IpZSrec+H4JxFF+8f1P4D0grfI9IEf5DoR/ufzRI/gC5JWHsHF1qbwBn1b2oVW+wnx8cOBr8oxlW4YQtrBEWgjTELYt0qYtRNoUIm13idQjUz+R1SheQKZFkLLDJYjJGEbJsF18AmUtjBL7/FosijKGDTNlu/xp7SKej53Dx78ERMq+eWeREyXs7/ZySxOY4JfwfPIci3DyQkjz/8+0Xb9EOckHpTk7rlEkqsrbwF/J1W+9Wqs3dUtYzxumMIS1oN8o5aqvFQt6raHnCoViQc+/rjdLRb1Ra+aa5VpVd4u5xo2SnnCLRd3NG41cuWAMRWMgpipurfqcZv5HqIyIe56VozynGlkIDewOwEfbUrZv96s2nCanA/ntu8DfGDMm5g1rbqLGZlFJTjPJf6wRpEjseDA0jtpoqDym6TiTfJJRLlc8+dtrGuuQIBt88IfjY/BoMxOlXUDBUzibnGGUs4oH9+MOaNEOCdITExKuFkin482dMV7/H7z+STwrwOvvAK+M0Xln2Jwo3WCaf7aBvzneyzTEZJ/ExaHV4Yth2XGvvdJqn2J14u19q8pmTxkd4r0dUKVfSRcOifWWFPJj3ukQhhGkOnEgdkyiXjF056Yz23ngxW722Zt+/JC19olK9Wxyi4T+l2g6w+xM49LamfWZ99cXP3MuBwXnundpPgD/S2g/m5TY1syVf92tAjLgwFVYhJegBHW4DbfJ3wMAxAaO3g==).

## Other builds of this spec

- [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-raid.md) (9/11/31, 762 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/153-0050203001-0050245103101351-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-18 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

