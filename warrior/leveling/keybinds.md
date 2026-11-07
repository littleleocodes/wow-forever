# Warrior leveling keybinds (hand-written)

[Warrior](../README.md) > [Leveling (solo)](README.md) > Keybinds

A personal layout, written 2026-11-06 on the player's own two action bars, for a player of League of Legends and Deadlock with a mouse
that has two side buttons (WoW shows them as Button 4 and Button 5). Same scheme as the [mage](../../mage/leveling/keybinds.md)
and [paladin](../../paladin/leveling/keybinds.md) layouts: Q the attack you press most, E the engage, R the payoff, F the
escape, the two thumb buttons the reactions, 1-4 the rest, the Shift bar the wider version of
the key under it. Keys are for spells you press in a fight; Battle Shout, food, bandages, the mount and the Hearthstone have no key and
are clicked between fights. It is built on the [Arms leveling page](arms.md).

**Which spell is on each key at your level:** the "Keybinds by level" tables of the
[Arms level-by-level guide](arms-by-level.md). This page is the layout at 60, the setup and the macro.

This file is hand-written: the regeneration that rewrites the rest of this folder leaves it alone. Edit it by hand.

## Set up first (Esc, Key Bindings and Interface)

- The two action bars: bar 1 is bound to Q, E, R, F, Mouse 5, Mouse 4, 1, 2, 3, 4, C and the middle mouse button; bar 2 to the same keys
  with Shift, with Shift+X in the last slot. The tables below list the slots in that order.
- Movement: Strafe Left on A and Strafe Right on D, turning with the right mouse button held, as in Deadlock.
- A side bar without keybinds for the things you click: Battle Shout, food, bandages, the mount, the Hearthstone.

## Bar 1: the fight

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Q | Heroic Strike macro (1), Mortal Strike from 40 (talent) | Heroic Strike with spare rage until 39; Mortal Strike whenever it is ready from 40. It starts your swings too |
| E | Charge (4) | To open every fight, after Bloodrage |
| R | Rend (4) | Once per mob, while it has more than a third of its health |
| F | Intimidating Shout (22) | A pull goes wrong: everything around you runs for 8 seconds |
| Mouse 5 (front side button) | Overpower (12) | Whenever it lights up: after a dodge, or from Bloodthrill while Rend ticks. Keep 15 rage for it |
| Mouse 4 (back side button) | Bloodrage (10) | Before the Charge, while you are above 45% of your health |
| 1 | Victory Rush (20) | It lights up after a kill: open the next fight with it when you are below 90% of your health |
| 2 | Execute (24) | First, once the mob is below 20% of its health |
| 3 | Hamstring (8) | A mob runs away |
| 4 | Retaliation (20) | A pull goes wrong and the mobs are on you |
| C | Heroic Strike (40) | Spare rage after Slam, once Mortal Strike has taken Q |
| Middle mouse | Free | |

## Bar 2: the same keys with Shift

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Shift+Q | Slam (35, with Improved Slam) | Spare rage, ahead of Heroic Strike. Keep 15 for Overpower and 30 more when Mortal Strike is almost ready |
| Shift+E | Thunder Clap (6) | Packs: after Sweeping Strikes |
| Shift+R | Sweeping Strikes (39, talent) | Two or more mobs: press it, then Thunder Clap and Cleave |
| Shift+Mouse 5 | Cleave (20) | Packs: the spare-rage strike that hits two |
| Shift+F, Shift+Mouse 4, Shift+1 to Shift+X | Free | |

## No key: click these between fights

Battle Shout (it lasts 3 minutes), Battle Stance (you never leave it), food, bandages, your mount (40 in Classic) and the Hearthstone.
Defensive Stance, Taunt, Sunder Armor, Shield Bash and Revenge are for tanking. Tab and Space stay on WoW's defaults.

## Macros (Esc, Macros, New; pick the question-mark icon)

Your strike with the start attack line, on Q from level 1. It starts your swings as well, so no key needs the plain Attack button. The
start line runs first, so a press still starts your swings when you are short of rage. At level 40, change both names to Mortal Strike
and put plain Heroic Strike on C.

```
#showtooltip Heroic Strike
/startattack [harm,nodead]
/cast Heroic Strike
```

`/startattack` is a command of the Classic client, and Forever macro guides use it
([RankedBoost](https://rankedboost.com/world-of-warcraft/forever/macros/),
[Kami Labs](https://kami-labs.fr/en/wow-forever/macros-wow-forever-9-classes/)). It is not tested in Forever's client here; if it fails,
put plain Heroic Strike back on Q and right-click the mob to start swinging.

Bloodrage and the Charge in one press, on Mouse 4 instead of plain Bloodrage. Bloodrage is off the global cooldown in the Classic client,
so the Charge fires at once; if it does not in Forever, keep Bloodrage on Mouse 4 and Charge on E.

```
#showtooltip Charge
/cast Bloodrage
/cast Charge
```
