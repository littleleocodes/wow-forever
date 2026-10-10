# Destruction Warlock — Leveling (solo)

[Warlock](../README.md) > [Leveling (solo)](README.md) > Destruction

**[Destruction — Leveling](../research/leveling/builds/destruction-leveling.md)** (21/0/30) — [open the talent tree](https://talentsforever.com/warlock/60/00550020134001--20550550331001-6)

> 🔬 Derived build: searched in the fight lab (this project's leveling simulator) from the spec's builds and the stats model's best one. A model of the beta, to check at launch.

## How to play

**Not in this build:** **Incinerate**, **Shadowburn** are talents this build does not take: skip the lines that use them. The fight lab played the build without them.

**Before the fight:** **Demon Skin** (**Demon Armor** from level 20) up, **Summon Voidwalker**. Send the Voidwalker in first and let it hold the mob with **Torment**. Open with **Amplify Curse** whenever it is ready: it makes that fight's **Bane of Agony** 50% stronger.

**In the fight**, top to bottom:

1. **Corruption** and **Bane of Agony** first while the Voidwalker builds threat, none of them on a mob below about a third of its health.
2. **Immolate** while you have more than half your mana and it will not pull the mob off the Voidwalker.
3. **Conflagrate** when **Immolate** has about 3 seconds left (at once with 5 points in **Shadow and Flame**, which keeps **Immolate** burning), or to finish a burning mob it would kill; then **Siphon Life**.
4. Above 80% mana, **Shadow Bolt** (**Searing Pain** when the mob has too little health left for it); below that, your wand.
5. With **Incinerate**: cast it instead of **Shadow Bolt** on a burning mob. With **Shadowburn**: finish any mob it would kill.
6. **Life Tap** in a fight only when you are short of mana and above 60% health.
7. If a mob reaches you: **Death Coil** below 60% health and let **Torment** take it back (no **Fear** and no **Drain Life**: both measured slower). Your Healthstone below 35% health.

**Between fights:** **Life Tap** back to 70% mana while your health stays above 60%, heal the Voidwalker with **Consume Shadows** (or **Health Funnel**) when it is below 60%, and eat only below 40% health.

## Why this rotation

Destruction levels with the same Voidwalker and Affliction dots as the other specs, since its first 21 points are Affliction, and adds a hard-hitting **Immolate** and, from level 59, **Conflagrate**. This build takes neither **Incinerate** nor **Shadowburn**, so your filler is **Shadow Bolt** when your mana is nearly full and the wand otherwise.

**Why it works**

- **Corruption** and **Bane of Agony** go first: both are instant (with 5 points in **Improved Corruption**) and cheap, and they give the Voidwalker time to build threat before your fire spells land. **Amplify Curse** before the pull makes that **Bane of Agony** 50% stronger, and **Siphon Life** joins at level 30. Skip **Corruption** on a mob below about a third of its health.
- **Immolate** only while you have more than half your mana: the fight lab measured that about 2.5% faster per kill than casting it every time. **Aftermath** makes its first hit 50% stronger, and the fight lab holds it back while it would pull the mob off the Voidwalker.
- **Conflagrate** (level 59 in this order) eats your **Immolate** in this build, so cast it when **Immolate** has about 3 seconds left, or to finish a burning mob it would kill. **Fire and Brimstone** (level 60) adds to its crit chance and **Ruin** doubles its crit bonus.
- Your filler is **Shadow Bolt** above about 80% mana and the wand below it. When a mob has too little health left for a **Shadow Bolt**, the fight lab casts **Searing Pain** instead, also only with nearly full mana.
- **Life Tap** when your mana runs short and your health is above 60%; between fights, **Life Tap** back up and heal the Voidwalker with **Health Funnel**. Eat only below 40% health: the fight lab measured that a little faster than eating at 55%, its default.

**Caveats**

- This build has neither **Incinerate** nor **Shadowburn**: where the steps name **Incinerate**, cast **Shadow Bolt** (the fight lab does), and finish mobs with **Conflagrate** or the wand. The talent search traded **Shadowburn** for a point of **Fire and Brimstone** and measured about 1% faster kills.
- Until level 59 you have no **Conflagrate**: you play **Corruption**, **Bane of Agony**, **Siphon Life**, **Immolate**, then **Shadow Bolt** or the wand.
- When a mob reaches you, cast **Death Coil** if you are hurt and let the Voidwalker take it back with **Torment**: the fight lab measured never casting **Fear** or **Drain Life** about 1% faster each. **Molten Skin** (10% less damage taken) and **Intensity** (casts that resist pushback) make those moments cheaper.

**When to change it**

- If you take **Incinerate** later, the fight lab's rotation casts it in place of **Shadow Bolt** on a burning mob: it deals 25% more damage while **Immolate** is on the target.
- Finish a nearly dead mob with the wand or **Conflagrate** instead of a new **Immolate**: the fight lab starts no **Immolate** on a mob below about a third of its health.

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10-14 | Improved Corruption (Affliction) | 5 |
| 15-19 | Malediction (Affliction) | 5 |
| 20 | Amplify Curse (Affliction) | 1 |
| 21-22 | Improved Bane of Agony (Affliction) | 2 |
| 23-25 | Pandemic (Affliction) | 3 |
| 26-29 | Malevolence (Affliction) | 4 |
| 30 | Siphon Life (Affliction) | 1 |
| 31-35 | Bane (Destruction) | 5 |
| 36-40 | Molten Skin (Destruction) | 5 |
| 41-45 | Aftermath (Destruction) | 5 |
| 46-48 | Agonizing Flames (Destruction) | 3 |
| 49-53 | Ruin (Destruction) | 5 |
| 54-55 | Destructive Reach (Destruction) | 2 |
| 56-58 | Intensity (Destruction) | 3 |
| 59 | Conflagrate (Destruction) | 1 |
| 60 | Fire and Brimstone (Destruction) | 1 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 26 |
| 30 | 32 |
| 40 | 39 |
| 50 | 42 |
| 60 | 43 |

---
*Generated by `_reference/data/render_modes.py` on 2026-10-10 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

