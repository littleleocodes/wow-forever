# Beast Mastery Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast Mastery

**[Beast Mastery — Raid](../research/raid/builds/beast-mastery-ml-raid.md)** (31/20/0) — [open the talent tree](https://talentsforever.com/hunter/60/5320001505101251-00530502005--7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target
2. **Arcane Shot**
3. **Rapid Fire**
4. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Bestial Wrath**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast Mastery in a raid is **Auto Shot** and your pet with a short list on top: keep **Serpent Sting** ticking, fire **Arcane Shot** and **Aimed Shot** each time their cooldowns end, and send **Bestial Wrath** whenever it is ready.

**Why it works**

- **Serpent Sting** comes first so it never drops: on the training dummy it is about 15% of this build's damage, 20% more with **Improved Stings**. Recast it only as it runs out, since a new sting replaces the old one and its last ticks; the full-raid rotation recasts it only while you have 30% mana or more.
- **Arcane Shot** goes out every time its cooldown ends: 5.4 seconds with 2 points in **Improved Arcane Shot**, about 33 times in a 3-minute fight. **Summon Hawk** shares that cooldown, and the full-raid rotation gives all of it to **Arcane Shot**, so the build's **Summon Hawk** point is never cast.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) goes once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown, so the next **Aimed Shot** is cast under it.
- **Aimed Shot** is last on the list but it is not a spam filler: it goes out almost every time it can, a 2-second cast and then its 6-second cooldown, about 23 times a fight. The instants above it cost only a global cooldown.
- **Bestial Wrath** (+50% pet damage for 18 seconds) goes at the pull and on every 2-minute cooldown, twice a fight. **Intimidation** is in the build only because **Bestial Wrath** requires it; the full-raid list never presses it.
- Your pet is about a quarter of your damage on the training dummy. It takes 10% of your attack power and all of your crit (this project's model of Forever's pet scaling), so **Ferocity** and **Frenzy** keep it critting and attacking faster, and **Focused Fire** adds 2% to you both while it is out.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator's best rotation never casts **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** is the first thing to drop when you run low.
- Keep the pet alive with **Mend Pet**: Forever pets take no stat buffs from players, and a dead pet takes **Focused Fire** with it. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; players have measured this only at levels 20 and 30).
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant, so keep pressing them.
- The simulator starts **Aimed Shot** 2.5 seconds before the pull so it lands as the fight begins; in a real raid, start it once your tank has the boss.
- Watch your ranks: in the beta client (build 70425) **Hunter's Mark** rank 4 gives +71 ranged attack power against rank 3's +98, and **Trueshot Aura** rank 5 +50 against rank 4's +75 (if your build has it); cast the stronger lower rank from your spellbook until Blizzard fixes the numbers. **Aspect of the Hawk** rank 7 (+120) is the best at 60. The simulator's numbers use **Hunter's Mark** rank 4, so they read about 0.3% low (estimate).

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown, since it hits up to 3 targets for weapon damage each while **Aimed Shot** adds 166 to one. For a pack, **Volley**: a 6-second channel with no cooldown in Forever, which holds **Auto Shot** while you channel.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds. The simulator's other hunter rotations stop refreshing it 3 to 6 seconds before the end.
- Inside 8 yards your shots and **Auto Shot** stop. Step back out; if you cannot, **Summon Hawk** still works, as it has no minimum range.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 768 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 746 | [31/20/0](https://talentsforever.com/hunter/60/5321001505001251-00500505005--7) |
| Phase 1 BiS | 770 | [31/20/0](https://talentsforever.com/hunter/60/5320001505101251-00520503005--7) |

**The gear** (average item level: Pre-BiS 63.4; Phase 1 BiS 65.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Pendant of Celerity](https://www.wowhead.com/forever/item=22340) · *Lord Valthalak, Blackrock Spire* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Giantstalker's Epaulets](https://www.wowhead.com/forever/item=16848) · *Sulfuron Harbinger, Molten Core* |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/item=273470) | [Giantstalker's Bracers](https://www.wowhead.com/forever/item=16850) · *Molten Core*<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/item=273470) |
| Hands | [Beaststalker's Gloves](https://www.wowhead.com/forever/item=16676) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Beaststalker's Gloves](https://www.wowhead.com/forever/item=16676) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Giantstalker's Belt](https://www.wowhead.com/forever/item=16851) · *Molten Core* |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Dragonstalker's Legguards](https://www.wowhead.com/forever/item=16938) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Giantstalker's Boots](https://www.wowhead.com/forever/item=16849) · *Gehennas, Molten Core*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234020) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMVF9IPFUUnjMzu3M8/X7retV2HCSmhWJdmOXOrBOuEbP61FMY9NBTObprO5LusrsPCj1YGYRU2FuGYKBLGhYGBRH0YgkrbLgq/aGkoAx86GEhKHqLmd1NyFeFvqdvzrl3vu/cczh0DyEKKuiQAA5s6N8vkcMYZGEKnoUSrABoryJiVNJeIgW/+LRXvXyAZPzqIyAZzxtRUvDLGqinYZ980qv+GiEFD2ug/gWk4M4roP4cIRl/+vM+Kfj2x+BfV/BgvxM/q/n/2dmJkIRvLpCMe+v+ve/XQb2KkEAKnp1G1R/74ylc9aJ1T33D09/fhMTlFqyBuOq9A9vue7Dv7sLFxAFs1aAO0IS3vEm6ru5zcdhOW5xz0+a2yU3LNg3O7TS3eZrz0booN0X8RfwjRAOEWphkbB5BHClMsmHyCg12orvbEO8hhUKGlbIrbBPYc27pxeeLpapucesxg2cMa2xcny24iy/kc3qxrLu5XD6nzyzr1UJeLxerbtUrLuqVvFueLeiJSj6vzywYZdfLGd2k0U6m5ivFxRFtnDhL0VAyhhLDed/ZyRFogQeesuwK9SV7MczEGUFTKERSmj+idU4xWRPHBeb9x6PJDZ65VY+KFiIJT4ps+aaUOXqrUjG6/0OYSMbDlSkmRuWgVp8/oT1OFuM0kGQosdChKGKo/SI8ZZKafBAl1vMBdJrYzdiB899ibP7OG9keoO/+fuqGlt8Q6w60dreB6dpDNJjsx1D3SYKZ5im7ElR+PqBKV2IdWqL1siQESGTXYJD6qQ/DUVRhRAjQcjjE96Qenwsrc9mhdzd8HDsPzwX41rFaoirrTrIuCv8rVLNddqd49MNb18l83Wg07k0fZCc6gew0vA6wAV6x9drxM984mSAqNJ0J/2Sj8bvzdJtcOEkJP4tNDl9vwPZGfzLY6QUowRIssX8GANsxQlU=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMVE9IG2kUnzczyXy+dTV+6mYcZJkN7BIDE74Zdxbjskz0tKfFhT3sadfRxM3IakKSg8Ie3EahSP9IT7UVLFjxDy14aKEUerEIEVKMSv/QCoXWgoceAj2U3spMkgr1qtDf6c17b77f7/e9j4eNBAIggwphYEA7Pn3xDHogDgPwJ2RgCkApEEICgvIfSuTB3Wb58CsUyeFlQJGUC4ASuV4OyLt+lMjDO83y6yaUyF4B5Pdu6eY5kF82oUj2vc71aXB/l8huoZZfmXHP2VsGFMjFMRTJ2pzb+GwO5KMm5FAi81dAftEaipJpJ1B05AuOurIA4cNFmAV+2rkKS/YNuGWvwkHfBiwuQxGgDJecfjx2d5/vNLsNxphuMlNnumHqGmNmNzOZwZhZ5MUyT17x73zYhkTxu762IETQj6Kmsxy217KrSxBqQAl9mhE1c3QB6F925t+/05m8ajDjJ43FNKOnVx1O2eP/JBNqOqvaiUQyoQ5NqvlUUs2m83beSY+ruaSdHU6p4VwyqQ6NaVnbSWj1olYtRkdz6fEupRcZjWJHJEgESkZdZTtboHgaWNQwc9gSaSZ+yg9xioQ+FLrZ90qti4oK38tR5zONOtNY7FQ1SooPBbKTppMnqfQfT5UqiF8/9yOKZHNqgPIB0fPqxr8oP6NBGbZFKBGob5Pnia96Iyyqoxz5hgi0YR1qQ6xXTE/5myAdPfNBVh/Q0w+/neByB2KcAdfqElBV+RbbI63EV78S702zqJnznO+3ycIRX4QKb/wvcB7C8Vlox1ZsIf4AkaGL81CxGITWhAY35qZG4h3X5l1sW9+NeHhiGRVeFlUrUuS5Lwr5eD06U/xw+9R5Yo9KpVLj4Ea8r5aID8J5gHlw0pWZ7T8eWzEvy5WtPrezVHpr/V4NDqyIQO4F+zuPN2B1o//q7fQUZGACJujHAQCLNUCl).

## Other builds of this spec

- [Beast Mastery (optimized, with a pet)](../research/raid/builds/opt-mm-raid-raid-dps.md) (31/16/4) — [open the talent tree](https://talentsforever.com/hunter/60/5420001505001251-0050550001-4-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-25 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

