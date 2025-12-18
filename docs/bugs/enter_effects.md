# Enter Effects

## [2.207] [18/12/25] Enter trigger crash

If you try to call 2 different Enter triggers with the same Enter Channel and Effect IDs but different values for the same variables, the game will crash in playtesting.

## [2.207] [18/12/25] Enter trigger portals

Using Enter trigger effects on portals and other objects composed of multiple objects only affects the foreground layer of portal objects.

## [2.207] [18/12/25] Legacy Enter triggers cannot be spawned

Legacy (pre-2.2) Enter triggers cannot be spawned with the Spawn Trigger option.
Touch Trigger does work however.

## [2.207] [19/12/25] Enter Scale & Rotate apply real scaling and rotation on target objects

There seems to be no difference between Enter and Area Scale & Rotate.

Examples of things affected by this bug:
- Keyframe objects get scaled / rotated which can cause keyframes to apply scaling & rotation wrongly
- Rotate Follow will copy the rotation of an object affected by Enter Rotate
