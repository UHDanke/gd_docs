# Gameplay Arrow Trigger

Controls the direction the player is travelling towards.

## Arrow Direction

The directions the tips and base of the arrow point towards determine the following:
- The axis the player travels on
- Whether the sideways motion is reversed in classic mode
- Whether gravity is normal or inverted

The arrow trigger can be rotated by 90, 180 or 270 degrees and can be flipped along its X or Y axis in order to change its settings.

The arrow direction is always aligned to the level's XY axes. If the arrow trigger has a rotation non-divisible by 90, then it will use the default settings.

The arrow trigger will not update its rotation settings dynamically if the arrow trigger is rotated or scaled by another trigger.

All direction settings can also be set individually from the level's start settings.

### Rotation Axis

Controls whether the player travels along the X axis (horizontally) or along the Y axis (vertically). 

### Reverse Direction

Controls whether the player's position increases or decreases horizontally as it travels in classic mode. The default direction is positive (X/Y coordinate increases) while the reversed direction is negative (X/Y coordinate decreases).

### Gravity

Controls in what direction gravity is applied on the player. Normal gravity acceleration is negative (gravity applied towards negative X/Y), while inverted gravity acceleration is positive (gravity applied towards positive X/Y).

## Edit Velocity

**Edit Velocity** modifies the player's current X/Y velocity when the arrow trigger changes what axis the player travels on. 

By default, **VelMod X** & **Y** are multipliers, if **Override Velocity** is used then the player's current X/Y velocity is replaced by the given velocity.

**VelMod X** multiplies the player's vertical (relative to player) velocity. This option only works in platformer. 

For example, if the player jumps into an arrow trigger, the velocity from the jump will be multiplied by **Velmod X** and carry on as horizontal velocity. 

Horizontal velocity applied to the player will have reduced friction if **Dont Slide** is not selected.

**VelMod Y** multiplies the player's horizontal (relative to player) velocity. In this case if the player slides into an arrow trigger, the velocity from the slide is multiplied by **VelMod Y** and will carry on as vertical velocity (like a jump).

Both options do not take into account the player's gravity.

## Change Channel

Changes the player's current trigger channel to a new channel if selected, otherwise keeps the same channel.

If **Channel Only** is selected the trigger will only change the makes 

## Instant Offset

**Instant Offset** updates the camera's position instantly when direction is reversed if the player's position is offset from the camera's center. Otherwise, the camera will move twice (if ahead of the player, half if behind) the speed of the player until it reaches the new offset.

## Dont Slide

Prevents the player from sliding sideways on normal surfaces after a force is applied on the player by one of the edit velocity settings. This option works only in platformer mode.
