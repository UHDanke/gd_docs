# Area Triggers

## Virtual Effects

Unlike their non-Area versions, the effects of Area triggers are virtual \- the effect is temporary and is undone when the trigger is stopped.  
Area effects are recalculated every game tick, 240 times per second.  

Non-Area Move, Rotate and Scaling effects use the real position of the objects.  
However, triggers that target the position of an object will use the virtual position of the object.  
Triggers that use transformations (rotation or scaling) of an object as reference will use the virtual transform of the object.  

## Timings

Area triggers are processed once per tick after all other moves.  
The latest point at which you can call an Area trigger and still be processed within the same tick is from a Keyframe Spawn.  
Collisions happen after Area triggers are processed.

Move processing order:  
Keyframe 🡒 Scale 🡒 Rotate 🡒 Move 🡒 Advanced Follow Y 🡒 Advanced Follow 🡒 Follow 🡒 **Area**

## EffectIDs

**EffectID**s are unique per type of Area trigger; Spawning a new Area Move will overwrite any active Area Move with the same **EffectID**, but not other kinds of Area trigger like Area Scale, Rotate, etc.  
**EffectID** 0 is not unique - there is no limit to how many triggers you can spawn using this ID.

## Center

**Center Group ID** must be a single object, or have an ID Parent.   
If present, the ID Parent is used as the center.  
Group and Area Parents have no effect on the center.  
If no valid center exists, the Area trigger uses the level's origin (0,0) coordinate as the center, which is 3 block units below the editor guide axis.  
P1 and P2 positions, as well as camera positions (center, edges, corners) can be used as the center.  
**Center Group ID** can be identical to **Target Group ID**.

## Order & Priority

### Order

Area triggers are processed in the following order:  
Area Scale 🡒 Area Rotate 🡒 Area Move 🡒 Area Fade / Area Tint  
It is not possible to change this order with **Priority**.

### Priority

Area triggers have cumulative effects \- **Priority** decides the order in which they are applied, from highest first to lowest last.  
If there are multiple active triggers with the same **Priority**, then spawn order is used (oldest first to newest last).

## Multiple Areas

When multiple Areas target the same objects, they are processed first by Priority, then from oldest to newest.  
Consecutive Area triggers use the position of center and target objects after the effect of the previous Area trigger is applied. Meaning that if you change the position of an object with an Area trigger, the next Area trigger will use the new positions as reference.

### Multiple Instances

Normally, spawning the same Area trigger while an instance of it is already active updates the current active instance, it will not create new instances or override previous ones.  
Spawn order is unaffected by this.  
Edit Area effects will be stopped and undone.  
**EffectID** has no effect on this behavior.  
With spawn remapping, it is possible to create additional instances of the same Area trigger for unique sets of target, center and control IDs.  
The same target group can be affected by different centers and the same center can affect multiple different target groups.  
As a result, it is not possible to use an Area trigger multiple times on the same set of target and center ID. Using **EffectID** to ensure only one instance of Area is active is unnecessary in most cases. Stopping the Area trigger before spawning is only necessary for refreshing active instances or changing spawn order.  
Special centers like **P1**, **P2**, **C**, etc override the default **Center Group ID** \- which can still be remapped, so it is possible to apply the same Area effect multiple times on the same group without needing to use multiple center groups if using a special center.

## Spawn Remapping

**Target Group ID** and **Center Group ID** can be remapped.  
**EffectID** cannot be remapped.  
**Color Channel** (Area Tint) cannot be remapped.  
While **EffectID**s are not remappable, ID 0 can be used to use the same Area trigger for multiple different groups. These instances can be stopped individually using a Control ID, but cannot be edited individually as only **GroupID**s or **EffectID**s can be used, which are not remappable.

## Area Parents and Group Parents

If no Area Parents are present, the Group Parent acts as both Group Parent and Area Parent, and vice-versa.  
Group and Area Parents do not update dynamically, the choice is done at level start.  
With multiple Group Parents in the same link, the left-most, then bottom-most Group Parent is used. Likewise for Area Parents.  
The Group Parent is the center for the effect applied (Area Scale & Area Rotate).  
The Area Parent is the center used to calculate the distance from the Area trigger's center.  
With **DEAP** selected, the Area Parent will not be affected by the Area trigger. Linked objects will still be affected.  
**DEAP** ignores Area Parents not part of linked objects or linked groups.

