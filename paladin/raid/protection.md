# Protection Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (0/35/16) — [open the talent tree](https://talentsforever.com/paladin/60/-05311102513301531-52233000001-12)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Righteous Fury**, **Retribution Aura**, **Seal of the Crusader**.

**Keep up all fight:** **Righteous Fury**, **Retribution Aura**.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**; no global cooldown, so press it alongside the others
2. **Consecration**
3. **Holy Shield**
4. **Holy Strike**
5. **Hammer of Wrath** when the target is below 20% health

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of Fury**: part of the rotation (about 6 times a fight)
- **Templar's Bulwark**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Lay on Hands**: when you are about to die: a full heal on a long cooldown that empties your mana
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Most of your threat is Holy damage, and **Righteous Fury** makes it 90% more threat. Keep **Holy Shield** up, judge **Seal of Righteousness** on cooldown and press **Consecration** and **Holy Strike** whenever they are ready; **Templar's Bulwark** and **Lay on Hands** are your big defensive buttons.

**Why it works**

- Before the pull: **Righteous Fury** (it lasts 30 minutes, and **Improved Righteous Fury** and **Iron Creed** only work while it is up), then **Seal of Righteousness** and **Holy Shield** in the last seconds, so the first hits already meet both.
- **Holy Shield** lasts 10 seconds and comes back every 10, so keep it up all fight: 30% more block for 4 blocks, and every block deals Holy damage with 20% extra threat and can trigger **Redoubt** and **Shield Specialization**'s mana. The simulator measured 1.3% more tank value with it at the top of the list.
- Press **Judgement** on cooldown, whether or not the short list shows it: it is off the global cooldown, judges **Seal of Righteousness** for about a tenth of your threat, and no longer uses up the seal in Forever. Judging every time it is ready, instead of only before the seal runs out, measured 4.3% more tank value; **Swift Judgement** is a second, free **Judgement** on its own 1-minute cooldown: use it whenever it is ready.
- **Consecration** and **Holy Strike** fill the rest: **Consecration** threatens everything standing in it, and **Holy Strike** with **Iron Creed** makes up to 30% more threat and cuts your damage taken by up to 6% for 6 seconds (rank 3). Refresh **Seal of Righteousness** when it has about a second left.
- **Templar's Bulwark** sits at the top because the simulator's 3-minute fight fits one use: it absorbs damage equal to your maximum health for 8 seconds, off the global cooldown, and using it at the pull measured 1.4% more tank value. It applies Forbearance for a minute, which locks you out of **Divine Protection**, **Divine Shield** and **Blessing of Protection**.
- **Lay on Hands** is last in the list with no health condition: in the simulator's fights nobody heals you, and casting it whenever nothing else is ready measured 0.4% more tank value than keeping it for 10% health (8% more than not using it). It heals you for your maximum health but drains all your mana, and its cooldown is 20 minutes: in a raid with healers, keep it for when you are about to die.

**Caveats**

- The simulator tanks with **Seal of Righteousness**. **Seal of Fury** (35 Holy damage a swing, plus an absorb of half of it while you hold a shield) is not part of its tuned rotation, so whether it is better for you was not measured.
- Mana: you run dry for a few seconds of each 3-minute fight in the simulator. **Consecration** is the expensive button (565 mana); blocks give mana back through **Shield Specialization** and judgements through **Sanctified Judgement**.
- The simulator measures one boss. **Consecration** and **Holy Shield** work on everything that hits you; **Holy Strike** and **Judgement** only on your target.

**When to change it**

- To taunt (a tank swap, a loose add), put up **Seal of Fury** and judge: its judgement taunts for 4 seconds. Use **Swift Judgement** if **Judgement** is on cooldown, then go back to **Seal of Righteousness**.
- Hold **Templar's Bulwark** for a known damage spike or a healer death when the fight has one: the simulator spends it at the pull only because its fight fits a single use.
- Undead or Demon packs: **Holy Wrath** (a 2-second cast) hits and stuns every Undead and Demon within 20 yards, and **Exorcism** hits one hard. Neither was measured: the simulator's boss is an Elemental.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Protection | 35 | Redoubt 5, Precision 3, Guardian's Favor 1, Sacred Duty 1, Templar's Bulwark 1, Shield Specialization 2, Toughness 5, Swift Judgement 1, Improved Righteous Fury 3, Anticipation 3, Holy Shield 1, Reckoning 5, Iron Creed 3, Shieldsworn 1 |
| Retribution | 16 | Deflection 5, Benediction 2, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Sacred Arbiter 1 |

