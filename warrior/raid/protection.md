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

**The gear** (average item level: Pre-BiS 61.3; Phase 1 BiS 67.0; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Helm of Awareness](https://www.wowhead.com/forever/item=18313) · *Zevrim Thornhoof, Dire Maul*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Helm of Wrath](https://www.wowhead.com/forever/item=16963) · *Onyxia, Onyxia's Lair*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Evil Eye Pendant](https://www.wowhead.com/forever/item=18381) · *Immol'thar, Dire Maul* | [Medallion of Steadfast Might](https://www.wowhead.com/forever/item=17065) · *Magmadar, Molten Core* |
| Shoulders | [Stoneform Shoulders](https://www.wowhead.com/forever/item=13955) · *Kirtonos the Herald, Scholomance* | [Stoneform Shoulders](https://www.wowhead.com/forever/item=13955) · *Kirtonos the Herald, Scholomance* |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Deathbone Chestplate](https://www.wowhead.com/forever/item=14624) · *Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Deathbone Chestplate](https://www.wowhead.com/forever/item=14624) · *Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Magically Sealed Bracers](https://www.wowhead.com/forever/item=18351) · *Magister Kalendris, Dire Maul*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Wristguards of True Flight](https://www.wowhead.com/forever/item=18812) · *Molten Core*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Force Imbued Gauntlets](https://www.wowhead.com/forever/item=18383) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Gauntlets of Might](https://www.wowhead.com/forever/item=16863) · *Lucifron, Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Handcrafted Mastersmith Girdle](https://www.wowhead.com/forever/item=13502) · *Goraluk Anvilcrack, Blackrock Spire* | [Belt of Might](https://www.wowhead.com/forever/item=16864) · *Molten Core* |
| Legs | [Legplates of the Eternal Guardian](https://www.wowhead.com/forever/item=11927) · *Blackrock Depths*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Legplates of Wrath](https://www.wowhead.com/forever/item=16962) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shalehusk Boots](https://www.wowhead.com/forever/item=11787) · *Panzor the Invincible, Blackrock Depths*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shalehusk Boots](https://www.wowhead.com/forever/item=11787) · *Panzor the Invincible, Blackrock Depths*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Tarnished Elven Ring](https://www.wowhead.com/forever/item=18500) · *Dire Maul* | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Demon's Blood](https://www.wowhead.com/forever/item=10779) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Main hand | [Greenhammer](https://www.wowhead.com/forever/item=279261) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Brutality Blade](https://www.wowhead.com/forever/item=18832) · *Garr, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Draconian Deflector](https://www.wowhead.com/forever/item=12602) · *Blackrock Spire*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Malistar's Defender](https://www.wowhead.com/forever/item=17106) · *Ragnaros, Molten Core*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Scholomance* | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/warrior/protection/#eJzMVE1oE1sUzrkzmTk5KWE6r483mffDNPBKDEy5yTBquknajS4VXEip2GmTmlhNQpJFFYSKBBSF1JVWFy1IUUGxCBbpQkRsSSHFIuhC/MFasIsu6kIQN8qkpgXXtfitzv3Oued+91zuRy0ICmhgQBg4qMHNFeOwF5JwAA5DAUYB9GUJmQL6aZLxQhW0FT+JuFgFEvDcSZLx2Rho7wMk4WRR+xAgGe9VQbsuu5kqaO8CJOCjLEl45Yi7VcKLfS4p4vMpIBGfjrmNbvaRiA+WFJLxTaVVW3PbzQ5ob926L5ch9L8yn9UuZY1P/4ZXJuAq3HAm4Y5zC151T8PEFDyGSrYG0ENbV5pl/1m2xTnnlsltk9vctiwe4xaPch617GiNictsVaQ/iXQkKSzhwhyEZPKSYEZL6rDa7xROHM0XykaMx3abPG7G4l3GYMbJHUunjHzRcFKpdMoYOGWUM2mjmC875Ww+Z5TSTnEwY4RL6bRRKObLZtnJDZvNtLmR7jxeyud26bLuJQE/Sqqosy6Pirqki8Rwn9qiNzXV5kA985OUKDej9jZLCZISCaCgsqJHl0gkFucNcd/aVNLRpfDzLKhhvYP+jgRRUANPwE/esBcXe1WmeN1iAluXm1wFdkB1O/0RaUWpodpHMnktq3OPrROhAWHE+TlQR3bgHdvIH/KRHHMHNtPrjgJnelW/7tschyasshqss9hZwdNAW/I+85OPZMX9bl8hdFvwubxndCgZvDbuYiHRPtTAy0RsnWmikYjUmOe3QjnZjH4pOu5u+znxxXq93tI/nez+QST74TzAOGTz65WFQy8S8QbrWUp0u5X1+lri4EbwOhER8OFfXUyBnn+2/GbDNPc3bDMDBRiBEfX7ACcfFl4=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/warrior/protection/#eJzMVE1oE1sUzrkzmTk5KWHevD7eZN4P08AreYEpNxlGTTdJu9GlQhdSBDs2qYnVJCRZ1EWhUgOCLqpurF20IEULCkWwSFdSaUkhxVLQhYj1p2IXXdSFICIok5gWXNfitzr3O+ee+91zuR+1ICiggQFh4KAGd1aMwyFIwlE4DgUYAdDfScgU0IdJxscXQdvwk4gzFSABR8+RjE/GQHsdIAmnitrbAMn45RpoEzLJuD4K2nqARHw1CiTjQmOzhJdPNOjbFSAR16bdVhM9JOKDVYVkHLsO2pbbaK0C2ku38NNVCP2nLGW1K1njwz/hjUm4AbecKbjr3IHnXbMwOQ2PoJKtAnTT7q3m2b+WbXHOuWVy2+Q2ty2Lx7jFo5xHLTtaZeIbtinSH0Q6khSWcHkRQjJ5STCjJXVQ7XMKZ0/mC2UjxmMHTB43Y/FOoz/j5E6nU0a+aDipVDplnDpvlDNpo5gvO+VsPmeU0k6xP2OES+m0USjmy2bZyQ2azbTZSHecKeVz/+uy7iUB30uqqLNOj4q6pIvE8LDaojc1VRdBHf5BSpSbUXuPpQRJiQRQUFnRo0skEovzurivrSrp6FL4cR7UsN5Of0WCKKiBBfCTN+zFlV6VKV63mMDW5SZXgX1Q3Ua/R35Dqa7aRzJ5LavjoK0ToQFhxKVFUIf24R1byR/ykRxzBzbX644C53pVv+7bGYcmbLIqbLPYBcFTR2vyPvOTj2TF/XGfITQj+FzeMzKQDN4cd7GcaBuo41kits000UhEqszzS6GcbEY/Fe339vyc+EqtVmvpm012fSeSfXAJYByy+e3Kcs/TRLzOelYTXW5lrbaVONYIXiQiAj78s5Mp0P33rt80fPNI3TkzUIAhGFK/DQCYlRb9).

## Other builds of this spec

- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (14/5/32) — [open the talent tree](https://talentsforever.com/warrior/60/35300003-05-050533020301001351-7)
- [Protection — Raid Tank](../research/raid/builds/prot-raid-tank.md) (14/5/32) — [open the talent tree](https://talentsforever.com/warrior/60/3500501-05-150533020300001351-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-22 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)). Simulations, not in-game measurements. Do not hand-edit.*

