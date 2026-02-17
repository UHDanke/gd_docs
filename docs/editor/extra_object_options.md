# Extra Object Options

Miscellaneous options that enable or disable extra properties of an object.

## Dont Fade

Disables fade from enter effect presets and from Fade Enter.

## Dont Enter

Disables most enter effects. 

Does not apply to fades from enter effect presets, but does apply to fades from Fade Enter.

## Group Parent

Defines the center object of a linked group or for a selection of objects. Also acts as an Area Parent if none other exist on the current linked group.

Acts as the center of scaling and rotation for the linked group when targetted by Area triggers.

## Area Parent

Defines the reference object of a linked group. Also acts as a Group Parent if none other exist on the current linked group.

Used by Area triggers and Advanced Follow to define the center of a group for distance calculations, and also the center for Advanced Follow rotation.

## Dont Boost Y

Makes blocks that push the player upwards not boost the player's movement. Movement equal or slower to 10 blocks per second do not boost the player.

## Dont Boost X

Makes blocks that push the player sideways not boost the player's movement. Movement equal or slower to 10 blocks per second do not boost the player.

## High Detail

Prevents the object from being loaded if LDM is enabled. 

This also prevents on load triggers from activating.

## No Touch

Disables the object's collisions.

Works partially for collision objects, the collision still exists but its position and rotation can only be updated by an Area or Enter effect.

## Passable

Makes the object act as a platform, the player can freely pass through the object from the sides or bottom of the object but not from above. This is relative to the direction gravity is applied on the player.

The player is teleported on top of the block if the bottom hitbox of the player is inside the block and within 1/6th of it's top side.

## Hide

Makes the object invisible and hides its particles. This is not the same as toggling off the object and still counts as being on-screen.

## Non Stick X

Makes the player not stick to blocks that move sideways relative to the player.

## Non Stick Y

Makes the player not stick to blocks that move downwards relative to the player. 

Overrides Extra Sticky and does not work on slopes.

## Extra Sticky

Makes the player stick better to blocks that move downwards. Only works in platformer mode.

By default the player can stick to an object moving down if it it's moved at roughly ~20.35 blocks per second, Extra Sticky extends this to ~40.35 blocks per second.

Does not work on slopes.

## Scale Stick

Makes the player move with the object when it scales horizontally (relative to the player). 

The player will stick to an object when it scales vertically (relative to the player) even if this option is disabled.

Only works in platformer mode.

## Extended Collision

By default the player or a dynamic collision object will only check for collisions in the chunk it is part of and that chunk's neighbors, this option removes that limitation.

Chunks are 100x100 units wide (3.33 blocks) and are aligned to the level's (0,0) coordinate.

## IceBlock

Makes the object slippery when moving sideways in platformer mode.

Does not apply if the player touches other non-slippery blocks.

Ice blocks reduce the player's horizontal friction by roughly ~97.2% and acceleration by ~62%.

## Grip Slope

Makes slopes no longer slippery. 

Slopes with an incline of 40 degrees or higher make the player slide down them.

## No Glow

Removes the glow layer from objects that have glow.

## No Effects

Disables visual effects on objects that create them like orbs, portals and pads. Does not include particles.

## No Particle

Disables particles on objects that create them.

Does not work on custom particle objects.

## No Audio Scale

Removes the scaling effect in response to audio from certain objects like orbs and some decorations.

Does not work on the classic 1.0 rod decorations.

## Single P Touch

Limits activations of a trigger that activates on touch to once per tick. Without this option, if multiple players collide with the trigger at the same time the trigger would activate once for each player.

Only works on triggers with the Touch Trigger option, it doesn't work on other interactibles like pads, portals and orbs.

This option is only visible when selecting a gameplay or trigger object.

## Center Effect

Makes touch-triggered Gameplay Arrow, Teleport (trigger & single portal) and Reverse triggers activate when the preview line passes through the center of the trigger instead of when the player would collide with their hitbox.
 
Doesn't work on other triggers as they already have this behavior by default when touch-triggered.

This option is only visible when selecting a gameplay or trigger object.

## Reverse

Reverses the player's direction on use. Reverse works only in classic mode.

This option is only applicable to pads and orbs.
