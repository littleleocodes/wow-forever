# Subtlety Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Subtlety

**[Subtlety — Hemorrhage](../research/raid/builds/subtlety-hemo-raid.md)** (20/0/31) — [open the talent tree](https://talentsforever.com/rogue/60/005303121014--5320003310013211501-7)

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point; refresh it early at 5 combo points when it has under 2 seconds left).

**Talents with no line below:** **Ghostly Strike**: a defensive or healing spell: cast it when you need it, it is not part of the damage rotation.

**Then press the first one that is ready**, top to bottom:

1. **Hemorrhage**: keep it on the target, when you have 4 or fewer combo points
2. **Rupture**: keep it on the target, when you have 2 or more combo points
3. **Vanish** when you have 45+ energy and 3 or fewer combo points and Slice and Dice is active, until the last 10 seconds of the fight
4. **Premeditation**
5. **Garrote**
6. **Eviscerate** (rank 8) when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
7. **Cold Blood** right before your finisher
8. **Preparation**

Between these, your white swings do the rest.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 576 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 681 | [20/0/31](https://talentsforever.com/rogue/60/005303103014--4320102311013211501-7) |
| Phase 1 BiS | 683 | [20/0/31](https://talentsforever.com/rogue/60/005303103014--4320003311013211501-7) (ties this build) |

**The gear** (average item level: Pre-BiS 66.5; Phase 1 BiS 66.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Leather Mask](https://www.wowhead.com/forever/item=16455)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Field Marshal's Leather Mask](https://www.wowhead.com/forever/item=16455)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Zandalar Madcap's Mantle](https://www.wowhead.com/forever/item=19835) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Marshal's Leather Handgrips](https://www.wowhead.com/forever/item=16454)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Marshal's Leather Handgrips](https://www.wowhead.com/forever/item=16454)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Marshal's Leather Leggings](https://www.wowhead.com/forever/item=16456)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Marshal's Leather Leggings](https://www.wowhead.com/forever/item=16456)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Grand Marshal's Longsword](https://www.wowhead.com/forever/item=12584)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Longsword](https://www.wowhead.com/forever/item=12584)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [High Warlord's Blade](https://www.wowhead.com/forever/item=16345)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [High Warlord's Blade](https://www.wowhead.com/forever/item=16345)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVl1oHFUU3nNndvfmJJ2MV6XjKDrZB0kXp947s1OzjZppsCiiEOrLvplJd9pdCbthM8XGl66tghARFCwmT9IkUEShBAOhb0WwUfrQViwoivEHrFJBRHyKP9yZTdxm8+DLxvMw9+455+755jvfuQzeR0EHAywYhHGowBQ0AV4DeBfgPADri6NERofAvNJPia6apzBLLzfB+KEXVbrwDqBKP7uiY5Z+tATGtYzcfNhvfK9hlp6ZA+Nrufm4CcY3Gqp09qrMXEuOZ+nl0y3/50vyf/48K58rV3VU6YW3ATP0/IRxS8MM/eKUXFV6/Zqe26+vVQdvTvKN4bEbb0Dp9/G3gGwMzwNdCN4Pvjp09rn3gLxevQDrh1fh1jkYpfFbgA8XyQDnnstdwV0uCrZdcB0uuOMKwYXrCOFxsUbU78ine9gSsHIwNfl8fSqyHO4csIWwuXPQOloJasfDslVvWEG5HJatiRkrqoRWox4FUbVes6bDoHG0Yg1Oh6E1fWIimgyjGbsRVMv2ZoqdpOx/Ybpe22c+hi4TSDGDatQ4EeKduTuwfxn6UKV/N4ERPW0A6nmNKkw5DSkzjQqCZ2Za8YXtOHnRdoa6gHMYHcZjIJk2IA725now66RRobMl7M/voWlGnm5Fh+RCZ0tspYNNbjuFLqB8Fp9goy2U5KWUpAlJwYs9ahtuF3EZspgeJPSPQhxNYMf5gse4L2msx8zG2x9rrL5LekgKzpe2ar9aYm/uVpP3ocXu/28t/XK3WtrAKjuOo6bfauJWW4WHD7E89lxX5TAs/vbM9gTHw95loEnQABwwH+iYJHFbinw5fWOY6abWLpCDKXbEHMMn2eGOASigMB/uEFOb+B4pxlOh/EvhAbnQxVKnpLjNRRcYTCT1bY39skPPeLELFV8BnDFfRI+5HYQJ1HJ9txEm6cm00YOPs0c7jnm4N383VRhe3Dq4eQNtU2jR3EzYiWDRDYkmBK9MMjTp1s18BnbpxrgXGdMTVs+1yLmkxYh+qhnKTbIGvxLnZSUV213+z6AiwVTuL9IjHanmMf+e+Tlpn4wMHIvtxoizTgzVGsmvktT/YpG/ueuqPfhB1+oU4+eRRf9Qy+GPyy+rOYh/pNZH8gpd3Tva9gHGYQh8eArGoAQVmIKTcJL8MwBYOCRN); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVlFoHFUUnftmduflJp2MT6XjKDrZD0kXp743s1OzjZppsCiiEOrP/plJd9pdCbthM8XGn66tBSGiqCgkX9ImUEShBAOhf0WwUfxoCxYUxagFq1QQEX8MKjOzidtsP/zZ9X7Me3vvfXvPnHvuY/A+CjoYYMEwTEIFZqAJ8CrAewDnANhAEiVxdATMzwcp0RXzBKr0UhOM6/2o0OtvACr0z0VAlX68DMaVbLz5aND4QUOVnloA45t480kTjG81VOj8ZR1Vup4eV+mlky3/F8vx/5x+O36uXtZRoeffAczSc1PGTQ2z9MsT8arQq1f03F59vTp8Y5pvjk5cex1Kv0++BWRzdBHo2eCD4OsD7z73PpDXqudh4+Aa3DwD4zR5C/DhAhni3HO5K7jLRcG2C67DOXddIbhwHSE8LtaJ8j35bBdbBlYOZqafr89ElsOdfbYQNnf2W4crQe1oWLbqDSsol8OyNTVnRZXQatSjIKrWa9ZsGDQOV6zh2TC0Zo9NRdNhNGc3gmrZ3kqx05S9L8zWa3vMx9BlAilmUYkax0K8M3cHDq7AACr07yYwomcMQD2vUZnJJ0EyMygjeGa2FT+7Eycv2s5IF3COosN4AiTbBsTB/lwfqk4GZTpfwsH8Lpph5OlWdCRe6HyJrXawyW2n0AWUz+ITbLyFkrwkxTQhKXiJR2nD7SKugIqZYUL/KCTRFHaSL3iC+6LG+kw12f5YY/Ue6SEtuFjarn26xN7sVZP3oMXu/28t/apXLW1glR3FcdNvNXG7rcLDh1ge+64q8TAs/fbMzgTHw/4VoGnQABwyH+iYJHFLSvxy+uYo002tXSD7JXbInMAn2cGOASigMB/uEFOb+B4pJlMh/0vhvnihS6VOSXGbiy4wmErquxr75TY948UuVHwFcM58ET3mdhAmUMsN3EJYTE+2jR58nD3acczD3fm7qczwwvbBrRtoh0KL5lbC7QgW3ZBoSvDqNEOTbt/Mp6BHN8a9yJiesnqmRc5FLUH0U82Qb5B1+JU4L8tSYnf5P4OCBKXcX6QvdkjNI/49iwuxfTo2dCSxa2POBjEUayy/RqT/xSJ/a9dVe/DDrtUpJs9DS/6BlsOfjL+sFiD5IW2M5WW6tnu87QOMwwj48BRMQAkqMAPH4Tj5ZwAf9SPx).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