## Object Linking

### Object Linking

When linking multiple objects, they are treated as one object for the effects of Area triggers as long as an Area Parent or Group Parent is present.  
Linked objects do not have to be part of the target group, however Group / Area Parents not part of the target group are ignored.  
**Ignore Linked** ignores any Area Links present.  
The Area trigger's effect is applied to all linked objects, even if they are not part of the target group.

### ID Parent Linking

If an ID Parent is present, the entire group is treated as one object for the effects of Area triggers.  
If no Area Parents or Group Parents are present, the ID Parent acts as both Group Parent and Area Parent.  
If an Area Parent or Group Parent is present on an object that is not the ID Parent, it will act as both Area and Group Parent.  
If the ID Parent object is an Area/Group Parent, other Area/Group Parents in the same group are ignored.

**Ignore GParent** ignores the ID Parent.  
ID Parents override object links.  
Unlike object links, for group links the area effect is not applied to objects not part of the target group.  
If the affected object is an ID Parent for another group, then the effect is applied to the entire group.
While object links need multiple objects to count as linked, you only need one ID Parent to create a linked group.  

## Visibility

An object counts as not visible if its center is outside of the screen's edges by at least half a block.  
Objects can take up to ~0.1333 seconds to count as not visible in some cases.  

Area Fade and Area Tint effects do not apply if the target is not visible.  
For Area Move, Scale and Rotate, if an object is not visible the effect will stop being applied in certain cases.

Link Visible can be used to force objects to be visible to fix any issues regarding visibility.

## Performance and Optimization

Area triggers reapply their effect every tick, so they put a constant strain on the processor. 
Lag components can be split in two categories:
- Strength calculations for each target
- Effect application

Out of the two, applying area effects is the much more demanding one.

Enter triggers are far more optimized and should not be replaced by Area triggers.

### Effect Strength

If the resulting effect strength is 0, no Area effect will be applied.

Certain proximity options will make the Area affect less (or more) targets depending on the strength calculation.

### Object Links

Transformations (Scale, Rotate) and color operations (Fade, Tint) are applied per object even when using object links.

Scaling and rotation on object links also applies movement on all objects linked to the target, which is done per object. This makes Area Scale and Rotate the laggiest Area triggers when using object links.

Movements are optimized for multiple objects, using object links with Area Move can make use of this optimization and significantly reduce lag. 

Overall, Area Move is the only Area trigger that sees a significant improvement from using object links. Area Fade and Tint have negligible increases from reducing the amount of targets that need to be calculated while Area Scale and Rotate are negatively impacted by it. 

### Fade and Tint

Area Fade and Tint effects are applied only on visible targets that are not toggled off. This includes completely transparent targets done using either the Hide object option, color blending, color opacity or Alpha triggers.

If there are multiple Area Fade triggers per target, all will do the strength calculation but only the strongest (or first) effect will be applied. This is not the case for other Area effects where all are applied.

### Scale, Rotate and Move

Whether Area Scale, Rotate and Move is applied on toggled off targets is inconsistent and depends on length and deadzone settings. Toggling off targets has no effect in most common cases, so toggling shouldn't be considered a reliable way to optimize these effects.

## Effect Strength Coefficient

The effect of Area triggers varies depending on the distance between the center and targets.  
The strength coefficient represents the proportion of the applied effect for all Area triggers.

### Distance
Distance is calculated between center and affected object then multiplied by **ModFront** / **ModBack**.  
**Offset** and **OffsetY** offset the position of the center after mod is applied.  
The distance value is sensible to float and addition errors \- centering an object perfectly after it is moved is not always possible.


Distance can be calculated using these formulas:

**c** is position of center  
**t** is position of target

#### Circular Proximity

$Distance=\sqrt{(OffsetY+Y_{c}-Y_{t})^{2}+(Offset+X_{c}-X_{t})^{2}}$

#### Horizontal Proximity

$Distance\=Offset+(X_{c}-X_{t})\cdot Mod$

#### Vertical Proximity

$Distance\=Offset+(Y_{c}-Y_{t})\cdot Mod$

### Mod

