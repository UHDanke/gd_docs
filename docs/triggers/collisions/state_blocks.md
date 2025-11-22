# State Blocks

Spawns **State On** or **State Off** when colliding with the Player.
Can be considered a simpler, single object alternative to collision objects and triggers.
Collision checks are done individually per each object, as State Blocks do not use **Block IDs**.

State Blocks spawn groups independently even if sharing the same group IDs. However, as State Blocks cannot be remapped, if the target group contains a spawn trigger it will only activate once due to the spawn limit.