# Advanced Follow

Makes objects part of a **Target GID** move towards a center object given by **Follow GID**.


## Follow Center

**Follow GID** must be a single object, or have an ID Parent. If present, the ID Parent is used as the center.

Group and Area Parents have no effect on the center.

P1 and P2 positions, as well as C (bottom-left camera corner) can be used as the center.

If no valid center exists, the Advanced Follow will not work.

**Follow GID** can be identical to **Target Group ID**, but will only work if there is a valid follow center.


## Velocity

All Advanced Follow effects internally use velocity to control the movement of the targets.

This velocity is separated on the X and Y axis.

One unit of **Speed** is equal to 1 unit (1/30th of a block) of movement done per tick (1/240th of a second), which is equivalent to 8 blocks per second (240 units in 240 ticks).

### Advanced Follow Stacking

If multiple Advanced Follow effects are active on the same target, the target will move faster than intended.

For example, if a target has 10 velocity on the X axis and is affected by multiple Advanced Follow effects that do not change the target's velocity, all Advanced Follow effects will move the target by 10 units each (when only the first one should apply the movement). So for 3 follow effects, the object will move by 30 units every tick instead of 10, 3 times faster than intended.

This also applies to **Rotation**, which is more noticeable when using **Mode 3**.

### Movement with Rotation

Rotation affects the velocity of the target in some cases and can cause movement to duplicate or velocity to not apply properly if done from **Edit Advanced Follow.


## Movement Updates

Advanced Follow actions are done after Follow Player Y, but before Follow and Area triggers.

Each action performs its motion calculation then executes the movement given by the result. They are done sequentially as dictated by **Priority** and spawn order.

Positions are updated after each action and can be used by other Advanced Follow triggers right after.

If the target ends up not being under the effect of any Advanced Follow triggers, it loses all velocity on the next Advanced Follow update and can no longer be affected by Edit and Re-Target Advanced Follow.

### Priority

**Priority** decides the order in which Advanced Follow actions are applied, from highest first to lowest last.

If there are multiple active instances with the same **Priority**, then spawn order is used (oldest first to newest last).

### Exclusive

If a target has an **Exclusive** Advanced Follow effect, all Advanced Follow effects that are processed after the exclusive one are ignored and do not affect the target.

**Exclusive** is applied on both X and Y even if **X** or **Y Only** is used.

If the exclusive Advanced Follow effect has a max range, the exclusivity will not apply to targets outside that range.


## Mode

Mode selects the movement mode of Advanced Follow.
Available modes are:
- Mode 1: Easing
- Mode 2: Acceleration & Friction
- Mode 3: Steering & Breaking

### Universal Options

**Delay** makes the target follow the position of the center group with a delay. This will also delay the start of the follow movement proportionally.

**MaxRange** is the distance from center in (small step) units inside which the Advanced Follow effect is applied.

If **MaxRange** is equal to 0, no distance limit is applied. If it's less than 0, then Advanced Follow will stop working.

**MaxRange** has a reference ID which currently does nothing.

**MaxSpeed** limits the target's speed to the given speed value. If **MaxSpeed** is less than or equal to 0, no speed limit is used.

### Mode 1

**Mode 1** sets the velocity of the target based on its distance from the center, divided by **Easing**:

$Velocity=Distance/Easing$

As a side-effect, because all velocity from other sources is overriden, Edit Advanced Follow will not work on **Mode 1**.

### Mode 2 & 3

**StartSpeed** is the value of the velocity applied, while **StartDir** offsets the angle the velocity is applied towards.

1.00 speed is equal to one unit of movement per tick. **StartDir** is defined in degrees going clockwise.

**StartSpeed** and **StartDir** have two boxes on the right side which can be used to define a reference ID for the direction of velocity.

If there are multiple objects with the same reference ID, one is picked at random for each target.

If the reference ID contains an ID parent, the ID parent is used as reference.

If **StartSpeed** has a defined ID, the direction used is the direction of the last movement of the reference.

**StartSpeed** is NOT a multiplier when a speed reference is used, it is a set speed value.

If **StartDir** has a defined ID and **StartSpeed** does not, the direction used is from the target towards the reference.

The object's default direction points upwards. The default is used if no reference IDs are defined, or if the reference returns no valid direction.

The behavior of **StartSpeed** depends on the options **Init**, **Set** and **Add**.

If **Init** is used and this is the first action applied on the target, the object's velocity is set to **StartSpeed**.

If **Set** is used and **StartSpeed** is different from 0, the object's velocity is replaced by **StartSpeed**.

If **Add** is used, **StartSpeed** is added to the object's current velocity.

Due to a bug, only one object per **Target GID** can be affected by **StartSpeed**.

### Mode 2

**Acceleration** multiplies the target's acceleration towards the center. 1.00 **Acceleration** is equal to 0.01 increase in speed per tick.

**Friction** is the percentage of velocity lost every tick. Values of **Friction** are not limited - values below 0 and above 100 will increase the velocity exponentialy if there is no opposing force.

**Friction** is applied prior to acceleration.

With **NearDist** the values of acceleration and friction change linearly, from normal values when distance is equal to or bigger than **NearDist** to **NearAccel** and **NearFriction** values when distance is 0.

### Mode 3

