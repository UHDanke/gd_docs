# Misc

## \[2.207\] Regrouping objects with Group Parent IDs creates phantom groups

Groups are remapped by Regroup and Build Helper, but Group Parent IDs are not.  
The object remains the Group Parent ID for the old group despite said group no longer being in the group list.  
This can cause issues by introducing phantom groups \- the group is technically unused and not visible in the group list of the affected object, so it'll be available for Regroup and Build Helper, but the object is still the Group Parent ID for said group, so if a trigger relies on Group Parent IDs like Area or Advanced Follow, then said object will be used as the center, causing issues.

## \[2.206\] Cannot create new Group Parent IDs if the trigger has 10 groups already

Group Parent IDs cannot be applied to an object with 10 existing groups, even if the object has that group already.

## \[2.207\] Hitbox does not update properly after rotating a slope object

Rotating a slope object does not update its orientation in the editor unless you move the object or quit the editor.  
Autobuild is affected by this.

## \[2.207\] Feather Landing event does not trigger if the player does not land with downward velocity
If the player lands with close to 0 velocity or clips / teleports into an object while traveling upwards none of the landing events will trigger.

# Particles 

## \[2.207\] Toggling off a Particle Object does not clear particles in playtesting

In editor, toggling off a Particle Object disables and clears all particles created by the particle object.
In playtesting, the particles are not cleared and become separate from the particle object - any changes to the main object no longer affect the disconnected particles which continue to linger until they despawn.

## \[2.207\] Deselecting **Animate on Trigger** deselects the option for all particle objects

Deselecting the **Animate on Trigger** option deselects the option for all particle objects when the level is saved.  

## \[2.207\] Particles with long lifespans linger after a level restart if **Quick Start** is selected

Particles are not properly cleared when the level restarts if using the **Quick Start** option.

# Enter Effects

## \[2.207\] Enter trigger crash

If you try to call 2 different Enter triggers with the same Enter Channel and Effect IDs but different values for the same variables, the game will crash in playtesting.

## \[2.207\] Enter trigger portals

Using Enter trigger effects on portals only affects the foreground layer of portal objects.

# Spawn Triggers

## \[2.207\] Overwriting a spawn remap of ID 2 crashes the game

If you spawn remap group ID 2 to any ID, then call another spawn which remaps group ID 2 to any other non-zero ID, then call a trigger which uses group ID 2, the game will instantly crash when calling the first spawn.  
Only ID 2 is affected.  
Only Steam and Android exhibit this bug. Mac and IOS are not affected.

## \[2.207\] Instant Collision resets remaps

Groups spawned by a remapped Instant Collision do not inherit remaps.

## \[2.207\] Spamming restart (R key) skips spawn activation

Spamming R quickly can skip the activation of spawns placed before the origin line.
I assume the reason this happens is because the level restarts before the spawn limit is reset, so the triggers are spawn limited on the next restart.

## \[2.207\] Count spawn inheritance without Multi Activate

If Multi Activate is not selected, the Count's spawn target inherits the remaps of the oldest active instance of a subsequent Count trigger with the Multi Activate option using the same Item ID.

# Items and Timers

## \[2.207\] Count desync

The values of Count triggers can be updated improperly when paused and resumed or when spawning pickups from inside other triggers.  
More information can be found in the count desync file.

## \[2.207\] Pickup operations are innacurate

Multiplying large numbers using Pickup triggers has significant errors.

## \[2.207\] Time **Ignore Timewarp** does nothing

Timer is still slowed down or sped up by timewarp with the option selected.

## \[2.207\] Counter labels do not update properly with items outside the 0-9999 range

Counter labels only update if a Pickup or Item Edit trigger with the same ItemID is used.  
IDs outside the 0-9999 range refer to ID 0 or 9999. If an ID outside this range is used, it will display the value of ID 0 (if below 0) or 9999 (if above 9999), but will not update when ID 0 / 9999 change values.
Timers text labels update properly and are not affected by this bug.  

# Area Triggers

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
You can find an example of [here](https://www.youtube.com/watch?v=JgN_ClrC5yk).
As a result the object will flicker constantly, moving on and off-screen every other tick.  
This is not a visual bug, triggers that use object positions are affected.  
This bug does not occur for the top, bottom or left side of the screen.
