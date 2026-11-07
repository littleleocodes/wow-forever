# Shaman leveling keybinds (hand-written)

[Shaman](../README.md) > [Leveling (solo)](README.md) > Keybinds

A personal layout, written 2026-11-06 on the player's own two action bars, for a player of League of Legends and Deadlock with a mouse
that has two side buttons (WoW shows them as Button 4 and Button 5). Same scheme as the [mage](../../mage/leveling/keybinds.md)
and [paladin](../../paladin/leveling/keybinds.md) layouts: Q the attack you press most, E the control, R the payoff, F the
save, the two thumb buttons the reactions, 1-4 the rest, the Shift bar the wider or rarer
version of the key under it. Keys are for spells you press in a fight and for the things that help you there; buffs, food, drink, the
mount and the Hearthstone have no key and are clicked between fights. It is built on the
[Enhancement leveling page](enhancement.md).

**Which spell is on each key at your level:** the "Keybinds by level" tables of the
[Enhancement level-by-level guide](enhancement-by-level.md). This page is the layout at 60, the setup and the macros.

This file is hand-written: the regeneration that rewrites the rest of this folder leaves it alone. Edit it by hand.

## Set up first (Esc, Key Bindings and Interface)

- The two action bars: bar 1 is bound to Q, E, R, F, Mouse 5, Mouse 4, 1, 2, 3, 4, C and the middle mouse button; bar 2 to the same keys
  with Shift, with Shift+X in the last slot. The tables below list the slots in that order.
- Movement: Strafe Left on A and Strafe Right on D, turning with the right mouse button held, as in Deadlock.
- Interface, Combat: Auto Self Cast on, Self Cast Key Alt. With a mob targeted, your heals land on you without changing target.
- A side bar without keybinds for the things you click: Lightning Shield, the weapon imbue, Ghost Wolf, food, water, the mount, the Hearthstone.

## Bar 1: the fight

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Q | Earth Shock macro (4) | Whenever the shock cooldown is free; after a Stormstrike it hits 20% harder. It also interrupts a caster, and it starts your swings too |
| E | Frost Shock (20) | A mob runs away, or you want to walk away from one. It shares the shock cooldown |
| R | Stormstrike (25, talent) | Whenever it is ready |
| F | Stoneclaw Totem (8) | Under 30% of your health: the mob turns on the totem while you heal |
| Mouse 5 (front side button) | Healing Wave (1), Lesser Healing Wave from 20 | Under 40% of your health |
| Mouse 4 (back side button) | Grounding Totem (30) | A caster mob is on you: the totem eats its next spell |
| 1 | Lightning Bolt (1) | Instant at 5 stacks of Maelstrom Weapon (35), once the mob is under 35% health; at 1-3 an opener if you like |
| 2 | Searing Totem (10) | As you pull, while you have more than half your mana |
| 3 | Free | |
| 4 | Rage of the Farseer (40, talent) | At the start of a fight whenever it is ready |
| C | Healing Wave (20) | The big heal, in a stun or behind the totem; between fights, back to 80% |
| Middle mouse | Free | |

## Bar 2: the same keys with Shift

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Shift+Q | Flame Shock (10) | Packs: a dot to spread before Fire Nova. Never on one mob |
| Shift+E | Fire Nova (12) | Packs: several mobs on you |
| Shift+R | Chain Lightning (32) | Packs |
| Shift+F | Earthbind Totem (6) | Escape: slows everything around you |
| Shift+Mouse 5 | Healing Stream Totem (20) | A heal that keeps ticking while you fight or rest |
| Shift+Mouse 4 | Tremor Totem (18) | A mob fears you |
| Shift+1 | Magma Totem (26) | Packs |
| Shift+2 | Purge (12) | A mob has a buff worth removing |
| Shift+3 to Shift+X | Free | |

## No key: click these between fights

Lightning Shield (before a pull, once its charges are gone), Rockbiter Weapon (Windfury Weapon from 30), Ghost Wolf, food, water, your mount (40 in Classic), the Hearthstone, and the buff totems
(Strength of Earth, Windfury Totem) that cost more than they return against one mob. Tab and Space stay on WoW's defaults.

## Macros (Esc, Macros, New; pick the question-mark icon so the button shows the spell)

Earth Shock with the start attack line, on Q from level 4. A shock does not start your swings by itself, and this macro does, so no key
needs the plain Attack button. The start line runs first, so a press still starts your swings while the shock is on cooldown. From
range, your swings begin when you reach the mob. At levels 1-3, right-click the mob to start swinging.

```
#showtooltip Earth Shock
/startattack [harm,nodead]
/cast Earth Shock
```

`/startattack` is a command of the Classic client, and Forever macro guides use it
([RankedBoost](https://rankedboost.com/world-of-warcraft/forever/macros/),
[Kami Labs](https://kami-labs.fr/en/wow-forever/macros-wow-forever-9-classes/)). It is not tested in Forever's client here; if it fails,
put plain Earth Shock back on Q and right-click the mob to start swinging.