For radial proximity, Mod has no effect.  
For horizontal and vertical proximity, **ModBack** is applied if $CenterPos>TargetPos$ and **ModFront** is applied if $CenterPos<TargetPos$.  
For the symmetrical options, the value of **Distance** is always positive when **ModFront** is applied, even if the value of **ModFront** is negative.  
Offsets are not affected by mod.

### Ease Out

With **Ease Out** enabled, **Easing** is applied on **ModBack** and **Easing2** is applied on **ModFront**.  
**Easing2** is mistakenly applied when using radial proximity, conflicting with **Easing**.

### Length and Deadzone
**Length** and **Deadzone** determine the strength of the effect at different distances, from a min of 0 to a max of 1.  

If **Length** is 0 or **Deadzone** is 1, then the value steps directly between max and min.  
Otherwise, the value follows a linear equation bounded between \[1,0\] using the formula:

$EffectStrength_{\ |⟹}=\frac{Distance-Length\cdot Deadzone}{Length\cdot(1-Deadzone)}$

$EffectStrength_{\ |⟹}=1-EffectStrength_{\ |⟸}$

The result is fed into the **Easing** function and is then used to calculate the strength of the effect applied.  

<details>
<summary>Notations</summary>

* L = Length  
* Dz = Deadzone  
* Max - Distance value at max strength  
* Min - Distance value at min strength  
* Center - Strength value at distance 0  
* Sign - The sign of distance (positive or negative) where the strength is greater than min  
* Direction -  The direction (relative to the center) along which the strength value decreases  
</details>

#### Center ⟹ Edge

| Length | Deadzone | Max | Min | Center | Sign | Direction |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $L \gt 0$ | $Dz \gt 1$ | $\ge Dz\cdot L$ | $\le L$ | 0 | + |\|⟸|
| $L \gt 0$ | $Dz = 1$ | $\lt L$ | $\ge L$ | 1 | + |\|⟹|
| $L \gt 0$ | $0\lt Dz\lt 1$| $\le Dz\cdot L$ | $\ge L$ | 1 | + |\|⟹|
| $L \gt 0$ | $Dz = 0$ | $\le 0$ | $\ge L$ | 1 | + |\|⟹|
| $L \gt 0$ | $Dz \lt 0$ | $\le Dz\cdot L$ | $\ge L$ | $Dz/(Dz-1)$ | -/+ |\|⟹|
| $L = 0$ | $Dz \gt 1$ | $\gt 0$ | $\le 0$ | 0 | + |\|⟸|
| $L = 0$ | $Dz \le 1$ | $\lt 0$ | $\ge 0$ | 0 | - |\|⟸|
| $L \lt 0$ | $Dz \gt 1$ | $\le Dz\cdot L$ | $\ge L$ | 0 | - |\|⟸|
| $L \lt 0$ | $Dz = 1$ | $\gt L$ | $\le L$ | 1 | - |\|⟹|
| $L \lt 0$ | $0\lt Dz\lt 1$| $\ge Dz\cdot L$ | $\le L$ | 1 | - |\|⟹|
| $L \lt 0$ | $Dz = 0$ | $\ge 0$ | $\le L$ | 1 | - |\|⟹|
| $L \lt 0$ | $Dz \lt 0$ | $\ge Dz\cdot L$ | $\le L$ | $Dz/(Dz-1)$ | -/+ |\|⟸|

#### Center ⟸ Edge

| Length | Deadzone | Max | Min | Center | Sign | Direction |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $L \gt 0$ | $Dz \gt 1$ | $\le L$ | $\ge Dz\cdot L$ | 1 | + |\|⟹|
| $L \gt 0$ | $Dz = 1$ | $\ge L$ | $\lt L$ | 0 | + |\|⟸|
| $L \gt 0$ | $0\lt Dz\lt 1$| $\ge L$ | $\le Dz\cdot L$ | 0 | + |\|⟸|
| $L \gt 0$ | $Dz = 0$ | $\ge L$ | $\le 0$ | 0 | + |\|⟸|
| $L \gt 0$ | $Dz \lt 0$ | $\ge L$ | $\le Dz\cdot L$ | $1/(1-Dz)$ | -/+ |\|⟸|
| $L = 0$ | $Dz \gt 1$ | $\le 0$ | $\gt 0$ | 1 | + |\|⟹|
| $L = 0$ | $Dz \le 1$ | $\ge 0$ | $\lt 0$ | 1 | - |\|⟹|
| $L \lt 0$ | $Dz \gt 1$ | $\ge L$ | $\le Dz\cdot L$ | 1 | - |\|⟹|
| $L \lt 0$ | $Dz = 1$ | $\le L$ | $\gt L$ | 0 | - |\|⟸|
| $L \lt 0$ | $0\lt Dz\lt 1$| $\le L$ | $\ge Dz\cdot L$ | 0 | - |\|⟸|
| $L \lt 0$ | $Dz = 0$ | $\le L$ | $\ge 0$ | 1 | - |\|⟸|
| $L \lt 0$ | $Dz \lt 0$ | $\le L$ | $\ge Dz\cdot L$ | $1/(1-Dz)$ | -/+ |\|⟹|

