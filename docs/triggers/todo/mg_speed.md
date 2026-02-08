# Middleground Speed

Controls the X and Y speed of the middleground.

Middleground speed works differently for X and Y:
- X axis: movement is relative to camera movement
- Y axis: position is relative to camera position
 
As a side-effect, if you change the middleground's Y speed this will also instantly change the middleground's position.

The middleground's movement and position can be calculated using the formulas:
$MGMoveX = CMoveX \cdot (1 - SpeedX)$
$MGPosY = CPosY \cdot (1 - SpeedY) + OffsetY \cdot 3$

For example, a speed of 1.00 makes the middleground stationary, while a speed of 0.00 matches the camera's movement.

The middleground's default X and Y speed are 0.3 and 0.5 respectively, which makes the middleground move at 70% of the camera's horizontal speed and syncs the middleground's vertical position to 50% of the way between the level's origin and the camera's current position.
