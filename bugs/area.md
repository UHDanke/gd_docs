# Area Bugs

## \[2.207\] Ease Out conflict

Ease Out is currently bugged and does not apply the effect properly to the radial proximity options.  
If the two easings differ they will both apply and conflict \- the game will pick and apply one of them. This is most obvious with opposing easings.

## \[2.207\] Thin solid hitboxes when scale is negative

When a solid object is scaled by a negative value, hitboxes become very thin and buggy. Spikes and other non-solid hitboxes are not affected.

## \[2.207\] Area Fade stops working for a short duration after the game is unpaused
Unpausing the game undoes the effect of Area Fade for at least one frame (guess, not measured).

## \[2.207\] Start Position multiplies Area effect

Area effects are accumulated for every calculation when starting from a Start Position.  
Only the first tick is affected, the effect is properly applied on the second one.  
All Area triggers are affected.  
With Area Scale and Area Move, this can crash your game.

## \[2.206\] Silent Move visual delay

When moving an object affected by Area Scale, Rotate or Move, the object will be rendered in the wrong position for one frame.  
The real position of the object is not affected, other triggers which use object position will not be affected.

## \[2.206\] DEAP has no effect when used on Area Tint or Area Fade
The center group is affected by Area Tint and Area Fade even with **DEAP** selected, **DEAP** effectively does nothing for these two triggers.

## \[2.206\] Area Tint ignores Base / Detail Color

Area Tint ignores the Base / Detail Color setting of single-color objects.

## \[2.206\] Edit Area with Duration 0 does not override an active Edit Area

Edit Area will override other active Edit Areas only if **Duration** \> 0\.

## \[2.206\] Stop has no effect on Edit Area

Stop does not work on Edit Area.  
I am not sure if this is unimplemented or a side effect of how Edit Area was implemented.

## \[2.206\] Area Scale / Rotate / Move visibility may break in certain situations

Area Scale / Rotate / Move effects are not applied in certain situations where the object would be visible after multiple Area effects.  
I was not able to figure out the exact reason why this happens, it seems there are multiple related bugs that cause this inconsistent behavior.  
Most of these issues can be fixed by using a Link Visible trigger on the group, but this isn't always desirable.

### Multiple Areas

You can see an example [here](https://youtu.be/8IS5lFdIBus). You can find the level ID in the video description.

### X Positive

This issue occurs when the Area Parent of an Area Scale, Rotate or Move effect is moved off screen towards the right (X positive) side.  
The Area effect will stop applying once off-screen, this will bring it back to its original position, on-screen, which makes the Area effect active again.  
As a result the object will flicker constantly, moving on and off-screen every other tick.  
This is not a visual bug, triggers that use object positions are affected.  
This bug does not occur for the top, bottom or left side of the screen.