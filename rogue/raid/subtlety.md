# Subtlety Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Subtlety

**[Subtlety — Hemorrhage](../research/raid/builds/subtlety-hemo-raid.md)** (20/0/31) — [open the talent tree](https://talentsforever.com/rogue/60/005303121014--5320003310013211501-7)

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point; refresh it early at 5 combo points when it has under 2 seconds left).

**Then press the first one that is ready**, top to bottom:

1. **Rupture**: keep it on the target, when you have 2 or more combo points
2. **Vanish** when you have 45+ energy and 3 or fewer combo points and Slice and Dice is active, until the last 10 seconds of the fight
3. **Premeditation**
4. **Garrote**: keep it on the target
5. **Eviscerate** (rank 8) when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
6. **Cold Blood** right before your finisher
7. **Hemorrhage**

**Hemorrhage** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Preparation**: once a fight, right after **Vanish**: it finishes the cooldown on your other rogue abilities, so you can Vanish again
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Subtlety in a raid is a bleed rotation: **Hemorrhage** builds combo points, **Rupture** stays on the boss from 2 points, **Slice and Dice** stays up, and **Vanish** buys a second stealth opener of **Premeditation** and **Garrote**.

**Why it works**

- **Rupture** is your main finisher, not **Eviscerate**: put it back on the boss whenever it is off and you have 2 or more points. **Hemorrhage** makes the boss take 15% more **Rupture** damage, **Serrated Blades** adds 30%, and each **Rupture** tick takes 3 energy off your next **Hemorrhage** (**Thousand Cuts**, up to 5 stacks). The simulator measured **Rupture** from 2 points about 1.5% better than waiting for 4.
- **Slice and Dice** is still 30% attack speed: put it back up with 1 point when it drops. When both are off, **Rupture** goes first if you have 2 or more points; with 4 or more points and under 3 seconds left on **Slice and Dice**, refresh it before you **Eviscerate**.
- **Vanish** puts you back in stealth, which **Premeditation** and **Garrote** need. **Premeditation** adds 2 points, and **Garrote** adds 2 more with **Initiative** plus an 18-second bleed, 20 energy cheaper and usable from the front with **Dirty Deeds**; the simulator measured that **Garrote** worth about 1.6%. The full list presses **Vanish** only with **Slice and Dice** up, 60 or more energy and 3 or fewer points.
- **Preparation** finishes the cooldown of your other abilities, **Vanish** and **Premeditation** included. Press it right after your first **Vanish** opener, not at the pull, so you get a second one; the simulator uses it only while **Vanish** is on cooldown.
- **Cold Blood** needs no timing here: it boosts only **Sinister Strike**, **Backstab**, **Ambush**, **Eviscerate** and **Mutilate**, so **Hemorrhage** and **Ghostly Strike** leave it up and it waits for your next **Eviscerate**. **Eviscerate** spends the points that **Rupture** and **Slice and Dice** do not need.
- **Hemorrhage** is your filler and **Ghostly Strike** goes in on its 20-second cooldown, a small gain (about half a percent in the simulator). Keep a dagger in your main hand: **Hemorrhage** then deals 145% weapon damage instead of 100%, and **Ghostly Strike** 180% instead of 125%.

**Caveats**

- The list says to keep **Garrote** on the target, but it only works from stealth: you cast it right after each **Vanish**, about twice in a 3-minute fight.
- Damage you take breaks stealth, and the simulator does not model that. If something is hitting you or ticking on you, the stealth from **Vanish** may break before you use **Premeditation** and **Garrote**; then keep building with **Hemorrhage**.
- Almost all of this works from the front: **Hemorrhage**, **Ghostly Strike**, **Rupture**, **Eviscerate**, and **Garrote** with **Dirty Deeds**. Only **Ambush** and **Backstab** need you behind the target.
- Subtlety has no cleave: on adds, stay on the kill target, and do not **Rupture** a target that dies within 8 seconds.

**When to change it**

