# Protection Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (17/3/31) — [open the talent tree](https://talentsforever.com/warrior/60/35310003002-03-250530020310001351-7)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Before the pull, then keep up all fight:** **Battle Shout**.

**Then press the first one that is ready**, top to bottom:

1. **Shield Wall**
2. **Revenge** after you block, dodge or parry
3. **Bloodrage** when you have less than 90 rage
4. **Shield Slam**
5. **Heroic Strike** when you have 34+ rage
6. **Rend**: keep it on the target

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

Tank value 1.011 (threat and damage taken under a boss, relative to our reference tank build).

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

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzElE9oE1sUxnPuTGZOTkqYzuvjTe/rg2kWZV5gys2EaNNN0m50Ka6kGzttUhMrSUhmURdiXQQEXShu2lqoUAvin4WCpXQlYksLinWhoGCtWrALhbpw40JlpkbEta3fYjjzfXfO/DgXDnUgaGCACRYMQhGqMA5wFuAKwDUAvSVImZ/2AH+tINOAnyYFN4aMzSjJODsBJOPzaSAVH18A44lCKn64AcbbGKl4bw6Myyqp+OChZryKkYyX1jRS8eJt8D9XcW0advync36fiTWNZNw+59d3g5MvG63Ge7/VeqPVWI+RhOuFeIe2XLI2Z2AKIrPuTfdF38wcXAflfOnjf41SPwXMYEEOFllnKp1KCiFSQji2SNlOWqT9WgRuMpVOrjD5DduS6W8ijqRYCq4uQVylMEl2sq6P6oNu9cTRStUzHeHss0XGdjK95nDRLR8r5M1KzXTz+ULeHDppesWCWat4rleqlM16wa0NF02rXiiY1VrFsz23PGo3Y3sn7j5er5T/5yoPk4TvFF3mrDekI1e4TAwP6C28ybSyBPqpX1CSwk6mfzNKO2mJGEo6q4W4QjKxjAjgvrbpxNG38NMi6Bbvon8T7SjpsfsQpbAVxkcDOtPC/mGCNFebXgP2gLqT/kq0ohJQR0ilcCrVvT/NidAEC3F5CfSxPbjHNorGI6Q6/sDmB/xR4PyAHuWRH+MwpC22AtvMOSOFArXl7rAoRUhFZoH4DPEvLOL7ofGRXPvUpK/VbOdIoGdZZ4MZsplNLLDQH5GXa1a7qq5bu/afTPA8fDXX993IDfrrbhKCl9BGNiHhwj+9TIP+nzajgB7IwUE4BEegCFUYgzH2bQDjkwQ/); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/protection/#eJzElE9oE1sUxnPuTGZOTkqYzuvjTe/rg2kWZV5gymRCtOkmaTe6FFfSjZ02qYmVJCSzqAuxLgouXCgqtLVQoRbEPwtdlNKViC0tKGajoIuaasEuFHThxoXKnRoR17Z+i8uZ75s58+NcONSFoIEBJlgwDEWowiTAeYDrADcB9LYgZSLtA76lINOAnyUFmyPGdpRkXJgGkvHFHJCKTy+CsRUjFd/fBuONKB4sgnFNJRUfPdaMVzGS8XJDIxUv3QPxuYqNOdj1ny2KPtMNjWRcDs7GFdGzeRWMd6LV5lS7sRkjCTcL8S5trWRtz8MsRBa8O97LgflFuAXKhdLH/6ZKgxQwgwU5WGHdqXQq6ThOynFc20nZbtpJi9oJ3GQqnVxn8mu2I9PfRBxJsRTcWIW4SmGS7GRdH9eHveqp45Wqb7qOe8B2Mrab6TdHi175RCFvVmqml88X8ubIadMvFsxaxff8UqVs1gtebbRoWvVCwazWKr7te+VxuxXbu3HvyXql/D9XeZgkfKvoMmf9IR25wmVieEhv4y2m9VXQz/yCknTsZPo3o3SSloihpLNaiCskE8s4AdzXDp04Cgs/rYBu8R76N9GJkh57CFEKW2F8MqQzLSxeJkhzteVNwT5Qd9NfiXZUAuoIqRROpXoPpjkRmmAhrq2CPrEP99hB0XiEVFcMbGlIjAKXhvQoj/wYhyHtsHX4wNxzUihQR+4+i1KEVGQWOJ8h/oVFhB+aHMt1zs4IbWS7xwI9z7pNZshmNrHMQn9Efq5V7al67u7ZfzLBefRGbuC7kRsW624GgodQM5uQcPmffqbB4E+b0YE+yMFhOALHoAhVmIAJ9m0AC4cERg==).

## Other builds of this spec

- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (14/5/32) — [open the talent tree](https://talentsforever.com/warrior/60/35300003-05-050533020301001351-7)
- [Protection — Raid Tank](../research/raid/builds/prot-raid-tank.md) (14/5/32) — [open the talent tree](https://talentsforever.com/warrior/60/3500501-05-150533020300001351-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)). Simulations, not in-game measurements. Do not hand-edit.*

