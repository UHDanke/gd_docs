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

### Spawn Inheritance

With **Multi Activate**, **Target ID** inherits spawn remaps.  
Without, **Target ID** does not inherit spawn remaps, instead it inherits the remaps of the oldest active instance of a subsequent Count trigger with the **Multi Activate** option using the same **Item ID**.  
If an instance of Count is spawned then activated during the spawn, the target of this activation will not inherit remaps.

### Multiple Instances

Count can be instantiated multiple times regardless of remaps.  
If an instance of Count activates during the spawn of another instance of the same Count trigger, the new spawn will use the remaps of the first unfinished spawn.   
