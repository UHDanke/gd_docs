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