# Area Triggers

## Ease Out conflict

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Ease Out is currently bugged and does not apply the effect properly to the radial proximity options.  
If the two easings differ they will both apply and conflict \- the game will pick and apply one of them. This is most obvious with opposing easings.

## ModBack / ModFront do nothing for the radial options

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
ModBack / ModFront are still displayed when used on the radial options despite doing nothing.

## Thin solid hitboxes when scale is negative

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
When a solid object is scaled by a negative value, hitboxes become very thin and buggy. Spikes and other non-solid hitboxes are not affected.

## Area Fade stops working for a short duration after the game is unpaused

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Unpausing the game undoes the effect of Area Fade for one frame.

## Start Position multiplies Area effect

**Version:** 2.208  
**Date:** 30/01/2026  

### Description
Area effects are accumulated for every calculation when starting from a Start Position.  
Only the first tick is affected, the effect is properly applied on the second one.  
All Area triggers are affected.  
With Area Scale and Area Move, this can crash your game.  
  
 Scale / Rotate Bug  
  
Scaling or Rotating an object by a large amount makes it impossible to undo the transformation if done inside the editor.  
This makes all affected objects get their scale and rotation be completely different when stopping playtesting after the bug.

## DEAP has no effect when used on Area Tint or Area Fade

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
The center group is affected by Area Tint and Area Fade even with **DEAP** selected, **DEAP** effectively does nothing for these two triggers.

## Area Tint ignores Base / Detail Color

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Area Tint ignores the Base / Detail Color setting of single-color objects.

## Edit Area with Duration 0 does not override an active Edit Area

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Edit Area will override other active Edit Areas only if **Duration** \> 0\.

## Stop has no effect on Edit Area

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Stop does not work on Edit Area.  
I am not sure if this is unimplemented or a side effect of how Edit Area was implemented.

## Area Scale / Rotate / Move visibility issues

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
If an object stops being visible, Area Scale / Rotate / Move will stop applying in certain situation.  
  
 Multiple Areas  
  
Example [here](https://youtu.be/8IS5lFdIBus) and level ID in the video description.  
  
 Flickering  
  
Flickering is caused when a target goes off screen and ends up back on screen when the effect is undone every other tick.  
Example [here](https://www.youtube.com/watch?v=JgN_ClrC5yk).  
  
 Rendering  
  
Objects with a hitbox that stop being visible once brought off-screen do not render properly if brough back instantly on-screen.

## Toggle Inconsistencies

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Toggle disables Area effects on the object only in very particular cases depending on the area settings.  
This should be replaced by a dedicated **Ignore Disabled** feature as there is no logic or indication to this behavior.

## Edit Area Tint / Fade doesn't pause in editor

**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Edit Area Tint and Edit Area Fade do not get paused when pausing the editor playtest.  
  
[Video](https://youtu.be/DKtR5YL6qAI?si=Zd47Lgf6qV_ZNnxk)

## Scale sliders

**Version:** 2.208  
**Date:** 02/01/2026  

### Description
In the Edit Area Scale trigger, the Scale X and Scale Y sliders appear to be directly copied from the Edit Area Move trigger, resulting in absurdly high limits (100 for Scale X and 200 for Scale Y).
