# Spawn Trigger

Activates a set of spawn-triggered triggers with the given **Group ID** instantly or after a **Delay**.

## Spawn Delays

The activation of Spawn triggers can be delayed by a value defined in seconds, up to 0.1 miliseconds in accuracy.

As the game processed delays in ticks and not in miliseconds, the delay is rounded up to the nearest tick.  
In order to keep delays and loops consistent overtime, this additional delay is passed on further to other Spawn triggers.

The delay's value can be either positive or negative, and can also be offset randomly using the -/+ option.

### Timings

Delay is only applied if it is strictly bigger than 0, otherwise the Spawn trigger is instant.

Spawn delays are processed at the beginning of the tick, in the order they were spawned in.

If a Spawn delay (with positive value, not instant) is spawned by another Spawn delay, it will only be checked starting next tick. 

### Delay Inheritance

If a Spawn trigger with delay is spawned by another Spawn trigger with delay, the new spawn will subtract the previous one's additional delay. This keeps chained delays and spawn loops accurate.

Negative delay values are also inherited and reduce the delay of further Spawn triggers by the same amount.  
Leftovers from randomized delays (-/+ option) are not inherited. 

Extra delays are not inherited by any other trigger except Spawn, so this leftover can be cleared if a trigger like Random or Item Compare spawns the next delay.

### Extra Spawn Limit 

Triggers spawned when delays are processed will be able to spawn the same group once again in the same tick when activated again after the Spawn delay interval.

## Spawn Ordered

Spawn Ordered spawns triggers over time similar to ones placed on the timeline. Each spawned trigger has a delay depending on its position, relative to the base (1x) player speed. 

This delay is calculated based on the object's X coordinate from the leftmost trigger in the group. The leftmost triggers are spawned instantly.

While triggers can be moved in order to change their delays, something not possible outside Spawn Ordered, this behavior is buggy and unreliable.

<br>

# Spawn Remapping

Spawn triggers allow spawning triggers with new groups with Spawn Remapping.

Remapped triggers spawn triggers with groups remapped to other groups.    

Remapping does not change the IDs of triggers, it creates independent copies of triggers (called instances) with new IDs.

IDs are not discerned by their type (Item ID, Block ID, Group ID, etc), they are all treated the same for the purposes of remapping.   

The main purpose of spawn remapping is reusing triggers, but it has many more uses thanks to its versatility.

## Remap Rules

An ID can be remapped to a single other ID at a time. If an ID is remapped to multiple IDs within the same trigger, the highest (last in the list) New ID is used.

If a Spawn trigger with remaps is activated by another remapped trigger, it adds its remaps to it. The new remaps overwrite previous ones if Original IDs are duplicated.

## Remappable Triggers

### Fully Remappable

* Move  
* Stop  
* Alpha  
* Toggle  
* Rotate  
* Scale  
* Follow  
* Animate  
* Animate Keyframe  
* Follow Player Y  
* Advanced Follow  
* Edit Advanced Follow  
* Retarget Advanced Follow  
* Edit Area  
* Area Stop  
* Touch  
* Count  
* Instant Count  
* Pickup  
* Time  
* Time Event  
* Time Control  
* Item Edit  
* Item Compare  
* Item Persist  
* Random  
* Advanced Random  
* Sequence  
* Spawn Particle  
* Reset Pickups  
* Static Camera  
* Camera Edge  
* Song  
* Edit Song  
* SFX  
* Edit SFX  
* Collision  
* Instant Collision  
* On Death  
* End  
* Teleport  
* Shock Wave  
* Shock Line  
* Lens Circle  
* Radial Blur  
* Motion Blur  
* Bulge  
* Pinch  
* Gray Scale  
* Enter Triggers (except Enter Tint)
* Enter Stop

### Not Remappable

* Color  
* Keyframes
* Rotate Gameplay  
* Gradient  
* Checkpoint  
* Legacy Enter triggers (not spawnable)

### Partially Remappable

#### Group Settings

**Yes**	Control ID  
**No**	Group ID, Parent ID, ORD, CH, Material ID

#### Pulse

