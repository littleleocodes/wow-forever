# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury — Dual-wield](../research/raid/builds/fury-dual-wield-open-raid.md)** (17/32/2) — [open the talent tree](https://talentsforever.com/warrior/60/32303013002-050530205122100231-2-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Fury — Raid](../research/raid/builds/fury-open-raid.md) (20/31/0, 938 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/32303013032-050530310122120231--12)

## How to play

**Setup, before the pull:** **Berserker Stance**: the simulator starts the fight in it, and the rotation below assumes it.

**Then press the first one that is ready**, top to bottom:

1. **Bloodthirst** until the last 30 seconds of the fight
2. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
3. **Reckless Swings**
4. **Whirlwind**
5. **Execute** when the target is below 20% health
6. **Hamstring** when **Bloodthirst** is more than 1.125 seconds from ready and **Whirlwind** is more than 2 seconds from ready
7. **Bloodrage** when you have less than 23 rage; no global cooldown, so press it alongside the others
8. **Heroic Strike** when you have 68+ rage; no global cooldown, so press it alongside the others

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Berserker Rage**: a cooldown, use it in the last 45 seconds of the fight (about 3 times a fight)
- **Recklessness**: once a fight, in the last 45 seconds of the fight
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fury in a raid fights in **Berserker Stance** with a two-handed weapon: **Bloodthirst** and **Whirlwind** on cooldown, **Execute** in the gaps below 20%, **Hamstring** in every other gap and **Heroic Strike** only at 90 rage or more. **Death Wish** waits for the last 45 seconds and **Recklessness** for the target's last 20%.

**Why it works**

