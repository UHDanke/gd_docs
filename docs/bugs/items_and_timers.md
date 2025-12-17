# Items and Timers

## [2.207] [18/12/25] Count desync

The values stored inside Count triggers can be updated improperly or not at all when paused and resumed, when spawning pickups from inside other triggers and when using a persistent item due to Count storing the last value of the item when activating.
More information can be found in the count desync file.

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