**Yes**	Channel ID, Group ID  
**No**	Color ID

#### Spawn

**Yes**	Group ID, New Group ID  
**No**	Original Group ID

#### Area Triggers

**Yes**	Target Group ID, Center Group ID  
**No**	Effect ID, Color Channel (Area Tint)

#### Enter Tint Effect
**Yes**	Enter Channel, Effect ID
**No**	Color Channel

### Notes

#### Pulse

You can remap what groups or color channels are affected, but not the copied channel.  
Pulse's Color ID is the color channel affected by the trigger and Channel ID is the copied channel, the names of the options are swapped for the Color trigger.

#### Spawn

Spawn ID and New Group ID can only be remapped from another Spawn trigger.   
New Group IDs will not be remapped by other spawn triggers if using Reset Remap.

#### Edit Adv Follow

Edit Advanced Follow has no effect on type 1 Advanced Follow.  
**Target GID** is the group ID of the target object. However, with **Target Control ID** selected **Target GID** is the control ID of the Advanced Follow Trigger.

#### Re-Target AdvFollow

**Target GID** is the group ID of the Advanced Follow trigger being re-targeted, not the target object.

#### Sequence

Without **Unique Remap**, any activation of the same Sequence trigger advances the same (single) counter, regardless of remaps.  
With the option selected, every remap origin has its own Sequence counter, allowing for multiple concurrent instances of Sequence from the same trigger.  
Despite the name, if you call the same Sequence trigger with two spawn triggers with identical remaps, they will not share the same counter.

#### Song

**Custom Song ID** can also be remapped, and any downloaded song can be played.

Songs played via remapping will not show in the download list however. 

Without mods or scripts you are not able to type an ID higher than 999999, which makes choosing an Audio Library song difficult.

#### SFX

**Custom SFX ID** can also be remapped, and any downloaded SFX can be played.

SFX played via remapping will not show in the download list however. 

#### Gradient

In editor preview, remapping the ID has no effect. However, in playtesting, remapping the ID makes the gradient not spawn.

#### Legacy Enter Triggers

It does not seem like you can spawn these triggers as of version 2.207.

## Remap Inheritance

Triggers that spawn groups also pass on their remaps to the activated triggers. In other words, the spawn target inherits the spawn trigger's remaps.

The following triggers have some form of remap inheritance:

* Instant Count  
* Item Compare  
* Collision  
* Random  
* Advanced Random  
* Sequence  
* Event  
* On Death  
* End  
* Touch  
* Keyframe
* Count
* Spawn
* Time

### Notes & Exceptions

#### Count

Yes if Multi Activated is selected, otherwise the target inherits the remaps of the oldest subsequent multi activated Count with the same ItemID.

#### Spawn

Yes, unless Reset Remap is selected.

#### Timers

Remaps of Time triggers are stored inside timers. 

Remaps can only be assigned when the timer is initialized, Time triggers update the timer's settings and groups, but not the timer's remaps.  

The only way to clear these remaps is to use a Stop trigger on one the groups or control IDs of the last Time trigger called for that ItemID.  
 
Pause, Resume and Time Control will not reset remaps.  

Assigning a value to a timer Item ID with Item Edit creates a paused timer instance with no remaps.

#### Instant Collision

Resets remaps.

#### Time Event

Makes the timer with the given Item ID spawn a group, so the spawn uses the timer's remaps.

#### Checkpoint

Cannot be remapped, resets remaps.

## ID Limits

Spawn remapping allows you to remap any ID value, except identical IDs.   
Out of bounds IDs are limited only when a trigger is spawned. 

### Limited IDs

#### Group IDs

Trying to assign ID values outside 0-9999 is not possible.  
Any value below 1 refers to ID 0.  
Any value above 9999 refers to ID 9999.

#### Color Channels

Trying to assign ID values outside 0-999 is not possible.  
Values below 1 do nothing.  
Values between 1000-1101 are reserved for special color channels.    
Any value above 1101 refers to ID 1101.

#### Item IDs

