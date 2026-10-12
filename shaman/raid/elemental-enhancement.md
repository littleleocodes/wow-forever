# Elemental-Enhancement Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Elemental-Enhancement

*A Lightning Bolt caster that dips Enhancement for its passive bonuses.* (a hybrid: Elemental/Enhancement).

**[Elemental-Enhancement — Raid](../research/raid/builds/elemental-enhancement-ml-raid.md)** (22/29/0) — [open the talent tree](https://talentsforever.com/shaman/60/530533102-05503001100510224--6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (elemental-raid-dps), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull, then keep up all fight:** **Strength of Earth Totem**, **Grace of Air Totem**, **Searing Totem**.

**Then press the first one that is ready**, top to bottom:

1. **Stormstrike**
2. **Flame Shock**: keep it on the target, until the last 10 seconds of the fight
3. **Lightning Bolt** when Maelstrom Weapon has 5 or more stacks
4. **Earth Shock**
5. **Fire Nova**

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

This hybrid is a melee shaman, not a caster: it plays the Enhancement list, and its 22 Elemental points make your shocks and **Fire Nova** cheaper, more frequent and harder hitting. Your weapon and **Windfury Weapon** still do about half the damage; spells fill the gaps between swings.

**Why it works**

- The order is Enhancement's: **Stormstrike** first (125 mana, a weapon hit, 20% more on your next **Lightning Bolt** or **Earth Shock**, and **Improved Stormstrike**'s mana regeneration while casting), then **Flame Shock** whenever the burn is off, a 5-stack **Lightning Bolt**, **Searing Totem** when it expires, **Earth Shock**, and **Fire Nova**.
- Your Elemental points shape the shocks: **Reverberation** brings the shared shock cooldown to 5 seconds, **Convection** and **Shamanistic Focus** cut their cost, and **Call of Flame** adds 15% to **Flame Shock**, **Fire Nova** and **Searing Totem**.
- You have 4 of 5 points in **Maelstrom Weapon**, so 5 stacks leave the bolt a half-second cast at a fifth of its mana. Still wait for 5 stacks: the rotation's condition is above 4.2 stacks, and the simulator measured waiting for 5 about 5% better than casting at 3 with this list.
- **Fire Nova** erupts around your Fire totem, so keep **Searing Totem** within 10 yards of the boss; **Improved Fire Nova** makes it 20% stronger on a 6-second cooldown. Adding Fire Nova to this list measured 7% more damage.
- **Elemental Devastation** turns every spell crit into 9% more melee crit chance for 10 seconds, which feeds **Flurry**: another reason to keep a spell going between swings.
- Put **Windfury Weapon** on your weapon with a sharpening stone on top: in Forever an imbue and a stone stack.

**Caveats**

- No **Rage of the Farseer**: it needs 30 Enhancement points and this build has 29. Use your trinkets and potion at the pull instead.
- Mana is tighter than for Enhancement: the simulator has this build out of mana for about 34 seconds of a 3-minute fight. Clearcasting from **Elemental Focus** makes your next damage spell free; use a mana potion when you are low, and do not hold shocks back.
- Several targets: **Fire Nova** hits every enemy within 10 yards of your Fire totem.
- A caster split of these trees (29/22/0) was the search's best only on the training dummy; in a full raid this melee build measured 22% ahead of the hand-made caster draft. For a Lightning Bolt caster, play Elemental.

**When to change it**

