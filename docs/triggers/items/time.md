# Time

Creates timers which can be used to keep track of elapsed time or activate groups after a given delay.

## Options

**StartTime** overrides the previous value of the timer.

**StopTime** pauses the timer and spawns **Target ID** when the stop value is reached. This option is ignored if the tickbox is unselected.

The timer gets set to the stop value if it goes over the stop point. The timer will not stop if it starts or is unpaused from or past the stop value.

**TimeMod** modifies the timer multiplier. The default multiplier is 1.00. If **TimeMod** is 0.00 then the timer is unable to spawn groups.

**Ignore Timewarp** is currently bugged and has no effect.

**Start Paused** pauses the timer.

With **Dont Override**, **StartTime** is ignored when updating the timer (but it is used as the start value when creating a timer).

## Timers

Time triggers create global timer instances, which are shared by **Item ID**. Timers store all of the Time trigger's groups, properties and remap information.

Activating a Time trigger while there is an already active timer for the given Item ID updates the timer with the trigger's settings and groups.

Timers update every tick, 240 times a second. Only timers initialized before the first timer spawn in the tick will be updated in the same titick. If a new timer is initialized during or after timer activation, it will be processed in the next update.

**TargetID** for Time triggers can only spawn if the timer crosses the **StopTime**, using Item Edit for this purpose will not work. This does not apply to Time Event triggers.
The value of timers is checked prior to Time and Time Event trigger spawns.

Unlike Count which is bi-directional, timers are one-directional and this depends on the value of **TimeMod**:
* For $TimeMod \gt 0$ **Target ID** is spawned if $previousValue \lt StopTime \le currentValue$.
* For $TimeMod \lt 0$ **Target ID** is spawned if $previousValue \gt StopTime \ge currentValue$.

### Assignment

Unlike Item Edit, timers are not limited between -9999999.00 and 9999999.00.

### Spawn Mechanics

Timers are processed in reversed spawn order.

All IDs can be spawn remapped. For remap inheritance, the timer instance stores the remaps.

Remaps can only be set when creating a timer instance, updating a timer will not update the remaps. Updating the timer does not change the timer's spawn limit.

## Stop, Pause and Resume

Stop triggers stop, pause or resume a timer given by group or control ID.

Resume will not resume a timer stopped by Time Control or Start Paused, and Time Control will not resume a timer stopped by Pause.

Stopping the timer clears all settings, remaps and current value.