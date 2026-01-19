# Spawn Triggers

## [FIXED 2.208] [19/1/26] Internal Remap Instance IDs are remappable

Every Spawn trigger with remaps is assigned a Remap Instance ID on level load in the order they are loaded in. Spawn triggers without remaps are assigned ID 0.

This Remap Instance ID is remappable which has the following effects:
- Spawn triggers may accidentally use the wrong set of remaps
- The game will crash if the ID is remapped to a remap instance that does not exist

Video Explanation: https://youtu.be/ZDzuKXkeM8g?si=mSGYaf9Lda75WfYV

## [FIXED 2.208] [19/1/26] Instant Collision resets remaps

Groups spawned by a remapped Instant Collision do not inherit remaps.

## [2.208] [19/1/26]  Checkpoint resets remaps

Groups spawned by a remapped Checkpoint do not inherit remaps.

## [2.208] [19/1/26] Spamming restart (R key) skips spawn activation

Spamming R quickly can skip the activation of spawns placed before the origin line in Platformer. This can also happen but only on the very first attempt in Classic.

I assume the reason this happens is because the level restarts before the spawn limit is reset, so the triggers are spawn limited on the next restart.

## [2.208] [19/1/26] Count spawn inheritance without Multi Activate

If Multi Activate is not selected, the Count's spawn target uses the remaps of the oldest active instance of a subsequent (activated after) Count trigger with the Multi Activate option using the same Item ID.
This makes one-time Count activations in remapped setups annoying to execute, since if you stop a Count trigger during a count update it will skip the next (or more, depending on how many were stopped) Count triggers.

## [2.208] [19/1/26]  Triggers that are not remappable or not fully remappable

The following triggers cannot be remapped, or have some IDs that are not remappable. I have highlighted the ones that cause some issues or make things more difficult in certain situations.

These triggers are not remappable:
- _**Color**_
- Rotate Gameplay
- _**Gradient (ID can get remapped but it always disables the gradient)**_
- **Checkpoint**
- Legacy Enter Effect triggers (not spawnable)
- Keyframe (trigger is remappable, groups inside keyframe objects are not)

These triggers have IDs that are not remappable:
- _**Pulse (Color ID)**_
- Spawn (Original Group ID)
- _**Area Triggers (Effect ID)**_
- _**Area Tint, Enter Tint (Color Channel)**_

## [2.208] [19/1/26] Stopping a spawn trigger with delay from another Spawn trigger with delay makes the last Spawn delay spawn again without remaps

Stopping any Spawn trigger with delay while spawn delays are checked makes the game check the last Spawn delay trigger twice, which if it were to spawn in the same tick would activate twice.

It doesn't matter if you stop a Spawn trigger that has already been activated in the current tick, one waiting to activate or you make the Spawn trigger stop itself.

Due to the spawn limit, this bug is only noticeable if the spawn trigger is remapped. The first activation will be remapped while the second spawn activation will have no remaps.

You can use a Spawn trigger with a very high delay value to counteract this bug, as even if it's checked twice it will not spawn.

### Spawn Ordered

This bug also affects Spawn Ordered, but only when spawning triggers that were moved.

The spawn delay of triggers spawned by Spawn Ordered depends partly on their current position, which can be affected by move triggers.

Not every move is affected, movements caused by Area triggers are completely ignored.

This behavior is inconsistent however, the game stops ignoring the new delays in some situations, and some spawns may be delayed until another spawns just like those placed on the timeline.