Values below 0 are reserved for special items (-1 is Time, -2 is Points, -3 is Attempts).  
Pickup, Item Edit and Item Compare can reference (but not change, they get limited to 0 or 9999) IDs outside 0-9999.  
Item Edit cannot use ID 0 as a parameter.  
Time, Time Event and Time Control can reference and use IDs outside 0-9999. As Item Compare and Item Edit cannot reference out of bounds IDs, accessing the values of these timers is not possible. It is however possible to store remaps inside timers and spawn a group with those remaps using Time Event.  

#### Song Channels

Trying to assign ID values outside 0-4  is not possible.  
Any value below 1 refers to ID 0\.  
Any value above 4 refers to ID 4\.

#### Collision IDs

Same as Group IDs.

#### Gradient IDs

* Trying to assign ID values outside 0-999 is not possible without mods or scripts.  
* Builder helper can assign at most to ID 1000\.

### Extended Limit IDs

IDs with extended limits can be assigned beyond the usual 10000 ID limit.   
ID values outside 0-9999 cannot be assigned inside (most) triggers, but can be referenced via remapping.

The following IDs are:

* Control IDs  
* Area Effect IDs  
* Enter Effect IDs
* Item IDs (timers only)
* Material IDs (between −/+ 32767\)  
* Enter Channels (between −/+ 32767\)  
* SFX IDs  
* SFX Groups

<br>

# Spawn Order

The activation order of triggers is the order they were spawned in, also known as the spawn order.  
By default, this is applied horizontally from left to right. If multiple triggers share the same horizontal position, they will activate in the order they were placed in.  

ORD can be used to enforce an activation order for triggers without the spawn or touch trigger option which activate in the same tick.

The following triggers have additional ordering mechanisms which are applied before spawn order:

### Count

First ordered by Target Count in ascending or descending order depending on whether the last item change increased or decreased the value.  
Count activates after every Pickup or Item Edit trigger with the Item option, even if the value remains the same. In this case ascending order is used.  
If Target Count is the same, spawn order will be used.

### Time

Activation order is different between platforms - on Steam they have normal spawn order, on Android their spawn order is reversed.

### Time Event

Activation order depends on the spawn order of Timer triggers for different Item IDs.  
If Item IDs are identical, spawn order is used.

### Collision

Activation order depends on the order collision objects are checked.  
Player collisions are checked before dynamic collisions.  
If two collision triggers share the same collision IDs, spawn order is used. The order of the IDs does not matter.

### Area Triggers

Priority is applied first, from highest first to lowest last.  
If Priority is the same, spawn order is used.

### Advanced Follow

Priority is applied first, from highest first to lowest last.  
If Priority is the same, spawn order is used.

## Spawn Schedule

The following spawns are instant:

* Spawn  
* Count  
* Instant Count  
* Instant Collision
* Item Compare
* Random  
* Advanced Random  
* Sequence  
* End

The remaining ones are scheduled, and will spawn in this order:

1. Spawn (delay)  
2. Toggle Orb/Block  
3. Event  
4. Touch  
5. Timer & Time Event  
6. Keyframe  
7. Collision (on enter)  
8. State (on enter)  
9. Instant (touch triggered)  
10. State (on exit)  
11. On Death  
12. Instant (from timeline)   
13. Collision (on exit)

<br>

# Activation Limits

All triggers can be spawned multiple times per tick, but not all can activate or create multiple instances per tick.

### Spawn Limit

Without remaps, a spawn trigger can spawn the same group once per reset.  
There are two resets per tick, before and after Spawn triggers with delay are scheduled.  
As a result, you can activate the same spawn group from a single Spawn trigger twice per tick - one time from a Spawn trigger with delay, and another time from any other spawn.    
While the applications of this are limited, having the option of a second activation per tick is very important for instanced spawn triggers like Count and Sequence, where otherwise each instance would only be able to activate once per tick which can interfere if the spawn is either on a timer or by player input. 

With remaps, the spawn limit is applied separately for each remap origin.  
The remap origin is the first remapped trigger in a spawn chain.    
Whether the spawned trigger has any of its IDs remapped does not matter, it can be any remap.

#### Remap Resets

Triggers that reset remaps can spawn the same group only once per tick.  
New remap origins can be assigned after a remap reset.

