# Select Color Menu

The color of a channel can be initialized in the level settings using the Select Color menu.

HSV values can be assigned in three ways:
- Individual RGB values
- Hex code
- Hue ring and Saturation-Value wheel

**Opacity** can only be modified with a slider.

The **Blending** option makes objects and Middle Ground blend additively with other layers.

**Player Color 1** and **Player Color 2** copy the player's colors.

## Copy Paste

The **Copy** button copies the RGB values from the color channel or Color / Pulse trigger.

The **Paste** button pastes the copied RGB values into the current channel or trigger.

The **Default** button copies the color channel's RGB and opacity values into the current Color / Pulse trigger . This button does nothing if used inside a color channel.

## Copy Color

Color channels can copy the colors of other channels using this option.

### Behavior

Copy Color effects are not instant and count as active color changes.

As color effects are done by frame, only on the next render frame will the color be copied.

Custom color channels (1-999) cannot copy themselves, but special channels (BG, G, etc) can. You need a secondary custom color in order to make them copy themselves.

### Channel Options

Channels that can be copied include:
* 1-999
* BG (1000)
* G1 (1001)
* G2 (1009)
* L / Line (1002)
* Obj (1004)
* 3DL (1003)
* MG (1013)
* MG2 (1014)

P1 and P2 used to be copy color options prior to 2.2 alongside the separate **Player Color 1** and **2** options, but are no longer assignable in-game.

**Player Color 1** and **2** are ignored if Copy Color is present.

The channel color can be further offset using the HSV sliders. Unlike the object HSV options, you can only use sliders and cannot modify the value directly.

**Legacy HSV** cannot be disabled in the default color list.

### Other Properties

Blending is not copied.

Opacity is not copied unless Copy Opacity is selected.

Color changes done by Pulse triggers are not copied.