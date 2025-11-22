# Other Color and Layering Options

## Color Filter

Found in the Delete menu, this option limits selection and deletion to objects that have the given color channel.

Valid channels are between 1-1101.

The following special channel can be selected using the menu:
* Obj
* Lighter
* 3DL
* P1
* P2

## Copy Values

Copies the following properties of an object:
* Color Channels
* HSV values
* Editor layers
* Z settings (Order and Layer)
* Groups
* Extra

These properties are not copied:
* Base / Detail
* Group ID Parents
* Extra2
* ORD
* CH

Properties can also be copied using the **Copy** button in the **Edit Group** menu. This feature is functionally identical to **Copy Values**.

Copied properties are not stored when exiting the editor, unlike copied objects.

### Paste State

Pastes the group properties of an object onto another object.

Groups will not be pasted if the **Disable Paste State Groups** editor option is selected.

State can also be pasted using the **Paste** button in the **Edit Group** menu. This will in addition paste the copied color settings.

**Disable Paste State Groups** does prevent the **Paste** button from pasting groups, despite being noted otherwise.

### Paste Values

Pastes the color properties of an object onto another object

Color values can also be pasted using the **Paste** button in the **Edit Group** menu. This will in addition paste the copied object settings.

## Copy + Color

Copies selected objects and their colors.

This will only copy colors with non-default values, colors used by objects or referenced by Color or Pulse triggers that have default values will NOT be copied.

Paste can be used to paste objects copied using this option, but this will not change their colors.

## Paste + Color

Pastes selected objects, remapped to new color channels if they are already in use.

The new channel assignment is done similar to **Next Free**.

This will also paste objects copied using the **Copy** option, being identical to **Paste** as **Copy** does not save color information.

IDs referenced by copied Color or Pulse triggers copied alongside the objects will also be remapped by this function. The only ID that cannot be remapped with this is the Channel ID of a Pulse trigger.

## Reset Unused

Resets color channels with non-default values that are not used by any object or referenced by Color or Pulse triggers.