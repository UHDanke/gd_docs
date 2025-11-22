# Default Camera Properties

Default target is Player 1.

Camera movement based on player movement is done relative to the player, not the screen.

The default gameplay offset when moving left or right is 25 (75 units) and can be modified by Gameplay Offset.

Easing is applied when moving left or right in platformer mode, and is equal to 30 for all modes.

## Non-Bordered Camera

Cube and Robot use a non-bordered camera. Camera behavior depends on mode.

In classic mode the camera has a padding of 40 units and an easing of 40.

In platformer mode the camera has a minimum padding of 28 units, which increases based on the player's velocity up to 159 units.

## Bordered Camera

Ship, Ball, UFO, Wave, Spider and Swing use a bordered camera.

Borders are parallel to the ground, and will not rotate if Rotate Gameplay is used.

Camera Mode allows modifying how the camera behaves when the player moves up or down, the default easing is 40 (noted as 10 in Camera Mode) and the max camera-player offset for a padding of 0.5 is equal to -66.