# Animate Keyframe

Animates keyframes from **Animate Group ID** on objects from **Target Group ID**.

## Options

Animate Keyframe will play all keyframe animations referenced by **Animate Group ID**. It does not matter which keyframe from a keyframe animation has **Animate Group ID**, or if multiple keyframes have the group ID - the keyframe animation will play once per **Animate Keyframe** activation, always from the start.

Keyframe animations apply on their own **Group ID** if **Target Group ID** is 0.

Keyframe scaling & rotation applies on the whole **Target Group ID** if a GID Parent is present, otherwise it applies individually to each object.

### Parent ID

If a **Parent ID** exists, the movement applied by the keyframe will be transformed by the parent's scale and rotation. If the target is affected by the same scale and rotation as the parent, then the animation's movement will be relative to the parent.

For example, when the parent is scaled by 2 and rotated by 180 degrees then the movement applied by the keyframe will be doubled and go in the opposite direction. If the target and parent rotate or scale around the same center, then any animation on the target will be relative to the rotation or scaling.

**Parent ID** must be unique (either single object or has a GID Parent), otherwise it is ignored.

Scale is separated on X and Y and skew X/Y is ignored. Scaling is applied prior to rotation and is not relative to the parent's rotation, different X/Y scales combined with rotation will have unexpected effects as a result.

The reference value of scaling is absolute, it will always be positive even if the parent's scaling is negative.

The scale and rotation of the parent will update dynamically, but will not be updated by other triggers within the same tick. 

### Modifiers

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

## Activation

Keyframe parameters are set at the moment of activation - changes to the rotation, scaling and position of keyframes after activation are ignored.

Unlike Move, Scale and Rotate, Animate Keyframe does not have a one tick delay.

## Movement Order

If multiple keyframe animations are present on the same target, there are three factors that determine the order they are applied in, from highest priority to lowest:
- Transformation Order: If one of the keyframes of an animation is scaled, then this animation applies before animations where one of the keyframes rotates but does not scale, which in turn also apply before animations that do not scale or rotate (Scale -> Rotate -> Position).
- Activation Order: If multiple Keyframe Animate triggers activate and they have the same transform order, the application order depends on the order the Keyframe Animate triggers were activated in.
- Load Order: If multiple keyframe animations are activated from the same **Animate ID** and they have the same transform order, the application order depends on the order the keyframes with the target **Animate ID** are loaded in

## Spawning

Keyframes can spawn even if no **Group ID** or **Target ID** is defined.

All keyframe spawns happen prior to affecting objects.

If Animate Keyframe is spawned by a keyframe, it'll activate in the same tick. Spawns with **Duration** 0.00 will spawn in the same tick, after the current spawns end, in order of activation.

Spawn limits are determined per keyframe object, not Animate Keyframe triggers.

**Animate Group ID**, **Target ID** and **Parent ID** can be remapped.

The **Group IDs** and **Spawn IDs** of keyframe objects cannot be remapped, but keyframe spawns inherit remaps from Animate Keyframe.

## Stop, Pause & Resume

Stop is not instant for Animate Keyframe - if stopped, the keyframe animation is marked as stopped and will end once the keyframe is processed again, after spawning and applying object transforms.
This means the next keyframe change cannot be prevented by stopping.

Paused keyframes are skipped. Stopping while paused does not prevent the next activation, as you can Pause or Resume a keyframe animation that is marked as stopped, if it hasn't executed its last change yet.
