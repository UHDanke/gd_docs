# Time Event

Spawns **TargetID** when the timer given by **ItemID** reaches the **TargetTime**.

## Activation

Time Event requires an active timer to work, which can be created with a Time or Item Edit trigger.

Time Event can be initialized even if the timer isn't active, and will continue to be active when the timer is cleared by Stop.

Time Event triggers do not spawn groups on their own, they assign extra groups for timers to spawn at the specified **TargetTime**.

Time Events store the timer's current value when checked. Unlike Count, pausing the Time Event does not prevent it from updating its value.

If a Time Event is initialized on an active timer, it will spawn instantly (even if the timer is paused) if:
- $(TimerMod > 0) \land (TargetTime > 0) \land (Time >= TargetTime)$
- $(TimerMod < 0) \land (TargetTime < 0) \land (Time <= TargetTime)$

### Spawn Mechanics
**ItemID** can be remapped.
Unlike Count triggers, Time Events are not ordered by **TargetTime**. If multiple Time Events with the same ItemID spawn in the same tick, spawn order will be used.

Since timers spawn the groups given by Time Event, the spawn behavior is not going to depend on the Time Event, but on the timer:
* The spawn target inherits the timer's remaps.
* The timer's spawn limit is applied to all extra groups added by Time Event.
* Time Events spawn after the corresponding timer, even if the Time Event was created before the timer.

Time Event triggers react in the same tick to timer value changes spawned by Time or Time Event triggers previous to them.