The remaps of a Spawn trigger with the Reset Remap option are reset before the Spawn trigger is spawned, so the Spawn trigger becomes the remap origin.  
If the Timer has no remaps, Time Event will spawn the group without remaps.   
Checkpoint and Instant Collision reset remaps.

<br>

# Other Spawn Triggers

<br>

# Stop

Stops, pauses or resumes a set of triggers given by Group or Control ID.

## Valid Targets

Most triggers that have a temporary or permanent effect can be stopped, the following triggers are affected:
- Color
- Move (if not silent)
- Pulse
- Alpha
- Spawn (if delayed)
- Rotate
- Scale
- Follow
- Keyframe Animation
- Follow Player Y
- Advanced Follow
- Area Triggers
- Touch
- Count
- Time
- Time Event
- Zoom Camera
- Offset Camera
- Rotate Camera
- SFX
- Event
- Collision
- On Death
- Gradient

### Exceptions

The following triggers have an active effect which cannot be stopped with the Stop trigger:
- Shake
- Edit Area Triggers
- Spawn Particle
- Static Camera
- Gameplay Offset
- Camera Edge
- Song
- Edit Song
- Edit SFX
- UI
- Link Visible
- Shader Triggers
- Enter Triggers

### Alternative Stops

Some of the active triggers, including ones not affected by Stop, have alternative stopping or pausing mechanisms.

#### Edit Area

Edit Area effects are done by the Area trigger, pausing or stopping the Edit Area requires respawning, stopping or pausing the target Area trigger.

#### Time

Can start paused, or be paused using a Time Control trigger.

This pause is different from the one done by Pause - it will not resume a Pause trigger and it cannot be resumed by Stop.

#### Static Camera

The follow cannot be stopped, but the target can be returned back to default by using the **Exit Static** option.

#### Camera Edge

Locked edges can be reset using ID 0 and with the **Unlock** button.

#### Song

Can be stopped by Channel ID with an Edit Song trigger.

#### SFX

Can be stopped by Unique, SFX Group or Group ID with an Edit SFX trigger.

#### Gradient

Can be stopped by using the **Disable** option. 

All active gradients can be cleared with the **Disable All** option. 

#### Shader Triggers

All shaders effects can be disabled using the Shader trigger's **Disable All** option. 

Chroma Glitch shader can be disabled using the trigger's **Disable** option.

#### Enter Triggers

Enter effects can be cleared using their Enter Channel or Effect ID from the Enter Stop trigger.

#### Item Persist

While not an active trigger, the item or timer's persistent flag can be reset using the **Reset** option, which also clears the value or **Reset All**, which affects all persistent items and timers.

## Stop Effect

The effect of a Stop, Pause or Resume trigger on other triggers varies, but can be split into three main categories:
- Effect is paused or stops applying:
 - Color
 - Move
 - Alpha
 - Rotate
 - Scale
 - Follow
 - Keyframe Animation
 - Follow Player Y
 - Advanced Follow
 - Zoom Camera
 - Offset Camera
 - Rotate Camera
- Effect gets cleared or is undone:
 - Pulse
 - Area Triggers
 - Time (settings reset)
 - SFX
 - Gradient
- Activation is prevented:
 - Spawn
 - Touch
 - Count
 - Time
 - Time Event
 - Event
 - Collision
 - On Death

### Notes

#### Color

The last stopped Color trigger on the channel before a checkpoint gets resumed when respawning.

#### Keyframe Animation

Spawning in the same tick cannot be prevented with Stop.

#### Spawn

Stopping a Spawn trigger with delay from inside another Spawn trigger with delay causes the last scheduled Spawn delay to be checked twice in the same tick. If this delay activates, the first activation uses the Spawn's remaps, while the second uses no remaps.

If a Spawn Ordered trigger is stopped, it will stop spawning triggers. If its the last one, it will continue spawning without remaps from the stop point.

Paused Spawn delays are ignored and will not tick down until resuming.	

Delays can be resumed (or paused) and activate (or not activate) in the same tick as long as they haven't been checked yet.

