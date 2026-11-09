# Paladin leveling keybinds (hand-written)

[Paladin](../README.md) > [Leveling (solo)](README.md) > Keybinds

A personal layout, written 2026-11-06 on the player's own two action bars, for a player of League of Legends and Deadlock with a mouse
that has two side buttons (WoW shows them as Button 4 and Button 5). It uses the same scheme as the
[mage layout](../../mage/leveling/keybinds.md), so both characters feel alike: Q is the strike you press most, E the control,
R the payoff after it, F the escape, the two thumb buttons the reactions, 1-4 the rest, and the Shift bar a stronger or wider version of
the key under it. Keys are for spells you press in a fight and for the things that help you there: the blessing, the aura, food, drink,
the mount and the Hearthstone have no key and are clicked between fights. It is built on the
[Retribution leveling page](retribution.md). The other paladin specs use the same keys; their level-by-level guides list the few slots that differ (Swift Judgement, Holy Shield, Templar's Bulwark, Holy Shock, Divine Favor).

**Which spell is on each key at your level:** the "Keybinds by level" tables of the
[Retribution level-by-level guide](retribution-by-level.md). This page is the layout at 60, the setup and the macros.

This file is hand-written: the regeneration that rewrites the rest of this folder leaves it alone. Edit it by hand.

## Set up first (Esc, Key Bindings and Interface)

- The two action bars: bar 1 is bound to Q, E, R, F, Mouse 5, Mouse 4, 1, 2, 3, 4, C and the middle mouse button; bar 2 to the same keys
  with Shift, with Shift+X in the last slot (not Shift+middle mouse). The tables below list the slots in that order.
- Movement: Strafe Left on A and Strafe Right on D, turning with the right mouse button held, as in Deadlock. That frees Q and E, which
  WoW uses for strafing by default.
- Interface, Combat: Auto Self Cast on, Self Cast Key Alt. With a mob targeted, your heals then land on you without changing target,
  which is what the thumb heal needs.
- A side bar without keybinds (Interface, Action Bars: the right bars) for the things you click: Blessing of Might, Devotion Aura, food,
  water, bandages, the mount, the Hearthstone.

## Bar 1: the fight

| Key | Spell (learned at) | Press it when | Habit it matches |
|---|---|---|---|
| Q | Holy Strike macro (6) | Whenever it is ready, every 10 seconds. It starts your swings too | League Q, the basic hit |
| E | Hammer of Justice (8) | A mob starts casting; from 20, right before Judgement when both are ready and the mob has more than 30% health left (it has a 1-minute cooldown, so that is about one pull in three); to buy time to heal | League E, the CC key |
| R | Seal and Judgement macro (4); plain Seal of Righteousness at 1-3 | The first press on a new mob, before the pull, casts the seal. Then whenever Judgement is ready; from 20, right after E, because Seal of Command's judgement hits a stunned mob twice as hard | League R, the payoff after the CC |
| F | Divine Protection (6), Divine Shield from 34 | The fight goes wrong: bubble, then heal inside it | Flash |
| Mouse 5 (front side button) | Holy Light (1) | Below a third of your health, inside the bubble or during a stun; between fights, back to about 80% | Thumb reaction |
| Mouse 4 (back side button) | Flash of Light (20) | Below a quarter of your health; a cheap top-up between fights | Thumb reaction, the quick heal next to the big one |
| 1 | Blessing of Protection (10) | F is on cooldown and a mob is killing you: safe from physical attacks for 6 seconds at 10, 8 at 24 and 10 from 38. It shares Forbearance with F, so it cannot follow the bubble within a minute. You cannot attack while it is on you, and it replaces your Blessing of Might: click that back on after | Deadlock ability 1 |
| 2 | Exorcism (20) | On cooldown, against Undead and Demons only | Deadlock ability 2 |
| 3 | Free | | |
| 4 | Purify (8), Cleanse from 42 | A poison or a disease is on you | Deadlock ability 4 |
| C | Healing potion macro (1), from the [macro page](../macros.md) | A bad pull: below a quarter of your health with F on cooldown, or when a heal would not land in time. Every potion shares one cooldown | An item key |
| Middle mouse | Free | | |

The whole fight is two keys: R once before the pull for the seal, then Q and R on cooldown, with E before R from level 20 whenever the stun is ready.

## Bar 2: the same keys with Shift

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Shift+Q | Consecration (20) | Packs only. The single-target rotation never casts it |
| Shift+E | Repentance (49, talent) | A humanoid: it stands incapacitated for up to 6 seconds, from 20 yards, until damage wakes it. A second setup for the doubled Judgement, or a breather. The fight lab does not model it |
| Shift+R | Hammer of Wrath (44) | A mob below 20% health that runs. Optional: the tuned rotation leaves it out |
| Shift+F | Blessing of Freedom (18) | You are rooted or slowed |
| Shift+Mouse 5 | Lay on Hands (10) | Below 15% of your health: a full heal every 20 minutes. It drains your mana, and its tooltip has no Forbearance, so it works right after the bubble |
| Shift+Mouse 4 | Turn Undead (24) | An extra Undead mob joins: send it running |
| Shift+1 | Free | |
| Shift+2 | Holy Wrath (50) | Several Undead or Demons at once |
| Shift+3 | Free | |
| Shift+4 | Free | |
| Shift+C | Free | |
| Shift+X | Free | |

Free slots stay free until something earns them. The fight lab's fights are Q, R and E, with heals and saves only for a bad pull, so the paladin
has more keys than spells worth one. Seal of Justice is the first candidate, for mobs that run.

## No key: click these between fights

Blessing of Might, Devotion Aura, food, water, bandages, your mount (40 in Classic) and the Hearthstone. Tab (target nearest enemy) and
Space (jump) stay on WoW's defaults. Seal of the Crusader, Seal of Fury and Righteous Fury are not part of leveling as Retribution.

## Macros (Esc, Macros, New; pick the question-mark icon so the button shows the spell)

The Holy Strike macro, on Q from level 6. It starts your swings as well, so no key needs the plain Attack button. The start line runs
first, so a press still starts your swings while Holy Strike is on its 10-second cooldown. At levels 1-5, right-click the mob to start
swinging.

```
#showtooltip Holy Strike
/startattack [harm,nodead]
/cast Holy Strike
```

The seal and Judgement macro, on R from level 4, so the seal needs no key of its own. The first press on a new target casts the seal, and
each press after that casts Judgement when it is ready. After three Judgements it casts the seal again, about when the 30 seconds run
out. One seal per mob is enough, because Judgement does not use up the seal in Forever.

```
#showtooltip Judgement
/castsequence reset=target Seal of Righteousness, Judgement, Judgement, Judgement
```

At level 20, when the build takes Seal of Command, change the macro's seal to Seal of Command. From 20, press R once before you stun: the
first press on a mob is always the seal. Levels 1-3 put plain Seal of Righteousness on R, because Judgement comes at 4.

`/startattack` and `/castsequence` are commands of the Classic client, and Forever macro guides use `/startattack`
([RankedBoost](https://rankedboost.com/world-of-warcraft/forever/macros/paladin/retribution/),
[Kami Labs](https://kami-labs.fr/en/wow-forever/macros-wow-forever-9-classes/)). Neither macro is tested in Forever's client here. If the
Holy Strike one fails, put plain Holy Strike back on Q and right-click the mob to start swinging. If the seal one fails, put plain
Judgement back on R and the seal on 1.

The stun combo needs no macro: E, then R. A second macro that casts Judgement would not move R's sequence on, so its reseal would come late.

Optional: the whole rotation on one key. Judgement is off the global cooldown in the simulator's data, so one press can cast both attacks, in
the fight lab's order. Put this on Q from level 6, in place of the Holy Strike macro, and R comes free. The stun combo is then E, then Q.
At level 20, change the seal to Seal of Command.

```
#showtooltip Holy Strike
/startattack [harm,nodead]
/castsequence reset=target Seal of Righteousness, Judgement, Judgement, Judgement
/cast Holy Strike
```
