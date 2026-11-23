# Protection Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (0/35/16) — [open the talent tree](https://talentsforever.com/paladin/60/-05311102513301531-52233000001-12)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Righteous Fury**, **Retribution Aura**, **Seal of the Crusader**.

**Keep up all fight:** **Seal of Fury**, **Righteous Fury**, **Retribution Aura**.

**Then press the first one that is ready**, top to bottom:

1. **Holy Strike** when Judgement is on cooldown
2. **Judgement**; no global cooldown, so press it alongside the others
3. **Consecration** when you have at least 25% mana
4. **Holy Shield**
5. **Hammer of Wrath** when the target is below 20% health

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Templar's Bulwark**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Lay on Hands**: when you are about to die: a full heal on a long cooldown that empties your mana
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Most of your threat is Holy damage: **Righteous Fury** adds a third to all your threat and 90% more to your Holy threat. Keep **Seal of Fury** and **Holy Shield** up, judge on cooldown, and press **Holy Strike** and **Consecration** (while you have a quarter of your mana or more) whenever they are ready; **Templar's Bulwark** and **Lay on Hands** are your big defensive buttons.

**Why it works**

- Before the pull: **Righteous Fury** (30 minutes; **Improved Righteous Fury** and **Iron Creed** only work while it is up), **Retribution Aura** and **Seal of the Crusader**. Your first **Judgement** judges the Crusader seal: the boss takes up to 161 more Holy damage, and your melee hits keep that judgement up all fight. Then **Seal of Fury** goes up and stays.
- **Seal of Fury** (30 seconds) adds 35 Holy damage to every swing, and while you hold a shield each swing also gives you an absorb of half of that damage. Renew it just before it runs out (about 6 times a fight). The list starts from the official simulator's own Protection rotation (since 2026-10-31), which tanks with this seal.
- Press **Judgement** (10-second cooldown) whenever it is ready, and **Swift Judgement**, a second **Judgement** on its own 1-minute cooldown, whenever that is: both are off the global cooldown and do not use up the seal in Forever. Each judges **Seal of Fury** for 153 to 167 Holy damage and a 3-second taunt: about 25 judgements a fight in the simulator, the two together.
- **Holy Shield** (10-second cooldown, 4 charges): 30% more block for 10 seconds, and every block deals 221 Holy damage with 20% extra threat and can trigger **Redoubt** and **Shield Specialization**'s mana. Forever's rank 4 is not in the official rotation; adding it measured 2.3-2.4% more tank value.
- **Holy Strike** and **Consecration** fill the rest. **Shieldsworn** takes 4 seconds off **Holy Strike**'s cooldown, so it comes back every 6 seconds (29 times a fight in the simulator). It also strikes with your shield: while **Holy Shield** is up, each one that lands deals its damage without spending a charge, it can return **Shield Specialization**'s mana, and for 6 seconds after it you can block spells. It goes right after **Judgement** when both are ready (0.4-0.6% more tank value with it at the top of the list), and with **Iron Creed** it makes up to 30% more threat and cuts your damage taken by up to 6% for 6 seconds (rank 3). **Consecration** threatens everything standing in it; the list keeps it for when you have a quarter of your mana or more (the re-tune of 2026-11-22: 0.3-0.5% more tank value).
- **Hammer of Wrath** (474 to 522 Holy damage, only below 20% of the boss's health) goes right after a white swing: 0.8% more tank value.
- **Templar's Bulwark** absorbs damage equal to your maximum health for 8 seconds, off the global cooldown; the simulator uses it as soon as it is ready, which its 3-minute fight allows once, at the pull (5-minute cooldown). It applies Forbearance for a minute, which locks you out of **Divine Protection**, **Divine Shield** and **Blessing of Protection**.
- **Lay on Hands** is near the end of the list with no health condition: in the simulator's fights nobody heals you, and using it whenever nothing above is ready measured 1.9-2.0% more tank value. It heals you for your maximum health but drains all your mana, and its cooldown is 20 minutes: in a raid with healers, keep it for when you are about to die.

**Caveats**

- Every **Judgement** of **Seal of Fury** taunts for 3 seconds. As the boss's main tank that costs nothing; as the second tank, it pulls the boss off the main tank. While another tank holds the boss, switch to **Seal of Righteousness** (its **Judgement** deals 170 to 186 Holy damage and does not taunt) or do not judge.
- **Seal of Righteousness** is in the simulator's list but switched off: the official rotation tanks with **Seal of Fury**, and turning the other seal on was among the rotation searches' tries and was never kept.
- Mana: you run dry for about a second of each 3-minute fight in the simulator. **Consecration** is the expensive button (565 mana); blocks give mana back through **Shield Specialization** and judgements through **Sanctified Judgement**.
- The simulator measures one boss. **Consecration** and **Holy Shield** work on everything that hits you; **Holy Strike** and **Judgement** only on your target.

**When to change it**

- To taunt (a tank swap, a loose add), judge it: with **Seal of Fury** up every **Judgement** taunts for 3 seconds, and **Swift Judgement** is a second one when **Judgement** is on cooldown.
- Hold **Templar's Bulwark** for a known damage spike or a healer death when the fight has one: the simulator spends it at the pull only because its fight fits a single use.
- Undead or Demons: **Exorcism** is in the list for them (the simulator's boss is an Elemental, so it never casts it), and **Holy Wrath** (a 2-second cast) hits and stuns every Undead and Demon within 20 yards. Neither was measured.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Protection | 35 | Redoubt 5, Precision 3, Guardian's Favor 1, Sacred Duty 1, Templar's Bulwark 1, Shield Specialization 2, Toughness 5, Swift Judgement 1, Improved Righteous Fury 3, Anticipation 3, Holy Shield 1, Reckoning 5, Iron Creed 3, Shieldsworn 1 |
| Retribution | 16 | Deflection 5, Benediction 2, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Sacred Arbiter 1 |

## The numbers

Tank value 1.017 (threat and damage taken under a boss, relative to our reference tank build).

**How this pick was checked:** a short check on 2026-11-22 (every one-move and chain-move neighbour raced in a full raid, two rounds; nothing better). A full search, talents and rotation in turns until stable, follows in the optimality pass.

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

*These sets were chosen before the tanks stood in front of the boss (2026-11-20), so they likely undervalue Expertise; they are being made again.*

*Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and Onyxia's Lair. These sets still count raid gear (Pre-BiS: Enchant Weapon - Spell Power (Molten Core); Raid BiS: Enchant Weapon - Spell Power (Molten Core)). The gear lists are being made again.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVU9oHFUY3+/N7My33zTd6Wtrpg8r00HrdmGWmdmOprlk2pMgyOLJi5hpd+OuKdk1u0i9SCMUPIiEXCRREmkaKEFdCBZiMKCibVoUeyiKC61tLehB8M9JLyJvptto68FDW3+Hx/d+3347v/f73sejBxFMsMCGAoxCHVpwHOA1gHcATgPwLUmWyewQiDOEqsnEK6TjD0t564ZBCv4xRir23gbS8atpsK5tJR3PTYP1vQy+Wcpbb+mk42dfmNZ3W0nFL5fypOGbz8piHb+dhpSe/skkFWcvynX1okkKXn6RdPz5fbA2tpOOV05ss67IHy6eAWePebZRuLEAc5BbjN+NewcXlmAZjNcbv+5ePg1vNE40DmGiGyJYYw+5Xlj2fd8LQr9c9vyw7LthEJTLnoS/wdTr7BOkHYRCIxU/OA8OkkaqG3htGqSc0ClbyOJ6xSFC0lx/qBTKBAkkraDhpXlwcqRT1vVLYZv3gI/GraPPNVsdO/CCx1zfc8v+sH2kHk88X6vazUk7rlZrVfvwy3anXrMnm52402hO2O1aPHmkbhfatZrdmmx23E48Me72026aLr3Qbk7sEy/ROG+Qx0u0s7gdNZ79TWeoSEGkeiW/3ac/Zf+kBxyDcidBnrM7D7S3+DCqPLfcJ8TOFcaR8dxJvc8oa2omcQDxcoWrgg1nOInUqu488EB4//lv5Gbm1Qp/XIS0jz9KVvEBVLixBtJIHc8tgEgVk9HTNrlbET+A8G+liJ/P316acrciPnVHW3w3CO5yW3bTtmIeNc4OJ56REoSPyKYUsvjRIvCjd0rw9t9lCWlnZi49yT1RIkfYlHcGyLiOUgbgh1MVGlgBIhWvzTzFmZlN9KnYvQB8i0jvtIIfLwI3RG6z8eP34VLrIksKnq3wU/djhCLaLwLaVRxE4MYcS8/dXQfpHzEvHSHltskK2jcN6q5vGqThhYql/Mg24BdW/Z3BlJJJsCNaAZUYZZw/WU4SmeNj0a65WYnzI3vGEnw9ElxllmqPFFdZ5n9BJ+pH9xR737tn3zmQrE+fig7eJKJR+YTNQrLJXB0pKrg6OMxMOPS3186DIYjgCajAM1CHFhyDY+yvAQDDY2UV); Raid BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVU9oHFUY3+/N7My33zTd6Wtrpg8r00HrdmGWmdmOprlk2pMgyOLJi5hpd+OuKdk1u0i9SCMUPIiEXCRREmkaKEFdCBZiMKCibVoUeyiKC61tLehB8M9JLyJvptto68FDW3+Hx/d+3347v/f73sejBxFMsMCGAoxCHVpwHOA1gHcATgPwLUmWyewQiDOEqsnEK6TjD0t564ZBCv4xRir23gbS8atpsK5tJR3PTYP1vQy+Wcpbb+mk42dfmNZ3W0nFL5fypOGbz8piHb+dhpSe/skkFWcvynX1okkKXn6RdPz5fbA2tpOOV05ss67IHy6eAWePebZRuLEAc5BbjN+NewcXlmAZjNcbv+5ePg1vNE40DmGiGyJYYw+5Xlj2fd8LQr9c9vyw7LthEJTLnoS/wdTr7BOkHYRCIxU/OA8OkkaqG3htGqSc0ClbyOJ6xSFC0lx/qBTKBAkkraDhpXlwcqRT1vVLYZv3gI/GraPPNVsdO/CCx1zfc8v+sH2kHk88X6vazUk7rlZrVfvwy3anXrMnm52402hO2O1aPHmkbhfatZrdmmx23E48Me72026aLr3Qbk7sEy/ROG+Qx0u0s7gdNZ79TWeoSEGkeiW/3ac/Zf+kBxyDcidBnrM7D7S3+DCqPLfcJ8TOFcaR8dxJvc8oa2omcQDxcoWrgg1nOInUqu488EB4//lv5Gbm1Qp/XIS0jz9KVvEBVLixBtJIHc8tgEgVk9HTNrlbET+A8G+liJ/P316acrciPnVHW3w3CO5yW3bTtmIeNc4OJ56REoSPyKYUsvjRIvCjd0rw9t9lCWlnZi49yT1RIkfYlHcGyLiOUgbgh1MVGlgBIhWvzTzFmZlN9KnYvQB8i0jvtIIfLwI3RG6z8eP34VLrIksKnq3wU/djhCLaLwLaVRxE4MYcS8/dXQfpHzEvHSHltskK2jcN6q5vGqThhYql/Mg24BdW/Z3BlJJJsCNaAZUYZZw/WU4SmeNj0a65WYnzI3vGEnw9ElxllmqPFFdZ5n9BJ+pH9xR737tn3zmQrE+fig7eJKJR+YTNQrLJXB0pKrg6OMxMOPS3186DIYjgCajAM1CHFhyDY+yvAQDDY2UV).

## Other builds of this spec

- [Protection — Tank](../research/raid/builds/prot-tank.md) (0/33/18) — [open the talent tree](https://talentsforever.com/paladin/60/-15310112513501031-50233300011-12)
- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (1/34/16) — [open the talent tree](https://talentsforever.com/paladin/60/01-25300132503501031-50033310001-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-23 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows. Windfury Totem's buff changed in client 1.60.1.71037 and the raid simulator used here predates it: full-raid numbers of melee builds assume the old totem.*

