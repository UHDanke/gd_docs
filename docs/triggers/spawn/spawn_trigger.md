# Spawn Trigger

Activates a set of spawn-triggered triggers with the given **Group ID** instantly or after a **Delay**.

## Spawn Delays

The activation of Spawn triggers can be delayed by a value defined in seconds, up to 0.1 miliseconds in accuracy.

As the game processed delays in ticks and not in miliseconds, the delay is rounded up to the nearest tick.
In order to keep delays and loops consistent overtime, this additional delay is passed on further to other Spawn triggers.

The delay's value can be either positive or negative, and can also be offset randomly using the -/+ option.

### Timings

Delay is only applied if it is strictly bigger than 0, otherwise the Spawn trigger is instant.

Spawn delays are processed at the beginning of the tick, in the order they were spawned in.

If a Spawn delay (with positive value, not instant) is spawned by another Spawn delay, it will only be checked starting next tick.

### Delay Inheritance

If a Spawn trigger with delay is spawned by another Spawn trigger with delay, the new spawn will subtract the previous one's additional delay. This keeps chained delays and spawn loops accurate.

Negative delay values are also inherited and reduce the delay of further Spawn triggers by the same amount.
Leftovers from randomized delays (-/+ option) are not inherited.

Extra delays are not inherited by any other trigger except Spawn, so this leftover can be cleared if a trigger like Random or Item Compare spawns the next delay.

### Extra Spawn Limit

Triggers spawned when delays are processed will be able to spawn the same group once again in the same tick when activated again after the Spawn delay interval.

## Spawn Ordered

Spawn Ordered spawns triggers over time similar to ones placed on the timeline. Each spawned trigger has a delay depending on its position, relative to the base (1x) player speed.

This delay is calculated based on the object's X coordinate from the leftmost trigger in the group. The leftmost triggers are spawned instantly.

While triggers can be moved in order to change their delays, something not possible outside Spawn Ordered, this behavior is buggy and unreliable.