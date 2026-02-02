# Animate Trigger

Animates monsters and other objects with the **Animate on Trigger** setting (animations, particles).

## Behavior

Objects affected by Animate Trigger:
```
918, 920, 921, 923, 924, 1050, 1051, 1052, 1053, 1054, 1329, 1516, 1518, 1519, 1583, 1584, 1591, 1592, 1593, 1614, 1618, 1697, 1698, 1699, 1839, 1840, 1841, 1842, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1860, 1936, 1937, 1938, 1939, 2012, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2065, 2223, 2246, 2605, 2629, 2630, 2694, 2864, 2865, 2867, 2868, 2869, 2870, 2871, 2872, 2873, 2874, 2875, 2876, 2877, 2878, 2879, 2880, 2881, 2882, 2883, 2884, 2885, 2886, 2887, 2888, 2889, 2890, 2891, 2892, 2893, 2894, 3001, 3002, 3119, 3120, 3121, 3219, 3303, 3304, 3482, 3483, 3484, 3492, 3493, 4211, 4300
```

### Monsters

Makes the targeted monsters switch to the animation given by **Animation ID**. **Animation IDs** are used only by monsters and have no effect on any other object.

The transition between animations is done smoothly over a period of 0.05 seconds. If the animation is already active, then it'll reset to the beginning.

Invalid IDs play the default animation (ID 0).

Big (918):
- 0: bite
- 1: attack01
- 2: attack01_end
- 3: idle01

Bat (1584):
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

Spikeball (2012):
- 0: idle01
- 1: idle02
- 2: toAttack01
- 3: attack01
- 4: attack02
- 5: toAttack03
- 6: attack03
- 7: idle03
- 8: fromAttack03

### Particles

Animates particle objects with the **Animate on Trigger** property. Any remaining particles still connected to the target object are cleared when activated by Animate Trigger.

Animated particle objects start inactive until activated by Animate Trigger. If emitter duration is infinite, the particles will continue to spawn indefinitely as long as they are active. If duration is non-infinite, the particles will spawn once without looping.

Inactive particle objects are ignored if they have the **Only if Active** property.

### Animated Objects

Animates objects with the **Animate on Trigger** property. The animation plays once from the start and does not loop.

Animated objects start invisible if on-screen but will be visible if reloaded, they will turn invisible once the animation ends.

Inactive objects are ignored if they have the **Only if Active** property.

**Single Frame** and **Offset Anim** properties are ignored when animating.
