# Misc

## [2.207] [18/12/25] Start Position 60hz

Start Positions simulate the game at only 60hz, while the tick rate in 2.2 is 240hz.
While this seems intentional, an option to enable 240hz start positions would be nice to have.

## [2.207] [18/12/25] Camera position is updated after move

The movement of an Advanced Follow with the C option will be delayed by one tick from the position of the camera, as the camera position is updated after all moves are processed.
This also affects Area triggers and Move (Lock Camera).

## [2.207] [18/12/25] Object Rotation Offset

The position of objects part of a group that is being rotated will get offset overtime.

All rotation transformations are affected except Area Rotate.

## [2.207] [18/12/25] Rotate Aim / Follow infinite rotation

When using Dynamic Mode with Aim or Follow options, on a Target Group ID without a Group ID Parent and a Center Group ID that is either 0 or made up of multiple objects, the target objects will spin rapidly.
If Center Group ID contains multiple objects (and no Group ID Parent), it will spin even faster.

[Video 1](https://youtu.be/uE5I8bRaMSg)
[Video 2](https://youtu.be/GkujxqE5pok)

## [2.207] [18/12/25] Relative Scale doesn't work with Scale 0.00

This isn't so much a bug as it is an oversight, Scale trigger will not work if scale is either 0 or 1.

Relative Scale lets you mimic additive scaling (increasing scale by an amount relative to current amount) if target and center have the same scale.

Due to the formula offseting scale by -1 ($RelativeScale=1+(Scale-1)/CenterScale$), increasing the scale by 1 needs a scale factor of 2.

In order to decrease the scale by -1, Scale would have to be 0 which doesn't work.

## [2.207] [18/12/25] Gradient doesn't account for screen rotation when loading the level

Gradient triggers without any references (ID 0) use the screen's edges as reference instead.
These edges are initialized when the level loads, however, if the camera trigger is placed before the origin camera rotation isn't taken into account.

Example:
![image](https://github.com/user-attachments/assets/e2baf11d-2f0b-45e5-bbc9-e15dc3fd271e)

## [2.207] [18/12/25] Color resumes when respawning from a checkpoint if stopped

If a Color trigger is stopped with a Stop trigger before the color change finishes, the color change will resume when you respawn from a checkpoint.
Pausing the Color trigger does not do this.

## [2.207] [18/12/25] Negative scaled Teleport triggers apply force in the opposite direction

Flipping a Teleport trigger by scaling it with a negative value does not change the direction force will be applied towards.

Flipping the trigger with the editor tool changes the direction, but:
- If the teleport has target group 0, flipping will flip the direction force is applied in
- If the teleport has a target group, the target group's rotation is used as reference for force, flipping does nothing even if you flip the tp or the target obj

## [2.207] [18/12/25] ORD doesn't work as intended

Triggers that use ORD are delayed until the last (either the left-most or top-most, if gameplay is rotated) trigger with a lower ORD in the same channel is activated.

## [2.207] [18/12/25] Kerning is not used properly when splitting text	

Using the split feature of text objects does not take kerning into account properly, with certain letters getting more offset.

This also depends on the game's texture quality, with High quality having more significant offset than Low.
