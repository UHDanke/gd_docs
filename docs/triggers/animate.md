## Animate Trigger

Animates monsters and other objects with the **Animate on Trigger** setting (animations, particles).

[2.207] All objects affected by Animate Trigger

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

### Behavior

#### Monsters

Makes the targeted monsters switch to the animation given by **Animation ID**. **Animation IDs** are used only by monsters and have no effect on any other object.

The transition between animations is done smoothly over a period of 0.05 seconds. If the animation is already active, then it'll reset to the beginning.

Invalid IDs play the default animation (ID 0).

Big (918)

- 0: bite
- 1: attack01
- 2: attack01_end
- 3: idle01

Bat (1584)

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

Spikeball (2012)

- 0: idle01
- 1: idle02
- 2: toAttack01
- 3: attack01
- 4: attack02
- 5: toAttack03
- 6: attack03
- 7: idle03
- 8: fromAttack03

#### Particles

Animates particle objects with the **Animate on Trigger** property. Any remaining particles still connected to the target object are cleared when activated by Animate Trigger.

Animated particle objects start inactive until activated by Animate Trigger. If emitter duration is infinite, the particles will continue to spawn indefinitely as long as they are active. If duration is non-infinite, the particles will spawn once without looping.

Inactive particle objects are ignored if they have the **Only if Active** property.

#### Animated Objects

Animates objects with the **Animate on Trigger** property. The animation plays once from the start and does not loop.

Animated objects start invisible if on-screen but will be visible if reloaded, they will turn invisible once the animation ends.

Inactive objects are ignored if they have the **Only if Active** property.

**Single Frame** and **Offset Anim** properties are ignored when animating.

## Edit Animation Settings

Allows editing the playback settings of animated objects, accessible from the Edit Special button.

### Options

**Randomize Start** is assigned by default on some animated objects, but currently does nothing.

**Use Speed** multiplies the animation's playback by the **Speed** option and removes the random start offset on selected objects if **Speed** is not 0. Negative **Speed** values can also be used.

**Animate on Trigger** makes the animation play from the start when activated by an Animate trigger, the animation plays once and does not loop. Animated objects start invisible if on-screen but will be visible if loaded later, they will turn invisible once the animation ends. Inactive objects (toggled off or offscreen) are ignored if **Only if Active** is selected.

**Disable Delayed Loop** removes the random delay some animations have between loops.

**Disable AnimShine** removes the white texture from a few animated objects. This property is removed by the game if used on objects this option has no effect on.

**Single Frame** makes the animation freeze on the selected frame. **Offset Anim** offsets the animation by the frame amount set in **Single Frame** instead. Objects animated by **Animate on Trigger** will not be offset.

### Notes

Monsters (918,1327,1328,1584,2012) and animated ground spikes (919) do not have an animation menu and cannot have these properties applied to them through save file editing.

Checkpoint objects (2063) have their elements move overtime, but this does not count as an animation and like monsters they are not affected by animation settings.

The coin collectible object (1614) can be edited, but the menu is overriden by the Edit Pickup Settings menu and it is only accessible if you also select an animated object.

Scale circles (1839,1840,1841,1842) do not have animation frames and instead scale and fade overtime. **Use Speed** is force selected by the game and frame options like **Single Frame** and **Offset Anim** have no effect.

Similarly, some gameplay elements (orbs) and decorations scale in sync with the music. They do not count as animated objects and thus are not affected by animation settings.

The lava bubble objects (1591,1593) ignore all animation settings except **Animate on Trigger** and **Only if Active**. Additionally, 1591 is randomized between 3 possible animations on level load.

The laser wall object (1697) has some of its frames randomized regardless of any settings used.

**Disable AnimShine** works on only 3 objects (2046,2047,2055).

### [2.207] Animated Objects

#### Properties

All objects affected by Edit Animation

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

Not random or delayed

- 1050, 1051, 1052, 1053, 1054, 1329, 1592, 1614
- 2605, 2694
- 3001, 3002
- 4211

Random start

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

Delayed loop

