# Protection Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (17/3/31) — [open the talent tree](https://talentsforever.com/warrior/60/35300103002-03-050530020330001351-12)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Setup, before the pull:** **Defensive Stance**: the simulator starts the fight in it, and the rotation below assumes it.

**Before the pull, then keep up all fight:** **Battle Shout**.

**Then press the first one that is ready**, top to bottom:

1. **Heroic Strike** when you have 40+ rage; no global cooldown, so press it alongside the others
2. **Shield Block**; no global cooldown, so press it alongside the others
3. **Revenge** after you block, dodge or parry
4. **Bloodrage** when you have less than 90 rage; no global cooldown, so press it alongside the others
5. **Shield Slam**
6. **Sunder Armor**: stack it to 5 on the target
7. **Heroic Strike** when you have 34+ rage; no global cooldown, so press it alongside the others
8. **Sunder Armor**

**Sunder Armor** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Rend**: part of the rotation (about 10 times a fight)
- **Shield Wall**: when a hit could kill you: much less damage taken for a few seconds, on a long cooldown
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Protection tanks in **Defensive Stance** with a shield: **Shield Block** every time it is ready, **Revenge** right after it whenever it lights up, **Shield Slam** on cooldown, **Sunder Armor** in the gaps and **Heroic Strike** queued with the rage left over: at 40 rage, or at 34 when **Shield Block**, **Revenge** and **Shield Slam** are not ready. **Thunder Clap** and **Demoralizing Shout** are not on the list, and **Shield Wall** is yours to time.

**Why it works**

- **Shield Block** (10 rage, 5-second cooldown) comes first among your presses: 75% more block chance for 7 seconds or 2 blocks, and each block gives 5 rage with **Shield Specialization** and opens **Revenge**. The simulator presses it about 35 times a fight; adding it measured 8.4% more tank value, and pressing it without waiting for 40 rage 2.2% more.
- **Revenge** is your first attack: 5 rage (2 with **Focused Rage**) for high threat, usable only for 5 seconds after you block, dodge or parry, so a missed window is lost. It is over a third of your threat in the simulator, which measured it better right after **Shield Block** and above **Shield Slam**.
- **Shield Slam** (20 rage, 17 with **Focused Rage**, 6-second cooldown) is your hardest hit, made stronger by your block value, and causes very high threat; the simulator casts it about 26 times a fight, almost every time it is ready.
- **Heroic Strike** is about a fifth of your threat in the simulator. It goes on your next swing, off the global cooldown, so you can queue it on top of everything else; queueing it at 40 rage, or at 34 only while **Shield Block**, **Revenge** and **Shield Slam** are not ready, keeps enough rage for them. The re-tune of 2026-11-21 added the 40-rage rule above the others, and the re-tune on trainer ranks of 2026-11-22 kept it (no change measured ahead of it); once the boss is below 20% of its health, only the 34-rage one is left.
- **Sunder Armor** (stacked to 5, then as the filler) takes the remaining global cooldowns for 7% of your threat, and **Rend** (kept on the boss) adds a little, worth 0.5% of tank value in the simulator. Use **Bloodrage** whenever you are under 90 rage, about 3 times a fight.
- **Shield Wall** (60% less damage for 12 seconds, 15-minute cooldown) is near the top of the simulator's full list only because its boss hits the same all fight, so any use saves the same damage there (3.2% of tank value). In a real fight, save it for the dangerous moment.

**Caveats**

- The list has no **Thunder Clap** or **Demoralizing Shout** because the simulator's raid already has those debuffs on the boss (a druid's Demoralizing Roar stands in for the shout), so casting them only cost rage there; dropping **Thunder Clap** measured 0.8% better. In a real raid they are usually yours.
- **Shield Bash** is your interrupt (12-second cooldown). Dropping it as a filler measured 0.4% better, so the list leaves it out: keep it ready for a spell the boss must not finish.
- The simulator's boss only melees you: it does not model adds, tank swaps or damage spikes, so it never needs a **Taunt**.

**When to change it**

- The simulator's raid already keeps 5 **Sunder Armor** stacks on the boss, so its list casts it for threat. When the stacks are yours, build them to 5 on the pull and refresh them before their 30 seconds run out.
- Keep **Thunder Clap** (bosses attack 20% slower in Forever, 30 seconds) and **Demoralizing Shout** (204 less attack power, 45 seconds) up unless another warrior or a druid's Demoralizing Roar covers them.
- Press **Shield Wall** for the worst moments: an enrage, a healer down, your health low.
- Adds: **Thunder Clap** hits up to 4 targets, **Challenging Shout** (10-minute cooldown) turns everything within 10 yards onto you for 6 seconds, and **Taunt** (8-second cooldown in Forever) takes back a single target.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arms | 17 | Improved Heroic Strike 3, Deflection 5, Improved Rend 3, Improved Overpower 1, Deep Wounds 3, Impale 2 |
| Fury | 3 | Cruelty 3 |
| Protection | 31 | Shield Specialization 5, Anticipation 5, Improved Revenge 3, Master of Defense 2, Defiance 3, Improved Sunder Armor 3, Concussion Blow 1, Focused Rage 3, Bastion 5, Shield Slam 1 |

## The numbers

Tank value 1.012 (threat and damage taken under a boss, relative to our reference tank build).

**How this pick was checked:** a short check on 2026-11-22 (every one-move and chain-move neighbour raced in a full raid, two rounds; nothing better). A full search, talents and rotation in turns until stable, follows in the optimality pass.

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

