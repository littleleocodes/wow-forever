# Protection Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (17/3/31) — [open the talent tree](https://talentsforever.com/warrior/60/35300103002-03-050530020330001351-12)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Setup, before the pull:** **Defensive Stance**: the simulator starts the fight in it, and the rotation below assumes it.

**Before the pull, then keep up all fight:** **Battle Shout**.

**Then press the first one that is ready**, top to bottom:

1. **Shield Block**; no global cooldown, so press it alongside the others
2. **Revenge** after you block, dodge or parry
3. **Bloodrage** when you have less than 90 rage; no global cooldown, so press it alongside the others
4. **Shield Slam**
5. **Sunder Armor**: stack it to 5 on the target
6. **Heroic Strike** when you have 34+ rage; no global cooldown, so press it alongside the others
7. **Rend**: keep it on the target

Between these, your white swings do the rest.

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

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arms | 17 | Improved Heroic Strike 3, Deflection 5, Improved Rend 3, Improved Overpower 1, Deep Wounds 3, Impale 2 |
| Fury | 3 | Cruelty 3 |
| Protection | 31 | Shield Specialization 5, Anticipation 5, Improved Revenge 3, Master of Defense 2, Defiance 3, Improved Sunder Armor 3, Concussion Blow 1, Focused Rage 3, Bastion 5, Shield Slam 1 |

## The numbers

Tank value 1.011 (threat and damage taken under a boss, relative to our reference tank build).

