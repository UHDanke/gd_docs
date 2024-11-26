TODO
# Collision

## Collision Schedule
* Collision (enter)
* State (enter)
* Touch Trigger
* State (exit)
* On Death
* Collision (exit)
  
## Interactions with Silent Move and Toggle
If collisions have yet to be checked, it is possible to prevent a collision from inside a collision spawn by using an instant trigger like Toggle or Move (with the Silent option).  
This is only possible for enter collisions, collisions are not checked again during exit collisions - the collision exit state is updated if there are no active collisions after all collision objects are checked.  

## Collision Objects
Used by Collision and Instant Collision triggers to implement collisions.	
Can be rotated, scaled or warped.	
**Block IDs** are limited between 0 and 9999.	
The **Dynamic** option allows collision objects to check collisions with other collision objects.	

### Collision Check
The collision state is updated every tick after all scheduled moves are processed, even if the position of the player or objects has not changed.  

Collision checks are done even if there is no active Collision trigger.  
If the object is toggled off, the collision check is skipped.  
As a small optimization, distance is checked before collision. If the objects or entities are more than 175 units apart on the X or Y axis the collision check is skipped.  
If one of the objects has Extended Collision the distance check is ignored and the collision will be checked regardless of distance.  

Collision checks are done sequentially one target at a time in the following order:
* Player 1
* Player 2
* Dynamic collision objects

## Collision Trigger
Toggles off a **Group ID** when collision blocks collide.

With the **Activate Group** option, toggles on and spawns the given group instead.  
**P1** and **P2** options replace **Block ID1** with Player 1 and Player 2 respectively.  
**PP** replaces **Block ID1** with P1 and **Block ID2** with P2.  

### Activation
Collision activates on block collision, but before the collision state is updated.  
Due to this, if Instant Collision is called from a Collision trigger with the same Block IDs it will spawn the opposite group from the one expected. 
Collision only activates when the collision state of the target IDs changes.

### Spawn Mechanics
Collision triggers can be spawn remapped and have spawn inheritance.
The spawn order of Collision triggers depends on the order collisions are checked.
If spawn an Instant Collision trigger from inside a Collision trigger, and 
### Block IDs
The order of Block IDs does not matter
Block IDs can be identical



## Instant Collision Trigger
Checks the 

Can be remapped but resets remaps.
The collision state is
