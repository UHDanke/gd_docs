

# Documentation Issues

## P1/P2/C (Pages 78, 85)

![image](https://github.com/user-attachments/assets/6632f1de-3f88-41f5-ac7a-ee58d92176dc)
![image](https://github.com/user-attachments/assets/276f3814-e8ee-41ec-9ad0-a58720809a22)

**C** is the bottom-left corner of the screen, not the center.

## Rotation Offset (Page 78)

![image](https://github.com/user-attachments/assets/27dee7db-8dce-447b-8d24-1635c360a102) 

Using *left* and *right* is understandable and gets the idea across (if you know the default direction) but not correct, should be replaced by *counter-clockwise* and *clockwise*.

## Init (Page 78)
![image](https://github.com/user-attachments/assets/80529fb5-9076-4480-908d-7949ca17f2bf)

This definition is alright if you know that a target under no Advanced Follow has no velocity values, but it seems to imply that an object affected by Advanced Follow with 0 velocity will be set to StartSpeed when using Init, when that is not the case.

## Set (Page 78)
![image](https://github.com/user-attachments/assets/31547429-4c1b-4fca-809f-fa18909eaebc)

Set will not override the current velocity if StartSpeed is equal to 0.

## Delay  (Pages 79, 80)
![image](https://github.com/user-attachments/assets/b5daa52a-a337-49d5-93a5-09b872d71f42)

This definition is incomplete - the position of the follow center is also delayed.

## MaxSpeed (Pages 79, 80)
![image](https://github.com/user-attachments/assets/24593595-6893-4f2d-8c2b-b82d28312f52)

Leaving MaxSpeed at 0 doesn't limit speed, it makes it unlimited.

## MaxRange (Pages 79, 80)
![image](https://github.com/user-attachments/assets/de58dcba-86f0-4257-9a13-eb2200af2eb9)

Only mentioning start of movement implies the target will continue to follow when exiting MaxRange, which isn't the case - MaxRange is the radius in which the Advanced Follow effect is applied, exiting this range removes all target velocity.

## Easing (Page 79)
![image](https://github.com/user-attachments/assets/16a6e0b6-f46c-4a92-a06c-1c7839fa63a7)

This definition is wrong, easing is applied at all times.  
I don't have a good way to describe this easing outside of mentioning the velocity equation ($Velocity=Distance/Easing$).

## NearFriction and NearAccel (Page 81)
![image](https://github.com/user-attachments/assets/a3ae08a5-ea9d-41ad-97e2-b3ea498b4449)

These definitions imply NearFriction and NearAccel replace Friction and Acceleration when inside NearDist but that is not the case - the values of acceleration and friction vary between normal and near values linearly, based on the distance of the target from the follow center divided by NearDist.

## StartDir
![image](https://github.com/user-attachments/assets/edb86c48-d543-4434-93b9-975d58f2683f)

StartDir offsets the angle when using a direction reference ID.

## Direction Reference (Pages 81, 83, 85)

![image](https://github.com/user-attachments/assets/f1d001f1-4dad-41ae-8def-82a9faaf493c)

StartSpeed is never a multiplier, it is a set value even when using a speed reference; only the movement direction is copied.

## Target Dir (Page 83)

![image](https://github.com/user-attachments/assets/7d64c91c-8588-4a04-a9ce-2c694abec8c4)

The definition of Target Dir is filler and doesn't explain anything concrete. Target Dir makes the object accelerate towards the follow center (like in Mode 2), without it acceleration is done in the direction of movement.

## Re-Target Advanced Follow Target GID
![image](https://github.com/user-attachments/assets/242405cb-c5e5-48c4-960d-97347e3ba932)
![image](https://github.com/user-attachments/assets/7e3a56d0-473b-43fe-927a-c0156cc50dc7)

For Re-Target Advanced Follow, Target GID is the group ID of an Advanced Follow trigger, not the Target GID of Advanced Follow.

## SteerForceLow/High
![image](https://github.com/user-attachments/assets/4cd1f96b-a241-4759-bfb9-a24e41fe6374)

This is straight up wrong, steerforce settings have nothing to do with MaxRange, the trigger doesn't even work on targets outside that range.  
SteerForceLow / SteerForceHigh replaces SteerForce if the velocity of the object is strictly below / above SpeedRangeLow / SpeedRangeHigh.

## BreakAngle
![image](https://github.com/user-attachments/assets/b0238496-0fff-4a2e-b09c-91fbfb0754d7)

This could use clarification as to what angle its talking about.  
The target starts braking if the angle between the direction of movement and the direction towards the follow center (where the target goes and where it wants to go, to put it another way) is higher than BreakAngle - in other words its how much the target tolerates going in a different direction before its forced to brake and steer itself towards the center. 

# Bugs

## [2.207] Velocity Duplication
Targets move way faster than they should if there are multiple Advanced Follows active, because the velocity movement is mistakenly applied again by every trigger.

[Example Video](https://youtu.be/obZ-G22lizU)

Rotation is also duplicated when using Mode 3.

A solution to this bug would be for only the first Advanced Follow in a tick to move by the velocity value, and subsequent ones to move by the difference in velocity.

## [2.207] Rotation and Object Groups

Advanced Follow movement breaks when using Rotation on targets part of linked objects or groups.

[Example Video](https://youtu.be/KJJ2YNqvOO8)

## [2.207] Timewarp

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

## [2.207] Camera position is updated after move

The movement of an Advanced Follow with the C option will be delayed by one tick from the position of the camera, as the camera position is updated after all moves are processed.
This also affects Area triggers and Move (Lock Camera).

## [2.207] Mode 3 X/Y Only cannot steer if other modes are present

When using X/Y Only on a Mode 3 trigger, the target is unable to steer if Mode 1 or 2 is present on the other axis.  

## [2.207] Edit Advanced Follow random is between 0/+ instead of -/+

The random variables in Edit Advanced Follow are always picked in a range between 0 and the given value, unlike other random settings.

# Suggestions & Additions

## AdvFollow Ignore Timewarp

Add **Ignore Timewarp** option to Advanced Follow. When used this would ensure high speed movement isn't affected while slowing down time.

## Edit AdvFollow Mod X and Mod Y reference ID

Add a reference ID besides Mod X and Mod Y, to allow the speed to be modified on the X or Y axis of a reference object. This would allow for accurate bounce physics off slopes or angled lines which is currently very difficult to do.

## Speed Multiplier

If speed not being a multiplier is intentional, a **Speed Multiplier** option should be added to allow for that behavior.  
While it takes an extra workaround, this would allow the implementation of accurate collision motions between solid physics objects.  
Additionally, any kind of movement could be converted to advanced follow speed values with this feature.

## Edit AdvFollow Use Dir
Add **Use Dir** option so the object's current direction is used for direction calculations.  
With Speed this would allow adding speed in the direction of movement without using an individual reference ID for each target.  
If Redirect Dir worked, you could use Dir to offset the direction of movement by a set amount of degrees.