*These sets were chosen before the tanks stood in front of the boss (2026-11-20), so they likely undervalue Expertise; they are being made again.*

*Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and Onyxia's Lair. These sets still count raid gear (Raid BiS: Blackguard (Molten Core)). The gear lists are being made again.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzEVUFoE1kYzv9mMvPmzxKmbwM7ne3CNIeSDUz3zcxmtykLSXvZPS7LHpZcttMm3WS7m2STHLqgUMVADz1UvNgqtKCCiCJ4KKVHEalitV6Uiq21FvTQgx6E6kHlTVuVem3rd0hmvu8f3vd//w8P2yjoYIAFCeiDIlRhBGAUYBrgPAD7IlCJULvAvK1RooN5CBW62m+sR1CirwZRpkunAVV6ZxyMx1FU6PLvxhPxP1owTqmo0mu3dONRFGV6YlFHlT48CuJblS6NwxZ/clFHmY5t6CjR5f9QprNB4XKzxdiIokpXmi3GiijcPA7xNv16KbE+BZOgnfEv+g96ps7BBVDGSi++aZZ6aWAYsjBH2r2Ux7nDPc5dm3s2T3FBuNzzOOeOl3LmibxG7qsYQ81UMZxQ6FQurmIYJdups2lgfX71nz8r1YblcvcH23Fs1+m2Bop++a9C3qrULD+fL+St/v+tRrFg1SoNv1GqlK16wa8NFK1EvVCwqrVKw2745SF7R7a35M6/65Xyt+ZP6LDvUE9GKTBpDUJmGCUEBzXh4yYhFAJRYaQWMhWUkXzPhVcL6OUcG9rtkNtu1x47VIUl2oyxfw8gjq05hOndT3vjadtN70tvTxUmm6Q7xKipmDIS+jM7vLtXbjupPT68NZis9GGyaR7YeRtjaFJB0ZdzwBJmB36dbKUSi16FSJDOQo4RPSyKEVLbiS3k2DE4ANcWfpls2d5HDVUMe17njylTQ9WCBBVLOXwAg4thJK6h6oq8ZnIiCTqTY5H3+7OQM6RnZB6ek/wmgSNSKEAse4VEUEOVkgTw1xB/QzTBh0YGs62TEwI3Mu2DAe5l3FViyFYmOUtCnwWN7M7TvqLj0r6dkw5+fzub7dkmsn3ibpmA4CW0mklKdParbqJD70fXEIcuyMIv8Cv8AUWowjAMk3cDAF0ecXY=); Raid BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzEVUFIHFcY3v/N7Mybf8t2fF3oOLUw7kG2C2PfzHRbVwq7emmPpfRQ9lJHd+1ubXe3u3uw0IKFSnPwYEgC0QQUEiGEhEAOIh5DCCbExFwMBjQbIyQHD8khYHJIwhs1Ceaq5js8Zr7vzbzv//4fHrZR0MEACxLQB0WowgjAEYBpgHMA7KNAJULtAvOWRokO5t+o0Ga/sRFBiT4fRJmunAZU6e1xMB5EUaGrPxkPo6jS5ZmPjVMqqvTqTd24H0WZHlvSUaH/F8S3Kl0Zh2365JKOMh3bFOvScUCJrv6JKm2eAGNT/GhttMVYExu3jkK8Tb9WSmxMwSRoZ/wL/r2eqRk4D8pY6enno6VeGhiGLMyTdi/lce5wj3PX5p7NU1wQLvc8zrnjpZwFIq+TuyrGUDNVDCcUOpWLqxhGyXbqbBpYn1/9/ZdKtWG53P3adhzbdbqtgaJf/rWQtyo1y8/nC3mr/y+rUSxYtUrDb5QqZate8GsDRStRLxSsaq3SsBt+ecjele1tufO3eqX8hfktOuxL1JNRCkxah5AZRgnBQU34uEEIhUBUGKmFTAVlJF9x4dUCeinHhvY65Lbbtc8OVWGJjsbYH4cQx3YfwvTO+7XxtO2mD6S2RwqTTdIdYtRUTBkJ/Y79s7dWbjupfT68Neis9LazaR7YeRVjaFJB0WfzwBJmB36WbKUSi16BSJDOYo4RPSw2I6R2ElvMsf/gEFxb+EmyZWceNVQx7Hmd36RMDVULElQM5fAhNC6GkbiGqivyms2JJOhsjkXezM9izpAekwV4QvJbBP6VQgFi2cskghqqlCSAv4D4S6IJPjQymG2dnBC4nmkfDLCccZvEkK1Mco6EPgga2d2nA0XHxQM7Jx2sP57N9uwQ2T5xt0xA8BJqZpISnfu0m+jQ+841xKELsvA9/AA/QxGqMAzD5PUARdFxcA==).

## Other builds of this spec

- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (8/5/38) — [open the talent tree](https://talentsforever.com/warrior/60/35-05-250530022331201351-12)
- [Protection — Raid Tank](../research/raid/builds/prot-raid-tank.md) (12/5/34) — [open the talent tree](https://talentsforever.com/warrior/60/3500301-05-150533020311001351-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-23 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows. Windfury Totem's buff changed in client 1.60.1.71037 and the raid simulator used here predates it: full-raid numbers of melee builds assume the old totem.*

