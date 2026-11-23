# Paladin macros (hand-written)

[Paladin](README.md) > Macros

Macro ideas for every paladin spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these paladin spells are: Judgement, Swift Judgement, Divine Favor, Templar's Bulwark and Voice of Truth. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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
- **Frees:** nothing: this fills a free key, C on your bars, for every spec. Swift Judgement never takes it: Prot-Ret holds it on 3, Protection on Shift+3.
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
- **Frees:** nothing: this fills a free key, Shift+C on your bars for every spec. It shares the healing potion's cooldown.

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

## Retribution

Leveling and raid. Keys below are your [Retribution keybinds](leveling/keybinds.md), which already hold two macros: the Holy Strike macro on Q and the seal and Judgement macro on R.

### The whole rotation on one key

```
#showtooltip Holy Strike
/startattack [harm,nodead]
/castsequence reset=target Seal of Righteousness, Judgement, Judgement, Judgement
/cast Holy Strike
```

- **Replaces:** Q and R, from level 6.
- **Frees:** R.
- **Fill it with:** R is free once Q holds the whole rotation: put Exorcism on R from level 20, the biggest hit you have on Undead and Demons, and key 2, where it sat, goes free. From 44 Hammer of Wrath can leave Shift+R for 2.
- **Why it works:** Judgement is off the global cooldown, so one press casts both attacks in the fight lab's order. Judgement then fires as soon as it is ready, so press E before Q when you want the doubled hit. Change the seal at level 20.

### Repentance that holds

```
#showtooltip Repentance
/stopattack
/cast Repentance
```

- **Replaces:** Nothing: a variant for Shift+E, from 49 if your build takes it.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Any damage wakes the mob, and your next white swing would do it. Turning your swings off first lets you heal, or set up the doubled Judgement on R. Humanoids only. Your next Q turns the swings back on.

## Protection

Tanking and the Protection leveling page.

### Two Judgements on one press

```
#showtooltip Judgement
/cast Judgement
/cast Swift Judgement
```

- **Replaces:** The Judgement and Swift Judgement keys.
- **Frees:** One key.
- **Fill it with:** Holy Shield, if it sits on a harder reach.
- **Why it works:** Both are off the global cooldown, and the rotation wants Swift Judgement right after a Judgement. Swift Judgement's 1-minute cooldown just makes that line do nothing most presses.

### Absorb, then heal

```
#showtooltip Templar's Bulwark
/cast Templar's Bulwark
/cast [@player] Holy Light
```

- **Replaces:** Templar's Bulwark, when you press it to heal behind it.
- **Frees:** One key.
- **Fill it with:** Divine Protection's key can take Blessing of Protection, since both share Forbearance.
- **Why it works:** Templar's Bulwark is off the global cooldown and applies Forbearance. The rotation heals behind its absorb.

### Seal of Fury and Judgement on one key

```
#showtooltip Judgement
/castsequence reset=target Seal of Fury, Judgement, Judgement, Judgement
```

- **Replaces:** The seal key and the Judgement key.
- **Frees:** One key.
- **Fill it with:** Consecration.
- **Why it works:** The Retribution macro with your tanking seal.

## Holy

Healing, and the Holy leveling page.

### A sure critical heal

```
#showtooltip Divine Favor
/cast Divine Favor
/cast [@mouseover,help,nodead][] Holy Light
```

- **Replaces:** Divine Favor and one heal press.
- **Frees:** One key.
- **Fill it with:** Cleanse on a mouseover.
- **Why it works:** Divine Favor is off the global cooldown.

### Heal whoever your mouse is on

```
#showtooltip
/cast [@mouseover,help,nodead][] Flash of Light
```

- **Replaces:** Clicking raid frames before each heal.
- **Frees:** No key, but every heal gets a click shorter.
- **Fill it with:** Do the same for Holy Light and Cleanse.
- **Why it works:** With no friend under the mouse it casts on your target. Fits any healer key.

### Holy Shock at the mob or yourself

```
#showtooltip Holy Shock
/cast [harm] Holy Shock; [@player] Holy Shock
```

- **Replaces:** Clicking yourself to heal with it while leveling.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** A hostile target gets the damage, anything else heals you. Holy leveling uses both sides of it.

## Prot-Ret and Shockadin

The hybrids.

### Holy Shock with Judgement

```
#showtooltip Holy Shock
/cast Judgement
/cast Holy Shock
```

- **Replaces:** The Judgement key, for Shockadin.
- **Frees:** One key.
- **Fill it with:** Exorcism.
- **Why it works:** Judgement is off the global cooldown. Prot-Ret plays Retribution's macros. From 56, when it takes Swift Judgement, add `/cast Swift Judgement` as the first line of the R macro (above the castsequence line): Swift Judgement is off the global cooldown, so one press fires both while it is ready, and 3, where the level guide puts it, goes free.
