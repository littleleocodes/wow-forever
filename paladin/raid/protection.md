# Protection Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (0/35/16) — [open the talent tree](https://talentsforever.com/paladin/60/-05311102513301531-52233000001-7)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Righteous Fury**, **Retribution Aura**, **Seal of the Crusader**.

**Keep up all fight:** **Righteous Fury**, **Retribution Aura**.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**
2. **Consecration**
3. **Holy Shield**
4. **Holy Strike**
5. **Lay on Hands**
6. **Hammer of Wrath** when the target is below 20% health

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of Fury**: a cooldown, use it at the start of the fight and again whenever it is ready (about 6 times a fight)
- **Templar's Bulwark**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Most of your threat is Holy damage, and **Righteous Fury** makes it 90% more threat. Keep **Holy Shield** up, judge **Seal of Righteousness** on cooldown and press **Consecration** and **Holy Strike** whenever they are ready; **Templar's Bulwark** and **Lay on Hands** are your big defensive buttons.

**Why it works**

- Before the pull: **Righteous Fury** (it lasts 30 minutes, and **Improved Righteous Fury** and **Iron Creed** only work while it is up), then **Seal of Righteousness** and **Holy Shield** in the last seconds, so the first hits already meet both.
- **Holy Shield** lasts 10 seconds and comes back every 10, so keep it up all fight: 30% more block for 4 blocks, and every block deals Holy damage with 20% extra threat and can trigger **Redoubt** and **Shield Specialization**'s mana. The simulator measured 1.3% more tank value with it at the top of the list.
- Press **Judgement** on cooldown, whether or not the short list shows it: it is off the global cooldown, judges **Seal of Righteousness** for about a tenth of your threat, and no longer uses up the seal in Forever. Judging every time it is ready, instead of only before the seal runs out, measured 4.3% more tank value; **Swift Judgement** goes right after a **Judgement**, because it finishes the cooldown and makes the next one free.
- **Consecration** and **Holy Strike** fill the rest: **Consecration** threatens everything standing in it, and **Holy Strike** with **Iron Creed** makes 25% more threat and cuts your damage taken by 10% for 6 seconds. Refresh **Seal of Righteousness** when it has about a second left.
- **Templar's Bulwark** sits at the top because the simulator's 3-minute fight fits one use: it absorbs damage equal to your maximum health for 8 seconds, off the global cooldown, and using it at the pull measured 1.4% more tank value. It applies Forbearance for a minute, which locks you out of **Divine Protection**, **Divine Shield** and **Blessing of Protection**.
- **Lay on Hands** is last in the list with no health condition: in the simulator's fights nobody heals you, and casting it whenever nothing else is ready measured 0.4% more tank value than keeping it for 10% health (8% more than not using it). It heals you for your maximum health but drains all your mana, and its cooldown is 20 minutes: in a raid with healers, keep it for when you are about to die.

**Caveats**

- The simulator tanks with **Seal of Righteousness**. **Seal of Fury** (35 Holy damage a swing, plus an absorb of half of it while you hold a shield) is not part of its tuned rotation, so whether it is better for you was not measured.
- Mana: you run dry for a few seconds of each 3-minute fight in the simulator. **Consecration** is the expensive button (565 mana before **Holy Conduit**); blocks give mana back through **Shield Specialization** and judgements through **Sanctified Judgement**.
- The simulator measures one boss. **Consecration** and **Holy Shield** work on everything that hits you; **Holy Strike** and **Judgement** only on your target.

**When to change it**

- To taunt (a tank swap, a loose add), put up **Seal of Fury** and judge: its judgement taunts for 4 seconds. Use **Swift Judgement** if **Judgement** is on cooldown, then go back to **Seal of Righteousness**.
- Hold **Templar's Bulwark** for a known damage spike or a healer death when the fight has one: the simulator spends it at the pull only because its fight fits a single use.
- Undead or Demon packs: **Holy Wrath** (a 2-second cast) hits and stuns every Undead and Demon within 20 yards, and **Exorcism** hits one hard. Neither was measured: the simulator's boss is an Elemental.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

Tank value 1.021 (threat and damage taken under a boss, relative to our reference tank build).

