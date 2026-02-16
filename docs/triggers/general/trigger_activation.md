# Trigger Activation

Triggers have three main ways they can be activated from:
- Timeline (default)
- Touch (touch trigger option)
- Spawn (spawn trigger option)

All three options are normally mutually exclusive, but touch and spawn properties can be forced at the same time if the object's string is edited.

## Timeline

Timeline triggers activate when the timeline moves past the trigger's position.

The game attempts to activate on every tick all timeline triggers that:
- have not been activated yet
- are on the same trigger channel as the timeline
- are placed before the timeline, relative to the timeline's movement

If multiple timeline triggers activate at the same time, their activation order matches the timeline's direction of movement (ex: left to right movement -> triggers activate left to right). If two triggers share the same position relative to the timeline (so if timeline moves left to right, same X position), they will activate in the order they were loaded in.

Timeline triggers can attempt to activate only once. Toggled off triggers will not activate and cannot be activated again even if toggled back on.

In classic mode the timeline matches the main player's position, while in platformer mode the timeline moves at a fixed speed (normal) and direction (left to right) starting from the origin of the level, regardless of any gameplay changes as the player is able to move freely.

### Order

**ORD** is made to enforce an activation order for triggers placed on the timeline, but as of 2.208 it does not work as intended. 

Currently, if a trigger uses **ORD** it's activation is delayed until all triggers with a lower **ORD** in the entire level are activated.

## Touch

Touch triggers activate when the player collides with the trigger's hitbox.

Can only activate once if **Multi Trigger** is not selected, however if multiple players collide at the same time it will activate once for each collision. Single PTouch changes this behavior - when selected only the first player collision will activate the trigger, the rest are ignored.

If the player collides with multiple touch triggers the activation order depends on the collision order.

Toggled off triggers will not check for collision.

## Spawn

Spawn triggers activate when spawned by another trigger by a given **Group ID**.

Can only activate once if **Multi Trigger** is not selected.

Spawn triggers within a group activate in order from left to right, if multiple triggers share the same horizontal position they activate in the order they are loaded.

Toggled spawn triggers will not be spawned.

## On Load

Start Position, UI and Link Visible activate and apply their effect when the level loads the objects.

The effect of On Load triggers cannot be stopped and is active for the remaining of the current attempt.


On load triggers have no additional effect if spawned, touched or activated by the timeline.

The order of on load triggers is strictly the order the triggers are loaded in, ignoring the trigger's position.

On Load triggers activate before timeline or touch triggers activate, so it is not possible to prevent their activation using triggers. The only way to prevent an On Load trigger from activating is if using LDM and the trigger is marked as High Detail.