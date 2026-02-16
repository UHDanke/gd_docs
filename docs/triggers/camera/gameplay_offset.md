# Gameplay Offset

Changes the offset between player 1 and the camera's center applied when the player moves left or right. Offset steps are equal to 3 units, or 1/10th of a block.

X and Y do not refer to the camera's X and Y, but rather to what axis the player is currently using - **Offset X** is applied when the player is on the X axis and **Offset Y** when the player is on the Y axis (with Rotate Gameplay).

Follow behavior depends on the value of the offset - if the value is positive, the camera will be offset ahead of the player, if it's negative it will be offset behind it. When changing direction the camera will catch up or stay still in order to catch up to the offset for the new direction.

Both **Offset X** and **Offset Y** are applied unless either **X** and **Y Only** are used.

**Dont Zoom** makes the offset not scale with zoom. Without **Dont Zoom**, gameplay offsets are divided by the camera's current zoom value.