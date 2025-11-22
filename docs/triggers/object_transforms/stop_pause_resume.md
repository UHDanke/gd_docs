# Stop, Pause & Resume

Stop is not instant for Animate Keyframe - if stopped, the keyframe animation is marked as stopped and will end once the keyframe is processed again, after spawning and applying object transforms.
This means the next keyframe change cannot be prevented by stopping.

Paused keyframes are skipped. Stopping while paused does not prevent the next activation, as you can Pause or Resume a keyframe animation that is marked as stopped, if it hasn't executed its last change yet.

## Options

Animate Keyframe will play all keyframe animations referenced by **Animate Group ID**. It does not matter which keyframe from a keyframe animation has **Animate Group ID**, or if multiple keyframes have the group ID - the keyframe animation will play once per **Animate Keyframe** activation, always from the start.

Keyframe animations apply on their own **Group ID** if **Target Group ID** is 0.

Keyframe scaling & rotation applies on the whole **Target Group ID** if either a GID Parent is present or a valid **Parent ID** exists, otherwise it applies individually to each object.

**Parent ID** must be unique (either single object or has a GID Parent) and needs to be present on an object that also has  **Target Group ID**, otherwise it is ignored.

The position of **Parent ID** is set at the activation of Animate Keyframe, it doesn't update when the keyframe animation moves the **Target Group ID**, so the resulting movement will be entirely different if the animation also scales or rotates the target.

## Modifiers

Modifiers can be used to change the parameters of all animated keyframes.

**Time Mod** multiplies all keyframe durations. Negative values multiply by 0.00 instead.

**Position X** and **Y Mod** multiply the keyframe's distances on the X and Y axes, where:
$NewPosition_i = Position_0 + (Position_i - Position_0) \cdot PositionMod$

If **Position Y Mod** is 0.00, it will copy the value of **Position X Mod**.

**Rotation Mod** multiplies keyframe rotations, where:

$$
NewRotation_i = (R_{i+1} - R_i) \cdot RotationMod + FullRotations +
\begin{cases}
  -360, & \text{if } (R_{i+1} - R_i) \cdot RotationMod > CW \cdot 180 \\
  360, & \text{if } (R_i - R_{i+1}) \cdot RotationMod > CCW \cdot 180 \\
  0, & \text{otherwise}
\end{cases}
$$

The calculation applies **Rotation Mod** incorrectly when determining how much the rotation should be offset:
- Rotations should not be multiplied by mod when comparing to CW or CCW.
- The resulting CW/CCW offset is not multiplied by **Rotation Mod**, when it should be.
- **Rotation Mod** does not multiply **x360** rotations, only keyframe object rotations.

**Scale X** and **Y Mod** multiply the keyframe's scales on the X and Y axes, relative to the first keyframe, where:

$NewScale_i = Scale_0 + (Scale_i - Scale_0) \cdot ScaleMod$