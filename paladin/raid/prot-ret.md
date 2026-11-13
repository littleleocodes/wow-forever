# Prot-Ret Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Prot-Ret

*Retribution's melee talents with Protection's Seal of Fury, Swift Judgement and Toughness: a melee split short of 30 Retribution points.* (a hybrid: Protection/Retribution).

**[Prot-Ret — Raid](../research/raid/builds/prot-ret-ml-raid.md)** (10/12/29) — [open the talent tree](https://talentsforever.com/paladin/60/05005-552-3523310100130034-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Retribution — Seal of Command), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Seal of Command**.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**; no global cooldown, so press it alongside the others
2. **Hammer of Wrath** when the target is below 20% health
3. **Consecration**
4. **Holy Strike**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Retribution Aura**: put it up at the start and keep it up
- **Seal of the Crusader**: put it up at the start and keep it up

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Holy | 10 | Divine Strength 5, Improved Seals 5 |
| Protection | 12 | Divine Intellect 5, Redoubt 5, Precision 2 |
| Retribution | 29 | Deflection 3, Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Vindication 1, Seal of Command 1, Sacred Arbiter 1, Two-Handed Weapon Specialization 3, Vengeance 3, Champion of the Light 4 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 682 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 677 | [10/12/29](https://talentsforever.com/paladin/60/05005-513110001-1423330110130034-12) |
| Phase 1 BiS | 682 | [10/12/29](https://talentsforever.com/paladin/60/05005-552-1523330100130034-12) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.7; Phase 1 BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) · *quest: Falrin's Vendetta* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Highlander's Lamellar Greaves](https://www.wowhead.com/forever/item=20049) · *sold by Samuel Hawke*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsFNcZ3n92dvb4X6+9PvgyPhiYbjHY2647M4sr6gJebNpyqdWtUQuVUMvYO/YuXe+4M2vLvFRuRWkbESLlJQFFJuKSICuECBIJWeGFJBLhySgRREgk1uYliohC/MDDPkTRzHq9F3wJCijnwTr+z7//5Tvn+/5dbCEQABEkaIPDkIBRmAT4H8CrABcBaLVzytmnW4HdbSJ8gGMTKJC5ATHrQ54cvwTIk1NfBtBLpmYD4m0BveS9t2vFz2vQS25cAPG+vZl6DcQzXuTJJ5cAveSbN8H+uJfcfgXEz2qQJ88/CCBPXp4NoJu8fgh58s6sHfL9CyA+qEEX8uTqbCDYEbiZbJv/u/xoIHbnJDwH3LHki8A9GjgNwjntDe3ezmnwnkhOX4STyTk4luwhTvkQhRlOkjtluTPcqUQURZZlJaxsUSORiKwoshKR5ciWmxyf5e434GZcmwURG3cOZpLjWkaXNMtKDqf1uKSNmVqQoIB8WJUtlLB+GuqwNidUI8bGUinJ1NLDeonHRmzOQiPWx0x9VNqvaynJGJJ6jZERLR0PetGD7nDEwp/jhiy0ICvz6k8OJzK6MWaldcsKVqEXPWGlo9PCdmzJQjM29WpWpljakbH4sD6ipzMlrnQjC2JNsBpxnnjR00bI/VgWatHfZ4zrUsaQRvSUrtNm1oT+nIBIDvxWGh7TzDgTkCeXp8AJsD7UQgTKdblYfU6ow9pdeko7KvVpRwxT6t1ldbloD4viFqZic6iJAPWd5ggKbW5y+TrYgZCTLWwIrSFu6pn3csTNHHzkDtVii440Rf+qjab+ZoxmJFVWfxlW5HBE6ZIGEzaicckwJS0e1+PSwFEpk9Al08homaSRlixdMwcTUpul65KpZ8LxUStcOAznDzuOWEa6naGTzUPePQf092wvdtPtFW2jP+jDqrOw0D2uywkMxb02spKpa6mkNSKNmkZGH7SjswKktJX9FJtyQj3S/QljLBWXTH3I1K2EtN/oXUh67Rys5NbvuBHywRTQNawuCzVY3WukLX3QdNqktcyfBUTymwnDHExaI6I71LrcC6U+VuUU5yHXY6Fdy74U2s4249qcIGLjbs1awsEpSiAfT0FocOk3TPexPbid/ho3BNetGArFnNCAa/5k6ZUhigCFzsNKHKD/AfZvwHGaWT3b+pywFptLs5WFQoX9AluCbPmqsDboR1+W2MUBeekMFC8o9ClfyaCHwL4CPAH0/7ByXaURsY/tW6GAYFBatY3FcC9MxvJEz3Je9IwY47pCDxU2DdNAMZAT/OjrswmfVynqN31YNU8KVCeLpPcGPeie4V20wBj78daYZTJC7wD7CNCi/1i5YVsayqC0K63EdpWrKG9MLTSm/tDG8nSrbGwS2D8xQpXVH1l5XRH6u8LmSeuqKCEUL/KcHmR/xn10jyOgHuq5wS0KqDMM6kK1tjgPuGzCo1uRWytFzKnyLBSC235tArkVCyUrJOYv7MDTzbQot2pwOQypEz9jjunqhiUvv8ShdQUmlLg1Pzah6MIQUutLp3Teqnaq9eW35EE3Qqe6rTgWqEw7HFSEigGmWAVzCVhyh2Kpx7mlZgH9GuiDp877LrYVffeERapiO92MvitQNIihRsJT30zRxPIPCaNsx+P0/BltR/89AQvOYj6CQH03gNjf4P4bE4E5OCmrzEj11lJA9NOrHH2Lc7Kv1upjWlFW6g627Ql1fFnsHDUoxS5vKMPOMRWw+yP7w/eQthIwnU8vgAkFMO8WwYysBmbP8md0U2gj4WnVdIGNrOEKRwlHq856CxZb07/gbsJDTv2X2+Ws+ugM8MihK/gtV2UbXJND0ebTp+z1YfdPhpx1p1ud40Re6g5d41w/yspEC7tnujZdemZ5fuX87T8f3blgiB62f2SdAucf11x3yE2uNfWU/BaTYStEYTfE4CAkYBQmYIL7bgDiugOX); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsE1ca9j8ej09+x4lzyGVyCDDrJZB419nxGK/YLBCTsLtcNqob1EIl1DKJJ7Gp40lnnBReqrSiV1GQ2ocWHkLFpUVRKRX0AUWlD7SVKE9UrWiFRBu5fagqqtI88OCHqppxHF/Ipaignofo5D+//8t3zvf9NrYQ8IEIErTBXkjACIwDvATwFsAZAFptn3LW6Xpg15oI7+PY0yiQ6X4x60GefH8EkCdHf/Shm0xc84mfC+gmH39QK35Xg25y+TSIN63NxNsgHncjT74+C+gmv7wH1scF8qYhfluDPPnotBXm1Vs+dJJ39iBPDr5u+X1yGsRbNehAnly45vN3+K4k22aelO/0x64fhleAO5h8Dbg7/cdAOKm+q97YPAnuQ8nJM3A4OQ0Hk93Erh6iMMUxOSLLkWAkogRDESUcDsshWQ6FZTm87grHZ7mbDbgWl2dBxMbNA5nkmJrRJNU0k0NpLS6po4bqJyggH1RkEyWsn4Q6rM0J1Yix0VRKMtT0kFbisRqbs9CI9TFDG5F2ampK0gelHn14WE3H/W50oTMYNvHvuCoLLcjKvPqSQ4mMpo+aac00/VXoRlcw1BExsR1bstCMTT2qmSmWtm80PqQNa+lMiStdzfxY469GnCFudLURcjOWhVr09upjmpTRpWEtpWm0mTWhNycgkl3/lYZGVSPOBOTJuQmwA6wMtBCBcp0OVp8T6rB2i5ZSD0i96j7dkHq2mJ0O2s2iuI4p2BxoIkA9xziCQpuTnLsEViDkZBMbAsuIk7pm3BxxMhsfuUMx2ZwjTdHH1ZHUE/pIRlJk5Z/BkBwMhzqlgYSFaFzSDUmNx7W41H9AyiQ0ydAzaiappyVTU42BhNRmappkaJlgfMQMFg6D+cOOfaaebmdoZ3ORD08C/T/bjl10Y0Xb6PV7sOoEzHaPK3ICQ3G7haxkaGoqaQ5LI4ae0Qas6KwAKW1lf8WmnFCPdGdCH03FJUMbNDQzIe3Ue2aTXjwJi7n12W6EfDoBdBmry0INVvfoaVMbMOw2aS3zZgGR/Ge/bgwkzWHRGWhd6IVSD6uyi3ORS7HAlgVfCm1na3F5ThCxcatqzuNgFyWQLycgMDD/G6Y72DbcSP+Nq/wrFg2FYk5owGWPmFpliCJAgVOwGAfo88CeAxyjmaWzrcwJy7G5NFtZKAyxf2CLny1cFdb6vejJEqs4IG8ch+IFBb7hKxl0G9hPgIeAvgyL11UaEXvZjkUK8PulJduYC3dkPJYnepZzo2tYH9NCdE9h0zAJFH05wYueXovweZWiXsODVTOkQHUyR3q334XOKd5BC4yxHm+NUSYj9DqwLwBN+tTiDVvSUAalVWkltktcRXljSqEx5Y82lqdbZWPjwJ7BMA0t/cjK6wrT/xU291pXRQmBeJHndDd7FHfQbbaAuqjrMjcnoPYwqAvUWuLc77AIj86Q3FopYnaVJ6AQ3PJrE8jVWCBZITGPsV33N9Oc3Cr+hTCkdvyMMaopq+a9/BKH1kWYUOLWfNeEorNDSKkvndJ5qxJR6stvyYVOhIiyoTgWqEw7bFSEigEWMgvmErDkjpCpvMDNNwvoz0Bv3Xfed7L16LkhzFEV2+la9JyHokEMNBKeeqaKJpZ/SBhlm+6m599oO3pvCFhwFvMRBOq5DMT66vZiTARm4xRaYkYqV+cDoo9e4Oj7nJ19qVbv0oqyUjexDfeo4wtiZ6tBKXZ5Qxl2tqmA3cPsod8hbSVg2p+eBRMKYH5VBDO8FJjdC5/RNYHVhKdVkwU2sobzHCUcrTrhLlgsTf+BuwK3OeVZp8Ne9dEp4JFDh/9XrsoyOMYHo83Hjlrrs66/DNrrepcyzYm81BW4yDn+lJWJFnYPdK05+8Dy/Mv+23cqunnWEN1r/bo6CvY/jumugJNcbOou+REmw3qIwlaIwW5IwAjsh/3cbwMAElQBsw==).

## Other builds of this spec

- [Retribution — Seal of Command](../research/raid/builds/ret-full-buffs-raid.md) (8/15/28, 652 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/05003-053020005-1523330100130033-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-13 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