- 921
- 1519
- 1618
- 1851, 1852, 1854, 1855, 1856, 1860
- 2020, 2021, 2022, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2033, 2035, 2036, 2037, 2038, 2039, 2040, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055
- 2867, 2868, 2869, 2870, 2871, 2872, 2875, 2876, 2877, 2878, 2880, 2882, 2883, 2885, 2886, 2887

Pixelated

- 2223, 2246, 2605, 2629, 2630, 2694
- 3119, 3120, 3121, 3219, 3303, 3304, 3482, 3483, 3484, 3492, 3493
- 4211, 4300

#### Frame Delay

Objects animated using scale, rotate, move or fade effects animate smoothly every frame. Monster animation transitions are also done smoothly.

Most other animated objects are made up of multiple sequential frames with a set frame delay between each frame.

##### Monsters

Big (918)

- 0: 0.0250
- 1: 0.0250
- 2: 0.0250
- 3: 0.0500

Big Spiked (1327)

- 0: 0.0600

Small Spiked (1328)

- 0: 0.0600

Bat (1584)

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

Spikeball (2012)

- 0: 0.0600
- 1: 0.0600
- 2: 0.0450
- 3: 0.0600
- 4: 0.0600
- 5: 0.0400
- 6: 0.0400
- 7: 0.0600
- 8: 0.0500

##### Animated

Delay 0.0250

- 2892

Delay 0.0333

- 2893

Delay 0.0400

- 2047

Delay 0.0450

- 1053
- 1592

Delay 0.0500

- 1050, 1051, 1052,
- 1516, 1518
- 1618
- 1860
- 2020, 2021, 2022, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055
- 2869, 2870, 2871, 2872, 2873, 2874, 2875, 2876, 2880, 2881, 2882, 2883, 2884, 2885, 2886, 2890, 2891, 2894
- 3001, 3002

Delay 0.0600

- 1054
- 1519
- 1697, 1698, 1699
- 1855, 1857
- 2023
- 2864, 2865, 2867, 2868, 2877, 2878, 2879, 2887, 2888, 2889

Delay 0.0700

- 1849, 1851, 1852, 1854, 1856
- 1936, 1937, 1938, 1939

Delay 0.0800

- 920, 921, 923, 924,
- 1583
- 1853, 1858
- 2034
- 4300

Delay 0.1000

- 1850
- 2223, 2246
- 2605, 2629, 2630

Delay 0.1150

- 1329

Delay 0.1200
- 1591
- 1614
- 3303, 3304
- 3482, 3483, 3484, 3492, 3493
- 4211

Delay 0.1300

- 1591
- 1593

Delay 0.1600

- 2694
- 3119
- 3120
- 3121
- 3219

## Particle Object

Allows the creation of custom particle effects tied to objects.

### Particle Editor

Particle properties can be edited from the Particle Editor accessible from Edit Special.

The editor is split into 4 main tabs (Motion, Visual, Extra & Texture) with an interactible preview on the bottom left side of the menu.

The Texture tab selects the particle's texture.

#### Randomization

Most particle variables can be randomized in a range using a **+-** variable found next to the base one.

Randomized settings

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

#### Copy Paste

**C** and **P** can be used to copy & paste the particle settings between different particle objects. Copied settings are lost when exiting the editor.

#### Interactible Preview

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

#### Motion

Particle settings that affect motion and emission behavior. Two motion modes are available - **Gravity** and **Radius**.

##### Common

**Max Particles** is the max amount of particles that can be active at once, any further particles will fail to spawn.

**Duration** is the amount of time the emitter spawns particles. The emitter spawns particles until **Duration** runs out, and once the lifetime of all remaining particles expires then the emitter despawns and is replaced by another emitter by the particle object. **Duration** is infinite if set to -1 so the emitter will not stop spawning particles unless the particle object is unloaded. If value is 0 particles will not spawn unless **Emission** is -1.

**Lifetime** is the lifetime of the particle.

**Emission** is the amount of particles that can spawn per second. **Emission** also delays the first particle spawn by $1/Emission$ seconds, if the delay is bigger than **Duration** then no particles will spawn. If **Emission** is -1 then emission is infinite - the emitter will try to respawn all particles every frame without delay. **Max** sets **Emission** to -1, **Calc** calculates **Emission** using the formula $MaxParticle/(Lifetime+LifetimeRand)$.

