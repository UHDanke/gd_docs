# Follow Player Y

This is a legacy trigger with most of its settings and features now found in Advanced Follow.

Advanced Follow Y works most similar to a Mode 1 Advanced Follow trigger that follows Player 1 on the Y axis.

## Mechanics

Advanced Follow Y works on individual objects only - it ignores ID Parents and object links.
It does not use velocities, so it will be treated like other moves by Advanced Follow triggers.

Advanced Follow Y movements are processed before Advanced Follow.

Advanced Follow Y can be instanced with spawn remapping and **Target Group ID** can be spawn remapped.
There can be only one follow player trigger active per **Target Group ID**, activating a new one will update the previous one's values.

## Settings

**Speed** controls the easing of the movement, to get the Advanced Follow equivalent use this formula:
$Easing(AdvFollow) = 4/Speed$

If **Speed** is equal to 4 or more then no easing is applied.

**Max Speed** limits the max movement speed of the target group. The value is 4 times higher compared to the Advanced Follow one, where:
$MaxSpeed(AdvFollow) = MaxSpeed/4$

**Delay** is equivalent to its Advanced Follow version.

**Move Time** is the duration of the trigger, after which it will stop.

**Offset** adds a vertical offset to Player 1's position.

**Move Time** and **Offset** are not found in Advanced Follow.