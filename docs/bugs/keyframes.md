# Keyframes

## [2.207] [18/12/25] Scale of Keyframe Parent ID is always positive

The scaling applied on keyframes by the Keyframe Parent ID is always positive, even if the scale is negative.

## [2.207] [18/12/25] Scale of Keyframe Parent ID is not relative to rotation and is applied after it

If a Keyframe Parent ID has different X & Y Scale and Rotation at the same time, rotation is always applied first then Scale X / Y is applied along the level's X / Y axis, not relative to the object's rotation.

## [2.207] [18/12/25] Warp Skew of keyframes is ignored when animating the keyframe.

Only the X and Y scale of the keyframe is used for warping the target objects, skewing is ignored.

**## [2.207]** Keyframes merge when copying to another level

Keyframes have a hidden unique ID which is used to determine what keyframe objects are connected.
The ID is kept even when copying to another level which results in the copied keyframes combining with existing ones.
This makes merging parts of a level that use keyframes difficult, as you cannot manually select the unique ID of the keyframe.

## [2.207] [18/12/25] Keyframe lines are not visible until reloading the level if pasted in a new level.

Keyframes copied to another level will not display the connecting lines until reloading the editor.

## [2.207] [18/12/25] Animate Keyframe Position Y Mod cannot be 0 if Position X Mod is different than 0

If the value of Position Y Mod is equal to 0 when exiting the editor it will automatically copy the value of Position X Mod.
There are some cases where using only the X movement of a keyframe chain is required which is currently not possible to do outside of the editor.

## [2.207] [18/12/25] Keyframe Preview does not match scaling
![image](https://github.com/user-attachments/assets/327217c9-e1fe-49f9-b0d2-ce96e51e3f39)

Keyframe scaling is relative to the Group Parent ID's rotation, which is not reflected in the preview where it is relative to the keyframe's rotation.

## [2.207] [18/12/25] Rotation of Keyframe objects is not calculated properly

The formula by which keyframe rotation is calculated is very badly implemented and makes no sense.

The current rotation can be calculated using this formula:
$rmod = (Rc-Rp)*mod$

$rmod > CW*180 -> offset = -360$  
$-rmod > CCW*180 -> offset = 360$  
$rotation = rmod + offset$

Where:
Rc is the current key's rotation  
Rp is the previous key's rotation  
mod is the keyframe animate's rotation mod  
rotation is the resulting rotation  

Where is the mistake? mod is not applied correctly - it should be applied on offset but not when comparing to CW or CCW

How the formula should look to get correct behavior at any mod:  
$Rc-Rp > CW*180 -> offset = -360$  
$(Rc-Rp)*-1 > CCW*180 -> offset = 360$  
$rotation = (Rc-Rp+offset)*mod$  

Minimal modifications to robtop's equation (this is equivalent to above):  
$rmod = (Rc-Rp)*mod$  
$rmod > CW*180*mod -> offset = -360$  
$-rmod > CCW*180*mod -> offset = 360$  
$rotation = rmod + offset*mod$  

The problems with the current behavior are:
- If the angle between the two keyframes is over 180, then CW and CCW do nothing
- If the angle multiplied by Mod is more than a full rotation, CW and CCW do nothing
- If rotation Mod is negative then CCW becomes CW and vice-versa
- Mod multiplier doesn't work as expected with angles over 180, CW or CCW
- x360 rotations are not multiplied by Mod

## Curve Keyframes with 0 duration break keyframe movement

Keyframes using Curve mode with very low duration like 0 result in very exaggerated movement that can send objects out of bounds, crashing the game.

Duration 0 should instead disable curve mode on the affected keyframe.

