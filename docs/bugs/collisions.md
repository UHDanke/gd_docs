# Collisions

## [2.207] [18/12/25] Move Silent Collision crash

If you spawn a Move trigger with the Silent option from inside a Collision trigger that moves two or more collision objects (at least one being dynamic) the game will sometimes crash.

The dynamic collision object must be moved before it checks for collisions.

The crash will not trigger if Extended Collision is used on the dynamic collisions, it is likely the crash happens when the game tries to check the chunks of the collision objects that were moved.

Example ID:
114561987

## [2.207] [18/12/25] Spider teleports through or into Extended Collision objects.

Spider gamemode and Spider Orb teleports through or into an object with extended collision instead of on it.

Spider Pad is not affected by this issue.
