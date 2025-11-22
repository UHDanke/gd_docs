# Advanced Follow

## [2.207] Velocity Duplication
Targets move way faster than they should if there are multiple Advanced Follows active, because the velocity movement is mistakenly applied again by every trigger.

[Example Video](https://youtu.be/obZ-G22lizU)

Rotation is also duplicated when using Mode 3.

A solution to this bug would be for only the first Advanced Follow in a tick to move by the current velocity value, and subsequent ones to move by the difference in velocity.

## [2.207] Rotation and Object Groups

Advanced Follow movement breaks when using Rotation on targets part of linked objects or groups.

[Example Video](https://youtu.be/KJJ2YNqvOO8)

## [2.207] Timewarp and instant movement

### Instant Movement reduction
Mode 1 Advanced Follow triggers with no easing follow the target using easing if timewarp is less than 1.

The motion of Advanced Follow is inversely proportional with timewarp values less than 1. Due to how Mode 1 works, this multiplies the easing value of Mode 1 triggers, even if easing is equal to 0.

This behavior makes it impossible to perfectly match an object's movement with Advanced Follow while time is slown down.
This also affects Mode 2 movement that relies on moving objects for a single tick very fast with high speed and limited MaxRange or 100 Friction.

### Max Rotation Speed

The max rotation speed of the Rotate option does not scale with timewarp.

## [2.207] Speedup when using high Friction values

Friction values over 100 can reverse the speed of an object, and if above 200 friction this speed will increase exponentially until the game crashes.

## [2.207] StartSpeed and Speed are not multipliers

StartSpeed and Speed are not multipliers when using a speed reference ID.
It is not clear to me whether this is intentional or a bug, as the only place where the multiplier is mentioned is on the editor guide.

## [2.207] Options that do nothing

The following options do nothing:
- MaxRange Reference ID
- Redirect Dir (Edit AdvFollow)
- SlowDist and SlowAccel (Mode 3)

While a MaxRange reference ID has limited applications, one such example is with Mode 1 with 0 easing - this would allow you to move a singular object from a group to a target position (like a target move for objects), which is very useful.

## [2.207] StartSpeed works on one target

If there are multiple targets inside Target GID, StartSpeed applies on one target only.

## [2.207] Physics issues when outside MaxRange

Even if an Advanced Follow target loses all velocity by leaving the MaxRange of the effect, if the player clips into the target's hitbox it will boost the player. This behavior continues until the trigger is stopped.
Without DontBoostX/Y, the player's jump will be boosted everytime the player jumps off the target.
Using DontBoostX/Y is not enough to fix this issue, the player will also be forcibly teleported to the top of the object if clipped inside or hit from below.

## [2.207] Hitbox move delay

Sometimes, the hitbox of the target object will be stuck in a previous position if Adv Follow movement is really fast.
Stopping the Adv Follow trigger fixes the hitbox position.

## [2.207] Mode 3 X/Y Only cannot steer if other modes are present

When using X/Y Only on a Mode 3 trigger, the target is unable to steer if Mode 1 or 2 is present on the other axis.

## [2.207] Edit Advanced Follow random is between 0/+ instead of -/+

The random variables in Edit Advanced Follow are always picked in a range between 0 and the given value, unlike other random settings.

## [2.207] Advanced Follow will not spawn if stopped then respawned in the same tick

If an Advanced Follow instance is stopped, then it is spawned again before the next Advanced Follow movement, it will not be active.

This bug is caused by two mechanics:
- Advanced Follow doesn't stop instantly, it is marked as stopped until the next scheduled movement where it gets cleared
- Advanced Follow will not spawn if an instance of it is already active for the given remap

A potential fix for this would be for Advanced Follow to replace the previous instance if its waiting to be stopped.

[Video](https://youtu.be/MNh11dOnu4U)
ID: 115061026

## [2.207] Advanced Follow reversed spawn order

Advanced follow processing order for triggers with the same Priority is reversed on mobile.