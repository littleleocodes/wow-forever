# Rogue macros (hand-written)

[Rogue](README.md) > Macros

Macro ideas for every rogue spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these rogue spells are: Cold Blood, Evasion, Premeditation, Riposte, Sprint, Stealth and Vanish. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

To make one: Esc, Macros, New, pick the question-mark icon so the button shows the spell, and drag it onto the key. Your layout is on the [keybinds page](leveling/keybinds.md).

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
- **Frees:** nothing: this fills a free key, C on your bars.
- **Why it works:** only the first potion you own goes off, because they share a cooldown.

### Quiet the not-ready errors

```
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_SPELL_COOLDOWN,false)
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_ABILITY_COOLDOWN,false)
/run for i=569772,569776 do MuteSoundFile(i) end
```

- **Replaces:** nothing. Click it once after each login from a side bar.
- **Why it works:** the first two lines turn off the text, speech and sound of the "not ready" errors only, the way Forever's own error frame does, and useful errors like "Out of range" stay. The last line mutes the spell fizzle sound until you restart the game. These macros press spells on cooldown a lot, so this keeps them quiet.

## Combat

Leveling and raid. Keys below are your [Combat keybinds](leveling/keybinds.md) (the layout is built on Combat with swords), with the Sinister Strike macro on Q.

### Stealth and the opener on one key

```
#showtooltip Garrote
/cast [nostealth] Stealth
/cast [stealth] Garrote
```

- **Replaces:** 1 and Shift+1.
- **Frees:** Shift+1.
- **Fill it with:** Shift+1 takes Vanish from 3, right above your opener, and 3 goes free.
- **Why it works:** Stealth is off the global cooldown. First press hides you, second press opens. In combat the first line fails and does no harm.

### Cold Blood into Eviscerate

```
#showtooltip Eviscerate
/cast Cold Blood
/cast Eviscerate
```

- **Replaces:** R and C.
- **Frees:** C.
- **Fill it with:** C takes Kick from Shift+E if you play daggers (swords never Kick in the tuned rotation: leave C free or put Blind there).
- **Only for a build that has Cold Blood.** The Combat leveling build takes it at 55; check the talent link of the raid page you follow, because a Combat raid build may not have it. Without the talent, use plain Eviscerate on R.
- **Why it works:** Cold Blood is off the global cooldown, so an Eviscerate pressed while it is ready always carries it (its cooldown is 3 minutes). It fires on every Eviscerate, including the small one that finishes a mob, so press R at 5 points; to spend Cold Blood on purpose, keep the plain macro on C instead.

### A breather that holds

```
#showtooltip Gouge
/stopattack
/cast Gouge
```

- **Replaces:** Nothing: a variant for E.
- **Frees:** Nothing.
- **Fill it with:** Do the same for Blind on Shift+2.
- **Why it works:** Your white swings wake a gouged or blinded mob, so turn them off first. Your next Q turns them back on.

### Run

```
#showtooltip Evasion
/cast Evasion
/cast Sprint
```

- **Replaces:** F and 4.
- **Frees:** 4.
- **Fill it with:** 4 takes Blind from Shift+2.
- **Why it works:** Both are off the global cooldown. Only for a fight you are leaving: Sprint's cooldown is long.

## Assassination

Mutilate builds (the Assassination leveling build takes Mutilate at level 40; before that the Q macro is Sinister Strike). The Daggers (split) raid builds are not Mutilate builds unless the talent link on their raid page shows it: otherwise use the Combat macros above.

### Stealth and the opener

```
#showtooltip Garrote
/cast [nostealth] Stealth
/cast [stealth] Garrote
```

- **Replaces:** The opener key and the Stealth key.
- **Frees:** One key.
- **Fill it with:** Vanish.
- **Why it works:** The same macro as Combat.

### Mutilate that starts your swings

```
#showtooltip Mutilate
/startattack [harm,nodead]
/cast Mutilate
```

- **Replaces:** the plain Mutilate button on Q. The Q macro already starts your swings from level 1 (no key holds Attack), so this changes the spell on Q from Sinister Strike to Mutilate at level 40.
- **Frees:** nothing.
- **Fill it with:** Nothing needs it.
- **Why it works:** The strike macro for this build. Before Mutilate, the same macro with Sinister Strike.

### Cold Blood into your finisher

```
#showtooltip Eviscerate
/cast Cold Blood
/cast Eviscerate
```

- **Replaces:** The finisher key and the Cold Blood key.
- **Frees:** One key.
- **Fill it with:** Kick.
- **Why it works:** Off the global cooldown, as for Combat. The Assassination leveling build has Cold Blood from level 25. It fires on every Eviscerate, including the small one that kills a mob, so press it at 5 points.

## Subtlety and Combat-Subtlety

Hemorrhage builds.

### Premeditation into the opener

```
#showtooltip Ambush
/cast [nostealth] Stealth
/cast Premeditation
/cast [stealth] Ambush
```

- **Replaces:** The opener, Stealth and Premeditation keys.
- **Frees:** Two keys.
- **Fill it with:** Ghostly Strike and Vanish.
- **Why it works:** Stealth and Premeditation are off the global cooldown. Swap Ambush for Garrote once your fights run long enough for the bleed.

### Hemorrhage that starts your swings

```
#showtooltip Hemorrhage
/startattack [harm,nodead]
/cast Hemorrhage
```

- **Replaces:** the plain Hemorrhage button on Q. The Q macro already starts your swings from level 1 (no key holds Attack), so this changes the spell on Q from Sinister Strike to Hemorrhage: at level 30 in the Subtlety build, at level 60 in Combat-Subtlety.
- **Frees:** nothing.
- **Fill it with:** Nothing needs it.
- **Why it works:** The strike macro for the Subtlety builds. Before Hemorrhage, the same macro with Sinister Strike.
