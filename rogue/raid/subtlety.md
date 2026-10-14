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

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVl2IG1UUnnNnkrl7djc7vbZ0OohM90G2A1PvzGy2m6442UVRBKFFH/Jmp01qImsmJCnulirrT0GJRSs+uHmQSl8qKkhVkD4JSkkhQrbUPkhF/MEWibAI+mJBmZlkEzcriJjF85CcnDnnnp/vy5mLYxQUUEGHKeDA9mz8IhxmIQ2HIAMlWAHQfhynRJG0Z1Gmv74L6g+jKNIPl1Civ9cBZfpWS1HX4ijTzz6aUL9PoExfWAX160BpNhX1mwRKtNZSME6vnwiCZfpqezwyn2krnU+RnnkKJfr2a8GJ19YUtR3Ef94KFYleXVMmDaVRUF8pTN1a5Lfn0nCodhUyF6/B60Buz70J571z8J53AW7MNwAWsNfbJbKX86TDHYs73Jo2zaRjc84dx+LccmzLSnKrQaTvyM1Rdh5Y1istPu6XqrrN7RmTp0x79qB+LO8Vn8hldb+se9lsLqsfXdar+Zxe9qteteAX9UrOKx/L61OVXE6vnDhaXcxVl82yV8iaXRczctn/ZMUv7tPm0GYcFSNB40x8HgQthiKCjaOTIyjbMRRpLYMTxjiNMfJw5+ls8EVrGfYy2aYqzwG+Aews4CntJCaZM1CwhYnJMcSLIGNsitDfpsOa472aZ3CeuXiHsaMbRjGOkrP/QBJ3G7uoyPDSRmwU4WxuO4U7jInOmTLGULR5RevGsI83I2Zxk9tDmMUjeD9b6AyAnBS0OEpIZiIMpb6ROH8ZR/A0gjD0t3jQE/00wUY0OVRvFtmpLdBMDaGDnX3sqmfC7PXMRiGnM+zsdrF/H+rsrn/GdUVL9A/0oMAe1Q7jg+yBAS5Oo6XdMzD8PrAOpEJqib0sMwGK9MIvwPxNnQcssobQeQT6t0X2zDYl3IVjX8VHUKSXfRYs8SD9ZZ/9vNXfZhikexFwWXv63y6P+9i9A2F/uznsgc3RWxOo0RDrP1ZAFW+RBqwT+zlRCGVn+ieQkKAw+Y44EhiElePpPfXVQK64e4+Hct2114kq6a7RIML/SqrprjZUufv9/zxP6otmszl25IP0fMeQPgIvAaxCwV8/feWxL91UaBVa7nzg2Wy23cORcsM1RPrJ7oU7e6/56NLyUHhtyUMJlmCJ/TkA2a/mgA==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVk+IG2UUn/fNJPPt291s+tnS6SAy3YOkA1O/mdmkm644yaIogtCih9zstElNZM2EJGK3VIhuA0pa2loP7h6k0oMVLEhRlD0JQkkhwirqQSqiFlplhcWDp4IyM8kmbiqImMV3mTfve/9/b958OEEhDgpokAAObM/mG+EwCxk4BDmoQANA/XmSkrikNgBleuY0KLfGUaK3zgFK9OMlX/j2Wlz5Iooy/ezDKeWnGMp0aRmU73xmdQmU72Mo0dZaHGV6NjSX6bn1yVD+btP307wIKNKzL6BE3znvu2xcBGXdd3A+ZCR6tQnTerxdUs6UEncW+N25DBxqfQm5a1/BG0Duzr0Fl91L8L57BW5m2wDz2C9vlezlPGlz2+Q2N2cMI2lbnHPbNjk3bcs0k9xsE+lHcnucXQaWdysLz3qVumZxK2XwtGHNHtSOFd3yc4W85lU1N58v5LWji1q9WNCqXt2tl7yyViu41WNFLVErFLTai0frC4X6olF1S3mjp2KEKvufr3nlfeocWoxjXI/RKBNfBUGNoIhg4fj0GMpWBEXayuGUPkkjjDzZPZ31H7SVY6+TbcryEuCbwC4AnlJPYpLZQwmbGJueQLwGMkYShP4+E+Qc7eecwixz8D59R8+MYhQle/+BJO7Wd1GR4eqmbWhhby07jTv0qa5PGSMoWrym9mzYR1sRM7nBrRH04il8lM13G0BOCmoUJSSpEENpoCX2X9rhn4YQBvom92uin8bYmCoH7O0yO3UPNNMjqGDnwHSt5ILoK7nNRJo5dmG7pn8fauyBfzbrcTU22NCDAntaPYyPs8eGZnEGTfWhoeYPgHUgHYyW2I+S8lGkV34D5m2p3J8icwSVh6D/UGYvb1PAXTjxbXQMRXrdY/4e98Nf99iv9/psRjF0pwEX1Zf+7fJ4hD08ZPa3m8Ma2hz9NYEqDbD+owGKeIe0YYNYr4hCQDszv4CEBIXp98QxXyA0jmf2rCz7dMPZezygbxxrgyiS5uhtIvyvqJ7pcSOlB6/+53HSn3c6nYkjH2SyXUHmCLwGsAwlb6N545mvnXQgFdacrK/Z6aw7h0PmpqOL9JPd8/f3f/PhveWJ4OZShAqcgBPszwEAS3zi1g==).

## Other builds of this spec

- [Subtlety — Raid](../research/raid/builds/subtlety-open-raid.md) (20/0/31, 676 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005303103014--3021013312113211501-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-14 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

