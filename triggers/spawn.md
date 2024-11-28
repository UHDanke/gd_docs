# WORK IN PROGRESS
## Activation Order

The activation order of triggers is the order they were spawned in (the spawn order).  
By default, this is applied horizontally from left to right. If multiple triggers share the same horizontal position, they will activate in the order they were placed in.  
ORD can be used to enforce an activation order for triggers without the spawn trigger or touch trigger option which activate in the same tick.

The following triggers have additional ordering mechanisms which are applied before spawn order:

#### Count

First ordered by Target Count in ascending or descending order depending on whether the last item change increased or decreased the value.  
Count activates after every Pickup or Item Edit trigger with the Item option, even if the value remains the same. In this case ascending order is used.  
If Target Count is the same, spawn order will be used.

#### Time Event

Activation order depends on the spawn order of Timer triggers for different Item IDs.  
If Item IDs are identical, spawn order is used.

#### Collision

Activation order depends on the order collision objects are checked.  
Player collisions are checked before dynamic collisions.  
If two collision triggers share the same collision IDs, spawn order is used. The order of the IDs does not matter.

#### Area Triggers

Priority is applied first, from highest first to lowest last.  
If Priority is the same, spawn order is used.

#### Advanced Follow

Priority is applied first, from highest first to lowest last.  
If Priority is the same, spawn order is used.

### Spawn Schedule

The following spawns are instant:

* Spawn  
* Count  
* Instant Count  
* Instant Collision  
* Random  
* Advanced Random  
* Sequence  
* End

The remaining ones are scheduled, and will spawn in this order:

1. Spawn (delay)  
2. Toggle Block  
3. Event  
4. Touch  
5. Timer & Time Event  
6. Keyframe  
7. Collision (on enter)  
8. State (on enter)  
9. Touch Trigger  
10. State (on exit)  
11. On Death  
12. Instant (from timeline)   
13. Collision (on exit)

## Spawn Remapping

### Remap Rules

New spawn remaps overwrite inherited remaps.  
If an ID is remapped to multiple IDs within the same trigger (one-to-many), the highest (last in the list) new ID is used.

### Remappable Triggers

#### Fully Remappable

* Move  
* Stop  
* Alpha  
* Toggle  
* Rotate  
* Scale  
* Follow  
* Animate  
* Keyframe Animation  
* Keyframe  
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
* Edit Son  
* SFX  
* Edit SFX  
* Collision  
* Instant Collision  
* On Death  
*  End  
* Teleport  
* Shock Wave  
* Shock Line  
* Lens Circle  
* Radial Blur  
* Motion Blur  
* Bulge  
* Pinch  
* Gray Scale  
* Enter Triggers  
* Enter Stop

### Not Remappable

* Color  
* Rotate Gameplay  
* Gradient  
* Checkpoint  
* Enter Effect Triggers (not spawnable)

### Partially Remappable

#### Group Settings

Partially  
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

### Notes

#### Pulse

You can remap what groups or color channels are affected, but not the copied channel.  
Pulse's Color ID is the color channel affected by the trigger and Channel ID is the copied channel, the names of the options are swapped for the Color trigger.

#### Spawn

New Group ID can only be remapped from another Spawn trigger.

#### Edit Adv Follow

Edit Advanced Follow has no effect on type 1 Advanced Follow.  
**Target GID** is the group ID of the target object. However, with **Target Control ID** selected **Target GID** is the control ID of the Advanced Follow Trigger.

#### Re-Target AdvFollow

**Target GID** is the group ID of the Advanced Follow trigger being re-targeted, not the target object.

#### Sequence

Without Unique Remap, any activation of the same Sequence trigger advances the same (single) counter, regardless of remaps.  
With the option selected, every remap origin has its own Sequence counter, allowing for multiple concurrent instances of Sequence from the same trigger.  
Despite the name, if you call the same Sequence trigger with two spawn triggers with identical remaps, they will not share the same counter.

#### Gradient

