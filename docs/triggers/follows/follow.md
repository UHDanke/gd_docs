# Follow

Copies a target's movement on the X and Y axis for a set duration and applies it on another group.

## Settings

**X/Y Mod** multiply the followed movement on the X/Y axis.

**Move Time** is how long the follow will be active.

**Target Group ID** is the ID of the group that follows the movement of **Follow Group ID**.

## Mechanics

**Follow Group ID** must be a single object or contain a Group Parent ID. Follow will copy the target object's movement for the duration specified.

### Follow Order

Follow triggers are processed after all other movements but before Area triggers. As a result, it will copy all movements except the ones made by Area.

Another exception to this is Move Silent - Follow will not copy instant movements.

Follows will copy the movements of previous Follows based on spawn order.

### Remapping

**Target Group ID** and **Follow Group ID** can be spawn remapped.

For all Follow triggers there can only be one instance per unique combination of follow and target IDs.

Calling a new instance will update the X / Y Mod values of the active one and refresh the Move Time if it's longer than the remaining time.

### Duration

For compatibility with Scale, Rotate and Move which are delayed by one tick, Follow is active by an additional tick prior to stopping.

If Move Time is 0, then Follow will be active for 2 ticks.
