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

Spawning the same Collision trigger again from the same remap while it is already active will do nothing.

### Interactions with Silent Move and Toggle
During collisions it is possible to prevent the activation another collision that is yet to be processed from inside a Collision trigger by using an instant trigger like Toggle or Move (with the Silent option).
This is only possible for enter collisions, this is not possible during exit collisions.

The toggle state of a dynamic collision object is checked only prior to its collision checks. As a result, toggling off the dynamic collision while it checks will not stop the Collision trigger from activating.

### Collisions spawning other collisions

Collision triggers spawned by other collision triggers can activate in the same tick as long as the collision state they are following hasn't been changed yet.

A collision trigger spawned by another collision trigger of the same type (enter, exit) and with the same set of block IDs will spawn in the same tick.

### Interactions with Stop

The spawn list of collision triggers is dynamic and can be changed during trigger activation.
When the state of a set of collision IDs changes, all Collision triggers with the same set of IDs for the respective state (enter, exit) are scheduled to activate, those triggers are then iterated through and spawned by index.

If you stop Collision triggers during that spawn, either by a Collision trigger stopping itself or another Collision trigger, the trigger list shrinks but the index is not updated.
This index mismatch can cause triggers that were not stopped and are yet to spawn to be skipped.

Paused Collision triggers are skipped. Pausing does not cause other triggers to be skipped.