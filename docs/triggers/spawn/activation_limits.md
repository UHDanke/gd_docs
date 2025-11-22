# Activation Limits

All triggers can be spawned multiple times per tick, but not all can activate or create multiple instances per tick.

### Spawn Limit

Without remaps, a spawn trigger can spawn the same group once per reset.
There are two resets per tick, before and after Spawn triggers with delay are scheduled.
As a result, you can activate the same spawn group from a single Spawn trigger twice per tick - one time from a Spawn trigger with delay, and another time from any other spawn.
While the applications of this are limited, having the option of a second activation per tick is very important for instanced spawn triggers like Count and Sequence, where otherwise each instance would only be able to activate once per tick which can interfere if the spawn is either on a timer or by player input.

With remaps, the spawn limit is applied separately for each remap origin.
The remap origin is the first remapped trigger in a spawn chain.
Whether the spawned trigger has any of its IDs remapped does not matter, it can be any remap.

#### Remap Resets

Triggers that reset remaps can spawn the same group only once per tick.
New remap origins can be assigned after a remap reset.

The remaps of a Spawn trigger with the Reset Remap option are reset before the Spawn trigger is spawned, so the Spawn trigger becomes the remap origin.
If the Timer has no remaps, Time Event will spawn the group without remaps.
Checkpoint and Instant Collision reset remaps.