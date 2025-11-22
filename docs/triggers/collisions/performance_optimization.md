# Performance & Optimization

Generally, it doesn't make sense to stop or disable collision triggers for performance purposes, or to use Instant Collision instead for the following reasons:
- Collision triggers only activate on Collision ID state changes
- The overhead of Collision trigger instances being active (stored in memory) is very small and doesn't significantly affect performance on modern devices
- The main performance cost of Collision and Instant Collision triggers is spawning other triggers; Collision object checks are often the main reason for lag
- Collisions are checked every tick regardless of whether any Collision trigger is active
- Collisions are always active even if off-screen
- Collisions are not checked if the objects are not found in nearby chunks (unless Extended Collision is used)

Other bad attempts at optimization:
- Spawning thousands of individual Instant Collision triggers at once instead of using Collision Triggers, this is laggier as it spawns more triggers at once
- Trying to reinvent the wheel by disabling Collision triggers based on a player-made distance measurement, the game already limits the area collisions are checked in
- Replacing Collision triggers with Instant Collision spawn loops

What optimizations DO make sense, if necessary:
- Using as few dynamic objects as possible
- Toggling off dynamic collision objects when not in use
- Avoid placing collision objects before X 200
- Avoid overloading the UI layer with collisions
- Avoid using Extended Collision if the objects are not scaled up
- Avoid using Extended Collision on dynamic objects if the level has a large amount of collision objects
- Toggling off Extended Collision objects when not in use (if in above case)
- Toggling off non-dynamic collision objects when not in use (but generally not necessary)

When Dynamic needs to be used:
- Dynamic only dictates whether the collision object checks collisions with other collision objects, it has nothing to do with whether the collision object can be moved or not
- Dynamic does not need to be used for object-player collisions, as the player is already dynamic