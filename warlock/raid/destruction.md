# Destruction Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Destruction

**[Destruction — Raid](../research/raid/builds/destruction-ml-raid.md)** (10/11/30) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055020510310035-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (destruction-incinerate-raid), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Shadow Bolt setup. The spec's best build for each other setup, in a full raid:

- Fire: [Destruction (optimized, fire)](../research/raid/builds/opt-fire-destro-raid-raid-dps.md) (10/11/30), 692 DPS in a full raid — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055030510310025-6)
- Incinerate: [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-raid.md) (9/11/31), 672 DPS in a full raid — [open the talent tree](https://talentsforever.com/warlock/60/153-0050203001-0050245103101351-6)

## How to play

**Before the pull:** **Life Tap**.

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage for 2 hours; summoning any demon cancels it).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Conflagrate**
7. **Shadow Bolt**

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Shadowburn**: in the last 1.5 seconds of the fight, when there is no time left for another **Shadow Bolt**
- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Destruction in a raid is still a **Shadow Bolt** spec: you sacrifice the Imp for 15% more Shadow damage, keep **Immolate** on the boss so **Conflagrate** can go out every 10 seconds, and let **Shadow and Flame** turn each **Conflagrate** into 10% more Shadow damage.

**Why it works**

- Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours; summoning any demon ends it), then **Life Tap** once so you start full. Put a Spellstone (**Create Spellstone**) on your weapon on top of your wizard oil: Forever lets them stack, and the simulator measured about 3% more damage. This build has no **Amplify Curse**; without the sacrifice the simulator measured about 10% less damage.
- **Curse of the Elements** goes up first: 10% more damage from every magic school, Fire and Shadow alike, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana (the simulator measured that 0.4% better than 10%), and **Improved Life Tap** adds 20% to each tap.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (0.8 seconds with 3 points in **Improved Corruption**) goes back up when it is about to run out, but not in the last 10 seconds.
- **Immolate** matters as much for **Conflagrate**, which needs it on the target, as for its own damage: start a new one when less than its cast (1.5 seconds with the **Bane** talent) is left on the old one, but not in the last 20 seconds. Both end-of-fight cut-offs measured small gains.
- **Conflagrate** goes out whenever it is ready. With 5 points in **Shadow and Flame** it no longer eats your **Immolate**, and each hit gives you 10% more Shadow damage for 20 seconds, twice its cooldown; **Fire and Brimstone** and **Ruin** make its crits frequent and big. The simulator measured adding it at about 8% more damage.
- **Shadow Bolt** is the filler, not **Incinerate**: the sacrificed Imp, **Improved Shadow Bolt** and **Shadow and Flame** raise Shadow damage only. Even the Incinerate build's own rotation search put **Shadow Bolt** ahead of **Incinerate** in a raid.

**Caveats**

- The last seconds belong to quick spells: with 3.5 seconds left the rotation casts **Searing Pain** (a 1.5-second cast) and with 1.5 left an instant **Shadowburn**, because a **Shadow Bolt** still casting when the boss dies does nothing. Neither belongs earlier in the fight.
- **Shadowburn** on cooldown measured worse in the fire rotation (about 0.8%): it costs nearly as much mana as **Shadow Bolt** for about two thirds of the damage. Keep it for the last global cooldown, or for a moment when you must move.
- With the Imp sacrificed you play without a demon: any summon ends the buff, so if you die, summon the Imp and sacrifice it again before the next pull.
- On the move, **Bane of Agony**, **Curse of the Elements**, **Conflagrate**, **Shadowburn** and **Life Tap** are instant; **Corruption** still has a 0.8-second cast in this build.

**When to change it**

