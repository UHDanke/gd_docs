# Advanced Follow

Makes objects part of a group move towards a center object.

## Multiple Follows

Multiple Advanced Follow effects can be applied on the same objects and on different objects depending on **MaxRange**.

### Remap Instances

Spawn remapping can create multiple instances of the same Advanced Follow trigger.

Instances are unique for sets of **Target GID** and **Follow GID**, spawning a new instance with an already used combination of target and follow IDs will update the existing instance without replacing it.

### Priority

**Priority** decides the order in which Advanced Follow actions are applied, from highest first to lowest last.  
If there are multiple active instances with the same **Priority**, then spawn order is used (oldest first to newest last).

### Exclusive

If **Exclusive** is used, the processing of Advanced Follow actions on the given target is stopped after the exclusive action.  
Advanced Follow effects prior to the exclusive action are still applied.

**Exclusive** is applied on both X and Y even if **X** or **Y Only** is used.  
The only way to control the exclusive area of effect is with **MaxRange**.	

## Object Links

Advanced follow can use object and group links.  
The movement of the objects or object groups is done independently of one another.  
Linking rules are the same as for Area triggers, more information can be found in the Area documentation.

### Area Parent
The Area Parent is the object group's center for distance calculations and the center of rotation when using **Rotate Dir**.  
While Group Parents are also considered Area Parents if no Area Parent is present already, they are not used by Advanced Follow.

## Follow Center
**Follow GID** must be a single object, or have an ID Parent.  
If present, the ID Parent is used as the center.  
Group and Area Parents have no effect on the center.  
P1 and P2 positions, as well as C (bottom-left camera corner) can be used as the center.  

If no valid center exists, the Advanced Follow will not work.  
**Follow GID** can be identical to **Target Group ID**, but will only work if there is a valid follow center.  

## X and Y Only

X and Y Only limit the movement action of Advanced Follow to the X or Y axis.

Mode 1 actions

## Rotation

Rotation speed is limited to 0.5 rad/tick. This is not affected by timewarp values below 1.  

The rotation of the object is updated when entering the area of effect of the Advanced Follow.

Rotation is done independently by each Advanced Follow action.

**Rotation Offset** offsets the rotation's target angle by a value given in degres.  

**Rotate Easing** eases the rotation using the formula:

$nextRotation = \frac{(currentAngle-targetAngle)}{easing}$

The target's rotation is not updated if the target's distance from the follow center is less than **Rotate Deadzone**, given in small step units.

With **Mode 1** and **2**, the rotation follows the object's direction of movement.

**Mode 3** has the following changes to rotation:
- Rotation always aims at the follow center, rotation speed is also limited by the steering speed
- **Rotate Easing** and **Rotate Deadzone** have no effect

## Ignore Disabled

With Ignore Disabled, targets that are toggled off are skipped by Advanced Follow.

## Mode

Mode selects the movement mode of Advanced Follow.  
Available modes are:
- Easing (Mode 1)
- Acceleration & Friction (Mode 2)
- Steering & Breaking (Mode 3)

### All Modes

**Delay** adds a delay (in seconds) to the position of the follow center and the start of the Advanced Follow effect. 

**MaxRange** is the distance from center in (small step) units inside which the Advanced Follow effect is applied.  
If **MaxRange** is equal to 0, no distance limit is applied. If it's less than 0, then Advanced Follow will stop working.

**MaxSpeed** limits the target's speed to the given speed value.	
If **MaxSpeed** is less than or equal to 0, no speed limit is used. 

### Mode 1

**Mode 1** overrides the velocity based on the ratio of distance and Easing using the formula:

$Velocity=Distance/Easing$

As a side-effect, Edit Advanced Follow will not work on **Mode 1**.

### Mode 2

**Acceleration** is the multiplier of the target's acceleration. 1.00 **Acceleration** is equal to 0.01 increase in speed per tick.

**Friction** is the percentage of velocity lost every tick. Values of **Friction** are not limited - values below 0 and above 100 will increase the velocity exponentialy if there is no opposing force.  
Friction is applied prior to acceleration.

NearDist

With NearDist, the values of acceleration and friction depend on the distance 
NearFriction / NearAccel are the values

### Mode 2 & 3

**StartSpeed** is the value of the velocity applied, while **StartDir** is the direction's angle offset.

1.00 Speed is equal to one (small step) unit per tick. **StartDir** is defined in degrees going clockwise.

**StartSpeed** and **StartDir** have two boxes on the right side which can be used to define a reference ID for the direction of velocity.  
If there are multiple objects with the same reference ID, one is picked at random for each target.  
If the reference ID contains an ID parent, the ID parent is used as reference.  

If **StartSpeed** has a defined ID, the direction used is the direction of the last movement of the reference. **StartSpeed** is NOT a multiplier when a speed reference is used, it is a set speed value.