**The gear** (average item level: Pre-BiS 62.5; Phase 1 BiS 61.4; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Talisman of Evasion](https://www.wowhead.com/forever/item=13177) · *War Master Voone, Blackrock Spire* | [Talisman of Evasion](https://www.wowhead.com/forever/item=13177) · *War Master Voone, Blackrock Spire* |
| Shoulders | [Highlander's Plate Spaulders](https://www.wowhead.com/forever/item=20057) · *sold by Samuel Hawke* | [Highlander's Plate Spaulders](https://www.wowhead.com/forever/item=20057) · *sold by Samuel Hawke* |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Breastplate of Heroism](https://www.wowhead.com/forever/item=226862) · *sold by Mokvar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Warrior's Embrace](https://www.wowhead.com/forever/item=10845) · *Avatar of Hakkar, The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* |
| Legs | [Legplates of Valor](https://www.wowhead.com/forever/item=16732) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Legplates of Valor](https://www.wowhead.com/forever/item=16732) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Grimy Metal Boots](https://www.wowhead.com/forever/item=18521) · *King Gordok, Dire Maul*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Grimy Metal Boots](https://www.wowhead.com/forever/item=18521) · *King Gordok, Dire Maul*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Finger | [Watcher's Signet of Vigilance](https://www.wowhead.com/forever/item=275980) | [Watcher's Signet of Vigilance](https://www.wowhead.com/forever/item=275980) |
| Trinket | [The Lion Horn of Stormwind](https://www.wowhead.com/forever/item=14557) · *world drop* | [Arena Grand Master](https://www.wowhead.com/forever/item=19024) · *quest: Arena Grandmaster* |
| Trinket | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* | [Vigilance Charm](https://www.wowhead.com/forever/item=18370) · *Immol'thar, Dire Maul* |
| Main hand | [Greenhammer](https://www.wowhead.com/forever/item=279261) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Annihilator](https://www.wowhead.com/forever/item=12798) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Instructor Malicia, Scholomance* | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Instructor Malicia, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzEVDFoE2EUzvvvcvfyUsP1jHg9K1wzlDNw5c8d0aZL0i46ipN0sdcmNbGSxCRDHZQqBBw6VFxsFSpoQUQdHErpJGJLi4pdFCq2Vi3o0EEHQR1U7mpE6GrrNxzvvu/dve//fnjUiqCABgaY0Ad5KMMIwCWAGwC3AdQmX2We2gn6ExmZAvp5knCtX1sPk4DfBknE5etAMj4fA+1thGS8v7FLe+8VD6dAuyaTjI+fKtqbCIl4ZUkhGV9fBO9rGZfHYJO/uqSQiKMbCgm4coZEnPEbV+rN2ob3p9V6s7bqNX69DLFWZb5grk/CBIRuunfdV92TU3AHpNHC5/31Qg/6liEDs6zNSTqcJ7jDuW1xx+JJ7hE2dxzOecJJJhaY+I69CNIeIh1JMiVcnIOYTEESrERVHVL73PLpE6VyzbC5fdBKcMvu7DIG8m7xZC5rlCqGm83mskb/WaOWzxmVUs2tFUpFo5pzKwN5w6zmcka5UqpZNbc4ZDVka1PuOFUtFQ/osh4kAevRLcN4yrJT2zLsg6SKOusKqKhLukgMD6tNeiOAhTlQz209dyL5j620kBKPoKCySkCXSCSW4r65n1GVdPQo/DILqqm30754Cwpq5BGEKWgG8VmvypSg10yQ1OUGV4cdcN1Gu+PNKPmuQyRT0HE6DiV1IjTARJyfA3V4B+4xSuFYiGTbC2y614sCp3vVsB76E4cmfGQL8InZF4SAj2jmAQtTiGRkJvDvEPvBQh4fGBnMtEyMe1hMtw36eJm215gmGun4DAv8F9QyjWpb0X5v2+ak/OexW5nu30Smz1us4+C/BNbScQFn9nYxBXr+2sEcOiEDR+AoHIc8lGEYhtmvAQAsTyeg); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzEVEFIFH8U3veb2Zm3b2UZ579/GieDcQ8yLYz8doYt18uuXuoY0SG85Oiu7WbsLrt7sINgwUIHIaMOaYFBCRF16SDiKSRFo8hLgVFmJdTBQx2C6mAxYxuB17Tv8Jj5vjfzvt/3g0etCApoYIAJfZCHMowCXAS4CXAHQG3yVeapnaA/lpEpoI+QhOv92kaYBPw2SCKu3gCS8dk4aG8jJOHrE9r7CMn4cBq06zLJ+OiJor2JkIhXVhSS8dUF8D6WcXUctvlrKwqJOLbp1ZWrQCLOXwKScGtA2/T+tFZv1ta8xq+XIdaqLBbMjSmYhNAt9577sntqGu6CNFb4fKBe6EHfMWRgjrU5SYfzBHc4ty3uWDzJPcLmjsM5TzjJxBIT37HnQfqfSEeSTAmXFyAmU5AEK1FVh9Q+t3z2VKlcM2xuH7IS3LI7u4yBvFs8ncsapYrhZrO5rNF/zqjlc0alVHNrhVLRqObcykDeMKu5nFGulGpWzS0OWQ3Z2pY7zlRLxYO6rAdJwHp0xzCesuzUrgz7IKmizroCKuqSLhLDI2qT3ghgaQHUkZ3nTiT/spUWUuIRFFRWCegSicRS3Df3I6qSjh6FX+ZANfV22h9vQUGNzEOYgmYQn/aqTAl6zQRJXW5wddgD1230X7wZJd91iGQKOk7H4aROhAaYiIsLoA7vwT1GKRwLkWx7gc30elHgTK8a1kO/49CEj2wJPjH7vBDwEc08YGEKkYzMBP4dYlss5PGB0cFMy+SEh+V026CPF2l7nWmikY7PssA/QS3TeNpVtN/ftTkpvx6/nen+RWT6vL06Af5LYD0dF3B2XxdToOePFcyhEzJwFI7BSchDGYZhmP0cAFBUJuY=).

**Points that do nothing for this spec:** **Improved Overpower** (1) only counts toward the points the tree needs before **Impale**; **Concussion Blow** (1) only counts toward the points the tree needs before **Bastion** and **Shield Slam**.

## Other builds of this spec

- [Protection — Raid Tank](../research/raid/builds/prot-raid-tank.md) (12/5/34) — [open the talent tree](https://talentsforever.com/warrior/60/3500301-05-150533020311001351-12)
- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (8/5/38) — [open the talent tree](https://talentsforever.com/warrior/60/35-05-250530022331201351-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-18 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

