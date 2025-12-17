# Area Triggers

## [2.207] [18/12/25] Ease Out conflict

Ease Out is currently bugged and does not apply the effect properly to the radial proximity options.
If the two easings differ they will both apply and conflict \- the game will pick and apply one of them. This is most obvious with opposing easings.

## [2.207] [18/12/25] ModBack / ModFront do nothing for the radial options
ModBack / ModFront are still displayed when used on the radial options despite doing nothing.

## [2.207] [18/12/25] Thin solid hitboxes when scale is negative

When a solid object is scaled by a negative value, hitboxes become very thin and buggy. Spikes and other non-solid hitboxes are not affected.

## [2.207] [18/12/25] Area Fade stops working for a short duration after the game is unpaused
Unpausing the game undoes the effect of Area Fade for one frame.

## [2.207] [18/12/25] Start Position multiplies Area effect

Area effects are accumulated for every calculation when starting from a Start Position.
Only the first tick is affected, the effect is properly applied on the second one.
All Area triggers are affected.
With Area Scale and Area Move, this can crash your game.

### Scale / Rotate Bug

Scaling or Rotating an object by a large amount makes it impossible to undo the transformation if done inside the editor.
This makes all affected objects get their scale and rotation be completely different when stopping playtesting after the bug.

## [2.207] [18/12/25] DEAP has no effect when used on Area Tint or Area Fade

The center group is affected by Area Tint and Area Fade even with **DEAP** selected, **DEAP** effectively does nothing for these two triggers.

## [2.207] [18/12/25] Area Tint ignores Base / Detail Color

Area Tint ignores the Base / Detail Color setting of single-color objects.

## [2.207] [18/12/25] Edit Area with Duration 0 does not override an active Edit Area

Edit Area will override other active Edit Areas only if **Duration** \> 0\.

## [2.207] [18/12/25] Stop has no effect on Edit Area

Stop does not work on Edit Area.
I am not sure if this is unimplemented or a side effect of how Edit Area was implemented.

## [2.207] [18/12/25] Area Scale / Rotate / Move visibility issues

If an object stops being visible, Area Scale / Rotate / Move will stop applying in certain situation.

### Multiple Areas

Example [here](https://youtu.be/8IS5lFdIBus) and level ID in the video description.

### Flickering

Flickering is caused when a target goes off screen and ends up back on screen when the effect is undone every other tick.
Example [here](https://www.youtube.com/watch?v=JgN_ClrC5yk).

### Rendering

Objects with a hitbox that stop being visible once brought off-screen do not render properly if brough back instantly on-screen.

## [2.207] [18/12/25] Toggle Inconsistencies

Toggle disables Area effects on the object only in very particular cases depending on the area settings.
This should be replaced by a dedicated **Ignore Disabled** feature as there is no logic or indication to this behavior.

## [2.207] [18/12/25] Edit Area Tint / Fade doesn't pause in editor

Edit Area Tint and Edit Area Fade do not get paused when pausing the editor playtest.

[Video](https://youtu.be/DKtR5YL6qAI?si=Zd47Lgf6qV_ZNnxk)
