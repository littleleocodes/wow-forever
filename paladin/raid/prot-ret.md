# Prot-Ret Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Prot-Ret

*Retribution's melee talents with Protection's Seal of Fury, Swift Judgement and Toughness: a melee split short of 30 Retribution points.* (a hybrid: Protection/Retribution).

**[Prot-Ret — Raid](../research/raid/builds/prot-ret-ml-raid.md)** (10/12/29) — [open the talent tree](https://talentsforever.com/paladin/60/05005-552-3523310100130034-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds); it beat the hand-made build (Retribution — Seal of Command), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Seal of Command**.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**; no global cooldown, so press it alongside the others
2. **Hammer of Wrath** when the target is below 20% health
3. **Consecration**
4. **Holy Strike**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Retribution Aura**: put it up at the start and keep it up
- **Seal of the Crusader**: put it up at the start and keep it up

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Holy | 10 | Divine Strength 5, Improved Seals 5 |
| Protection | 12 | Divine Intellect 5, Redoubt 5, Precision 2 |
| Retribution | 29 | Deflection 3, Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Vindication 1, Seal of Command 1, Sacred Arbiter 1, Two-Handed Weapon Specialization 3, Vengeance 3, Champion of the Light 4 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 727 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 677 | [10/12/29](https://talentsforever.com/paladin/60/05005-513110001-1423330110130034-12) |
| Raid BiS | 682 | [10/12/29](https://talentsforever.com/paladin/60/05005-552-1523330100130034-12) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.8; Raid BiS 63.0; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Raid BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) · *quest: Falrin's Vendetta* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsFNcZ3n92dvb4X6+9PvgyPhiYbjHY2647M4sr6gJebNpyqdWtUQuVUMvYO/YuXe+4M2sXXiq3ovQiQqS8BFBkIi4JskKIIJGQFV5IIhGeHCVyIksk1uYlD0QhfuBhH6JoZr3eC74EBZTzYB3/59//8p3zff8uthAIgAgStMFRSMAoTAD8F+BlgKsAtNo55ezT7cBmmwgf4NjfUSDzA2LWhzw5dQ2QJ3MvAXrJ5ExA/EBAL3nnzVrx8xr0kjtXQLxvbyZfAfGCF3nyyTXb8+vXwf64QM6a4mc1yJPnHgSQJ2dnAugmrx5Bnrw1E0AvefcKiA9q0IU8uTkTCHYE7ibbFv4qPxqIzZ6B/wN3MvkCcI8GzoNwSXtNm9s9Bd7TyamrcCY5DyeTPcSpHqIwzUlypyx3hjuViKLIsqyElW1qJBKRFUVWIrIc2XaX47Pc/QbciuuzIGLj7sFMclzL6JJmWcnhtB6XtDFTCxIUkA+rsoUS1k9BHdbmhGrE2FgqJZlaelgv8diMzVloxPqYqY9KB3UtJRlDUq8xMqKl40EvetAdjlj4U9yUhRZkZV79yeFERjfGrLRuWcEq9KInrHR0WtiOLVloxqZezcoUSzs2Fh/WR/R0psSVbmZBrAlWIy4QL3raCLkfy0It+vuMcV3KGNKIntJ12sya0J8TEMmhX0vDY5oZZwLy5PokOAE2hlqIQLkuF6vPCXVYu0dPaSekPu2YYUq9e6wuF+1hUdzGVGwONRGgvvMcQaHNTa7fBjsQcrKFDaF1xE09C16OuJmDj9yhWmzJkabon7XR1F+M0YykyurPw4ocjihd0mDCRjQuGaakxeN6XBo4IWUSumQaGS2TNNKSpWvmYEJqs3RdMvVMOD5qhQuH4fxhxzHLSLczdLJ5yNuXgP6W7cduurOibfQHfVh1ERa7xw05gaG430ZWMnUtlbRGpFHTyOiDdnRWgJS2sh9jU06oR3owYYyl4pKpD5m6lZAOGr2LSW9dgtXc+h03Qt6bBLqO1WWhBqt7jbSlD5pOm7SW+bOASH513DAHk9aI6A61rvRCqY9VOcV5yO1YaM+KL4W2s624PieI2LhXs5ZxcIoSyEeTEBpc/g3TA2wf7qS/xE3BDauGQjEnNOC6P1h6ZYgiQKHLsBoH6L+B/QtwnGbWzrYxJ6zH5tJsZaFQYT/DliBbuSqsDfrRlyV2cUBevADFCwp9ylcy6CGwLwFPA/0frF5XaUTsYwdWKSAYlNZsYync8xOxPNGznBc9I8a4rtAjhU3DFFAM5AQ/+vpswudVivpNH1YtkALVyRLpvUEPuqd5Fy0wxn68NWaZjNBZYB8CWvRvqzdsS0MZlHalldiucRXljamFxtTv21iebpWNTQD7B0aosvYjK68rQn9T2DxpXRUlhOJFntPD7I94gO5zBNRDPXe4JQF1hkFdqNYW5wGXTXh0K3JrpYg5VV6EQnDbr00g92KhZIXE/IkderqZluRWDa6EIXXiZ8wxXd207OWXOLSuwoQSt+bHJhRdHEJqfemUzlvVTrW+/JY86EboVHcUxwKVaYeDilAxwBSrYC4BS+5QLPUUt9wsoF8BffDUed/FtqNvTliiKrbTrei7AUWDGGokPPVNF00s/5AwynY9Ts+f0Hb0zwlYcBbzEQTquwPE/gL3n5gIzMFJWWNGqveWA6Kf3uToG5yTfa1WH9OKslJ3sR1PqOMrYueoQSl2eUMZdo6pgN3v2e++g7SVgOl8ehFMKID5cRHMyFpg9qx8RreENhOeVk0V2MgabnCUcLTqordgsTX9C+4uPOTUf7pdzqqPTgOPHLqC33BVtsE1MRRtPn/OXu93/2jIWbPd6jwn8lJ36Bbn+kFWJlrYPdO15dozy/ML52//5ejuRUP0qP0b6xw4/7jmu0Nucqupp+SnmAzbIQp7IQaHIQGjcByOc98OAALUAxQ=); Raid BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsE1ca9j8ej09+x4lzyGVyCDDrJZB419nxGK/YLBCTsLtcNlpv0C6shHaZxJPYrONJZ5wUXqq0oldRkPrSgqpQcWlRVEoFrYSi0gfaSpSnVK1oFYk2cvvQB6rSPPDgh6qacRxfyKWooJ6H6OQ/v//Ld873/Ta2EPCBCBK0wUFIwAiMAzwH8BrABQBabZ9y1ulmYNNNhPdx7HEUyGy/mPUgT745AciTmVcB3WRi2id+IqCbfPBOrfh1DbrJ9fMg3rY2E6+DeNqNPPniouX5w1tgfVwgrxjiVzXIk/fPW2FevONDJ3njAPLk3WkfusmH50G8U4MO5MmVaZ+/w3cj2Tb3f/lef+zWcXgBuKPJl4C7138KhLPqm+rM9klwH0tOXoDjyVk4muwmdvUQhSmOyRFZjgQjESUYiijhcFgOyXIoLMvhTTc4PsvdbsCNuDoLIjZuH8gkx9SMJqmmmRxKa3FJHTVUP0EB+aAimyhh/STUYW1OqEaMjaZSkqGmh7QSj/XYnIVGrI8Z2oi0V1NTkj4o9ejDw2o67nejC53BsIm/x3VZaEFW5tWXHEpkNH3UTGum6a9CN7qCoY6Iie3YkoVmbOpRzUyxtEOj8SFtWEtnSlzpeubHGn814hxxo6uNkNuxLNSit1cf06SMLg1rKU2jzawJvTkBkez7qzQ0qhpxJiBPLk2AHWBtoIUIlOt0sPqcUIe1O7SUekTqVQ/phtSzw+x00G4WxU1MweZAEwHqOcURFNqc5NI1sAIhJ5vYEFhFnNQ15+aIk9n4yB2KyRYcaYr+Vx1J/U8fyUiKrPwxGJKD4VCnNJCwEI1LuiGp8bgWl/qPSJmEJhl6Rs0k9bRkaqoxkJDaTE2TDC0TjI+YwcJhMH/YccjU0+0M7Wwu8t5ZoH9nu7GLbq1oG71+D1adgfnucU1OYCjutpCVDE1NJc1hacTQM9qAFZ0VIKWt7LfYlBPqke5N6KOpuGRog4ZmJqS9es980qtnYTm3PtuNkI8mgK5idVmoweoePW1qA4bdJq1l3iwgkr8c1o2BpDksOgOtS71Q6mFVdnEuci0W2LHkS6HtbCOuzgkiNu5UzUUc7KIE8tkEBAYWf8N0D9uFW+mfcZ1/zbKhUMwJDbjqX6ZWGaIIUOAcLMcB+jSwpwDHaGblbGtzwmpsLs1WFgpD7A/Y4mdLV4W1fi96ssQqDsjLp6F4QYEv+UoG3QX2HeAxoM/D8nWVRsRetmeZAvx+acU2FsKdGI/liZ7l3Oga1se0ED1Q2DRMAkVfTvCip9cifF6lqNfwYNUcKVCdLJDe7Xehc4p30AJjrMdbY5TJCL0F7FNAkz62fMOWNJRBaVVaie0KV1HemFJoTPmljeXpVtnYOLAnMExDKz+y8rrC9G+FzYPWVVFCIF7kOd3P/o176C5bQF3UdZ1bEFB7GNQFai1x7ndYhEdnSG6tFDG7yjNQCG75tQnkZiyQrJCY/7B9DzfTgtwq/qUwpHb8jDGqKesWvfwSh9ZlmFDi1nzfhKLzQ0ipL53SeasSUerLb8mFToSIsqU4FqhMO2xUhIoBFjIL5hKw5I6QqTzDLTYL6PdA7zx03neyzeiZERaoiu10I3ouQ9EgBhoJTz1TRRPLPySMsm330/N3tB29MwIWnMV8BIF6rgOxvro9GxOB2TiFVpiRys3FgOijVzj6NmdnX6nV+7SirNRtbMsD6viS2NlqUIpd3lCGnW0qYPdP9o+fIW0lYNqfngcTCmB+XgQzvBKY3Uuf0Q2B9YSnVZMFNrKGyxwlHK064y5YLE3/lrsBdznlSafDXvXRKeCRQ4f/R67KMjjGB6PNp05a6+Ou3wza61aXMsuJvNQVuMo5fpWViRZ2j3RtuPjI8vzJ/tt3Lrp93hA9aP26Ogn2P47ZroCTXG3qLvkRJsNmiMJOiMF+SMAIHIbD3E8DAPuWAhQ=).

## Other builds of this spec

- [Retribution — Seal of Command](../research/raid/builds/ret-full-buffs-raid.md) (8/15/28, 694 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/05003-053020005-1523330100130033-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-18 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