- In the last 8 seconds, start no **Rupture**; in the last 6, put 4 or more points into **Eviscerate** even with **Slice and Dice** down.
- Without a warrior's Sunder Armor on the boss, keep **Expose Armor** up at 5 points: **Improved Expose Armor** in this build makes it 10 energy cheaper and hands back 2 points. On the training dummy the simulator measured it about 2.5% better.
- The simulator starts every fight out of stealth. In the game you can start in **Stealth** and open with **Premeditation** and **Garrote** at the pull; that opener was not simulated.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 609 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 641 | [20/0/31](https://talentsforever.com/rogue/60/005303103014--5320003310013211501-7) |
| Phase 1 BiS | 618 | [20/0/31](https://talentsforever.com/rogue/60/005303103014--5320003310013211501-7) |

**The gear** (average item level: Pre-BiS 63.2; Phase 1 BiS 63.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Zandalar Madcap's Mantle](https://www.wowhead.com/forever/item=19835) | [Zandalar Madcap's Mantle](https://www.wowhead.com/forever/item=19835) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVk9oHFUYn+/NZPflS7odHi0ZB5HXHCRdnPrezG7NdtVMQ4MiFUK9zM1Mu1M3EnaW3Q1NxENstQhRUUEhexCxEUQtlGIg9CYejNBDUjQnxfgHLBJBRAU1qMzsbrLN5uBl43eY+fb7M+/3ft/vLQ/vpqCDARyGYAKKUIY5gBcB3gZ4D4D1x1kSZYfBXD1Aia6Zc4BJ+tsHYHzfhxq9fBVQo3/Vo+Bbq7qxlsAk/eSjg8Z3KUzSSwtgfBU5N2/qxtcp1Oj8qo4Juj4ddSfppxehEf7i3egzL2/qqNGl1eh57Y3ok5+v6cZmasfR6K01ffCYvjI5dHtKbOXH118B79eJ14Fs5etAr/gf+l+efPOJ94G8NHkNNsaWYfMdGO3f2aULN8gRIbKOcKRwhMxYliNsKaTjSFtKx5YyK+QK0b4lK33sCrCCX556MizXuC3s45bIWfbwCX6u6JeeCgo8rHC/UAgK/OwsrxUDXglrfm0yLPFq4FfOFflQNQh4dfpsbSqozVoVf7JgtUqsRsmxp6th6aiZR5sJ1NMpmmDqRVDMHlQRbOwb7MWk3YMqnffwYPoA7WHksWZ2OHrReY8t7UYphWVnuoDycTzFRpsoyTOKmUANSSYbR7Q23A7idUhizxChv2fibAN2XC9FjPvjFOs1k7H7Q4k9uwfPuS7s4FAbo3UvXr3ubQN5wWOv7dfEjyJn9/y3+f6xX/N9FfAysEuAo6bbHOr2mGUW72Np7L2lJVCji7+c3l1gZ7HvOtBG0gB8yMzHJWqbMCSafyYG8PDYTDmsBtzip8ML/NR0JYZ7R3u0d30rz3Qz1S6mEwo7Y47jI2ys47BkUJr3dwivTagP5OITpO4wfDx60UWPhZ0EC9kFght6/6bEftpjpKIbgn8ecNa8gFnmdBAmMTXYfwdhET2JNnrwYfZgR1sWB9KHqcrwxnZj699ql4BzZqtgL4JlNxTcIHhpiqFJI1nSf+bAUG+TFfiZ2M+pSmyH3B9BQ4LK4N+kNwooc+fdu+oLkX02cuR8bOsj9gYxND6SXibK/2I1t+V11e692rV1cvHzzKJ7shlwJ6LbxQLEP5SNkbRKlwdG2y4hAobBhUdhHDwoQhlmYIb8OwAo2txv); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVk9oHFUY3+/NZPflS7odHi0ZB5HXHCRdnPrezG7NdtVMQ4MiFUK9zM1Mu1M3EnaW3Q1NxENsVYT4HypkDyI2gvgHSjEQehMPRughKZqTYtSCRSKIqKAGlTebpNtsDl42/Q4z335/3vze7/u95eHdFAwwgcMAjEEJKjAD8BLAOwDvA7DeOEtUdhCs5X2UGLo1A5iiv38I5o0e1OmN1wB1+ndDBd9eNsyVJKboZ5/sN39IY4pemAPzG+Vcu2aY36ZRp7PLBibp6qTqTtHPz0Mz/NV7aplX1g3U6cKyel6+qJZcuwjmulrgyxVDOTq9vmL0HzGWxgduToiNwujqq+D/NvYmkI1CA+il4KPg6+NvPfEBkJfHL8PayCKsvwvDvbd26cFVckiInCtcKVwhs7btCkcK6brSkdJ1pMwJuUT078lSD7sErBhUJp6MKnXuCOeoLfK2M3iMnykF5afCIo+qPCgWwyI/Pc3rpZBXo3pQH4/KvBYG1TMlPlALQ16bPF2fCOvTdjUYL9pbJXaz5MjTtah82CqgwwQamTRNMu08JKwu1BAc7OnvxpTThRqd9XF/Zh/tYuSxzeygetFZny3sRCmF7WQ7gPJxPMGGN1GSZxJWEnUk2Vwc0Vtwu4hXIIVdA4T+kY2zTdhxvRQx7k/TrNtKxe6PZfbsLjznO7CDAy2MNvz46w1/G8gLPntjryZ+GDm75//N98+9mu/rgC8CuwA4bHmbQ90es8zhfSyD3df1JOp0/teTOwucHPZcAdpMmoAPWYW4RGsRhkTrr2QfHhyZqkS1kNv8ZHSOn5isxnBva1d7NzYKzLDSrWI6lmCnrFF8hI20HZYsSuv+NuG1CPWBfHyCtFsMH1UvOu+zqJ1gITtAcFPv35XZz7uMVHRC8M8DTlvnMMfcNsIkpvt7byNM0ZNsoQcfZg+2teWwL3OQagyvbjdu/VvtEHDe2irYjWDZCQU3CV6YYGhRJUv67wyY2k2yBL8Q5zktEdsB7yfQkWCi/x/SrQKJmbPeXY05ZV8MHTob2+qQs0ZMnQ9lFknijljd2/I6avd+3LHv5OPnqXnv+GbAG1O3izmIfyTWhjIaXewbbrmECBgEDx6FUfChBBWYginy3wBJFtxw).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

