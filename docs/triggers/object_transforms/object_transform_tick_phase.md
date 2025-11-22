# Object Transform Tick Phase

Triggers that transform an object's parameters like position (including hitbox), rotation or scale are all (with one exception) scheduled - their effects are applied in a given consistent order.

Object Order
1. Keyframe
2. Scale
3. Rotate
4. Move
5. Follow Player Y
6. Advanced Follow
7. Follow
8. Area Scale
9. Area Rotate
10. Area Move

Object transform trigger activations prior to this tick phase are processed in the current tick, while those after are done in the next tick.

No spawns happen during this phase of the tick, keyframes spawn prior while collisions spawn after.

## Durations

Triggers with a set **Duration** calculate their effects using time values ($TimeElapsed / Duration$).

Elapsed time increases by $1/TickRate$ seconds every tick.

Triggers last for $Duration \cdot TickRate$ amount of ticks, rounded up - the last tick limits the elapsed time so it doesn't overshoot the duration.

Example: a duration of 0.19 is proportional to 45.6 ticks, the trigger will last 46 ticks total with the last tick having a smaller change than the rest.