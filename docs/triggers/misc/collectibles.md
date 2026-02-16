# Collectible

Collectibles are objects than can be picked up when the player gets near them.

## Edit Pickup Options

Certain actions can be tied to picking up a collectible:
- **Pickup Item** - the value of the **Item ID** is increased by 1. If **Sub Count** is selected, the value is decreased by 1 instead.
- **Toggle Trigger** - toggles off target **Group ID**. If  **Enable Group** is selected, the target group is toggled on and spawned instead.
- **Points** - increase the current points score by the given amount.
- **Particle** - spawns particles from a group at the position of the collectible. This option behaves identically to a Spawn Particle trigger with default settings.

All collectibles except user coins can use these settings.


