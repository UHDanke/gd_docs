## Durations

Triggers with a set **Duration** calculate their effects using time values ($TimeElapsed / Duration$).

Elapsed time increases by $1/TickRate$ seconds every tick.

Triggers last for $Duration \cdot TickRate$ amount of ticks, rounded up - the last tick limits the elapsed time so it doesn't overshoot the duration.

Example: a duration of 0.19 is proportional to 45.6 ticks, the trigger will last 46 ticks total with the last tick having a smaller change than the rest.
