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

# Zoom Camera

<br>

# Static Camera

<br>

# Offset Camera

Offsets the camera's position by **Offset X** or **Offset Y** overtime. Offset steps are equal to 3 units, or 1/10th of a block.

Both **Offset X** and **Offset Y** are applied unless either **X** and **Y Only** are used.

The transition rate can be controlled using **Duration** and **Easing**.
<br>

# Gameplay Offset

Changes the offset between player 1 and the camera's center applied when the player moves left or right. Offset steps are equal to 3 units, or 1/10th of a block.

X and Y do not refer to the camera's X and Y, but rather to what axis the player is currently using - **Offset X** is applied when the player is on the X axis and **Offset Y** when the player is on the Y axis (with Rotate Gameplay).

Follow behavior depends on the value of the offset - if the value is positive, the camera will be offset ahead of the player, if it's negative it will be offset behind it. When changing direction the camera will catch up or stay still in order to catch up to the offset for the new direction.

Both **Offset X** and **Offset Y** are applied unless either **X** and **Y Only** are used.

**Dont Zoom** makes the offset not scale with zoom. Without **Dont Zoom**, gameplay offsets are divided by the camera's current zoom value.

# Rotate Camera

<br>

# Camera Edge

Defines an object given by **Target ID** as one of the camera's **Left**, **Right**, **Up** or **Down** limit edge.

Target ID must contain a single object or an ID parent.

Edge triggers cannot be stopped, unlocking an edge can only be done by setting the group to an unused group, such as 0, or to a group with more than one target.

The **Left** edge has priority over **Right**, and **Down** has priority over **Up**.

Camera Edge follows the movement of a target object.

## Default Edges

Y = 0 is the lowest the camera's bottom edge can go and cannot be overriden. It has priority over all other Y axis edges.

X = 30 is the furthest left the camera can go on the first attempt only. It has priority over all other X axis edges and cannot be overriden. On future attempts this edge is not applied.

The ceiling counts as a camera edge and can be overriden by a **Down** edge, but not by a **Top** edge. The ceiling is set 240 units above the topmost object.
The end wall counts as a camera edge and can be overriden by another **Left** edge, but not by a **Right** edge. The end wall is set 355 units right of the rightmost object in classic mode, platformer has no end wall.

## Player Camera

Locking the edge moves the camera instantly to a valid position, while unlocking makes the camera ease back towards its normal position.

## Static Camera

Camera Edge also affects static cameras. When unlocking the camera, the movement will be instant if the Static Camera doesn't follow the target, otherwise it will use the follow's easing value.
 
<br>

# Camera Mode

Removes borders for certain gamemodes when **Free Mode** is selected and changes how the camera behaves when the player moves up or down if **Edit Camera Settings** is used.

These settings can also be set when switching gamemode using a portal, they have the exact same behavior as the trigger version.

Gamemodes without borders like Cube and Robot are not affected by Camera Mode, not even by the camera settings.

Padding determines the Y offset, this can be calculated by the formula $OffsetY = 130-128 \cdot Padding$

Gameplay borders snapping to the Y axis grid can be disabled with **Disable Gridsnap**.

<br>

# Camera Guide

Editor only object which displays a reference outline for the camera's edges.

## Guidelines

The yellow line shows the Player's X position relative to the camera center.

The green outline shows the camera's default size, which at zoom 1.000 is 480 by 320 units (or 3:2, NOT 4:3). This area is guaranteed to be visible on all devices.

The orange outline shows the camera's coverage for the current resolution.

## Options

**Zoom** changes the referenced zoom level for the guide.

**Offset X** and **Offset Y** offset the guide from the center object by a small step unit amount.

**Preview Opacity** modifies the opacity of the camera outlines.

## Notes

Camera Guides cannot be rotated in any way.

The position of the yellow line is updated only while playtesting.

Camera Guide objects are often used as reference for triggers such as Static Camera and UI.

<br>

# UI

Marks objects part of **Group ID** as UI objects.

## Options

If **Group ID** has a Group ID Parent, all objects in the group will copy the parent's alignment. This effect is only noticeable when using the **Auto** or **Relative** settings, as the other settings apply the same alignment to all objects.

**UI Target** is used as a reference for the camera's center; it does not have to be a Camera Guide object, but there's little reason to use anything else. 

**UI Target** must contain one valid target for UI to activate, if multiple objects are present then you have to define one as the Group ID Parent or else UI will not work.

### Alignments

UI objects can be made to keep their position relative to a reference point like the camera's center or edges using alignments. For example, if a **Left** alignment is used then the object will keep the same distance from the left edge of the screen on all aspect ratios.

By default, the default screen ratio (Camera Guide's green outline) is used as reference, NOT your aspect ratio (the orange guideline).

Alignments are split into XRef and YRef, only one alignment is applied at a time depending on your screen's aspect ratio. If your aspect ratio is wider than default (orange guideline appears on the sides of the camera guide) XRef is used and if its taller than default (guideline appears at the top and bottom) then YRef is used.

**Auto** makes UI objects align to the closest edge - **Left** or **Right** for XRef, **Top** or **Bottom** for YRef.

**Center** applies no alignment, the objects keep their positions relative to the center which is static for all aspect ratios.

**Left**, **Right**, **Top** and **Bottom** align objects to the respective edge.

**Relative** makes the objects position scale with the aspect ratio - if your object is 50% of the distance between the camera's center and the closest edge, it will be 50% of the distance on all aspect ratios. This option ignores all other alignments, it doesn't matter whether **Auto**, **Center** or any other alignment is used.

## Behavior

UI is an on-load trigger, it is activated once when the level loads and remains permanently active.

The UI layer is unaffected by ALL camera changes (ex: zoom, rotate, offset, etc).

UI effects do not stack and only one is applied per object, as a result only the first alignment on an object will be applied, and any further UI triggers will skip it. If the parent of a group ID has already been affected by an UI trigger, this group cannot be affected by another UI.

While UI objects render above every other layer, objects part of UI do perserve their layering (layer, Z-order, tileset, blending, etc). It is not possible to differentiate between these sub-layers when using shaders or gradients, as they reference the entire UI layer.

UI objects do not follow the camera's movement, their position is set on-load and will remain static unless affected by other triggers. When marked as UI, they are moved to the default camera position (the initial camera position when loading the level in classic mode) based on their position relative to **UI Target**, their alignment settings and your device's aspect ratio.

Object part of UI can only collide with other UI objects. Hitboxes will no longer collide with the player and UI collision objects will only be able to collide with other UI collision objects. The chunk optimization is skipped by UI collisions, so all UI collisions will check all other UI collisions, just like when using Extended Collision.
