# Re-Target Advanced Follow

Changes the follow target of an Advanced Follow effect.

## Options

**Target GID** references one or more Advanced Follow triggers by **Group ID** or **Control ID** (if **Target Control ID** is selected).

**P1**, **P2** and **C** can also be selected as new follow targets.

## Behavior

The activation of Re-Target Advanced Follow is instant.

If **Target GID** exists but is not a valid follow center, the advanced follow effect remains active but will not apply on the target. The trigger has no effect if **Follow GID** is 0.
Both **Target GID** and **Follow GID** can be remapped.

While instances of an Advanced Follow trigger are unique for sets of target, follow and control IDs, if you retarget an instance of Advanced Follow to a new follow center it will allow you to create a new instance with the old IDs. The old instance can be retargeted back to the old follow center and you will end up with multiple instances using the same set of IDs.

