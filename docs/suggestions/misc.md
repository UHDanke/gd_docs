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