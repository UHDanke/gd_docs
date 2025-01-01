



# Documentation Issues

## P1/P2/C (Page 78)

![image](https://github.com/user-attachments/assets/6632f1de-3f88-41f5-ac7a-ee58d92176dc)

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

# Delay  (Pages 79, 80)
![image](https://github.com/user-attachments/assets/b5daa52a-a337-49d5-93a5-09b872d71f42)

This definition is incomplete - the position of the follow center is also delayed.

# MaxSpeed (Pages 79, 80)
![image](https://github.com/user-attachments/assets/24593595-6893-4f2d-8c2b-b82d28312f52)

Leaving MaxSpeed at 0 doesn't limit speed, it makes it unlimited.

# MaxRange (Pages 79, 80)
![image](https://github.com/user-attachments/assets/de58dcba-86f0-4257-9a13-eb2200af2eb9)

Only mentioning start of movement implies the target will continue to follow when exiting MaxRange, which isn't the case - MaxRange is the radius in which the Advanced Follow effect is applied, exiting this range removes all target velocity.

# Easing (Page 79)
![image](https://github.com/user-attachments/assets/16a6e0b6-f46c-4a92-a06c-1c7839fa63a7)

This definition is wrong, easing is applied at all times.  
I don't have a good way to describe this easing outside of mentioning the velocity equation ($Velocity=Distance/Easing$).

# NearFriction and NearAccel (Page 81)
![image](https://github.com/user-attachments/assets/a3ae08a5-ea9d-41ad-97e2-b3ea498b4449)

These definitions imply NearFriction and NearAccel replace Friction and Acceleration when inside NearDist but that is not the case - the values of acceleration and friction vary between normal and near values linearly, based on the distance of the target from the follow center divided by NearDist.

![image](https://github.com/user-attachments/assets/edb86c48-d543-4434-93b9-975d58f2683f)

StartDir offsets the angle when using a direction reference.

# Direction Reference (Page 81, 82)

![image](https://github.com/user-attachments/assets/f1d001f1-4dad-41ae-8def-82a9faaf493c)

StartSpeed is never a multiplier, it is a set value even when using a speed reference; only the movement direction is copied.


![image](https://github.com/user-attachments/assets/7d64c91c-8588-4a04-a9ce-2c694abec8c4)
