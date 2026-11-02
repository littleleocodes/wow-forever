# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury — Raid](../research/raid/builds/fury-open-raid.md)** (18/31/2) — [open the talent tree](https://talentsforever.com/warrior/60/31305013002-05053035102010501-2-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Fury — Dual Wield), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 816 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013032-25050034102210501--7)

## How to play

**Press the first one that is ready**, top to bottom:

1. **Bloodthirst**
2. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
3. **Whirlwind**
4. **Execute** when the target is below 20% health
5. **Hamstring**
6. **Bloodrage** when you have less than 23 rage
7. **Heroic Strike** when you have 68+ rage
8. **Bloodrage** when you have less than 90 rage

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Recklessness**: once a fight, in the last 45 seconds of the fight
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fury in a raid fights in **Berserker Stance** with a weapon in each hand: **Bloodthirst** and **Whirlwind** on cooldown, **Execute** in the gaps below 20%, **Hamstring** in the short gaps and **Heroic Strike** only when rage piles up. **Death Wish** and **Recklessness** wait for the last 45 seconds.

**Why it works**

- **Bloodthirst** (30 rage, 6-second cooldown) and **Whirlwind** (25 rage, 22 with **Raging Blows**, 10-second cooldown) are your main attacks: press them the moment they are ready. **Whirlwind** now always hits with both weapons, and it needs **Berserker Stance**, the stance this list never leaves.
- Below 20%, **Execute** still comes after **Bloodthirst** and **Whirlwind**. It spends all your rage (600 damage plus 15 per extra rage point; 10 rage to cast with **Improved Execute**), so it takes the global cooldowns between them; a full raid gives you enough rage that the simulator measured this order slightly better.
- **Death Wish** (+20% physical damage for 30 seconds, 3-minute cooldown) and **Recklessness** (+100% crit chance for 15 seconds) wait until about 45 seconds are left, so they cover the execute phase. Crits give double rage in Forever, so the **Recklessness** window also feeds bigger **Execute** hits. The simulator measured 0.7% more damage with **Death Wish** at 45 seconds than at 30, and in fights longer than about 3.5 minutes it presses it at the pull as well.
- **Hamstring** (10 rage) fills a global cooldown only when **Bloodthirst** is more than a second away and **Whirlwind** more than 1.5 seconds: it is a cheap extra main-hand hit that can trigger on-hit effects such as a shaman's Windfury Totem, but it must never delay your main attacks. The simulator measured 1.9% more damage with this rule than with **Hamstring** only above 80 rage.
- **Heroic Strike** is a rage dump, not a filler: queue it only at about 68 rage or more on a single target. It replaces a white swing, and white swings are your steady rage (each gives rage in proportion to your weapon's speed, double on a crit), so an early one starves **Bloodthirst** and **Whirlwind**; in Forever it also no longer helps your off-hand hit. The simulator measured 0.9% more damage at 67.5 rage than at 45.
- **Bloodrage** waits until you are under about 23 rage, so it refills an empty bar instead of topping up a full one. The simulator measured 1% more damage than pressing it whenever you are under 90.

**Caveats**

- The page's numbers assume a **Recklessness** in every fight and two Mighty Rage Potions (one early, one in the last 30 seconds). **Recklessness** has a 30-minute cooldown, so you will not have it on every boss: the simulator measured 11% more damage with it than without.
- With several targets, **Whirlwind** hits up to 4 of them, and above 40 rage **Cleave** replaces **Heroic Strike** (the full list does this).
- The simulator ignores threat. **Heroic Strike** causes a high amount of threat, so it is the first thing to stop if you pull aggro. **Death Wish** and **Recklessness** also make you take 5% and 20% more damage.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- Alone or in a small group (fewer buffs, less rage), put **Execute** first below 20%, stack **Sunder Armor** to 5 yourself and skip **Hamstring**. That is the simulator's rotation for a warrior alone on a training dummy, where stacking **Sunder Armor** was worth 12%.
- If nobody in your group has **Battle Shout** up, keep it up yourself (3 minutes), and put one **Sunder Armor** on a boss that has none: the list leaves both out because the simulator's raid already had them.
- Before a boss's fear, press **Berserker Rage** (30-second cooldown, 10 seconds of fear immunity); **Death Wish** also makes you immune. The simulator's boss never fears, so the list leaves it out.
- With a two-hander (the page's two-handed option), drop **Heroic Strike** and cast **Hamstring** whenever nothing else is ready: in the simulator's two-handed raid rotation those two changes were worth 5.3% and 6.8%. That rotation also uses **Bloodrage** under 90 rage and puts **Whirlwind** before **Bloodthirst** when **Bloodthirst** is more than 1.5 seconds away.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 864 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 977 | this build |
| Phase 1 BiS | 981 | [19/31/1](https://talentsforever.com/warrior/60/30305213002-35053005102010501-1-7) (ties this build) |

**The gear** (average item level: Pre-BiS 66.9; Phase 1 BiS 66.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Field Marshal's Plate Shoulderguards](https://www.wowhead.com/forever/item=16480) | [Field Marshal's Plate Shoulderguards](https://www.wowhead.com/forever/item=16480) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Marshal's Plate Gauntlets](https://www.wowhead.com/forever/item=16484)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Marshal's Plate Gauntlets](https://www.wowhead.com/forever/item=16484)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Marshal's Plate Boots](https://www.wowhead.com/forever/item=16483)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Marshal's Plate Boots](https://www.wowhead.com/forever/item=16483)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Grand Marshal's Longsword](https://www.wowhead.com/forever/item=12584)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Longsword](https://www.wowhead.com/forever/item=12584)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [High Warlord's Blade](https://www.wowhead.com/forever/item=16345)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [High Warlord's Blade](https://www.wowhead.com/forever/item=16345)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVk9oHGUU3zczO/vykm6nX1Iz+WJ1DCVOpm78ZnYnyUYxm6KiXix6sHgxm+zGrEgSdiK2ILqJF1Ep9WBpIiXRGgjRipaqpUgPFksVWoxgoKIY0oKCHip4EFEr32S30TUHCWn6DrNv35/9fr/33rz96GYEA0ywwIY+GIJRKAG8BDADMAfA6kKvIr1dwC8w1Azgz5OOS/3mci1pePQwkIZLJaAYnpkFc0GXyomt5qU4xfDFSTC/k8rlEpjTMdLwtyMy8pf3QKbH8FIJzO/jpOGfh+TvfD0rnx9+aZCG778OpONcv/lznHS8+IL81PCrBaPFNs4W7MvTsGfxAOz9te9lUCYKU1BzNPtu9pve6VmYB+XVwhWYKOzGED5k4JRya9JNCl+4SSG8hPCFnxRJ3xWecKU14Z1TtGXlgsHqOHEk3dZw8RSwDL+HksylZqcJVRb/FGopakfx/ONMMaI8SiqBS6zFoPjxsuv0Y6ErVomr4TEZZxx6lBFHrpNmLLwG7A1gA9nRp58YGR2zPOF1JFyREF63NTCUHX4yn7NGilY2l8vnrP791thQ3iqOjGXHCiPDVpDPFgeGLDvI563BZ4r7E7lnE8VsIZeoRCRWItqfCkaG23iKdvE22uZsRY0pD0V4jKKkpvyAGhyGemgiQtI91233A4kU5/rYLQicV2e5Zf/HW9jhtdCnNx69S2389mocSREQc4wyeiSdNDclAq6RYnLWyf21KHviP5TdVEhZJw2/nQG2gzdXJ3WIQDYMfzoNzOfJ/wsmuZJmfDK7njR864d1nTZ+Yt1p76zRzqS78e28l+5m3dTKdxJNYYxU4+oug1f08TtW9YmCwclw4rLSxYjESYrrlzv83Oa8Odurq5jyg+4IG92cya+RZ1pxPLiF1fNtFP1CURBk6+wofvQmVHYJfjC3qh/442H2CmxOdXZSk9OIUVY7D9e2pQREighWoffyHnLZnWEro0xdhkhlZzbzptCqrzY4JSo0idACO4oXZ4AdW4OQ17nxhO6nu1iadjjN1aTC9ei2u54fkOnchFFG81BhWB7NkLKt4vk0m6jGK9IJr2vj8TaHb7Qali9cO57X7svq4tUG9iACvy8kJP+4qgiF0XL1EXfMKjrXfJIYnjkI7AhszsB3kM1aw5GAfw1KeW9VWHZ0tvvl+UA8+xmw0ibNx8q4qqvjmhaVajfy7VTXQoTHQVqm6kPHVL2p/qicgyuKN65GQmnIzCu1VEMxVG0Qv0PLX0qNtEdKg5mmqUkpn/fcNhjKYo+3pJia1eOcVCI3RMYyFe26Suux63ZOOnw+8namt2zI9Mm77SSEXyJLPY6KJxt3/+MKLKALMvAA7IG9MASjsA/2KX8PABBMSzU=); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl1MHNUX3zMzO3s40O30Qv8Ml391JA0OUxfvzO4Ai0aWRo36YqMPNr7Iwi6yxgDZwdgmRhd8MWpqfbARTAN+kBC0RpuqTWN4sLGpJm3EB5IajYSSaKIPNfHBGLXmDrtFVx4MoXgeZs+ej72/3zlnzl76P4IBJlhgQx8MwSiUAJ4DmAGYA2B1oVeR3i7gFxlqBvCnScflfnOlljRcfQlIw+USUAzPzoK5qEvl1E7zcpxi+OwkmN9IZbUE5nSMNPzluIz86V2Q6TG8XALz2zhp+Psx+TsLs/L5wRcGafjeK0A6zvWbP8ZJx0vPyE8Nv1w0WmzjXMFenYYDS0fg4M99z4MyUZiCmjez72S/6p2ehXlQXixcgYnCfgzhQwbOKDcmRVL4npsUwkskfeEnhfBd4QlX+MJNuOcVbUW5aLA6ThxJtzVcOgMsw++gJHOp2WlClcU/gVqK2lG88DBTjCiPkkrgEmsxKH6y7Fp4KHTFKnE1PCbjjGMPMuLIddKMxZeBvQZsIDv6+CMjo2OWJ7yOhCsSwuu2Boayw4/mc9ZI0crmcvmc1X/YGhvKW8WRsexYYWTYCvLZ4sCQZQf5vDX4RPFwIvdkopgt5BKViMRaRPtjwchwG0/RPt5Gu5ydqDHlvgiPUZTUlB9Qg8NQD01ESLrnuu1+IJHiXB+7AYHz6iy37P9oB3t1I/TprUfvUhu/uRpHUgTEHKOMHkknzU2JgGukmJx1cn8jyp74B2U3FVLWScOvZ4Dt4c3VSR0ikA3DHxaA+Tz5b8Ek19KMj2c3k4ZvfLep08ZPbTrt7Q3amXS3vp130u2sm1r5XqIpjJFqXN1n8Io+fsu6PlEwOBlOXFa6GJE4SXH9coef2p43Z3d1FVN+0B1ho9sz+TXyTCuOR3ewer6Lop8rCoJsnR3FD1+Hyi7B9+fW9SO/3c9egO2pzl5qchoxymrn4dq2lIBIEcE69F7eQy67NWxllKkrEKnszGbeFFr19QanRIUmEVpgR/HSDLATGxDyOree0N10G0vTHqe5mlS4Ht121/MDMp3/YZTRPFQYlkczpGyreCHNJqrxinTC69p6vM3hG62G5QvXjue1+7K6eLWB3YvA7woJyT+uKkJhtFx9xB2zis41nySGZ48COw7bM/AdZLPWcCTgb4NS3lsVlh2d7X55PhDPfQqstE3zsTau6vq4pkWl2o18N9W1EOFJkJap+tAxVW+q3yvn4YrijauRUBoy80ot1VAMVRvEr9Dyh1Ij7ZHSYKZpalLKZz03DYay1OMtK6Zm9Tinlch/ImOZinZdpfXEdTsnHT4feCvTWzZk+uTddhLCL5HlHkfF0437/3IFFtAFGbgHDsBBGIJROASHlD8HAH7QS1Y=).

## Other builds of this spec

- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (18/33/0, 854 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013102-05053035102210501--7)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 816 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/20305012-55053005152010501--7)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 798 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013031-55350000052010501--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

