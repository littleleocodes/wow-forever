package core

import "os"

// wow-forever patch (2026-10-08): WOW_FOREVER_NO_RACIALS=1 skips every racial effect (passives such as Tauren's hit, weapon
// specializations, and on-use cooldowns such as Berserking, Blood Fury, Elune's Light), so specs and classes compare without the
// race the simulator's preset picked. The race's base stats stay. Off by default: the community simulator's behavior.
var noRacialsSwitch = os.Getenv("WOW_FOREVER_NO_RACIALS") == "1" // read once at program start

func noRacials() bool {
	return noRacialsSwitch
}
