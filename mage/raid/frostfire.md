# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-3550000123013303-2135000301113002-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Frostfire — Fingers of Frost / Ice Lance), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Pyroblast**.

**Then press the first one that is ready**, top to bottom:

1. **Scorch** when either the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 10 seconds left and the target has fewer than 4 stacks of Fire Vulnerability
2. **Pyroblast** when Heating Up has 3 stacks
3. **Fire Blast** when the target has fewer than 2 stacks of Fingers of Frost
4. **Frostfire Bolt**

**Frostfire Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Scorch**: in the last 3 seconds of the fight, when there is no time left for another **Frostfire Bolt**
- **Evocation**: when you run low on mana (about 1 time a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frostfire is a Fire list whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost, so both trees' talents apply, its chill rolls **Fingers of Frost**, and its crits stack **Heating Up** for a 1.5-second **Pyroblast**. **Scorch** keeps Fire Vulnerability at 5 stacks and **Fire Blast** fills between casts. **Ice Lance** is in the build only because **Fingers of Frost** requires it: the list never casts it. 772 DPS in a full raid on the simulator of 2026-11-11, 10% behind the Fire page.

**Why it works**

- **Scorch** keeps Fire Vulnerability at 5 stacks (**Improved Scorch**: 3% more Fire damage per stack for 30 seconds, and **Frostfire Bolt** counts as Fire) and refreshes it under 10 seconds left, a wider margin than the Fire list's 5 (+2.2% in the search), between casts unless the stacks are under 4. About 14 casts and 7% of the damage. Trinkets and the other cooldowns wait for the fifth stack.
- **Pyroblast** at 3 stacks of **Heating Up** (12 casts, 22%, and most of **Ignite**'s 13%): crits from **Frostfire Bolt**, **Fire Blast** and **Scorch** cut its cast by 25% each and **Fire Blast** adds a stack on every hit. One hard cast before the pull.
- **Fire Blast** (21 casts, 17%) every 6 seconds with **Improved Fire Blast**, but only while fewer than 2 **Fingers of Frost** charges are up. A proc treats your next 2 spells as cast on a frozen target, where **Shatter** adds 50% crit chance: the list spends both charges on **Frostfire Bolt**, whose crit starts **Ignite** and a **Heating Up** stack, and holds **Fire Blast** until a charge is gone.
- **Frostfire Bolt** fills everything else (40 casts, 41%): 2.5 seconds with **Accelerant**, 370 mana less **Frost Channeling**'s 15%, a 40% slow, **Ice Shards**' doubled crit bonus and **Critical Mass**'s 6% crit, and one cast rolls for **Fingers of Frost**, **Heating Up**, **Ignite** and **Master of Elements**' refund at once. It is checked against the lower of the target's Fire and Frost resistance.
- **Ice Lance** has no line: on the same **Fingers of Frost** charge a **Frostfire Bolt** is worth more than its 136-160 damage, and the search dropped the **Ice Lance** line in its last passes. The talent is the one point **Fingers of Frost** requires.
- **Fire Power** adds 3% Fire damage per Fire effect of yours on the target, up to 12%: Fire Vulnerability, **Ignite** and **Pyroblast**'s burn count; **Frostfire Bolt**'s own burn, a mixed school, does not.
- Mana: your mana gem (from **Conjure Mana Citrine**) whenever it is ready, two mana potions, a Demonic Rune, **Master of Elements**, and **Evocation** once a fight (an 8-minute cooldown). In a 6-minute fight the simulator's DPS falls to 306: this list is the mage's most front-loaded.

**Caveats**

- **Fingers of Frost** charges go to the next 2 spells you cast, whatever they are: do not spend one on a **Scorch** refresh if a **Frostfire Bolt** fits.
- Moving: **Fire Blast** and the 1.5-second **Scorch**. For packs, **Flamestrike** and **Blizzard**.
- **Frostfire Bolt** is new in Forever: its numbers are the simulator's model of the tooltip, not checked in game.
- The simulator's boss resists nothing. Against Fire resistance **Frostfire Bolt** keeps working (the lower of the two resistances), while **Fire Blast**, **Scorch** and **Pyroblast** lose damage.

**When to change it**

- In the last 3 seconds, **Scorch** instead of starting a **Frostfire Bolt**.
- Out of mana with the fight going on: **Evocation** if it is back, else **Scorch** (150 mana) keeps the stacks and **Heating Up** moving until a gem or potion returns.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Fire | 29 | Accelerant 5, Incineration 3, Ignite 5, Improved Fire Blast 2, Pyroblast 1, Heating Up 1, Improved Scorch 3, Master of Elements 3, Critical Mass 3, Fire Power 3 |
| Frost | 22 | Frost Warding 2, Improved Frostbolt 1, Precision 3, Ice Shards 5, Frost Channeling 3, Ice Lance 1, Arctic Reach 1, Ice Block 1, Shatter 3, Fingers of Frost 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 798 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 821 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-12) |
| Phase 1 BiS | 842 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.6; Phase 1 BiS 63.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Sorcerer's Leggings](https://www.wowhead.com/forever/item=226933) · *sold by Mokvar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Second Wind](https://www.wowhead.com/forever/item=11819) · *Golem Lord Argelmach, Blackrock Depths* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVl9oHEUYv292m5v70iaXqdbtNg/T05hkk0v2T1KSCOZaEGutpPgkItq9293c6ub2uN2U9q3aPkjRBGqpJCpIUPxbCxWkyZv34vkiwQd98CGhUhQpaAIWRBCZvaSNL31rfMgHN7PzffP7vpnf993MYCeFLCjAoQdOQhmqcBbgdYD3AT4GYLsTKxHWEVBnOijNUjXCNP37Cig3W1Gm564CyvS3S6J9ZzmLLbRRUX5uwzStfwjKT20o0XoFZXpzFjBN/7y1R8Ba6GJZmU2jTC8vZ1GmM7dE+9VyFiX62QuYpr9/AUpjL8r0jVlAia4Huf5sw+/5bgb028UTby7ABSDn/YtAbhfngfxy+FOgH70Ln1+AGX8VzvtHaLJuKMASyeWHhod1XdcN00p+Vt40LKGxdMMwLF03GwSWSesNcqkdH0GqtqBM/7oIOeUaeZBKLDNPNjTCgiRvsCpz7WrwUliNuambh/KGnreMMV4q25VJ1+FhjduO4zq8eIbHZZfXwtiO/bDCI9eulcq8J3Jd7tXCKPb8mpuv2b6T35yTb84ZeDkKK71qWt2FUvabx9kcYWuwNZbwG3qeX/LtgEf+1HRgx2GtO+JT9qQ76FSjQbsaRIOeVxywq0HijtsxHx4quXbpkDXCbSesxq7De+5EDuxJbk87fsxtL3ZrzaW7+apfGeN95oDexb2wqXUrce1Md8SLbhTz4rQfONyvcJt700HAxXb6eZ8xYHTxOBRIs4n044gHfiSCJpionxt6v67r3PMny3HEE4ZcJ+ImtysOt3rVh3Gv1kElRp5PqZl1aSMPN6AVM0+cCksJq2wFtisdp3CKvYKPqaOoagqV2J46IMr06pfASJaIXCEM4wFtv7At/ceWlI6hY7+q3QM8hLtziHQddqFEVyaER7oywS7vzOxz7NRUCqy9DrvvMqXABtFjKfbJziTGwl7Wjfu0ByiwTB3E32JtUWnSYuGeXCtm1mHLoSV69vbO5OogKto+KrHWOlCU6XtLymYBmaKjP06wc9t2gKiY1dpoCyPHUiIvSKxI9PTr+tPbfKnQlQlF0hZg60H6lPokdjK1WUDXkgJaajyDme9l8bm4dtzs3rgeF9eO44HXQEGJvvWi2qG1iz0VU2oad6E0OtrFjqlHsU/tbbq6g28OF2BzeDfIPXz9ShrwBzFflVKJDBUSPBIKuX9IRqhSZ73C/vk5Id+OH/QS+WHcXCWKzMe16yT1v0hc2Py6r/LolfsWZzRpn/2gcHhDUTgp3oZzkAxSq+OaRK8/dGTLE1KHESjAUTgBz0EZqnAaTpN/BwBZNYau); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG0UU9pt14vFLmjhTKNttDlNDSLKJk/1JqiRIxK2EKKUoFScEEnTt3Y0XHO/Ku6naW4EcUAUJSltQAkgoAvEjClK5NLnhC0ZIqOIAB4QSFSoQF0gOlRBShWadpOHSW8MhT/LMznvzvTfzveeZwU4KGZCBQw+chhIEcB7gNYD3AT4GYK2xlQjrCCizHZRmqBJiiv5zBeSbLZikt+cBk/SPS6J953oGm2m9Iv/Shila+xDkn9pQorUKJunNOcAU/flyDGumyyV5LoVJ+u1l2G5nLgJK9M0pTNE/Pwe5vh+T9PU5ofv1uWx/pu71fDcL2q3CqTeW4AKQGW8eyK3CIpDfjn4K9KN34bMLMOutwYx3jMbrhjyskGxuaHhY0zRNN8z4Z+YM3RQaU9N13dQ0o07gOmm5QS6140NIlWZM0r/nIStfJfdTiaUXyaZGWJDkdBYwxwrKL/hBxA3NOJLTtZypj/FiyapMOjb3q9yybcfmhXM8Kjm86kdW5PkVHjpWtVjiPaHjcLfqh5HrVZ1c1fLs3NacXGPOwIuhX+lVUkoTSpmvH2ULhK3DzljCr++6XtGzyjz0pqbLVuRXu0M+ZU06g3YQDlpBORx03cKAFZRjd9yK+PBQ0bGKR8wRbtl+EDk279mOXLYmuTVtexG33MipNpbu5AKvMsb7jAGti7t+Q+tUouq57pAXnDDihWmvbHOvwi3uTpfLXGynn/fpA3oXj3yBNBpILwp52QtF0BgT9nNd69c0jbveZCkKecyQY4fc4FbF5mav8iDuVzuoxMizCSW9IW3m4Qa0YPqxM34xZpWtwm6l4wxOsZfwEWUUFVWmEttXA8Qk/eJLYCRDRK4QhvGQelDYVv5ji0tH17BfUe8CHsLWLCLdgCaU6OqE8EhXJ9hbezP7HDtVhQJrr0HrHaZk2CR6LME+2ZvEmNjLuvGAeh8Flq6B+FusL8sNWkzcl23B9AbsOLREz97em1wdRlk9QCXWUgOKSfreirxVQIbo6I8T7NVdO0AUzKhttJmREwmRFyRmKHr6Ve3JXb5U6OqELKlLsPMgfUJ5HDuZ0iigq3EBrdSfwvT3SfG5vH7S6N68HpfXT+KhV0BGiV58XulQ28WeCgklhU0ojY52sRPKcexTehuutvGN4RJsDe8EuYuv30kd/iLGy1IilqF8jEdCIXubpIUqcd7NH1xcEPLN+GE3lh/GjTUiJ/m4eo0k/heJ8ltf91QevnLP4ozG7dMf5I9uKvKnxdtwAeJBYm1clei1B47teEJqMAJ5OA6n4BkoQQBn4Sz5dwB+sYWs).

**Points that do nothing for this spec:** **Improved Frostbolt** (1) only counts toward the points the tree needs before **Arctic Reach**, **Fingers of Frost**, **Ice Block** and **Shatter**; **Ice Block** (1) only counts toward the points the tree needs before **Fingers of Frost**.

## Other builds of this spec

- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 789 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-3551000113013303-2135000301113002-12)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (7/31/13, 724 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0410011-32510301230133031-20350003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-17 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

