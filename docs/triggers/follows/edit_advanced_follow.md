# Edit Advanced Follow

Modifies the speed and direction of an Advanced Follow target.

## Target

Target GID is the group of the target. It does not have to be a group targeted by an Advanced Follow trigger, only a target that is under an Advanced Follow effect.

The target must be a single object, the ID Parent of a group or the Area Parent of an object group.

Edit Advanced Follow will not work on a Mode 1 Advanced Follow trigger, as Mode 1 overrides the current velocity.

## Axis Modifiers

Mod X and Y multiply the current acceleration of the object on the respective axis prior to applying Speed.

With **X Only** and **Y Only**, the trigger will only edit the velocity of the given axis.
This is also the case if the target is affected by Advanced Follow on one axis only.

## Speed and Dir

**Speed** and **Dir** settings share the same behavior with **StartSpeed** and **StartDir**.

Unlike **StartSpeed**, **Speed** is always additive and is not limited to one object per **Target GID**.

**Redirect Dir** currently does nothing.

### Velocity

The velocity of the targets can be calculated using the following formulas:

$VelocityX = Speed*cos(TargetDirection+Dir)$

$VelocityY = Speed*sin(TargetDirection+Dir)$

$Velocity = (CurrentVelocityX)*ModX+(CurrentVelocityY)*ModY+VelocityX+VelocityY$

## Random Values

The values of Mod X/Y, Speed and Dir can be randomized in a range using the -/+ boxes respective to each setting.
Contrary to what the option says, random values are picked in the 0/+ range, not -/+.
The randomization is done individually per target everytime the trigger is activated.

## Target Control ID

If Target Control ID is selected, Target GID references the Control ID of one or more Advanced Follow instances.
Edit Advanced Follow acts on all targets that have at least one of the Advanced Follows' Target GIDs.

## Remapping

All IDs, including the reference IDs, can be remapped.

## Timings

Edit Advanced Follow is instant, the reference values are taken at the time of spawning.

The target must have been under an active Advanced Follow effect during the previous tick in order for Edit Advanced Follow to work.

If an Advanced Follow has Delay, Edit Advanced Follow will not work if the Advanced Follow has not been active for at least the amount of Delay.