**Angle** is the starting angle of the particle's motion. The value is given in degrees with 0 pointing right, positive values offset the angle clockwise and negative ones offset counter-clockwise.

##### Gravity

**Speed** is the particle's starting velocity, given in units (small steps) per second. All acceleration settings change the particle's velocity by $accel/100$ units per second.

**PosVar X** and **PosVar Y** give a range in units that randomize the particle's offset on the X and Y axis from the emitter's origin.

**Gravity X** and **Gravity Y** applies acceleration on the X and Y axes towards positive values, negative values accelerate away from positive and towards negative instead.

**AccelRad** applies acceleration away from the emitter's origin for positive values and towards the origin for negative ones.

**AccelTan** applies acceleration tangential to the particle's current direction, positive values accelerate clockwise while negative ones counter-clockwise.

**AccelRad** and **AccelTan** are not applied if velocity is null.

##### Radius

**StartRad** and **EndRad** are  the radial distances in units the particle starts from and ends at respectively. This movement is unaffected by **FrictionP**.

**RotSec** is the amount of degrees per second by which particles rotate around the emitter's center. Rotation is done in whole degree increments, so at low values the rotation is choppy.

#### Visual

Particle settings that affect scaling, rotation and color (RGBA) values.

##### Scale & Rotation

**StartSize** is the particle's initial scale, while **EndSize** is its final scale. Scale 16 is equivalent to the scale of the object variant of the particle.

**StartSpin** is the initial rotation of the particle texture, while **EndSpin** is its final rotation. This rotation offsets texture rotations done by **Start Rot is Dir** and **Dynamic Rotation**.

##### Colors

Start and End RGB values for the particles can be set in two ways:
- Using the two color pickers found on the top left of the menu
- Individual Start and End variables for each color channel, normalized to 1.00 (**Start_R**,  **Start_B**,  **Start_G**, **End_R**, **End_B**,  **End_G**)

The **<>** button next to the color selectors copies the main color to the secondary color. Changing the color from the color picker updates the RGB variables instantly, but changing the RGB variables updates the colors from the picker only when you reopen the particle editor.
Particle objects store RGBA as normalized values with 1% accuracy, rounding to the nearest value when converted to 8-bit RGBA.

Alpha cannot be set from the color picker, it can only be edited using the two **Start_A** and **End_A** variables.

#### Extra

Miscellaneous particle settings and extra options that do not fit in other tabs.

##### Free, Relative & Grouped
**Free**, **Relative** and **Grouped** change what point of reference the particles are relative to (camera, world, object)

- **Free** makes the particles copy the camera's movement and the opposite of the object's movement (particles appear relative to camera).
- **Relative** makes the particles copy the opposite of the object's movement. (particles appear relative to world).
- **Grouped** is default and applies no extra movement (particles appear relative to emitter).

How the particle object's scaling and rotation affects the spawned particles is different between **Free** / **Relative** and **Grouped**:
- With **Grouped**, the particle object can be scaled, warped and rotated as any other object.
- With **Free** & **Relative**, the game adds a special property to the particle object when you save the level which makes particles ignore the object's scale, warp and rotate; ignore rotations done by rotate triggers; if scaled by a trigger, scale the particles by either X or Y scale, whichever is smaller (but not equal to 1).

This may appear inconsistent when testing in the editor, because the property is added or removed only when saving and re-entering the level.

##### Fade, Friction & Respawn

**Fade In** and **Fade Out** add fades to the start and end of particles.

Min fade duration is 0, while max duration depends on the lifetime - **Fade In** is limited by the particle's lifetime, while **Fade Out** is limited to whatever time is left after **Fade In**. Both fades stack together with alpha.

There are 3 unique friction values that each affect one of the particle's transformations:
- **FrictionP** (velocity)
- **FrictionS** (scale)
- **FrictionR** (rotation)

All three friction settings can be approximated by an exponential decay function optimized for different frame rates:
$Gradient = Gradient \cdot exp(-Friction \cdot FrameDelay)$.

For **FrictionP** gradient is speed, for **FrictionS** gradient is $(EndScale-StartScale)/Lifetime$ and for **FrictionR** gradient is $(EndSpin - StartSpin) / Lifetime$. Frame delay is truncated to 4 decimals, since the friction required to match Advance Follow is ~2.44 to 1.00.

