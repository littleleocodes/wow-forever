# Local patches to the community simulator

`setup.py` builds the ElliotWood/Forever wowsims fork unchanged except for the files in `patches/forever/`, which it copies over the
clone before every build (`--rebuild`, `--update`, first setup), and the insertions listed in `patches/forever/edits.json`. An update
(`--update`) resets the patched files to the fork's version first, so `git pull` stays clean, and applies the patches again.

| Patch | Why | Since |
|---|---|---|
| `sim/mage/frostfire_bolt.go` + the `registerFrostfireBolt()` call in `sim/mage/mage.go` | The fork ships Frostfire Bolt as a stub ("To be implemented"); our version reads the spell from the client's spell store exactly like the fork's Fireball (cost, cast time, damage, coefficient, periodic tail, the frostfire school), so the talents that already name it (Improved Fireball, Hot Streak, Missile Barrage) apply. No rotation of the fork casts it, so every other result is unchanged. | 2026-09-28 |
| `sim/hunter/aspect_of_the_beast.go` + the `registerAspectOfTheBeastSpell()` call in `sim/hunter/aspects.go` | The fork models only Aspect of the Hawk and the ranged half of Deadly Aspects ("nothing a ranged hunter does would pick Beast"), so a melee hunter had no aspect and Deadly Aspects never procced for it. Adds Aspect of the Beast (+110 melee attack power, same exclusive aspect category as Hawk) and the melee half of Deadly Aspects (the client's triggered spell 1299448: 2%/rank per landed melee auto attack, +30% melee speed for 12 s), values from the client rows with the beta tooltips as fallback. No rotation but the melee hunter's casts it. | 2026-09-29 |
| `sim/core/no_racials.go` + the `noRacials()` check at the top of `applyRaceEffects` in `sim/core/racials.go` | Off by default. `WOW_FOREVER_NO_RACIALS=1` skips every racial effect (passives such as Tauren +1% hit and weapon specializations, on-use cooldowns such as Berserking, Blood Fury, Elune's Light), so specs and classes compare without the preset's race; the race's base stats stay. Test (full raid, 4,000 fights): Troll Frostfire mage -0.6%, Tauren Balance druid -1.1%, Troll melee hunter -0.3%. User preference 2026-10-07: as unbiased as possible | 2026-10-08 |

Numbers from a patched spell are **our** model of the beta, not the community's: reports name the patch where a build casts it.
