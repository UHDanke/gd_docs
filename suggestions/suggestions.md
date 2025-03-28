# Misc

## Song trigger Spawn GID on Song Load

Song trigger should be able to spawn a group ID when the song loads, either normally or with Prep.

## Reset trigger "Reset Trigger" option

With this option, the reset trigger would be able to reset triggers without the "Multi Trigger" option that have already been activated

## "Trigger limit persist between attempts" trigger object option

With this object option, triggers without multi-trigger would only be able to activate once between attempts, similar to Item Persist.  

## Reverse trigger inverts left/right controls of player

Since it is fairly useless, the reverse trigger (or the options trigger) should be able to invert left/right controls in platformer mode.  
This could be used to fix input issues in "circular" levels that use all 4 player direction modes.

## Options trigger "Disable 2 Player" option

Useful for having both symmetrical and assymetrical duals

## Sequence trigger "Randopmize Sequence" option

Groups of sequences are taken in random order with this option.  
Randomization is separate per remap.

## Mean / Gaussian Blur Shader

Would be much better than radial blur for out of focus objects in the foreground.

## Item Edit "Power" and "Root" operations

Add Power and Root as possible operations inside the Item Edit trigger.    

Integer powers can be done with repeated item edits, but roots are a bit less intuitive and require approximation (newton's method) to obtain, which makes euclidian distance calculations more difficult than they have to be.

## Scale "Set Scale" option

Sets the scale of Target GID using Center Group ID's current scale as reference.

For example, if the center's x scale is 10.00 and the trigger's x scale is 2.00, the trigger will scale the target group by 0.20 on the X axis.

## Sequence "Ignore Toggled" option

Sequence ignores toggled groups and skips to the next active group.

## Advanced Random "Ignore Toggled" option

Toggled groups have 0 weight with this option.  
This would be useful for adding unique drops or actions that are removed from the loot table.

## Time Control "Clear" option

Stop triggers are able to clear timers by Group ID. "Clear" on Time Control would be able to clear a timer by item id.

This isn't new functionality but it is less awkward than spawning a timer with the given item ID then stopping it, if the group of the timer is unknown or cannot be referred to.

Clearing is useful primarily for removing timers completely and clearing their remaps.

## Follow Trigger "Y Copy X" / "X Copy Y" options

These options would be useful for turning X movement into Y movement and vice-versa.  

The only way this can currently be achieved in some manner is with Area Move, but it is quite limited and inconvenient to do.

## Decimal Particle Emission

Allow Emission variable inside Particle Objects to have decimals, to allow finer control over the particle spawn rate.

## More Player Events

More events for the Event trigger:
- Grounded and Airborne player events
  - The current landing and jump events are not sufficient to tell whether the player is grounded or in the air accurately.
- Enter / Exit Practice Mode event
- Fall off platform (without jumping) event
- Clip into platform event
  - Would trigger when you jump into a hitbox and get pushed ontop of it.
- Directional Player Movement events
  - Player Move X Positive
  - Player Move X Negative
  - Player Move X Stop
  - Player Move Y Positive
  - Player Move Y Negative
  - Player Move Y Stop
- Game Unpaused event

## Build Helper / Regroup Copy Paste

Combined regroup + paste option to allow regrouping and pasting group ID parents.

## Teleport Trigger P2 option

Add P1/P2 options to the teleport trigger. The current workaround for this is to use teleport portals which also affect P1 and not just P2.

## Modifying player velocity X/Y only

An option in either the Player Control or Teleport trigger that would allow you to change the velocity of an object on the X or Y axis only.

## "Dynamic Reordering" Extra Object Option for triggers

With this option, if the trigger is moved by a move trigger and spawned, the game will use the trigger's current position instead of its load position.

## ItemID persist when exiting the level

Option for Item IDs to persist between attempts.  
Can be cleared from the level options menu.

## Spawn trigger "Random Order" option

Triggers spawned with this option will be sorted randomly.

# Area Triggers

## Edit Area use Control ID

The **EffectID** of Area triggers cannot be remapped, if you want to use the same Area trigger for different groups at the same time, you need to use **EffectID** 0\.  
However, since groups of objects cannot be remapped, you cannot use Edit Area on a particular remap, all instances of the same Area trigger will be affected.  
A solution for this would be to allow Edit Area to use Control IDs to refer to specific instances of the Area trigger.

## Edit Area Fade From Opacity

Currently, Edit Area Fade can only edit the To Opacity setting of Area Fade.

## Hide ModFront / ModBack for the first two Proximity settings

**ModFront** / **Modback** have no effect for the two circular area proximity options.   
Adding additional behavior would be nice, but it might break existing levels.   
These settings should be hidden while using those proximity options.

## Pause / Resume freeze / unfreeze Area triggers

Currently for Area triggers Pause has the same behavior as Stop and Resume has no effect.  
Pause / Resume should freeze / unfreeze recalculations of Area effects, similar to how they already work for Advanced Follow.

# Advanced Follow

## Advanced Follow Ignore Timewarp

Add **Ignore Timewarp** option to Advanced Follow. When used this would ensure high speed movement isn't affected while slowing down time.

## Edit AdvFollow Mod X and Mod Y reference ID

Add a reference ID besides Mod X and Mod Y, to allow the speed to be modified on the X or Y axis of a reference object. This would allow for accurate bounce physics off slopes or angled lines which is currently very difficult to do.

## Speed Multiplier

If speed not being a multiplier is intentional, a **Speed Multiplier** option should be added to allow for that behavior.  
While it takes an extra workaround, this would allow the implementation of accurate collision motions between solid physics objects.  
Additionally, any kind of movement could be converted to advanced follow speed values with this feature.

## Edit AdvFollow Use Dir
Add **Use Dir** option so the object's current direction is used for direction calculations.  
With Speed this would allow adding speed in the direction of movement without using an individual reference ID for each target.  
If Redirect Dir worked, you could use Dir to offset the direction of movement by a set amount of degrees.


