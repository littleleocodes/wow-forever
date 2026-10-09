# Subtlety Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Subtlety

**[Subtlety — Hemorrhage](../research/raid/builds/subtlety-hemo-raid.md)** (20/0/31) — [open the talent tree](https://talentsforever.com/rogue/60/005303121014--5320003310013211501-6)

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point; refresh it early at 4 combo points when it has under 3 seconds left).

**Then press the first one that is ready**, top to bottom:

1. **Rupture**: keep it on the target, when you have 2 or more combo points
2. **Vanish** when you have 60+ energy and 3 or fewer combo points and Slice and Dice is active, until the last 10 seconds of the fight
3. **Premeditation**
4. **Garrote**: keep it on the target
5. **Eviscerate** when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
6. **Cold Blood** right before your finisher
7. **Ghostly Strike**
8. **Hemorrhage**

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

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 673 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 610 | [20/0/31](https://talentsforever.com/rogue/60/005303103014--5320003310013211501-6) |
| Phase 1 BiS | 674 | [20/0/31](https://talentsforever.com/rogue/60/005303103014--5320003310013211501-6) (ties this build) |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 62.9; Phase 1 BiS 67.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Bloodfang Hood](https://www.wowhead.com/forever/item=16908) · *Onyxia, Onyxia's Lair*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Zandalar Madcap's Mantle](https://www.wowhead.com/forever/item=19835) | [Nightslayer Shoulder Pads](https://www.wowhead.com/forever/item=16823) · *Sulfuron Harbinger, Molten Core* |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) | [Nightslayer Gloves](https://www.wowhead.com/forever/item=16826) · *Gehennas, Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Bloodfang Pants](https://www.wowhead.com/forever/item=16909) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) · *quest: Garona: A Study on Stealth and Treachery* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) · *quest: Garona: A Study on Stealth and Treachery* |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Perdition's Blade](https://www.wowhead.com/forever/item=18816) · *Ragnaros, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Brutality Blade](https://www.wowhead.com/forever/item=18832) · *Garr, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Striker's Mark](https://www.wowhead.com/forever/item=17069) · *Magmadar, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVU+IG2UUn/fNJPPl7TY7/WzpOIhMV5DtwNRvZjbppnuYZFEUQWjRQ27utElNZM2EJIVtqbIqBSUWW/Hg5iCVXioqSFWQngSlpBAhW2oPUhH/gEVyWATrwQVlZpJN3PXgwSx9h5k373vve+/3fo95OElBARV0mAEO7KHNL8JhDrJwBPKwCCWowgrAawDnAbS7E5QokvYSyvT3D0D9eQJF+skySvTPFqBM3+0q6locZfrlp1PqT0mU6auroH4XKJ2Oon6fRIk2uwrG6a2TQbBM3+ztisznekr/KdJzL6BE3zsf3HhzTVF7QfxX3VCR6I01ZdpQ2mX1jfLMnSW+MZ+FI80bkL9yE94CsjH/DlzyLsKH3mW4nWsDLOAQ5VWyn/OUwx2LO9yaNc2UY3POHcfi3HJsy0pxq02kH8kfCXYJWMGrLj3rVxu6ze20yTOmPXdYP17yKs8VC7pf071CoVjQj53SG6WiXvMbXqPsV/R60asdL+kz9WJRr5881lgqNk6ZNa9cMAcuZuRy8Pm6XzmgzaPNOCpGksaZ+AoIWgxFBBsnphMo2zEUaTOPU8YuGmPkyf7pXPCizTx7nexQlRcB3wZ2AfCMdhpTzNlWsIXJ6UnEKyBjbIbQu7NhzfFhzWnMMRfvM3YPwijGUXIOHkrhPmMvFRle3YyNIpytsDO425jq3yljDEWb17VBDPtsK2MWN7k9hl48hY+yhX4DyGlBi6OEJB1xKI20xPlHO4LTiMLQ3+IBJvpFkiU0OVR/qbAz/8JmZgwI9oxMVysfZm/lNws5m2cXdmr6D6DOHvxvs65oydGGHhbY09pRfJw9tm0WZ9HSHtnW/BGyDmXC0RKHWdIBi/Tyb8D8LciDKbLGgDwi/YcKe3GHEu7FyW/jCRTpNZ8FP/Eg/TWfoUZD7H+tgCreIW1YJ/bLohDKnuyvICFBYfp9MREYhJUT2ftbq4Fcd/efCOWWa68TVdZdo02Ee0oa2YE2Vnn4o/89T+brTqczufhxNtc3ZBeDFbwKZX/97PVnvnEzoVXournAs9PpuUcj5bZriPTzfQsPDNdetM6fCBd6CaqwDMvs7wEA/GS1Fw==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVU+IG2UUn/fNJPPl7TabfrZ0HESmK8h2YOo3M5vtpnuYZFEUQWjRQ27utElNZM2EJEJbKkTXgJKWbq0Hdw9S6cEKFqQoyp4EoaQQYRX1IBVRCxbZw+JBEQrKN5Ns4q4HD2bxXfLyvvfv936PeThOIQUaGDAFHNhDW/8Ih1nIwjHIwwKUoApNgNcAlgH0P8YoSSl6E1Cl518F7c4YKvTORUCFfrwkjG+vp7Qv4qjSzz6c0H5KokqXVkD7TihrS6B9n0SFttdTqNILUbhKL27siezvtkSe1mVAmV54ARX6zrJI2bwM2oZIsBwpCr3egkkz1Slr58tTdxf5vbksHGt/CfkbX8EbQO7NvQVX/Svwvn8Nbuc6APM4ALpGDnKedrlrc5fb05aVdh3OuevanNuuY9tpbneI8iP5PcGuAiv41cVng2rDcLgzY/GM5cweNU6W/MpzxYIR1Ay/UCgWjBNnjEapaNSCht8oBxWjXvRrJ0vGVL1YNOovnmgsFhtnrJpfLlh9FytyOfx8Pagc0ufQYRxTZpLGmfwKSHoMZQQHxyYTqDoxlGk7jxPmHhpj5Mne66z4oe08e53sUpdXAN8EdgnwnH4W08zd0bCNyclxxBugYmyK0N+mw57jg55nMMc8vM/c2w+jGEfFPXwkjQfM/VRmuLYVG0W422FncK850cupYgxlh9f1fgz7aDtjNre4M4JZPIWPsvneAMhZSY+jgmQm4lAZGon7t3GI14jC0N/mAhP9NMkSuhqqP1fYuX9gMzMCBPuGtms1H1ZfzW810sqzS7u1/YfQYA/+u11P6cnhgR6V2NP6cXycPbZjF6fR1h/ZMfwhso5kwtWSB1VmBIv02q/Agm3IxRbZI0Aekf5Dhb20SwX34/i38QTK9GbAxHdclL8ZMNRpiP3PJmjyXdKBTeK8LEuh7Mv+AgoSlCbfkxPCIDVPZe9fXRFyyzt4KpRvPGeTaKrhmR0i/a+kke1rI5WHr//ndTKfd7vd8YUPsrmeIbsgrvAKlIPN1q1nvvYyoVVa93LCs9vd8I5Hym3PlOknB+YfGJy96KI/Ed70ElThNJxmfw0A47ixbQ==).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

