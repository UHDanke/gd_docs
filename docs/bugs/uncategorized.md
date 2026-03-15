# Uncategorized

## Float save precision

**Version:** 2.208  
**Date:** 02/01/2026  

### Description
Float properties are rounded to 6 significant digits when objects are copied or the level is saved. This causes lots of precision issues with many float properties that can have high values like object positions. It is NOT a float precision issue, this is caused by the save function using the format %g when casting floats to string.

## Mirror Mode does not do anything in level options.

**Version:** 2.208  
**Date:** 02/01/2026  

## Player 2 does not copy Player 1's gameplay rotation

**Version:** 2.208  
**Date:** 02/01/2026  

### Description
When entering a dual portal while the first player is travelling on vertically the 2nd player will travel horizontally instead

## Player 2 does not copy Player 1's gravity

**Version:** 2.208  
**Date:** 02/01/2026  

### Description
When entering a dual portal while the first player has non-default gravity the 2nd player will always have default gravity

## Negative object rotations get offset upon reloading

**Version:** 2.208  
**Date:** 02/01/2026  

### Description
If an object has negative rotation or skew x/y and has a decimal part it offsets until it reaches a whole number value. For example, -32.555 will round to -32.55, then -32.54 then -32.54 and so on until reaching -32.00.

## Collectibles cannot be recollected in classic mode after they are reset by Reset trigger

**Version:** 2.208  
**Date:** 02/01/2026  

### Description
Reset Trigger does not work for collectables in Classic mode. It will make them reappear, but without their collisions (non-recollectable).

## Animated shaders remain active permanently once the animation ends

**Version:** 2.208  
**Date:** 02/01/2026  

### Description
Some shaders like the shockwave are designed to play briefly and then end. While the main effect (the expanding wave) disappears as expected, a grainy or noise overlay remains active. This happens because the shader itself is still enabled even after the visible animation finishes, so the residual grain layer persists until the shader is explicitly turned off.

## Reverse Sync does not work as intended

**Version:** 2.208  
**Date:** 02/01/2026  

### Description
Reverse sync does not make the player go any faster or slower depending on how late/early you press an orb/pad which is set as reverse

## Music Line jumps when touching teleports with no target

**Version:** 2.208  
**Date:** 17/02/2026  

### Description
If the music line touches a teleport trigger or portal with target group ID 0, instead of ignoring the the teleport object the music line skips to the center of it.

### Workarounds
Use Center Effect on the problem object.
