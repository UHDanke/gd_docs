# Sequence Trigger

Spawns a group ID from a sequence of group IDs when activated. The sequence advances by one step every activation.

## Sequence Menu

A new group ID and a count of how many times the activation of the group will be repeated can be added to the sequence using the **[+]** sign.

Groups part of a sequence can be selected by clicking on them. 

Clicking on **[+]** while a group is selected will increase the group's count by the given value.

Clicking on **[-]** removes the group, while clicking on the arrows **[<]** and **[>]** moves the group before the previous group or after the next group, respectively.

The menu will show up to 20 groups at a time but there is no limit to the number of groups that can be added.

## Options

### MinInt

**MinInt** sets a cooldown to sequence activations, the sequence trigger will not activate if the time between the last activation and the current call is less than **MinInt**.

### Reset 

**Reset** resets the number of steps done by the sequence if the time between the last activation and the current call is more than **Reset**. If **Reset Full** is selected, the sequence will reset back to step 0. If **Reset Step** is selected, the sequence will reset one step for every **Reset** duration, down to step 0 at most. 

### Mode

Mode controls the behavior of the sequence when its last step is reached.

**Mode Stop** is the default behavior, the sequence will stop activating groups after the last group is reached. For the purpose of **Reset Step**, the sequence stops at a step one above the last group, which spawns nothing if activated.

**Mode Loop** makes the sequence reset its step back to 0 after the last step has been reached. **Reset** will not loop back to a higher step or reset below step 0 even if using **Mode Loop**.
 
**Mode Last** stops the sequence at the last step. Further activations will keep spawning the last group ID in the sequence.

### Unique Remap

**Unique Remap** makes the sequence unique to each remap instance that has spawned the trigger. These instances will keep track of their current sequence step and when they last activated the sequence trigger.