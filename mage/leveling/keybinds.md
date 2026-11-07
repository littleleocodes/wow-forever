# Mage leveling keybinds (hand-written)

[Mage](../README.md) > [Leveling (solo)](README.md) > Keybinds

A personal layout, written 2026-11-04 and moved onto the player's own two action bars on 2026-11-06, for a player of League of Legends
and Deadlock with a mouse that has two side buttons (WoW shows them as Button 4 and Button 5). League's Q/E/R and F (Flash) hold the
core rotation, the two thumb buttons the two reaction spells, 1-4 the secondary spells, and the Shift bar the pack spells and the wards.
Keys are for spells you press in a fight and for the things that help you there: buffs, food, drink, conjuring, the mount and the
Hearthstone have no key and are clicked between fights. It fits both recommended builds: [Frost](frost.md) and
[Arcane-Frost](arcane-frost.md), which adds **Arcane Missiles** on **Missile Barrage** procs.

**Which spell is on each key at your level:** the "Keybinds by level" tables of the
[Frost level-by-level guide](frost-by-level.md). This page is the layout at 60, the setup and the macros.

This file is hand-written: the regeneration that rewrites the rest of this folder leaves it alone. Edit it by hand.

## Set up first (Esc, Key Bindings and Interface)

- The two action bars: bar 1 is bound to Q, E, R, F, Mouse 5, Mouse 4, 1, 2, 3, 4, C and the middle mouse button; bar 2 to the same keys
  with Shift, with Shift+X in the last slot (not Shift+middle mouse). The tables below list the slots in that order.
- Movement: Strafe Left on A and Strafe Right on D, turning with the right mouse button held, as in Deadlock. That frees Q and E, which
  WoW uses for strafing by default.
- Interface, Combat: Auto Self Cast on, Self Cast Key Alt, so Alt+key self-casts like League.
- A side bar without keybinds (Interface, Action Bars: the right bars) for the things you click: armor, Arcane Intellect, Conjure Water,
  Conjure Food, the eat-and-drink macro, the mount, the Hearthstone.

## Bar 1: the fight

| Key | Spell (learned at) | Press it when | Habit it matches |
|---|---|---|---|
| Q | Frostbolt (4); Fireball at 1-3 | The filler: while the mob walks in and whenever nothing else applies, while the mob has more than a fifth of its health | League Q, Deadlock Q (the basic hit) |
| E | Frost Nova (10) | The mob reaches you, then step back with S | League E, the CC key |
| R | Ice Lance (20, talent) | Into every freeze (Frost Nova, Frostbite, Fingers of Frost), one per 8 seconds | League R, the big hit |
| F | Blink (20) | Out of melee, out of a root | Flash |
| Mouse 5 (front side button) | Fire Blast (6) | The mob will reach you before a bolt lands, it is on you with Nova down, or the finish between a tenth and a fifth of its health | Thumb reaction |
| Mouse 4 (back side button) | Counterspell (24) | A mob starts casting | Thumb reaction, like Deadlock's parry |
| 1 | Arcane Missiles (8), Arcane-Frost build only | Whenever Missile Barrage lights up; not while being hit unless the mob is frozen. Free with the Frost build | Deadlock ability 1 |
| 2 | Polymorph (8) | A second mob joins | Deadlock ability 2 |
| 3 | Mana Shield (20) | Emergency only: mob on you, Nova down, low health | Deadlock ability 3 |
| 4 | Evocation (20) | Between fights, when it is ready and you are under 40% mana. The one between-fights spell with a key: a cooldown and a mana rule make it a decision. Click it instead if you want 4 free | Deadlock 4, the long cooldown |
| C | Cone of Cold (26) | A mob on you with Frost Nova down: slow it and walk; and packs | A reaction key next to the movement hand |
| Middle mouse | Shoot (wand) | Finishing hits on a mob that is almost dead; while the mob closes if Fire Blast is down | The weapon attack |

## Bar 2: the same keys with Shift

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Shift+Q | Presence of Mind macro (53, talent), Arcane-Frost build only | At the pull whenever it is ready, every 3 minutes: an instant Frostbolt. Free with the Frost build |
| Shift+E | Arcane Explosion (14) | Packs: several mobs on you |
| Shift+R | Blizzard (20) | Packs: on a frozen or slowed group |
| Shift+F | Free | |
| Shift+Mouse 5 | Fire Ward (20) | A fire caster is on you: absorbs its next spells |
| Shift+Mouse 4 | Frost Ward (22) | A frost caster is on you |
| Shift+1 | Free; Ice Barrier with the hand-made Frost build | Before every pull, with that build |
| Shift+2 | Free; Cold Snap with the hand-made Frost build | Frost Nova has more than 8 seconds of cooldown left and the mob still has 40% of its health |
| Shift+3 | Remove Lesser Curse (18) | A curse is on you |
| Shift+4 | Free | |
| Shift+C | Free | |
| Shift+X | Free | |

The single-target rotation never casts Cone of Cold, Arcane Explosion or Blizzard; they are for the AoE build under Other builds on the
Frost page and for a pull that brings friends. Free slots stay free until something earns them.

## No key: click these between fights

Frost Armor (Ice Armor from 30), Arcane Intellect, Conjure Water, Conjure Food, the eat-and-drink macro, your mount (40 in Classic),
the Hearthstone, Slow Fall and the teleports. Tab (target nearest enemy) and Space (jump) stay on WoW's defaults. Frost Blast (trained at
24) is never cast by the list.

## Macros (Esc, Macros, New; pick the question-mark icon so the button shows the spell or the item count)

Presence of Mind and the Frostbolt in one press, on Shift+Q (Arcane-Frost build). Presence of Mind is off the global cooldown in the
Classic client, so the second line fires at once; if it does not in Forever, press the two separately.

```
#showtooltip Presence of Mind
/cast Presence of Mind
/cast Frostbolt
```

Eat and drink in one click, on the side bar. Food and drink share no cooldown in the Classic client, so the meal starts right after the drink.

```
#showtooltip
/use Conjured Water
/use Conjured Muffin
```

The names are the rank you currently conjure. The water rank comes at the round level and the food rank two levels later: edit the water
line at the round level and the food line two levels after. Keep one rank of each in the macro (a line for an older water you still carry
would restart the drink with the weaker rank).

| Level | Water line | Food line |
|---|---|---|
| 4 | Conjured Water | Conjured Muffin (from 6) |
| 10 / 12 | Conjured Fresh Water | Conjured Bread |
| 20 / 22 | Conjured Purified Water | Conjured Rye |
| 30 / 32 | Conjured Spring Water | Conjured Pumpernickel |
| 40 / 42 | Conjured Mineral Water | Conjured Sourdough |
| 50 / 52 | Conjured Sparkling Water | Conjured Sweet Roll |
| 60 | Conjured Crystal Water | Conjured Cinnamon Roll |

These are Classic's item names. If a line does nothing, hover the item in your bag and copy its exact name into the macro.

Sources for the Deadlock defaults: [Shacknews, Deadlock controls and keybindings](https://www.shacknews.com/article/141162/deadlock-pc-controls-keybindings),
[Deadlock wiki, Parries](https://deadlock.wiki/Parries), [Deadlock wiki, Melee Attacks](https://deadlock.wiki/Melee_Attacks).
