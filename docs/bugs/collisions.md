# Collisions

## Move Silent Collision crash

**Version:** 2.208\
**Date:** 30/01/2026\
**Level ID:** 114561987\

### Description
If you spawn a Move trigger with the Silent option from inside a Collision trigger that moves two or more collision objects (at least one being dynamic) the game will sometimes crash. The dynamic collision object must be moved before it checks for collisions. The crash will not trigger if Extended Collision is used on the dynamic collisions, it is likely the crash happens when the game tries to check the chunks of the collision objects that were moved.

## Spider teleports through or into Extended Collision objects.

**Version:** 2.208\
**Date:** 30/01/2026\
**Level ID:** 114561987\

### Description
Spider gamemode and Spider Orb teleports through or into an object with extended collision instead of on it. Spider Pad is not affected by this issue.
