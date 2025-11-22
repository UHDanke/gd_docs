# Toggle

Toggles off objects, making them invisible and non-interactible.

## Behavior

Toggled objects are invisible and count as being inactive.

The player will not interact with toggled hitboxes, such as solid blocks, spikes or collision blocks.

### Collisions

Collision checks are skipped for toggled off collisions.

Dynamics will check their toggle state only once, prior to checking other collisions.

### Triggers

Toggled triggers will not activate.

Toggling off a trigger will only prevent it from activating, it will not stop it if it's already active.

Other triggers also toggle groups on or off, these are:
* Touch
* Count
* Collision
* Toggle Orb / Block
* On Death