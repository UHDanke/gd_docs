# Misc

### Sequence "Ignore Toggled" option.

Allows Sequence to skip toggled groups.

### Advanced Random "Ignore Toggled" option.

Toggled groups have 0 weight with this option.

### Time Control "Clear" options

Stop triggers are able to clear timers by Group ID. "Clear" on Time Control would be able to clear a timer by item id.

This isn't new functionality but it is less awkward than spawning a timer with the given item ID then stopping it.

### Grounded and Airborne player events

Grounded and Airborne player events for platformers.

### Build Helper / Regroup Copy Paste

Combined regroup + paste option to allow regrouping and pasting group ID parents.

# Area Triggers

### Edit Area use Control ID

The **EffectID** of Area triggers cannot be remapped, if you want to use the same Area trigger for different groups at the same time, you need to use **EffectID** 0\.  
However, since groups of objects cannot be remapped, you cannot use Edit Area on a particular remap, all instances of the same Area trigger will be affected.  
A solution for this would be to allow Edit Area to use Control IDs to refer to specific instances of the Area trigger.

### Edit Area Fade From Opacity

Currently, Edit Area Fade can only edit the To Opacity setting of Area Fade.

### Hide ModFront / ModBack for the first two Proximity settings

**ModFront** / **Modback** have no effect for the two circular area proximity options.   
Adding additional behavior would be nice, but it might break existing levels.   
These settings should be hidden while using those proximity options.

### Pause / Resume freeze / unfreeze Area triggers

Currently for Area triggers Pause has the same behavior as Stop and Resume has no effect.  
Pause / Resume should freeze / unfreeze recalculations of Area effects, similar to how they already work for Advanced Follow.

# Sequence