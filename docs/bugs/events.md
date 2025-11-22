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