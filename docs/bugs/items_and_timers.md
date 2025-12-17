# Items and Timers

## [2.207] [18/12/25] Count desync

The values stored inside Count triggers can be updated improperly or not at all when paused and resumed, when spawning pickups from inside other triggers and when using a persistent item due to Count storing the last value of the item when activating.

### Persistent Items

The value stored inside Count and the value of the item will no longer match when the player respawns, if the item is persistent and the value changes after the count was initialized.

### Paused Counts

Count triggers do not update the stored item value if they are paused.

### Count activating its own Item ID

If a Count trigger activates a Pickup or Item Edit trigger with the same Item ID as the Count's Item ID, this will trigger a new check for all Count triggers of that Item ID. 

On this new check, Count triggers will update their stored value to the new Item ID value. However, if a previous Count check was interrupted by this new check, the game will resume the previous check when the new one is done. 

When the game updates the Count's stored value, it doesn't use the current Item ID value, it uses the value from when the check was initialized - this means the previous check will update the remaining Count triggers to an old value causing a desycn from the current Item.

## [2.207] [18/12/25] Count check can reverse order if interrupted by a new check

Count trigger checks are ordered by Target Count, the order of activations depends on whether the item was added or subtracted.

If a Count trigger activates a Pickup or Item Edit trigger with the same Item ID as the Count's Item ID, but the operation subtracts instead of adding (or vice-versa), the order of checks for both the new AND any previous remaining checks for that item ID will be reversed.

Count checks are done by looping over count instances mapped by Target Count using an index. This index will count from the start if adding and from the end if subtracting. If the order changes in a new item change, then that can cause the same Count triggers to be checked again.

## [2.207] [18/12/25] Time **Ignore Timewarp** does nothing

Timer is still slowed down or sped up by timewarp with the option selected.

## [2.207] [18/12/25] Counter labels do not update properly with items outside the 0-9999 range

Counter labels only update if a Pickup or Item Edit trigger with the same ItemID is used.
IDs outside the 0-9999 range refer to ID 0 or 9999. If an ID outside this range is used, it will display the value of ID 0 (if below 0) or 9999 (if above 9999), but will not update when ID 0 / 9999 change values.
Timers text labels update properly and are not affected by this bug.

## [2.207] [18/12/25] Level is unlisted if it contains a Pickup with high count or negative item id

The server unlists any level that contains a Pickup, Count or Instant Count trigger with either high count (100k or more) or an item ID less than 0.

This is an intentional fix to the 2.1 ACE exploit which has remained in place as 2.1 clients are still able to download levels.

Item Edit and Time triggers are not affected by either issue.

## [2.207] [18/12/25] Item Attempts value only returns 1

Attempts item is not updated on new attempts and always returns value 1 when used inside Item Edit or Item Compare.

## [2.207] [18/12/25] Timers reversed spawn order

Timers spawn from the oldest timer first to newest last on mobile (reversed), and from newest first to oldest last on PC.

## [2.207] [18/12/25] Float Operations return a different value on PC and mobile

When assigning a value higher than 2^31-1 to an item with Item Edit or Pickup (using Multiply / Divide), the overflow value differs between pc and mobile - on pc the overflow is -2^31 while on mobile the overflow is 2^31-1. For values lower than -2^31 the overflow is -2^31 on both versions.

## [2.207] [18/12/25] Pickup Multiply / Divide is innacurate

Multiply / Divide Pickup operations use single precision floats instead of double precision like in the case of Item Edit which introduces significant errors.
