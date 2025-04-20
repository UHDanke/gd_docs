# Misc

## [2.207] Start Position 60hz

Start Positions simulate the game at only 60hz, while the tick rate in 2.2 is 240hz.  
While this seems intentional, an option to enable 240hz start positions would be nice to have.

## [2.207] Camera position is updated after move

The movement of an Advanced Follow with the C option will be delayed by one tick from the position of the camera, as the camera position is updated after all moves are processed.
This also affects Area triggers and Move (Lock Camera).

## [2.207] Object Rotations are highly innacurate for slow speeds.

The position of objects and their rotations get offset if rotations are slow (~30 degrees per second).  
All rotation transformations are affected except Area Rotate.

## [2.207] Rotate Aim / Follow infinite rotation

When using Dynamic Mode with Aim or Follow options, on a Target Group ID without a Group ID Parent and a Center Group ID that is either 0 or made up of multiple objects, the target objects will spin rapidly.  
If Center Group ID contains multiple objects (and no Group ID Parent), it will spin even faster.

[Video 1](https://youtu.be/uE5I8bRaMSg)  
[Video 2](https://youtu.be/GkujxqE5pok)

## [2.207] Relative Scale doesn't work with Scale 0.00

This isn't so much a bug as it is an oversight, Scale trigger will not work if scale is either 0 or 1.
Relative Scale lets you mimic additive scaling (increasing scale by an amount relative to current amount) if target and center have the same scale.
Due to the formula offseting scale by -1 ($RelativeScale=1+(Scale-1)/CenterScale$), increasing the scale by 1 needs a scale factor of 2.
In order to decrease the scale by -1, Scale would have to be 0 which doesn't work.

## [2.207] Gradient doesn't account for screen rotation when loading the level

Gradient triggers without any references (ID 0) use the screen's edges as reference instead.  
These edges are initialized when the level loads, however, if the camera trigger is placed before the origin camera rotation isn't taken into account.

Example:  
![image](https://github.com/user-attachments/assets/e2baf11d-2f0b-45e5-bbc9-e15dc3fd271e)

## [2.207] Color resumes when respawning from a checkpoint if stopped

If a Color trigger is stopped with a Stop trigger before the color change finishes, the color change will resume when you respawn from a checkpoint.  
Pausing the Color trigger does not do this.

## [2.207] Negative scaled Teleport triggers apply force in the opposite direction

Flipping a Teleport trigger by scaling it with a negative value does not change the direction force will be applied towards.

Flipping the trigger with the editor tool does change the force direction.

<br>

# Editor

## [2.207] Using editor Preview Mode hotkey at least twice while playtest is paused resets object position permanently

Pressing the F3 Preview Mode hotkey two times or more while editor playtesting is paused moves objects permanently.

The first use resets object positions to default, the second use reverts the position back to where it was in playtesting. The second move will not be undone when playtesting is stopped.

## [2.207] Regrouping objects with Group Parent IDs creates phantom groups

Groups are remapped by Regroup and Build Helper, but Group Parent IDs are not.  
The object remains the Group Parent ID for the old group despite said group no longer being in the group list.  
This can cause issues by introducing phantom groups \- the group is technically unused and not visible in the group list of the affected object, so it'll be available for Regroup and Build Helper, but the object is still the Group Parent ID for said group, so if a trigger relies on Group Parent IDs like Area or Advanced Follow, then said object will be used as the center, causing issues.

## [2.207] IDs that are not affected by Build Helper or Regroup

This is a list of all IDs that are not affected by Build Helper or Regroup. While i do not know which ones are on purpose, i'll highlight the ones that cause issues or look like oversights:
- _**Group Parent ID**_
- Enter Channel ID
- _**Control ID**_
- Material ID
- Enter Channel
- CH
- Target Channel (Start Position)
- Color ID (Color trigger, Pulse trigger)
- _**Rotate Target ID (Rotate)**_
- Animation ID (Animate)
- _**Animation Group ID (Animate Keyframe)**_
- _**Reference IDs (Advanced Follow, Edit Advanced Follow)**_
- _**Effect ID (Area triggers)**_
- _**Group ID (Sequence)**_
- Target Channel (Rotate Gameplay)
- Channel (Song)
- _**Unique ID, SFXGroup (SFX)**_
- _**Group ID, Unique ID, SFXGroup (SFX)**_
- Extra ID, Extra ID2 (Event)
- _**Item ID (Counter Label)**_
- Color Channel (Area Tint, Enter Tint Effect)
- Enter Channel (Legacy Enter Effect)
- Enter Channel, EffectID (Enter Effect triggers, Stop Enter Effect)
- _**RespawnID (Checkpoint)**_

## [2.207] Cannot create new Group Parent IDs if the trigger has 10 groups already

Group Parent IDs cannot be applied to an object with 10 existing groups, even if the object has that group already.

## [2.207] Hitbox does not update properly after rotating a slope object

Rotating a slope object does not update its orientation in the editor unless you move the object or quit the editor.  
Autobuild is affected by this.

## [2.207] Incorrect trigger duration line length when teleporting

The length of the duration line is double what it should be if the trigger is placed in a part of the level skipped by a teleport trigger.

![image](https://github.com/user-attachments/assets/ae1e5fec-1326-49fa-8ad3-cd50ca69c448)

## [2.207] On-load triggers have effect lines

On-load triggers like Link Visible and UI have effect lines when placed on the timeline, despite activating only when the level loads.
![image](https://github.com/user-attachments/assets/23007373-16ab-4cac-a4c7-66689abd4378)

## [2.207] Triggers that do not display their target ID

The following triggers, mostly added in 2.2, do not display any target IDs even though they should: 
- Re-Target Advanced Follow
- Area (Move, Scale, Rotate, Tint, Fade)
- Edit Area (Move, Scale, Rotate, Tint, Fade)
- Area Stop
- Item Compare
- Time
- Time Event
- Time Control
- Item Edit
- Item Persist
- Static Camera
- Event
- Toggle Block
- Enter Effect (Move, Scale, Rotate, Tint, Fade)
- Enter Stop
- Link Visible
- UI

The following triggers which spawn on either true or false only display one / no target ID, when they should display both true / false:
- Item Compare
- Instant Collision

## [2.207] **Disable Paste State Groups** prevents **Paste** from pasting groups

![image](https://github.com/user-attachments/assets/db5a88af-c6a6-4a71-992b-38364ee565a8)

**Disable Paste State Groups** affects both **Paste State** and the **Paste** button from the **Edit Groups** menu, despite being noted otherwise.

## [2.207] Lighter on Base Color or an object with only Base or Detail Color crashes the game

Using the Lighter option on the Base Color of an object or on an object with only Base or Detail Color will either crash the game when the object becomes visible or kick you out of the level on load.

This bug does not occur inside the editor.

## [2.207] Paste + Color does not remap Pulse's Channel ID

The Channel ID of a Pulse trigger cannot be remapped to a new value using Paste + Color.

<br>

# Move Trigger

## [2.207] Move Trigger Target Dynamic ignores X and Y Only

Move (Target Mode) options X and Y Only are ignored when using dynamic movement. 

## [2.207] Move Trigger Camera Lock X axis bugs on level replay

While the checkpoint / practice bug was fixed, restarting after completing a classic level places the camera locked group in the wrong position for that attempt.  
This only happens if the Move trigger is placed left or ontop of the level origin.

## [2.207] Pausing a Move trigger stops objects without a hitbox based on frames instead of ticks

Pausing a Move trigger stops the movement of objects, but objects without a hitbox are stopped on the next visual frame instead of the next tick.

This causes objects without a hitbox (spikes, solid blocks, collision objects) to offset from the position of objects with one (decoration, or using no touch).

Resuming undoes the offset.

Stopping does not create an offset, however stopping after pausing makes the offset permanent.

All other triggers with move functionality (rotate, scale, keyframe, etc) do not share this issue.

<br>

# Collisions

## [2.207] Move Silent Collision crash

If you spawn a Move trigger with the Silent option from inside a Collision trigger that moves two or more collision objects (at least one being dynamic) the game will sometimes crash.  

The dynamic collision object must be moved before it checks for collisions.

The crash will not trigger if Extended Collision is used on the dynamic collisions, it is likely the crash happens when the game tries to check the chunks of the collision objects that were moved.

Example ID:  
114561987

## [2.207] Spider teleports through or into Extended Collision objects.

Spider gamemode and Spider Orb teleports through or into an object with extended collision instead of on it.

Spider Pad is not affected by this issue.

<br>

# Events

## [2.207] Player Reversed event only works on pads and orbs

The Player Reversed event only works when activating a pad or orb with the Reverse option.

## [2.207] Feather Landing event does not trigger if the player does not land with downward velocity
If the player lands with close to 0 velocity or clips / teleports into an object while traveling upwards none of the landing events will trigger.

## [2.207] Left/Right Release events do not trigger if interrupted by the other direction on mobile

On mobile devices, if you press Left while already pressing Right (and vice-versa), releasing Right after this will not trigger a Right Release (or Left Release) event.  
This affects both player events.

## [2.207] Input Release events do not trigger if game is paused

If you pause the game while holding a player input and release it during the pause, the input release event will not trigger.

Input release should trigger on unpausing if the player no longer holds the input.

<br>

# Keyframes 

## [2.207] Keyframe movement is bugged if using a Parent ID in Animate Keyframe.

The parent's position is static when using a Parent ID inside the Animate Keyframe trigger, which results in bugged movement when scaling or rotating the keyframe.

## [2.207] Warp Skew of keyframes is ignored when animating the keyframe.

Only the X and Y scale of the keyframe is used for warping the target objects, skewing is ignored.

## [2.207] Keyframes merge when copying to another level

Keyframes have a hidden unique ID which is used to determine what keyframe objects are connected.  
The ID is kept even when copying to another level which results in the copied keyframes combining with existing ones.  
This makes merging parts of a level that use keyframes difficult, as you cannot manually select the unique ID of the keyframe.

## [2.207] Keyframe lines are not visible until reloading the level if pasted in a new level.

Keyframes copied to another level will not display the connecting lines until reloading the editor.

## [2.207] Animate Keyframe Position Y Mod cannot be 0 if Position X Mod is different than 0

If the value of Position Y Mod is equal to 0 when exiting the editor it will automatically copy the value of Position X Mod.
There are some cases where using only the X movement of a keyframe chain is required which is currently not possible to do outside of the editor.

## [2.207] Keyframe Preview does not match scaling
![image](https://github.com/user-attachments/assets/327217c9-e1fe-49f9-b0d2-ce96e51e3f39)

Keyframe scaling is relative to the Group Parent ID's rotation, which is not reflected in the preview where it is relative to the keyframe's rotation.

## [2.207] Rotation of Keyframe objects is not calculated properly

The formula by which keyframe rotation is calculated is very badly implemented and makes no sense.

The current rotation can be calculated using this formula:  
$Rotation = RotDiff \cdot Mod + 360 \cdot (RotFull + Offset)$

$RotDiff = Rotation2 - Rotation1$ 

This formula was determined with the help of [this spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vRI6_MKs2LkhxcaZf5eHm9yHjoKrrWYV_CYWWmqYX1WSStsrk2KzQ-aHuTIghjF926q-KHWq2UaC63k/pubhtml).

Where: 

*RotDiff* is the angle difference between the rotations of the first and second keyframe, going clockwise.  

*Mod* is the Rotation Mod multiplier from the Keyframe trigger.  

*RotFull* is the number of x360 rotations.   

*Offset* is an additional x360 rotation that can be determined using this table:  
| RotDiff | $RotDiff \cdot Mod$ | Direction | Offset |
| :---: | :---: | :---: | :---: |
| $>180$ | $>0$ | Any | \-1 |
| $>180$ | $<0$ | Any | 1 |
| $<=180$ | $>=360$ | None | \-1 |
| $<=180$ | $<=-360$ | None | 1 |
| $<=180$ | $>=360$ | CW | \-1 |
| $<=180$ | $<0$ | CW | 1 |
| $<=180$ | $>0$ | CCW | \-1 |
| $<=180$ | $<=-360$ | CCW | 1 |

The problems with this behavior are:
- If the angle between the two keyframes is over 180, then CW and CCW do nothing
- If the angle multiplied by Mod is more than a full rotation, CW and CCW do nothing
- If rotation Mod is negative then CCW becomes CW and vice-versa
- Mod multiplier doesn't work as expected with angles over 180, CW or CCW
- x360 rotations are not multiplied by Mod

Based on the above i propose this alternative formula to be used (possibly as a legacy option):

$Rotation = (Angle + 360 \cdot RotFull ) \cdot Mod$

Where Angle is:  
| RotDiff  | Direction | Angle |
| :---: | :---: | :---: |
| $<=180$ | None | RotDiff |
| $<=180$ |  CW  | Rotdiff |
| $<=180$ | CCW | 360-RotDiff |
| $>180$ | None | 360-RotDiff |
| $>180$ |  CW  | RotDiff |
| $>180$ | CCW | 360-RotDiff |

<br>

# Particles 

## [2.207] Toggling off or unloading a Particle Object does not clear particles in playtesting

In editor, toggling off or unloading a Particle Object disables and clears all particles created by it.
In playtesting, the particles are not cleared and become separate from the particle object - any changes to the main object no longer affect the disconnected particles which continue to linger until they despawn.

## [2.207] Deselecting **Animate on Trigger** deselects the option for all particle objects

Deselecting the **Animate on Trigger** option deselects the option for all particle objects when the level is saved.  

## [2.207] Particles with long lifespans linger after a level restart if **Quick Start** is selected

Particles are not properly cleared when the level restarts if using the **Quick Start** option.

## [2.207] Uniform Color particles spawned by Spawn Particle are not uniform

A particle with the Uniform Color option that is spawned will use the color channel value at the time of spawning instead of syncing with the color channel continuously.

## [2.207] Some Particle Objects can end up having erratic spin

Particle objects can get bugged and end up having very erratic movement.  
Level ID: 114681413

[Video](https://youtu.be/5zb-JCvD5JY)


## [2.207] Particle sometimes fail to spawn when near the particle limit

The first particle in a particle loop will fail to spawn if the particle limit has been hit already.

This usually happens if $Emission \cdot Lifetime = MaxParticles$

## [2.207] Spawn Particle Position Group ID is tied to game FPS

The spawn position of particles with Spawn Particle is the position of the group at the last rendered frame, instead of the current position.  
This can cause particles to spawn in the wrong position when dealing with high speed or instant movement when the game runs below 240 fps.  
The bug only happens while playtesting and not in the editor.

[Video: 200, 300, 60 and 120 fps](https://youtu.be/Co1UDLP2Ahk)  
[Video: 120 fps vsync, mobile](https://youtu.be/wxT__dKYsr8?si=X3O1ywGwrP5fIucm)

Setup attempts to spawn a particle every tick on a moving target.  
ID: 114953438

## [2.207] Spawn Particle fails to spawn on inactive targets

Spawn Particle will not spawn if the target is inactive (position is off-screen).  
This only happens while playtesting and not in the editor.  
If the object was active on screen at least once before, the particle will spawn at its previous on-screen position.

Link Visible can keep the target active as a potential workaround to this issue.  
While this might be intentional for performance reasons, there should be an option to allow the particle to spawn regardless of whether the target is active or not.

[Video](https://youtu.be/Co1UDLP2Ahk)

<br>

# Enter Effects

## [2.207] Enter trigger crash

If you try to call 2 different Enter triggers with the same Enter Channel and Effect IDs but different values for the same variables, the game will crash in playtesting.

## [2.207] Enter trigger portals

Using Enter trigger effects on portals and other objects composed of multiple objects only affects the foreground layer of portal objects.

## [2.207] Legacy Enter triggers cannot be spawned

Legacy (pre-2.2) Enter triggers cannot be spawned with the Spawn Trigger option.  
Touch Trigger does work however.

<br>

# Spawn Triggers

## [2.207] Overwriting a spawn remap of ID 2 crashes the game

If you spawn remap group ID 2 to any ID, then call another spawn which remaps group ID 2 to any other non-zero ID, then call a trigger which uses group ID 2, the game will instantly crash when calling the first spawn.  
Only ID 2 is affected.  
Only Steam and Android exhibit this bug. Mac and IOS are not affected.

## [2.207] Instant Collision resets remaps

Groups spawned by a remapped Instant Collision do not inherit remaps.

## [2.207] Checkpoint resets remaps

Groups spawned by a remapped Checkpoint do not inherit remaps.

## [2.207] Spamming restart (R key) skips spawn activation

Spamming R quickly can skip the activation of spawns placed before the origin line.
I assume the reason this happens is because the level restarts before the spawn limit is reset, so the triggers are spawn limited on the next restart.

## [2.207] Count spawn inheritance without Multi Activate

If Multi Activate is not selected, the Count's spawn target uses the remaps of the oldest active instance of a subsequent (activated after) Count trigger with the Multi Activate option using the same Item ID.
This makes one-time Count activations in remapped setups annoying to execute, since if you stop a Count trigger during a count update it will skip the next (or more, depending on how many were stopped) Count triggers.

## [2.207] Triggers that are not remappable or not fully remappable

The following triggers cannot be remapped, or have some IDs that are not remappable. I have highlighted the ones that cause some issues or make things more difficult in certain situations.

These triggers are not remappable:
- _**Color**_  
- Rotate Gameplay  
- _**Gradient (ID can get remapped but it always disables the gradient)**_
- **Checkpoint**  
- Legacy Enter Effect triggers (not spawnable)
- Keyframe (trigger is remappable, groups inside keyframe objects are not)

These triggers have IDs that are not remappable:
- _**Pulse (Color ID)**_
- Spawn (Original Group ID)
- _**Area Triggers (Effect ID)**_
- _**Area Tint, Enter Tint (Color Channel)**_

## [2.207] Stopping a spawn trigger with delay from another Spawn trigger with delay makes the last Spawn delay spawn again without remaps

Stopping any Spawn trigger with delay while spawn delays are checked makes the game check the last Spawn delay trigger twice, which if it were to spawn in the same tick would activate twice.

It doesn't matter if you stop a Spawn trigger that has already been activated in the current tick, one waiting to activate or you make the Spawn trigger stop itself.

Due to the spawn limit, this bug is only noticeable if the spawn trigger is remapped. The first activation will be remapped while the second spawn activation will have no remaps.

You can use a Spawn trigger with a very high delay value to counteract this bug, as even if it's checked twice it will not spawn.

## [2.207] Spawn triggers on the timeline have inconsistent spawn order and may be delayed or crash the game

The spawn order of different Spawn triggers placed on the timeline does not follow normal spawn order rules.

Some of the Spawn triggers can spawn only in a certain order, and will wait for certain other Spawn triggers to spawn, delaying them for an arbitrary amount of time.

A bug related to this can also crash the game, deleting the triggers and undoing the deletion fixes the crash in most cases.

Deleting and undoing the triggers does not change this order however.

**Example ID**: 115526701  
[Video](https://youtu.be/LbjoGxoutUg)

### Spawn Ordered

This bug also affects Spawn Ordered, but only when spawning triggers that were moved.

The spawn delay of triggers spawned by Spawn Ordered depends partly on their current position, which can be affected by move triggers.  

Not every move is affected, movements caused by Area triggers are completely ignored.

This behavior is inconsistent however, the game stops ignoring the new delays in some situations, and some spawns may be delayed until another spawns just like those placed on the timeline.

<br>

# Items and Timers

## [2.207] Count desync

The values stored inside Count triggers can be updated improperly or not at all when paused and resumed, when spawning pickups from inside other triggers and when using a persistent item due to Count storing the last value of the item when activating.  
More information can be found in the count desync file.

## [2.207] Pickup operations are innacurate

Multiplying large numbers using Pickup triggers has significant errors.
This isn't the case for Item Edit triggers however.

## [2.207] Item Compare may be inaccurate when checking if an ItemID equals a value

Item Compare can return false when comparing an integer Item ID to a value it is equal to (for example, 1).  
This may be caused by Pickups, but i was not able to accurately figure out a cause for this.

## [2.207] Time **Ignore Timewarp** does nothing

Timer is still slowed down or sped up by timewarp with the option selected.

## [2.207] Counter labels do not update properly with items outside the 0-9999 range

Counter labels only update if a Pickup or Item Edit trigger with the same ItemID is used.  
IDs outside the 0-9999 range refer to ID 0 or 9999. If an ID outside this range is used, it will display the value of ID 0 (if below 0) or 9999 (if above 9999), but will not update when ID 0 / 9999 change values.
Timers text labels update properly and are not affected by this bug.  

## [2.207] Level is unlisted if it contains a Pickup with high count or negative item id

The server unlists any level that contains a Pickup, Count or Instant Count trigger with either high count (100k or more) or an item ID less than 0.

This is an intentional fix to the 2.1 ACE exploit which has remained in place as 2.1 clients are still able to download levels. 

Item Edit and Time triggers are not affected by either issue.

## [2.207] Item Attempts value only returns 1

Attempts item is not updated on new attempts and always returns value 1 when used inside Item Edit or Item Compare.

<br>

# Area Triggers

## [2.207] Ease Out conflict

Ease Out is currently bugged and does not apply the effect properly to the radial proximity options.  
If the two easings differ they will both apply and conflict \- the game will pick and apply one of them. This is most obvious with opposing easings.

## [2.207] ModBack / ModFront do nothing for the radial options
ModBack / ModFront are still displayed when used on the radial options despite doing nothing.

## [2.207] Thin solid hitboxes when scale is negative

When a solid object is scaled by a negative value, hitboxes become very thin and buggy. Spikes and other non-solid hitboxes are not affected.

## [2.207] Area Fade stops working for a short duration after the game is unpaused
Unpausing the game undoes the effect of Area Fade for at least one frame (guess, not measured).

## [2.207] Start Position multiplies Area effect

Area effects are accumulated for every calculation when starting from a Start Position.  
Only the first tick is affected, the effect is properly applied on the second one.  
All Area triggers are affected.  
With Area Scale and Area Move, this can crash your game.

### Scale / Rotate Bug

Scaling or Rotating an object by a large amount makes it impossible to undo the transformation if done inside the editor.  
This makes all affected objects get their scale and rotation be completely different when stopping playtesting after the bug.

## [2.207] DEAP has no effect when used on Area Tint or Area Fade

The center group is affected by Area Tint and Area Fade even with **DEAP** selected, **DEAP** effectively does nothing for these two triggers.

## [2.207] Area Tint ignores Base / Detail Color

Area Tint ignores the Base / Detail Color setting of single-color objects.

## [2.207] Edit Area with Duration 0 does not override an active Edit Area

Edit Area will override other active Edit Areas only if **Duration** \> 0\.

## [2.207] Stop has no effect on Edit Area

Stop does not work on Edit Area.  
I am not sure if this is unimplemented or a side effect of how Edit Area was implemented.

## [2.207] Area Scale / Rotate / Move visibility issues

If an object stops being visible, Area Scale / Rotate / Move will stop applying in certain situation.

### Multiple Areas

Example [here](https://youtu.be/8IS5lFdIBus) and level ID in the video description.

### Flickering

Flickering is caused when a target goes off screen and ends up back on screen when the effect is undone every other tick. 
Example [here](https://www.youtube.com/watch?v=JgN_ClrC5yk).

### Rendering

Objects with a hitbox that stop being visible once brought off-screen do not render properly if brough back instantly on-screen.

## [2.207] Toggle and negative Length
Toggle disables Area effects on the object only in some cases for certain proximities and if Length is negative.  
This should be replaced by a dedicated **Ignore Disabled** feature as there is no logic or indication to this behavior.

## [2.207] Edit Area Tint / Fade doesn't pause in editor

Edit Area Tint and Edit Area Fade do not get paused when pausing the editor playtest.

[Video](https://youtu.be/DKtR5YL6qAI?si=Zd47Lgf6qV_ZNnxk)

## [2.207] Area Memory Leak, Stop and Area Stop do not properly clear Area triggers

Area triggers are not properly cleared by Stop or Area Stop triggers and accumulate lag vertime.  
The culprit seems to be the processAreaActions function but the details are not known.

The only way to properly clear an Area trigger is by replacing it with another Area trigger by using an EffectID.

Known affected levels are 3Depth and Dead of Night, both implement the EffectID workaround to fix the issue.

<br>

# Advanced Follow

## [2.207] Velocity Duplication
Targets move way faster than they should if there are multiple Advanced Follows active, because the velocity movement is mistakenly applied again by every trigger.

[Example Video](https://youtu.be/obZ-G22lizU)

Rotation is also duplicated when using Mode 3.

A solution to this bug would be for only the first Advanced Follow in a tick to move by the current velocity value, and subsequent ones to move by the difference in velocity.

## [2.207] Rotation and Object Groups

Advanced Follow movement breaks when using Rotation on targets part of linked objects or groups.

[Example Video](https://youtu.be/KJJ2YNqvOO8)

## [2.207] Timewarp and instant movement

### Instant Movement reduction
Mode 1 Advanced Follow triggers with no easing follow the target using easing if timewarp is less than 1.

The motion of Advanced Follow is inversely proportional with timewarp values less than 1. Due to how Mode 1 works, this multiplies the easing value of Mode 1 triggers, even if easing is equal to 0.

This behavior makes it impossible to perfectly match an object's movement with Advanced Follow while time is slown down.  
This also affects Mode 2 movement that relies on moving objects for a single tick very fast with high speed and limited MaxRange or 100 Friction.

### Max Rotation Speed

The max rotation speed of the Rotate option does not scale with timewarp.

## [2.207] Speedup when using high Friction values

Friction values over 100 can reverse the speed of an object, and if above 200 friction this speed will increase exponentially until the game crashes.

## [2.207] StartSpeed and Speed are not multipliers

StartSpeed and Speed are not multipliers when using a speed reference ID.  
It is not clear to me whether this is intentional or a bug, as the only place where the multiplier is mentioned is on the editor guide.  

## [2.207] Options that do nothing

The following options do nothing:
- MaxRange Reference ID
- Redirect Dir (Edit AdvFollow)
- SlowDist and SlowAccel (Mode 3)

While a MaxRange reference ID has limited applications, one such example is with Mode 1 with 0 easing - this would allow you to move a singular object from a group to a target position (like a target move for objects), which is very useful.

## [2.207] StartSpeed works on one target

If there are multiple targets inside Target GID, StartSpeed applies on one target only.

## [2.207] Physics issues when outside MaxRange

Even if an Advanced Follow target loses all velocity by leaving the MaxRange of the effect, if the player clips into the target's hitbox it will boost the player. This behavior continues until the trigger is stopped.  
Without DontBoostX/Y, the player's jump will be boosted everytime the player jumps off the target. 
Using DontBoostX/Y is not enough to fix this issue, the player will also be forcibly teleported to the top of the object if clipped inside or hit from below.

## [2.207] Hitbox move delay

Sometimes, the hitbox of the target object will be stuck in a previous position if Adv Follow movement is really fast.    
Stopping the Adv Follow trigger fixes the hitbox position.

## [2.207] Mode 3 X/Y Only cannot steer if other modes are present

When using X/Y Only on a Mode 3 trigger, the target is unable to steer if Mode 1 or 2 is present on the other axis.  

## [2.207] Edit Advanced Follow random is between 0/+ instead of -/+

The random variables in Edit Advanced Follow are always picked in a range between 0 and the given value, unlike other random settings.

## [2.207] Advanced Follow will not spawn if stopped then respawned in the same tick

If an Advanced Follow instance is stopped, then it is spawned again before the next Advanced Follow movement, it will not be active.

This bug is caused by two mechanics:
- Advanced Follow doesn't stop instantly, it is marked as stopped until the next scheduled movement where it gets cleared
- Advanced Follow will not spawn if an instance of it is already active for the given remap

A potential fix for this would be for Advanced Follow to replace the previous instance if its waiting to be stopped.

[Video](https://youtu.be/MNh11dOnu4U)  
ID: 115061026

