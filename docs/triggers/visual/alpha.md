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