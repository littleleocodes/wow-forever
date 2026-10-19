package hunter

import "os"

// wow-forever patch (2026-10-08, ported to wowsims/forever 2026-10-18; patches/README.md): Forever does not normalize a pet's damage
// per hit by its attack speed. The client's Faster Attack passives (spells 1263099-1263114, build 70291) raise a 2.0 s base speed and
// change nothing else, and forum measurements at levels 20 and 30 put a 1.2 s cat 42% and a faster wolf 26-30% ahead of a 2.0 s pet
// with the same attack power. The official simulator divides the swing's damage by the speed gain ("a faster swing deals less a
// swing"); this keeps the swing's damage whole. WOW_FOREVER_PET_NORMALIZE=1 restores the simulator's rule.
var foreverPetNormalizeSwitch = os.Getenv("WOW_FOREVER_PET_NORMALIZE") == "1"

func foreverPetNormalize() bool {
	return foreverPetNormalizeSwitch
}
