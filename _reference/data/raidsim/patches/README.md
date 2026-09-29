# Local patches to the community simulator

`setup.py` builds the ElliotWood/Forever wowsims fork unchanged except for the files in `patches/forever/`, which it copies over the
clone before every build (`--rebuild`, `--update`, first setup), and the insertions listed in `patches/forever/edits.json`. An update
(`--update`) resets the patched files to the fork's version first, so `git pull` stays clean, and applies the patches again.

| Patch | Why | Since |
|---|---|---|
| `sim/mage/frostfire_bolt.go` + the `registerFrostfireBolt()` call in `sim/mage/mage.go` | The fork ships Frostfire Bolt as a stub ("To be implemented"); our version reads the spell from the client's spell store exactly like the fork's Fireball (cost, cast time, damage, coefficient, periodic tail, the frostfire school), so the talents that already name it (Improved Fireball, Hot Streak, Missile Barrage) apply. No rotation of the fork casts it, so every other result is unchanged. | 2026-09-28 |
| `sim/hunter/aspect_of_the_beast.go` + the `registerAspectOfTheBeastSpell()` call in `sim/hunter/aspects.go` | The fork models only Aspect of the Hawk and the ranged half of Deadly Aspects ("nothing a ranged hunter does would pick Beast"), so a melee hunter had no aspect and Deadly Aspects never procced for it. Adds Aspect of the Beast (+110 melee attack power, same exclusive aspect category as Hawk) and the melee half of Deadly Aspects (the client's triggered spell 1299448: 2%/rank per landed melee auto attack, +30% melee speed for 12 s), values from the client rows with the beta tooltips as fallback. No rotation but the melee hunter's casts it. | 2026-09-29 |

Numbers from a patched spell are **our** model of the beta, not the community's: reports name the patch where a build casts it.
