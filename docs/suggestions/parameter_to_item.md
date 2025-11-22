# Parameter To Item

Copies the value of a selected variable into the given item ID (item, timer).

Currently, measuring these parameters can be difficult or outright impossible.

This functionality would be split into two to three categories (or menus):
- Object Parameter
- Level Parameter
- Player Parameter

The options listed are examples made to give a general idea on the purpose of the trigger.

UI could be similar to the event selection inside the Event trigger, but only one parameter can be chosen at a time.

The main purpose of this trigger is to make measuring and calculating distances between objects and entities (players) easier, but it could also be used to measure a lot of other things which are currently not possible.

## Object Parameter

References an object using a group ID.

If the group contains multiple objects, it picks one at random (unless using an ID parent).

Options:
- Position (X,Y)
- Last tick move (X,Y)
- Rotation (rad,degrees)
- Scale (X,Y,skew)

## Level Parameter

Returns the value of a given level parameter, such as:
- Object Count
- Lifetime Attempts
- Current Time Elapsed
- Practice Mode
- etc

## Player Parameter

Returns the parameters of either P1 or P2:
- Position (X,Y)
- Velocity (X,Y)
- Momentum (Force) (X,Y)
- Gamemode
- Scale
- Gravity