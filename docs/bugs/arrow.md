# Arrow Trigger

## [2.207] [18/12/25] Arrow trigger & channel 0 triggers

If you place an arrow trigger (without touch or spawn) that changes the trigger channel to 0 anywhere in the editor, the activation of all channel 0 triggers in the entire level will now depend on the position of the triggers relative to the arrow trigger.

If the triggers are placed after the arrow trigger, depending on the direction the arrow points towards, their activation is completely ignored.

This happens even if the arrow trigger hasn't been reached yet or if any other arrow triggers (without channel 0) are placed before it.

## [2.207] [18/12/25] Arrow trigger activation delay
The activation of arrow triggers (without spawn or touch) is delayed until all triggers on the same channel that are placed before the arrow trigger (relative to where the arrow points) are activated.

## [2.207] [18/12/25] Arrow and Music Line mismatch

The music line uses the arrow trigger as the origin when gameplay rotates, but trigger activation depends mostly on the player's position, which is inconsistent and can be affected by variations in the player's position.

## [2.207] [18/12/25] Music Line Y 0
The music line cannot go below Y 0. The behavior depends on the position and direction of the arrow trigger:
- Position below Y 0 and pointing up: the music line will start from Y 0
- Position below Y 0 and pointing down: the music line freezes in place before rotating
- Position above Y 0 and pointing down: the music line freezes upon hitting Y 0

## [2.207] [18/12/25] Strange Vel Mod behavior

Edit velocity behavior of arrow trigger is unintuitive:
- Velmod X and Y do nothing if the player only reverses direction
- When gameplay is rotated, the player's vertical velocity is set to the player's previous horizontal velocity multiplied by Velmod Y
- Velmod X does nothing in classic mode, in platformer when gameplay is rotated, the player's horizontal velocity is set to the player's previous vertical velocity multiplied by Velmod X
- If using Override Velocity then the vertical velocity is set to Velmod Y and the horizontal velocity is set to Velmod X (this works as intended)
- Neither Velmod X or Y take into account whether the arrow trigger inverts gravity
