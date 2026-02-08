# Spawn Order

The activation order of triggers is the order they were spawned in, also known as the spawn order.
By default, this is applied horizontally from left to right. If multiple triggers share the same horizontal position, they will activate in the order they were placed in.

The following triggers have additional ordering mechanisms which are applied before spawn order:

### Count

First ordered by Target Count in ascending or descending order depending on whether the last item change increased or decreased the value.
Count activates after every Pickup or Item Edit trigger with the Item option, even if the value remains the same. In this case ascending order is used.
If Target Count is the same, spawn order will be used.

### Time

Activation order is different between platforms - on Steam they have normal spawn order, on Android their spawn order is reversed.

### Time Event

Activation order depends on the spawn order of Timer triggers for different Item IDs.
If Item IDs are identical, spawn order is used.

### Collision

Activation order depends on the order collision objects are checked.
Player collisions are checked before dynamic collisions.
If two collision triggers share the same collision IDs, spawn order is used. The order of the IDs does not matter.

### Area Triggers

Priority is applied first, from highest first to lowest last.
If Priority is the same, spawn order is used.

### Advanced Follow

Priority is applied first, from highest first to lowest last.
If Priority is the same, spawn order is used.

## Spawn Schedule

While some spawns activate instantly, most of them are scheduled and activate in a specific order throughout the game tick.

Instant spawns

* Spawn
* Count
* Instant Count
* Instant Collision
* Item Compare
* Random
* Advanced Random
* Sequence
* End
* Checkpoint (Spawn)

Scheduled spawns (in order)

1. Checkpoint (Respawn)
2. Spawn (delay)
3. Toggle Orb/Block
4. Event
5. Touch
6. Timer & Time Event
7. Keyframe
8. Collision (on enter)
9. State (on enter)
10. Instant (touch triggered)
11. State (on exit)
12. On Death
13. Instant (from timeline)
14. Collision (on exit)
