# Rogue macros (hand-written)

[Rogue](README.md) > Macros

Macro ideas for every rogue spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these rogue spells are: Cold Blood, Evasion, Premeditation, Riposte, Sprint, Stealth and Vanish. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

To make one: Esc, Macros, New, pick the question-mark icon so the button shows the spell, and drag it onto the key. Your layout is on the [keybinds page](leveling/keybinds.md).

## Every spec

### Best healing potion in your bags

```
#showtooltip
/use item:18253
/use item:13446
/use item:18839
/use item:3928
/use item:241650
/use item:1710
/use item:247242
/use item:929
/use item:247241
/use item:247240
/use item:858
/use item:247239
/use item:118
/use item:4596
```

- **Replaces:** clicking a potion in your bags.
- **Frees:** nothing: this fills a free key, C on your bars.
- **Why it works:** only the first potion you own goes off, because they share a cooldown.

The numbers are item ids, best first: the 14 names would not fit in a macro's 255 characters (this is 232; with the RestCue add-on, which writes the best potion you carry into the first line, 244). Item ids work in Forever's client: the button shows the potion's icon and how many you carry (tested in game on 2026-11-22). The order is the health you keep. Forever's Discolored potions heal more at once, then take three quarters of it back as a 6-second poison or a 12-second disease (from the client's spell data, not seen in game), so they rank by the quarter you keep; for a last-second save, press a Discolored potion by hand from your bags. Left out: the battleground draughts (they work only inside a battleground); Restored and Perishable Healing Potion, Forever's own (no source found); a second Major Healing Potion (item 223913, not confirmed in Forever).

| Line | Potion: health, level, where from |
|---|---|
| item:18253 | Major Rejuvenation Potion: 1,440-1,760 health and as much mana; level 50; Alchemy, or the auction house. |
| item:13446 | Major Healing Potion: 1,050-1,750; level 45; First Aid, or the auction house. |
| item:18839 | Combat Healing Potion: 700-900; level 35; battleground vendors (Alterac Mountains, Stormwind, the battlegrounds); bind on pickup. |
| item:3928 | Superior Healing Potion: 700-900; level 35; First Aid, or the auction house. |
| item:241650 | Major Discolored Healing Potion: 2,625-2,975 at once, 75% back as a poison or disease: about 700 kept; level 60; Alchemy, or the auction house. |
| item:1710 | Greater Healing Potion: 455-585; level 21; First Aid, or the auction house. |
| item:247242 | Superior Discolored Healing Potion: 1,500-1,700 at once: about 400 kept; level 35; Alchemy, or the auction house. |
| item:929 | Healing Potion: 280-360; level 12; First Aid, or the auction house. |
| item:247241 | Greater Discolored Healing Potion: 975-1,105 at once: about 260 kept; level 21; Alchemy, or the auction house. |
| item:247240 | Discolored Healing Potion: 600-680 at once: about 160 kept; level 12; Alchemy, or the auction house. |
| item:858 | Lesser Healing Potion: 140-180; level 3; First Aid, or the auction house. |
| item:247239 | Lesser Discolored Healing Potion: 300-340 at once: about 80 kept; level 3; Alchemy, or the auction house. |
| item:118 | Minor Healing Potion: 70-90; level 1; First Aid, or the auction house. |
| item:4596 | Minor Discolored Healing Potion: 150-170 at once: about 40 kept; level 5; Alchemy, or the auction house. |

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
- **Fill it with:** leave C free or put Blind there: no tuned rogue rotation casts Kick (Assassination dropped it on 2026-11-15), so Kick stays on Shift+E for a caster that hits too hard.
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
- **Fill it with:** Blind, or leave it free: the tuned rotation never casts Kick (2026-11-15).
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

- **Replaces:** the plain Hemorrhage button on Q. The Q macro already starts your swings from level 1 (no key holds Attack), so this changes the spell on Q from Sinister Strike to Hemorrhage: at level 30 in the Subtlety build, at level 32 in Combat-Subtlety.
- **Frees:** nothing.
- **Fill it with:** Nothing needs it.
- **Why it works:** The strike macro for the Subtlety builds. Before Hemorrhage, the same macro with Sinister Strike.
