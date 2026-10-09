package hunter

// wow-forever patch (2026-10-09): no off-hand hit bonus while Raptor Strike is queued. In Classic, any queued on-next-swing attack let
// the off-hand's white swings skip the 19% dual-wield miss penalty; Blizzard's beta notes of 2026-10-01 (us.forums.blizzard.com/en/wow/
// t/2360696) remove it for warriors: "Queueing Heroic Strike will no longer increase off-hand hit chance", and the fork applies that to
// Heroic Strike and Cleave only. Raptor Strike is the same mechanic, so we assume the fix covers it (our reading: Blizzard named only
// Heroic Strike). Raptor Strike's own hit rolls the special attack table, which never pays the penalty. WOW_FOREVER_RAPTOR_QUEUE_HIT=1
// restores the fork's rule (comparisons).

import "os"

func foreverRaptorQueueHit() bool {
	return os.Getenv("WOW_FOREVER_RAPTOR_QUEUE_HIT") == "1"
}
