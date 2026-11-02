# Retribution Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Retribution

**✅ Recommended** for raid (the best paladin spec here, or within 3% of it).

**[Retribution — Raid](../research/raid/builds/retribution-open-raid.md)** (16/4/31) — [open the talent tree](https://talentsforever.com/paladin/60/0502510021-4-35233001001301351-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Seal of Command**, **Seal of Righteousness**.

**Talents with no line below:** **Repentance**: taken because Unsealed Wrath requires it.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**
2. **Hammer of Wrath** when the target is below 20% health
3. **Consecration**
4. **Holy Strike**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of the Crusader**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Retribution Aura**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Retribution in a raid twists seals: you swap between **Seal of Righteousness** and **Seal of Command** around every swing so each hit carries both, judge **Seal of Righteousness** on cooldown, and give the remaining global cooldowns to **Consecration**, **Holy Strike** and, under 20% health, **Hammer of Wrath**.

**Why it works**

- Only one seal can be active, so keeping up two seals means a twist: with **Twist of Light**, replacing a seal leaves an Echo of it that your next melee swing applies. The full rotation casts **Seal of Righteousness** in the last 0.4 seconds before each swing and **Seal of Command** after the swing, in any global cooldown that **Hammer of Wrath**, **Consecration** and **Holy Strike** do not need: about 14 and 12 times a minute. Opening with **Seal of Command** means your very first swing already carries both.
- Press **Judgement** every time it is ready while **Seal of Righteousness** is up, whether or not the short list shows it. It is off the global cooldown, comes back every 8 seconds with **Improved Judgement**, no longer uses up your seal in Forever, and **Sanctified Judgement** returns 60% of the seal's mana cost; in the simulator the judgement of **Seal of Righteousness** is about an eighth of your damage. If it comes off cooldown while **Seal of Command** is up, judge anyway.
- **Hammer of Wrath** goes first once the boss is below 20% health: with 2 points in **Instrument of Law** it is instant, it comes back every 6 seconds, and at about 500 Holy damage plus a share of your spell damage it is your biggest single hit.
- **Consecration** comes before **Holy Strike** while you have at least a quarter of your mana: on a single boss it deals 312 Holy damage over 8 seconds plus a share of your spell damage, about a sixth of your damage in the simulator, and **Holy Conduit** makes it 40% cheaper.
- **Holy Strike** sits last but is not a real filler: it has a 10-second cooldown, so press it whenever it is ready (20 mana, and **Sacred Arbiter** adds 20% to it). The global cooldowns between your other buttons go to the seal swaps.
- **Seal of Command** is always rank 4: every rank adds the same 70% of weapon damage, rank 4 costs 30 mana less, and the simulator measured it 0.3% better than rank 5. When mana runs low the full rotation steps down: **Seal of Righteousness** rank 7 below half mana, **Seal of Command** rank 2 below 30%, a rank 1 **Consecration** below a quarter, and no seal swaps at all below 15%.

**Caveats**

- The twist rests on the simulator's reading of **Twist of Light**: every Echo you have up fires on the next swing, so a swing after both swaps applies **Seal of Righteousness** twice (the seal and its Echo) and **Seal of Command**'s chance once. If the game allows only one Echo per swing, one swap per swing, alternating the two seals, does the same work with half the global cooldowns: check it at launch.
- All those swaps cost mana, even 20% cheaper with **Twist of Light**. The full-raid numbers assume the raid's **Blessing of Wisdom**, Mana Spring and other paladins' judgements of **Seal of Wisdom** and **Seal of the Crusader** on the boss; with only your own buffs the simulator keeps **Seal of Righteousness** up and twists on every swing only while your mana is above about two thirds.
- Forever weakens ranks far below your level, and the simulator applies an assumed formula (TBC's) since 2026-10-09. **Seal of Command** rank 4 and **Seal of Righteousness** rank 7 are close enough to 60 to lose nothing, but rank 1 **Consecration** keeps only a bit over half of its spell damage bonus, so it is a low-mana stopgap only; the game may also lower a low rank's chance to trigger effects, which no simulator models.
- Several targets: only **Consecration** spreads (its bonus damage hits the first four enemies in it); your seals, judgements and **Holy Strike** stay on one target.
- The full rotation also has a **Holy Shock** line (after **Holy Strike**) for builds that take it, worth several percent there in the simulator; this build has no **Holy Shock**, so skip it.

**When to change it**

- If you cannot time your swings (no swing timer, high latency), skip the swaps: keep **Seal of Righteousness** up, judge it on cooldown and press **Consecration** and **Holy Strike**. How much that costs on the current beta build was not measured.
- Against an Undead or Demon boss, add **Exorcism** on cooldown (15 seconds, 40% cheaper with **Holy Conduit**): it hits harder than **Holy Strike**. The simulator's target is an Elemental, so where it fits best was not measured.
- When you have to leave melee range, keep pressing **Judgement** (10 yards) and, under 20%, **Hammer of Wrath** (30 yards); your seals only work on swings.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 840 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 893 | [12/8/31](https://talentsforever.com/paladin/60/050150001-503-25233001011301351-7) |
| Phase 1 BiS | 903 | [12/8/31](https://talentsforever.com/paladin/60/050150001-503-35233001001301351-7) (ties this build) |

**The gear** (average item level: Pre-BiS 63.6; Phase 1 BiS 63.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Storm Gauntlets](https://www.wowhead.com/forever/item=12632) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Storm Gauntlets](https://www.wowhead.com/forever/item=12632) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Grand Marshal's Sunderer](https://www.wowhead.com/forever/item=18830)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Sunderer](https://www.wowhead.com/forever/item=18830)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) | [Libram of Law](https://www.wowhead.com/forever/item=272435) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV2tsFNcV3jM7O3t91uvHxY/xxeDpFoO97bozs92KuoAXm7Y8anVr1EKlqmXsHXuXrnfcmbVl/lRuRelDiCqJlAikQMRDQg4EBIqErKBIRJEIv4iSOAiJxNr8iSKiEP9AyUqJopn1eh/4ERRQ7o/V7LlnzuO79/uOBlsJ1IEIEnTAAUjAGEwB/AfgJYDzALTa2eXs3c3AZpsJX8exSRTI3KCY9SFPjlwE5MnxT+rQS944B+LbAnrJly+D+FENesmNcyDeq0GB3BkUT3mRJ1+8COgln78C9ttecvkCiB/WIE++et4O8945+/fV23XIk2det0Meew7E+zXoQp5cvV0X6Kq7meyY/6v8cDA2ewz+B9zh5LPAPRw8AcIZ7YJ2d/s0eI8mp8/DseQcHE72Eqd8iMIM1yZHZCUiy7ISisjhkBpRw2FZVmRFCctKOKLc5Pgsd68RN+HaLIjYtH0ok5zQMrqkWVZyJK3HJW3c1AIEBeRDqmyhhA3TUI+1OaEaMTaeSkmmlh7RSzw2YEsWmrAhZupj0l5dS0nGsNRnjI5q6XjAix50h8IW/hjbstCKrMxrIDmSyOjGuJXWLStQhV70hJSuiIWd2JqFFmzu06xMsbSD4/ERfVRPZ0pc6QYWwJpANeI88aKng5B7sSzUor/fmNCljCGN6ildpy2sGf05AZHs+5U0Mq6ZcSYgTy6dBCfA+mArESjX7WINOaEea3foKe2Q1K8dNEypb4fV7aK9LIo/ZSq2BJsJUN8JjqDQ4SaXroMdCDnZwsbgGuKmnnkvR9zMwUfuUi226EhT9M/aWOovxlhGUmX1ZyFFDoWVbmkoYSMalwxT0uJxPS4NHpIyCV0yjYyWSRppydI1cyghdVi6Lpl6JhQfs0KFzVB+s+ugZaQ7GTrZPOS1M0B/w3ZjD91a0Tb6Az6sOg0L3eO6nMBQ3G0jK5m6lkpao9KYaWT0ITs6K0BK29kPsTknNCDdmzDGU3HJ1IdN3UpIe42+haTXzsBKbgOOGyFvngS6htVnoQar+4y0pQ+ZTpu0lvmzgEh+OWmYQ0lrVHQH25e7odTHqpziPOR6LLhj2ZtCO9kmXJsTRGzaqVlLODhFCeTdkxAcWvoO0z1sF26lv8C2wLoVQ6GYExpxze8tvTJEEaDgWViJA/RfwP4JOEEzq2dbnxPWYktptrJQqLCfYGuALV8V1gb86MsSuzggL5yC4gEFP+ArGfQA2KeAR4H+F1auqzQi9rM9KxQQCEirtrEY7v9TsTzRs5wXPaPGhK7QPxUeGqeBYl1O8KOv3yZ8XqWo3/Rh1TwpUJ0skt4b8KB7hnfRAmPsy1tjlskInQX2DqBF/7Zyw7Y0lEFpV1qJ7SpHUd6YWmhM/a6N5elW2dgUsL9jmCqrX7LyusL014WHx62rooRgvMhzup/9AffQXY6AeqjnBrcooM4wqA/W2uI86LIJj25Fbq8UMafK01AIbvt1CORWLJiskJg/sn1PNtOi3KqB5TCkTvyMOa6rbUsefolD+wpMKHFreWRC0YUhpDaUTum8VY2oDeWn5EE3QkTdUhwLVKZdDipCxQBTrIK5BCy5S7HUI9xSs4B+BvT+E+d9N9uMvrvCIlWxk25C3xUoGsRgE+Gpb6ZoYvmLhFG27VF6/oh2ov+ugAVnMR9BoL4bQJAnd/4dE4E5OCmrzEj11lJADNCrHL3MOdlXa/URrSgrdRvb8pg6vix2jhqUYpc3lGHnmArY/Y799ltIWwmYztsLYEIBzPeLYIZXA7N3+T26MbiB8LRqusBG1niFo4SjVae9BYut6R9zN+EBp/7D7XJWQ3QGeOTQFfiaq7INrqnhaMuJ4/Z6q+cHw86a7VHnOJGXeoLXONf3sjLRwtNTXRsvPrU8P3d+B85Gty8Yogfsb6zj4PxxzfUE3eRac2/Jp5gMmyEKOyEG+yEBYzAJk9w3AwDqrQOG); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsFNcZ3n92dvb4X68vB1/GB4OnWwz2tuvOzHYr6gJebNpyqdWtUQuVqpaxd+xdut5xZ9aWeancil4SIZCClAikQMRFQg4JCBQJWSEPRJEIT0SJHIREYm3yEEVEIX5AyUqJopn1ei/4EhRQzsNq9j///JfvnO/7NdhKoA5EkKADDkACxmAK4P8ALwFcAKDVzi5n724GNttM+DqOTaJA5gbFrA958vExQJ6c+LQOveTN8yC+I6CXfPUyiB/VoJfcOA/ivRoUyJ1B8bQXefLli4Be8sWrYL/tJZcvgvhhDfLkjfN2mK+ft39fu12HPDl83PY8ehzE+zXoQp5cvV0X6Kq7meyY/7v8cDA2exSeBe5w8jngHg6eBOGsdlG7u30avEeS0xfgaHIODid7iVM+RGGGa5MjshKRZVkJReRwKBxRw2FZVmRZCctKOKLc5Pgsd68RN+HaLIjYtH0ok5zQMrqkWVZyJK3HJW3c1AIEBeRDqmyhhA3TUI+1OaEaMTaeSkmmlh7RSzw2YEsWmrAhZupj0l5dS0nGsNRnjI5q6XjAix50h8IW/hTbstCKrMxrIDmSyOjGuJXWLStQhV70hJSuiIWd2JqFFmzu06xMsbSD4/ERfVRPZ0pc6QYWwJpANeI88aKng5B7sSzUor/fmNCljCGN6ildpy2sGf05AZHs+400Mq6ZcSYgTy6dAifA+mArESjX7WINOaEea3foKe2Q1K8dNEypb4fV7aK9LIo/Zyq2BJsJUN9JjqDQ4SaXroMdCDnZwsbgGuKmnnkvR9zMwUfuUi226EhT9K/aWOpvxlhGUmX1FyFFDoWVbmkoYSMalwxT0uJxPS4NHpIyCV0yjYyWSRppydI1cyghdVi6Lpl6JhQfs0KFzVB+s+ugZaQ7GTrZPOT1s0B/x3ZjD91a0Tb6Az6sOgML3eO6nMBQ3G0jK5m6lkpao9KYaWT0ITs6K0BK29mPsTknNCDdmzDGU3HJ1IdN3UpIe42+haTXzsJKbgOOGyFvnQK6htVnoQar+4y0pQ+ZTpu0lvmzgEh+PWmYQ0lrVHQH25e7odTHqpziPOR6LLhj2ZtCO9kmXJsTRGzaqVlLODhFCeS9UxAcWvoO0z1sF26lv8K2wLoVQ6GYExpxzR8tvTJEEaDgOViJA/Q/wP4NOEEzq2dbnxPWYktptrJQqLCfYWuALV8V1gb86MsSuzggL5yG4gEFP+ArGfQA2GeAR4A+AyvXVRoR+9meFQoIBKRV21gMd2wqlid6lvOiZ9SY0BX6l8JD4zRQrMsJfvT124TPqxT1mz6smicFqpNF0nsDHnTP8C5aYIx9eWvMMhmhs8DeBbToP1Zu2JaGMijtSiuxXeUoyhtTC42p37exPN0qG5sC9k8MU2X1S1ZeV5j+tvDwuHVVlBCMF3lO97M/4R66yxFQD/Xc4BYF1BkG9cFaW5wHXTbh0a3I7ZUi5lR5BgrBbb8OgdyKBZMVEvNntu/JZlqUWzWwHIbUiZ8xx3W1bcnDL3FoX4EJJW4tj0woujCE1IbSKZ23qhG1ofyUPOhGiKhbimOByrTLQUWoGGCKVTCXgCV3KZb6X26pWUA/B3r/ifO+m21G311hkarYSTeh7woUDWKwifDUN1M0sfxFwijb9ig9f0I70X9XwIKzmI8gUN8NIMiTO/+LicAcnJRVZqR6aykgBuhVjl7mnOyrtfqIVpSVuo1teUwdXxY7Rw1KscsbyrBzTAXs/sB+/x2krQRM5+0FMKEA5vtFMMOrgdm7/B7dGNxAeFo1XWAja7zCUcLRqjPegsXW9E+4m/CAU//ldjmrIToDPHLoCnzDVdkG19RwtOXkCXu93fOjYWfN9qhznMhLPcFrnOsHWZlo4empro2vPLU8v3R+B85Fty8Yogfsb6wT4PxxzfUE3eRac2/Jp5gMmyEKOyEG+yEBYzAJk9y3AwBp7QNn).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (9/14/28, 670 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/05013-053020004-1523330100130033-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

