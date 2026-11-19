# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-3550000123013303-2135000301113002-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds); it beat the hand-made build (Frostfire — Fingers of Frost / Ice Lance), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Pyroblast**.

**Talents with no line below:** **Ice Lance**: taken because Fingers of Frost requires it.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 779 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 698 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2035001301113002-12) |
| Pre-BiS | 788 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2035001301113002-12) |
| Raid BiS | 811 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2035001301113002-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 60.9; Pre-BiS 61.9; Raid BiS 63.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Shroud of the Nathrezim](https://www.wowhead.com/forever/item=18720) · *Balnazzar, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Amplifying Cloak](https://www.wowhead.com/forever/item=18350) · *Magister Kalendris, Dire Maul* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Netherflame Cuffs](https://www.wowhead.com/forever/item=254065) · *Tailoring*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Highlander's Cloth Girdle](https://www.wowhead.com/forever/item=20047) · *sold by Samuel Hawke* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Don Mauricio's Band of Domination](https://www.wowhead.com/forever/item=22433) · *Darkmaster Gandling, Scholomance* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Tracker's Signet of Brilliance](https://www.wowhead.com/forever/item=275973) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213) · *Mother Smolderweb, Blackrock Spire* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Flarethorn](https://www.wowhead.com/forever/item=22266) · *Gorosh the Dervish, Blackrock Depths*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG8UX95t14vFLmjjT/79stzlMDSHJJk72I6mSIBG3EqKUolScEAjo2rtrLzjexbup2luAIqEKmiogqkStVCKkAqJUKpcmt0ZChAtfBzhwSBRAcOBAcqgEB4Rm7bTh0lvDIU/yzsx783tv5veeZwY7KWRABg49cBLKEMA0wJsAVwA+BGCtsZUI6wgob3VQmqHKK5iiV2dB/qUFk3T9ImCSXpkV309nAFP02xmQf2rDFL11AeQf21Cin5cwSb++BNhMN10Ba6aLZXkmhUn6/nUBfOP3DEr0wiRK9HIJU/SvayCv7EWJTj+PEv35uWx/ZsXr+eo8aLcLJ95egHNAznqzQG4X5oH8evhjoFcvwSfn4Ly3Bme9IzReNeRhiWRzQ8PDmqZpumHGPzNnaOawpummpuu6qWnGCoFvSMs6ebcdH0KqNGOS/jkLWfkG+T+VWHqeNDTCgiSns4A5VlB50Q8ibmjGoZyu5Ux9jBfLVrXk2Nyvccu2HZsXzvCo7PCaH1mR51d56Fi1Ypn3hI7D3ZofRq5Xc3I1y7NzW3Ny9TkDL4V+tVdJKU0oZb54lM0RtgHbYwm/vut6Rc+q8NCbnKpYkV/rDvmkVXIG7SActIJKOOi6hQErqMTuuBXx4aGiYxUPmSPcsv0gcmzecydyxSpxa8r2Im65kVOrL93JBV51jPcZA1oXd/261qlGtTPdIS84YcQLU17F5l6VW9ydqlS42E4/79MH9C4e+QJp1JFeFPKKF4qgMSbs57rWr2kad71SOQp5zJBjh9zgVtXmZq/yIO5VO6jEyLMJJb0pNfKwDi2YfuyUX4xZZauwU+k4hZPsZXxEGUVFlanE9iwDYpJe/wwYyRCRK4RhPKDuF7alf9ni0tE17FfUe4CHsDWLSDehCSW6OiE80tUJ9t7uzD7HTlWhwNqXofUuUzI0iB5LsI92JzEm9rJu3Kf+jwJLL4P4W2wsynVaTNyTbcH0Jmw7tETLLu5Org6irO6jEmtZBopJenlJ3iogQzT0hwn2+o4dIApm1DbazMixhMgLEjMULb21/OQOXyp0dUKW1AXYfpA+oTyOnUypF9CNuICWVp7C9HdJ0V3cOG50N67HxY3jeOA1kFGi77ygdKjtYk+FhJLCJpRGR7vYMeUo9im9dVd38PXhAmwN7wa5h6/fyAr8QYxXpUQsQ/kYj4RC9m+SFqrEtJvfPz8n5Mvxg24s348ba0RO8nH1Jkn8JxLlt3r3VR6+dt/ijMbfpz/IH24o8ifFy3AO4kFibVyV6M0Hjmx7QGowAnk4CifgGShDAKfhNPlnAFsDhEs=); Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG8UX95vdxOOXNHGm/3/ZbnOYGkKSTZzsR1IlQSJuJUQpRak4IZCga+9uvOB4Le+mam+F9oAqmlSlKkoACUVIfIhSqUioya2+YC4o4gAHDokKFQghQXKohJAQmrXThktvDYc8yTM7783vvZnfe54Z7KaQBgU49MFJKEIFzgK8CfABwMcArD22EmEdA/ViF6VpqlYxSf+6BsqdNpTpueuAMv31imjfXU1jK62XlR87MElvXQLlhw6UaK2MMr0zD9hKNz2BaqXLRWU+iTKd+y2NMr26KtovV9Mo0UszmKS/fw5KfS/K9K15QIn+9FJmMF33+76ZA/1u/sTFJbgA5Lx/Gcjd/CKQnw9/CvSj9+CzCzDnr8N5/wiNlw05WCGZ7MjoqK7rumFa8c/Kmro1quuGpRuGYem6WSewStpukyud+BhStRVl+udlyCg3yP+pxFKLpKkRFiRZg1WYa1dKrwSViJu6eShr6FnLmOCFol2edh0eVLntOK7D82d4VHR5NYjsyA/KPHTtaqHI+0LX5V41CCPPr7rZqu072a052cacoVfDoNyvJtUWlNJfPckWCNuA7bGE38Dz/IJvl3joz8yW7Cio9oZ8xp52h51KOGxXSuGw5+WH7EopdsftiI+OFFy7cMga47YTVCLX4X33IpfsaW7POn7EbS9yq42lu9mKX57gA+aQ3sO9oKF1y1H1TG/I824Y8fysX3K4X+Y292ZLJS62M8gHjCGjh0eBQJoNpB+FvOSHImiMCQe5oQ/qus49f7oYhTxmyHVCbnK77HCrX30U92pdVGLkxYSa2pSaebgNbZh66lRQiFlla7BT6TiFM+w1fEIdR1VTqMT21ABRpte/AEbSROQKYRQPaPuFbeVftrh0DB0HVe0B4BFszyDSTWhBia5NCY90bYpd3Z3Z59itqRRYZw3a7zOlQJPoiQT7ZHcSY2E/68V92v8osFQNxN9iY1lp0GLhnkwbpjZh26ElevbO7uTqICraPiqxthpQlOn7K8pWAZmio99PsXM7doComNY6aCsjxxIiL0isUPT0Vu3ZHb5U6NqUImlLsP0gfUZ9GruZ2iigG3EBrdSfw9S3svhc3jhu9javx+WN43jgDVBQom+/rHZpnWJP+YSaxBaUxsd72DH1KA6o/Q1X9/CN4RJsDe8HeYCvX0gd/iDm61IilpFcjEdCIfM3SQlV4qyX27+4IOTryYNeLN9NmutEkfmkdpMk/hOJcltfD1Uev/bQ4ozH7fMf5g43FbmT4mm4APEgsT6pSfTmI0e2vSB1GIMcHIUT8AIUoQKn4TT5ZwDjEoXW); Raid BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG0UU9pt14/FLmjhTKNttDlNDSLKJk/1JqiRIxK2EKKUoFScEEnTt3Y0XHO/Ku6naW4EcUCVSlLagBJBQhMSPaJHKpckJfMEICVUc4IBQokIF4gLJoRJCqtCsnTRcems45Eme2Xlvvvdmvvc8M9hFIQMycOiFU1CCAM4BvAHwAcDHAKwtthJhHQVlrpPSDFVCTNF/roB8qxWT9M48YJL+cUm0797IYAutV+Rf2jFF17/skH9qR4nWKpikty4ApujPl2NYC10uyRdSmKTfXoatdvYioETfmsYU/fMqyPV9mKTLV4Xu1xeyA5m61/vdHGi3CyffXILzQGa9eSC3C4tAfjvyKdCP3oPPzsOctwaz3lEarxvysEKyueGREU3TNN0w45+ZMzRzRNN0U9N13dQ0o07gBmm9SS514CNIlRZM0r/nIStfIw9SiaUXSVMjLEhyOguYYwXll/wg4oZmHM7pWs7Ux3mxZFWmHJv7VW7ZtmPzwlkelRxe9SMr8vwKDx2rWizx3tBxuFv1w8j1qk6uanl2bnNOrjFn8OXQr/QpKWUPSpmvH2cLhK3D9ljCr++6XtGzyjz0pmfKVuRXe0I+bU05Q3YQDllBORxy3cKgFZRjd9yK+Mhw0bGKh81Rbtl+EDk2792KXLamuDVjexG33MipNpbu5AKvMs77jUGtm7t+Q+tUourZnpAXnDDihRmvbHOvwi3uzpTLXGxngPfrg3o3j3yBNBpILwp52QtF0BgTDnBdG9A0jbveVCkKecyQY4fc4FbF5maf8jDuUzupxMjzCSW9ITXzcBNaMf3Eab8Ys8pWYafScRqn2Sv4mDKGiipTie2tAWKSfv4FMJIhIlcII3hQPSBsK/+xxaWjazigqPcAD2NbFpFuwB6U6Oqk8EhXJ9nbuzP7HLtUhQLrqEHbXaZkaBI9nmCf7E5iTOxjPbhffYACS9dA/C3Wl+UGLSbuzbZiegO2HVqiZ+/sTq4OoazupxJrrQHFJH1/Rd4sIEN09MdJ9vqOHSAKZtR22sLI8YTICxIzFD39qvb0Dl8qdHVSltQl2H6QPqU8iV1MaRTQtbiAVurPYPr7pPhcXj9h9DSvx+X1E3jwNZBRohdfVDrVDrGnQkJJ4R6Uxsa62XHlGPYrfQ1XW/jGcAk2h3eD3MPX76QOfxHjVSkRy3A+xiOhkL1D0kKVOOfmDywuCPlm4pAbyw8TxhqRk3xCvU4S/4tE+c2v+yqPXrlvccbi9tkP80eaivwp8TZcgHiQWJtQJXr9oaPbnpAajEIejsFJeA5KEMAZOEP+HQDXVIZQ).

**Points that do nothing for this spec:** **Improved Frostbolt** (1) only counts toward the points the tree needs before **Arctic Reach**, **Fingers of Frost**, **Ice Block** and **Shatter**; **Ice Block** (1) only counts toward the points the tree needs before **Fingers of Frost**.

## Other builds of this spec

- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 771 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-3551000113013303-2135000301113002-12)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (7/31/13, 708 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0410011-32510301230133031-20350003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

