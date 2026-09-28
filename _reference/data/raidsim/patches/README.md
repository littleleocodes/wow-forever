# Local patches to the community simulator

`setup.py` builds the ElliotWood/Forever wowsims fork unchanged except for the files in `patches/forever/`, which it copies over the
clone before every build (`--rebuild`, `--update`, first setup), and the insertions listed in `patches/forever/edits.json`. An update
(`--update`) resets the patched files to the fork's version first, so `git pull` stays clean, and applies the patches again.

| Patch | Why | Since |
|---|---|---|
| `sim/mage/frostfire_bolt.go` + the `registerFrostfireBolt()` call in `sim/mage/mage.go` | The fork ships Frostfire Bolt as a stub ("To be implemented"); our version reads the spell from the client's spell store exactly like the fork's Fireball (cost, cast time, damage, coefficient, periodic tail, the frostfire school), so the talents that already name it (Improved Fireball, Hot Streak, Missile Barrage) apply. No rotation of the fork casts it, so every other result is unchanged. | 2026-09-28 |

Numbers from a patched spell are **our** model of the beta, not the community's: reports name the patch where a build casts it.