## Proximity Settings

| Image | No. | Area | Direction | ModBack | ModFront | Offset |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| <img src="https://github.com/user-attachments/assets/8d30a8f5-7813-49c6-b008-bee239b53811" width="50%"> | 1 | Circular | \|⟹ | No Effect | No Effect | X axis |
| <img src="https://github.com/user-attachments/assets/b9e3d8a0-f7a5-4f50-abff-55bc8ea97878" width="50%"> | 2 | Circular | \|⟸ | No Effect | No Effect | X axis |
| <img src="https://github.com/user-attachments/assets/24f5af6d-f09b-476f-80bf-90269069104f" width="50%"> | 3 | Horizontal | \|⟹ | Left | Right, Absolute | X axis |
| <img src="https://github.com/user-attachments/assets/e7a29b01-8bf9-4409-acf3-59734c621cbb" width="50%"> | 4 | Horizontal | \|⟸ | Left | Right, Absolute | X axis |
| <img src="https://github.com/user-attachments/assets/3148644d-6f9a-4bc6-92b1-e3fb5a816ab0" width="50%"> | 5 | Horizontal | \|⟹ | Left | Right | X axis |
| <img src="https://github.com/user-attachments/assets/2bab4f43-e4fc-4afc-83cb-841c432dd181" width="50%"> | 6 | Horizontal | \|⟸ | Left | Right | X axis |
| <img src="https://github.com/user-attachments/assets/ba9d01d7-066d-414f-bd5f-62c89ac6ec94" width="50%"> | 7 | Vertical | \|⟹ | Down | Up, Absolute | Y axis |
| <img src="https://github.com/user-attachments/assets/1c5da365-99c2-4c48-a0f3-db6878e16c25" width="50%"> | 8 | Vertical | \|⟸ | Down | Up, Absolute | Y axis |
| <img src="https://github.com/user-attachments/assets/11ae6d24-0702-499f-8f29-4d8b1beef073" width="50%"> | 9 | Vertical | \|⟸ | Down | Up | Y axis |
| <img src="https://github.com/user-attachments/assets/d861d58b-622a-4bcf-b4c5-3fab9074c526" width="50%"> | 10 | Vertical | \|⟹ | Down | Up | Y axis |

## Specific Settings & Behavior

### Area Move

<details>
<summary>Unique Settings</summary>

- **MoveDist**  
- **MoveAngle**  
- **Relative**  
- **RFade**  
- **XY Mode**  
- **MoveX**  
- **MoveY**
</details>

#### Behavior

Moves the object by the distance specified by **MoveDist**  (10 units \= 1 block unit) in the direction given by **MoveAngle**.  
**MoveAngle** is defined in degrees (360 degrees \= 1 rotation going counterclockwise) and the 0 degree point is down.  
With **Relative** enabled each object moves in the opposite direction of the center (angle between object and center, offset by 180°). **Relative** overrides **MoveAngle**.  
Angle is not affected by object rotation.  
Angle is not affected by **ModFront** / **Modback**.  
Center of angle is affected by **Offset** and **OffsetY**.  
**MoveDist** is multiplied by the distance between target and center and then divided by **RFade** if **Relative** is enabled.  
**XY Mode** replaces the angle and move settings with the cardinal movement settings **MoveX** and **MoveY**.

#### Equations

##### XY Movement

$X = XMove \cdot EffectStrength + X_{t}$  
$Y = YMove \cdot EffectStrength + Y_{t}$

##### Relative Movement

