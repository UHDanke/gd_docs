# Events

## Player Reversed event does not activate

**Fixed:**   
**Version:** 2.207  
**Date:** 18/12/2025  

### Description
Player Reversed event does not seem to activate when the player reverses direction in any circumstance. It used to activate only on pad / orb reversal but that no longer seems to be the case.

## Feather Landing event does not trigger if the player does not land with downward velocity

**Fixed:**   
**Version:** 2.207  
**Date:** 18/12/2025  

### Description
If the player lands with close to 0 velocity or clips / teleports into an object while traveling upwards none of the landing events will trigger.

## Left/Right Release events do not trigger if interrupted by the other direction on mobile

**Fixed:**   
**Version:** 2.207  
**Date:** 18/12/2025  

### Description
On mobile devices, if you press Left while already pressing Right (and vice-versa), releasing Right after this will not trigger a Right Release (or Left Release) event. This affects both player events.

## Input Release events do not trigger if game is paused

**Fixed:**   
**Version:** 2.207  
**Date:** 18/12/2025  

### Description
If you pause the game while holding a player input and release it during the pause, the input release event will not trigger. Input release should trigger on unpausing if the player no longer holds the input.
