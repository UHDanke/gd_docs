
# Animate Trigger

Animates monsters and other objects with the **Animate on Trigger** setting (animations, particles).

<details>
<summary>[2.207] All objects affected by Animate Trigger</summary>

- 918, 920, 921, 923, 924
- 1050, 1051, 1052, 1053, 1054
- 1329
- 1516, 1518, 1519, 1583, 1584, 1591, 1592, 1593
- 1614, 1618, 1697, 1698, 1699
- 1839, 1840, 1841, 1842, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1860
- 1936, 1937, 1938, 1939
- 2012, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2065
- 2223, 2246
- 2605, 2629, 2630, 2694
- 2864, 2865, 2867, 2868, 2869, 2870, 2871, 2872, 2873, 2874, 2875, 2876, 2877, 2878, 2879, 2880, 2881, 2882, 2883, 2884, 2885, 2886, 2887, 2888, 2889, 2890, 2891, 2892, 2893, 2894
- 3001, 3002, 3119, 3120, 3121, 3219, 3303, 3304, 3482, 3483, 3484, 3492, 3493
- 4211, 4300
</details>

## Behavior

### Monsters

Makes the targeted monsters switch to the animation given by **Animation ID**. **Animation IDs** are used only by monsters and have no effect on any other object.

The transition between animations is done smoothly over a period of 0.05 seconds. If the animation is already active, then it'll reset to the beginning.

Invalid IDs play the default animation (ID 0).


<details>
<summary>Big (918)</summary>

- 0: bite
- 1: attack01
- 2: attack01_end
- 3: idle01
</details>

<details>
<summary>Bat (1584)</summary>

- 0: idle01
- 1: idle02
- 2: idle03
- 3: attack01
- 4: attack02
- 5: attack02_end
- 6: sleep
- 7: sleep_loop
- 8: sleep_end
- 9: attack02_loop
</details>

<details>
<summary>Spikeball (2012)</summary>

- 0: idle01
- 1: idle02
- 2: toAttack01
- 3: attack01
- 4: attack02
- 5: toAttack03
- 6: attack03
- 7: idle03
- 8: fromAttack03
</details>


### Particles

Animates particle objects with the **Animate on Trigger** property. Any remaining particles still connected to the target object are cleared when activated by Animate Trigger.

Animated particle objects start inactive until activated by Animate Trigger. If emitter duration is infinite, the particles will continue to spawn indefinitely as long as they are active. If duration is non-infinite, the particles will spawn once without looping.

Inactive particle objects are ignored if they have the **Only if Active** property.

### Animated Objects

Animates objects with the **Animate on Trigger** property. The animation plays once from the start and does not loop. 

Animated objects start invisible if on-screen but will be visible if reloaded, they will turn invisible once the animation ends. 

Inactive objects are ignored if they have the **Only if Active** property.

**Single Frame** and **Offset Anim** properties are ignored when animating.

<br>

# Edit Animation Settings

Allows editing the playback settings of animated objects, accessible from the Edit Special button.

## Options

**Randomize Start** is assigned by default on some animated objects, but currently does nothing.

**Use Speed** multiplies the animation's playback by the **Speed** option and removes the random start offset on selected objects if **Speed** is not 0. Negative **Speed** values can also be used.

**Animate on Trigger** makes the animation play from the start when activated by an Animate trigger, the animation plays once and does not loop. Animated objects start invisible if on-screen but will be visible if loaded later, they will turn invisible once the animation ends. Inactive objects (toggled off or offscreen) are ignored if **Only if Active** is selected.

**Disable Delayed Loop** removes the random delay some animations have between loops.

**Disable AnimShine** removes the white texture from a few animated objects. This property is removed by the game if used on objects this option has no effect on.

**Single Frame** makes the animation freeze on the selected frame. **Offset Anim** offsets the animation by the frame amount set in **Single Frame** instead. Objects animated by **Animate on Trigger** will not be offset.

## Notes

Monsters (918,1327,1328,1584,2012) and animated ground spikes (919) do not have an animation menu and cannot have these properties applied to them through save file editing.

Checkpoint objects (2063) have their elements move overtime, but this does not count as an animation and like monsters they are not affected by animation settings. 

The coin collectible object (1614) can be edited, but the menu is overriden by the Edit Pickup Settings menu and it is only accessible if you also select an animated object.

Scale circles (1839,1840,1841,1842) do not have animation frames and instead scale and fade overtime. **Use Speed** is force selected by the game and frame options like **Single Frame** and **Offset Anim** have no effect.

Similarly, some gameplay elements (orbs) and decorations scale in sync with the music. They do not count as animated objects and thus are not affected by animation settings.

The lava bubble objects (1591,1593) ignore all animation settings except **Animate on Trigger** and **Only if Active**. Additionally, 1591 is randomized between 3 possible animations on level load.

