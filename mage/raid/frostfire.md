# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-1355000013012503-2135000301113002-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Frostfire — Fingers of Frost / Ice Lance), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Talents with no line below:** **Ice Lance**: taken because Fingers of Frost requires it.

**Then press the first one that is ready**, top to bottom:

1. **Pyroblast** when Heating Up has 3 stacks
2. **Fire Blast**
3. **Scorch** when the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 7.5 seconds left
4. **Frostfire Bolt** when your mana is below 30%
5. **Frostfire Bolt** when you have at least 10% mana

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Evocation**: when you run low on mana (about 1 time a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frostfire is a Fire mage whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost damage, so both trees' talents apply, and its chill lights up **Fingers of Frost** for **Ice Lance**. The Fire side adds **Fire Blast**, **Scorch** upkeep and **Pyroblast** at full **Heating Up**.

**Why it works**

- **Ice Lance** on **Fingers of Frost** comes first. Each **Frostfire Bolt** chill has a 15% chance to treat your next 2 spells as if the target were frozen; a frozen target takes 300% more damage from **Ice Lance** and **Shatter** adds 50% crit, so spend both charges on **Ice Lance**.
- **Pyroblast** at 3 stacks of **Heating Up**: crits from **Frostfire Bolt**, **Fire Blast** and **Scorch** each take 25% off its 6-second cast, so 3 stacks make it 1.5 seconds. Unlike the Fire list, this one never casts it at 2 stacks; the simulator measured dropping that line 0.3% better.
- **Fire Blast** on cooldown (every 8 seconds: this build has no **Improved Fire Blast**): instant, and its crits feed **Heating Up** and **Ignite**. Using it without a mana condition was the biggest single gain of the full-raid rotation search, about 5%.
- **Scorch** keeps Fire Vulnerability (from **Improved Scorch**) at 5 stacks, +15% to your Fire damage, and **Frostfire Bolt** counts as Fire. This list refreshes it once 15 seconds or less of its 30 are left, a wider margin than the Fire list's 7.5.
- **Frostfire Bolt** is the main spell: 2.5 seconds with **Improved Fireball**, and one cast rolls for **Fingers of Frost**, **Heating Up** and **Ignite** at once. Below 30% mana the full rotation casts Rank 2 (285 mana against 370): the page's line "when your mana is below 30%". The simulator measured this about 2% better than the old rule of stopping at 10% mana.
- **Fireball** (Rank 2 in the full rotation) is last: a stopgap for when you cannot afford even a Rank 2 **Frostfire Bolt**. Forever gives ranks that far below your level only part of your spell power; keep your mana up with gems and a potion so it rarely comes up.

**Caveats**

- **Fingers of Frost** charges go to the next 2 spells you cast, whatever they are: do not let a **Frostfire Bolt** use one up.
- Mana: **Frostfire Bolt** costs 370 at top rank. The list uses both of your mana gems (from **Conjure Mana Ruby** and **Conjure Mana Citrine**), **Master of Elements** refunds 30% of the base cost on each Fire or Frost crit, and below 30% mana the cheaper Rank 2 stretches what is left.
- Moving: **Ice Lance** and **Fire Blast** are instant. For packs, **Flamestrike** and **Blizzard** are your area spells.
- **Frostfire Bolt** is new in Forever: its numbers here are the simulator's model of the beta tooltip, not yet checked in game.
- The full rotation also opens with **Arcane Power** for builds that take it; this build does not, so skip it.

**When to change it**

- Below 30% mana, switch to Rank 2 **Frostfire Bolt** rather than stop casting it; a **Fireball** is a weak stopgap only for when even that is out of reach.
- Against a target that resists Fire, **Frostfire Bolt** keeps working (it is checked against the lower of the target's Fire and Frost resistance), while **Fire Blast**, **Scorch** and **Pyroblast** lose damage.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 799 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 789 | [0/29/22](https://talentsforever.com/mage/60/-1355000013012503-2035010301113002-7) |
| Phase 1 BiS | 793 | this build |

**The gear** (average item level: Pre-BiS 62.7; Phase 1 BiS 63.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Finger | [Brilliant Watcher's Signet](https://www.wowhead.com/forever/item=275982) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Alchemist's Stone](https://www.wowhead.com/forever/item=13503) · *Alchemy* |
| Trinket | [Alchemist's Stone](https://www.wowhead.com/forever/item=13503) · *Alchemy* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVU9oI1UYz/dmmvny9d/4LDpOWxgDlRhMeTPT1LZik/YkCKZ40os2aSZmRJKQRKi3KqVIwRaKKK09SLFUpVpRkNqLmItRUHpS0ENLd8suy8LuslDYy7LMpKVdNtd0f4dH3vv9Hr/v+/FlHvUhqKCBARGYhjyUYA7gY4AvAb4G4B0+yzx2BPSFdkQV9fdJwb2PQDtuJxmPPgeS8can3vrFvkpBrBe0K12kYG0TtP+7SMJagWQ8XgZScKdxTcEftkFbVkjG/za9m0s3VZLx532VJPzVJQVvfQ9a/UmS8e5nHv/Nenf4BbXuRv5eAnGSmfpkAxaBzbsrwE4ya8CuTXwLuLUO24uw5B7CvDvZcd5XEvZYOGba8bgQQpi2MK24sGOWsOPCFLYwTdMWwqoz2GftR2whxEvcSZfee7tYqhqWsIZjpohZ9pgxk08X3nGyRrFspLNZJ2tkPjCqeccoF6vpqlssGBUnXZ7JG5GK4xi5crFSzbllJ1ZOu9nYmSbW0Ay+WykWntcVvY0k9STTzNEcapkjLr7Fw7pBT0V7EHioBkGS8c4vmlcNga1723sr0KwqEW9dVf+meA0etbRaEsSbNMVfo84/ZSIZd34CztQ2ell/ifSohhLvrMEFohFMnPqjvSjzzr2HOKQgyS8OxiueCg9SvE/X6YloN8qcZQK6Qm0kjYgBj1Xr401DHW5ZqOrv41zW2ViALzSJVoy2wrjf7146794WAzpSMMLwt9qrvF/v9QXBc4EpBvyh8+genVPoR38k/2qMJF5N8fJlpRbyKoow3Epd9megXuCh03/CQUqTrrM63GbWh1LAx1Byw8uEGEL4Pgt5R4G5XPKZtVUPfySezfn4J2EdMk02EtFdFngsqCbPfrUUz33XMp9Rf339q+TE6UFy2nsTV8HfBA4TUQl3n5688HQKGIEkvAJT8AbkoQSzMMseDABara/e); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVU1oK1UUzrkzTU5O/8Zr0XHawhioxGDKnZmmthWbtCtBMMWVbrRJMzEjkoQkQt1VKUUKtlCl0NqFFEtVqhXd1G7EbIyC0pWCLlrUorjRx4PC25THnbS0j5dt+s7iMvd83+U75+PMvTSAoIEOJkRhFgpQhgWAdwE+AvgEgHf5KJPoGBhLnYgaGm9SCA/fAf20k1Q8XwNS8d8P5PrhkUZBbBT1P3sohPUd0H/vIQXrRVLxdBUohPvNYyH8cg/01RCp+NuOPLl+pJGC33qk4uL7kvjfF6A3HiYVb69L/NOt3shTWsOL/rwC4iw78942LANb9NaAnWU3gf099Rng7hbsLcOKdwKL3nTXVV8pOGSRuOUkEkIIYTnCshPCiduWIxOOsCzLEcJuMDhinX+wpTAvczdTfuPVUrlm2sIejVsibjsT5lwhU3zNzZmlipnJ5dycmX3LrBVcs1KqZWpeqWhW3UxlrmBGq65r5iulai3vVdx4JePl4peceJMz/Hq1VHzSCBkdpGhn2VaK1kjbFHH5FR4xTHok1ofAw3UIkoq3vtFlNQSOIbd31qBVVSLRvqp+TfM63C9pt8WIl2mGv0DdP6pEKu5/DZxpHfSs8QwZMR0V3l2Ha0DTmAQNxvpR5d2H92BIQVKfHk5UJQuP03zAMOihWC+qnGUDRog6SBkTQxLVGpMtTR1tm6na95NcNdhEgC+1sFaMt0N40O9euereEUMGUjDK8Lv683zQ6PcJwSuCJYb8oZNwn8Ep/JU/kj81RxL/SvPKTbkWlhVFGe6mb/oaaBR5+OJPOE7ryj+sAf8z+20l4MdIalt6Qgwhcs7CMhVYyKce29yQ8UPy8bwfvyTtE6arZjJ2wAIPJGqpy6+2xhOft01n3F9f/Dg1dZFIzco3cQP8TeAkGVPw4NHpa0+ngDFIwXMwAy9BAcowD/Ps7gAd6q9j).

## Other builds of this spec

- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 764 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-1355100013013303-2135000301113002-7)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (5/33/13, 743 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0041-23251030130135031-20350003-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

