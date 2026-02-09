# Toggle Object

Toggles off a **Group ID** when the player clicks while inside its hitbox.

Can be used as an orb or as a block, both are functionally identical.

## Options

Toggles on and spawns a group instead if **Activate Group** is enabled.

**Spawn Only** makes it only spawn the target group without toggling it. **Activate Group** does not change this behavior.

If **Claim Touch** is enabled the player's input is used only by the toggle object, this input will not activate other orbs or make the player jump or boost.

## Notes

Only one toggle object can be activated by an input at once. If multiple toggle objects overlap the player, each input will activate a different one in a fixed sequence, based on the order you collided with each toggle object. 
