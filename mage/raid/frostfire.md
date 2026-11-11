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

Frostfire is a Fire list whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost, so both trees' talents apply, its chill rolls **Fingers of Frost**, and its crits stack **Heating Up** for a 1.5-second **Pyroblast**. **Scorch** keeps Fire Vulnerability at 5 stacks and **Fire Blast** fills between casts. **Ice Lance** is in the build only because **Fingers of Frost** requires it: the list never casts it. 759 DPS in a full raid, 8% behind the Fire page.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 772 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 821 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-12) |
| Phase 1 BiS | 842 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.5; Phase 1 BiS 63.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Cloud Stone](https://www.wowhead.com/forever/item=17737) · *Landslide, Maraudon* | [Cloud Stone](https://www.wowhead.com/forever/item=17737) · *Landslide, Maraudon* |
| Ranged/relic | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG0UU9pvdxuOXNHGmULbbHKaGkGQTJ/uTVEmQiFsJUUpRKk4IJOjauxsvOF7Lu6naW6E9oEhNUahACSBBBCogoFKRUJMbvuByQBEHOHBIVKhACAmSQyUuCM3aacOlt4ZDnuSdmffme2/me88zg10U0qAAh144BUWowDmA1wHeB/gYgLXFViKso6Be7KQ0TdUqJumVeVButaJMz18FlOnvl8X3ndU0ttB6Wfm5HZO09hEoP7WjRGtllOmtS4AtdNMTqBa6XFQuJVGmc3+kUabffiDQX62mUaJvTGOS/vkFKPV9KNMbs4AS/eWFzEC67vd+Nwf67fzJi0swC+SCPw/kdn4RyK9HPgV65V34bBbm/HW44B+l8bIhByskkx0eGdF1XTdMK/5ZWdOwhMbSDcOwdN2sE1glrTfJ5Q58BKnagjL9ex4yyjXyIJVYapE0NcKCJGuwCnPtSumloBJxUzcPZw09axnjvFC0y1Ouw4Mqtx3HdXj+LI+KLq8GkR35QZmHrl0tFHlv6LrcqwZh5PlVN1u1fSe7NSfbmDP4chiU+9Skugel9DePswXCNmB7LOE38Dy/4NslHvrTMyU7Cqo9IZ+2p9whpxIO2ZVSOOR5+UG7UordcTviI8MF1y4ctka57QSVyHV4753IJXuK2zOOH3Hbi9xqY+lutuKXx3m/Oah3cy9oaN1yVD3bE/K8G0Y8P+OXHO6Xuc29mVKJi+0M8H5j0OjmUSCQZgPpRyEv+aEIGmPCAW7oA7quc8+fKkYhjxlynZCb3C473OpTH8Z9WieVGHk+oaY2pWYebkIrpp44HRRiVtka7FQ6TuM0ewUfU8dQ1RQqsb01QJTp1S+BkTQRuUIYwYPaAWFb+Y8tLh1DxwFVuwd4GNsyiHQT9qBE1yaFR7o2yd7andnn2KWpFFhHDdruMqVAk+jxBPtkdxJjYR/rwf3aAxRYqgbib7GxrDRosXBvphVTm7Dt0BIte3t3cnUIFW0/lVhrDSjK9L0VZauATNHQHyfZ+R07QFRMa+20hZHjCZEXJFYoWvp17ekdvlTo2qQiaUuw/SB9Sn0Su5jaKKBrcQGt1J/B1Pey6C5vnDB7mtfj8sYJPPgaKCjRN19UO7UOsad8Qk3iHpTGxrrZcfUY9qt9DVd38I3hEmwN7wa5h6/fSB3+IuarUiKW4VyMR0Ih8w9JCVXinJc7sLgg5MbEIS+WHybMdaLIfEK7ThL/i0S5rd59lUc/v29xxuLvsx/mjjQVuVPiabgA8SCxPqFJ9PpDR7e9IHUYhRwcg5PwHBShAmfgDPl3ABfKhas=); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG0UU9pt14vFLmjhTKNttDlNDSLKJk/1JqiRIxK2EKKUoFScEEnTt3Y0XHO/Ku6naW4EcUCRSlLagBJBQBCogfqRyaXLDF1whoYoDHBBKVKhAXCA5VOJSoVknabj01vSQJ3lm57353pv53vPMYCeFDMjAoQdOQwkCOA/wFsBHAJ8CsNbYSoR1BJS5DkozVAkxRa/Mg3yrBZP0zjxgkv51SbTv38hgM61X5N/aMEVrn4D8SxtKtFbBJL11ATBFf70cw5rpckm+kMIk/f4ybLczFwEl+s4UpujfX4Fc349Jen1W6H5/KdufqXs9P8yBdrtw6u0lmAUy480DuV1YBPLH0c+BXvkAvpiFOW8NZrxjNF435GGFZHNDw8Oapmm6YcY/M2foptCYmq7rpqYZdQI3SMtNcqkdH0OqNGOS/jsPWfkqeZhKLL1INjXCgiSns4A5VlB+xQ8ibmjGkZyu5Ux9jBdLVmXSsblf5ZZtOzYvnONRyeFVP7Iiz6/w0LGqxRLvCR2Hu1U/jFyv6uSqlmfntubkGnMGXg39Sq+SUppQynz3JFsgbB12xhJ+fdf1ip5V5qE3NV22Ir/aHfIpa9IZtINw0ArK4aDrFgasoBy741bEh4eKjlU8Yo5wy/aDyLF5z3bksjXJrWnbi7jlRk61sXQnF3iVMd5nDGhd3PUbWqcSVc91h7zghBEvTHtlm3sVbnF3ulzmYjv9vE8f0Lt45Auk0UB6UcjLXiiCxpiwn+tav6Zp3PUmS1HIY4YcO+QGtyo2N3uVR3G/2kElRl5MKOkNaTMPN6EF00+d8Ysxq2wVdisdZ3CKvYZPKKOoqDKV2L4aICbp198AIxkicoUwjIfUg8K28j9bXDq6hv2Keg/wELZmEekGNKFEVyeER7o6wd7dm9nn2KkqFFh7DVrvMiXDJtFjCfbZ3iTGxF7WjQfUhyiwdA3E32J9WW7QYuK+bAumN2DHoSV69t7e5OowyuoBKrGWGlBM0g9X5K0CMkRHf55gb+7aAaJgRm2jzYycSIi8IDFD0dNva8/u8qVCVydkSV2CnQfpM8rT2MmURgFdjQtopf4cpn9Mis/l9ZNG9+b1uLx+Eg+9ATJK9OLLSofaLvZUSCgpbEJpdLSLnVCOY5/S23C1jW8Ml2BreDfIPXz9SerwDzFelxKxDOVjPBIK2TskLVSJ827+4OKCkOvjh91Yfho31oic5OPqNZJ4IBLlt77uqzz+5X2LMxq3z3+cP7qpyJ8Wb8MFiAeJtXFVotceObbjCanBCOThOJyCF6AEAZyFs+S/AQA4toV1).

**Points that do nothing for this spec:** **Improved Frostbolt** (1) only counts toward the points the tree needs before **Arctic Reach**, **Fingers of Frost**, **Ice Block** and **Shatter**; **Ice Block** (1) only counts toward the points the tree needs before **Fingers of Frost**.

## Other builds of this spec

- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 762 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-3551000113013303-2135000301113002-12)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (7/31/13, 701 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0410011-32510301230133031-20350003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