The laser wall object (1697) has some of its frames randomized regardless of any settings used.

**Disable AnimShine** works on only 3 objects (2046,2047,2055).

## [2.207] Animated Objects

### Properties
<details>
<summary>All objects affected by Edit Animation</summary>

- 920, 921, 923, 924
- 1050, 1051, 1052, 1053, 1054
- 1329
- 1516, 1518, 1519, 1583, 1591, 1592, 1593
- 1614, 1618, 1697, 1698, 1699
- 1839, 1840, 1841, 1842, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1860
- 1936, 1937, 1938, 1939
- 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055
- 2223, 2246
- 2605, 2629, 2630, 2694
- 2864, 2865, 2867, 2868, 2869, 2870, 2871, 2872, 2873, 2874, 2875, 2876, 2877, 2878, 2879, 2880, 2881, 2882, 2883, 2884, 2885, 2886, 2887, 2888, 2889, 2890, 2891, 2892, 2893, 2894
- 3001, 3002
- 3119, 3120, 3121, 3219
- 3303, 3304
- 3482, 3483, 3484, 3492, 3493
- 4211, 4300
</details>

<details>
<summary>Not random or delayed</summary>
  
- 1050, 1051, 1052, 1053, 1054, 1329, 1592, 1614
- 2605, 2694
- 3001, 3002
- 4211
</details>

<details>
<summary>Random start</summary>
  
- 920, 921, 923, 924, 
- 1516, 1518, 1519, 1583
- 1618, 1697, 1698, 1699
- 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1860
- 1936, 1937, 1938, 1939
- 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055
- 2223, 2246
- 2629, 2630
- 2864, 2865, 2867, 2869, 2871, 2872, 2873, 2874, 2875, 2876, 2877, 2878, 2879, 2880, 2881, 2882, 2883, 2884, 2885, 2886, 2887, 2888, 2889, 2890, 2891, 2892, 2893, 2894
- 3119, 3120, 3121, 3219
- 3303, 3304
- 3482, 3483, 3484, 3492, 3493
- 4300
</details>

<details>
<summary>Delayed loop</summary>

- 921
- 1519
- 1618
- 1851, 1852, 1854, 1855, 1856, 1860
- 2020, 2021, 2022, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2033, 2035, 2036, 2037, 2038, 2039, 2040, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055
- 2867, 2868, 2869, 2870, 2871, 2872, 2875, 2876, 2877, 2878, 2880, 2882, 2883, 2885, 2886, 2887
</details>

<details>
<summary>Pixelated</summary>

- 2223, 2246, 2605, 2629, 2630, 2694
- 3119, 3120, 3121, 3219, 3303, 3304, 3482, 3483, 3484, 3492, 3493
- 4211, 4300
</details>

### Frame Delay

Objects animated using scale, rotate, move or fade effects animate smoothly every frame. Monster animation transitions are also done smoothly.

Most other animated objects are made up of multiple sequential frames with a set frame delay between each frame.

#### Monsters

<details>
<summary>Big (918)</summary>

- 0: 0.0250
- 1: 0.0250
- 2: 0.0250
- 3: 0.0500
</details>

<details>
<summary>Big Spiked (1327)</summary>

- 0: 0.0600
</details>

<details>
<summary>Small Spiked (1328)</summary>

- 0: 0.0600
</details>

<details>
<summary>Bat (1584)</summary>

- 0: 0.0600
- 1: 0.0600
- 2: 0.0600
- 3: 0.0600
- 4: 0.0600
- 5: 0.0600
- 6: 0.0600
- 7: 0.1000
- 8: 0.0600
- 9: 0.0500
</details>

<details>
<summary>Spikeball (2012)</summary>

- 0: 0.0600
- 1: 0.0600
- 2: 0.0450
- 3: 0.0600
- 4: 0.0600
- 5: 0.0400
- 6: 0.0400
- 7: 0.0600
- 8: 0.0500
</details>

#### Animated

<details>
<summary>Delay 0.0250</summary>

- 2892
</details>

<details>
<summary>Delay 0.0333</summary>

- 2893
</details>

<details>
<summary>Delay 0.0400</summary>

- 2047
</details>

<details>
<summary>Delay 0.0450</summary>

- 1053
- 1592
</details>

<details>
<summary>Delay 0.0500</summary>

- 1050, 1051, 1052,
- 1516, 1518
- 1618
- 1860
- 2020, 2021, 2022, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055
- 2869, 2870, 2871, 2872, 2873, 2874, 2875, 2876, 2880, 2881, 2882, 2883, 2884, 2885, 2886, 2890, 2891, 2894
- 3001, 3002
</details>

<details>
<summary>Delay 0.0600</summary>

