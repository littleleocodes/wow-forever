# Protection Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (17/3/31) — [open the talent tree](https://talentsforever.com/warrior/60/35300103002-03-050530020330001351-7)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Before the pull, then keep up all fight:** **Battle Shout**.

**Then press the first one that is ready**, top to bottom:

1. **Shield Block**
2. **Shield Wall**
3. **Revenge** after you block, dodge or parry
4. **Bloodrage** when you have less than 90 rage
5. **Shield Slam**
6. **Sunder Armor**: stack it to 5 on the target
7. **Heroic Strike** when you have 34+ rage
8. **Rend**: keep it on the target

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Protection tanks in **Defensive Stance** with a shield, and threat comes from three buttons: **Revenge** whenever it lights up, **Shield Slam** on cooldown and **Heroic Strike** whenever 45 rage is spare. The boss's debuffs and your big cooldowns are not on the list: they are yours to manage.

**Why it works**

- **Revenge** comes first: 5 rage (2 with **Focused Rage**) for high threat, usable only for 5 seconds after you block, dodge or parry, so a missed window is lost. The simulator measured it slightly better above **Shield Slam**.
- **Shield Slam** (20 rage, 17 with **Focused Rage**, 6-second cooldown) is your hardest hit, made stronger by your block value, and causes very high threat; the simulator casts it every time it is ready.
- **Heroic Strike** is about a third of your threat in the simulator. It goes on your next swing, off the global cooldown, so you can queue it on top of everything else; waiting for 45 rage keeps enough for **Shield Slam** and **Revenge**.
- **Rend** (kept on the boss) and **Shield Bash** fill the remaining global cooldowns for a little threat, worth 0.5% and 0.2% of tank value in the simulator. Use **Bloodrage** whenever you are under 70 rage, about 3 times a fight.
- **Shield Wall** (60% less damage for 12 seconds, 15-minute cooldown) is at the top only because the simulator's boss hits the same all fight, so any use saves the same damage there (3.2% of tank value). In a real fight, save it for the dangerous moment.

**Caveats**

- The list has no **Sunder Armor**, **Thunder Clap** or **Demoralizing Shout** because the simulator's raid already has those debuffs on the boss (a druid's Demoralizing Roar stands in for the shout), so casting them only cost rage there; dropping **Thunder Clap** measured 0.8% better. In a real raid they are usually yours.
- **Shield Block** has no line at all: the simulator never casts it, so its worth is unmeasured. It gives 75% more block chance for 7 seconds or 2 blocks, and each block gives 5 rage with **Shield Specialization** and opens **Revenge**.
- **Shield Bash** is your interrupt (12-second cooldown). As a filler it is worth little, so keep it ready for a spell the boss must not finish.
- The simulator's boss only melees you: it does not model adds, tank swaps or damage spikes, so it never needs a **Taunt**.

**When to change it**

- On the pull, stack **Sunder Armor** to 5 for the raid's armor reduction and your threat, then refresh it before its 30 seconds run out.
- Keep **Thunder Clap** (bosses attack 20% slower in Forever, 30 seconds) and **Demoralizing Shout** (204 less attack power, 45 seconds) up unless another warrior or a druid's Demoralizing Roar covers them.
- Press **Shield Block** when the boss hits hard, and **Shield Wall** for the worst moments: an enrage, a healer down, your health low.
- Adds: **Thunder Clap** hits up to 4 targets, **Challenging Shout** (10-minute cooldown) turns everything within 10 yards onto you for 6 seconds, and **Taunt** (8-second cooldown in Forever) takes back a single target.

*This guide was written for the rotation of 2026-10-09; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

Tank value 1.020 (threat and damage taken under a boss, relative to our reference tank build).

