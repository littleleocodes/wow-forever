# Protection Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Protection

> **Being checked:** The tank lane re-tunes, checks and races the tanks after the audit's D12 (2026-11-20). The builds and numbers on this page may change when it is done.

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (17/3/31) — [open the talent tree](https://talentsforever.com/warrior/60/35300103002-03-050530020330001351-12)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Setup, before the pull:** **Defensive Stance**: the simulator starts the fight in it, and the rotation below assumes it.

**Before the pull, then keep up all fight:** **Battle Shout**.

**Then press the first one that is ready**, top to bottom:

1. **Shield Block**; no global cooldown, so press it alongside the others
2. **Revenge** (rank 5) after you block, dodge or parry
3. **Bloodrage** when you have less than 90 rage; no global cooldown, so press it alongside the others
4. **Shield Slam**
5. **Sunder Armor**: stack it to 5 on the target
6. **Heroic Strike** (rank 8) when you have 34+ rage; no global cooldown, so press it alongside the others
7. **Rend**: keep it on the target
8. **Sunder Armor**

**Sunder Armor** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Shield Wall**: when a hit could kill you: much less damage taken for a few seconds, on a long cooldown
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Protection tanks in **Defensive Stance** with a shield: **Shield Block** every time it is ready, **Revenge** whenever it lights up, **Shield Slam** on cooldown, **Sunder Armor** in the gaps and **Heroic Strike** whenever 34 rage is spare. **Thunder Clap** and **Demoralizing Shout** are not on the list, and **Shield Wall** is yours to time.

**Why it works**

- **Shield Block** (10 rage, 5-second cooldown) leads the list: 75% more block chance for 7 seconds or 2 blocks, and each block gives 5 rage with **Shield Specialization** and opens **Revenge**. The simulator presses it about 35 times a fight; adding it measured 8.4% more tank value, and pressing it without waiting for 40 rage 2.2% more.
- **Revenge** is your first attack: 5 rage (2 with **Focused Rage**) for high threat, usable only for 5 seconds after you block, dodge or parry, so a missed window is lost. It is two fifths of your threat in the simulator, which measured it slightly better above **Shield Slam**.
- **Shield Slam** (20 rage, 17 with **Focused Rage**, 6-second cooldown) is your hardest hit, made stronger by your block value, and causes very high threat; the simulator casts it about 26 times a fight, almost every time it is ready.
- **Heroic Strike** is about a fifth of your threat in the simulator. It goes on your next swing, off the global cooldown, so you can queue it on top of everything else; waiting for 34 rage keeps enough for **Shield Slam** and **Revenge**.
- **Sunder Armor** (stacked to 5, then as the filler) takes the remaining global cooldowns for 8% of your threat, and **Rend** (kept on the boss) adds a little, worth 0.5% of tank value in the simulator. Use **Bloodrage** whenever you are under 90 rage, about 3 times a fight.
- **Shield Wall** (60% less damage for 12 seconds, 15-minute cooldown) is at the top of the simulator's full list only because its boss hits the same all fight, so any use saves the same damage there (3.2% of tank value). In a real fight, save it for the dangerous moment.

**Caveats**

- The list has no **Thunder Clap** or **Demoralizing Shout** because the simulator's raid already has those debuffs on the boss (a druid's Demoralizing Roar stands in for the shout), so casting them only cost rage there; dropping **Thunder Clap** measured 0.8% better. In a real raid they are usually yours.
- **Shield Bash** is your interrupt (12-second cooldown). Dropping it as a filler measured 0.4% better, so the list leaves it out: keep it ready for a spell the boss must not finish.
- The simulator's boss only melees you: it does not model adds, tank swaps or damage spikes, so it never needs a **Taunt**.

**When to change it**