- 1054
- 1519
- 1697, 1698, 1699
- 1855, 1857
- 2023
- 2864, 2865, 2867, 2868, 2877, 2878, 2879, 2887, 2888, 2889
</details>

<details>
<summary>Delay 0.0700</summary>

- 1849, 1851, 1852, 1854, 1856
- 1936, 1937, 1938, 1939
</details>

<details>
<summary>Delay 0.0800</summary>

- 920, 921, 923, 924,
- 1583
- 1853, 1858
- 2034
- 4300
</details>

<details>
<summary>Delay 0.1000</summary>

- 1850
- 2223, 2246
- 2605, 2629, 2630
</details>

<details>
<summary>Delay 0.1150</summary>

- 1329
</details>

<details>
<summary>Delay 0.1200</summary>
- 1591
- 1614
- 3303, 3304
- 3482, 3483, 3484, 3492, 3493
- 4211
</details>

<details>
<summary>Delay 0.1300</summary>

- 1591
- 1593
</details>

<details>
<summary>Delay 0.1600</summary>

- 2694
- 3119
- 3120
- 3121
- 3219
</details>

<br>

# Spawn Particle

<br>

# Particle Object

Allows the creation of custom particle effects tied to objects. 

## Behavior

Particles animate by frame, not by tick. Visuals are going to differ between devices with different framerates - particles with very high emissions will not look as smooth on lower framerates and have more clumps if not randomized.

Particles have a softcap of 100k particles active at once, if the softcap is hit any further particle objects that become active will not spawn particles until reloaded. The softcap can be passed by an emitter that goes over the limit. The total particle count is calculated based on the emitter's max particle property, not its current particle count, so avoid oversizing the value of max particle. The particle softcap is not used in the level editor.

Particle objects do not unload correctly in normal mode, but they do in the editor. Emitters tied to particle objects are not cleared if the object is unloaded, and continue being active until they despawn on their own. These emitters are disconnected from the object that created them, so any particle setting that depends on the parent object will stop updating. When the particle object becomes active again, it will create a new emitter separate from the previous one.

## Particle Editor

Particle properties can be edited from the Particle Editor accessible from Edit Special.

The editor is split into 4 main tabs (Motion, Visual, Extra & Texture) with an interactible preview on the bottom left side of the menu.

### Randomization

Most particle variables can be randomized in a range using a **+-** variable found next to the base one.

<details>
<summary>Randomized settings</summary>

- **Lifetime +-**
- **Angle +-**
- **Speed +-**
- **AccelRad +-**
- **AccelTan +-**
- **StartRad +-**
- **EndRad +-**
- **RotSec +-**
- **StartSize +-**
- **EndSize +-**
- **StartSpin +-**
- **EndSpin +-**
- **Start_R +-**
- **Start_G +-**
- **Start_B +-**
- **Start_A +- **
- **End_R +-**
- **End_G +-**
- **End_B +-**
- **End_A +-**
- **Fade In +-**
- **Fade Out +-**
- **FrictionP +-**
- **FrictionS +-**
- **FrictionR +-**
- **Respawn +-**
</details>

### Copy Paste

**C** and **P** can be used to copy & paste the particle settings between different particle objects. Copied settings are lost when exiting the editor.

### Interactible Preview

Previews the current particle effect. The preview is interactible and can be used to pan around or change some particle effects by touch.

Options 1, 2 and 3 change what settings are being edited by touching the preview. Only one can be active at a time, and if none are selected dragging pans the preview. Options can be deselected by clicking them once again.

Options edit different settings for Gravity and Radius modes, these are:

Gravity
- Option 1: PosVar X & PosVar Y (rendered as green rectangle) 
- Option 2:  Gravity X & Gravity Y (cyan line)
-Option 3: Speed & Angle (yellow line, angle random is represented as a yellow semicircle but is not edited)

Radius
- Option 1: StartRad (green semicircle)
- Option 2: EndRad (orange semicircle)
- Option 3: Angle (not represented, all options render at once, semicircle arc depends on angle random, if 0 none render)

Two more buttons, **C** and a color box affect the preview box. **C** recenters the screen back to the particle's origin, the preview's background color can be set from the preview box - it is black by default and is reset when closing the menu.

### Motion

Particle settings that affect motion and emission behavior. Two motion modes are available - **Gravity** and **Radius**.

#### Common

**Max Particles** is the max amount of particles that can be active at once, any further particles will fail to spawn. 

**Duration** is the amount of time the emitter spawns particles. The emitter spawns particles until **Duration** runs out, and once the lifetime of all remaining particles expires then the emitter despawns and is replaced by another emitter by the particle object. **Duration** is infinite if set to -1 so the emitter will not stop spawning particles unless the particle object is unloaded. If value is 0 particles will not spawn unless **Emission** is -1.

**Lifetime** is the lifetime of the particle.

