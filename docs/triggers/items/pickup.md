# Pickup

Changes the value of an item given by **Item ID** by adding the value of **Count** to it.


Items use 32 bit signed integers to store their value in a range of -2^31 to 2^31-1, operations that go above or below these limits will cause integer overflow.

## Multiply & Divide

If **Multiply** or **Divide** is selected, **Modifier** multiplies or divides the item value. 

This operation uses single precision float which is not accurate for high values. 

The result is rounded to the nearest whole number.

If the resulting value is above 2^31-1, on PC the result value is -2^31 while on mobile the  result is 2^31-1. For values below -2^31 the result is -2^31 on all versions.

## Override

If **Override** is selected, the item is set to the value of **Count**.