In Mode 3, acceleration is applied in the direction of movement. With **Target Dir**, acceleration is applied towards the follow center like in Mode 2.

**SlowAccel** and **SlowDist** currently do nothing.

**SteerForce** is the multiplier of the max rotational speed applied on the object towards the follow center.
1.00 **SteerForce** is equal to 0.01 radians / tick. Steering is done prior to braking and acceleration.

**SteerForceLow** / **SteerForceHigh** replaces **SteerForce** if the velocity of the object is strictly below / above **SpeedRangeLow** / **SpeedRangeHigh**.

The target stops accelerating and starts braking if the direction of movement and the direction towards the center are offset by more than **BreakAngle**.

Breaking stops being applied once the target reaches 0 velocity, acceleration will continue to be disabled until the offset returns below **BreakAngle**.

If **BreakAngle** is above or equal to 180 degrees, the target will never brake. If it's below 0, it will be stuck braking.

**BreakForce** is the percentage of velocity lost every tick while braking, similar to friction in **Mode 2**.

Unlike friction, **BreakForce** is limited between 0 and 100.

**SteerForce** , **SteerForceLow** and **SteerForceHigh** are not applied while braking - **BreakSteerForce** is used instead if the velocity of the target is equal to or below **BreakSteerSpeedLimit**.


## Rotation

With **Rotate Dir**, the target rotates towards the follow center.

Rotation is done independently by each Advanced Follow action.

The rotation of the object is updated when entering the area of effect of the Advanced Follow.

Rotation speed is limited to 0.5 rad/tick. This is not affected by slowing down the game with timewarp.

**Rotation Offset** offsets the rotation's target angle by a value given in degres.

**Rotate Easing** eases the rotation using the formula:
$nextRotation = \frac{(currentAngle-targetAngle)}{easing}$

The target's rotation is not updated if the target's distance from the follow center is less than **Rotate Deadzone**, given in small step units.

With **Mode 1** and **2**, the rotation follows the object's direction of movement.

**Mode 3** has the following changes to rotation:
- Rotation always aims at the follow center
- Rotation speed is limited by the steering speed
- **Rotate Easing** and **Rotate Deadzone** have no effect

Having any **Mode 1** or **2** Advanced Follows active on the same target will override **Mode 3** rotation.


## X and Y Only

**X** and **Y Only** limit the movement action of Advanced Follow to the X or Y axis. This makes most Advanced Follow parameters apply on one axis (1D) instead of both axes (2D).

For 1D movement, the target and the follow center's position will be considered to be on the same axis.

If a target has an Advanced Follow present on one axis only, then the target will only have velocity on that respective axis.

**Max Range** and **NearDist** distance calculations are always 2D and not affected by **X** or **Y Only**.

### Mode 1

Easing is applied on each axis separately.

### Mode 2

Friction is applied on each axis separately.

Acceleration is done along the given axis towards the center.

### Mode 3

Braking is applied on each axis separately.

Without **Target Dir**, acceleration will be applied on the given axis based on the target's angle relative to it.

The target is unable to steer if **Mode 1** or **2** is present on the other axis.


## Ignore Disabled

With **Ignore Disabled**, targets that are toggled off are skipped by Advanced Follow. This will not skip targets that are off-screen.


## Random Values

Most Advanced Follow parameters can be randomized with the respective +/- option.

Similarly to Area triggers, these random coefficients are picked per object at level start and cannot be changed. More information can be found in the Area documentation.


## Object Links

Advanced Follow can use object and group ID links.

The movement of target objects and linked objects is done independently of one another.

Linking rules are the same as for Area triggers, more information can be found in the Area documentation.

### Area Parent

The Area Parent is the object group's center for distance calculations and the center of rotation when using **Rotate Dir**.

While Group Parents are also considered Area Parents if no Area Parent is present already, they are not used by Advanced Follow otherwise.

### Ignoring GID Parent / Linked Groups

It is possible to make the Advanced Follow ignore Group ID Parents and Linked Groups by applying the respective properties on the trigger, but the options are not implemented in the menu so this is currently possible only by modifying the object using external tools.


## Other Interactions

### Visibility

Advanced Follow acts on all targets, including the ones placed off-screen.

Link Visible is not needed when using Advanced Follow.

### Stop, Pause and Resume

Stopping is not instant and schedules the Advanced Follow instance to stop at the next tick of movement. The instance still counts as being active even if it's scheduled to stop, so in some cases it can prevent other instances of the same trigger from activating until then.

Pausing makes the Advanced Follow instance inactive until it is resumed or respawned,  **Delay** is not paused and continues to tick down while the trigger is paused.

### Remapping

Spawn remapping can create multiple instances of the same Advanced Follow trigger.

An Advanced Follow trigger's instances are unique for sets of **Target GID**, **Follow GID** and **Control ID**. 

Only one instance can be active on the same set of groups, trying to spawn additional ones does nothing.

### Timewarp

Timewarp increases the tick rate at values higher than 1, for values lower than 1 the tick rate remains the same but movements are multiplied to match the slow-down.

Advanced Follow behavior remains consistent at higher game speed compared to default speed, but at lower game speed instant movement is reduced and all Advanced Follow effects that change velocity are no longer consistent with default speed.