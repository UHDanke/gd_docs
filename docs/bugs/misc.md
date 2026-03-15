# Misc

## Start Position 60hz

**Version:** 2.207\
**Date:** 18/12/2025\

### Description
Start Positions simulate the game at only 60hz, while the tick rate in 2.2 is 240hz. While this seems intentional, an option to enable 240hz start positions would be nice to have.

## Camera position is updated after move

**Version:** 2.207\
**Date:** 18/12/2025\

### Description
The movement of an Advanced Follow with the C option will be delayed by one tick from the position of the camera, as the camera position is updated after all moves are processed. This also affects Area triggers and Move (Lock Camera).

## Object Rotation Offset

**Version:** 2.207\
**Date:** 18/12/2025\

### Description
The position of objects part of a group that is being rotated will get offset overtime. All rotation transformations are affected except Area Rotate.

## Rotate Aim / Follow infinite rotation

**Version:** 2.207\
**Date:** 18/12/2025\

### Description
When using Dynamic Mode with Aim or Follow options, on a Target Group ID without a Group ID Parent and a Center Group ID that is either 0 or made up of multiple objects, the target objects will spin rapidly. If Center Group ID contains multiple objects (and no Group ID Parent), it will spin even faster. [Video 1](https://youtu.be/uE5I8bRaMSg) [Video 2](https://youtu.be/GkujxqE5pok)

## Relative Scale doesn't work with Scale 0.00

**Version:** 2.207\
**Date:** 18/12/2025\

### Description
This isn't so much a bug as it is an oversight, Scale trigger will not work if scale is either 0 or 1. Relative Scale lets you mimic additive scaling (increasing scale by an amount relative to current amount) if target and center have the same scale. Due to the formula offseting scale by -1 ($RelativeScale=1+(Scale-1)/CenterScale$), increasing the scale by 1 needs a scale factor of 2. In order to decrease the scale by -1, Scale would have to be 0 which doesn't work.

## Color resumes when respawning from a checkpoint if stopped

**Version:** 2.207\
**Date:** 18/12/2025\

### Description
If a Color trigger is stopped with a Stop trigger before the color change finishes, the color change will resume when you respawn from a checkpoint. Pausing the Color trigger does not do this.

## Negative scaled Teleport triggers apply force in the opposite direction

**Version:** 2.207\
**Date:** 18/12/2025\

### Description
Flipping a Teleport trigger by scaling it with a negative value does not change the direction force will be applied towards. Flipping the trigger with the editor tool changes the direction, but: - If the teleport has target group 0, flipping will flip the direction force is applied in - If the teleport has a target group, the target group's rotation is used as reference for force, flipping does nothing even if you flip the tp or the target obj

## Kerning is not used properly when splitting text

**Version:** 2.207\
**Date:** 18/12/2025\

### Description
Using the split feature of text objects does not take kerning into account properly, with certain letters getting more offset. This also depends on the game's texture quality, with High quality having more significant offset than Low.

## No Audio Scale Orbs scale more than they should if affected by a scaling trigger

**Version:** 2.207\
**Date:** 18/12/2025\

### Description
Orb objects with No Audio Scale that have been scaled up by an Area / Scale trigger will be much bigger visually than they should (roughly same size as when clicked), if they are not affected by any enter effect.

## Out of bounds crash

**Version:** 2.208\
**Date:** 30/01/2026\

### Description
If an object moves out of bounds and cannot be added to a section, the game crashes.
