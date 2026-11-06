# Paladin leveling keybinds (hand-written)

[Paladin](../../README.md) > [Leveling research](README.md) > Keybinds

A personal layout, written 2026-11-06 on the player's own two action bars, for a player of League of Legends and Deadlock with a mouse
that has two side buttons (WoW shows them as Button 4 and Button 5). It uses the same scheme as the
[mage layout](../../../mage/research/leveling/keybinds.md), so both characters feel alike: Q is the strike you press most, E the control,
R the payoff after it, F the escape, the two thumb buttons the reactions, 1-4 the rest, and the Shift bar a stronger or wider version of
the key under it. It is built on the [Retribution leveling page](../../leveling/retribution.md).

**Which spell is on each key at your level:** the "Keybinds by level" tables of the
[Retribution level-by-level guide](../../leveling/retribution-by-level.md). This page is the layout at 60, the setup and the macro.

This file is hand-written and nothing generates or deletes it (`paladin/leveling/` is regenerated, so it lives here). Edit it by hand.

## Set up first (Esc, Key Bindings and Interface)

- The two action bars: bar 1 is bound to Q, E, R, F, Mouse 5, Mouse 4, 1, 2, 3, 4, C and the middle mouse button; bar 2 to the same keys
  with Shift, with Shift+X in the last slot (not Shift+middle mouse). The tables below list the slots in that order.
- Movement: Strafe Left on A and Strafe Right on D, turning with the right mouse button held, as in Deadlock. That frees Q and E, which
  WoW uses for strafing by default.
- Interface, Combat: Auto Self Cast on, Self Cast Key Alt. With a mob targeted, your heals then land on you without changing target,
  which is what the thumb heal needs.

## Bar 1: the fight

| Key | Spell (learned at) | Press it when | Habit it matches |
|---|---|---|---|
| Q | Holy Strike (6) | Whenever it is ready, every 10 seconds | League Q, the basic hit |
| E | Hammer of Justice (8) | A mob starts casting; from 20, right before Judgement when both are ready and the mob has more than 30% health; to buy time to heal | League E, the CC key |
| R | Judgement (4) | Whenever it is ready; from 20, right after E, because Seal of Command's judgement hits a stunned mob twice as hard | League R, the payoff after the CC |
| F | Divine Protection (6), Divine Shield from 34 | The fight goes wrong: bubble, then heal inside it | Flash |
| Mouse 5 (front side button) | Holy Light (1) | Below a third of your health, inside the bubble or during a stun; between fights, back to about 80% | Thumb reaction |
| Mouse 4 (back side button) | Lay on Hands (10) | Below 15% of your health | Thumb reaction, the panic button |
| 1 | Seal of Righteousness (1), Seal of Command from 20 (talent) | Before every pull, and again when it runs out after 30 seconds | Deadlock ability 1 |
| 2 | Exorcism (20) | On cooldown, against Undead and Demons only | Deadlock ability 2 |
| 3 | Flash of Light (20) | Below a quarter of your health; a cheap top-up between fights | Deadlock ability 3 |
| 4 | Purify (8), Cleanse from 42 | A poison or a disease is on you | Deadlock ability 4 |
| C | Your water | Below about 15% of your mana | A consumable key next to the movement hand |
| Middle mouse | Attack | To start swinging at levels 1-5, and whenever your swings stop. A right-click on the mob does the same | The weapon attack, like the mage's wand |

The whole fight is three keys: 1 before the pull, then Q and R on cooldown, with E before R from level 20.

## Bar 2: the same keys with Shift

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Shift+Q | Consecration (20) | Packs only. The single-target rotation never casts it |
| Shift+E | The stun combo macro (below), from 20 | Hammer of Justice is ready: press twice |
| Shift+R | Hammer of Wrath (44) | A mob below 20% health that runs. Optional: the tuned rotation leaves it out |
| Shift+F | Blessing of Freedom (18) | You are rooted or slowed |
| Shift+Mouse 5 | Blessing of Protection (10) | A second save against physical damage. You cannot attack while it is on you |
| Shift+Mouse 4 | Turn Undead (24) | An extra Undead mob joins: send it running |
| Shift+1 | Blessing of Might (4) | When it runs out |
| Shift+2 | Holy Wrath (50) | Several Undead or Demons at once |
| Shift+3 | Your bandage | If you train First Aid; otherwise free |
| Shift+4 | Your mount (40 in Classic) | Travel |
| Shift+C | Your food | Between fights, if you are out of mana for heals |
| Shift+X | Hearthstone | The recall key |

## No key needed

Tab (target nearest enemy) and Space (jump) stay on WoW's defaults. Devotion Aura is a click once per login. Seal of the Crusader, Seal
of Fury and Righteous Fury are not part of leveling as Retribution.

## Macro (Esc, Macros, New; pick the question-mark icon so the button shows the spell)

The stun combo on one key, on Shift+E. Press it twice: the first press stuns, the second judges.

```
#showtooltip
/castsequence reset=10 Hammer of Justice, Judgement
```

It only moves on when Hammer of Justice goes off, so use it when the stun is ready and keep plain Judgement on R for the fifty seconds
in between. `/castsequence` is a command of the Classic client; if Forever lacks it, press E then R.

Drag your water and food from the bag onto the C and Shift+C slots. Replace them when you buy a better kind.
