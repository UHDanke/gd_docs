# Zoom Camera

Changes the camera's current **Zoom** over a **Duration** of time with an **Easing**.

**Zoom** values higher than 1 zoom in, while values lower zoom out. Negative **Zoom** flips the camera on both axes.

The default value of **Zoom** is 1.000 and it is limited between 0.400 (x2.5 times zoomed out) and 3.000 (x3 zoomed in). This does not affect the max zoom level that can be hit through easings like back or elastic.

Only one Zoom change can be active globally, new activations overide previous ones.

The C reference of an Advanced Follow trigger follows the bottom-left corner of the screen when zoomed or offset.