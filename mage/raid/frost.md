# Frost Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frost

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Frost — Raid](../research/raid/builds/frost-ml-raid.md)** (21/0/30) — [open the talent tree](https://talentsforever.com/mage/60/053005003000311--055500031100030025-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Frost — Winter's Chill), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Arcane Missiles** when Missile Barrage is active
2. **Ice Lance** when Fingers of Frost is active
3. **Frostbolt**

**Frostbolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Fire Blast**: in the last 3 seconds of the fight, when there is no time left for another **Frostbolt**
- **Presence of Mind**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frost in a raid is a **Frostbolt** caster that cashes in two procs: free **Arcane Missiles** from **Missile Barrage** and instant **Ice Lance** casts on **Fingers of Frost**. One **Fire Blast** in the last seconds of the fight uses time no **Frostbolt** can fill.

**Why it works**

- **Arcane Missiles** on **Missile Barrage** comes first. Each **Frostbolt** that lands has a 20% chance to make your next Missiles free and twice as fast (the full damage in 2.5 seconds), and they are about a fifth of your damage in the simulator.
- **Ice Lance** on **Fingers of Frost** comes next. Each **Frostbolt** chill has a 15% chance to treat your next 2 spells as if the target were frozen; a frozen target takes 300% more damage from **Ice Lance** and **Shatter** adds 50% crit chance, so spend both charges on **Ice Lance**. With both procs up, the simulator measured the free Missiles first slightly better (0.2%).
- **Frostbolt** fills everything else: 2.5 seconds with **Improved Frostbolt**, and the spell that rolls for both procs. **Winter's Chill** needs no button: in Forever it is your own debuff, each Frost hit adds a stack (+2% crit to your **Frostbolt** and **Ice Lance**, up to 5), and steady casting keeps it full.
- **Fire Blast** waits for the last 3 seconds. A **Frostbolt** started then would still be casting or in flight when the boss dies, while **Fire Blast** is instant; the simulator measured this 0.5% better. The rotation search kept it out of the rest of the fight: no Frost talent improves it, it costs more mana than a **Frostbolt** (340 against 290) and it rolls for neither proc.
- **Presence of Mind** at the pull makes your next spell instant. Its cooldown is 3 minutes, so a 3-minute fight gets one; in a longer fight press it again when it is back.
- Mana: the list uses your mana gem (from **Conjure Mana Ruby**) as soon as you are down to 80% mana, and **Evocation** only below 20% mana with more than 25 seconds left. With a raid's mana buffs the simulator never needed **Evocation** in a 3-minute fight.

**Caveats**

- Several targets: this list is for one boss, and the simulator's raid fights are single-target. For packs, **Blizzard**, **Cone of Cold** and **Arcane Explosion** are your area spells.
- Moving: **Frostbolt** needs you to stand still. **Ice Lance** and **Fire Blast** are instant, and **Presence of Mind** makes one **Frostbolt** instant.
- Threat: the simulator ignores it. On a fresh pull, give the tank a few seconds before your opener.

**When to change it**

- In the last 3 seconds, cast **Fire Blast** instead of starting a **Frostbolt** (the Advanced line above).
- Without a paladin's or shaman's mana buffs you run dry sooner: below 20% mana with more than 25 seconds to go, channel **Evocation**. Any later and the mana comes back too late to spend.
- If you must move while **Fingers of Frost** is up, spend the charges on **Ice Lance** as you go: it is instant.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 680 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 665 | [21/0/30](https://talentsforever.com/mage/60/0520050031003101--055500031100030025-6) |
| Phase 1 BiS | 685 | [21/0/30](https://talentsforever.com/mage/60/0520050031003101--155500030100030025-6) (ties this build) |

**The gear** (average item level: Pre-BiS 62.2; Phase 1 BiS 65.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Shroud of Arcane Mastery](https://www.wowhead.com/forever/item=22330) · *Blackrock Depths* | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Netherwind Pants](https://www.wowhead.com/forever/item=16915) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Elemental Attuned Blade](https://www.wowhead.com/forever/item=20698) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMVE9oI1UYz/dmmry+/ouvqNOhh2exJYaOvEyNtD2YpCe1iBU8iAftSzJJRuJMmJnY9mSrLUgPVfRU0UMLokL6h55qj2olLVF60UoVEUXcw8KW7tLLXpaZNJvDXneX/cHMfN/v+37M9wc+0o0hCgowiAEHOnDXQxzGIQ0z8AZUYBFArYUxjmLVIRF8ewuU/7qIjD/cASLjv2/2EBkfbAMJ47ql/NtLIvj7r0D5o5dI+LBIZPzXZQ8J44uCr4rg3RooH0eIjH/Y9uXHG0Ak/IFBJPzJuySCzzZAqfcTGX+37QcuykOjeNmM1k329RcQ+2UN+GV2ZvNHWAW0bH4K6DL7Dfyf2YfaKpzAmjlF2h0doKd5Uuc8yflYIngSmsaTyST3nYT/5lxP1hGcoK5/0I5MB1WVPBbvwzJF2ZAaIR1EGufDageRovUXqKyiyRAdUxMkRkeCPKmdp/PhgOqg6OUWlXR9Kf7sLVoDugIinzfyTOf68xqf0PTxSZZxcsIy2Cum65plw2W2xUTLY1PCcUTRYBXHzo2yYlU4vjy7wETVES+505Y9ZzHXZoJlq2Y5z+ZMr2RXvXv0lvGe4bCccD2XmZ46RBT6BOk8lsNExrfOEOncgytT9b9LPwF9XO1v0V8eKAF943Savk+FqJTftites4sE17g+yXIlYRWNPLMd1mwxu8C8ksEc2xOeaVvMNYSTK7GYaxis4NiupznCzGutuNaMP/uOa1vPqCqJxntxOBhjmMgEjblBAb8fAl2Fh1HBMBmMq34Fb4ZUuof6sNTeaSLBg52evqpI11AdzpG+JIUCPJfe9AdJEIahb6VOnwotFtIDn6/7OEo9VQjwW0o/R4rMUvE6Cj1S8NIt64FiZOu+/2fi50aj0T27m85cEelZ+AhgHUz7fOXo9V9TEwEbOkll/MxG43rqtabxZyou4f0npwbbZ6N5+l4Mjl8JKjAP8/TOAK0TBeg=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMVE9MI1UY7/dmaB8PhPqIOkw4PImQ2jDmzdQa4GBbTioxYuLBeFBe24GOITPNzFTgJJiSGA6YQHrA6AGiURNQ5IScjP9StCoXxX8Ho9nsHkiWZDdcNtlsZkq3h73ubvaXzJvv/X7fL+/73ks+0o0hDgowSAAH2n97hziMQham4FUowxKA+mUU4zhW50kM39gF5VIXkfHNdSAy/vfaQ0TGf24BieGjGij/95AY/uZjUP7uITI+3Qpyvq4F6kY1NMbw3g4o78WIjH+qBeq3nwdrdQOIhN8xSQz/ugJKvY/I+KtQ+agGgyO4asXrFvvkA0j8sgb8PD+1/R2sAqpa64DO85/C5dwB7KzCMaxZE6Td1iF6gqcNztOcp/Tw0zVNT6fTnPMU18OVG+k6gmPU9R/6QqYDqkoeTvZimaJ8RI2RDiKN8iG1g0jx+rNUVtF4hKZUnSTocJgntfMMPhRSHRS90KLSXmDFG6/THaArIIpFs8gMbjyj8THNGB1nObcgbJO9aHmeNWd6zLGZaO3YhHBdMWuysusURthsRbiBPb/IRMUVz3uTtjNvM89hguUr1lyRzVt+yan4d/ht8y3TZQXh+R6zfHWQKPRR0vmjHCUyvv4XIp37cBGqwX/5B6CPqH0t+sNDJaSvnkzSt6kQ5bk3nLLf7ELnGjfGWaEk7FmzyByXNVvMLzK/ZDLX8YVvOTbzTOEWSizhmSabcR3P11xhFbWWrjX1p970HPtJVSXxZA+OhtcYJTJBKS8s4I/vga7C/ahgiAwk1aCC1yIq3Ue9WGq/qa7z8E1PXlKkK6gOZ8hYliIhns5uBxdJEIbBz6TOgIoszWT7398McJR5fCbE7xnjDCkyyyTrKPJAwc+2onuK4d27fs7Yz41Go3t6L5u7ILLT8C7AJljO2crRK79lxkI2cpzJBZmNxmnm5WbwTyYp4YPHJgbaY6M5/54LJ2AJyrAAC/TWAGF3Bew=).

## Other builds of this spec

- [Frost (optimized, another mage's Winter's Chill)](../research/raid/builds/opt-frost-raid-raid-dps-extwc.md) (1/13/37, 646 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/1-2330203-0555000331021301251-6)
- [Frost — Winter's Chill](../research/raid/builds/frost-winters-chill-raid.md) (21/0/30, 612 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/054005003000211--055500033002100105-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

