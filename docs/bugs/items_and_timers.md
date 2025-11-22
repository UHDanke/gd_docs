# Items and Timers

## [2.207] Count desync

The values stored inside Count triggers can be updated improperly or not at all when paused and resumed, when spawning pickups from inside other triggers and when using a persistent item due to Count storing the last value of the item when activating.
More information can be found in the count desync file.

## [2.207] Pickup operations are innacurate

Multiplying large numbers using Pickup triggers has significant errors.
This isn't the case for Item Edit triggers however.

## [2.207] Item Compare may be inaccurate when checking if an ItemID equals a value

Item Compare can return false when comparing an integer Item ID to a value it is equal to (for example, 1).
This may be caused by Pickups, but i was not able to accurately figure out a cause for this.

## [2.207] Time **Ignore Timewarp** does nothing

Timer is still slowed down or sped up by timewarp with the option selected.

## [2.207] Counter labels do not update properly with items outside the 0-9999 range

Counter labels only update if a Pickup or Item Edit trigger with the same ItemID is used.
IDs outside the 0-9999 range refer to ID 0 or 9999. If an ID outside this range is used, it will display the value of ID 0 (if below 0) or 9999 (if above 9999), but will not update when ID 0 / 9999 change values.
Timers text labels update properly and are not affected by this bug.

## [2.207] Level is unlisted if it contains a Pickup with high count or negative item id

The server unlists any level that contains a Pickup, Count or Instant Count trigger with either high count (100k or more) or an item ID less than 0.

This is an intentional fix to the 2.1 ACE exploit which has remained in place as 2.1 clients are still able to download levels.

Item Edit and Time triggers are not affected by either issue.

## [2.207] Item Attempts value only returns 1

Attempts item is not updated on new attempts and always returns value 1 when used inside Item Edit or Item Compare.

## [2.207] Timers reversed spawn order

Timers spawn from the oldest timer first to newest last on mobile (reversed), and from newest first to oldest last on PC.