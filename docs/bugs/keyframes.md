# Keyframes

## [2.207] Keyframe movement is bugged if using a Parent ID in Animate Keyframe.

The parent's position is static when using a Parent ID inside the Animate Keyframe trigger, which results in bugged movement when scaling or rotating the keyframe.

## [2.207] Warp Skew of keyframes is ignored when animating the keyframe.

Only the X and Y scale of the keyframe is used for warping the target objects, skewing is ignored.

## [2.207] Keyframes merge when copying to another level

Keyframes have a hidden unique ID which is used to determine what keyframe objects are connected.
The ID is kept even when copying to another level which results in the copied keyframes combining with existing ones.
This makes merging parts of a level that use keyframes difficult, as you cannot manually select the unique ID of the keyframe.

## [2.207] Keyframe lines are not visible until reloading the level if pasted in a new level.

Keyframes copied to another level will not display the connecting lines until reloading the editor.

## [2.207] Animate Keyframe Position Y Mod cannot be 0 if Position X Mod is different than 0

If the value of Position Y Mod is equal to 0 when exiting the editor it will automatically copy the value of Position X Mod.
There are some cases where using only the X movement of a keyframe chain is required which is currently not possible to do outside of the editor.

## [2.207] Keyframe Preview does not match scaling
![image](https://github.com/user-attachments/assets/327217c9-e1fe-49f9-b0d2-ce96e51e3f39)

Keyframe scaling is relative to the Group Parent ID's rotation, which is not reflected in the preview where it is relative to the keyframe's rotation.

## [2.207] Rotation of Keyframe objects is not calculated properly

The formula by which keyframe rotation is calculated is very badly implemented and makes no sense.

The current rotation can be calculated using this formula:
$Rotation = RotDiff \cdot Mod + 360 \cdot (RotFull + Offset)$

$RotDiff = Rotation2 - Rotation1$

This formula was determined with the help of [this spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vRI6_MKs2LkhxcaZf5eHm9yHjoKrrWYV_CYWWmqYX1WSStsrk2KzQ-aHuTIghjF926q-KHWq2UaC63k/pubhtml).

Where:

*RotDiff* is the angle difference between the rotations of the first and second keyframe, going clockwise.

*Mod* is the Rotation Mod multiplier from the Keyframe trigger.

*RotFull* is the number of x360 rotations.

*Offset* is an additional x360 rotation that can be determined using this table:
| RotDiff | $RotDiff \cdot Mod$ | Direction | Offset |
| :---: | :---: | :---: | :---: |
| $>180$ | $>0$ | Any | \-1 |
| $>180$ | $<0$ | Any | 1 |
| $<=180$ | $>=360$ | None | \-1 |
| $<=180$ | $<=-360$ | None | 1 |
| $<=180$ | $>=360$ | CW | \-1 |
| $<=180$ | $<0$ | CW | 1 |
| $<=180$ | $>0$ | CCW | \-1 |
| $<=180$ | $<=-360$ | CCW | 1 |

The problems with this behavior are:
- If the angle between the two keyframes is over 180, then CW and CCW do nothing
- If the angle multiplied by Mod is more than a full rotation, CW and CCW do nothing
- If rotation Mod is negative then CCW becomes CW and vice-versa
- Mod multiplier doesn't work as expected with angles over 180, CW or CCW
- x360 rotations are not multiplied by Mod

Based on the above i propose this alternative formula to be used (possibly as a legacy option):

$Rotation = (Angle + 360 \cdot RotFull ) \cdot Mod$

Where Angle is:
| RotDiff  | Direction | Angle |
| :---: | :---: | :---: |
| $<=180$ | None | RotDiff |
| $<=180$ |  CW  | Rotdiff |
| $<=180$ | CCW | 360-RotDiff |
| $>180$ | None | 360-RotDiff |
| $>180$ |  CW  | RotDiff |
| $>180$ | CCW | 360-RotDiff |