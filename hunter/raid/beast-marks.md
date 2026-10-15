# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Marksmanship's shots with Beast Mastery's pet talents: the classic raid hunter split.* (a hybrid: Beast Mastery/Marksmanship).

**[Beast-Marks — Raid](../research/raid/builds/beast-marks-ml-raid.md)** (7/39/5) — [open the talent tree](https://talentsforever.com/hunter/60/502-0053352501522051-5-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (mm-hawk-raid), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Talents with no line below:** **Trueshot Aura**: turn it on before the pull; **Trueshot Aura**: turn it on before the pull.

**Then press the first one that is ready**, top to bottom:

1. **Arcane Shot**
2. **Rapid Fire**
3. **Aimed Shot**
4. **Serpent Sting**: keep it on the target
5. **Sniper Shot**

Between these, **Auto Shot** keeps firing on its own.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Multi-Shot**: now and then (in about 1 of 10 fights)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast-Marks puts Beast Mastery's pet talents on a Marksmanship shot core and plays the same short list as Beast Mastery: keep **Serpent Sting** up, fire **Arcane Shot** and **Aimed Shot** each time they are ready, and let **Auto Shot** and the pet do the rest.

**Why it works**

- **Serpent Sting** first so it never drops, 20% stronger with **Improved Stings**. Recast it only as it runs out (a new sting replaces the old one), and the full rotation does so only while you have 30% mana or more.
- **Arcane Shot** every time it is ready: 3 points in **Improved Arcane Shot** bring its cooldown to 5.1 seconds, about 34 casts in a 3-minute fight. **Summon Hawk** would share that timer, and in a full raid the simulator measured **Arcane Shot** as the better use of it, so this build skips the hawk.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown.
- **Aimed Shot** is listed last but goes out almost every time it can: a 2-second cast, then its 6-second cooldown. The simulator measured it slightly better below the instants; **Multi-Shot** shares its cooldown and never comes up on one target.
- The pet half: **Unleashed Fury** (+15% pet damage), **Ferocity** (+10% pet crit on top of your own crit, which Forever pets inherit), **Frenzy** and **Focused Fire** (+2% to you and the pet while it is out). There is no **Bestial Wrath** here, so there is nothing to time but **Rapid Fire**, trinkets and a potion.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator drops **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** goes first when you run low.
- Keep the pet alive with **Mend Pet**: it is about a quarter of your damage and takes no stat buffs from players in Forever. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; measured by players only at levels 20 and 30).
- Track the boss's creature type: **Improved Tracking** (3 points here) counts only against the tracked type.
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant. The simulator starts **Aimed Shot** 2.5 seconds before the pull; in a real raid, wait for your tank.

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown (up to 3 targets for weapon damage each, against 166 extra on one). For a pack, **Volley**: a 6-second channel with no cooldown in Forever.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds.
- Inside 8 yards your shots and **Auto Shot** stop: step back out at once; the pet keeps attacking meanwhile.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 878 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 817 | [7/39/5](https://talentsforever.com/hunter/60/502-0053252501523051-5-6) |
| Phase 1 BiS | 875 | this build |

**The gear** (average item level: Pre-BiS 63.5; Phase 1 BiS 66.3; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Pendant of Celerity](https://www.wowhead.com/forever/item=22340) · *Lord Valthalak, Blackrock Spire* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Giantstalker's Epaulets](https://www.wowhead.com/forever/item=16848) · *Sulfuron Harbinger, Molten Core* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/spell=7778) | [Giantstalker's Bracers](https://www.wowhead.com/forever/item=16850) · *Molten Core*<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/spell=7778) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) | [Giantstalker's Gloves](https://www.wowhead.com/forever/item=16852) · *Shazzrah, Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Giantstalker's Belt](https://www.wowhead.com/forever/item=16851) · *Molten Core* |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Dragonstalker's Legguards](https://www.wowhead.com/forever/item=16938) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Giantstalker's Boots](https://www.wowhead.com/forever/item=16849) · *Gehennas, Molten Core*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234020) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMlV2IG1UUx+fcmcycHNvs7N2vcfBjDCLbgQl3pk51+zLZIiI+SBQffNF2bFIzi9mETB4qPriFCqX4sX1rVajQLrZFpYKCCL6sLqQY2bTiB1pUtEIffAgISt9kZhKjom+70P/TzTnnnvz+5zAztANBBwMsmAcBfO6vX0zA/VCGCrRgBcA8kUfUZfN50vDjDyaMa7eQgp++C6Tgj7/tJA1f7+vGZZU0/OT9CePnAmm4vgbGH0Aa9nq68UOBFPz+96TyxHuQXFfx1UYWvrKWtDl7tkAyvtwgBc+vJte+WQXjeoEk0vDKZd34bqpYwqOR3o2MlyLrrTdg/tppOA7saHQSzoRvwtvhObi6eBFOr0EXoA+vRPtobO0jNusLzxHC3+35ni9c39stfNfxu0zpM/yJHdNomtBUScH+BhSRVFIcV8Q0M4yeOwPFPGmUc7ySH/O8qZk5knGzyVeBPxW2nt3fbHUsT3h7HFc44t691sF6uPxMrWo121ZYrdaq1tPPWZ16zWo3O2Enai5bcS1sH6xb83GtZjUaTjuMqs4o6WTJ0lLcXN5lluhuXqSd36pECn594xHOdIUm7QlUOXtYMjXKkeyKOAVN0orJ9kr8hX9xiQXHu29LuW6naZujzHPrjGEu4xAlN53ML3P8yPZP5k6asacwNyJI9yZKfjzaGbfMO/6vJKH8Ypp/9l+U/pZSRrSfP0mz9jTKHJcStM0NSBCJuTEZ9iyqPH8BhsyjOfo0Z8+gyvECZKjjhG4XhrtPm+zJ/G5uAF/a9pFnz8ONk8AfMyv0IH+ApuzJ8XxHrhK3/3CVI5nATZfxd09ZOO25vlIx5OusCwPmHZGlVPPl4zBDUzSJqo4G7JJSDQIBxfNyPjlLK4fKt752KtGl4K5Dqb4KvAEzFCuwu0y6qdQpj07bqnve2fL/Wfi81+vtOHCxvDgMlA/AMYBTEDUHL156/MtgIY1K/WAxqez1fg0ezQ5XA1vGD+f23TZ+IWdfl4egAk9AHVpwGA7zPwcADPhUIA==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMlU9oI3UUx+f9ZjLzy3NN01+SZhz8MwaR7MCE38w6q93LpIuIeJAoHrzo7rjJmim2CZkcVhDs0i4si3/KnrYirLCUbYtCDwoieKkUUow0bf2HFgSt0IOH3KQ3mZnEqOitBb+nN++9+c3n+x4zg6copEEFHYrAgeX/vCIcnoAyVKAJcwDazSSlaVF7AxX6+Sdj6sE9KNGDdwEl2psHVOgXy6DuyGHw8Zj6SwoVujsP6u9h6et5UH9KoUT3os61BQhvV+jOMH/3WnjO7jKgSN+eQYmuLoaN3y+CephCARW6dBPUHzOFEl3w0x1ffcvX774PxYPbcAPIgn8L7ngfwIfeCuxPrcPtZegA9OAd/zyOvH1GJhxum5w7Z844tsMtx7a5Y5lOh0g9Qn8m1xXMItXk0NEmFCjKKJkWDzA3yK7cgUISFUyYdskJWFJTtASKdLvBFoG97DVfu9BotnWb22dNi5v8sXP6pbo3+2qtqjdaulet1qr6K6/r7XpNbzXaXttvzOpBzWtdquvFoFbTZ2bMludXzWHRjIul6aAxe1or4SOsgPf+ICNK9LujZxlJSzhujFGZkWcETcEEihYPItCwLGnknMDe/AcXnzTtx4+V6wHMGoyKLLFBCE3EHLxkRZP5Nc+unvxkHsKckaGJIUG0N15yguHOmK49+F8tIeVeln35b5TOsVL6eIG9hBNGloqMTodo25sQIiKxAlSNCSqz5BoMmIdzdDBv5KjM6BrEqKNC2kgNdh8dcjb2u70JbPrERx6/D0e3gD2vVfAp9iRmjPHRfIeuQrd/c5VAEcGKlvFXT3E6OnNjrqKKh6QDfWJfFYVIxfINyGEGx6mcpiqcFiL1XQ6FVTEZxsLc5fJ97y2F2nIfvhzpW9fuE1XSXaNDhP+V2uVhdKJ69KNjf87kV91u99TF9fLUIFG+CNcBlsBv9K9tvfCNOxllhZ47FXZ2u7+5z8XBvmuI9NP8+ftHH+T49/I0VOBFqEMTrsAV9scAQ7RSLw==).

## Other builds of this spec

- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 806 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--6)
- [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 803 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

