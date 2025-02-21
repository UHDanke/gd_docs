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

### Spawn Remapping

**Item ID** and **Target ID** can be remapped.

#### Spawn Inheritance

With **Multi Activate**, **Target ID** inherits spawn remaps.  
Without, **Target ID** does not inherit spawn remaps, instead it inherits the remaps of the oldest active instance of a subsequent Count trigger with the **Multi Activate** option using the same **Item ID**.  
If an instance of Count is spawned then activated during the same spawn, the target of this activation will not inherit remaps.

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

With **Dont Override**, **StartTime** is ignored when updating the timer (but it is used as the start value when creating a timer).

## Timers
Time triggers create global timer instances, which are shared by **Item ID**. Timers store all of the Time trigger's groups, properties and remap information.  
Activating a Time trigger while there is an already active timer for the given Item ID updates the timer with the trigger's settings and groups.

Timers update every tick, 240 times a second.  
Only timers initialized before the first timer spawn will be updated. If a new timer is initialized during or after timer activation, it will be processed in the next update.

**TargetID** for Time triggers can only spawn if the timer crosses the **StopTime**, using Item Edit for this purpose will not work. This does not apply to Time Event triggers.  
The value of timers is checked prior to Time and Time Event trigger spawns.

When updating, timers record the current timer value which is used to determine whether **Target ID** or Time Event triggers spawn.  
Unlike Count which is bi-directional, timers are one-directional and this depends on the value of **TimeMod**:
* For $TimeMod \gt 0$ **Target ID** is spawned if $previousValue \lt StopTime \le currentValue$.	
* For $TimeMod \lt 0$ **Target ID** is spawned if $previousValue \gt StopTime \ge currentValue$.

### Spawn Mechanics
Timers are processed in spawn order.  
All IDs can be spawn remapped.  
For remap inheritance, the timer instance stores the remaps.  
Remaps can only be set when creating a timer instance, updating a timer will not update the remaps.  
Updating the timer does not change the timer's spawn limit.

## Stop, Pause and Resume
Stop triggers stop, pause or resume a timer given by group or control ID.  
Stopping the timer clears all settings, remaps and the current value is reset to 0.

# Time Event

Spawns **TargetID** when the timer given by **ItemID** reaches the **TargetTime**.  

## Activation

Time Event requires an active timer to work, which can be created with a Time or Item Edit trigger.  

Time Event can be initialized even if the timer isn't active, and will continue to be active when the timer is cleared by Stop.

Time Event triggers do not spawn groups on their own, they assign extra groups for timers to spawn at the specified **TargetTime**.  

If a Time Event is initialized on an active timer, it will spawn instantly (even if the timer is paused) if:
- $(TimerMod > 0) \land (TargetTime > 0) \land (Time >= TargetTime)$
- $(TimerMod < 0) \land (TargetTime < 0) \land (Time <= TargetTime)$

### Spawn Mechanics
**ItemID** can be remapped.  
Unlike Count triggers, Time Events are not ordered by **TargetTime**. If multiple Time Events with the same ItemID spawn in the same tick, spawn order will be used.  

Since timers spawn the groups given by Time Event, the spawn behavior is not going to depend on the Time Event, but on the timer:
* The spawn target inherits the timer's remaps.
* The timer's spawn limit is applied to all extra groups added by Time Event.
* Time Events spawn after the corresponding timer, even if the Time Event was created before the timer.

# Time Control

Pauses or resumes a timer given by **ItemID**.

Only works on active timers.  

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
Timers created using this trigger are paused, use default settings and have no remaps, groups or control IDs.  
These timers can be cleared only with a Stop trigger using Control ID 0.  
Item Edit can only update the value of an active timer.	

# Item Compare

Spawns **TrueID** or **FalseID** based on the result of the comparison of two parameters.

## Parameters
Can be items, timers, points, main timer or attempts.

## Math Operators

### Mod
First button changes the operator of Mod1 and the first parameter between = (assign), += (add), -= (subtract), ⋅= (multiply) and \\= (divide).
Second button changes the operator of Mod2 and the second parameter.

### Comparison
Third button changes the comparison operator between the results of the mod functions between == (equal), >= (greater or equal), <= (lower or equal), > (greater than), < (lower than) and != (not equal).

#### Tolerance
Tol adds tolerance to the comparison functions which allows for slight variations within the given tolerance.

Tolerance formulas for every comparison operator:
* Equal:  $\left\|Result1-Result2\right\|\le Tol$
* Not Equal:  $\left\|Result1-Result2\right\|\gt Tol$
* Greater:  $Result1-Result2 \gt -Tol$
* Greater or Equal:  $Result1-Result2 \ge -Tol$
* Lower:  $Result1-Result2 \lt Tol$
* Lower or Equal:  $Result1-Result2 \le Tol$

### Sign Functions
The two buttons change the functions applied on the results of the mod operations between between none, A (Absolute) and N (Negative).  
Sign functions are applied after the respective rounding functions.

### Rounding Functions
The two buttons change the functions applied on the results of the mod operations between NA (none), RN (Round to nearest), FL (Round down) and CE (Round up).  

# Item Persist
Makes the item or timer given by **Item ID** persistent between attempts.

**Persistent** makes the target persistent.  

**Reset** makes the target no longer persistent and resets its value to 0.  
Targets continue to be persistent until **Reset** is used, even between attempts.

**TargetAll** targets all persistent items or timers.

When persistent, items and timers keep all of their values and settings between attempts.  
In the case of timers, this includes timer stop options and remaps.  

Count triggers are not persistent between attempts, the Count's stored item value does not get updated on respawn if the Count was activated prior to the checkpoint. If the persistent item value changes after the checkpoint, the Count's stored value and item value will differ.    

While timers are persistent, Time Event triggers are not.

Special items are not affected by Item Persist - Main time and Attempts are persistent, Points are not.

# Counter Labels

Displays the value of a given **ItemID** using a text label.  
Displays the value of a timer instead if **Time Counter** is selected.  

Special items like Main Time, Points and Attempts can be displayed if the respective option is selected. As these are items, they will not be displayed if **Time Counter** is selected.  
Items -1, -2 and -3 can also be used to display the three special items Main Time, Points and Attempts.  
By default the text of the label is aligned to center, **Left Align** and **Right Align** aligns the text to the left and right respectively.  

If by any reason the label is not updated properly and displays the wrong value, a Pickup with the same ItemID will update the label even if it doesn't change the value of the item.
Points will not be displayed by a counter label until the first point is obtained.  

Item labels will only be updated by a Pickup with the same ID, even if its outside the normal ID range.  
ItemIDs outside the 0-9999 range refer to ID 0 or 9999 for both items and timers.

# Item ID Limits

## Items
Items are limited between ID 0 and 9999.  

While some triggers can be assigned items outside the usual range, these items refer to either ID 0 or 9999.  
ItemIDs below 0 are reserved for items like Main Time, Points and Attempts.  

## Timers
Timers are not limited and can be assigned both positive IDs higher than 9999 and negative IDs lower than 0.  
The only triggers able to use negative timers are Time, Time Event, Time Control and Item Persist.  
Item Edit and Item Compare are not able to be used to assign or extract values from these timers, it is not possible to use these timers as a way to store numerical values. It is possible however to store remaps, which can be accessed by Time Event.
