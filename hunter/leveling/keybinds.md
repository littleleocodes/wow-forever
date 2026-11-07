# Hunter leveling keybinds (hand-written)

[Hunter](../README.md) > [Leveling (solo)](README.md) > Keybinds

A personal layout, written 2026-11-06 on the player's own two action bars, for a player of League of Legends and Deadlock with a mouse
that has two side buttons (WoW shows them as Button 4 and Button 5). Same scheme as the [mage](../../mage/leveling/keybinds.md)
and [paladin](../../paladin/leveling/keybinds.md) layouts: Q the attack you press most, E the control, R the payoff, F the
escape, the two thumb buttons the reactions, 1-4 the rest, the Shift bar the rarer tools.
Keys are for spells you press in a fight and for the things that help you there; aspects, tracking, pet care, food, drink, the mount
and the Hearthstone have no key and are clicked between fights. It is built on the
[Beast-Survival leveling page](beast-survival.md), the melee hunter, the fastest hunter build in the fight lab.

**Which spell is on each key at your level:** the "Keybinds by level" tables of the
[Beast-Survival level-by-level guide](beast-survival-by-level.md). This page is the layout at 60, the setup and the macros.

This file is hand-written: the regeneration that rewrites the rest of this folder leaves it alone. Edit it by hand.

## Set up first (Esc, Key Bindings and Interface)

- The two action bars: bar 1 is bound to Q, E, R, F, Mouse 5, Mouse 4, 1, 2, 3, 4, C and the middle mouse button; bar 2 to the same keys
  with Shift, with Shift+X in the last slot. The tables below list the slots in that order.
- Movement: Strafe Left on A and Strafe Right on D, turning with the right mouse button held, as in Deadlock.
- The pet bar keeps its own keys for the pet's attack and follow commands. Send the pet from there before you walk in.
- A side bar without keybinds for the things you click: the aspects, the tracking, Call Pet, Feed Pet, Revive Pet, food, drink, the
  mount, the Hearthstone.

## Bar 1: the fight

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Q | Raptor Strike (1) | Once the mob is below 20% of its health: it replaces your next swing. The tuned rules keep it for the finish |
| E | Wing Clip (12) | A mob runs away |
| R | Immolation Trap (16) | At your feet while the mob has more than 40% of its health and you have half your mana or more |
| F | Feign Death (30) | A pull gone wrong: the mobs go for the pet or home |
| Mouse 5 (front side button) | Mongoose Bite (16) | It lights up after you dodge |
| Mouse 4 (back side button) | Serpent Sting macro (4) | The pull, every fight, as the mob comes at you. It starts your swings too |
| 1 | Lacerate (30) | While the mob has more than half its health and you have 80% of your mana or more |
| 2 | Freezing Trap (20) | Before a pull that will bring two mobs: the second stands frozen |
| 3 | Mend Pet (12) | The pet drops below a third of its health |
| 4 | Auto Shot (1) | One shot as the mob comes, then melee |
| C | Free | |
| Middle mouse | Free | |

## Bar 2: the same keys with Shift

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Shift+Q | Concussive Shot (8) | Slow a mob at range |
| Shift+E | Scare Beast (14) | A second beast joins |
| Shift+R | Explosive Trap (34) | Packs |
| Shift+Mouse 5 | Arcane Shot (6) | A ranged hit on a mob that runs |
| Shift+1 | Frost Trap (28) | Packs, or an escape: a slow field under your feet |
| Shift+F, Shift+Mouse 4, Shift+2, Shift+3, Shift+4, Shift+C, Shift+X | Free | |

## No key: click these between fights

Aspect of the Monkey (Aspect of the Beast from 30), the tracking (keep the right one on: Improved Tracking is 5% of your damage), Call Pet,
Feed Pet, Revive Pet, food, drink, your mount (40 in Classic) and the Hearthstone. Hunter's Mark is never cast by the tuned rotation.
Aimed Shot, Multi-Shot and Aspect of the Hawk are for the ranged builds. Tab and Space stay on WoW's defaults.

## Macros (Esc, Macros, New; pick the question-mark icon so the button shows the spell)

Serpent Sting with the start attack line, on Mouse 4 from level 4. Your Q is kept for the finish, and the sting is the first thing you press
in a fight, so this is the key that starts your swings: they begin when the mob reaches you, and no key needs the plain Attack
button. If it ends your Auto Shot, that is fine: this build fires one shot and goes to melee. At levels 1-3, right-click the mob to
start swinging.

```
#showtooltip Serpent Sting
/startattack [harm,nodead]
/cast Serpent Sting
```

`/startattack` is a command of the Classic client, and Forever macro guides use it
([RankedBoost](https://rankedboost.com/world-of-warcraft/forever/macros/),
[Kami Labs](https://kami-labs.fr/en/wow-forever/macros-wow-forever-9-classes/)). It is not tested in Forever's client here; if it fails,
put plain Serpent Sting back on Mouse 4 and right-click the mob to start swinging.
