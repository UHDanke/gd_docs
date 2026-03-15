# Particle Object

Allows the creation of custom particle effects tied to objects.

## Particle Editor

Particle properties can be edited from the Particle Editor accessible from Edit Special.

The editor is split into 4 main tabs (Motion, Visual, Extra & Texture) with an interactible preview on the bottom left side of the menu.

The Texture tab selects the particle's texture.

### Randomization

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

- **Free** makes the particles copy the camera's movement and the opposite of the object's movement (particles appear relative to camera).
- **Relative** makes the particles copy the opposite of the object's movement. (particles appear relative to world).
- **Grouped** is default and applies no extra movement (particles appear relative to emitter).

How the particle object's scaling and rotation affects the spawned particles is different between **Free** / **Relative** and **Grouped**:
- With **Grouped**, the particle object can be scaled and rotated like normal.
- With **Free** & **Relative**, the game adds a special property to the particle object when you save the level which makes particles ignore the object's scale, warp and rotate; ignore rotations done by rotate triggers; if scaled by a trigger, scale the particles by either X or Y scale, whichever is smaller (but not equal to 1).

This may appear inconsistent when testing in the editor, because the particle is updated only when re-entering the editor.

Particle objects can be warped and skewed and this will warp the emitter, but if the object was already warped before the emitter is created, then the emitter will not have the object's warping.

#### Fade, Friction & Respawn

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

#### Misc Settings

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

### Alpha & Blending Behavior

Alpha values are calculated differently depending on the options selected, below you can find a table approximating these calculations.
<!-- @csv: .data/tables/animate.csv -->
| **Object ID** | **Not Editable** | **Disable AnimShine** | **Smooth Animation** | **Randomize Start** | **Random Speed** | **Random Frames** | **Random Animations** | **Delayed Loop** | **Frame Delay** |
| :-----------: | :--------------: | :-------------------: | :------------------: | :-----------------: | :--------------: | :---------------: | :-------------------: | :--------------: | :-------------: |
|      918      |       Yes        |                       |                      |                     |                  |                   |                       |                  |   0.025 - 0.05  |
|      919      |       Yes        |                       |                      |                     |                  |                   |                       |                  |                 |
|      920      |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      921      |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.08      |
|      923      |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      924      |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      1050     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      1051     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      1052     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      1053     |                  |                       |                      |                     |                  |                   |                       |                  |      0.045      |
|      1054     |                  |                       |                      |                     |                  |                   |                       |                  |       0.06      |
|      1327     |       Yes        |                       |                      |                     |                  |                   |                       |                  |       0.06      |
|      1328     |       Yes        |                       |                      |                     |                  |                   |                       |                  |       0.06      |
|      1329     |                  |                       |                      |                     |                  |                   |                       |                  |      0.115      |
|      1516     |                  |                       |                      |         Yes         |                  |                   |                       |                  |       0.05      |
|      1518     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      1519     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      1583     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      1584     |       Yes        |                       |                      |                     |                  |                   |                       |                  |    0.06 - 0.1   |
|      1591     |                  |                       |                      |                     |                  |                   |          Yes          |                  |   0.12 - 0.13   |
|      1592     |                  |                       |                      |                     |                  |                   |                       |                  |      0.045      |
|      1593     |                  |                       |                      |                     |                  |                   |                       |                  |       0.13      |
|      1614     |                  |                       |                      |                     |                  |                   |                       |                  |       0.12      |
|      1618     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      1697     |                  |                       |                      |         Yes         |                  |        Yes        |                       |                  |       0.06      |
|      1698     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      1699     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      1839     |                  |                       |         Yes          |                     |                  |                   |                       |                  |                 |
|      1840     |                  |                       |         Yes          |                     |                  |                   |                       |                  |                 |
|      1841     |                  |                       |         Yes          |                     |                  |                   |                       |                  |                 |
|      1842     |                  |                       |         Yes          |                     |                  |                   |                       |                  |                 |
|      1849     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      1850     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      1851     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.07      |
|      1852     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.07      |
|      1853     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      1854     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.07      |
|      1855     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      1856     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.07      |
|      1857     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      1858     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      1860     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      1936     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      1937     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      1938     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      1939     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      2012     |       Yes        |                       |                      |                     |                  |                   |                       |                  |   0.04 - 0.06   |
|      2020     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2021     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2022     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2023     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2024     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2025     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2026     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2027     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2028     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2029     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2030     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2031     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2032     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2033     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2034     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      2035     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2036     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2037     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2038     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2039     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2040     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2041     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2042     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2043     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2044     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2045     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2046     |                  |          Yes          |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2047     |                  |          Yes          |                      |         Yes         |       Yes        |                   |                       |                  |       0.04      |
|      2048     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2049     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2050     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2051     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2052     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2053     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2054     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2055     |                  |          Yes          |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2223     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      2246     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      2605     |                  |                       |                      |                     |                  |                   |                       |                  |       0.1       |
|      2629     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      2630     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      2694     |                  |                       |                      |                     |                  |                   |                       |                  |       0.16      |
|      2864     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2865     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2867     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      2868     |                  |                       |                      |                     |       Yes        |                   |                       |                  |       0.06      |
|      2869     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2870     |                  |                       |                      |                     |       Yes        |                   |                       |                  |       0.05      |
|      2871     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2872     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2873     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2874     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2875     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2876     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2877     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      2878     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      2879     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2880     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2881     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2882     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2883     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2884     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2885     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2886     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2887     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      2888     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2889     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2890     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2891     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2892     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |      0.025      |
|      2893     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |      0.0333     |
|      2894     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      3001     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      3002     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      3119     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.16      |
|      3120     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.16      |
|      3121     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.16      |
|      3219     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.16      |
|      3303     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3304     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3482     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3483     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3484     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3492     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3493     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      4211     |                  |                       |                      |                     |                  |                   |                       |                  |       0.12      |
|      4300     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
<!-- @end -->
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
