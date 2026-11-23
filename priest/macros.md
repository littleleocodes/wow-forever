# Priest macros (hand-written)

[Priest](README.md) > Macros

Macro ideas for every priest spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these priest spells are: Inner Focus and Power Infusion. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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
- **Frees:** nothing: this fills a free key, Shift+C on your bars. It shares the healing potion's cooldown.

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

## Shadow

Leveling and raid. Keys below are your [Shadow keybinds](leveling/keybinds.md).

### The pull on one key

```
#showtooltip Shadow Word: Pain
/castsequence reset=target Vampiric Embrace, Shadow Word: Pain
```

- **Replaces:** Mouse 4 and 1.
- **Frees:** 1.
- **Fill it with:** 1 takes Flash Heal from 3, closer to your hand.
- **Why it works:** Both are on the global cooldown, so press Mouse 4 twice: Vampiric Embrace, then Shadow Word: Pain. A third press on the same mob would cast Vampiric Embrace again (a sequence returns to its first spell), so go back to Mind Blast and Mind Flay after two. Use it from 39, when Vampiric Embrace arrives. Until then keep plain Shadow Word: Pain.

### Out of Shadowform and heal

```
#showtooltip Flash Heal
/cancelaura Shadowform
/cast [@player] Flash Heal
```

- **Replaces:** Nothing: a variant for 3.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** You cannot heal in Shadowform, so this saves the click off the form. Click Shadowform back on afterward.

### Shield yourself, whatever you target

```
#showtooltip Power Word: Shield
/cast [@player] Power Word: Shield
```

- **Replaces:** Nothing: a variant for F.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** It never asks for a target and never lands on a friend by mistake.

### A wand that never turns itself off

```
#showtooltip Shoot
/cast !Shoot
```

- **Replaces:** Middle mouse, which holds Shoot.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Plain Shoot is a toggle, so a second press stops the wand, like the Attack button. The `!` keeps it on. A simple swap on the key you already use.

## Discipline

The Discipline raid healer. The Discipline leveling page levels in the same raid talents (healers level in their raid build): the shield macro works there too, while the leveling rotation spends **Inner Focus** on the pull's first spell rather than a heal. No Discipline build of ours takes Power Infusion, so there is no macro for it.

### Inner Focus into a big heal

```
#showtooltip Inner Focus
/cast Inner Focus
/cast [@mouseover,help,nodead][] Greater Heal
```

- **Replaces:** Inner Focus and one heal press.
- **Frees:** One key.
- **Fill it with:** Penance on a mouseover (the next macro, done for Penance).
- **Why it works:** Inner Focus is off the global cooldown.

### Shield whoever your mouse is on

```
#showtooltip
/cast [@mouseover,help,nodead][] Power Word: Shield
```

- **Replaces:** Clicking raid frames.
- **Frees:** Nothing.
- **Fill it with:** Do the same for Penance and Flash Heal.
- **Why it works:** With no friend under the mouse it casts on your target.

## Holy

Healing, and the Holy leveling page.

### Heal whoever your mouse is on

```
#showtooltip
/cast [@mouseover,help,nodead][] Flash Heal
```

- **Replaces:** Clicking raid frames.
- **Frees:** Nothing.
- **Fill it with:** Do the same for Renew and Greater Heal.
- **Why it works:** With no friend under the mouse it casts on your target.

### Inner Focus into a group heal

```
#showtooltip Inner Focus
/cast Inner Focus
/cast Prayer of Healing
```

- **Replaces:** Inner Focus and one group heal.
- **Frees:** One key.
- **Fill it with:** Dispel Magic on a mouseover.
- **Why it works:** Inner Focus is off the global cooldown.

## Smite

The Holy Fire and Smite damage build.

### The Smite pull on one key

```
#showtooltip Holy Fire
/castsequence reset=target Holy Fire, Shadow Word: Pain
```

- **Replaces:** The Holy Fire and Shadow Word: Pain presses at the pull (keys 2 and Mouse 4).
- **Frees:** Nothing: the rotation casts both again when their burn runs out, so keep them on their own keys for the recasts. It saves a press at the pull.
- **Fill it with:** Nothing.
- **Why it works:** Press it twice at the pull: Holy Fire, then Shadow Word: Pain. A sequence returns to its first spell after the last, so a third press on the same mob would cast Holy Fire again; after two presses go to Q (Smite) and Mind Blast on R. The build has no Penance.