**FrictionP** is only applied to gravity mode, **FrictionR** is only applied to spin and not **Dynamic Rotation**.

**Respawn** is how long it takes for a particle object to respawn an emitter with a finite **Duration** after the current one expires.

##### Misc Settings

**Additive** makes particles blend. Also works for **Use Obj Color** and **Uniform Obj Color** in some cases, but changes how alpha is calculated in a non-intuitive way.

**Start Size = End** increases the particle's end size by its start size. This is particularly useful if **StartSize** is randomized and you want the particle to change or keep its end size relative to it.

**Start Spin = End** does the same thing for spin (rotation) and **Start Rad = End** does the same for radius.

**Start Rot is Dir** makes the particle's rotation match its start **Angle**.

**Use Obj Color** makes the particle use the particle object's colors instead of the emitter's RGB values. These colors are set at the creation of each particle and do not update if the parent object changes color. Base RGB variables are ignored, but RGB can still be randomized using the **+-** options.

**Uniform Obj Color** makes the particle copy the particle object's colors dynamically. All particle color options besides alpha are ignored.

**Dynamic Rotation** makes the particle rotate dynamically in the direction of movement.

**Animate On Trigger** allows activating the particle object with an Animate trigger. Animated particle objects start inactive until activated by Animate Trigger, any remaining particles still connected to the target object are also cleared.

If **Duration** is infinite, the particles will continue to spawn indefinitely as long as they are active, otherwise they will spawn once without looping.

Inactive particle objects are ignored if they have the **Only If Active** property.

**Order Sensitive** makes newer particles from the same emitter layer above older ones, without this option the layering / render order is randomized.

**StartRGB Var Sync** and **EndRGB Var Sync** replace Start and End RGB randomization with lightness randomization (brightness and saturation only are randomized) - the R channel **Start_R +-** and **End_R +-** options are used to randomize lightness, B and G random options are ignored.

**Quick Start** makes the particle skip simulating the first 2 seconds when starting if **Duration** is infinite. A particle with **Quick Start** still connected to its parent object will persist to the next attempt, even if resetting all checkpoints.

### Misc Behavior

Particles animate by frame, not by tick. Visuals are going to differ between devices with different framerates - particles with very high emissions will not look as smooth on lower framerates and have more clumps if not randomized.

Particles have a softcap of 100k particles active at once, if the softcap is hit any further particle objects that become active will not spawn particles until reloaded. The softcap can be passed by an emitter that goes over the limit. The total particle count is calculated based on the emitter's max particle property, not its current particle count, so avoid oversizing the value of max particle. The particle softcap is not used in the level editor.

Particle objects do not unload correctly in normal mode, but they do in the editor. Emitters tied to particle objects are not cleared if the object is unloaded, and continue being active until they despawn on their own. These emitters are disconnected from the object that created them, so any particle setting that depends on the parent object will stop updating. When the particle object becomes active again, it will create a new emitter separate from the previous one.

#### Alpha & Blending Behavior

Alpha values are calculated differently depending on the options selected, below you can find a table approximating these calculations.

| Additive | Obj Color | Uniform Color | Blending | Solid Alpha | Blending Alpha |
| :---: | :---: | :---: | :---: | :---: | :---: |
| No | No | No | Either | $(start \cdot (1-t)+end\*t) \cdot base$ | \- |
| No | No | Yes | No | $(start \cdot (1-t)+end \cdot t) \cdot base$ | \- |
| No | No | Yes | No | $(start \cdot (1-t)+end \cdot t) \cdot base$ | \- |
| No | Yes | No | No | $(base \cdot (1-t)+end \cdot t) \cdot base$ | \- |
| No | Yes | No | Yes | \- | $(base^2 \cdot (1-t)+end \cdot t) \cdot base^2$ |
| Either | No | Yes | Yes | \- | $(start \cdot (1-t)+end \cdot t) \cdot base^2$ |
| Yes | Yes | No | No | $(base \cdot (1-t)+end \cdot t) \cdot base$ | $((1-base) \cdot (1-t)+(1-end) \cdot t) \cdot base$ |
| Yes | Yes | No | Yes | \- | $(base \cdot (1-t)+end \cdot t) \cdot base^2$ |
| Yes | No | No | Either | \- | $(start \cdot (1-t)+end \cdot t) \cdot base^2$ |
| Yes | No | Yes | No | $(start \cdot (1-t)+end \cdot t) \cdot base$ | $((1-start) \cdot (1-t)+(1-end) \cdot t) \cdot base$ |

