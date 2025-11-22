# Spawn Triggers

## [2.207] Overwriting a spawn remap of ID 2 crashes the game

If you spawn remap group ID 2 to any ID, then call another spawn which remaps group ID 2 to any other non-zero ID, then call a trigger which uses group ID 2, the game will instantly crash when calling the first spawn.
Only ID 2 is affected.
Only Steam and Android exhibit this bug. Mac and IOS are not affected.

## [2.207] Instant Collision resets remaps

Groups spawned by a remapped Instant Collision do not inherit remaps.

## [2.207] Checkpoint resets remaps

Groups spawned by a remapped Checkpoint do not inherit remaps.

## [2.207] Spamming restart (R key) skips spawn activation

Spamming R quickly can skip the activation of spawns placed before the origin line.
I assume the reason this happens is because the level restarts before the spawn limit is reset, so the triggers are spawn limited on the next restart.

## [2.207] Count spawn inheritance without Multi Activate

If Multi Activate is not selected, the Count's spawn target uses the remaps of the oldest active instance of a subsequent (activated after) Count trigger with the Multi Activate option using the same Item ID.
This makes one-time Count activations in remapped setups annoying to execute, since if you stop a Count trigger during a count update it will skip the next (or more, depending on how many were stopped) Count triggers.

## [2.207] Triggers that are not remappable or not fully remappable

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

## [2.207] Stopping a spawn trigger with delay from another Spawn trigger with delay makes the last Spawn delay spawn again without remaps

Stopping any Spawn trigger with delay while spawn delays are checked makes the game check the last Spawn delay trigger twice, which if it were to spawn in the same tick would activate twice.

It doesn't matter if you stop a Spawn trigger that has already been activated in the current tick, one waiting to activate or you make the Spawn trigger stop itself.

Due to the spawn limit, this bug is only noticeable if the spawn trigger is remapped. The first activation will be remapped while the second spawn activation will have no remaps.

You can use a Spawn trigger with a very high delay value to counteract this bug, as even if it's checked twice it will not spawn.

## [2.207] Spawn triggers on the timeline have inconsistent spawn order and may be delayed or crash the game

The spawn order of different Spawn triggers placed on the timeline does not follow normal spawn order rules.

Some of the Spawn triggers can spawn only in a certain order, and will wait for certain other Spawn triggers to spawn, delaying them for an arbitrary amount of time.

A bug related to this can also crash the game, deleting the triggers and undoing the deletion fixes the crash in most cases.

Deleting and undoing the triggers does not change this order however.

**Example ID**: 115526701
[Video](https://youtu.be/LbjoGxoutUg)

### Spawn Ordered

This bug also affects Spawn Ordered, but only when spawning triggers that were moved.

The spawn delay of triggers spawned by Spawn Ordered depends partly on their current position, which can be affected by move triggers.

Not every move is affected, movements caused by Area triggers are completely ignored.

This behavior is inconsistent however, the game stops ignoring the new delays in some situations, and some spawns may be delayed until another spawns just like those placed on the timeline.