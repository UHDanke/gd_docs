# Collision Objects

Used by Collision and Instant Collision triggers to implement collisions.
Can be rotated, scaled or warped, but not skewed.
**Block IDs** are limited between 0 and 9999.
The **Dynamic** option allows collision objects to check collisions with other collision objects.

## Collision Check

The collision state is updated every tick after all scheduled moves are processed, even if the position of the player or objects has not changed.

Collision checks are done even if there is no active Collision trigger and they are always active even if the objects are off-screen.

### Collision Schedule
* Collision (enter)
* State (on)
* Instant (Touch Trigger)
* State (off)
* Collision (exit)

### Dynamic Order

Collision checks are done sequentially one dynamic target at a time in the following order:
- Player 1
- Between players
- Player 2
- Dynamic collision objects
  - Collisions are checked in the order the dynamic collision objects were placed

### Toggle

If an object is inactive, the collision check is skipped.

If a dynamic target is inactive, it will not check for collisions.

### Chunk Check

The grid is split into 100x100 chunks, starting from (0,0).

Collisions near a dynamic target will be checked in a 3x3 chunk grid centered on the chunk that contains the dynamic target, collisions outside this area are ignored.

If the dynamic target's X position is less than 200, it will additionally check all chunks before X 200 regardless of Y position.

#### Chunk Order

Chunks are checked from bottom to top (towards Y positive), then left to right (towards X positive).

Collision objects within a chunk are checked in the order they were placed.

### Extended Collision

If a non-dynamic target uses Extended Collision, it will be checked by all dynamic targets regardless of chunk position.

If the dynamic target uses Extended Collision, it will check all chunks.

### Load Limit

A chunk can contain at most 7998 objects when the level is loaded, the level fails to play otherwise.

### UI Trigger

Collision objects on the UI layer will only check for collisions with other UI objects.
Players are unable to collide with UI collisions.

UI collisions are not divided in chunks, dynamic UI collisions will check all other UI collisions regardless of position.