**The gear** (average item level: Pre-BiS 63.7; Phase 1 BiS 63.7; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) |
| Shoulders | [Highlander's Plate Spaulders](https://www.wowhead.com/forever/item=20057) | [Highlander's Plate Spaulders](https://www.wowhead.com/forever/item=20057) |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Breastplate of Heroism](https://www.wowhead.com/forever/item=21997)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Breastplate of Heroism](https://www.wowhead.com/forever/item=21997)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184)<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184)<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Highlander's Plate Greaves](https://www.wowhead.com/forever/item=20048)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Highlander's Plate Greaves](https://www.wowhead.com/forever/item=20048)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) |
| Trinket | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Arena Grand Master](https://www.wowhead.com/forever/item=19024) |
| Main hand | [Greenhammer](https://www.wowhead.com/forever/item=279261) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzEVE9oE2kUz/tmMvPyUsJ0NstOv+3CNIcyG5jyZYbsNr0k7WX3uOxJerHTJjWxkoQkh3oQ6yEg6EHx0tZChVoQ/xwULKUnEVta8E89VFCwFi3oQaEevHhQmakRoVdbf4fhm9/vzXu/+X3wqBNBAwNMsGAIilCFCYDTAJcArgDobYHKfLUX+EMVmQb8JCm4NWxsR0nGuUkgGZ/OAKn46BwYjxVS8d01MF7FSMU782BcVEnFe/c140WMZLywrpGK52+C/7mK6zOwy2/M+30m1zWSceeMf74dVD5vthtv/VabzXZjM0YSbhYSndpKydqehWmIzHnXvWf9s/NwFZSzpfd/NEsDFHgGC3KwxLrctCtESrhCOLZwbZEWPuEI1xVCpNx0apXJL9lGmH4l4kiKpeDaMiRUCpNkp+r6mD7kVY8drlQbpiOcv+yUsJ3ePnOk6JWPFPJmpWZ6+Xwhbw4fNxvFglmrNLxGqVI26wWvNlI0rXqhYFZrlYbd8Mpjdku2d+Weo/VK+U+u8jBJ2IzvGSYytpPZl2GvFV3mrC+kI1e4TAz/0dt4K4DVZdBP7P3vVPoHW+kgLRlDSWe1EFdIJpYRgbnPcZ04+hR+WALd4t30e7IDJT12F6IUtsL4YFBnWtgvJkhztcU14QBcd9EvyXZUAtcRUinsuj1/pzkRmmAhriyDPn4A9xinaCJCquMHtjDoR4ELg3qUR77FYUhv2CrsMOeUFAoQz91iUYqQiswC8RESn1jE50MTo7mO6Skfa9mu0QBPss4WM2Qzm1xkoZ+CRq512ld039i3OZng+f/lXP9XIjfk79YpCF5CW9mkhIu/9TENBr5bwwJ6IQf/wn9wCIpQhXEYZ18GALOLJ0U=); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzEVD9oE3EUzvvd5e7lpYTrGfF6VrhmKGfgyi93RJsuSbvoKE7SxV6b1MRKEpIMdRDrEHBwUFRoa6FCLYh/Bh1K6SRiSwv+yVJBhxq1oIOCDi4OKnc1InS19Rt+vPu+u/e++37wqBNBAQ0MMGEI8lCGCYCLADcBbgOobb7KPLUX9OcyMgX08yRhc1jbDJOIc5NAIr6aAZLxxWXQ3kZIxs93QXvvFY/mQbshk4xPniramwiJeLWhkIxXHoD3uYyNGdji1+e9PpMNhURc9M/GNa9n8zpon7xWG/V2bSNCAm7kYp3KSsHcnIVpCM2599zX/bPzcAekS4WvB+qFAfI9gwkZWGJdTtLhPMEdzm2LOxZPco+wueNwzhNOMrHKxHdsPUh7iXQkyZRwbRliMgVJsBJVdUwdcstnTpbKNcPm9iErwS27t88YybvFU7msUaoYbjabyxrDZ41aPmdUSjW3VigVjWrOrYzkDbOayxnlSqlm1dzimNWSrS2553S1VDyoy3qQBKxHtw3jKctO7ciwD5Iq6qwvoKIu6SIxPKK26a0AVpdBPbf9vxPJf2ylg5R4BAWVVQK6RCKxFPfN/YyqpKNH4bclUE29m/bHO1BQI48hTEEziM8GVaYEvZcJkrrc4uqwC667aE+8HSXfdYhkCjpOz+GkToQGmIgry6CO78I9RikcC5Fse4EtDHpR4MKgGtZDf+LQhI9sFb4w+4IQ8BHNPGRhCpGMzAT+HWI/WMjjAxOjmY7pKQ9r6a5RHy/TdpNpopGOL7LAf0Et06p2FN33d2xOyj+P38r0/yYyQ95unQL/IdBMxwVc3NfHFBj4aw1z6IUMHIVjcALyUIZxGGe/BgDeaydM).

## Other builds of this spec

- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (8/5/38) — [open the talent tree](https://talentsforever.com/warrior/60/35-05-250530022331201351-7)
- [Protection — Raid Tank](../research/raid/builds/prot-raid-tank.md) (14/5/32) — [open the talent tree](https://talentsforever.com/warrior/60/3500501-05-150533020300001351-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

