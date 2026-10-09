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
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire* | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire* |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair* |
| Chest | [Ironfeather Breastplate](https://www.wowhead.com/forever/item=15066) · *Leatherworking* | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core* |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Leggings of Arcana](https://www.wowhead.com/forever/item=12756) · *quest: Leggings of Arcana* | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking* |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) |
| Finger | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Lord Valthalak's Staff of Command](https://www.wowhead.com/forever/item=22335) · *Lord Valthalak"].." - "..format(AL["Tier %s Sets, Blackrock Spire* | [Staff of Dominance](https://www.wowhead.com/forever/item=18842) · *Golemagg the Incinerator, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/druid/balance/#eJzMk7FrFE0YxveZme/u/d4kulkjnqPi5UAJByezeywYm927ysIigoVYHRFjVhADUUkZJYJYBK0kQQsFiYKRVCI2wmnwAqscooIiIrFQUORQsLGR2ajxD1DwVyzP/uYZZop3uJvgooAiBmDg9f/6EwYxhrAfDYxiDJPAWeA8oJuC8m6XPsCKvs2DFS1ftN83X3pY0YsrYEkvT7Ci5jUbFw+zotdfe1jS04OsaOGmLV/+7LKih3NrWNLpQ6zodtuKe7fADjulrTSVuK2kOHcJA4+nMXT1Ac5BTCXX8a7WxnRS59VL3xXahNUgCIzvh6HxTehXTFgJTWhMtSXQFl3L4iT3MR3JsaLZJkrEOVYV34x7SotdjrdFb+Le8lpSnhh2dJ7/Y1k127Stf3oLb71eV+9lRRfuw8XKsjk67vVpr+6ypA97fresKdv4ZBEF+V600BHBKelk7IiHc1qxYKd0Q/5vjTM5Em+cnbEsRf0jGc+joCMK+WJUbgnnn+J4/DP9VbbP//FzBh+ladrdWIhrP0TcsOM8g+RY58zSvmfRYGaddlSzzTT9GO1dCa+isqQ7G+qbVyfOYCdi7M4exyjGMIEJ7/sAt+N2EA==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/druid/balance/#eJzMk7FrFEEUxuebHe+eL5Fs1ojnqHg5UMLByeweC8Zm966ysIhgYWFxBIxZQQxEJGWUC4hFUEOKBG0EUcFAChGxkpjIHa5yCFpZiBYKihxaCiKzUeMfoOBXPL75zTe8Kd7jXoKLAooYgoE3+PskDWKM4BgaGMcEpoGLwGVAr0rKuz36OCv6tgRW9P2qrW++bmFF92esb8/bunIT7NDaSVb0KANP7vWxouW71l//4rKip/M2cuEEK2rOWbw4BxYsSnuombitpHjrGoaez2LkxiouQTaT23hf62A2qfPGtx9KbcJqEATG98PQ+Cb0KyashCY0ptqS6Miet/IcDzCdytkWKygR51hVfDPpKS0PCm+33sn95T5SnhwVOs+b2KmavdrGP7+Dt01vrfezoiuP4WL92pye9Aa0V3fZoY+H/6SsKXv4Yg0F54NsoSuD847ItD8ezWnFkkXpjrPZEjE9Fu9YXLBqR4NjmV5FQVcW8sWo3JLiv9LZ+Jf7p9q39Nf7DD9L07S3sRzXfoK4YQd6AcmZ7kz76MtoOKOiE9VsMk0/RUfWzeuo7NCD7fVdGxNncAAxDmXrMY4JTGHK+zEArSx07A==).

## Other builds of this spec

- [Balance (optimized)](../research/raid/builds/opt-balance-dps-raid-dps.md) (33/5/13, 592 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/0532220115501051-05-505003-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

