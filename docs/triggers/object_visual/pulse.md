# Pulse

Temporarily changes the RGB values of a given color channel.

## Behavior

Pulse triggers cannot change a channel's opacity or blending properties.

Pulse triggers effects are temporary and are cleared once the Pulse trigger stops being active.

Additionally, color changes done by Pulse triggers cannot be copied by other pulses, color triggers or color channels.

### Rendering

Pulses are applied after color changes, object HSV is applied after all pulses and color changes.

Pulses are rendered in the following order, from top to bottom:
- Group (Color)
- Group (Color ID + HSV)
- Group (HSV)
- Channel (Color ID + HSV)
- Channel (Color)
- Channel (HSV)

### Stacking

HSV pulses stack together, while pulses that copy or apply a color only combine while fading.

Channel (Color ID + HSV) will disable any pulse below it while active.

## Options

### Fades

Pulses can fade into the target color or HSV, hold that value then fade out over a period of time.

Color changes fade in linearly, while HSV changes fade in using Ease In (2.00). **Static HSV** makes HSV changes fade in linearly as well.

### Copy Paste

Pulse triggers have the Copy and Paste color option, but do not share the Default color option of Color triggers.

### Pulse Mode

The pulse behavior can be changed with the Pulse Mode options Color and HSV.

Color pulses with a solid color given by RGB values or hex code.

HSV can be used to offset the object or channel's color by Hue, Saturation and Value (or Brightness).

Unlike Color triggers, Pulse Triggers can copy the value of the same channel ID they target.

In the case of pulses the copied value will be the channel's primary value, so pulses will not copy their own HSV offsets.

### Target Type

The pulse target can be modified using the Target Type settings Channel and Group.

Channel applies the pulse effect per channel.

Group applies the pulse effect on all objects part of the group.

### Exclusive

A Pulse trigger with Exclusive will clear other pulses active on the same target.

For Channel mode, pulses on the same Channel ID are affected.

For Group mode, pulses on the same Group ID are affected.

## Spawning

Pulse triggers can be spawned by other triggers.

Spawning a pulse trigger multiple times will not override previous pulses of the same trigger.

**Channel ID** and **Group ID** are remappable, while Color ID is not.

Normally, you are not able to reference channels outside IDs 1-999 (or the special channels). With remapping, you can pulse any channel between 1 and 1101, including special and unused channels that cannot be referenced otherwise.

Pulsing ID 0 or lower will do nothing.

Color Channels higher than 1101 are the same as 1101.

## Stopping

Pulse triggers can be stopped, paused and resumed.

Paused pulses will be frozen at the current fade until resumed.

Pulse triggers support Control IDs.