- **Bloodthirst** (30 rage, 6-second cooldown) and **Whirlwind** (25 rage, 8-second cooldown with **Improved Whirlwind**) are your main attacks: press **Bloodthirst** the moment it is ready, and **Whirlwind** whenever **Bloodthirst** is more than 1.5 seconds away. **Whirlwind** needs **Berserker Stance**, the stance this list never leaves.
- Below 20%, **Execute** still comes after **Bloodthirst** and **Whirlwind**. It spends all your rage (600 damage plus 15 per extra rage point; 10 rage to cast with **Improved Execute**), so it takes the global cooldowns between them. A full raid gives you the rage for this order; the simulator's rotation for a warrior alone on a training dummy, short of rage, puts **Execute** first.
- **Death Wish** (+20% physical damage for 30 seconds, 3-minute cooldown) waits until 45 seconds are left and **Recklessness** (+100% crit chance for 15 seconds) until the target is below 20%, so both cover the execute phase; **Reckless Swings** (your next 4 melee attacks give 5 more rage) joins them in the last 34 seconds. Crits give double rage in Forever, so the **Recklessness** window also feeds bigger **Execute** hits. The simulator measured 0.7% more damage with **Death Wish** at 45 seconds than at 30, and in fights longer than about 3.5 minutes it presses it at the pull as well.
- **Hamstring** (10 rage) is your filler: cast it whenever nothing else is ready, about 56 times a fight. It is a cheap extra main-hand hit that can trigger on-hit effects such as a shaman's Windfury Totem; the simulator measured 6.8% more damage casting it freely than only above 80 rage with **Bloodthirst** and **Whirlwind** more than 1.5 seconds away.
- **Heroic Strike** is a rage dump, not a filler: queue it only at 90 rage or more, and not below 20%, where **Execute** wants every point. It replaces a white swing, and white swings are your steady rage (each gives rage in proportion to your weapon's speed, double on a crit), so an early one starves **Bloodthirst** and **Whirlwind**. The simulator measured 5.3% more damage after dropping its default line at 40 rage, and 0.2% more after adding this one at 90.
- **Bloodrage** (1-minute cooldown) goes whenever you are under 90 rage, about twice a fight.

**Caveats**

- The page's numbers assume a **Recklessness** in every fight and two Mighty Rage Potions (one at the pull, one when its cooldown is back). **Recklessness** has a 30-minute cooldown, so you will not have it on every boss: the simulator measured 13% more damage with it than without.
- With several targets, **Whirlwind** hits up to 4 of them, and above 40 rage the full list adds **Cleave**.
- The simulator ignores threat. **Heroic Strike** causes a high amount of threat, so it is the first thing to stop if you pull aggro. **Death Wish** and **Recklessness** also make you take 5% and 20% more damage.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- Alone or in a small group (fewer buffs, less rage), put **Execute** first below 20%, stack **Sunder Armor** to 5 yourself and use **Hamstring** only above 80 rage. That is the simulator's two-handed rotation for a warrior alone on a training dummy, where stacking **Sunder Armor** to 5 was worth 5.8%.
- If nobody in your group has **Battle Shout** up, keep it up yourself (3 minutes), and put one **Sunder Armor** on a boss that has none: the list leaves both out because the simulator's raid already had them.
- Before a boss's fear, press **Berserker Rage** (30-second cooldown, 10 seconds of fear immunity); **Death Wish** and **Recklessness** also make you immune. The simulator's boss never fears, so the list leaves it out.
- With a weapon in each hand (the page's dual-wield option), the simulator's dual-wield raid rotation differs: **Reckless Swings** on cooldown, **Heroic Strike** from 67.5 rage on a single target, **Hamstring** only when **Bloodthirst** is more than a second away and **Whirlwind** more than 2 seconds, **Recklessness** with **Death Wish** in the last 45 seconds, and no **Bloodthirst** in the last 30 seconds. **Whirlwind** hits with both weapons there.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arms | 17 | Improved Heroic Strike 3, Deflection 2, Improved Rend 3, Improved Tactical Mastery 3, Anger Management 1, Deep Wounds 3, Impale 2 |
| Fury | 32 | Cruelty 5, Unbridled Wrath 5, Furious Precision 3, Dual Wield Specialization 5, Reckless Swings 1, Improved Execute 2, Improved Berserker Rage 2, Death Wish 1, Improved Whirlwind 2, Flurry 3, Bloodthirst 1, Blood Craze 2 |
| Protection | 2 | Improved Bloodrage 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 937 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 908 | [17/32/2](https://talentsforever.com/warrior/60/32303013002-150530205121100231-2-12) |
| Phase 1 BiS | 883 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.1; Phase 1 BiS 61.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Spaulders of Containment](https://www.wowhead.com/forever/item=287022) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* | [Highlander's Chain Girdle](https://www.wowhead.com/forever/item=20043) · *sold by Samuel Hawke* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Furbolg Berserker's Boots](https://www.wowhead.com/forever/item=287033)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Furbolg Berserker's Boots](https://www.wowhead.com/forever/item=287033)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Main hand | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV21oHFUX3jMzu3P2pN1Obtq3k5v2ZQylbqduvDO7kzZVzLao+IFY9UeLCGbb3ZoV6YadiCmINEFB/KiViLQrkvgRDNEWrFVrkSBtLVVaSBECfmGIgoL9EcFfWqzc6W7WbvJDQrLeH8PZOefufZ7zPHOGoTUIBphgQRy6oBt6YD/AswDDAKMAbFmQVWR2M/DLq1AzgD9FEZzaZU43kIof9JGGX503SMfTI2BejJCOZ46vMH+MkY6fjYD5vQzOnDfMIZ00HJyQlb8dBblbx09ONZo/xEjDFy8ZpOGhCXn9cMIgFd95iHScOQrmJfkH3z7TKAMNB1+C1rhxNh//aQi2Tx6Anb93PQfKQL4E0bcy72W+2To0AmOgvJCfgYH8NgzgQxpOKlbSTYqkcJJCuAnHE15SuMJzXMcRwk06Cfecok0rfzaxp4HtzvQ89nChp9dyhduecJyE2LzF2t2d2ftILmsVilYmm81lrV37rN7unFUs9GZ684W9lp/LFHd3W3E/l7P2PF7cl8g+kShm8tlEpSJxtaLtUb+wdwNfS432Coww5a4Q1ylMalL4HCkS13DyJLA0v4WSzKEWuxlVFjsFDRSOh/HCg0wxwjxMKoFDrNWg2LFyanxHkNIrdVGuyzrj1QcYceQR0oyLLwN7bQ4/kRDu4vNL0Ua+IeCoVTmmPJ9W2qxMmwgp4jpOm+dLpDjaxf6PwHntLqec/3g5OzQf+o7FR+/QBn59LY6k8InZRhk9UoQ0JyV8rpFicraJe/NRdsUcyk4qoBwhDb8bBraWt9Ruahe+FAx/HQfm8eS/BSMtJHX+dGQh2/DNnxd0Wv/xBW8r1KrpJERq8dUM3I+Dg/exd+fxT9JZ/BNvpZvZFlrP1xGVUCfVuLLR4JW4/4ZqPJA3OBl2TEpbDEmcpDhe2VJP1udRXVUrW8rzt4RYT30etag804rhweWsiTdS+EtFQZBeiYfxozegMrzw/dFqfODyvex5qE931lGzvRrDrGEMZsezBESK8KvQt/JOctiNgZRhpk5DqDKkW3hzcDdSFTglKjSJ0IJ4GL8eBnakTm+e2+km1kFr7ZZaUsE8dtoc1/PJtP+HYUZjUGF4FbkbUI6reKGDDdTiFR0JdwnwtgQjRA3aF8w5123zZHfxykp2JwK/LSAk35Q1hIJqOWuJ22YNndmcJIanDwJ7Hepj+HaKs/WBJeAao5QHZYVl+6Y2r+wPxLOfAxuokz/m9Lt9U7Xf41Cfkb2D7mF3B0NUShdh0TGQOkmbRkt6OaQ1NsfINbJSSa/E1DCN0tyArwzDrMqr+Spa1kqEx0BaqNQUMCs1meovyjmYUdx+NRSslekxpYGipKMaB/EHtP6lROX90P496ebSYbm+6LxuT7AmO90pxdSsTvuEEvpPVm+6Ei3pWn9kyc7pCK73v53eWr6R7pJfIoch+BGa6rRVPLF62z8+WARshjTcAdthJ3RDD/RBn/L3AASxyWk=); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHFUU3jMzO3P2pN1Oblo7uWllDKVup268M7uTNlXMtqj4g1j1oUUEs+1uzYp0w07EFkTaoFD8aSsVsetP408xRBuwVK1F8hC11J9C+xLwD0MsKNiHCD5psXKnu1m7yYOEZL0Py9l77p37fef75gyXViCYYIENCeiBXuiDPQD7AAYBhgDYojCryOx64JeWoWYCf4p0nNhmTTaRhhcOAGk4MtZMBr5xzrTO62Tg5yeWWD/HScd9eevHuJz4xrSOGKTh168BGfj7CMjdBn4y1mz9FCcNR4/Kx7xw0SQNPzxnkorvPkQGfv9Ms3VRPmBqBGSg4aED0J4wTxcSF47A5vH9sPWPnmdBGSiUIfZ29v3sdxuPHIVhUJ4vTMFAYROG8CEDpxQ75aVESrgpIbyk8IWfEp7wXc9zhfBSbtI7o2iTyl8t7Glg27N9jz1c7Ou3PeF1Jl03KdZvsLf3Znc+ks/ZxZKdzeXyOXvbbru/N2+Xiv3Z/kJxpx3ks6XtvXYiyOftHY+XdidzTyRL2UIuWV2RvLKi49GguHMNX0nNzhLUmXJXhBsUJTUlAo6kJzQcPwUsw2+hFHOpzWlFlcXHoImiiSiefZApZpRHSSVwibWbFD9eSY1uCVNGdV2MG3Kd+fIDjDhynTTz/IvAXp3BTySFN//80rSWrwk5ajWOaT+gpQ6r0CZC0j3X7fADiRSHeti1CJzX73Ir+Y8Xs1dmQ981/+hdWsOvr8eREgExx6ygR9JJc9Mi4BopFmfruD8bZU/MoOymQ8o6afjDILCVvK1+U6cIpGD42ygwn6f+KxhpIanzp0fnsg3f+mVOp+09MedtxXo13aRIz7+aofvx0KH72Huz+Cflzv+Jt9LNbAOt5quIymiQal5ea/JqvPeGWjxQMDmZTlxKW4pInKS4fsVSTzbmVV1WL1vaDzZEWF9jXrWYPNOO48HFrIU3U/QrRUGQXklE8aM3odq88IOhWrz/0r3sOWhMdVZRq7Mco6xpGKbbswREighq0DfybnLZjaGUUaZOQqTapNt4azir1wROiypNIrQhEcVvB4Eda9CX53a6iXXRSqetnlTYj90O1/MDspxrMMpoGKoMryD3QsoJFc92sYF6vKIr6S0A3rawhahh+cI+53kdvqwuXl7K7kTgt4WE5JeyjlC4WvZa4o5VR2c6J4nhZweBvQ6NMXwnJdjq0BJwlVEqjbLKsnNdh1/xB+LpL4ANNMgfM+rdua5W71FoTMveQvewu8MmKqXTWWwYpE7SprGyUQlphcNRv0pWKhvVmJomUZob8KVBmFZ5OV9Gi9qJ8DhIC5VbQmblFkv9VTkDU4q3V42EY2lmWGmiGBmoJkD8Ce1/KzE5H9mzI9NaPizHl93X7QjHeLc3oVia3e2cVCL/y+jPVKMFHauPLdg5XeHv/e9kNlYmMj3yJnIYwj+RiW5HxZPLN/3rwiJgPWTgDtgMW6EX+mAX7FL+GQD1eskB).

**Points that do nothing for this spec:** **Improved Tactical Mastery** (3) only counts toward the points the tree needs before **Anger Management** and **Impale**.

## Other builds of this spec

- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (18/33/0, 905 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013102-050530305022110231--12)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 863 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/22303012-550530055021100231--12)
- [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 930 DPS in a full raid; fails the signature-spell check: core share 72% under 80% (melee, Bloodthirst, Whirlwind, Heroic Strike, Execute, Slam)) — [open the talent tree](https://talentsforever.com/warrior/60/05303013032-250500305022100231--12)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 916 DPS in a full raid; fails the signature-spell check: core share 71% under 80% (melee, Bloodthirst, Whirlwind, Heroic Strike, Execute, Slam)) — [open the talent tree](https://talentsforever.com/warrior/60/05303013031-553500050020100231--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-17 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

