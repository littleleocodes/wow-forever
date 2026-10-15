# Fire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Fire

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Fire — Ignite / Hot Streak](../research/raid/builds/fire-raid.md)** (12/34/5) — [open the talent tree](https://talentsforever.com/mage/60/005205-23550020130133051-005-6)

## How to play

**Then press the first one that is ready**, top to bottom:

1. **Fire Blast**
2. **Scorch** when the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 7.5 seconds left
3. **Pyroblast** when Heating Up has 2 or more stacks and Heating Up has under 3.5 seconds left
4. **Pyroblast** when Heating Up has 3 stacks
5. **Fireball**

**Fireball** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Scorch**: in the last 3 seconds of the fight, when there is no time left for another **Fireball**
- **Combustion**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fire keeps its own **Improved Scorch** debuff at 5 stacks, fires **Fire Blast** on cooldown and casts **Fireball** in between. Crits build **Heating Up**; at 3 stacks **Pyroblast** becomes a 1.5-second cast.

**Why it works**

- **Fire Blast** first whenever it is ready: every 6 seconds with **Wake of Fire**, instant, and **Incineration** and **Critical Mass** make it crit often, feeding **Heating Up** and **Ignite**. The simulator measured using it on cooldown, with no mana saving, 3.7% better than the rule it replaced.
- **Scorch** keeps Fire Vulnerability at 5 stacks. In Forever **Improved Scorch** is your own debuff: +3% to your Fire damage per stack, for 30 seconds. Build 5 stacks, then refresh it once 7.5 seconds or less are left so a long cast cannot let it drop; the list shows only the stack count, but the early refresh is part of the rule (the simulator measured 7.5 seconds 0.4% better than 5).
- **Pyroblast** waits for 3 stacks of **Heating Up**. Each crit from **Fireball**, **Fire Blast** or **Scorch** takes 25% off your next **Pyroblast**'s 6-second cast, so 3 stacks make it 1.5 seconds: your biggest hit for its cast time. The list's 2-stack line is a last-chance rule: cast a 3-second **Pyroblast** at 2 stacks only if **Heating Up** has under 3.5 seconds left or the boss dies within 6 seconds.
- **Fireball** fills everything else: 3 seconds with **Improved Fireball**, about half your damage, and each crit also starts **Ignite**. The list stops starting it with under 3 seconds left, when it would land too late.
- **Combustion** at the pull and whenever it is back (3 minutes): each Fire hit adds 10% crit until you land 3 crits, which fills **Heating Up** fast. It shares its cooldown with **Presence of Mind** (client data), so a build with both gets only one of the two every 3 minutes.

**Caveats**

- Mana: Fire runs short even in a full raid. The simulator uses your mana gem (from **Conjure Mana Ruby**) at 80% mana and a mana potion whenever it is ready, and still runs dry now and then; **Master of Elements** refunds 30% of a spell's base cost on each crit.
- The raid list has no **Evocation**: in a 3-minute fight with raid buffs the simulator measured it slightly better without (0.2%). In a longer fight or without mana buffs, channel it when nearly empty with plenty of fight left; the simulator's list for playing without raid buffs does so below 10% mana with more than 25 seconds to go.
- Several targets: the simulator's own Fire list adds **Blast Wave** and **Flamestrike** at 3 or more targets; this build has no **Blast Wave**, so use **Flamestrike**.
- The simulator's boss resists nothing. Against an enemy that resists or ignores Fire, every spell here loses damage, and **Frostbolt** is your fallback.

**When to change it**

- In the last 3 seconds a **Fireball** would land too late: cast **Scorch**. The simulator's list uses Rank 1 there, the same line it falls back on when you cannot afford a **Fireball**; Forever gives ranks that low only part of your spell power and fewer talent procs, so use your top **Scorch** whenever you have the 150 mana.
- With 2 stacks of **Heating Up** and the boss dying within 6 seconds, cast **Pyroblast** now: the third crit may never come.
- After an add dies, your next **Fire Blast** within 30 seconds gets +50% crit chance from **Wake of Fire**, a likely **Heating Up** stack. The simulator never kills anything, so this is extra.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 685 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 645 | this build |
| Phase 1 BiS | 698 | this build |

**The gear** (average item level: Pre-BiS 60.3; Phase 1 BiS 67.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Arcanist Crown](https://www.wowhead.com/forever/item=16795) · *Garr, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Spritecaster Cape](https://www.wowhead.com/forever/item=11623) · *Houndmaster Grebmar, Blackrock Depths* | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair* |
| Chest | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Inferno Gloves](https://www.wowhead.com/forever/item=18408) · *Tailoring* | [Gloves of the Hypnotic Flame](https://www.wowhead.com/forever/item=18808) · *Molten Core* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Ghostweave Pants](https://www.wowhead.com/forever/item=14144) · *Tailoring*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Netherwind Pants](https://www.wowhead.com/forever/item=16915) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Arcanist Boots](https://www.wowhead.com/forever/item=16800) · *Lucifron, Molten Core*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Searing Golden Blade](https://www.wowhead.com/forever/item=12260) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMlE1ME2kYx/u8M0zfPnxsd3azDBMOsyS7YZsd9u3MDlAOtHDa1QOYaGK8QEsHO4ptbXvAi0GsifEAhBvGiyRGNPKReAFOBjUpphouaqJGjR+BgwfUhMR4Me+UQiIewfg/vf0//77PM7+8ebCKgh8U0KARGMh1W78Ig1aIQDcchjQMAah5SqmfqifRSz9Pg/K2EkV6dhZQpC8/VqNAV4+gRIcTyusa9NKlK6A8rUGRro3yxPONapTorST/l5fO3QBl1IsivT3Di/cuAwp02EaBjp1Aib7pUQq/oEgXZrj/YaDhb5p3/AVHu3oJGh+MANuIdU/egQtA8s44kI3YFKx2zMP1KViBEacTtz9okdQzZhnM0g3TshgzWNBkQdNkVlBnzCoQWCGVr8iYJB+Xe6PpgZ5UOqcZzGjWWUg3Wtq0vkQ0edSOa6mMFo3H7bgWO6XlEraWSeWiOSeV1LJ2NNOX0Bqztq31Oxlbz0SduF4u66Vy07FsKvmX6lUrUKCPu+RJ+Ea31l3u1o6WauJvgV+pIPuWQEKRzt4EPgKChXWBWirKvsUtn6KEYkuTleUJ+qJLFlXS5pHrVRV/DvxERZnEPKoXK1BoZX/wjL/QvoNakOkstBfU/HlHXviaGu+229QO4X75f5eaVKb2fkEpUTPwH1VHf6CGCjLZ51ElFJE0Z12WQpklT7ssTc6SO5/GQW5QNfdS2HGpuZU5/R1gqu740vb4ZmnGJ3dB9m0+0HytIqyRAqwT44zgcfVvZJI/FCQUGq4JPm55hvojdRcnuJbDv/e7ehQ21okiauFAgXh+KOUi5dOe6s/pXe8Tul8sFqt65yIdm0akF84DTICTWj+3fPBhOOS6npVwB08Wi+/CB0qHZ+GAQOdrO+u392Fppf/nLvUEpGEQBuUvAwBQLENQ); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMlE9IFG8Yx/d5Z9x599Gfv+0tchw8TEJhS2PvzjTqenBXT/05aFDQLXfdsZ0Sd9ldwi5huUJ1sFA8WB1CiCzoDwShnkIKVtrKSwUVFEXUoYMVSF0iZtZdITtq9D0M73zf77zPMx9eHqyi4AcZVGgADqy2/EY4tEAEuuAQpGAQQDlLKfVT5ThK9NIQyB8qUaQ/RwFF+vbbfyjSe8OAEp0fB/l9NUp07irIr6pRpN/dzP1xZ3cs534o0StDIJ+XUKSPxqH8zI0BCvS0hRJ9OgxyfiOKdOaW433tq99Bc7Y/b6vXLkPDkxHgS7GuyQdwDkjOHgWyFJuCj+3TcGMKFmDE7sCVv5oldZybOjc13TBNznUeNHjQMLgZ1Dg38wQWSOU7csHLjrHuaKrvcDKVVXWuN2k8pOnNrWpPItp/xIqrybQajcetuBo7oWYTlppOZqNZO9mvZqxouiehNmQsS+2105aWjtpxrbStFbcbj2aS/dsVSalAgb7oZJPwh2ota1ytDU3FwM2BTVRgvjnwokhv3wWnBQQTawM1VGS+2bJP0Ytic6OZcRL0TScTFdLqYXWKghsC/1ORkZhHkbAChRa+1cn4822rqAW5xkPrQc2fs9nM79ScamtN7SDuY3tcat4StS8zcpGajjsVDf2BaiowstejeFFE0pRxWQollk7aZWk4LB3nxyiwekV1D4VVhxrlzMm/AFNx2/eutG8Ue3z5EJhv+YLmamThE8nDItFPCR5XuyKTzkVBQqH+uuBzLM9gb6T24oSj+fCWXlfPw/oikUU1HMgTzz+lbKS0Wldtu7nmdUKPC4VCVfedSPuyEemGMwATYCcXh+cPPAuHXNezEG53koXC5/D+4uJ1OCDQ6ZqOupV5WJzru93JnoAUDMAA+zUAkVVC7Q==).

## Other builds of this spec

- [Fire (optimized)](../research/raid/builds/opt-fire-raid-raid-dps.md) (14/32/5, 685 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/24020501-23550000130133051-005-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

