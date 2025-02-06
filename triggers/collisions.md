# Collision Objects
Used by Collision and Instant Collision triggers to implement collisions.  
Can be rotated, scaled or warped.  
**Block IDs** are limited between 0 and 9999.  
The **Dynamic** option allows collision objects to check collisions with other collision objects.	

## Collision Check

The collision state is updated every tick after all scheduled moves are processed, even if the position of the player or objects has not changed.  

Collision checks are done even if there is no active Collision trigger and they are always active even if the objects are off-screen.  

### Dynamic Order

Collision checks are done sequentially one dynamic target at a time in the following order:
- Player 1
- Player 2
    - Player-Player collisions are checked first
- Dynamic collision objects
  - Collisions are checked in the order the dynamic collision objects were placed
 
### Toggle

If an object is inactive, the collision check is skipped.

If a dynamic target is inactive, it will not check for collisions.

### Chunk Check

The grid is split into 100x100 chunks, starting from (0,0).

Collisions near a dynamic target will be checked in a 3x3 grid centered on the chunk that contains the dynamic target, collisions outside this area are ignored.

If the dynamic target's X position is less than 200, it will additionally check all chunks before X 200 regardless of Y position.

#### Chunk Order

Chunks are checked from bottom to top (towards Y positive), then left to right (towards X positive).

Collision objects within a chunk are checked in the order they were placed.

### Extended Collision

If a non-dynamic target uses Extended Collision, it will be checked by all dynamic targets regardless of chunk position.  

If the dynamic target uses Extended Collision, it will check all chunks.

### UI Trigger

Collision objects on the UI layer will only check for collisions with other UI objects.  
Players are unable to collide with UI collisions.

UI collisions are not divided in chunks, dynamic UI collisions will check all other UI collisions regardless of position.


# Collision Trigger
Toggles off a **Group ID** when collision blocks collide.  
With the **Activate Group** option, toggles on and spawns the given group instead.  
**P1** and **P2** options replace **Block ID1** with Player 1 and Player 2 respectively.  
**PP** replaces **Block ID1** with P1 and **Block ID2** with P2.  

## Activation
Collision activates on block collision, but before the collision state is updated.  
Due to this, if Instant Collision is called from a Collision trigger with the same **Block IDs** it will spawn the opposite group from the one expected.  
Collision only activates when the collision state of the Block IDs changes.
If placed before the level origin, Enter Collisions can activate when the level loads.

## Spawn Mechanics
Collision triggers can be spawn remapped and have spawn inheritance.  
The spawn order of Collision triggers depends on the order collisions are checked - which is affected by the Dynamic and Player options.  
If multiple triggers share the same **Block IDs**, spawn order is used. The order of **Block IDs** does not matter, **Block ID 1** and **2** are interchangeable.   
Collision triggers with the **PP** option activate after Player 1 and before Player 2 collisions.

# Instant Collision Trigger
Checks the current collision state of the given Block IDs and spawns True ID and False ID accordingly.

Can be remapped, but resets remaps when spawning other groups.

The collision state is only updated once per tick, Instant Collision does not check collisions, it checks what the last recorded collision state was.

# State Blocks

Spawns **State On** or **State Off** when colliding with the Player.
Can be considered a simpler, single object alternative to collision objects and triggers.
Collision checks are done individually per each object, as State Blocks do not use **Block IDs**.

State Blocks spawn groups independently even if sharing the same group IDs. However, as State Blocks cannot be remapped, if the target group contains a spawn trigger it will only activate once due to the spawn limit.

# Collision Schedule
* Collision (enter)
* State (on)
* Instant (Touch Trigger)
* State (off)
* Collision (exit)

# Interactions with Silent Move and Toggle
During collisions it is possible to prevent another collision that is yet to be processed from inside a Collision trigger by using an instant trigger like Toggle or Move (with the Silent option).  
This is only possible for enter collisions, collisions are not checked again during exit collisions.

Using Toggle or Silent Move with Instant Collision to do multiple checks per tick is not possible.

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

