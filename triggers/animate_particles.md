
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
<summary>Big Monster (918)</summary>

- 0: bite
- 1: attack01
- 2: attack01_end
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
<summary>Not Random or Delayed</summary>
  
- 1050, 1051, 1052, 1053, 1054, 1329, 1592, 1614
- 2605, 2694
- 3001, 3002
- 4211
</details>

<details>
<summary>Random Start</summary>
  
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
<summary>Delayed Loop</summary>

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

# Spawn Particle

# Particle Object
