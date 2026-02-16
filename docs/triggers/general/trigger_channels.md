# Trigger Channels

Channels limit what objects the player interacts with, players on a channel will not collide with or activate interactibles placed on other channels.

The player's current trigger channel can be changed using a Gameplay Arrow trigger.

## Notes

All players share the same channel.

Channel 0 is the default channel.

## Collisions

Interactibles affected are:
- Gameplay Objects
- Triggers (touch trigger)
- Collectibles

Objects not affected are:
- Collidables
- Hazards
- Collision Objects

Channel 0 is special for collisions in that it interacts with every other channel:
- if the player is on channel 0, it can interact with all triggers and objects regardless of channel.
- if an object is on channel 0 it will interact with players regardless of what channel they are on.

## Timeline

The timeline uses the player's current trigger channel.

The timeline can activate triggers on the same channel only, channel 0 has no special behavior.

If the timeline changes direction or channel, all triggers that will be behind the timeline after the change will activate at the same time.