If **StartDir** has a defined ID and **StartSpeed** doesn't, the direction used is aimed towards the reference.

The object's default direction points upwards. The default is used if no reference IDs are defined, or if the reference returns no valid direction.

The behavior of **StartSpeed** depends on the options **Init**, **Set** and **Add**.  
If **Init** is used and this is the first action applied on the target, the object's velocity is set to **StartSpeed**.  
If **Set** is used and StartSpeed is different from 0, the object's velocity is replaced by **StartSpeed**.  
If **Add** is used, **StartSpeed** is added to the object's current velocity.  

Due to a bug, only one object per **Target GID** can be affected by **StartSpeed**.

### Mode 3

**SteerForce** is the multiplier of the max rotational speed applied on the object towards the follow center.  
1.00 **SteerForce** is equal to 0.01 radians / tick. Steering is done prior to braking and acceleration.

**SteerForceLow** / **SteerForceHigh** replaces **SteerForce** if the velocity of the object is strictly below / above **SpeedRangeLow** / **SpeedRangeHigh**. 

The target starts braking if the direction of movement and the direction towards the center are offset by more than **BreakAngle**.
If **BreakAngle** is above or equal to 180 degrees, the target will never brake. If it's below 0, it will be stuck braking.

**BreakForce** is the percentage of velocity lost every tick while braking, similar to friction in **Mode 2**.
Unlike friction, **BreakForce** is limited between 0 and 100 and acceleration is not applied while braking.

**SteerForce** , **SteerForceLow** and **SteerForceHigh** are not applied while braking - **BreakSteerForce** is used instead if the velocity of the target is equal to or below **BreakSteerSpeedLimit**.

In Mode 3, acceleration is applied in the direction of movement. With **Target Dir**, acceleration is applied towards the follow center like in Mode 2.

**SlowAccel** and **SlowDist** currently do nothing.

## Advanced Follow Update

Advanced Follow actions are processed after Follow Player Y, but before Follow and Area triggers.

Each action performs its motion calculation then executes the movement given by the result. 
They are done sequentially as dictated by Priority and spawn order. 
Positions are updated after each action and can be used by other Advanced Follow triggers right after.

If the target ends up not being under the effect of any Advanced Follow triggers, it loses all velocity on the next Advanced Follow update and can no longer be affected by Edit and Re-Target Advanced Follow.

### Velocity Duplication Bug

Multiple Advanced Follow actions on the same object are bugged and do not stack properly.  
Because each action executes the movement without checking if said velocity has been already applied on the target in the current tick, the same velocity is applied multiple times erronously. In other words, the object moves way faster than it should if there are multiple non-exclusive Advanced Follow triggers acting on the same object.  
This bug is shared across all modes of movement.  
The actions are done separately on each axis - two Advanced Follow triggers, one **X Only** and another **Y Only** will not duplicate the other's motion.  
This also applies to **Rotation**, which is more noticeable when using **Mode 3**.

## Pause and Resume

Pausing disables the Advanced Follow instance temporarily. Delays are not paused and continue to tick down while the trigger is inactive.  
The spawn order of the instance is kept when resuming.

# Edit Advanced Follow

Modifies the speed and direction of an Advanced Follow target.

## Target

Target GID is the group of the target. It does not have to be a group targeted by an Advanced Follow trigger, only a target that is under an Advanced Follow effect.  

The target must be a single object, the ID Parent of a group or the Area Parent of an object group.

Edit Advanced Follow will not work on a Mode 1 Advanced Follow trigger, as Mode 1 overrides the current velocity.

## Axis Modifiers

Mod X and Y multiply the current acceleration of the object on the respective axis prior to applying Speed.

With **X Only** and **Y Only**, only the Speed component VelocityX, respectively VelocityY is used.

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

The values of Mod X/Y, Speed and Dir can be randomized in a range using the +- boxes respective to each setting.  
The randomization is done individually per target everytime the trigger is activated.

## Target Control ID

If Target Control ID is selected, Target GID references the Control ID of one or more Advanced Follow instances. Edit Advanced Follow acts on all Target GIDs of the referenced instances.

## Remapping

All IDs, including the reference IDs, can be remapped.

## Timings

Edit Advanced Follow is instant, the reference values are taken at the time of spawning.  

The target must be under an active Advanced Follow effect in order for Edit Advanced Follow to work. This happens after an Advanced Follow action, not when the Advanced Follow trigger is spawned.

If an Advanced Follow has Delay, Edit Advanced Follow will not work if the Advanced Follow has not been active for at least the amount of Delay.

# Re-Target Advanced Follow

Changes the follow target of an Advanced Follow effect.

## Behavior

**Target GID** references one or more Advanced Follow triggers by **Group ID** or **Control ID** (if **Target Control ID** is selected).

The activation of Re-Target Advanced Follow is instant.

The trigger has no effect if **Follow GID** is 0.

Both **Target GID** and **Follow GID** can be remapped.