**Emission** is the amount of particles that can spawn per second. **Emission** also delays the first particle spawn by $1/Emission$ seconds, if the delay is bigger than **Duration** then no particles will spawn. If **Emission** is -1 then emission is infinite - the emitter will try to respawn all particles every frame without delay. **Max** sets **Emission** to -1, **Calc** calculates **Emission** using the formula $MaxParticle/(Lifetime+LifetimeRand)$.

**Angle** is the starting angle of the particle's motion. The value is given in degrees with 0 pointing right, positive values offset the angle clockwise and negative ones offset counter-clockwise.

#### Gravity

**Speed** is the particle's starting velocity, given in units (small steps) per second. All acceleration settings change the particle's velocity by $accel/100$ units per second.

**PosVar X** and **PosVar Y** give a range in units that randomize the particle's offset on the X and Y axis from the emitter's origin.

**Gravity X** and **Gravity Y** applies acceleration on the X and Y axes towards positive values, negative values accelerate away from positive and towards negative instead.

**AccelRad** applies acceleration away from the emitter's origin for positive values and towards the origin for negative ones.

**AccelTan** applies acceleration tangential to the particle's current direction, positive values accelerate clockwise while negative ones counter-clockwise.

**AccelRad** and **AccelTan** are not applied if velocity is null.

#### Radius

**StartRad** and **EndRad** are  the radial distances in units the particle starts from and ends at respectively. This movement is unaffected by **FrictionP**.

**RotSec** is the amount of degrees per second by which particles rotate around the emitter's center. Rotation is done in whole degree increments, so at low values the rotation is choppy.

### Visual

Particle settings that affect scaling, rotation and color (RGBA) values.

#### Scale & Rotation

**StartSize** is the particle's initial scale, while **EndSize** is its final scale. Scale 16 is equivalent to the scale of the object variant of the particle.

**StartSpin** is the initial rotation of the particle texture, while **EndSpin** is its final rotation. This rotation offsets texture rotations done by **Start Rot is Dir** and **Dynamic Rotation**. 

#### Colors

Start and End RGB values for the particles can be set in two ways:
- Using the two color pickers found on the top left of the menu
- Individual Start and End variables for each color channel, normalized to 1.00 (**Start_R**,  **Start_B**,  **Start_G**, **End_R**, **End_B**,  **End_G**)

The **<>** button next to the color selectors copies the main color to the secondary color. Changing the color from the color picker updates the RGB variables instantly, but changing the RGB variables updates the colors from the picker only when you reopen the particle editor.
Particle objects store RGBA as normalized values with 1% accuracy, rounding to the nearest value when converted to 8-bit RGBA.

Alpha cannot be set from the color picker, it can only be edited using the two **Start_A** and **End_A** variables. 

### Extra

Miscellaneous particle settings and extra options that do not fit in other tabs.

#### Free, Relative & Grouped
**Free**, **Relative** and **Grouped** change what point of reference the particles are relative to (camera, world, object)

- **Free** makes the particles copy the opposite of both the camera and the object's movement (particles appear relative to camera).
- **Relative** makes the particles copy the opposite of the object's movement. (particles appear relative to world).
- **Grouped** is default and applies no extra movement (particles appear relative to emitter).

How the particle object's scaling and rotation affects the spawned particles is different between **Free** / **Relative** and **Grouped**:
- With **Grouped**, the particle object can be scaled, warped and rotated as any other object.
- With **Free** & **Relative**, the game adds a special property to the particle object when you save the level which makes particles ignore the object's scale, warp and rotate; ignore rotations done by rotate triggers; if scaled by a trigger, scale the particles by either X or Y scale, whichever is smaller (but not equal to 1).

This may appear inconsistent when testing in the editor, because the property is added or removed only when saving and entering the level.

#### Fade, Friction & Respawn

**Fade In** and **Fade Out** add fades to the start and end of particles.

Min fade duration is 0, while max duration depends on the lifetime - **Fade In** is limited by the particle's lifetime, while **Fade Out** is limited to whatever time is left after **Fade In**. Both fades stack together with alpha.

There are 3 unique friction values that each affect one of the particle's transformations:
- **FrictionP** (velocity)
- **FrictionS** (scale)
- **FrictionR** (rotation)

All three friction settings can be approximated by an exponential decay function optimized for different frame rates: $Gradient = Gradient \cdot e^{-Friction \cdot FrameDelay}$. For **FrictionP** gradient is speed, for **FrictionS** gradient is $(EndScale-StartScale)/Lifetime$ and for **FrictionR** gradient is $(EndSpin - StartSpin) / Lifetime. 

**FrictionP** is only applied to gravity mode, **FrictionR** is only applied to spin and not **Dynamic Rotation**.

**Respawn** is how long it takes for a particle object to respawn an emitter with a finite **Duration** after the current one expires.

#### Misc Settings
