# Color Assignment

Objects can be assigned a color using the Edit Object menu.

Color channels as well as HSV and layering settings can be modified per object.

## Color Layers

Objects have at least one of Base (primary) or Detail (secondary) color layers.

For objects with a single color layer, you can select whether its treated as a Base or Detail color using the options (gear) sub-menu.

## Channel Selection

A color channel for Base or Detail can be selected using this menu. The channels available are, in placement order:
* Player Color 1
* Player Color 2
* Light BG
* Default
* 1-9
* Last selected channel ID

All color channels can be viewed using the Browse option.

The Next Free option selects the lowest unused color channel.
Unused color channels have default values, are not used by any object or referenced by any Color or Pulse triggers.

The channel ID select box can be used to select a specific ID, including ones higher than ID 999.

Objects can use any color channel between 1 and 1101. Other elements such as BG (Background) and G (Ground) cannot be reassigned to another channel.

ID 0 is replaced by the Default channel.

## HSV Selectors

The object's colors can be offset from the color channel using the Hue, Saturation and Brightness (Value) sliders or by modifying the value directly.

Saturation and Brightness are multiplicative, but can be made additive using the corresponding check box.

Current HSV settings can be cleared using the trash button.