$Distance=\sqrt{(VerticalOffset+Y_{c}-Y_{t})^{2}+(HorizontalOffset+X_{c}-X_{t})^{2}}$

$Radius = (3\cdot MoveDist) \cdot EffectStrength\cdot \min(\frac{Distance}{RFade},1)$

$Angle = \arctan(\frac{(Y_{c}-Y_{t}}{X_{c}-X_{t}})$

$X = Radius \cdot \cos(Angle) + X_{t}$  
$Y = Radius \cdot \sin(Angle) + Y_{t}$

Where:  
**c** is position of center  
**t** is position of target  
$VerticalOffset$ is **OffsetY** for radial and **Offset** for vertical proximity.  
$HorizontalOffset$ is **Offset** for radial and horizontal proximity.  

### Area Rotate

<details>
<summary>Unique Settings</summary>

- **Rotation**
</details>


**Rotation**

#### Behavior

Rotates objects by a number of degrees given by **Rotation** (360 degrees \= 1 rotation going clockwise).   
Move effects (except Area Move) are also rotated.  
The hitbox of solid objects is always in line with the coordinate system. While the visual rotates by any degree given, the hitbox can only rotate in increments of 90 degrees. If the rotation value is between 90 degree increments, then the hitbox is going to be sized up so the rotated object would fit inside. 

### Area Scale

<details>
<summary>Unique Settings</summary>

- **ScaleX**  
- **ScaleY**
</details>

#### Behavior

If not linked, objects are scaled along their own XY axis.  
If linked, objects are scaled along the world XY axis.  
Area Scale does not support relative rotation.

The scale effect applied is calculated using this formula:

$EffectScale=1+EffectStrength \cdot (Scale-1)$

Where *Scale* is **ScaleX** or **ScaleY**.

If the scale value is negative, the object will be flipped around the respective axis.   
Due to a bug with Area Scale solid object hitboxes become thin when scaled with a negative value.  
Area Scale will not work if both X and Y scale are equal to 0. Objects can be scaled by 0 on one axis if the other axis is non-zero; To scale an object on both X and Y to 0 two Area Scale triggers are needed.  
Area Scale is considered a scaling effect by Scale trigger's **Relative Scale** option.     
The degree of slopes can be changed using transform effects like object warping or Area Scale.  
Move effects (except Area Move and Area Rotate) are also scaled.

### Area Fade

<details>
<summary>Unique Settings</summary>

- **From Opacity** 
- **To Opacity**
</details>

#### Behavior

**From Opacity** is the opacity at maximum strength, while **To Opacity** is the opacity at minimum.  
Unlike other Area triggers, Area Fade effects do not stack additively or multiplicatively with one another. When multiple Area Fade effects are applied on the same object, the one with the highest Effect Strength is applied regardless of the opacity value. If there is a tie, the first effect is used as determined by **Priority** and spawn order.  
The effect multiplies with other opacity effects (Alpha trigger and color channel Opacity).  
Area Fade does not have an **Easing** option.  
Due to a bug, Area Fade effects stop working for one frame after the game is unpaused.

### Area Tint

<details>
<summary>Unique Settings</summary>

- **Color Channel**  
- **Tint**  
- **HSV**  
- **Main Only**  
- **Secondary Only**
</details>

#### Behavior

Area Tint is applied after other color effects (Color, Pulse, Copy Color).

The effect applied is calculated using this formula:  
$Color=ObjectColor+Tint(ColorChannel-ObjectColor)$  
$ObjectColor \le Color \le ColorChannel$

For $Tint \le 0$ no tint is applied.  
For $0 \lt Tint \lt 1$ the max tint is proportional to **Tint**.  
For $Tint = 1$ at max tint the object color is equal to **Color Channe**l.  
For $Tint \gt 1$ the strength of the tint applied is increased, but still maxes out at the color given by **Color Channel**.

Area Tint does not have an **Easing** option.  
With **Main Only** or **Secondary Only** selected, only the Base, respectively Detail Color will be tinted.  
Objects keep their blending and alpha values when tinted.  
Area Tint ignores the Base / Detail Color setting of single-color objects.

## Random Values

Some variables can be randomized with the corresponding **\+/-** option (the offset). For example, with a value of 5 \+/- 1 a random value between 4 and 6 will be picked.  
The formula used is:  
$RandomValue=BaseValue+RandomCoefficient\cdot RandomOffset$

The random coefficient (a random value between \+/-1) for each setting is calculated per object at level start.

Different triggers can have different base values and offsets, but they all share the same random coefficients since they are defined per object.  
While you can change the base value and offset of each setting, this will not randomize the values again.  
It is not possible to change random coefficients without restarting the level.  
With linked objects, the Group Parent's random coefficients are used.  
Shared parameters, like **Length**, have the same random coefficient for all types of Area trigger. This also applies to **OffsetY** and **Offset**. 

<br>

# Edit Area Triggers

Edits the parameters of an active Area Trigger.

## Area Options

<details>
<summary>Common</summary>

- **Duration**  
- **Easing**  
- **GroupID**  
- **EffectID**  
- **Use EffectID**
- **Offset**  
- **OffsetY**  
- **ModFront**  
- **ModBack (BK)**  
- **Deadzone**
</details>

<details>
<summary>Area Move</summary>

- **MoveDist**  
- **MoveAngle**  
- **RFade**  
- **XY Mode**  
- **MoveX**  
- **MoveY**
</details>

<details>
<summary>Area Rotate</summary>

- **Rotation**
</details>

<details>
<summary>Area Scale</summary>

- **ScaleX**  
- **ScaleY**
</details>

<details>
<summary>Area Fade</summary>

- **(To) Opacity**
</details>

<details>
<summary>Area Tint</summary>

- **Tint %**  
- **Edit HSV**  
- **Use HSV**
</details>


## Behavior

Settings are independent of each other. The values of different settings can be changed by different triggers independently of one another with their own **Duration** and **Easing**.  
Settings with value *NaN* are not affected.  
Spawning an Area trigger again will stop and undo active Edit Area effects.

### Multiple Instances

There can be only one Edit Area effect active for each setting of an Area trigger.   
New effects override previous ones. When overriding, the new Edit Area effect will start from where the previous effect stopped.  
When calling multiple Edit Area triggers that edit the same settings, the last one will override all previous ones.  
Edit Area will override other active Edit Areas only if **Duration** is bigger than 0\. This is likely a bug.

### Settings

**EffectID** and **GroupID** can both be remapped.  
**EffectID** 0 will edit all Area triggers without an **EffectID**.  
**Duration** is the time it takes to transition between the old and new set of values, this is affected by the **Easing** option.  
**Easing** does not change the Area trigger's easings.  
**XY Mode** only changes which settings are displayed, an Edit Area Move trigger can affect both Angle and XY Mode Area triggers at the same time.  
**Tint %** and **Set HSV** can be edited at the same time by one Edit Area Tint trigger.  
There is no option to change the **From Opacity** setting of an Area Fade trigger.

<br>

# Area Stop

Stops an active Area trigger using its **EffectID**.  
**EffectID** can be remapped.  
**EffectID** 0 will stop all Area triggers without an **EffectID**.

<br>

# Other Notable Interactions

### Stop

Stop works on Area triggers.  
Paused Area triggers do not apply their effect.

Stop does not work on Edit Area.    
Stopping the Area trigger will undo and stop all active Area and Edit Area effects.    
Pausing the Area trigger itself pauses all of its active Edit Area effects.

### Toggle

Toggle disables Area effects on targets only in certain cases, (for example - **Length** is negative and using a Center ⟹ Edge proximity), otherwise has no effect.

### Follow

Follow does not copy Area movements.

### Gradient

Gradients are not affected by Area Tint. 

Gradient Rotation is not affected by Area Rotate outside of the editor.

### Enter

Area triggers are not affected by movements caused by Enter triggers.

### Particle Objects

Particle effects are affected by Area triggers.

### Spawn Particle

Particles created using Spawn Particle ignore Area effects on the particle object.

### Advanced Follow

Advanced Follow works on objects and supports object links.  
Area effects happen after Advanced Follow movements.  
Advanced Follow targeting is affected by Area effects. Due to this, certain interactions can create loops or crash / freeze the game.  
Using DEAP with Advanced Follow is recommended.

### Rotate

Aim and Follow modes use the object's virtual rotation instead of the real rotation, so using Area Rotate to offset these rotations will not work as they will constantly try to override the rotation made by Area Rotate.

### Scale

Relative Scale and Relative Rotation use the object's virtual scale or rotation as reference.
