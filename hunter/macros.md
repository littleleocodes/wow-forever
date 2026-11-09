# Hunter macros (hand-written)

[Hunter](README.md) > Macros

Macro ideas for every hunter spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform`, `/petattack`, `/targetenemy` and `/console` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these hunter spells are: Auto Shot, Bestial Wrath, Deterrence, Feign Death, Rapid Fire and Raptor Strike. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

To make one: Esc, Macros, New, pick the question-mark icon so the button shows the spell, and drag it onto the key. The melee layout (Beast-Survival and Survival) is on the [keybinds page](leveling/keybinds.md); the Beast Mastery, Beast-Marks and Marksmanship keys are in the key table of each spec's by-level guide ([Beast Mastery](leveling/beast-mastery-by-level.md), [Beast-Marks](leveling/beast-marks-by-level.md), [Marksmanship](leveling/marksmanship-by-level.md)).

## Every spec

### Best healing potion in your bags

```
#showtooltip
/use Major Healing Potion
/use Superior Healing Potion
/use Greater Healing Potion
/use Healing Potion
/use Lesser Healing Potion
/use Minor Healing Potion
```

- **Replaces:** clicking a potion in your bags.
- **Frees:** nothing: this fills a free key. C is free in the Beast-Survival guide; the other guides hold Rapid Fire on C from level 26, so put it on Shift+C there.
- **Why it works:** only the first potion you own goes off, because they share a cooldown.

### Best mana potion in your bags

```
#showtooltip
/use Major Mana Potion
/use Superior Mana Potion
/use Greater Mana Potion
/use Mana Potion
/use Lesser Mana Potion
/use Minor Mana Potion
```

- **Replaces:** clicking a potion in your bags.
- **Frees:** nothing: this fills a free key, Shift+C (Shift+X where the healing potion took Shift+C). It shares the healing potion's cooldown.

### Quiet the not-ready errors

```
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_SPELL_COOLDOWN,false)
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_ABILITY_COOLDOWN,false)
/run for i=569772,569776 do MuteSoundFile(i) end
```

- **Replaces:** nothing. Click it once after each login from a side bar.
- **Why it works:** the first two lines turn off the text, speech and sound of the "not ready" errors only, the way Forever's own error frame does, and useful errors like "Out of range" stay. The last line mutes the spell fizzle sound until you restart the game. These macros press spells on cooldown a lot, so this keeps them quiet.

## Beast-Survival and Survival

The melee hunter. Keys below are the [Beast-Survival keybinds](leveling/keybinds.md), with the Serpent Sting macro on Mouse 4 and the Raptor Strike macro below on Q.

### Melee only: no Auto Shot

```
/console autoRangedCombat 0
```

- **Replaces:** nothing. Click it once from a side bar. The game should keep the setting; if Auto Shot comes back after a login, click it again.
- **Why it works:** the client's "Auto Ranged Combat" setting turns any attack you start on a mob outside melee range into Auto Shot: a Raptor Strike press as the mob runs in, or a `/startattack` line, turns your bow on. With it off, you only ever swing. Forever's settings code has it under Gameplay, Combat (Blizzard_SettingsDefinitions_Frame/Combat.lua), but shows the box only when the client allows it. Untested here. To shoot again, run the line with 1 at the end.

### Raptor Strike that picks the mob

```
#showtooltip Raptor Strike
/targetenemy [noharm][dead]
/startattack
/cast Raptor Strike
```

- **Replaces:** Q.
- **Frees:** nothing. Tab keeps its default.
- **Fill it with:** Nothing.
- **Why it works:** `/targetenemy` is Tab. The first line picks the nearest enemy only when you have no living enemy targeted, so a press never drops the mob you are on. `/startattack` keeps your swings going while Raptor Strike waits out its 6-second cooldown. Turn Auto Ranged Combat off first, or that line starts Auto Shot whenever the mob is out of reach. The tuned rules keep Raptor Strike for the last 20% of the mob's health: pressed all fight, it spends mana the sting would use better.

### Send the pet with the sting

```
#showtooltip Serpent Sting
/petattack
/startattack [harm,nodead]
/cast Serpent Sting
```

- **Replaces:** the plain Serpent Sting macro on Mouse 4 (keybinds page), and the pet bar's attack key.
- **Frees:** The pet bar's attack key.
- **Fill it with:** Nothing: keep the pet bar's keys for Growl and follow.
- **Why it works:** `/petattack` is off the global cooldown. One press sends the pet, arms your swings and stings. It uses your target, so pick the mob first. With Auto Ranged Combat off (above), the `/startattack` line is untested at range.

### Feign, then trap

```
#showtooltip Feign Death
/castsequence reset=30 Feign Death, Freezing Trap
```

- **Replaces:** F and 2.
- **Frees:** 2.
- **Fill it with:** 2 takes Frost Trap from Shift+1.
- **Why it works:** Traps work in combat in Forever and land at your own feet, so the trap alone needs no Feign Death. The pair is for a mob that is already on you: Feign Death drops it back on the pet or off you, and the Freezing Trap is then ready where you lie. Feign Death can be resisted, so look before the second press. Untested.

### Finish, or dodge back

```
#showtooltip Raptor Strike
/cast Mongoose Bite
/cast Raptor Strike
```

- **Replaces:** Q and Mouse 5.
- **Frees:** Mouse 5.
- **Fill it with:** Nothing planned. Lacerate stays on 1.
- **Why it works:** Raptor Strike is off the global cooldown and replaces your next swing. This spends mana on Raptor Strike all fight, which the tuned rules do not (they keep it for the last 20% of the mob's health): use it only if you dislike watching for a dodge.

## Beast Mastery

The pet hunter.

### Everything at the pull

```
#showtooltip Bestial Wrath
/cast Bestial Wrath
/cast Rapid Fire
/cast Intimidation
```

- **Replaces:** Bestial Wrath (R), Rapid Fire (C) and Intimidation (middle mouse) in the Beast Mastery guide.
- **Frees:** Two keys, C and the middle mouse button.
- **Fill it with:** Your healing potion on C (above). Mend Pet (3) and Wing Clip (E) already have keys.
- **Why it works:** Bestial Wrath and Rapid Fire are off the global cooldown, so all three go in one press. Intimidation needs the pet in melee: send it first. The leveling rotation casts all three at the pull; a raid rotation never presses Intimidation, so drop that line there. Beast-Marks has neither Bestial Wrath nor Intimidation.

### Sting and send

```
#showtooltip Serpent Sting
/petattack
/cast !Auto Shot
/cast Serpent Sting
```

- **Replaces:** the Serpent Sting key and the pet bar's attack key (Auto Shot has no key in the guides).
- **Frees:** The pet bar's attack key.
- **Fill it with:** Nothing: Hunter's Mark already has key 1, as a similar macro.
- **Why it works:** `!` stops a second press turning Auto Shot off.

## Marksmanship and Beast-Marks

The ranged hunter.

### Aimed Shot that keeps Auto Shot on

```
#showtooltip Aimed Shot
/cast !Auto Shot
/cast Aimed Shot
```

- **Replaces:** Q (Auto Shot has no key in the guides).
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Pressing it starts your shooting and never stops it.

### Rapid Fire with your burst

```
#showtooltip Rapid Fire
/cast Rapid Fire
/cast Aimed Shot
```

- **Replaces:** Rapid Fire (C) and one Aimed Shot press.
- **Frees:** Nothing, but the opener is one press.
- **Fill it with:** Nothing.
- **Why it works:** Rapid Fire is off the global cooldown.
