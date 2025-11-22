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

Fully Remappable

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

Not Remappable

* Color
* Keyframes
* Rotate Gameplay
* Gradient
* Checkpoint
* Legacy Enter triggers (not spawnable)

Partially Remappable

Group Settings
- [x]	Control ID
- [ ]	Group ID, Parent ID, ORD, CH, Material ID

Pulse
- [x]	Channel ID, Group ID
- [ ]	Color ID

Spawn
- [x]	Group ID, New Group ID
- [ ]	Original Group ID

Area Triggers
- [x]	Target Group ID, Center Group ID
- [ ]	Effect ID, Color Channel (Area Tint)

Enter Tint Effect
- [x]	Enter Channel, Effect ID
- [ ]	Color Channel

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

Spawn triggers with remap inheritance

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

IDs with extended limit

* Control IDs
* Area Effect IDs
* Enter Effect IDs
* Item IDs (timers only)
* Material IDs (between −/+ 32767\)
* Enter Channels (between −/+ 32767\)
* SFX IDs
* SFX Groups