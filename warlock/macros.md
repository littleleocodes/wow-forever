# Warlock macros (hand-written)

[Warlock](README.md) > Macros

Macro ideas for every warlock spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these warlock spells are: Amplify Curse, Demonic Sacrifice and Fel Domination. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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
- **Frees:** nothing: this fills a free key, Shift+C on your bars (C holds your Healthstone).
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

### Best mana potion in your bags

```
#showtooltip
/use item:13444
/use item:18253
/use item:18841
/use item:13443
/use item:6149
/use item:3827
/use item:3385
/use item:2455
/use item:2456
```

- **Replaces:** clicking a potion in your bags.
- **Frees:** nothing: this fills a free key, Shift+X on your bars. It shares the healing potion's cooldown.

The numbers are item ids, best first by the mana they give: the nine names would not fit in 255 characters (this is 151; 162 with RestCue's first line). Major Rejuvenation Potion gives as much health as mana: it is second here and first in the healing macro, so either macro can spend it. Every potion here shares the healing potions' 2-minute cooldown. Left out: the battleground draughts; Restored Mana Potion, Forever's own (no source found).

| Line | Potion: mana, level, where from |
|---|---|
| item:13444 | Major Mana Potion: 1,350-2,250; level 49; Alchemy, or the auction house. |
| item:18253 | Major Rejuvenation Potion: 1,440-1,760 mana and as much health; level 50; Alchemy, or the auction house. |
| item:18841 | Combat Mana Potion: 900-1,500; level 41; battleground vendors (Alterac Mountains, Stormwind, the battlegrounds); bind on pickup. |
| item:13443 | Superior Mana Potion: 900-1,500; level 41; Alchemy, or the auction house. |
| item:6149 | Greater Mana Potion: 700-900; level 31; Alchemy, or the auction house. |
| item:3827 | Mana Potion: 455-585; level 22; Alchemy, or the auction house. |
| item:3385 | Lesser Mana Potion: 280-360; level 14; Alchemy, or the auction house. |
| item:2455 | Minor Mana Potion: 140-180; level 5; Alchemy, or the auction house. |
| item:2456 | Minor Rejuvenation Potion: 90-150 mana and as much health; level 5; Alchemy, or the auction house. |

### Quiet the not-ready errors

```
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_SPELL_COOLDOWN,false)
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_ABILITY_COOLDOWN,false)
/run for i=569772,569776 do MuteSoundFile(i) end
```

- **Replaces:** nothing. Click it once after each login from a side bar.
- **Why it works:** the first two lines turn off the text, speech and sound of the "not ready" errors only, the way Forever's own error frame does, and useful errors like "Out of range" stay. The last line mutes the spell fizzle sound until you restart the game. These macros press spells on cooldown a lot, so this keeps them quiet.

## Affliction

Leveling and raid. The keys below are those of the [keybinds page](leveling/keybinds.md).

### Every dot on one key

```
#showtooltip Corruption
/petattack
/castsequence reset=target Corruption, Bane of Agony, Siphon Life
```

- **Replaces:** The pull macro on Mouse 4, Bane of Agony on 1 and Siphon Life on 3.
- **Frees:** Keys 1 and 3.
- **Fill it with:** Nothing needed: Fear, Drain Life and Death Coil, the keys for when a mob reaches you, already sit on E, R and F.
- **Why it works:** One press each: three presses put every dot up, and the pet goes in with the first. The sequence loops, so stop pressing once they are up. Before you learn Siphon Life, drop it from the list. It does not know the tuned limits (no Corruption below 35% of the mob's health, none below 15% mana), so skip a dot by hand on a mob that is nearly dead. In a raid the dots are recast on their own timers, so use the plain keys there. The Amplify Curse macro below needs key 1 for itself: keep this one to Corruption and Siphon Life once you have the talent.

### Amplified curse

```
#showtooltip Bane of Agony
/cast Amplify Curse
/cast Bane of Agony
```

- **Replaces:** Plain Bane of Agony on 1: the keybinds page puts this macro there once you have the talent.
- **Frees:** The key Amplify Curse would need of its own.
- **Fill it with:** Nothing: Life Tap already has 4.
- **Why it works:** Amplify Curse is off the global cooldown.

### A wand that never turns itself off

```
#showtooltip Shoot
/cast !Shoot
```

- **Replaces:** Middle mouse, which holds Shoot.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Plain Shoot is a toggle, so a second press stops the wand, like the Attack button. The `!` keeps it on. A simple swap on the key you already use.

## Demonology

Demon builds.

### Sacrifice the Imp and summon the Succubus (raid)

```
#showtooltip Summon Succubus
/cast Demonic Sacrifice
/cast Summon Succubus
```

- **Replaces:** Clicking Demonic Sacrifice and the summon on your side bar before the pull.
- **Frees:** Nothing on your bars: summons have no key. Put it on the side bar.
- **Fill it with:** Nothing.
- **Why it works:** Demonic Sacrifice is off the global cooldown, so one press sacrifices the Imp and starts the Succubus cast. It is for the Demonology raid build, which takes Demonic Pact: with it the sacrifice survives the new summon. Without Demonic Pact the summon would end the buff, so do not use it. Fel Domination (which makes the next summon fast) is not in any Demonology build on the pages, so there is no macro for it.

### Dots and the brand

```
#showtooltip Searing Pain
/petattack
/cast Searing Pain
```

- **Replaces:** Searing Pain on Mouse 5, if you would rather send the pet with the brand than with the Corruption pull on Mouse 4.
- **Frees:** Nothing: the pull macro on Mouse 4 already sends the pet.
- **Fill it with:** Nothing: Fear has E.
- **Why it works:** The pet goes in with your Searing Pain. The fight lab opens with Corruption instead (the pull macro on Mouse 4), so this is for players who would rather open with the brand. The tuned rules cast Searing Pain only on a mob above a third of its health and while you have more than 30% mana, so do not open with it on a nearly dead mob.

### A wand that never turns itself off

```
#showtooltip Shoot
/cast !Shoot
```

- **Replaces:** Middle mouse, which holds Shoot.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Plain Shoot is a toggle, so a second press stops the wand, like the Attack button. The `!` keeps it on. A simple swap on the key you already use.

## Destruction

Immolate and Conflagrate.

### Immolate, then Conflagrate (leveling, from 5 points in Shadow and Flame)

```
#showtooltip Conflagrate
/castsequence reset=target Immolate, Conflagrate
```

- **Replaces:** Immolate on 2 and Conflagrate on R: put the macro on one of them, and the other is free.
- **Frees:** Key 2, if you put the macro on R.
- **Fill it with:** Nothing needed: Shadowburn already sits on Mouse 5.
- **Why it works:** First press burns the mob, the second casts Conflagrate. A castsequence stops at a step that is not ready, so it stalls on Conflagrate's 10-second cooldown: press the plain Conflagrate key then, and the sequence starts over on a new target. Conflagrate consumes Immolate unless Shadow and Flame saves it (20% per rank, so always at 5 ranks, level 39): before that, cast it when Immolate has about 3 seconds left, by hand. In a raid Immolate and Conflagrate run on separate timers, so use the plain keys there.

### Pet and fire

```
#showtooltip Immolate
/petattack
/cast Immolate
```

- **Replaces:** Immolate on 2. The keybinds page's Destruction pull macro on Mouse 4 opens with Shadow Bolt instead, as the fight lab does from level 10.
- **Frees:** Key 2, if you pull with this macro.
- **Fill it with:** Nothing: Fear has E.
- **Why it works:** The pet goes in with your opener.

### A wand that never turns itself off

```
#showtooltip Shoot
/cast !Shoot
```

- **Replaces:** Middle mouse, which holds Shoot.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Plain Shoot is a toggle, so a second press stops the wand, like the Attack button. The `!` keeps it on. A simple swap on the key you already use.
