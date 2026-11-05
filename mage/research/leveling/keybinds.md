# Mage leveling keybinds (hand-written)

[Mage](../../README.md) > [Leveling research](README.md) > Keybinds

A personal layout, written 2026-11-04 and updated 2026-11-05, for a player of League of Legends and Deadlock with a mouse that has two
side buttons (WoW shows them as Button 4 and Button 5). It is built on the recommended [Arcane-Frost leveling page](../../leveling/arcane-frost.md)
(23/0/28): the Frost list plus **Arcane Missiles** on **Missile Barrage** procs. The idea: League's Q/E/R and F (Flash) hold the core
rotation, Deadlock's 1-4 row holds the secondary spells, its Z/X item keys hold the consumables, and the two mouse buttons take the two
reaction spells.

This file is hand-written and nothing generates or deletes it (`mage/leveling/` is regenerated, so it lives here). Edit it by hand.

## Set up first (Esc, Key Bindings and Interface)

- Movement: bind Strafe Left to A and Strafe Right to D, and turn with the right mouse button held, as in Deadlock. That frees Q and E,
  which WoW uses for strafing by default.
- Interface, Combat: turn on Auto Self Cast and set the Self Cast Key to Alt, so Alt+key self-casts like League.
- Interface, Action Bars: enable the Bottom Left bar for the extra slots. Drop each spell into a slot and bind the key to that slot under
  Action Bar Functions.

## The keys

| Key | Spell (learned at) | Press it when | Habit it matches |
|---|---|---|---|
| Q | Frostbolt (4) | The filler: while the mob walks in and whenever nothing else applies, while the mob has more than 10% of its health | League Q, Deadlock Q (the basic hit) |
| E | Frost Nova (10) | The mob reaches you, then step back with S | League E, the CC key |
| R | Ice Lance (20, talent) | Into every freeze (Frost Nova, Frostbite, Fingers of Frost), one per 8 seconds | League R, the big hit |
| F | Blink (20) | Out of melee, out of a root | Flash |
| Shift+Q | Presence of Mind (53, talent), macro below | At the pull whenever it is ready, every 3 minutes: an instant Frostbolt | An empowered Q |
| Mouse 5 (front side button) | Fire Blast (6) | The mob will reach you before a bolt lands, it is on you with Nova down, or the finish while it still has more than 10% | Thumb reaction |
| Mouse 4 (back side button) | Counterspell (24) | A mob starts casting | Thumb reaction, like Deadlock's parry |
| 1 | Arcane Missiles (8) | Whenever Missile Barrage lights up (the talent's first point at 37, complete at 38); not while being hit unless the mob is frozen | Deadlock ability 1 |
| 2 | Polymorph (8) | A second mob joins | Deadlock ability 2 |
| 3 | Mana Shield (20) | Emergency only: mob on you, Nova down, low health | Deadlock ability 3 |
| 4 | Evocation (20) | Between fights, when it is ready and you are under 40% mana | Deadlock 4, the long cooldown |
| T | Shoot (wand) | Finishing hits under 10% of the mob's health; while the mob closes if Fire Blast is down | Next to R, same finger, hand stays on WASD |
| Z | Eat-and-drink macro (below) | Drink below 15% mana, eat below 40% health: one press starts both | Deadlock item 1 |
| X | Conjured food alone | Only if the macro's food line ever stops working | Deadlock item 2 |
| Tab | Target nearest enemy | WoW's default | |
| Space | Jump | WoW's default | Both games |

The thumb buttons took Fire Blast and Counterspell because both are pressed in reaction with a short window. To keep every spell on the
keyboard, swap them with 1 and 2. If T is a stretch, the middle mouse button (the wheel click, Button 3) works as well for the wand.

## Optional

- B: Hearthstone, the recall key. It costs Open All Bags, which moves to Shift+B.
- Shift+1, Shift+2, Shift+3: Arcane Explosion (14), Cone of Cold (26), Blizzard (20). Only for the AoE build under Other builds on the Frost
  page; the single-target list never casts Cone of Cold.
- The hand-made Frost build (the alternative on the Frost page) has Ice Barrier (before every pull) and Cold Snap: put them on 3 and 4 and
  move Mana Shield and Evocation to Shift+3 and Shift+4.

## No key needed

Frost Armor (Ice Armor from 30), Arcane Intellect, Conjure Water and Conjure Food last an hour or are cast between fights: click them.
Frost Blast (trained at 24) is never cast by the list, and this build has no Arcane Blast.

## Macros (Esc, Macros, New; pick the question-mark icon so the button shows the spell or the item count)

Presence of Mind and the Frostbolt in one press, on Shift+Q. Presence of Mind is off the global cooldown in the Classic client, so the second
line fires at once; if it does not in Forever, press the two separately.

```
#showtooltip Presence of Mind
/cast Presence of Mind
/cast Frostbolt
```

Eat and drink in one press, on Z. Food and drink share no cooldown in the Classic client, so the meal starts right after the drink.

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