**The gear** (average item level: Pre-BiS 62.8; Phase 1 BiS 63.2; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Enriched Thorium Helm](https://www.wowhead.com/forever/item=250597) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Enriched Thorium Helm](https://www.wowhead.com/forever/item=250597) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Enriched Thorium Breastplate](https://www.wowhead.com/forever/item=250595) · *Blacksmithing*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Enriched Thorium Breastplate](https://www.wowhead.com/forever/item=250595) · *Blacksmithing*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Warder's Wristguards](https://www.wowhead.com/forever/item=250583) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Warder's Wristguards](https://www.wowhead.com/forever/item=250583) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Warder's Gloves](https://www.wowhead.com/forever/item=250553) · *Blacksmithing*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Warder's Gloves](https://www.wowhead.com/forever/item=250553) · *Blacksmithing*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Belt of Heroism](https://www.wowhead.com/forever/item=21994) | [Belt of Heroism](https://www.wowhead.com/forever/item=21994) |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Warder's Sabatons](https://www.wowhead.com/forever/item=250563) · *Blacksmithing*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Warder's Sabatons](https://www.wowhead.com/forever/item=250563) · *Blacksmithing*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) |
| Trinket | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) |
| Trinket | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVd+LG1UUzrlzM3PmTLeJ19adXlSmg9Q0MGFmYnS7Lzvtk08SfPLNHZvUxJUkJEHqW1coCIrUPtlVstI0UNYfwUVhu7ggirXtiyL+gEBrfwkiBat/gMidNI0WH3xp/R4u537fPXfOfOcwQw8iZMEGB3KwCDVowRGAVwHeBTgNILYlKlPqHMhvEXmWyWUgA38eZOzrFnHsvwXEcfSOIr8+BvaV7WTgtUHGvqaCHwcZ+22DDDwzyNg/bSeOv76nTr75Eah0A7+Y8N8P1D3HbmSJ48Y3ar35mjr524dg31BXXTp6n31Jnex/Au7u7Nl67voqrIDZj9+PR/tXB7AG1uv13x9aOw1v1I/WD2BSO0SwyR72/FIxCAI/LAXFoh+UioFXCsNi0VcIzjF+lV3UaQeh1Injx+fBRdKJe6HfoVkypUHpXBq3yi4Rku4Fc4WSEkgi6Tkdv+uBa5JBaS8olDpiBGIxbr34bLPVdUI/fNwLfK8YzDsHa3Hj+WrFabaduFKpVpznXna6tarTbnbjbr3ZcDrVuH2w5uQ61arTaje7XjduLHkT2RvLhRc6zcZe+RItiTr5okA78/ejLtJ/GAw1VRBxvxB0JvTn7J/0jGuReRLUew57QHvyjyAX5tqEkDvXmUAmzJPGhNE2eSpxAPFiWXDJ5lOC5NiqYQ9EKP3/fI3aHH+lLJ6QJdorHiU7/wBqwtoEZaSBX62CHFdM1kifcrcjsQ/h31IRv+zdmTrmbkdimxz3K42f9kH4skCudCjjzpB1FZUAeGa5TDPrQMTxyvGnBMumkwyOwwvTfA0/64OwpDk1ZekeNNyQadLwbFmcuhfjFdFjMqRd+VkEYa0w5YKGwy1QXSfmj8dLu2Pqws4tg4ZbU4N0vFC2tV/YObjJwmUtlWBHtA6cGKXcP5mpiNSRQ9GulRMK5xd2H0rww0J4mdncWchvsNT/gm40ie4q9nxw156zL1mfPhXtv0VEi+r7fgKSTeryQl7Djdl5loUDf/sV+DAHETwJZXgGatCCw3CY/TUAuzocpg==); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVd+LG1UUzrlzM3PmTLeJ19adXlSmg9Q0MGFmYnS7Lzvtk08SfPLNHbupiStJSILUt65QEBSpBcGukpWmgbIqwUVhu7ggirXtiyL+gEDr9ocg0ofqHyByJ02jxQdfuv0eLud+3z13znznMEMPI2TBBgdyMA9VaMIxgNcBPgA4CyB2JCpT6gzI7xF5lsklIAN/7WfsGxZx7L0LxHH4viK/PQH21Z1k4PV+xr6ugp/7Gfs9gww818/Yv+wkjr9/qE6+/QmodAO/GvM/9tU9J25mieP6d2q99YY6ufUO2DfVVVeOP2BfUSd7n4G7N3u+lruxAstg9uKP4uHBlT6sgvVm7Y9HVs/CW7XjtUOY1A4RbLBHPb9UDILAD0tBsegHpWLglcKwWPQVgguMX2OXddpFKHXi+OlFcJF04l7ot2maTGlQOpfGzbJLhKR7wUyhpASSSHpOxx+64JpkUNoLCqW2GIKYj5svP99odpzQD5/0At8rBrPO4Wpcf7Gy4DRaTrywUFlwXnjV6VQrTqvRiTu1Rt1pV+LW4aqTa1cqTrPV6HiduL7ojWVvJBdeajfq++UrtChq5IsC7c4/iLpI/2kw1FRBxP1C0B7TX7J/01OuReZpUO856ALtyz+GXJirY0LuXmMCmTBPG2NG2+CpxAHEy2XBJZtNCZIjqwZdEKH0//c1anPytbJ4SpZov3ic7PxDqAlrA5SRBn6zAnJUMVlDfcLdicQBhP9KRfy6e3fqiLsTiR1y1K80ft4D4csCudKhjDtF1jVUAuC5pTJNrQERx6snnxEsm04yOA4uTfI1/KIHwpLmxJTFbWi4IdOk4fmyOLMd4xXREzKkPflpBGEtM+WChoNNUF0n5o/GS7tr6sL2bYMGmxODdLxUtrXf2AW4xcIlLZVgV7QGnBil3L+YqYjUsSPRnuVTChfn9h5J8NNcuMVs7szl11nqvqATjaN7in0f37PnHEjWZ89EB28T0bz6vp+CZJPamstruD49y7Jw6B+/Ah9mIIKnoQzPQRWacBSOsr8HAN3cHH4=).

## Other builds of this spec

- [Protection — Tank](../research/raid/builds/prot-tank.md) (0/33/18) — [open the talent tree](https://talentsforever.com/paladin/60/-15310112513501031-50233300011-7)
- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (1/34/16) — [open the talent tree](https://talentsforever.com/paladin/60/01-25300132503501031-50033310001-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