Notes:
- $start$ is the initial alpha, equal to: $Start\textunderscore A+Start\textunderscore A\textunderscore Rand$
- $end$ is the final alpha, equal to: $End\textunderscore A+End\textunderscore A\textunderscore Rand$
- $base$ is the alpha (opacity) of the base color channel.
  - The detail color channel's opacity is not used by particles.
  - **Use Obj Color** replaces $start$ with $base$ in all calculations.
  - $base$ is applied multiple times in some equations.
- For a particle to count as blending either the base or detail color must be blending.
  - If **Use Obj Color** or **Uniform Obj Color** are used with **Additive** but neither color channels blend, then the particle renders as both normal and additive.
- The resulting color for one particle is equal to: $BG\textunderscore RGB*(1-Solid\textunderscore Alpha)+Particle\textunderscore RGB*(Solid\textunderscore Alpha+Blending\textunderscore Alpha)$

## Spawn Particle

Spawns particles from particle objects in **Particle Group** at a target's position in **Position Group**.

Spawn Particle only works on particle objects, it cannot spawn the particles of other objects like pads or portals.

### Options

**Offset X** / **Y** offset the particle's spawn position by a set amount on the X / Y axis. **OffVar X** / **Y** further offset the spawn position randomly in a +/- range. All offsets are given in units (1/30 block).

**Rotation** offsets the rotation of spawned particles.

**Scale** multiplies the scale of spawned particle.

**Match Rot** adds the target object's rotation to the spawned particles.

**Rotation** and **Scale** can be randomized using the respective **+-** option.

### Group ID Parents

Group ID Parents change how **Particle Group** and **Position Group** work when they contain multiple objects.

If **Particle Group** has no GID Parent particles spawn individually at the target's position, using their own center for scale and rotation. If a GID Parent is present it becomes the center of the group - particles spawn relative to it, scale and rotation apply on the whole group.

For **Position Group** the GID Parent enforces an object as the target, without it the target is picked at random from all objects in the group.

Group Parents, Area Parents and object links have no effect on spawned particles.

### Differences from object particles

Infinite **Duration** is set to 0.00, if **Emission** is not infinite then no particles will spawn.

Spawned particle emitters do not respawn, therefore **Respawn** is ignored.

Particle emitters created by Spawn Particle are not tied to any object and cannot be repositioned after spawning, therefore **Relative** has the exact same behavior as **Grouped**. Additionally, **Free** and **Relative** emitters can be rotated or scaled which will also rotate and scale all movement, including **Free**'s camera movement.

Particle emitters created by Spawn Particle ignore most of the properties of the parent object except:
- rotation
- scale (X and Y, but not warp skew)
- position (if **Particle Group** has an ID Parent)
- Z order & layer
- if either **Use Obj Color** or **Uniform Obj Color** are used - the object's current base & detail colors (after all color changes, except Area Tint), but not alpha value (from color channel or triggers) or blending.

Particle colors do not update dynamically with **Uniform Obj Color**,
 the behavior for Spawn Particle is identical to **Use Obj Color**.

Alpha and blending behavior of emitters created by Spawn Particle is consistent between all combinations of **Additive**, **Use Obj Color** and **Uniform Obj Color**:
- base object opacity is ignored
- **Start_A** is not ignored when **Use Obj Color** is selected
- Particles will not fade between solid / blending

### Frame behavior

Spawn Particle uses the target's last active position, updated every frame (not tick) - this has two detrimental effects:
- If the target moves very fast (or instantly) and the game runs at a framerate lower than 240Hz, particles can spawn "earlier" than they should
- If the target becomes inactive by moving off screen, the particle will spawn on screen instead of at the target's current position

The second issue can be worked around by using a Link Visible trigger and keeping one object on screen at all times.