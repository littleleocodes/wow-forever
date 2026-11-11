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
- **Lay on Hands**: when you are about to die: a full heal on a long cooldown that empties your mana
- **Templar's Bulwark**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
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

Tank value 1.022 (threat and damage taken under a boss, relative to our reference tank build).

**The gear** (average item level: Pre-BiS 61.8; Phase 1 BiS 62.4; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Talisman of Evasion](https://www.wowhead.com/forever/item=13177) · *War Master Voone, Blackrock Spire* | [Talisman of Evasion](https://www.wowhead.com/forever/item=13177) · *War Master Voone, Blackrock Spire* |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Warrior's Embrace](https://www.wowhead.com/forever/item=10845) · *Avatar of Hakkar, The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Warrior's Embrace](https://www.wowhead.com/forever/item=10845) · *Avatar of Hakkar, The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Warder's Waistguard](https://www.wowhead.com/forever/item=250573) · *Blacksmithing* | [Warder's Waistguard](https://www.wowhead.com/forever/item=250573) · *Blacksmithing* |
| Legs | [Legplates of the Eternal Guardian](https://www.wowhead.com/forever/item=11927) · *Chest of The Seven, Blackrock Depths*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Legplates of the Eternal Guardian](https://www.wowhead.com/forever/item=11927) · *Chest of The Seven, Blackrock Depths*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Grimy Metal Boots](https://www.wowhead.com/forever/item=18521) · *King Gordok, Dire Maul*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Grimy Metal Boots](https://www.wowhead.com/forever/item=18521) · *King Gordok, Dire Maul*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVU9oHFUY3+/N7Mw33zTJ+Nqa6UNlOkjdLswyM9vVNJdMexIEWcSDB8WMzcZdU7JLdpF6EFqh4EEk5KKNkki3iyWoC0EhRgNFtKZVsYciuNDa1oIeBP/cvIi8mW5XgwcPNv4Oj/d+v/lmfvP7Pnh0D4IFNjiQg0moQgOOA7wM8BbAWQC+I1GZVMdAfGSgajHxIun4Q2fEvmmSgr9Pk4q9N4F0/Hoe7OvDpOGVx+3vh0nHcx2w39BJx0+/tOzvhknFrzojpOFrT8laHb+dh5Se/8kiFV+/JNe1SxYp+PaTpOPP74G9uZN0vHryLvuqfLD9Abh7rfO13M1lWASjHb8T9w4td2AFzFdqv967chZerZ2sHcbENkSwzu7z/FIxCAI/LAXFoh+UioFXCsNi0ZcINpl6g32h0y5CoZGK718AF0kj1Qv9Jo2SIXTK5rK4UXaJkDQvGCuUpEACSctpeHkJXIN0ynpBodTkPeCTcePo0/VGywn98EEv8L1iMO4cqcazz1amnPqcE09NVaacZ15wWtWKM1dvxa1afdZpVuK5I1Un16xUnMZcveW14tkZry97qVx4rlmf3S+epxleI58XaHd+J2o8+5vOUJGGSPULQbNPf8L+Tg+5JhmnQf5ndwloX/5+VLmx0ifE7lXGkXHjtN5nlHU1kySAeKXMVcHGM5xEGlV3CXgo/H/9GnlYeKnMHxIl2s8fIDt/NyrcXAcZpI6fL4NIHZPZ0wbc7R0/iPBPpYifLW0tTbnbO75DpP3K4sdt4Ee39ijw/AP/cY/SjBYuP8J9USBXODTiDpF5A6UNwA9PlGloFYhUvL7wKGdWNvGnYvfiwK2C59rATWEMWjCzDeOliywpeL7Mz2zHMEd0QIS0Jz+KwM1FJlNQsLsBMj9ifjrMypYZD5u3AupuDALS8GLZVn5km/ALC08omQS7olVQiVHG/YMZksgcn472LJ6SuDCxdzrBNxPhNWarzkR+jWX+F7Si/u6OYt+7d+w7B5P1sTPRoVtENCkvklOQHDLXJvIKro2OMwsO/+XO8WEMIngYyvAEVKEBx+AY+3MAlmg/eA==); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVU9oHFUY3+/N25lvvmmS9bU104fKdJC6XZhlZraraS6Z9iQIsogHL2LGZuOuKdklu0i9SCsWPIiEiEijJNI0UIK6EBRiaKCI1rRV9FAEF1rbWtCD4J+bF5E30+1q8ODBxt9h+N7vN+/Nb37fB4/uQ8iBDQ7kYRxq0ITjAK8CvAtwFkDsSFSm1BGQ50zkOSZfIgN/WB6yb1mk4e+TxLH7DpCBX82CfWOQdLz6pP39IBl4fhnstw0y8NMvcvZ3g8Txy+Uh0vGtp9VeA7+dhZSe/SlHHC+/CcRx7WtVv/KGOvHnD8De3EkGXjt5j31Nvbn0Ebh7cxfq+VuLMA/mUvxe3D20uAwrYL1W//X+lbPwev1k/TAmviGCdfaA55dLQRD4YTkolfygXAq8chiWSr5CsMn4TXbZoF2EUieOH14EF0kn7oV+i4bJlAZl81ncqLhESLoXjBTLSiCJpOd1vLIArkkGZb2gWG6JLojxuHn0mUaz7YR++LAX+F4pGHWO1OLp56oTTmPGiScmqhPOsy867VrVmWm043a9Me20qvHMkZqTb1WrTnOm0fba8fSU15O9VC4+32pM75cv0JSoky+KtLuwE3WR/c1gqClDxP1i0OrRn7C/0wOuReZpUP/ZWQDaV3gQuTBXeoTcvcoEMmGeNnqMts4zSQKIVyuCSzaaESTTqDoLIELp/+tj1GLu5Yp4RJZpv3iI7MK9qAlrHVSQBn6+CDJ1TFZX73N3KnEQ4Z+2In62sHVryt2pxA6Z9iuL55ZAHN3ao8DzD/zHPUozmrvymPBlkVzp0JA7QNZNVDYAPz5RoYFVIOJ4Y+5xwXLZxB/HzqW+Ww3PL4GwpNlvwdQ2jJchs6ThhYo4sx3DHNEBGdKewjCCsOaZSkHDzgao/Ij56TBrW2Y8bN0OqLPRD0jHSxVb+5Ftwi8sPKFlEuyKVoETo4z7BzMVkTk+Ge2ZP6VwcWzvZIJvxsLrzObOWGGNZf4XtKNedVex7/279p2DyfOJM9Gh20Q0rm6SU5AsMtfHChquDY+yHBz+y6XjwwhE8ChU4CmoQROOwTH25wC+jj95).

## Other builds of this spec

- [Protection — Tank](../research/raid/builds/prot-tank.md) (0/33/18) — [open the talent tree](https://talentsforever.com/paladin/60/-15310112513501031-50233300011-12)
- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (1/34/16) — [open the talent tree](https://talentsforever.com/paladin/60/01-25300132503501031-50033310001-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

