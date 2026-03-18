# Advanced Follow

## Velocity Duplication

**Version:** 2.208  
**Date:** 30/01/2026  

### Description
Targets move way faster than they should if there are multiple Advanced Follows active, because the velocity movement is mistakenly applied again by every trigger.  
  
Rotation is also duplicated when using Mode 3.

### Suggestions
A solution to this bug would be for only the first Advanced Follow in a tick to move by the current velocity value, and subsequent ones to move by the difference in velocity.

### Video
https://youtu.be/obZ-G22lizU

## Rotation and Object Groups

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Advanced Follow movement breaks when using Rotation on targets part of linked objects or groups.

### Video
https://youtu.be/KJJ2YNqvOO8

## Timewarp Movement

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Mode 1 Advanced Follow triggers with no easing follow the target using easing if timewarp is less than 1.  
  
The motion of Advanced Follow is inversely proportional with timewarp values less than 1. Due to how Mode 1 works, this multiplies the easing value of Mode 1 triggers, even if easing is equal to 0.  
  
This behavior makes it impossible to perfectly match an object's movement with Advanced Follow while time is slown down.  
This also affects Mode 2 movement that relies on moving objects for a single tick very fast with high speed and limited MaxRange or 100 Friction.

## Speedup when using high Friction values

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Friction values over 100 can reverse the speed of an object, and if above 200 friction this speed will increase exponentially until the game crashes.

## StartSpeed and Speed are not multipliers

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
StartSpeed and Speed are not multipliers when using a speed reference ID.  
It is not clear to me whether this is intentional or a bug, as the only place where the multiplier is mentioned is on the editor guide.

## Options that do nothing

**Version:** 2.208  
**Date:** 31/01/2026  

### Description
The following options do nothing:  
- MaxRange Reference ID  
- Redirect Dir (Edit AdvFollow)  
- SlowDist and SlowAccel (Mode 3)

## StartSpeed works on one target

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
If there are multiple targets inside Target GID, StartSpeed applies on one target only.

## Physics issues when stopping instantly

**Version:** 2.208  
**Date:** 30/01/2026  

### Description
When an Advanced Follow target loses all velocity instantly, if the player clips into the target's hitbox it will boost the player. This behavior continues until the trigger is stopped.  
Without DontBoostX/Y, the player's jump will be boosted everytime the player jumps off the target.  
Using DontBoostX/Y is not enough to fix this issue, the player will also be forcibly teleported to the top of the object if clipped inside or hit from below.

## Hitbox move delay

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Sometimes, the hitbox of the target object will be stuck in a previous position if Adv Follow movement is really fast.  
  
Stopping the Adv Follow trigger fixes the hitbox position.

## Mode 3 X/Y Only cannot steer if other modes are present

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
When using X/Y Only on a Mode 3 trigger, the target is unable to steer if Mode 1 or 2 is present on the other axis.

## Edit Advanced Follow random is between 0/+ instead of -/+

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
The random variables in Edit Advanced Follow are always picked in a range between 0 and the given value, unlike other random settings.

## Advanced Follow will not spawn if stopped then respawned in the same tick

**Version:** 2.207  
**Date:** 18/12/2025  
**Level ID:** 115061026  

### Description
If an Advanced Follow instance is stopped, then it is spawned again before the next Advanced Follow movement, it will not be active.  
  
This bug is caused by two mechanics:  
- Advanced Follow doesn't stop instantly, it is marked as stopped until the next scheduled movement where it gets cleared  
- Advanced Follow will not spawn if an instance of it is already active for the given remap

### Suggestions
A potential fix for this would be for Advanced Follow to replace the previous instance if its waiting to be stopped.

### Video
https://youtu.be/MNh11dOnu4U

## Timewarp Rotation

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
The max rotation speed of the Rotate option does not scale with timewarp.

## Near Dist slider

**Version:** 2.208  
**Date:** 02/01/2026  

### Description
Adv follow near dist slider has 0 to 1.00 range despite being a distance value like max range

## Unused Ignore GParent and Ignore Linked

**Version:** 2.208  
**Date:** 16/03/2026  

### Description
Ignore GParent and Ignore Linked are implemented for Advanced Follow triggers but the UI does not display the options.

### Workarounds
You have to edit the property through other means.
