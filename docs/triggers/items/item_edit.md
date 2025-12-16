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

### Precision

Item Edit operations are done at double precision.

### Items & Points

When assigned to an Item, the result is truncated to a whole number.

Item assignments are limited between -2^31 and 2^31-1. Operations on items will not cause integer overflow since they are always done in floating point.

Due to a bug, on the steam version of the game values above 2^31-1 instead are replaced by -2^31.

### Timers

Timer assignments are limited between -9999999.00 and 9999999.00.

Item Edit can initialize timers if there isn't one active already.

Timers created using this trigger are paused, use default settings and have no remaps, groups or control IDs.

These timers can be cleared only with a Stop trigger using Control ID 0.

Item Edit will update only the value of a timer if it is already active.

### INF and NAN

INF and NAN can be used inside item edits through external editing.

INF and -INF can be assigned to timers or items but they will be limited like any other high value.

NAN cannot be assigned to items and it will be replaced by an integer value - on PC it is replaced by -2^31 while on mobile it is replaced by 0.

NAN can be assigned to timers, but this will make the timer unusable - all operations including NAN have NAN asa result and all comparison operations including NAN return false.