- In the last 10 seconds, skip **Flame Shock** (its burn would not finish) and use **Earth Shock**.
- In a party of warriors and rogues, ask whether they want **Windfury Totem** instead of **Grace of Air Totem**: a party gets only one, and it does nothing for you while you use **Windfury Weapon**.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 690 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 663 | [22/29/0](https://talentsforever.com/shaman/60/500533132-05503001100510224--6) |
| Phase 1 BiS | 679 | this build |

*Gear-tier numbers searched on 2026-10-03, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 62.9; Phase 1 BiS 64.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Deep Earth Spaulders](https://www.wowhead.com/forever/item=18829) · *Molten Core* |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) |
| Chest | [Zandalar Augur's Hauberk](https://www.wowhead.com/forever/item=19828)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) | [Gloves of the Greatfather](https://www.wowhead.com/forever/item=17721) · *Leatherworking* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Lord Valthalak's Staff of Command](https://www.wowhead.com/forever/item=22335) · *Lord Valthalak, Blackrock Spire*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Staff of Dominance](https://www.wowhead.com/forever/item=18842) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/enhancement/#eJzMlE9oE1kcx+f3ZpJ5+W23TadddjrbZacpLN3AhDeTZml6SdrTsqcG9tDbdmymJv5JQiZIvUjV+oeiFk/a4kGRUoW0VhCpvQgVYioRclDBP4hoCz14KCoV9CKTpK32bIvf05svnze/73u/xw/rKHhBBhU6gIHUsvlFGHRBFPqgHzIwAqAsidTtFZUsivTzDMgrP6FAj98AFOir9z+jSJ9eAXmEoEg/TIL8ph5FujgF8vN6FOjClIO9XHewwq0GZ69I5/Igj4so0PvTDnNvFpCnxywU6O2yF0V6dxbkYhNyyPmCdDTpLSblM0l1+hJ0vNvft3wT+seOjAEZTV6Eq+ZlyJvX4FnPPKzoRYAynEv24tbBFshvIcZCwaAeNDQWCrEgY7rOWEhnhtFZJFAm/GvywIW/IFXcKNDzBfB5UESX1hkI2dhUs8cL4BPRhbwWtLEZRcWFPC3EaqgeCNnSH8rv2ORvpILkGuMJBWcfEmZv/HY7QL4BxgsgCQrp5iRUqiUfnQLpAkhDZubA/+lMTjWY8bfGwprR1a0OJszUXiuuprOqGY9bcXXPYTWXsNRsOmfmkumUaltmdjChdtiWpVqphJkatA5aqZwWz9jaBqRVocA+O536S9GwXWrDOh8iNZzy+WXARn8DdUvkX06pnF2vZc0vg3R2ezKdaSy8I8naUfHL1C15FsEJduejrFSuvTNg6F2VRqwekk7u3k21ft1FfrOLTpBCTPIo1ccxG5Oyuxap+mIm1mWZXyVFWCPGUZ6rqDn6CVChSCh4eRl813mPY3MjQ9GWyQlHS5G2oYqeRIw1IgtqxF8k3A+lXHRjtaP6c+a71wk/LJVKdQNz0Z6aER2A0wATkEyvnVj673EkXHG5cqTHIUult5FYdfEi4ufp/K+9rVvDrDqX/6lM5gRkYBiGpS8DABnXLhA=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/enhancement/#eJzMlE9oE1sUxufcmWRuzittOu3jTef18aYpPPoCE+5MmkfTTdKuHq4acNGdHZupiX+SkAlSN1KlVQnWoqVoiwtBRIW0VBBpXUmFkGiELtSFutIWunBRXCgoiEySttq1LX6L4c6Z353z3XsOBxsoeEEGFbqAgdS2/UYY9EAUBmAQMjAGoJRF6vaKShZF+mUe5PXfUKBfrwAKdHIaUKQPJkAeIyjS8gzI7xpRpCu3QH7diAJdzjvYoxkHK95vcvaKdLEA8pSIAn284Hx9OuM8x6cBeXrWQpHOTYNcakEOOV+Qjie9paR8Manevg5dH44NrN2DwfzpPJDx5DW4ad6AgnkHXvUtwbpeAliFS8l+3DnYQ/JnKMhCwaDODI2FQizImK4zFtKZYXSXCKwS/i154sLfkSpuFOjlIvg8KKJL6w6EbGyph6eK4BPRhbwWtLEVRcWFPC3G6qgeCNnS38pf2OJvpoLkyvOEgrMPCbO3frsbID8AU0WQBIX0chIqtZTPz4N0FaQRM3P8UDqTUw1m/KexsGb09KrDCTN1xIqr6axqxuNWXD18Ss0lLDWbzpm5ZDql2paZHU6oXbZlqVYqYaaGrRNWKqfFM7a2BWk1KHDUTqf+VTTslDqwwYdIDSd9YQ2w2d9E3RI5wCnVs+t1r4U1kCZ3O9OZxsJ74qwTFb9M3ZJnBRxjy59kpXrt3QFD76kWYuOkdG7/bqr9+yry21V0jBRjkkepNcdCTMrum6Vax8x+lGV+g5RgkxhneK6q1uhnQIUioeDlZfDd5T1OmBsbibbNzToqRzpGqnoZMTaJLKgRf4lwv5Ry0a3Vnuqf+Z+eJ/ysUqk0DC1G++qB6BBcAJiFZHpzonzwRSRcjXKrkT6HrFTeR2K1xZuIn6dLf/S37wyz2lz+vzqZE5CBURiVvg0AwaIrwA==).

## Other builds of this spec

- [Elemental — Lava Burst / Lightning Overload](../research/raid/builds/elemental-raid-dps.md) (29/22/0, 518 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/550230130210304-255000001340002--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-12 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

