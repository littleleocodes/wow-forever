package hunter

import "os"

// wow-forever patch (2026-10-08, ported to wowsims/forever 2026-10-18; patches/README.md). Since 2026-11-19 the simulator's own rule
// is the default again: a faster pet's swing damage is divided by its speed gain, so speed alone adds nothing a second. Upstream's
// evidence note EV-0071 (docs/evidence/EV-0071-hunter-cat-swing-level-30.md: one combat log of a level-30 Cat, 152 swings at 1.2 s,
// 42-55 at 119 attack power and 46-59 at 146) fits that rule and excludes ours, under which those swings would read about 70-92. Ours
// (2026-10-08 to 2026-11-19) kept the whole 2.0 s swing on a faster pet, from forum DPS comparisons at levels 20 and 30 that also carried
// the Cat's +10% and happiness; the independent audit's H15 retired it. WOW_FOREVER_PET_NORMALIZE=0 reproduces the old rule.
var foreverPetNormalizeSwitch = os.Getenv("WOW_FOREVER_PET_NORMALIZE") != "0"

func foreverPetNormalize() bool {
	return foreverPetNormalizeSwitch
}
