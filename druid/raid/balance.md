# Balance Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Balance

**[Balance — Moonkin / Eclipse](../research/raid/builds/balance-moonkin-raid.md)** (33/5/13) — [open the talent tree](https://talentsforever.com/druid/60/0532220115501051-05-505003-6)

## How to play

**Before the pull, then keep up all fight:** **Moonkin Form**.

**Then press the first one that is ready**, top to bottom:

1. **Insect Swarm**: keep it on the target
2. **Moonfire**: keep it on the target
3. **Starfire**

**Starfire** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Innervate**: when you run out of mana (needed in about 1 of 10 fights)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

A raid Moonkin keeps **Insect Swarm** and **Moonfire** ticking on the boss and casts **Starfire** the rest of the time. **Moonkin Form** goes up before the pull, and **Innervate** is your mana button.

**Why it works**

- **Moonkin Form** first (the rotation shifts 10 seconds before the pull) and for the whole fight: it gives your party 3% critical strike chance and doubles how often **Omen of Clarity** makes your next spell free. The aura does not stack with **Leader of the Pack**, and you cannot heal while in the form.
- **Insect Swarm** and **Moonfire** each do close to a fifth of your damage for one instant cast every 14 to 15 seconds (**Nature's Splendor** makes them last that long, **Genesis** adds 5% to their ticks). Recast each one the moment it runs out, not before: recasting a running one throws away the ticks it had left.
- When both are due, **Insect Swarm** goes first: it costs 160 mana against 375 for **Moonfire**, and the simulator measured that order 0.3% better in a full raid (1.8% on a training dummy, where mana runs short).
- **Starfire** is your filler and about two thirds of your damage. It beats **Wrath** per second of casting at any gear: 350 to 412 damage plus all of your spell power in 3 seconds with **Improved Starfire**, against 92 to 102 plus 57% of it in 2 seconds. The raid build takes no **Eclipse**, so **Wrath** has no place in the list.
- Critical strikes feed the filler: **Vengeance** doubles their bonus damage, and every critical hit from **Starfire** or **Moonfire**'s first hit triggers **Nature's Grace**, 10% faster casts and global cooldown for 3 seconds.
- **Innervate** at 30% mana: for 20 seconds your mana regeneration is five times higher and all of it continues while you cast (6-minute cooldown). Not earlier, since regeneration is wasted once your bar is full. With a raid's Blessing of Wisdom and Mana Spring you need it in about 1 fight in 10.

**Caveats**

- Moving: **Starfire** needs 3 seconds standing still. Refresh **Insect Swarm** or **Moonfire** while you move, then go back to **Starfire**.
- Damage taken pushes your casts back. **Nature's Focus** gives you a 70% chance to ignore each push, and **Barkskin** (1-minute cooldown) stops pushback for 15 seconds without slowing your casts as it did in Classic: press it when the raid is taking damage.
- Without raid mana buffs (a small group, or alone) you run short. The training-dummy rotation then casts rank 1 **Starfire** (95 mana) whenever a full one is out of reach, which the simulator measured better than waiting for mana.
- **Eclipse** (each **Wrath** takes up to 0.5 seconds off your next 2 **Starfire** casts, at 3 points) is not in the raid build despite its name, and no rotation here weaves **Wrath**. A 3-point **Eclipse** with a **Wrath** whenever its charges run out has not been simulated.

**When to change it**

- When the boss will die before a 3-second **Starfire** can land, cast an instant **Moonfire** instead: its first hit lands at once.
- In the last 10 seconds of a fight, skip a new **Insect Swarm**: most of its 14 seconds would tick on nothing. The simulator measured that 0.2% better on the training dummy.
- On a pack that will live a while, **Hurricane** hits every enemy in the area each second for 10 seconds (1,495 mana); the list itself is for one target.
- If you end fights with mana to spare, your raid may want **Innervate** on a healer instead: it works on any target.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 592 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 566 | this build |
| Phase 1 BiS | 614 | this build |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 62.8; Phase 1 BiS 65.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair* |
| Chest | [Ironfeather Breastplate](https://www.wowhead.com/forever/item=15066) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Leggings of Arcana](https://www.wowhead.com/forever/item=12756) · *quest: Leggings of Arcana*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Lord Valthalak's Staff of Command](https://www.wowhead.com/forever/item=22335) · *Lord Valthalak, Blackrock Spire*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Staff of Dominance](https://www.wowhead.com/forever/item=18842) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/druid/balance/#eJzMk79rFEEYhvedHW8/v0viZhPJOiqeB0o4OJndY8HY7N5VFhYRLCxDxOiKYiAqKaNEEIuIlSTYKEgUTEglYiMkBjewyiFR8AciCaKgyIFgYyO7UeMfoOBTffPM+zJTzHAbwYaLEnqh4fT8XgmNCP04jGGMAWpZkGUX1Um26PsM3PdFlrRyDSzp3dd2lvTyBrhAr866qx1s0fwtuK872KTFYyzp7bd2LtDykaxl0dxduFcslrQwm9UfT2e5C0dZ0r2mzRY9nIWbdLHBRnkHjcd2Epemr6P36QT6bz7CZYjx+DY+1JuYiBu8fvkHQumg5vu+9rwg0J4OvKoOqoEOtK4lAk1RXBHnuJvpRIElTc2jTFxgWfX0iCOV2Gc429VW7qxsIumIQUNZvIHNmt6lsviXVTibVVejkyVdXYCNtW19asTpVk7DZpM+HfjTsqK8+GwRrvlRJGgJ/7xp5OyJBgtKsmCjfMfcmBljbCjaMjWZsRTuHMp5Efot4cpSWEmE8V9xJvo1/VN2z/z1c/qepGnaNjAX1X+KaACXgEnEp1sXlw49D/tyazTDepZM08/hwbXhTVgx6X5PY9v6i9PYiwj7809yHMMYxajzYwCjTXnh); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/druid/balance/#eJzMk7FrFE8Ux/c7O7/b93sXk8smknVUPA+UcHAyu8eCsdm9qywsIlhYhoDRFdRARFJGuYBYRDRckcNKEBWMpBARK0mM7OEqh2AaLcQgCoocWAoiu1HjH6Dgp3rzed83M8UM9xAKcFDEMDTsoV8roRFiFEcxiRlArQmyCnl1mi36ugjnXZ4lfbsKlvTmyxaWdH8WbFG7CWe9ly1avgHnVS+btHqcJT1qps0n9/rSOYuW7sC5bLGklbvpBk+bYJMuHGNJjfk02JqHEw+wwUZpFzWiQhwVb17D8PM5jF5/jEsQjegW3tc6mIvqvHn9h0Jpv+p5nnZd39eu9t2K9iu+9rWuxgIdkX8rzvEg08kcS2oto0ScY1lx9ZQtlThg2DvVdu4v95G0xbihLP6Pzareo9L453XYW9VAvZ8lXVlBARttfWrKHlR2vcAmfTz0u2VF2eCLVTjmBxGjK7zzppGxLxzPKcmCjdJt8//UGDMT4bbWQko72D2RsRZ4XeHIYlCOhfFPcTb8Wf1V9i7+8XNGniVJ0jO2FNZ+iHAMF4EFRGe6s+0jL4ORzBqdoJYmk+RTcHijeB2UTXowVN+x+eI09iPEweybnMAkpjFtfx8Ak5Z4vQ==).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-14 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

