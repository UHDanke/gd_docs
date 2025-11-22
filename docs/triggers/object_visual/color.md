# Color

Changes the RGBA values and blending properties of a given color channel.

For more info on how the color select menu works, check the colors editor guide.

## Behavior

### Timings

Color changes are registered based on the next rendered frame, not on the game's ticks.

Only one color change per color channel can be active at once. Color changes include color fades and copy color.

Setting the color channel to a new value (not copy color) is instant.

### Color Changes

For fading color changes, the color will fade between the channel's current color and its new color.

If a color change is overriden by another color change (be it fade or copy), the current color value will be saved as the channel's color. This color value is static even if it resulted from a copy color - as a result, a channel can copy only one other channel at a time.

Copy color fades are updated whenever the copied channel changes color. If the channel fades towards a copy color, then the color value will fade between the channel's color and the copied channel's current color.

Color fading behavior also applies to opacity. Color copy behavior only applies if using **Copy Opacity**.

Blending changes are instant and cannot be faded.

Color and HSV changes fade in linearly, **Legacy HSV** makes HSV changes apply instantly regardless of fade.

## Spawning

Color can be spawned by other triggers, but cannot be remapped in any way.

## Stop

Stopping or Pausing color fades interrupts the color change at it's current color mix.

Copy color remains active even if the color change was stopped, the current color and the copy color will continue to be mixed at the current fade until resumed or interrupted by another color change.

Due to a bug, stopped color changes will resume when respawning from a checkpoint. Paused color changes will not resume however.

Control IDs do not work on Color triggers. Color cannot be stoped, paused or resumed by a Stop trigger using Control ID.