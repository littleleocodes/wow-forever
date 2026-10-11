# Affliction Warlock — Leveling (solo)

[Warlock](../README.md) > [Leveling (solo)](README.md) > Affliction

**[Affliction — Leveling](../research/leveling/builds/affliction-leveling.md)** (35/6/10) — [open the talent tree](https://talentsforever.com/warlock/60/0555002013500135-00050001-0055-6)

> 🔬 Derived build: searched in the fight lab (this project's leveling simulator) from the spec's builds and the stats model's best one. A model of the beta, to check at launch.

## How to play

**Not in this build:** **Soul Link** is a talent this build does not take: skip the lines that use it. The fight lab played the build without it.

**Before the fight:** **Demon Skin** (**Demon Armor** from level 20) up, **Summon Voidwalker**. Send the Voidwalker in first and let it hold the mob with **Torment**. Open with **Amplify Curse** whenever it is ready: it makes that fight's **Bane of Agony** 50% stronger. With **Soul Link**: turn it on once the Voidwalker is out.

**In the fight**, top to bottom:

1. **Corruption**, **Bane of Agony** and **Siphon Life** on the mob, none of them on a mob below about a third of its health.
2. **Immolate** only on a mob above half its health and while you have more than half your mana.
3. Then your wand, not **Shadow Bolt**: the dots do the killing and the wand costs no mana.
4. **Drain Life** whenever you drop below 60% health, and in place of the wand while you are below 85%.
5. **Life Tap** in a fight only when you are short of mana and above 60% health.
6. If a mob reaches you: **Death Coil** below 60% health, then **Drain Life** while it runs; otherwise let **Torment** take it back. Your Healthstone below 35% health.

**Between fights:** **Life Tap** back to 70% mana while your health stays above 60%, heal the Voidwalker with **Consume Shadows** (or **Health Funnel**) when it is below 60%, and eat only below 55% health.

## Why this rotation

Affliction levels by letting its damage-over-time spells do the killing while the Voidwalker holds the mob: you put **Corruption**, **Bane of Agony** and **Siphon Life** on it, add **Immolate** when mana allows, and shoot your wand while they tick.

**Why it works**

- Send the Voidwalker in first: its **Torment** holds the mob while you stand at range, and your dots build threat slowly enough that it keeps the mob. Open with **Amplify Curse** whenever it is ready (3-minute cooldown): it makes that fight's **Bane of Agony** 50% stronger.
- **Corruption** and **Bane of Agony** do about half your damage at 60, and **Siphon Life** (from level 30) another tenth while it heals you. Skip **Corruption** on a mob below about a third of its health: it dies before the spell pays for its mana (the fight lab measured that about 1% faster).
- **Immolate** comes last, only on a mob above about half its health and while you have more than half your mana: it costs the most mana of your dots and brings about 5% of your damage at 60.
- Your wand is the filler, not **Shadow Bolt**: the fight lab measured kills about 7% faster with no **Shadow Bolt** at all. The wand costs no mana, so you spend less time getting mana back while the dots do the killing.
- **Drain Life** is for when you are hurt, not for damage: the fight lab casts it below 60% health, and in place of the wand below 85%. Between fights, **Life Tap** back to about 70% mana while your health stays above 60%, and eat only when a fight leaves you below about 55%: **Siphon Life** and **Drain Life** win the rest back in the next fight.

**Caveats**

- This build has no **Wrack**, and the fight lab measured kills about 6.5% faster when a build that has it never casts it: its 6-second channel holds you in place for little damage.
- When a mob reaches you, cast **Death Coil** if you are below about 60% health (it heals you for its damage); otherwise let the Voidwalker's **Torment** take it back. The fight lab measured never casting **Fear** about 1.5% faster.
- **Curse of the Elements** does not pay while leveling: the fight lab measured kills up to 3% slower at levels 50-60 with it, because the mob dies before the curse repays its global cooldown and mana.
- Pulls of several mobs with **Rain of Fire** were slower than single pulls at level 40 in the fight lab and only about 10% faster at 60, with about one death per ten kills: pull one mob at a time.

**When to change it**

- Finish a nearly dead mob with the wand; start no new spell on it.
- Below about a third of your health with a mob on you, use a Healthstone (**Create Healthstone** between fights).
- If the Voidwalker dies, summon a new one before the next pull rather than fight without your tank, and heal a hurt one between fights with **Consume Shadows** (not usable in combat) or **Health Funnel**.

*This guide was written for the rotation of 2026-10-09; the list above was re-tuned since, so follow the list where the two differ.*

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10-14 | Improved Corruption (Affliction) | 5 |
| 15-19 | Malediction (Affliction) | 5 |
| 20 | Amplify Curse (Affliction) | 1 |
| 21-22 | Improved Bane of Agony (Affliction) | 2 |
| 23-25 | Pandemic (Affliction) | 3 |
| 26-29 | Suppression (Affliction) | 4 |
| 30 | Siphon Life (Affliction) | 1 |
| 31 | Suppression (Affliction) | 1 |
| 32-34 | Malevolence (Affliction) | 3 |
| 35-39 | Shadow Mastery (Affliction) | 5 |
| 40-41 | Malevolence (Affliction) | 2 |
| 42-46 | Unholy Power (Demonology) | 5 |
| 47-49 | Soul Siphon (Affliction) | 3 |
| 50-54 | Bane (Destruction) | 5 |
| 55-59 | Molten Skin (Destruction) | 5 |
| 60 | Demonic Energies (Demonology) | 1 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 26 |
| 30 | 32 |
| 40 | 39 |
| 50 | 41 |
| 60 | 41 |

---
*Generated by `_reference/data/render_modes.py` on 2026-10-11 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

