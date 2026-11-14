package hunter

// wow-forever patch (2026-11-13): Lacerating Strikes' bleed OVERWRITES in game (the user, 2026-11-12: "It overwrites in game": a new
// Mongoose Bite replaces the bleed and the damage it had not ticked yet). Upstream (sim/hunter/talents_survival.go,
// registerLaceratingStrikes, no source cited) rolls it like its Deep Wounds: the unticked damage is added to the new bleed, spread over a
// full set of ticks, the first application's timer kept. With Expose Prey a raid Survival hunter bites about every 5 s, so overwriting
// keeps about one of the bleed's seven ticks. WOW_FOREVER_LACERATING_ROLL=1 restores upstream's roll.

import "os"

var foreverLaceratingRoll = os.Getenv("WOW_FOREVER_LACERATING_ROLL") == "1"
