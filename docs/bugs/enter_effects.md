# Enter Effects

## [FIXED] Enter trigger crash

**Version:** 2.208
**Date:** Sat Jan 31 2026 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
If you try to call 2 different Enter triggers with the same Enter Channel and Effect IDs but different values for the same variables, the game will crash in playtesting.

## Enter trigger portals

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
Using Enter trigger effects on portals and other objects composed of multiple objects only affects the foreground layer of portal objects.

## Legacy Enter triggers cannot be spawned

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
Legacy (pre-2.2) Enter triggers cannot be spawned with the Spawn Trigger option. Touch Trigger does work however.

## Enter Scale & Rotate apply real scaling and rotation on target objects

**Version:** 2.207
**Date:** Fri Dec 19 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
There seems to be no difference between Enter and Area Scale & Rotate. Examples of things affected by this bug: - Keyframe objects get scaled / rotated which can cause keyframes to apply scaling & rotation wrongly - Rotate Follow will copy the rotation of an object affected by Enter Rotate
