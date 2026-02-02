# Limited IDs

## Group IDs

Trying to assign ID values outside 0-9999 is not possible.
Any value below 1 refers to ID 0.
Any value above 9999 refers to ID 9999.

## Color Channels

Trying to assign ID values outside 0-999 is not possible.
Values below 1 do nothing.
Values between 1000-1101 are reserved for special color channels.

Any value above 1101 refers to ID 1101.

## Item IDs

Values below 0 are reserved for special items (-1 is Time, -2 is Points, -3 is Attempts).
Pickup, Item Edit and Item Compare can reference (but not change, they get limited to 0 or 9999) IDs outside 0-9999.
Item Edit cannot use ID 0 as a parameter.
Time, Time Event and Time Control can reference and use IDs outside 0-9999. As Item Compare and Item Edit cannot reference out of bounds IDs, accessing the values of these timers is not possible. It is however possible to store remaps inside timers and spawn a group with those remaps using Time Event.

## Song Channels

Trying to assign ID values outside 0-4  is not possible.
Any value below 1 refers to ID 0\.
Any value above 4 refers to ID 4\.

## Collision IDs

Same as Group IDs.

## Gradient IDs

* Trying to assign ID values outside 0-999 is not possible without mods or scripts.
* Builder helper can assign at most to ID 1000\.

# Extended Limit IDs

IDs with extended limits can be assigned beyond the usual 10000 ID limit.
ID values outside 0-9999 cannot be assigned inside (most) triggers, but can be referenced via remapping.

IDs with extended limit

* Control IDs
* Area Effect IDs
* Enter Effect IDs
* Item IDs (timers only)
* Material IDs (between −/+ 32767\)
* Enter Channels (between −/+ 32767\)
* SFX IDs
* SFX Groups
