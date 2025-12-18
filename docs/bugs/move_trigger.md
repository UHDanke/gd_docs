# Move Trigger

## [2.207] [18/12/25] Move Trigger Target Dynamic ignores X and Y Only

Move (Target Mode) options X and Y Only are ignored when using dynamic movement.

## [2.207] [18/12/25] Move Trigger Camera Lock X axis bugs on level replay

While the checkpoint / practice bug was fixed, restarting after completing a classic level places the camera locked group in the wrong position for that attempt.
This only happens if the Move trigger is placed left or ontop of the level origin.

## [2.207] [18/12/25] Pausing a Move trigger stops objects without a hitbox based on frames instead of ticks

Pausing a Move trigger stops the movement of objects, but objects without a hitbox are stopped on the next visual frame instead of the next tick.

This causes objects without a hitbox (spikes, solid blocks, collision objects) to offset from the position of objects with one (decoration, or using no touch).

Resuming undoes the offset.

Stopping does not create an offset, however stopping after pausing makes the offset permanent.

All other triggers with move functionality (rotate, scale, keyframe, etc) do not share this issue.

The reason this happens is that movements are optimized for decorative objects - they only move every frame rather than every tick. Pause fails to take this into account hence the offset.

If the deco object is targeted by adv follow / rotate / scale / other triggers that work on obj then the deco object will no longer be optimized and move every tick instead. 
