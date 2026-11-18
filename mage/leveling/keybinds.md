# Mage leveling keybinds (hand-written)

[Mage](../README.md) > [Leveling (solo)](README.md) > Keybinds

A personal layout, written 2026-11-04 and moved onto the player's own two action bars on 2026-11-06, for a player of League of Legends
and Deadlock with a mouse that has two side buttons (WoW shows them as Button 4 and Button 5). League's Q/E/R and F (Flash) hold the
core rotation, the two thumb buttons the two reaction spells, 1-4 the secondary spells, and the Shift bar the pack spells and the wards.
Keys are for spells you press in a fight and for the things that help you there: buffs, food, drink, conjuring, the mount and the
Hearthstone have no key and are clicked between fights. It is built on the [Arcane-Frost](arcane-frost.md) build (the recommended one;
the [Frost](frost.md) build uses the same keys and leaves key 1 and Shift+Q free). The Arcane, Fire and Frostfire guides change a few
keys; their changes are in the notes under each guide's own keybind tables.

**Which spell is on each key at your level:** the "Keybinds by level" tables of your spec's own level-by-level guide:
[Arcane-Frost](arcane-frost-by-level.md), [Frost](frost-by-level.md), [Arcane](arcane-by-level.md), [Fire](fire-by-level.md) or
[Frostfire](frostfire-by-level.md). This page is the Arcane-Frost layout at 60, the setup and the macros.

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
| Mouse 5 (front side button) | Fire Blast (6) | The finish, on a mob between a tenth and a fifth of its health: in the Frost and Arcane-Frost builds the tuned rules use it for nothing else (Fire also presses it on a mob that reaches it, Arcane when it cannot afford Missiles; Frostfire never does) | Thumb reaction |
| Mouse 4 (back side button) | Counterspell (24) | A mob starts casting | Thumb reaction, like Deadlock's parry |
| 1 | Arcane Missiles (8, used from 37 in this build) | Whenever Missile Barrage lights up; not while being hit unless the mob is frozen. Free with the Frost build; the Arcane guide puts Arcane Blast here, the Fire guide Pyroblast | Deadlock ability 1 |
| 2 | Polymorph (8) | A second mob joins | Deadlock ability 2 |
| 3 | Mana Shield (20) | Emergency only: mob on you, Nova down, low health | Deadlock ability 3 |
| 4 | Evocation (20) | Between fights, when it is ready and you are under 40% mana. The one between-fights spell with a key: a cooldown and a mana rule make it a decision. Click it instead if you want 4 free | Deadlock 4, the long cooldown |
| C | Cone of Cold (26) | Packs: slow the group and walk. The single-target lists of Frost, Arcane-Frost and Frostfire never cast it; Arcane casts it only on a mob on it below a fifth of its health | A reaction key next to the movement hand |
| Middle mouse | Shoot (wand) | Finishing hits on a mob that is almost dead; while the mob closes too fast for a bolt | The weapon attack |

## Bar 2: the same keys with Shift

| Key | Spell (learned at) | Press it when |
|---|---|---|
| Shift+Q | Presence of Mind macro (53, talent), Arcane-Frost build only | At the pull whenever it is ready, every 3 minutes: an instant Frostbolt. Free with the Frost build |
| Shift+E | Arcane Explosion (14) | Packs: several mobs on you |
| Shift+R | Blizzard (20) | Packs: on a frozen or slowed group |
| Shift+F | Free | |
| Shift+Mouse 5 | Fire Ward (20) | A fire caster is on you: absorbs its next spells |
| Shift+Mouse 4 | Frost Ward (22) | A frost caster is on you |
| Shift+1 | Free; Ice Barrier with the hand-made Leveling - Frost build (under Other builds on the Frost page) | Before every pull, with that build only |
| Shift+2 | Cold Snap (39, talent; the hand-made build has it too) | Frost Nova has more than 8 seconds of cooldown left and the mob still has 40% of its health |
| Shift+3 | Remove Lesser Curse (18) | A curse is on you |
| Shift+4 | Free | |
| Shift+C | Healing potion macro (any level) | A bad pull: the best healing potion in your bags. Every potion shares one cooldown |
| Shift+X | Free; the mana potion macro fits here | |

The Arcane-Frost single-target rotation never casts Cone of Cold, Arcane Explosion or Blizzard; they are for the AoE build under Other
builds on the Frost page and for a pull that brings friends. Free slots stay free until something earns them.

## No key: click these between fights

Your armor (Frost Armor, Ice Armor from 30, Mage Armor from 34; Ice Armor again for a pack, and the Fire build keeps it), Arcane
Intellect, Conjure Water, Conjure Food, the eat-and-drink macro, your mount (40 in Classic), the Hearthstone, Slow Fall and the
teleports. Tab (target nearest enemy) and Space (jump) stay on WoW's defaults.

## Macros (Esc, Macros, New; pick the question-mark icon so the button shows the spell or the item count)

Presence of Mind and the Frostbolt in one press, on Shift+Q (Arcane-Frost build, from 53). Presence of Mind is off the global cooldown in
the simulator's spell data for Forever, so the second line fires at once; if it does not in game, press the two separately.

```
#showtooltip Presence of Mind
/cast Presence of Mind
/cast Frostbolt
```

Eat and drink in one click, on the side bar. The macro holds every rank, best first, so it never needs editing: it drinks the best
conjured water in your bags and eats the best conjured food. In Forever's client data (build 1.60.1.70888, ItemEffect and SpellCooldowns)
every conjured water shares a 1-second cooldown and so does every conjured food. The first water you own goes off and the water lines
after it fail without using anything; the food lines work the same way. Water and food have separate cooldowns, and neither is on the
global cooldown, so one press starts both.

```
/use item:8079
/use item:8078
/use item:8077
/use item:3772
/use item:2136
/use item:2288
/use item:5350
/use item:22895
/use item:8076
/use item:8075
/use item:1487
/use item:1114
/use item:1113
/use item:5349
```

The numbers are the items' ids: the names do not fit in a macro's 255 characters (this one is 210). Highest rank first:

| Conjure rank (water / food level) | Water | Food |
|---|---|---|
| 7 (60) | 8079 Conjured Crystal Water | 22895 Conjured Cinnamon Roll |
| 6 (50 / 52) | 8078 Conjured Sparkling Water | 8076 Conjured Sweet Roll |
| 5 (40 / 42) | 8077 Conjured Mineral Water | 8075 Conjured Sourdough |
| 4 (30 / 32) | 3772 Conjured Spring Water | 1487 Conjured Pumpernickel |
| 3 (20 / 22) | 2136 Conjured Purified Water | 1114 Conjured Rye |
| 2 (10 / 12) | 2288 Conjured Fresh Water | 1113 Conjured Bread |
| 1 (4 / 6) | 5350 Conjured Water | 5349 Conjured Muffin |

Give it a water icon, not the question mark: the question mark would show the first line's item, Crystal Water, until you have it. Older
water stays in your bags while you carry the new rank (conjured items vanish after 15 minutes logged out), and water a higher-level mage
gives you that you are too low to drink is skipped. Not tested in game yet: if one press ever uses two waters, go back to one line of each.

Sources for the Deadlock defaults: [Shacknews, Deadlock controls and keybindings](https://www.shacknews.com/article/141162/deadlock-pc-controls-keybindings),
[Deadlock wiki, Parries](https://deadlock.wiki/Parries), [Deadlock wiki, Melee Attacks](https://deadlock.wiki/Melee_Attacks).
