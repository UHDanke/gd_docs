# Count

Spawns or toggles a **Group ID** when the **Item ID** value reaches or passes **Target Count**.

## Activation

Each instance of Count stores the **Item ID**'s last value. When the **Item ID** value changes, Count updates its stored value to the new one.  
If the stored value is different from the new one and **Target Count** is between the stored and new item value or equal to the new value, Count disables the **Target ID**.  
With **Activate Group** selected Count enables and spawns the **Target ID**. This can interfere with Toggle triggers if they target the same group.  
Without **Multi Activate**, Count stops after one activation.

## Spawn Mechanics

### Stored Value

When spawned, Count initializes the stored value with the current value of the **Item ID**.

#### Pause & Resume

When paused, Count does not update the stored **Item ID** value.  
On Resume, the Count will have the same stored **Item ID** value prior to Pause, and will only update on the next **Item ID** value change.  
As a consequence it is not possible to use Pause & Resume to skip past the **Target Count** of a Count trigger.  
Count will activate on the next item update since the stored value no longer matches the value of the **Item ID**.

### Spawn Order

**Target ID** spawns immediately after a Pickup or Item Edit trigger, interrupting any other active spawns.  
The interrupted spawn is resumed after all activated Count spawns finish.   
If multiple Count triggers activate at the same time, they are spawned in order, one after the other.

#### Target Order

Count instances are ordered by **Target Count** in ascending order if the new **Item ID** value is bigger or equal to the old one, and in descending order if the value is strictly lower.  
Instances with the same **Target Count** use spawn order (from oldest to newest).

#### Count Interrupt

The spawn of Count can interrupt other active Count spawns.   
This happens even if the old and new **Item ID** value are identical, for example from a Pickup trigger that adds 0\.

On an item change, all Count instances with the specified **Item ID** get queued as outlined in Target Order. This Count update will use the new value of the **Item ID** at the moment of the change to update the stored values and decide what instances spawn.

If any of the Count spawns trigger an item change, a new Count update will be created, as described above, using the new item value. The instances will, again, be sorted using the Target Order in ascending or descending order.

When the initial Count update resumes, two issues arise if the **Item IDs** of both updates are identical:

1. When interrupted, the first update will use the last update's order. If the second update changes the ascending / descending order, then the queued counts will be processed in the wrong order. It will also keep its offset.  
2. The item value used in the initial update is still the same, the initial Count update will update the stored value using an outdated item value.

For example, If the first Pickup changes the item value from 0 to 1000, then the third Count instance activates another Pickup that changes the value from 1000 to 0, it will resume from the fourth last Count instance and continue in descending order. The stored value is updated to 1000 for the first 3 instances, then updated to 0 for all instances, then updated back to 1000 for all but the last 3 instances.

If there is any interest in making this behavior less nonsensical, new Count spawns should discard any queued Count spawns using the same **Item ID**.

### ID Limits

Minimum **Item ID** is 0, maximum **Item ID** is 9999\.  
**Item ID** 0 is usable by Count, but only Pickup is able to modify it.

### Remappable IDs

**Item ID** and **Target ID** can be remapped.

#### Spawn Inheritance

With **Multi Activate**, **Target ID** inherits spawn remaps.  
Without, **Target ID** does not inherit spawn remaps, instead it inherits the remaps of the oldest active instance of a subsequent Count trigger with the **Multi Activate** option using the same **Item ID**.  
If an instance of Count is spawned then activated during the spawn, the target of this activation will not inherit remaps.

### Multiple Instances

Count can be instantiated multiple times regardless of remaps.  
If an instance of Count activates during the spawn of another instance of the same Count trigger, the new spawn will use the remaps of the first unfinished spawn.   

# Instant Count
Toggles off a **Group ID** by comparing **Item ID** to **Target Count**.

Toggles on and spawns **Group ID** if **Activate Group** is selected.
The comparison options are:
* **Equals**:  $Item=TargetCount$
* **Larger**:  $Item\gt TargetCount$
* **Smaller**:  $Item\lt TargetCount$

# Pickup

Changes the value of an item given by **Item ID** by adding the value of **Count** to it.

If **Multiply** or **Divide** is selected, **Modifier** multiplies or divides the item value.

If **Override** is selected, the item is set to the value of **Count**. 

# Time

