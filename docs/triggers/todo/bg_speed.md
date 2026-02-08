# Background Speed

Controls the X and Y speed of the background, relative to the camera's movement.

The background's movement can be calculated using the formulas:
$BGMoveX = CMoveX \cdot (1 - SpeedX)$
$BGMoveY = CMoveY \cdot (1 - SpeedY)$

For example, a speed of 1.00 makes the background stationary, while a speed of 0.00 matches the camera's movement.

The background's default X and Y speed are both 0.1, which makes the background move at 90% of the camera's speed.