- The simulator's raid already keeps 5 **Sunder Armor** stacks on the boss, so its list casts it for threat. When the stacks are yours, build them to 5 on the pull and refresh them before their 30 seconds run out.
- Keep **Thunder Clap** (bosses attack 20% slower in Forever, 30 seconds) and **Demoralizing Shout** (204 less attack power, 45 seconds) up unless another warrior or a druid's Demoralizing Roar covers them.
- Press **Shield Wall** for the worst moments: an enrage, a healer down, your health low.
- Adds: **Thunder Clap** hits up to 4 targets, **Challenging Shout** (10-minute cooldown) turns everything within 10 yards onto you for 6 seconds, and **Taunt** (8-second cooldown in Forever) takes back a single target.

*This guide was written for the rotation of 2026-11-09; the list above was re-tuned since, so follow the list where the two differ.*

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arms | 17 | Improved Heroic Strike 3, Deflection 5, Improved Rend 3, Improved Overpower 1, Deep Wounds 3, Impale 2 |
| Fury | 3 | Cruelty 3 |
| Protection | 31 | Shield Specialization 5, Anticipation 5, Improved Revenge 3, Master of Defense 2, Defiance 3, Improved Sunder Armor 3, Concussion Blow 1, Focused Rage 3, Bastion 5, Shield Slam 1 |

## The numbers

Tank value 1.010 (threat and damage taken under a boss, relative to our reference tank build).

**How this pick was checked:** a full search on 2026-10-28 (the talent search that found this build).

