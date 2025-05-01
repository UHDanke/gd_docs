
# Shake

Applies a shaking effect to the screen.

## Behavior

Shakes the screen by moving the view on both X and Y axes by a random offset multiplied by **Strength**. The view is offset every **Interval** until Duration runs out.

UI, Background and Middleground will not move at all. Ground will only move vertically.

Only one shake effect can be active at a time and new shakes override previous ones. This includes the on death shake as well, which can be overriden.

### Options

Strength and Duration must both be bigger than 0 for the shake to trigger. 

If Interval is 0, the view will offset every render frame. 

The lowest value of Strength that can be used is 0.01, which is low enough to be imperceptible.

The max values of a Shake trigger are Strength 100, Interval 0.20s and Duration 10.00s.

All shaking effects can be disabled using the "Disable Shake" level option.

<br>

# Change Background 

Changes the level's Background to a different preset. There are currently 59 BG presets.

Only one Background change can be made per render frame. The first will trigger, while any other subsequent BG trigger is ignored until the next frame.

<br>

# Change Middleground

Changes the level's Middleground to a different preset. There are currently 3 MG presets.

Only one Middleground change can be made per render frame. The first will trigger, while any other subsequent MG trigger is ignored until the next frame.

<br>

# Change Ground

Changes the level's Ground or Line to a different preset. There are currently 22 G presets and 3 Line options.

Only one Ground change can be made per render frame. The first will trigger, while any other subsequent G trigger is ignored until the next frame.

<br>

# Disable / Enable Player Trail

Disables / Enables the Players' icon after-effect.

The trail is disabled by default.

<br>

# Show / Hide Player

Makes the Players' visible or invisible.

The **Hide P1** / **P2** options from the Options trigger can be used to hide or show each player individually.

Players are visible by default. 

<br>

# BG Effect On / Off

<br>


# Gradient

<br>

# Shaders

<br>



# Options 

<br>

# BPM Guide

<br>


# Default Camera Properties

Default target is Player 1.

Easing on X axis is 7.5, while on Y axis it is 10. Multiply these values by 4 to obtain the equivalent Advanced Follow easing.
 
The default gameplay offset on X axis is 25 (75 units) and can be modified by Gameplay Offset. Y axis offset can be calculated by the formula $OffsetY=-1 \cdot HeightY \cdot Padding$ and can be controlled by Camera Mode.

X and Y are the Player's X and Y, not the screen's. If the gameplay is rotated by 90 degrees using a Rotate Gameplay trigger, then the axes on which easing and max offset are applied will also be switched around.

# Zoom Camera

<br>

# Static Camera

<br>

# Offset Camera

<br>

# Gameplay Offset

Changes the offset between player 1 and the camera's center applied on the X axis.

Currently the Y axis seems completely unaffected by this trigger.

Follow behavior depends on the value of the offset - if the value is positive, the camera will be offset ahead of the player, if it's negative it will be offset behind it. When changing direction the camera will catch up or stay still in order to catch up to the offset for the new direction.

**X** and **Y Only** override the gameplay offset only on the X, respectively Y axis.

**Dont Zoom** makes the offset not scale with zoom. Without **Dont Zoom**, gameplay offsets are divided by the camera's current zoom value.

# Rotate Camera

<br>

# Camera Edge

<br>

# Camera Mode

Removes borders for certain gamemodes with **Free Mode** is selected and changes the Y camera settings if **Edit Camera Settings** is used.

These settings can also be set when switching gamemode using a portal.

Gamemodes without borders like Cube and Robot are not affected by Camera Mode, not even by the camera settings.

<br>

# Camera Guide

Editor only object which displays a reference outline for the camera's edges.

## Color Guide

The yellow line shows the Player's X position relative to the camera center.

The green outline shows the camera's minimum guaranteed coverage.

The orange outline shows the camera's coverage for the current resolution.

## Options

**Zoom** changes the referenced zoom level for the guide.

**Offset X** and **Offset Y** offset the guide from the center object by a small step unit amount.

**Preview Opacity** modifies the opacity of the camera outlines.

## Notes

Camera Guides cannot be rotated in any way.

The position of the yellow line is updated only while playtesting.

Camera Guide objects are often used as reference for triggers such as Static Camera and UI.
