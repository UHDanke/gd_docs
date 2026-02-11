# Trigger Channels

Channels can be used to limit what objects the player interacts with, players on a channel will not collide with or activate interactibles placed on other channels.

Interactibles affected are:
- Gameplay Objects
- Triggers (except spawn-triggered)
- Collectibles

Objects not affected are:
- Collidables
- Hazards
- Collision Objects

Channel 0 is special in that it interacts with every other channel:
- if the player is on channel 0, it can interact with all triggers and objects regardless of channel
- if an object is on channel 0 it will interact with players regardless of what channel they are on