Creates timers which can be used to keep track of elapsed time or activate groups after a given delay.

## Options

**StartTime** overrides the previous value of the timer.

**StopTime** pauses the timer and spawns **Target ID** when the stop value is reached.  
This option is ignored if the tickbox is unselected.  
The timer gets set to the stop value if it goes over the stop point.  
The timer will not stop if it starts or is unpaused from or past the stop value.  

**TimeMod** modifies the timer multiplier. The default multiplier is 1 per second.  
If **TimeMod** is 0 then the timer is unable to spawn groups.

**Ignore Timewarp** is currently bugged and has no effect.

**Start Paused** pauses the timer.

With **Dont Override**, **StartTime** is ignored when updating the timer.

## Activation
Time triggers create global timer instances, which are shared by **Item ID**.  
Activating a Time trigger while there is an already active timer for the given Item ID updates the timer with the trigger's settings and groups.

Timers update every tick, 240 times a second.  
Only timers initialized before the first timer spawn will be updated. If a new timer is initialized during or after timer activation, it will be processed in the next update.

When updating, timers record the current timer value which is used to determine whether **Target ID** or Time Event triggers spawn.  
Unlike Count which is bi-directional, timers are one-directional and this depends on the value of **TimeMod**:
* For $TimeMod \gt 0$ **Target ID** is spawned if $previousValue \lt StopTime \le currentValue$.	
* For $TimeMod \lt 0$ **Target ID** is spawned if $previousValue \gt StopTime \ge currentValue$.

### Spawn Mechanics
Timers activate groups in spawn order.  
All IDs can be spawn remapped.  
For remap inheritance, the timer instance stores the remaps.  
Remaps can only be set when creating a timer instance, updating a timer will not update the remaps.  
Updating the timer does not change the timer's spawn limit.

## Stop, Pause and Resume
Stop triggers stop, pause or resume a timer given by group or control ID.  
Stopping the timer clears all settings, remaps and the current value is reset to 0.

# Time Event

Stops after activating without **Multi Activate**.

## Activation
Activates after
If spawned from inside a timer

# Time Control

Pauses or resumes a timer given by **ItemID**. Only works on active timers.  
Can be used on timers created by Item Edit triggers.  
Can be remapped.

# Item Edit
Updates the value of the target variable based on the values of the given parameters using mathematical functions.

## Parameters
Items and Timers can be selected by ID.  
Points returns the total amount of points obtained so far.  	
Time returns the value of the level's global timer, which is updated every tick before spawn delays are scheduled.  
Att returns the player's current attempts.  

## Math Operations
Besides **Mod**, there are seven buttons which change the operators and functions used in calculation.  
From top left, the first three buttons change the assignment, parameter and mod operator.  
The next two on the same line change the sign functions applied after rounding.  
The two below change the rounding functions applied after the mod and assignment operators.  

### Assignment
First button changes the assignment operator between = (assign), += (add), -= (subtract), ⋅= (multiply) and \\= (divide).

### Parameters
Second button changes the operator applied on the two parameters between +, -, ⋅ and \\.

### Mod
Third button changes the operator applied on Mod and the result of the parameter operation between ⋅ and \\.

### Sign Functions
The first button changes the function applied on the result of the mod operation between between none, A (Absolute) and N (Negative).  
The second button changes the function applied on the result of the assignment operation.  
Sign functions are applied after the respective rounding functions.

### Rounding Functions
The first button changes the function applied on the result of the mod operation between NA (none), RN (Round to nearest), FL (Round down) and CE (Round up).  
The second button changes the function applied on the result of the assignment operation.

## Result Assignment
The result can be assigned to an item or timer given by ID, or to the Points variable.  
If the result is assigned to an integer variable like Item or Points, decimal values are truncated. 

### Timers
Item Edit can initialize timers if there isn't one active already.  
Timers created using this trigger are paused, use default settings and have no remaps.  
Item Edit can only update the value of an active timer.	

# Item Compare

# Item Persist
Makes the item or timer given by **Item ID** persistent between attempts.

**Persistent** makes the target persistent.  

**Reset** makes the target no longer persistent and resets its value to 0.  
Targets continue to be persistent until **Reset** is used, even between attempts.

**TargetAll** targets all persistent items or timers.

When persistent, items and timers keep all of their values and settings between attempts.
In the case of timers, this includes timer stop options and remaps.