## The numbers

Tank value 1.023 (threat and damage taken under a boss, relative to our reference tank build).

**The gear** (average item level: Pre-BiS 61.9; Raid BiS 61.9; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Raid BiS |
|---|---|---|
| Head | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Talisman of Evasion](https://www.wowhead.com/forever/item=13177) · *War Master Voone, Blackrock Spire* | [Talisman of Evasion](https://www.wowhead.com/forever/item=13177) · *War Master Voone, Blackrock Spire* |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Kromcrush's Chestplate](https://www.wowhead.com/forever/item=18503) · *Captain Kromcrush, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Kromcrush's Chestplate](https://www.wowhead.com/forever/item=18503) · *Captain Kromcrush, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Warder's Wristguards](https://www.wowhead.com/forever/item=250583) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Warder's Wristguards](https://www.wowhead.com/forever/item=250583) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Warder's Waistguard](https://www.wowhead.com/forever/item=250573) · *Blacksmithing* | [Warder's Waistguard](https://www.wowhead.com/forever/item=250573) · *Blacksmithing* |
| Legs | [Legplates of the Eternal Guardian](https://www.wowhead.com/forever/item=11927) · *Chest of The Seven, Blackrock Depths*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Legplates of the Eternal Guardian](https://www.wowhead.com/forever/item=11927) · *Chest of The Seven, Blackrock Depths*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Grimy Metal Boots](https://www.wowhead.com/forever/item=18521) · *King Gordok, Dire Maul*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Grimy Metal Boots](https://www.wowhead.com/forever/item=18521) · *King Gordok, Dire Maul*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) |
| Finger | [Ring of Awareness](https://www.wowhead.com/forever/item=272409) · *sold by Pix Xizzix* | [Ring of Awareness](https://www.wowhead.com/forever/item=272409) · *sold by Pix Xizzix* |
| Trinket | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* |
| Trinket | [The Lion Horn of Stormwind](https://www.wowhead.com/forever/item=14557) · *world drop* | [The Lion Horn of Stormwind](https://www.wowhead.com/forever/item=14557) · *world drop* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVU9oHFUY3+/N7Mw33zTN+Nqa6UNlOkjdLswyM9vVNJdMexIEWTx5ETM2G3dNya7ZRepFWqHgQSTkIomykW4XSlAXgkIMDYhom1bFHoriQmtbC3oQ/HPzIvJmul0NHjzY+js8vvf7zZv5ze/74NEDCBbY4EAOpqAKDTgB8BrAOwBnAfiORGVSHQdxzkDVYuIV0vGH7qh9yyQFf58hFftvA+n41QLYN3aSjhcWwP5eFt90R+23dNLx0y8s+7udpOKX3VHS8M1n5GEdv12AlF74ySIVly7Ldf2yRQpefZF0/Pl9sLd2kY7XTt1nX5MPdj4Ed591vpa7tQLLYHTid+P+4ZUurIL5eu3XB1fPwhu1U7UjmPiGCDbYQ55fKgZB4IeloFj0g1Ix8EphWCz6EsEWU2+yz3XaTSg0UvGDi+AiaaR6od+kMTKETtlcFjfLLhGS5gXjhZIUSCBpOQ2vtME1SKesFxRKTd4HPhU3jj1bb7Sc0A8f9QLfKwYTztFqPPd8Zdqpzzvx9HRl2nnuZadVrTjz9VbcqtXnnGYlnj9adXLNSsVpzNdbXiuem/UGspfKhRea9bkD4iWa5TXyeYH25HehxrO/6QwVaYhUvxA0B/Qn7O/0iGuScRrkf/baQPvzD6PKjdUBIfasMY6MG6f1AaNsqJkkAcSrZa4KNpHhJNKoem3gofD/9WvkZvHVMn9MlOgAf4Ts/P2ocHMDZJA6XlgBkToms68NuTsVP4TwT0cRP2tvP5pydyq+Q6T9yuK5DvBj23sUeP7B/7hHaUaLV57gviiQKxwadUfIvInSBuBHJ8s0sgZEKt5YfJIzK5v4U7F3aehWwY87wE1hDFswew/GSxdZUvB8mZ+5F8Mc0UER0t78GAI3l5lMQcHeJsj8iPnpMCvbZjxs3g6otzkMSMNLZVv5kW3BLyw8qWQS7I7WQCVGGfcPZkgic2Im2ru8JHFxct9Mgq8nw+vMVp3J/DrL/C9oRYPqrmL/e3ftO4eS9akz0eHbRDQlb5IlSDaZ65N5BdfHJpgFR/5y6fgwDhE8DmV4GqrQgONwnP05AFnzQBM=); Raid BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVU9oHFUY3+/N7Mw33zTN+Nqa6UNlOkjdLswyM9vVNJdMexIEWTx5ETM2G3dNya7ZRepFWqHgQSTkIomykW4XSlAXgkIMDYhom1bFHoriQmtbC3oQ/HPzIvJmul0NHjzY+js8vvf7zZv5ze/74NEDCBbY4EAOpqAKDTgB8BrAOwBnAfiORGVSHQdxzkDVYuIV0vGH7qh9yyQFf58hFftvA+n41QLYN3aSjhcWwP5eFt90R+23dNLx0y8s+7udpOKX3VHS8M1n5GEdv12AlF74ySIVly7Ldf2yRQpefZF0/Pl9sLd2kY7XTt1nX5MPdj4Ed591vpa7tQLLYHTid+P+4ZUurIL5eu3XB1fPwhu1U7UjmPiGCDbYQ55fKgZB4IeloFj0g1Ix8EphWCz6EsEWU2+yz3XaTSg0UvGDi+AiaaR6od+kMTKETtlcFjfLLhGS5gXjhZIUSCBpOQ2vtME1SKesFxRKTd4HPhU3jj1bb7Sc0A8f9QLfKwYTztFqPPd8Zdqpzzvx9HRl2nnuZadVrTjz9VbcqtXnnGYlnj9adXLNSsVpzNdbXiuem/UGspfKhRea9bkD4iWa5TXyeYH25HehxrO/6QwVaYhUvxA0B/Qn7O/0iGuScRrkf/baQPvzD6PKjdUBIfasMY6MG6f1AaNsqJkkAcSrZa4KNpHhJNKoem3gofD/9WvkZvHVMn9MlOgAf4Ts/P2ocHMDZJA6XlgBkToms68NuTsVP4TwT0cRP2tvP5pydyq+Q6T9yuK5DvBj23sUeP7B/7hHaUaLV57gviiQKxwadUfIvInSBuBHJ8s0sgZEKt5YfJIzK5v4U7F3aehWwY87wE1hDFswew/GSxdZUvB8mZ+5F8Mc0UER0t78GAI3l5lMQcHeJsj8iPnpMCvbZjxs3g6otzkMSMNLZVv5kW3BLyw8qWQS7I7WQCVGGfcPZkgic2Im2ru8JHFxct9Mgq8nw+vMVp3J/DrL/C9oRYPqrmL/e3ftO4eS9akz0eHbRDQlb5IlSDaZ65N5BdfHJpgFR/5y6fgwDhE8DmV4GqrQgONwnP05AFnzQBM=).

## Other builds of this spec

- [Protection — Tank](../research/raid/builds/prot-tank.md) (0/33/18) — [open the talent tree](https://talentsforever.com/paladin/60/-15310112513501031-50233300011-12)
- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (1/34/16) — [open the talent tree](https://talentsforever.com/paladin/60/01-25300132503501031-50033310001-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

