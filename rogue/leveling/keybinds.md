# Rogue leveling keybinds (hand-written)

[Rogue](../README.md) > [Leveling (solo)](README.md) > Keybinds

A personal layout, written 2026-11-06 on the player's own two action bars, for a player of League of Legends and Deadlock with a mouse
that has two side buttons (WoW shows them as Button 4 and Button 5). Same scheme as the [mage](../../mage/leveling/keybinds.md)
and [paladin](../../paladin/leveling/keybinds.md) layouts: Q the attack you press most, E the control, R the payoff, F the
save, the two thumb buttons the reactions, 1-4 the rest, the Shift bar the rarer tools. Keys
are for spells you press in a fight and for the things that help you there; poisons, food, the mount and the Hearthstone have no key and
are clicked between fights. It is built on the [Combat leveling page](combat.md) (swords).

**Which spell is on each key at your level:** the "Keybinds by level" tables of the
[Combat level-by-level guide](combat-by-level.md). This page is the layout at 60, the setup and the macros.

This file is hand-written: the regeneration that rewrites the rest of this folder leaves it alone. Edit it by hand.

## Set up first (Esc, Key Bindings and Interface)

- The two action bars: bar 1 is bound to Q, E, R, F, Mouse 5, Mouse 4, 1, 2, 3, 4, C and the middle mouse button; bar 2 to the same keys
  with Shift, with Shift+X in the last slot. The tables below list the slots in that order.
- WoW switches bar 1 to a second page while you are in **Stealth** (the stealth bar, as in Classic). Put the same spells in the same slots
  on it, so every key does the same thing in and out of Stealth.
- Movement: Strafe Left on A and Strafe Right on D, turning with the right mouse button held, as in Deadlock.
- A side bar without keybinds for the things you click: the poisons, food, bandages, the mount, the Hearthstone.

## Bar 1: the fight

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Q | Sinister Strike macro (1) | Until you have 5 combo points. It starts your swings too |
| E | Gouge (6) | A breather: the mob stands stunned while you bandage or walk away |
| R | Eviscerate (1) | At 5 combo points, or earlier when it would kill the mob |
| F | Evasion (8) | Below half your health while the mob has more than 30% of its own |
| Mouse 5 (front side button) | Shank (24) | Whenever it is ready, unless the energy it gives would go over your maximum |
| Mouse 4 (back side button) | Riposte (21, talent) | It lights up after you parry |
| 1 | Garrote (14) | The opener, from stealth |
| 2 | Sap (10) | A second mob next to your target, from stealth, before the pull |
| 3 | Vanish (22) | The emergency exit |
| 4 | Sprint (10) | Close a gap, or open one |
| C | Cold Blood (55, talent) | Right before an Eviscerate at 5 points, whenever it is ready |
| Middle mouse | Free | |

## Bar 2: the same keys with Shift

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Shift+E | Kick (12) | The tuned rotation never interrupts; for a caster that hits too hard |
| Shift+1 | Stealth (1) | Before each pull from 14: Shift+1, then 1 for the opener |
| Shift+2 | Blind (34) | A second mob joins mid-fight |
| Shift+Q, Shift+R, Shift+F, Shift+Mouse 5, Shift+Mouse 4, Shift+3, Shift+4, Shift+C, Shift+X | Free | |

## No key: click these between fights

Instant Poison and Deadly Poison, food, bandages, your mount (40 in Classic) and the Hearthstone. Slice and Dice, Cheap Shot and Kidney
Shot are never cast by the tuned rotation, and Backstab, Ambush and Mutilate are for daggers. Tab and Space stay on WoW's defaults.

## Macros (Esc, Macros, New; pick the question-mark icon so the button shows the spell)

Your strike with the start attack line, on Q from level 1. It starts your swings as well, so no key needs the plain Attack button. The
start line runs first, so a press still starts your swings when you are short of energy.

```
#showtooltip Sinister Strike
/startattack [harm,nodead]
/cast Sinister Strike
```

`/startattack` is a command of the Classic client, and Forever macro guides use it
([RankedBoost](https://rankedboost.com/world-of-warcraft/forever/macros/),
[Kami Labs](https://kami-labs.fr/en/wow-forever/macros-wow-forever-9-classes/)). It is not tested in Forever's client here; if it fails,
put plain Sinister Strike back on Q and right-click the mob to start swinging.
