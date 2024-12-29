# Advanced Follow

Makes objects part of a group move towards a center object.

## Multiple Follows

Multiple Advanced Follow effects can be applied on the same objects.
Since Advanced Follow acts on each object or object group independently of one another

### Remap Instances

Spawn remapping can create multiple instances of the same Advanced Follow trigger.

Instances are unique for sets of **Target GID** and **Follow GID**, spawning a new instance with an already used combination of target and follow IDs will update the existing instance without replacing it.

### Stacking Effects

Multiple Advanced Follow actions on the same object are bugged and do not stack properly.	
Each action is multiplied by the total number of actions applied on the target, regardless of mode.
For example, three **Mode 2** actions on the same object with Acceleration 3 will apply an acceleration of $3\cdot 3 = 9$. One **Mode 1** with Easing 100 and One **Mode 2** with Acceleration 3 will apply both easing and acceleration twice each.
This also applies to **Rotation** when using **Mode 3**.

### Priority

Priority decides the order in which Advanced Follow actions are applied, from highest first to lowest last.
If there are multiple active instances with the same Priority, then spawn order is used (oldest first to newest last).

### Exclusive

If Exclusive is used, the processing of Advanced Follow actions on the given target is stopped after the exclusive action.
Advanced Follow effects prior to the exclusive action are still applied.

**Exclusive** is applied on both X and Y even if **X** or **Y Only** is used.	
The only way to control the exclusive area of effect is with **MaxRange**.	

## Object Links

Advanced follow uses object and group links.
The movement of the objects or object groups is done independently of one another.
Linking rules are the same as for Area triggers, more information can be found in the Area documentation.

### Area Parent
The Area Parent is the object group's center for distance calculations and the center of rotation when using **Rotate Dir**.	
While Group Parents are also considered Area Parents if no Area Parent is present already, they are not used by Advanced Follow.

## Follow Center
Follow GID must be a single object, or have an ID Parent.
If present, the ID Parent is used as the center.
Group and Area Parents have no effect on the center.
P1 and P2 positions, as well as C (bottom-left camera corner) can be used as the center.

If no valid center exists, the Advanced Follow will not work.
Center Group ID can be identical to Target Group ID, but will only work if there is a valid follow center.

## Rotation

Rotation speed is limited to 0.5 rad/tick. This is not affected by timewarp values below 1.

Rotation Offset offsets the rotation's target angle by a value given in degres.

**Rotate Easing** eases the rotation using the formula:

$nextRotation = \frac{(currentAngle-targetAngle)}{easing}$

The target's rotation is not updated if the target's distance from the follow center is less than **Rotate Deadzone**, given in small step units.

For Mode 1 and 2, the rotation follows the object's direction of movement.

Mode 3 has the following changes to rotation:
- Rotation always aims at the follow center, rotation speed is also limited by the steering speed
- The target angle is initialized to point towards the follow center when entering the area of effect of the advanced follow 
- **Rotate Easing** and **Rotate Deadzone** have no effect

## 


# Bugs