In editor preview, remapping the ID has no effect. However, in playtesting, remapping the ID makes the gradient not spawn.

#### Enter Effect Triggers

It does not seem like you can spawn these triggers as of version 2.207.

## Remap Inheritance

Triggers that spawn groups also pass on their remaps to the spawned triggers. In other words, the spawn target inherits the spawn trigger's remaps.

The following triggers have some form of remap inheritance:

* Instant Count  
* Item Comp  
* Collision  
* Random  
* Adv Random  
* Sequence  
* Event  
* On Death  
* End  
* Touch  
* Keyframe
* Count
* Spawn
* Timer

### Notes & Exceptions

#### Count

Yes if Multi Activated is selected, otherwise the target inherits the remaps of the oldest subsequent multi activated Count with the same ItemID.

#### Spawn

Yes, unless Reset Remap is selected.

#### Timer

Spawning a Timer while there is already another active Timer with the same ItemID updates the Timer's settings and groups, but not the timer's remaps.  
The only way to clear these remaps is to use a Stop trigger on the current active Timer instance for that ItemID.  
In a way you can consider the remaps of Timers to be saved inside the Item ID until the Timer trigger is stopped with a Stop trigger.  
Pause, Resume and Time Control will not reset remaps.

#### Instant Collision

Resets remaps.

#### Time Event

Makes the Timer with the given Item ID spawn a group, so the spawn uses the Timer's remaps.

#### Checkpoint

Resets remaps.

## ID Limits

Spawn remapping allows you to remap any ID value, except identical IDs.   
Out of bounds IDs are limited only when a trigger is spawned. 

### Limited IDs

#### Group IDs

Trying to assign ID values outside 0-9999 is not possible.  
Any value below 1 refers to ID 0\.  
Any value above 9999 refers to ID 9999\.

#### Color Channels

Trying to assign ID values outside 0-999 is not possible.  
Values below 1 do nothing.  
Values above 999 are reserved for special color channels.

#### Item IDs

Values below 0 are reserved for special items (-1 is Time, \-2 is Points, \-3 is Attempts).  
Pickup can reference (but not change, they get limited to 0 or 9999\) IDs outside 0-9999.  
Item Edit cannot use ID 0\.

#### Song Channels

Trying to assign ID values outside 0-4  is not possible.  
Any value below 1 refers to ID 0\.  
Any value above 4 refers to ID 4\.

#### Collision IDs

Same as Group IDs.

#### Gradient IDs

* Trying to assign ID values outside 0-999 is not possible.  
* Builder helper can assign at most to ID 1000\.

### Extended Limit IDs

IDs with extended limits can be assigned beyond the usual 10000 ID limit.   
ID values outside 0-9999 cannot be assigned inside (most) triggers, but can be referenced via remapping.

The following IDs are:

* Control IDs  
* Area Effect IDs  
* Enter Effect IDs  
* Material IDs (between −/+ 32767\)  
* Enter Channels (between −/+ 32767\)  
* SFX IDs  
* SFX Groups

## Activation Limits

All triggers can be spawned multiple times per tick,  but not all can activate or create multiple instances per tick.

### Spawn Limit

Without remaps, a spawn trigger can spawn the same group once per reset.
There are two resets per tick, before and after Spawn triggers with delay are scheduled.
As a result, you can activate the same spawn group from a single Spawn trigger twice per tick - one time from a Spawn trigger with delay, and another time from any other spawn.  

With remaps, the spawn limit is applied separately for each remap origin.
The remap origin is the first remapped trigger in a spawn chain.    
Whether the spawned trigger has any of its IDs remapped does not matter, it can be any remap.

#### Remap Resets

Triggers that reset remaps can spawn the same group only once per tick.  
New remap origins can be assigned after a remap reset.

The remaps of a Spawn trigger with the Reset Remap option are reset before the Spawn trigger is spawned, so the Spawn trigger becomes the remap origin.  
If the Timer has no remaps, Time Event will spawn the group without remaps.   
Checkpoint and Instant Collision reset remaps.
