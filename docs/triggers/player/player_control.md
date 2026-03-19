# Player Control

Controls a player's current actions.

## Options

**P1** and **P2** specify which players the trigger targets, if none are selected the trigger has no effect.

**Stop Jump** stops the player's current jump if held.

**Stop Move** stops the player's current left / right movement in platformer mode 

**Stop Rot** behavior depends on mode:
- Cube: resets the cube's spin direction
- Ball: stops the ball's rotation completely
- Other: no effect

**Stop Slide** stops the player's low-friction state after a force is applied (from teleport or a force object, for example).