# Rotate Camera

Rotates the camera view.

## Options

The camera's current rotation can be changed using **Degrees**. Positive degrees rotate the camera clockwise, negative degrees rotate counter-clockwise. 
 
Can be animated using **Move Time** and **Easing**.

With **Add** enabled **Degrees** are added to the current rotation instead.

**Snap 360** snaps the target rotation to the nearest full 360 rotation, relative to the camera's current rotation. 

The resulting rotation formulas are:
- Default: $Target = Degrees$
- Add: $Target = Current + Degrees$
- Snap 360: $Target = Current - 180 + (Target - Current + 180) % 360

## Notes

Only one camera rotate trigger can be active at once, activating a new camera rotate trigger stops the previous one. If the new rotate trigger uses **Add**, the degrees value is added to the previous camera rotate's target.