# Area Triggers

Changes the position, scale, rotation, color or opacity of objects and groups of objects from **Target ID** depending on their distance from a **Center ID**.

More info on common settings and behavior can be found on the area mechanics page.

## Area Move

Unique Settings:
- **MoveDist**
- **MoveAngle**
- **Relative**
- **RFade**
- **XY Mode**
- **MoveX**
- **MoveY**

### Behavior

Moves the object by the distance specified by **MoveDist**  (10 units \= 1 block unit) in the direction given by **MoveAngle**. **MoveAngle** is defined in degrees (360 degrees \= 1 rotation going counterclockwise) and the 0 degree point is down.

With **Relative** enabled each object moves in the opposite direction of the center (angle between object and center, offset by 180°). **Relative** overrides **MoveAngle**.

Angle is not affected by object rotation or by **ModFront** / **Modback** but it does take the center's **Offset** and **OffsetY** into account.

**MoveDist** is multiplied by the distance between target and center and then divided by **RFade** if **Relative** is enabled.

**XY Mode** replaces the angle and move settings with the cardinal movement settings **MoveX** and **MoveY**.

## Equations

### XY Movement

$X = XMove \cdot EffectStrength + X_{t}$

$Y = YMove \cdot EffectStrength + Y_{t}$

### Relative Movement

$$
\begin{aligned}
Distance= \sqrt{(VerticalOffset+Y_{c}-Y_{t})^{2}+(HorizontalOffset+X_{c}-X_{t})^{2}}
\end{aligned}
$$

$$
\begin{aligned}
Radius = 
  \begin{cases} 
    \dfrac{MoveDist \cdot EffectStrength \cdot Distance}{RFade} & \text{if } Distance < RFade \\
    MoveDist \cdot EffectStrength & \text{if } Distance \geq RFade 
  \end{cases}
\end{aligned}
$$

$Angle = \arctan(\frac{(Y_{c}-Y_{t}}{X_{c}-X_{t}})$

$X = Radius \cdot \cos(Angle) + X_{t}$

$Y = Radius \cdot \sin(Angle) + Y_{t}$

Where:
- **c** is position of center 
- **t** is position of target
- $VerticalOffset$ is **OffsetY** for radial and **Offset** for vertical proximity
- $HorizontalOffset$ is **Offset** for radial and horizontal proximity
- All values are assumed to be in units

## Area Rotate

Unique Settings:
- **Rotation**

### Behavior

Rotates objects and groups of objects by a number of degrees given by **Rotation** (360 degrees = 1 full rotation going clockwise).

## Area Scale

Unique Settings:
- **ScaleX**
- **ScaleY**

### Behavior

If linked, objects are scaled along the world XY axis, otherwise they are scaled along their own XY axis. Area Scale does not support relative rotation.

The scale effect applied is calculated using this formula:  
$$EffectScale=1+EffectStrength \cdot (Scale-1)$$

Where *Scale* is **ScaleX** or **ScaleY**.

If the scale value is negative, the object will be flipped around the respective axis.

Due to a bug with Area Scale solid object hitboxes become thin when scaled with a negative value.

Area Scale will not work if both X and Y scale are equal to 0. Objects can be scaled by 0 on one axis if the other axis is non-zero; To scale an object on both X and Y to 0 two Area Scale triggers are needed.

Area Scale is considered a scaling effect by Scale trigger's **Relative Scale** option.

## Area Fade

Unique Settings:
- **From Opacity**
- **To Opacity**

### Behavior

**From Opacity** is the opacity at maximum strength, while **To Opacity** is the opacity at minimum.

Unlike other Area triggers, Area Fade effects do not stack additively or multiplicatively with one another. When multiple Area Fade effects are applied on the same object, the one with the highest Effect Strength is applied regardless of the opacity value. If there is a tie, the first effect is used as determined by **Priority** and spawn order.

The effect multiplies with other opacity effects (Alpha trigger and color channel Opacity).

Area Fade does not have an **Easing** option.

Due to a bug, Area Fade effects stop working for one frame after the game is unpaused.

## Area Tint

Unique Settings:
- **Color Channel**
- **Tint**
- **HSV**
- **Main Only**
- **Secondary Only**

### Behavior

Area Tint is applied after other color effects (Color, Pulse, Copy Color).

The effect applied is calculated using this formula:  
$$Color =
  \begin{cases}
    ObjectColor & Tint \le 0 \\
    ObjectColor + Tint \cdot (ColorChannel - ObjectColor) & 0 < Tint < 1 \\
    ColorChannel & Tint \ge 1
  \end{cases}$$

Area Tint does not have an **Easing** option.

With **Main Only** or **Secondary Only** selected, only the Base, respectively Detail Color will be tinted.

Objects keep their blending and alpha values when tinted.

Area Tint ignores the Base / Detail Color setting of single-color objects.
