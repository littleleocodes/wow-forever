# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**[Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md)** (20/31/0) — [open the talent tree](https://talentsforever.com/warrior/60/35310003131-25050034102210501--7)

**Other setups of this spec.** This build is the Two-handed setup. The spec's best build for each other setup, in a full raid:

- Dual-wield: [Fury — Raid](../research/raid/builds/fury-open-raid.md) (18/31/2, 883 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/31305013002-05053035102010501-2-7)

## How to play

**Press the first one that is ready**, top to bottom:

1. **Whirlwind**
2. **Bloodthirst**
3. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
4. **Execute** when the target is below 20% health
5. **Hamstring**
6. **Bloodrage** when you have less than 90 rage

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Recklessness**: once a fight, in the last 33.75 seconds of the fight
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fury in a raid fights in **Berserker Stance** with a weapon in each hand: **Bloodthirst** and **Whirlwind** on cooldown, **Execute** in the gaps below 20%, **Hamstring** in the short gaps and **Heroic Strike** only when rage piles up. **Death Wish** and **Recklessness** wait for the last 45 seconds.

**Why it works**

- **Bloodthirst** (30 rage, 6-second cooldown) and **Whirlwind** (25 rage, 22 with **Raging Blows**, 10-second cooldown) are your main attacks: press them the moment they are ready. **Whirlwind** now always hits with both weapons, and it needs **Berserker Stance**, the stance this list never leaves.
- Below 20%, **Execute** still comes after **Bloodthirst** and **Whirlwind**. It spends all your rage (600 damage plus 15 per extra rage point; 10 rage to cast with **Improved Execute**), so it takes the global cooldowns between them; a full raid gives you enough rage that the simulator measured this order slightly better.
- **Death Wish** (+20% physical damage for 30 seconds, 3-minute cooldown) and **Recklessness** (+100% crit chance for 15 seconds) wait until about 45 seconds are left, so they cover the execute phase. Crits give double rage in Forever, so the **Recklessness** window also feeds bigger **Execute** hits. The simulator measured 0.7% more damage with **Death Wish** at 45 seconds than at 30, and in fights longer than about 3.5 minutes it presses it at the pull as well.
- **Hamstring** (10 rage) fills a global cooldown only when **Bloodthirst** is more than a second away and **Whirlwind** more than 1.5 seconds: it is a cheap extra main-hand hit that can trigger on-hit effects such as a shaman's Windfury Totem, but it must never delay your main attacks. The simulator measured 1.9% more damage with this rule than with **Hamstring** only above 80 rage.
- **Heroic Strike** is a rage dump, not a filler: queue it only at about 68 rage or more on a single target. It replaces a white swing, and white swings are your steady rage (each gives rage in proportion to your weapon's speed, double on a crit), so an early one starves **Bloodthirst** and **Whirlwind**; in Forever it also no longer helps your off-hand hit. The simulator measured 0.9% more damage at 67.5 rage than at 45.
- **Bloodrage** waits until you are under about 23 rage, so it refills an empty bar instead of topping up a full one. The simulator measured 1% more damage than pressing it whenever you are under 90.

**Caveats**

- The page's numbers assume a **Recklessness** in every fight and two Mighty Rage Potions (one early, one in the last 30 seconds). **Recklessness** has a 30-minute cooldown, so you will not have it on every boss: the simulator measured 11% more damage with it than without.
- With several targets, **Whirlwind** hits up to 4 of them, and above 40 rage **Cleave** replaces **Heroic Strike** (the full list does this).
- The simulator ignores threat. **Heroic Strike** causes a high amount of threat, so it is the first thing to stop if you pull aggro. **Death Wish** and **Recklessness** also make you take 5% and 20% more damage.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- Alone or in a small group (fewer buffs, less rage), put **Execute** first below 20%, stack **Sunder Armor** to 5 yourself and skip **Hamstring**. That is the simulator's rotation for a warrior alone on a training dummy, where stacking **Sunder Armor** was worth 12%.
- If nobody in your group has **Battle Shout** up, keep it up yourself (3 minutes), and put one **Sunder Armor** on a boss that has none: the list leaves both out because the simulator's raid already had them.
- Before a boss's fear, press **Berserker Rage** (30-second cooldown, 10 seconds of fear immunity); **Death Wish** also makes you immune. The simulator's boss never fears, so the list leaves it out.
- With a two-hander (the page's two-handed option), drop **Heroic Strike** and cast **Hamstring** whenever nothing else is ready: in the simulator's two-handed raid rotation those two changes were worth 5.3% and 6.8%. That rotation also uses **Bloodrage** under 90 rage and puts **Whirlwind** before **Bloodthirst** when **Bloodthirst** is more than 1.5 seconds away.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 881 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, ElliotWood/Forever fork 2ce8265 (client 70291); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 887 | [18/31/2](https://talentsforever.com/warrior/60/31305013002-05053035102010501-2-7) |
| Phase 1 BiS | 903 | [18/31/2](https://talentsforever.com/warrior/60/31305013002-05053035102010501-2-7) |

**The gear** (average item level: Pre-BiS 63.0; Phase 1 BiS 62.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Band of the Better Half](https://www.wowhead.com/forever/item=284716) | [Band of the Better Half](https://www.wowhead.com/forever/item=284716) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl1oHNUX33N3ZufkJN1OblIyufn37xikTkY23pndSZMWzaYgVF8s+mDxxWyzG7MiSdiJ2IIPaR5EVEp9sNhITfyIhNjWWqqWIkVsLVVaSBQCimKIgkJ9iOCDiF/cyW6jaxAJTTwPy93zMff3O/s7Z4f+h2CCBTY40AsDMAyjAE8BTAJMA/C6KMpUtBPE6yZqJohRoAQu7LMWa0nDJ08AafjpFZMMfGnWtOYSZOCFM5utr5Nk4PtTYH2pDhevmNaEQRr+dAzIwB9Ogio38NobYH2VJA2Pn6onDX89op729qxJGp56XmVenDWt79UTlk6COmj4yZzZ6piXis43E7Bn/hDs/bH3aWBjxXGoeTV3PPd5z8QUzAB7trgEY8VddSv8snCO3ZT20jKQXlpKPyUDGaRlOvCkLz3lTfmXmbbIJpK8TpBASjgazp8DnhV3Upp71OI2Y5wnP4Ba0h0drz7ImakLneIEHvFWk5Kny6HzD0Qho5JXIwyVZx65n5NAkSDNnHsO+IvA+3LDjz40NDxi+9LvSHkyJf0ddt9AbvDhQt4eKtm5fL6Qt/cdsEcGCnZpaCQ3UhwatMNCrtQ3YDthoWD3P1Y6kMo/nirlivlUJSO1nNH+SDg02CYydJtoo3p3M2qc3RMTBukUzwQhNbocE5GLCCnhe157ECqkON3L/48gRHWVV46/u4m/sBr6rhuP3qM2cWs1jrQMibtmGT1SgjQvI0OhEbME3y6C1Sj78m+UvUxEOUEafjEJfKtoqS7qkKH6wfDaeeCBSP9bMOnlMvO9qbWU4Svfrum2g2fWXPbExmhxSzWuTBDuiPHhjdFSjbrTBjy8iTeIetI/ZgxBNcPR8Z2XoTKd+Nb0yvnQL/fyZzZoUm+hZrcJdV47A9f3jwJETIYr0HtEN3n8djLdJOo8vgixyhZqEc2RN8FZKbZcmJEVmkRog6PjZ5PA31yNUOeNJ7Sb7uA7aavbUk1qefraPT8ISbgW6pxmoMKwLE81mWqHxvFqFx+rRiy7Uv46IG6JpiQeNTCC4fvtgeov/t7I70YQd9FO3hX9GVRRug76HwkpSV04DPwYbIzkO8jh2yJRwF+kUt4FFZYd29uDskIQL30IvElsobpWIjwNivx4Q9SD8QYr/h27DEvMPxiPRdaYnWG1VEMGxh2QP0Prb6xG+WOj/dnm8aPKPuq+uT+y+W5/gVma3e2eZbH/xEayldO62rYT63ZPV/R532vZnrIj26ve2Y5C9CW20O3G8WzTrj+92knohCzshj2wFwZgGPbDfvbHAKuF+nM=); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl1oHNUX33N3ZufkJN1OblIyufn37xikTkY23pndSZMWzaYgVF8s+mDxxWyzG7MiSdiJ2IIPaZ5EpdYHi420iR8pIdZaS9VSpIjVUsVCohBQFEMsKNSHCD6I+MWd7Da6BpHQxPOw3D0fc3+/s79zduh/CCZYYIMDvTAAwzAK8CTAJMA0AK+LokxFO0GcMFEzQYwCJXBhn7VYSxpefRZIw88+McnA47OmNZcgAy+e3Wx9kyQD35sC6yt1OH4CrAmDNPzpGJCBP5wCVW7gtdfA+jpJGp48XU8a/npEPe2tWZM0PP28yvxg1rS+V09YOgXqoOGnc2arY14qOlcnYM/8Idj7Y+9TwMaK41DzSu5k7oueiSmYAfZMcQnGirvqVvhl4Ty7Ke2lZSC9tJR+SgYySMt04Elfesqb8i8zbZFNJHmdIIGUcDScPw88K+6kNPeoxW3GOE++D7WkOzpeeZAzUxc6xQk84q0mJc+UQxceiEJGJa9GGCrPPHI/J4EiQZo59xzwF4H35YYffWhoeMT2pd+R8mRK+jvsvoHc4MOFvD1UsnP5fCFv7ztgjwwU7NLQSG6kODRoh4VcqW/AdsJCwe5/rHQglX88VcoV86lKRmo5o/2RcGiwTWToNtFG9e5m1Di7JyYM0imeCUJqdDkmIhcRUsL3vPYgVEhxupf/H0GI6iqvHH9nE39hNfRdNx69R23i1mocaRkSd80yeqQEaV5GhkIjZgm+XQSrUfbl3yh7mYhygjT8chL4VtFSXdQhQ/WD4bULwAOR/rdg0stl5rtTaynDl79d020Hz6657ImN0eKWalyZINwR48Mbo6UadacNeHgTbxD1pH/MGIJqhqPj2y9BZTrxzemV86Ff7uVPb9Ck3kLNbhPqvHYGru8fBYiYDFeg94hu8vjtZLpJ1Hl8EWKVLdQimiNvgrNSbLkwIys0idAGR8fPJ4G/sRqhzhtPaDfdwXfSVrelmtTy9LV7fhCScC3UOc1AhWFZnmoy1Q6N45UuPlaNWHal/HVA3BJNSTxqYATD99sD1V/8vZHfjSDuop28K/ozqKJ0HfQ/ElKSungY+DHYGMl3kMO3RaKAv0ilvAsqLDu2twdlhSBe+hB4k9hCda1EeAYU+fGGqAfjDVb8O3YZlph/MB6LrDE7w2qphgyMOyB/htbfWI3yx0b7s83jR5V91H1zf2Tz3f4CszS72z3HYv+JjWQrp3W1ba+v2z1d0ed9r2Z7yo5sr3pnOwrRl9hCtxvHc027/vRqJ6ETsrAb9sBeGIBh2A/72R8DALMX+lg=).

## Other builds of this spec

- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 870 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013031-55350000052010501--7)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 839 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/20305012-55053005152010501--7)
- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (18/33/0) — [open the talent tree](https://talentsforever.com/warrior/60/35310003102-05053035102210501--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)). Simulations, not in-game measurements. Do not hand-edit.*

