# Sequence Control

Sequence is one of the new triggers introduced in update 2.2 which makes it easier to spawn groups in a specific order from a single trigger.  
Previously, to get the same effect you would need to implement a switch-case using Instant Count triggers, where you check if the Item ID value is equal to any of your defined cases and spawn a group if the value matches your case.

The issue with Sequence is you do not have a trigger like Pickup or Item Edit that can modify the Sequence's counter. You cannot reset, go back or modify the sequence's current step easily.   
This limits what you can do with Sequence significantly; If you want to reset or set the counter to a specific value on demand, you need to use the old method of Pickup \+ Instant Count (or Item Edit / Item Compare).

As to why Sequence should have this capability, it is for ease of use and optimization.  
Setting up a Sequence trigger is easier and much less tedious than a switch case. It is also a single trigger and you do not need to spawn multiple Instant Count / Item Compare triggers to implement something as simple as indexing a list. No need for an Item ID either and it makes looping logic much easier to do.  
Taking this into consideration, i propose a Sequence Control trigger to make up for Sequence's shortcomings.

## Options & Functionality

Modifies the current step of a Sequence trigger.

### Options

#### Counter

Modifies the current counter value.

#### Set / Offset

Whether Counter offsets or sets the counter value.

#### By Group

If selected, Counter works by group instead of by step. This always resets the counter before the first step of the group.

#### Group ID

The group ID of the affected Sequence trigger.

#### Use Control ID

Use control ID instead of group ID.

### Usage Examples

Set 0 resets the counter to 0 (like Reset Full).  
Set \-1 sets the counter to the last step.  
Offset \-1 decreases the counter by 1 (like Reset Step).  
Offset \+1 increases the counter by 1 (skips step).  
With Mode Stop and Mode Last, if the counter is outside.  
With Mode Loop, if the counter is larger than the sequence's steps it will loop forwards, if it's negative it loops backwards.  
The behavior i propose for negative looping is different from Reset Step, which only resets down to the first step and does not go further.  
With By Group, Set 2 sets the counter to the first step of the second group. Offset \-1 goes back to the previous group, Offset 1 skips to the next group. This is useful for advanced looping logic.  
With Unique Remap the Sequence trigger has an unique counter for each remap trigger. Use Control ID would allow you to target a specific counter.

