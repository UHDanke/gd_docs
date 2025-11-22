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