- If you play the Incinerate build listed above instead, it still fills with **Shadow Bolt** in a raid: its full-raid rotation adds **Shadowburn** on cooldown (with 10 or more seconds left) and keeps **Shadow Bolt** ahead of **Incinerate**.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 710 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 712 | [9/11/31](https://talentsforever.com/warlock/60/252-0050203001-055030510310035-6) |
| Phase 1 BiS | 744 | [9/11/31](https://talentsforever.com/warlock/60/252-0050203001-055030510310035-6) (ties this build) |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 62.5; Phase 1 BiS 65.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire* | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire* |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Stats](https://www.wowhead.com/forever/spell=13824) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Stats](https://www.wowhead.com/forever/spell=13824) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire* | [Nemesis Leggings](https://www.wowhead.com/forever/item=16930) · *Ragnaros, Molten Core* |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18467) · *quest: Harnessing Shadows* | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Elemental Attuned Blade](https://www.wowhead.com/forever/item=20698) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMlU1oK1UUx3PuTDI3x/a99D6lk/GDMdBHDEy4M2Fs0k3StyquKrgQCtqkSZuEkoRMFhU31VYUkSpm1VDQKqUt2BrcWF35FUwhSjcKWqviRhcugko2bmQm0xTaLlyk8M4iOXP+98z9/edcuDhCIQAyqBAGDiw4eCIc4pCCWXgWKrAKoOwhFQJ+pYIi/fcAUKRrH9q/v/49ihL9YRvkVYI+elyS35VQol/sgHx6CwXaWkKR/twbRYH+tYgSbX4A8psSivTLQ7v961170cs5FOn7bwFK9MdtkNt3UKSfHILdsxzidL0QaBfU3S0If7sBvJeZfe8reB3IeuFtIL3MHvw+3YR3duAImjMnsFG4hxeePiWPGaahcW5yg8c41zVumjzGTZ3HdM5jZpsIJ+SB38g+xTtIFR+KtLsBIQm9KGimhQ+ipHhRoPtzIT9K6NX0qGmxR5WHcSx0G0c/AkSRfvbqLCMBr9Nt54bCMczu4ljkNvUx8pRHcd6nm5ZTEhnJuKVJc0IRkchjrA7suXRl+flypaYa3HhS07nGjSl1IZ8uLeWyarmqprPZXFbNvKDW8jm1Wq6la4VySbVy6epCXg1buZxqZbRqupDVzkWtL0aLVrn0hKL/T6g4n7A9B3oZJipkytO32wcftEVNx+7HdbhOjrny2hvAXrxkjCc0Y3KoxoIYiNyigvNZfSgiMSfcoTFUBkNlIUXF8chDVGRS0ZY/n1Nog7hZ/49tXR6DTRsfKu0UchbFYGSciowWbbhfWqD4G8RNr0yIW4orXY83ecN4Zxd4Z1fxDBfvrAWseInOPsP6UOn60/ynfv1eieHvFVivw+AUnbZAFv4gbegS4yXB40Qi1SAjiEgpqCQMcRLaF/y24FldTAUbm3YcJx9fdOL7pNElsqgmI23iua+iljrPbjTuHgx9n8Q3nU5nZL6ZmnYLqXl4DWATCuXuK8fPfJdMOFXPSXLaXtnp/Jl8up/8lIwI9Gj83iMXF0b/2ptxLr48VGAFVth/AwCvh3sA); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMlU1oK1UUx3PuTDo3x7730vuUTsYPxkAfMTDhzoSxSTdJuyquIrgQCtqkSZuE0oRMFhU3VVMqIhUaumgoqIWiFVuCG6ur+hFIMWo3ClKL4kYXLoJKN4LITKYptF24SMGzSM6c/71zf/85Fw4OU/CDDCqEgAML9J8IhxgkIQXPQxlWAJQPkAp+n1JBkf69DyjSfzbs35//vIMS/eFdkFcISvR4E+R3JJTo57sgn95FgbYWUKRHm/banRqgRJsfgvyWhCL94sAufuVItTqgQF/NoUS/XQW5fR9F+smBXftjMchpreBvF9T3tiH0zTrw80xq50t4A0itsAHkPPM+/DrZhLd34RCa0yewXpjCS1efkicM09A4N7nBo5zrGjdNHuWmzqM651GzTYQT8tAvZI/ifaTKEIq0uw5BCb0oaKaFD6OkeFGgezNBH0ro1fSIabHHlUdxJHgP73wEaBtcSzHi9zq7j9ZSzFA4htgDHAnfo0OMPONRnPfppuWUREYybmncHFNEJPIIqwN7IV1efLFUrqoGN57WdK5xY0Kdy6eXFnJZtVRR09lsLqtmXlKr+ZxaKVXT1UJpSbVy6cpcXg1ZuZxqZbRKupDVLkStJ0aKVmnpKUX/j1AxPmZ79p9nmKiQCU/Pbg+8vy1iOnY/rsNNctSVX3sT2MtXjPG4ZowP1FgA/eG7VHA+6xCKSMwxt2kMlX5TWVBRcTT8CBWZVLTlz2YU2iBu1vtj21fbYNPGBko7gZxFMBAepSKjRRvupxYovgZx02sd4pbiSjfjjd8y3tkl3tl1PMPFO2sBK16hs++wPlC6Xjf/qt98VnzwZ/lrdejfotMWyMJvpA1dYrwieJyIJxtkGBEpBZWEIEaCe4LPFjwr88lAY8uO48ST8058nzC6RBbVRLhNPP+rqCYvsluNB/sDPyf+dafTGZ5tJifdQnIWXgfYgkKpu3r83HeJuFP1nCQm7ZWdzu+JZ3vJj4mwQA9Hpx67HBi9wTftjL48lGEZltm/AwA4PHpy).

## Other builds of this spec

- [Destruction (optimized, fire)](../research/raid/builds/opt-fire-destro-raid-raid-dps.md) (10/11/30, 692 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055030510310025-6)
- [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-raid.md) (9/11/31, 672 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/153-0050203001-0050245103101351-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-14 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

