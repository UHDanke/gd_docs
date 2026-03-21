# Area Mechanics

## Center

**Center Group ID** must be a single object, or have an ID Parent. If present, the ID Parent is used as the center. Group and Area Parents have no effect on the center.

P1 and P2 positions, as well as camera positions (center, edges, corners) can be used as the center.

If no valid center exists, the Area trigger uses the level's origin (0,0) coordinate as the center, which is 3 block units below the center of the editor guide axis.

## Object Linking

When linking multiple objects, they are treated as one object for the effects of Area triggers as long as an Area Parent or Group Parent is present.

Linked objects do not have to be part of the target group, however Group / Area Parents not part of the target group are ignored.

**Ignore Linked** ignores any object links present.

The trigger's effect is applied to all linked objects, even if they are not part of the target group.

## ID Parent Linking

ID Parents override object links.

If an ID Parent is present, the entire group is treated as one object for trigger effects. 

If no Area Parents or Group Parents are present, the ID Parent acts as both Group Parent and Area Parent. 

If an Area Parent or Group Parent is present on an object that is not the ID Parent, it will act as both Area and Group Parent.

If the ID Parent object is an Area/Group Parent, other Area/Group Parents in the same group are ignored.

**Ignore GParent** ignores the ID Parent.

Unlike object links, for group links the trigger effect is not applied to objects not part of the target group.

If the affected object is an ID Parent for another group, then the effect is applied to the entire group.

While object links need multiple objects to count as linked, you only need one ID Parent to create a linked group.

## Temporary Effects

Unlike their non-Area versions, the effects of Area triggers are temporary - the effect is applied only while the trigger is active and is undone when the trigger is paused or stopped.

Rotate and Scale trigger ignore Area effects when moving objects (by scaling or rotating groups), most other triggers will take into the account the current Area effect applied on the object.

## Timings

Area triggers are processed once per tick after all other moves. Collisions happen after Area triggers are processed.

Area effects are recalculated every game tick, 240 times per second.

## EffectIDs

**EffectIDs** are unique per type of Area trigger - spawning a new Area Move will overwrite any active Area Move with the same **EffectID**, but not other kinds of Area trigger like Area Scale, Rotate, etc.

**EffectID** 0 is not unique - there is no limit to how many triggers you can spawn using this ID.

## Order & Priority

### Order

Area triggers are processed in the following order: 
Area Scale 🡒 Area Rotate 🡒 Area Move 🡒 Area Fade / Area Tint

It is not possible to change this order with **Priority**.

### Priority

Area triggers (except Area Fade) have cumulative effects - **Priority** decides the order in which they are applied, from highest first to lowest last.

If there are multiple active triggers with the same **Priority**, then spawn order is used (oldest first to newest last).

## Multiple Areas

When multiple Areas target the same objects, they are processed first by Priority, then from oldest to newest. Consecutive Area triggers use the position of center and target objects after the effect of the previous Area trigger is applied - meaning that if you change the position of an object with an Area trigger, the next Area trigger will use the new position as reference.

### Multiple Instances

Normally, spawning the same Area trigger while an instance of it is already active updates the current active instance, it will not create new instances or override previous ones. This will also clear all active Edit Area effects on the trigger.

With spawn remapping, it is possible to create additional instances of the same Area trigger for unique sets of target, center and control IDs (only if control ID is not 0). The same target group can be affected by different centers and the same center can affect multiple different target groups.

As a result, it is not possible to use an Area trigger multiple times on the same set of groups. Using **EffectID** to ensure only one instance of Area is active is unnecessary in most cases. Stopping the Area trigger before spawning is only necessary for refreshing active instances or changing their order.

Special centers like **P1**, **P2**, **C**, etc override the default **Center Group ID** \- which can still be remapped, so it is possible to apply the same Area effect multiple times on the same group without needing to use multiple center groups if using a special center.

## Spawn Remapping

**Target Group ID** and **Center Group ID** can be remapped, **EffectID** and **Color Channel** (Area Tint) cannot be remapped.

While **EffectID**s are not remappable, ID 0 can be used to use the same Area trigger for multiple different groups. These instances can be stopped individually using a Control ID, but cannot be edited individually as only Group IDs or Effect IDs can be used, which are not remappable.


## Proximity Settings
<!-- @csv: data/tables/area_proximity.csv -->
|                                                **Image**                                                | **Proximity** | **Offset Direction** | **Inverted** | **Mirrored** |
| :-----------------------------------------------------------------------------------------------------: | :-----------: | :------------------: | :----------: | :----------: |
| <img src="https://github.com/user-attachments/assets/8d30a8f5-7813-49c6-b008-bee239b53811" width="50%"> |     Radial    |          X           |              |              |
| <img src="https://github.com/user-attachments/assets/b9e3d8a0-f7a5-4f50-abff-55bc8ea97878" width="50%"> |     Radial    |          X           |     Yes      |              |
| <img src="https://github.com/user-attachments/assets/24f5af6d-f09b-476f-80bf-90269069104f" width="50%"> |   Horizontal  |          X           |              |     Yes      |
| <img src="https://github.com/user-attachments/assets/e7a29b01-8bf9-4409-acf3-59734c621cbb" width="50%"> |   Horizontal  |          X           |     Yes      |     Yes      |
| <img src="https://github.com/user-attachments/assets/3148644d-6f9a-4bc6-92b1-e3fb5a816ab0" width="50%"> |   Horizontal  |          X           |              |              |
| <img src="https://github.com/user-attachments/assets/2bab4f43-e4fc-4afc-83cb-841c432dd181" width="50%"> |   Horizontal  |          X           |     Yes      |              |
| <img src="https://github.com/user-attachments/assets/ba9d01d7-066d-414f-bd5f-62c89ac6ec94" width="50%"> |    Vertical   |          Y           |              |     Yes      |
| <img src="https://github.com/user-attachments/assets/1c5da365-99c2-4c48-a0f3-db6878e16c25" width="50%"> |    Vertical   |          Y           |     Yes      |     Yes      |
| <img src="https://github.com/user-attachments/assets/11ae6d24-0702-499f-8f29-4d8b1beef073" width="50%"> |    Vertical   |          Y           |     Yes      |              |
| <img src="https://github.com/user-attachments/assets/d861d58b-622a-4bcf-b4c5-3fab9074c526" width="50%"> |    Vertical   |          Y           |              |              |
<!-- @end -->

