# Demonology Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Demonology

**✅ Recommended** for raid (the best warlock spec here, or within 3% of it).

**[Demonology — Raid](../research/raid/builds/demonology-ml-raid.md)** (2/31/18) — [open the talent tree](https://talentsforever.com/warlock/60/011-0025003031220301351-0550005003-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage), then summon your Succubus: Demonic Pact keeps the Imp's buff while another demon is out; **Soul Link**: turn it on with your demon out (it lasts while the demon lives).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Shadow Bolt**

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Demonology in a raid is a **Shadow Bolt** caster with two demons' worth of bonuses: you sacrifice the Imp for 15% more Shadow damage, and **Demonic Pact** keeps that buff while your Succubus fights. Then you keep **Curse of the Elements** and your dots up and cast **Shadow Bolt**.

**Why it works**

- Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours), then summon the Succubus and turn on **Soul Link**. **Demonic Pact** keeps the sacrifice while a different demon is out, but summoning the Imp again cancels it; the simulator measured about 10% less damage without the sacrifice.
- The Succubus earns her place: while she is out, **Master Demonologist** gives you and her 10% more Shadow damage, **Soul Link** 3% more damage and **Demonic Knowledge** 60 more spell damage at level 60. She takes 17% of your spell damage as attack power and 10% as spell damage, and her attacks and **Lash of Pain** add about 9% of your damage.
- **Curse of the Elements** goes up first: 10% more damage from every magic school for 5 minutes, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana: every tap is a global cooldown with no damage, and the simulator measured tapping at 5% about 0.5% better than at 10%.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (a 1.6-second cast with this build's single point of **Improved Corruption**) goes back up when less time is left on it than its cast, but not in the last 10 seconds.
- **Immolate** is Fire, so none of your Shadow bonuses reach it, and it only just pays: the simulator measured this spec better without it when it was recast to the very end, and better with it when you stop 20 seconds before the end. Start it when less than its 1.5-second cast is left on the old one.
- **Shadow Bolt** is the filler because every bonus you stacked is Shadow: the sacrificed Imp, **Master Demonologist** and **Improved Shadow Bolt**'s 20% after your own crits. **Decimation** adds 6% to it once the boss is below 35% health.

**Caveats**

- **Searing Pain** has no cooldown: the rotation casts it only in the last 3.5 seconds, when its 1.5-second cast lands before the boss dies and a **Shadow Bolt** might not. So **Demonic Brand** and the **Soul Fire** half of **Decimation** do nothing here: they are points on the way to deeper talents, and the simulator found **Soul Fire** a loss wherever it tried it.
- If the Succubus dies, summon her again unless the boss is about to die (6 seconds with **Master Summoner**) and turn **Soul Link** back on: without a demon you lose **Master Demonologist**, **Soul Link**, **Demonic Knowledge** and her own damage. Never summon the Imp during the fight: that cancels your sacrifice even with **Demonic Pact**.
- Summon her after your buffs, wizard oil and Spellstone (**Create Spellstone**) are on: in this project's model a demon copies its share of your spell damage when it is summoned. Forever lets the Spellstone stack with the oil, and the simulator measured about 3% more damage from it.
- On the move, **Bane of Agony**, **Curse of the Elements** and **Life Tap** are instant; **Corruption** keeps a 1.6-second cast in this build, so put it back when you stand still.

**When to change it**

- In the last 20 seconds start no new **Immolate**, and in the last 10 no **Corruption**: cast **Shadow Bolt**, then **Searing Pain** in the last 3.5 seconds.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 822 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, ElliotWood/Forever fork 2ce8265 (client 70291); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 801 | [2/31/18](https://talentsforever.com/warlock/60/011-0005203031220301351-0550005003-7) |
| Phase 1 BiS | 839 | [2/31/18](https://talentsforever.com/warlock/60/011-0005203031220301351-0550005003-7) (ties this build) |

**The gear** (average item level: Pre-BiS 62.4; Phase 1 BiS 63.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair* |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Stats](https://www.wowhead.com/forever/spell=13824) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Stats](https://www.wowhead.com/forever/spell=13824) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Felheart Gloves](https://www.wowhead.com/forever/item=16805) · *Lucifron, Molten Core* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Nemesis Leggings](https://www.wowhead.com/forever/item=16930) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Elemental Attuned Blade](https://www.wowhead.com/forever/item=20698) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMlU9oK1UUxnPuTDMn57V96RXpZFQYA+8RA1PuTJhn003Sroq4qOBC6MImzaRJaTMhyaLdVVtRRKroqlGwFUstWA2uqiv/BVOI0o2C1qoIogsXpUI2bmQmUwvWhQur72zuN985Z87vzsC9NIgQBRV0SIAAHvvziQkYhyzMwBNQhTUAbTuCUjSi1UjB3w9A/ekGybj+LpCMP/w2RDJ+vQMUxqOKuq2Qgh/vgnoyTBK2F0jG73pDFMbzotelYOttUF9USMbP9oZJxk/eAZLwaYckfGmZFPxmB9TOPSTj+37ifCkucKMc7ZT1vdcg8cUmiF5+5o1P4XlgG+WXgfXyb8HPky14fRcOoTV9DJvlKbrc1QcsLkzTEELYlkiJlGl5i5myTUPYtmcLkeow6Zjd+JG9qvAHtPtoJH6Tht4DIhk/fHaGs+iAFg60pQlK8Ns0kryJYc4eCWkKDZBk2nXfkjnLB9bD9i1NJqaO8JRm/sOeO+KWNkBStJfnssYmQn2a/nsv2lJjtk+z/gLwdeDFXHXpSbfa0C1h3TFE2rDGJ/T5Uq6y4BR0t6bnCgWnoOdX9UbJ0WtuI9couxW97uRq8yU9UXccveAsuxV3yV1YNWq5csG4KDL6RWOLdbfykBajaHIYJX9/YZKJ2T4q7s/yuKbTaPJelLmy6FkfzWrYZIHqL/zNv5KawhDWtZBOkOBjFEuOosxx0ftU37dBizRZIK/8B1HXgtT/i3l6iXl6FdMKME/bwGt/Q5m+Fkr0ZkY3XvnPZ+LB+aOcAn3SBlX6hXXgjFlPSSE/0tkmGyQiREln4ywL8X0p4iVCa8VsrLnlxVHmwaIfX2WsM6bKeibZYaG7KhrZC3WtcfvgX5+T/rzb7Q7OtbKTgZGdg+cAtqDsnj1z9PiXmbTvho4zk15lt/tr5rG++DaTlPBwdOr+y2O6f91M+xdOCaqwAiv8jwEAK8RiSg==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMlU9IHGcYxvf9ZnS+ff23fqU4O21huqBsF0a+mWWs62VXT1J6sNBDwUPddUd3xe4su0vRm60rLaVYUDy4LbSI0gq1LD0U21MTIqxkk3hJLkYSAiE55CAGvARCmNlRIeaQQ0zyHuZ75nnfd97fNwPzYSuFAMigQhg4sODpHeHQDwkYgS8gD3MAyrqfCgG/8jVK9MkWyPdbUKRPlwBFevdxG4r0nwVAie6ugPybhBK9vAHyfjuKdGPeqfl/xcmuld1GiVb/BPknCUV6dQVOr+VlQIF+a6FEbyyAXHsHRfrvX453NB3itJwN1LLq779A+Poi8OPUyNoV+AFIObsE5Dj1BzwYrMKvG7AN1eE9WMwO4dnO/iMhrusa59w0eJRHdcNZ9Kipa9w0HZvzaI0Ie6TlHvlZYh8o72FnqAPb/gZ04L8bYSTQpDR72lA4hlkPdkY6aDMjn/gUCZtQ0M2ia4mMpDzrY7NbEZHInSyq6C/Z08e7lSYUAscpJipkwNegaTz3pC3aa7o08z8Cmwc2kcxPf2nnS6rBjT6NxzSjf0AdzyRzk1ZatQtqMp220mpqVi1lLLVgl5KlrJ1Ti1ayMJ5Rw0XLUtPWV3bOnrYnZ7VCMpvWToq0RlHvVNHOfaQEMRBpp4K7v2YUkZguKt0cZSFFxa7Iu1Rk0pRjXRpVaIV4qrGw9edJda5x40JIB5CzXgxGuqjI6JTzqu7sgOKvEE+e+w68qHipN4t5cIZ5cB7T8DAPdoAVXkAZuxBK6swMlJdf+0y6dfQpQ0/v74AsPCQ1OCTGN4LPjViiQloRkVJBJf0kAaFNwe8kfHMTiWBl1Ynd+IcTbtyKG4dEFtV4pEZ8b1WUEifqQqNn65XPiV2r1+utY9XEoGckxuB7gFXI2ocLu5/fjMdc17cXH3Qq6/VH8c8a4nY8ItDtrqH3z37TjSNn2D10MpCHGZhhzwYAmnthpg==).

## Other builds of this spec

- [Demonology — Demonic Pact](../research/raid/builds/demonology-pact-raid.md) (2/31/18, 816 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/101-0035003021220301351-0550005003-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-25 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)). Simulations, not in-game measurements. Do not hand-edit.*

