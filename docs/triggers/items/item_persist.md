# Item Persist

Makes the item or timer given by **Item ID** persistent between attempts.

**Persistent** makes the target persistent if enabled and removes persistency if not. Targets continue to be persistent between attempts.

**Reset** resets the value of the target to 0. It does not clear timers.

**TargetAll** targets all persistent items or timers.

When persistent, items and timers keep all of their values and settings between attempts.
In the case of timers, this includes timer stop options and remaps.

Count triggers are not persistent between attempts, the Count's stored item value does not get updated on respawn if the Count was activated prior to the checkpoint. If the persistent item value changes after the checkpoint, the Count's stored value and item value will differ.

While timers are persistent, Time Event triggers are not.

Special items are not affected by Item Persist - Main time and Attempts are persistent, Points are not.