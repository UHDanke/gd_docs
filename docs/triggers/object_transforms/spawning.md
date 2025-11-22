# Spawning

Keyframes can spawn even if no **Group ID** or **Target ID** is defined.

All keyframe spawns happen prior to object transforms.

If Animate Keyframe is spawned by a keyframe, it'll activate in the same tick. Spawns with **Duration** 0.00 will spawn in the same tick, after the current spawns end, in order of activation.

Spawn limits are determined per keyframe object, not Animate Keyframe triggers.

**Animate Group ID**, **Target ID** and **Parent ID** can be remapped.

The **Group IDs** and **Spawn IDs** of keyframe objects cannot be remapped, but keyframe spawns inherit remaps from Animate Keyframe.