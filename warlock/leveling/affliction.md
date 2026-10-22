# Affliction Warlock — Leveling (solo)

[Warlock](../README.md) > [Leveling (solo)](README.md) > Affliction

**[Affliction — Leveling](../research/leveling/builds/affliction-leveling.md)** (33/6/12) — [open the talent tree](https://talentsforever.com/warlock/60/0550032013500135-00050001-0055002-7)

> 🔬 Derived build: searched in the fight lab (this project's leveling simulator) from the spec's builds and the stats model's best one. A model of the beta, to check at launch.

## How to play

**Not in this build:** **Soul Link**, **Wrack** are talents this build does not take: skip the lines that use them. The fight lab played the build without them.

**Before the fight:** **Demon Skin** (**Demon Armor** from level 20) up, **Summon Voidwalker**. Send the Voidwalker in first and let it hold the mob with **Torment**. Open with **Amplify Curse** whenever it is ready: it makes that fight's **Bane of Agony** 50% stronger. With **Soul Link**: turn it on once the Voidwalker is out.

**In the fight**, top to bottom:

1. **Corruption**, **Bane of Agony** and **Siphon Life** once each, none of them on a mob below about a third of its health; **Corruption** only while you have more than 15% mana.
2. **Immolate** only on a mob above about half its health and while you have more than half your mana.
3. With **Wrack**: channel it once **Corruption** is up.
4. **Shadow Bolt** while the mob has more than about a third of its health and you keep the mana for **Fear** and **Drain Life**; your wand otherwise while the dots finish the mob.
5. **Drain Life** whenever you drop below 60% health, and in place of the wand while you are below 85%.
6. **Life Tap** in a fight only when the next **Shadow Bolt** would eat into that mana reserve, you are above 60% health and the mob still has more health than one bolt takes.
7. If a mob reaches you: **Death Coil** below 60% health, otherwise **Fear** it, then **Drain Life** while it runs. Your Healthstone below 35% health.

**Between fights:** **Life Tap** back to 70% mana while your health stays above 60%, heal the Voidwalker with **Consume Shadows** (or **Health Funnel**) when it is below 60%, eat only below 55% health, and drink only below 15% mana (when you are too hurt to **Life Tap**).

## Why this rotation

Affliction levels by letting its damage-over-time spells do the killing while the Voidwalker holds the mob: **Corruption**, **Bane of Agony** and **Siphon Life** on a healthy mob, **Shadow Bolt** while the mob has more than about a third of its health, then the wand while the dots finish it.

**Why it works**

- Send the Voidwalker in first: its **Torment** holds the mob while you stand at range, and your dots build threat slowly enough that it keeps the mob. **Amplify Curse** (level 20) goes on whenever it is ready (3-minute cooldown): it makes that fight's **Bane of Agony** 50% stronger.
- **Corruption**, **Bane of Agony** and **Siphon Life** (level 30) go on once each, none of them on a mob below about a third of its health: it dies before the spell pays for its mana. The 2026-10-20 re-tune measured the 35% rule on **Corruption** about 2% faster per kill, and keeping **Corruption** for when you have more than 15% mana a little under 1%.
- **Shadow Bolt** fills while the mob has more than 35% of its health and you keep the mana for **Fear** and **Drain Life**; below that, your wand while the dots finish the mob. The tuned rule (no **Shadow Bolt** on a mob below 35%) measured about 6.5% faster per kill, the largest gain of the re-tune.
- **Immolate** only on a mob above about half its health and while you have more than half your mana: it costs the most of your dots, and the fight lab casts it on one mob in two at level 20 and one in five at 60.
- **Drain Life** below 60% health, and in place of the wand below 85% (**Improved Drains** and **Soul Siphon** make it stronger). **Life Tap** in a fight only when the next **Shadow Bolt** would eat into your **Fear** and **Drain Life** mana, while you stay above 60% health; between fights tap back to about 70% mana and eat only below 55% health.

**Caveats**

- No **Curse of the Elements** while leveling: the 2026-10-20 re-tune measured about 2-3% faster per kill without it (it costs a global cooldown and mana on a mob that dies quickly).
- This build has no **Wrack** and no **Nightfall**. With **Wrack**, the fight lab channels it once **Corruption** is up.
- Affliction is the one warlock list that drinks: **Shadow Bolt** spends mana faster than the other specs' wand-heavy play, and when you are too hurt to **Life Tap** you drink below 15% mana (about 6-8 seconds per kill in the fight lab).
- When a mob reaches you: **Death Coil** if you are below about 60% health (it heals you for its damage), otherwise **Fear** it and **Drain Life** while it runs, until the Voidwalker's **Torment** takes it back.

**When to change it**

- Finish a nearly dead mob with the wand; start no new spell on it.
- Below about a third of your health with a mob on you, use a Healthstone (**Create Healthstone** between fights).
- If the Voidwalker dies, summon a new one before the next pull rather than fight without your tank, and heal a hurt one between fights with **Consume Shadows** (not usable in combat) or **Health Funnel**.

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10-14 | Improved Corruption (Affliction) | 5 |
| 15-19 | Suppression (Affliction) | 5 |
| 20 | Amplify Curse (Affliction) | 1 |
| 21-22 | Improved Bane of Agony (Affliction) | 2 |
| 23-25 | Pandemic (Affliction) | 3 |
| 26-29 | Malevolence (Affliction) | 4 |
| 30 | Siphon Life (Affliction) | 1 |
| 31 | Malevolence (Affliction) | 1 |
| 32-34 | Soul Siphon (Affliction) | 3 |
| 35-39 | Shadow Mastery (Affliction) | 5 |
| 40-42 | Improved Drains (Affliction) | 3 |
| 43-47 | Unholy Power (Demonology) | 5 |
| 48-52 | Bane (Destruction) | 5 |
| 53-57 | Molten Skin (Destruction) | 5 |
| 58-59 | Ruin (Destruction) | 2 |
| 60 | Demonic Energies (Demonology) | 1 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 31 |
| 30 | 38 |
| 40 | 42 |
| 50 | 41 |
| 60 | 40 |

---
*Generated by `_reference/data/render_modes.py` on 2026-10-22 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70425). Simulations, not in-game measurements. Do not hand-edit.*

