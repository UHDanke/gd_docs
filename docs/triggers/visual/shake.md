# Shake

Applies a shaking effect to the screen.

## Behavior

Shakes the screen by moving the view on both X and Y axes by a random offset multiplied by **Strength**. The view is offset every **Interval** until **Duration** runs out.

UI, Background and Middleground will not move at all. Ground will only move vertically.

Only one shake effect can be active at a time and new shakes override previous ones. This includes the on death shake as well, which can be overriden.

### Options

**Strength** and **Duration** must both be bigger than 0 for the shake to trigger.

If **Interval** is 0, the view will offset every render frame.

The lowest value of **Strength** that can be used is 0.01, which is low enough to be imperceptible.

The max values of a Shake trigger are **Strength** 100, **Interval** 0.20s and **Duration** 10.00s.

All shaking effects can be disabled using the **Disable Shake** level option.