**The gear** (average item level: Pre-BiS 62.2; Raid BiS 61.3; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Raid BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Talisman of Evasion](https://www.wowhead.com/forever/item=13177) · *War Master Voone, Blackrock Spire* | [Talisman of Evasion](https://www.wowhead.com/forever/item=13177) · *War Master Voone, Blackrock Spire* |
| Shoulders | [Highlander's Plate Spaulders](https://www.wowhead.com/forever/item=20057) · *sold by Samuel Hawke* | [Highlander's Plate Spaulders](https://www.wowhead.com/forever/item=20057) · *sold by Samuel Hawke* |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Warrior's Embrace](https://www.wowhead.com/forever/item=10845) · *Avatar of Hakkar, The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Warrior's Embrace](https://www.wowhead.com/forever/item=10845) · *Avatar of Hakkar, The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Sentinel's Wristguards](https://www.wowhead.com/forever/item=250582) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* |
| Legs | [Legplates of Valor](https://www.wowhead.com/forever/item=16732) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Warmaster Legguards](https://www.wowhead.com/forever/item=12935) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Grimy Metal Boots](https://www.wowhead.com/forever/item=18521) · *King Gordok, Dire Maul*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Grimy Metal Boots](https://www.wowhead.com/forever/item=18521) · *King Gordok, Dire Maul*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Finger | [Watcher's Signet of Vigilance](https://www.wowhead.com/forever/item=275980) | [Watcher's Signet of Vigilance](https://www.wowhead.com/forever/item=275980) |
| Trinket | [The Lion Horn of Stormwind](https://www.wowhead.com/forever/item=14557) · *world drop* | [Arena Grand Master](https://www.wowhead.com/forever/item=19024) · *quest: Arena Grandmaster* |
| Trinket | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* | [The Lion Horn of Stormwind](https://www.wowhead.com/forever/item=14557) · *world drop* |
| Main hand | [Greenhammer](https://www.wowhead.com/forever/item=279261) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Instructor Malicia, Scholomance* | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Instructor Malicia, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzEVEFoE10Qzrzd7E4mP2G7f+Df7l9hm0OJgS0vu0SbXpL2okcRD7IXu21SEytJTPZQQaGKgR56qHixVaiggogieCilRxFpwWL1IFRsrVrQQw96EKoHld22UOjV1u+w+973zWO+mYGhNgQFNDAgCX1QghqMAIwC3AK4B6D+E6jMV7tAn5eRKaBfIAlX+7W1KAn4fZBEXLoJJOOLcdDex0jC5RPaR/8/WtRuyCTj0+eK9i5GIl5bVEjGt5fBfyvj0jhs8tcXFRJxbF0hAZfPkYgzQeBys0Vbj5GMK80WbcUP3LgKiTblWTm5NgWTELntPnDf9EzdhfsgjZW/HmiWezEwDHmYZe12xuY8zW3OLZPbJs9wn7C4bXPO03YmPcfED+xVmOIU0WUKJyWcchIyhUkw0w11SO1za2dPVWueYXHrkJnmptXVbQyU3MrpYsGo1g23UCgWjP7zhlcqGvWq53rlasVoFN36QMlINopFo1aveqbnVobMbdnclDvPNKqVg7qsh0nAZnxXMp41reyeJPskqaLOukMq6pIuEsMjalTfrD+MLx314u6y05k/7KSVlFQMBZXVQ7pEIrEsD7z9iquko0/ht1lQk3oH/Z9qRUGNPYFoYHDBUZkS9oMJMlumFxz1CuyDa4P+TbWgFLiOkExh2+48nNEjJBuQRHzkqMP7MMU4RRMRki2/X9OO3wmcdnaMcMHRhM9sDr6wwgaDS0IoQDz/mEUpQjKyJPAfkPjJIj4fGhnMt05O+JjPtQ8GeJ2zVpkmGrnUDAv9FXj57dOeouPhnuXJBt/jd/I9W0S+z1+rExBcQqu5lIAz/3UzBXp3bGAOXZCHo3AMTkIJajAMw+z3AAGbJkw=); Raid BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzEVEFIFH8U3veb2Zm3b//sf5wWGieDcQ+yLYz8doYt18uuXuoY0SHmkqO7tpuxu+3uwaDAIKmDB6OCtMCghIgi6CDiMSIUkqyDYKBtJdTBQx0C61Axo4LgNe07PGa+7828770Hj1oQFNDAgDj0QAEqMARwDeAewEMA9T9fZZ7aAfqcjEwB/SJJ2OjVVsMk4I9+EnHpLpCMr0dB+xAhCZdPap8iJOPi5P/aHZlkfPFK0d5HSMQbCwpJeDXvfSvj0ihs0LcXFBJxZM2LCzeBBFw+TzI2boG25v1oZbhJW/ES169DrEV5WYyvTsA4hO67j913XROT8AikkeK3g8PFbvQNQxZmWKudsjlPcptzy+S2yVPcIyxu25zzpJ1KzjLxI3sbpCiFdJmCcQknnJhMQRLMZE0dUHvcyrnT5UrdsLh12Exy0+roNPoKbulMPmeUq4aby+VzRu8Fo17IG9Vy3a0XyyWjlnerfQUjXsvnjUq1XDfrbmnA3JLNDbn9bK1cOqTLepAEHI7uKMbTppXelWKfJVXUWWdARV3SRWJ4VA3rG/0H8Y2jXtrZdjL1l500k5KIoKCyakCXSCSW5r6331GVdPQo/D4DalxvowOJZhTUyHMI+wbnHZUpQS+ZILVpet5Rr8AeuDZoX6IJJd91iGQK2nb7kZQeItmAOOJTRx3cgy1GKRwLkWx585pyvEnglLNthfOOJnxhs/CV5dYZXBYCPqLZZyxMIZKRxYH/hNgvFvL4wFB/tnl8zMNcprXfx2LGajBNNDKJaRb4J6hnt552FW1Pdq1O2o8nHmS7Nolsj3dWx8B/CTQyCQGn93cyBbq3XWAOHZCFY3AcTkEBKjAIg+zPAPBdJkY=).

## Other builds of this spec

- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (8/5/38) — [open the talent tree](https://talentsforever.com/warrior/60/35-05-250530022331201351-12)
- [Protection — Raid Tank](../research/raid/builds/prot-raid-tank.md) (12/5/34) — [open the talent tree](https://talentsforever.com/warrior/60/3500301-05-150533020311001351-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-21 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

