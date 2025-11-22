# Camera Edge

Defines an object given by **Target ID** as one of the camera's **Left**, **Right**, **Up** or **Down** limit edge.

Target ID must contain a single object or an ID parent.

Edge triggers cannot be stopped, unlocking an edge can only be done by setting the group to an unused group, such as 0, or to a group with more than one target.

The **Left** edge has priority over **Right**, and **Down** has priority over **Up**.

Camera Edge follows the movement of a target object.

## Default Edges

Y = 0 is the lowest the camera's bottom edge can go and cannot be overriden. It has priority over all other Y axis edges.

X = 30 is the furthest left the camera can go on the first attempt only. It has priority over all other X axis edges and cannot be overriden. On future attempts this edge is not applied.

The ceiling counts as a camera edge and can be overriden by a **Down** edge, but not by a **Top** edge. The ceiling is set 240 units above the topmost object.
The end wall counts as a camera edge and can be overriden by another **Left** edge, but not by a **Right** edge. The end wall is set 355 units right of the rightmost object in classic mode, platformer has no end wall.

## Player Camera

Locking the edge moves the camera instantly to a valid position, while unlocking makes the camera ease back towards its normal position.

## Static Camera

Camera Edge also affects static cameras. When unlocking the camera, the movement will be instant if the Static Camera doesn't follow the target, otherwise it will use the follow's easing value.