## Effect Strength Coefficient

The effect of Area triggers varies depending on the distance between the center and targets, the strength coefficient represents the proportion of the effect applied for all Area triggers.

### Formulas

**Radial:**

$$\Delta = \sqrt{(Target_x - (Center_x + Offset))^2 + (Target_y - (Center_y + OffsetY))^2}$$

**Horizontal:**

$$\Delta = Target_X - ( Center_X + Offset )$$

**Vertical:**

$$\Delta = Target_Y - ( Center_Y + Offset )$$

**Mod:**

$$\Delta' = 
\begin{cases} 
\Delta \cdot M_b & \text{if } \Delta < 0 \text{ and not mirrored} \\ 
\Delta \cdot M_f & \text{if } \Delta \geq 0 \text{ and not mirrored} \\ 
|\Delta| \cdot M_b & \text{if } \Delta < 0 \text{ and mirrored} \\ 
|\Delta| \cdot |M_f| & \text{if } \Delta \geq 0 \text{ and mirrored} 
\end{cases}$$

**Length:**

$$Normalized = \frac{\Delta'}{Length}$$

**Deadzone:**

$$EffectStrength = \frac{Normalized - Deadzone}{1 - Deadzone}$$

**Clamped:**

$$EffectStrength = 
\begin{cases} 0 & \text{if } t < 0 \\ 
t & \text{if } 0 \leq t \leq 1 \\ 
1 & \text{if } t > 1 
\end{cases}$$

**Inverted:**

$$EffectStrength = 
\begin{cases} 
EffectStrength & \text{if not inverted} \\ 
1 - EffectStrength & \text{if inverted} 
\end{cases}$$

**Easing:**

$$EffectStrength = 
\begin{cases} 
\text{ease}(t, \text{Easing2}) & \text{if } \Delta \geq 0 \text{ and EaseOut} \\
\text{ease}(t, \text{Easing}) & \text{otherwise} 
\end{cases}$$

### Distance

Distance is calculated between center and affected object then multiplied by **ModFront** / **ModBack**.

The distance value is sensible to float and addition errors \- centering an object perfectly after it is moved is not always possible.

### Mod

For horizontal and vertical proximity, **ModBack** is applied if $CenterPos>TargetPos$ and **ModFront** is applied if $CenterPos<TargetPos$.

For the symmetrical options, the value of **Distance** is always positive when **ModFront** is applied, even if the value of **ModFront** is negative.

### Length and Deadzone

**Length** and **Deadzone** determine the strength of the effect at different distances, from a min of 0 to a max of 1.

If **Length** is 0 or **Deadzone** is 1, then the value steps directly between max and min.

The result is fed into the **Easing** function and is then used to calculate the strength of the effect applied.

### Ease Out

With **Ease Out** enabled, **Easing** is applied on **ModBack** and **Easing2** is applied on **ModFront**.

**Easing2** is mistakenly applied when using radial proximity, conflicting with **Easing**.

## Visibility

An object counts as not visible if its center is outside of the screen's edges by at least half a block.
Objects can take up to ~0.1333 seconds to count as not visible in some cases.

Area Fade and Area Tint effects do not apply if the target is not visible. For Area Move, Scale and Rotate, if an object is not visible the effect will stop being applied in certain cases.

Link Visible can be used to force objects to be visible to fix any issues regarding visibility.

## Random Values

Some variables can be randomized with the corresponding **\+/-** option (the offset). For example, with a value of 5 \+/- 1 a random value between 4 and 6 will be picked.
The formula used is:
$RandomValue=BaseValue+RandomCoefficient\cdot RandomOffset$

Different triggers can have different base values and offsets, but they all share the same random coefficients since they are per object. Shared parameters, like **Length**, have the same random coefficient for all types of Area trigger. This also applies to **OffsetY** and **Offset**.

The random coefficient (a random value between \+/-1) for each setting is determined from a massive float array of randomly generated values. While you can change the base value and offset of each setting, this will not randomize the values again, it is not possible to change random coefficients without restarting the level.

With linked objects, the Group Parent's random coefficients are used.

## Interactions

### Stop

Stop works on Area triggers but not on Edit Area triggers.

Stopping the Area trigger will also clear all active Area and Edit Area effects.

Pausing the Area trigger prevents it from applying its effect and pauses all of its active Edit Area effects.

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
