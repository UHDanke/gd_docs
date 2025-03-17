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

If a color change is overriden by another color change (be it fade or copy), the current color value will be saved as the channel's color. This color value is static even if it resulted from a copy color.

In the case of Copy Color, a channel can copy only one channel at a time. If the channel fades towards a copy color, then the color value will fade between the channel's color and the copied channel's current color.

Color fading behavior also applies to opacity. Color copy behavior only applies if using **Copy Opacity**.

Blending changes are instant and cannot be faded.

## Spawning

Color can be spawned by other triggers, but cannot be remapped in any way.

## Stop

Stopping or Pausing color fades interrupts the color change at it's current color mix.

Copy color remains active even if the color change was stopped, the current color and the copy color will continue to be mixed at the current fade until resumed or interrupted by another color change.

Due to a bug, stopped color changes will resume when respawning from a checkpoint. Paused color changes will not resume however.

Control IDs do not work on Color triggers. Color cannot be stoped, paused or resumed by a Stop trigger using Control ID.



# Pulse

Temporarily changes the RGB values of a given color channel.

## Behavior

Pulse triggers cannot change a channel's opacity or blending properties.

Pulse triggers effects are temporary and are cleared once the Pulse trigger stops being active. 

Additionally, color changes done by Pulse triggers cannot be copied by other color channels.

### Display Limits

While multiple Pulse triggers can be active per channel, only the latest one will be displayed.

Fade In and Fade Out pulses will always fade to and from the channel's color, even if other pulses are active.

This limit applies to HSV pulses as well, not just color pulses.

A similar limit applies to Pulse triggers that reference Group IDs as well, but this limit is per object not per group.

These two limits are independent, a Pulse trigger that acts on channel and another that acts on a group can stack together as a result.

Color trigger fades and object HSV settings will stack with HSV pulses.

## Options

### Fades

Pulses can fade into the target color or HSV, hold that value then fade out over a period of time.

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


# Shake

Applies a shaking effect to the screen.

## Behavior

Shakes the screen by moving the view on both X and Y axes by a random offset multiplied by **Strength**. The view is offset every **Interval** until Duration runs out.

UI, Background and Middleground will not move at all. Ground will only move vertically.

Only one shake effect can be active at a time and new shakes override previous ones. This includes the on death shake as well, which can be overriden.

### Options

Strength and Duration must both be bigger than 0 for the shake to trigger. 

If Interval is 0, the view will offset every render frame. 

The lowest value of Strength that can be used is 0.01, which is low enough to be imperceptible.

The max values of a Shake trigger are Strength 100, Interval 0.20s and Duration 10.00s.

All shaking effects can be disabled using the "Disable Shake" level option.


# Toggle

Toggles off objects, making them invisible and non-interactible.

## Behavior

Toggled objects are invisible and count as being inactive.

The player will not interact with toggled hitboxes, such as solid blocks, spikes or collision blocks.

### Collisions

Collision checks are skipped for toggled off collisions.

Dynamics will check their toggle state only once, prior to checking other collisions.

### Triggers

Toggled triggers will not activate. 

Toggling off a trigger will only prevent it from activating, it will not stop it if it's already active.

Other triggers also toggle groups on or off, these are:
* Touch
* Count
* Collision
* Toggle Orb / Block
* On Death

# Alpha

Modifies the opacity of the objects of a target Group ID.

## Behavior

Like the Color trigger, the opacity value can fade over a duration from the current to the new value.

Opacity is stored per Group ID. Only one alpha change can be active per group at a time, spawning another overrides the previous one.

An object can be under multiple alpha effects from different groups. 

## Spawning

Alpha can be spawned by other triggers.

Group ID can be remapped.

## Stopping

Stopping or Pausing Alpha triggers stops the fade at its current value. 

The fade will continue if Resumed, as long as it hasn't been overriden by another Alpha trigger.

Alpha supports Control IDs.

# Change Background 

Changes the level's Background to a different preset. There are currently 59 BG presets.

Only one Background change can be made per render frame. The first will trigger, while any other subsequent BG trigger is ignored until the next frame.


# Change Middleground

Changes the level's Middleground to a different preset. There are currently 3 MG presets.

Only one Middleground change can be made per render frame. The first will trigger, while any other subsequent MG trigger is ignored until the next frame.


# Change Ground

Changes the level's Ground or Line to a different preset. There are currently 22 G presets and 3 Line options.

Only one Ground change can be made per render frame. The first will trigger, while any other subsequent G trigger is ignored until the next frame.


# Link Visible

Makes all objects part of a group active if at least one of them is active.

## Behavior

This trigger is activated on level load no matter where its placed. It cannot be activated later or deactivated in any way.

Objects count as being active if they are on-screen. 

### Toggle

Toggled off objects count as inactive for Link Visible. 

### UI

UI objects that are visible on-screen also count as active for Link Visible.

### Object Linking

Object Links and Group ID Parents are ignored by Link Visible.

### Invisible Objects

Making the object invisible with Hide, Alpha, Opacity or Blending does not make them inactive.
