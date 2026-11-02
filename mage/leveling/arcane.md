# Arcane Mage — Leveling (solo)

[Mage](../README.md) > [Leveling (solo)](README.md) > Arcane

**[Arcane — Leveling](../research/leveling/builds/arcane-leveling.md)** (29/0/22) — [open the talent tree](https://talentsforever.com/mage/60/21221500301030153--0525300001013002-7)

> 🔬 Derived build: searched in the fight lab (this project's leveling simulator) from the spec's builds and the stats model's best one. A model of the beta, to check at launch.

> **Signature spells: this build fails the check** in the fight lab (lacks Arcane Blast; core share 0% < 50%). Arcane is defined by **Arcane Blast** cast in every fight and Arcane Blast, Arcane Missiles, Arcane Wrath carrying 50% of the damage at level 60. No leveling build of this spec passes yet; it stays on the page until one does (the leveling searches since 2026-10-22 look only for such builds).

## How to play

**Not in this build:** **Cold Snap**, **Ice Barrier** are talents this build does not take: skip the lines that use them. The fight lab played the build without them.

**Before the fight:** **Frost Armor** (**Ice Armor** from level 30) and **Arcane Intellect** up; **Ice Barrier** before each pull once you have it. Pull from as far away as you can.

**In the fight**, top to bottom:

1. **Frostbolt** while the mob walks in (it slows it) and whenever nothing below applies, but only while the mob has more than a fifth of its health; if the mob would reach you before the cast ends, **Fire Blast** it instead (or wand it until it arrives if **Fire Blast** is on cooldown and **Frost Nova** is ready).
2. **Frost Nova** when it reaches you, then step back out of melee; **Cold Snap** resets **Frost Nova** if it has more than 8 seconds of cooldown left and the mob still has 40% of its health; with both down, **Fire Blast**.
3. **Ice Lance** again and again while the mob is frozen (**Frost Nova**, **Frostbite** or **Fingers of Frost**).
4. Below a fifth of the mob's health: **Fire Blast** (not below a tenth), an **Ice Lance** that will kill, or your wand. No Cone of Cold at all.
5. **Counterspell** a mob that casts spells.

**Between fights:** Drink your conjured water below a third of your mana, **Evocation** when it is ready and you are under 40% mana, eat below two thirds of your health.

## Why this rotation

Arcane levels on its own spells: **Arcane Wrath** to open, two **Arcane Blast** stacks while the mob walks in, then **Arcane Missiles**, which you keep channeling when the mob reaches you; the tuned rules (2026-10-22) never cast **Frost Nova**. In the fight lab at level 60, **Arcane Missiles** is about 71% of this build's damage, **Arcane Blast** 16%, **Fire Blast** 7% and **Arcane Wrath** 5%.

**Why it works**

- **Presence of Mind** (level 30) at the pull makes your first cast instant (in the fight lab the opening **Arcane Wrath**); **Arcane Power** (level 40) at the pull too while you have more than half your mana: 30% more damage and 30% more mana cost for 15 seconds.
- **Arcane Wrath** (level 25) opens when its 3.5-second cast lands before the mob arrives, then goes out whenever it is ready (6-second cooldown) and the cast fits. It gains spell damage equal to 5% of your maximum mana.
- **Arcane Blast** (level 20) twice while the mob walks in: each cast gives all your spells spell damage (15% of your Intellect) for 15 seconds and makes the next **Arcane Blast** 175% more expensive, so the fight lab stops at two, and starts one only while it costs at most a quarter of your mana and will finish before the mob reaches you. Without it a kill at level 60 takes about 4.1 seconds longer in the fight lab.
- **Arcane Missiles** is the main spell, at range and in melee: **Improved Channeling** at 5/5 (done at level 31) gives a 100% chance that hits do not interrupt the channel. **Missile Barrage** (levels 10-11; 40% from **Arcane Blast**, 20% from **Arcane Wrath**) makes the next one free and twice as fast: cast it at once after your two stacks, or when the mob is on you. Without **Missile Barrage** a kill at level 60 takes about 4.3 seconds longer, without **Improved Channeling** 2.9.
- No **Frost Nova**: the tuned rules measured kills about 2% faster without it. Our reading: with hits unable to stop the Missiles, the global cooldown and the step back cost more than the hits do.
- When the mob is on you and below a fifth of its health, **Cone of Cold** and a step back (a tuned rule, about 1.5% faster); **Fire Blast** finishes a mob it will kill. The Fire half (levels 44-60) is mostly for **Fire Blast**: **Improved Fire Blast** takes 2 seconds off its cooldown, **Incineration** adds 6% crit chance, **Impact** gives your Fire spells a 10% chance to stun for 2 seconds. **Improved Fireball** and **Pyroblast** only open the rows to **Master of Elements**: the list casts neither **Fireball** nor **Pyroblast**.

**Caveats**

- This build has no **Ice Lance**: skip that line of the list.
- Mana: **Arcane Missiles** costs 655 at top rank, every **Arcane Blast** stack makes the next one dearer and **Arcane Power** adds 30%. **Frostbolt** (290 at top rank) is for when you cannot afford the Missiles. Drink below a third of your mana and use **Evocation** between fights when it is ready and you are under 40% mana.
- The tuned rules eat below 40% of your health, not two thirds: the fight lab measured kills slightly faster that way, with no deaths in its tuning runs.
- The fight lab measured only single pulls for this list: with several mobs on you, **Frost Nova** and **Arcane Explosion** (everything within 10 yards) are back in play.

**When to change it**

- If the mob would reach you before an **Arcane Blast** or **Arcane Wrath** finishes, do not start it: channel **Arcane Missiles** instead (an instant cast with **Presence of Mind** is the exception).
- A mob that hits harder than a normal same-level mob is still worth a **Frost Nova**: the rule only says it costs time against the mobs the fight lab models.
- Against a caster mob, **Counterspell** it when it starts a cast, as every mage list in the fight lab does.

## Other builds of this spec

- [Arcane — Leveling](../research/leveling/builds/arcane-open-leveling.md) (31/17/3) — [open the talent tree](https://talentsforever.com/mage/60/050105203100311531-3402300120002-012-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707). Simulations, not in-game measurements. Do not hand-edit.*

