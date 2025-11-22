# Particles

## [2.207] Toggling off or unloading a Particle Object does not clear particles in playtesting

In editor, toggling off or unloading a Particle Object disables and clears all particles created by it.
In playtesting, the particles are not cleared and become separate from the particle object - any changes to the main object no longer affect the disconnected particles which continue to linger until they despawn.

## [2.207] Deselecting **Animate on Trigger** deselects the option for all particle objects

Deselecting the **Animate on Trigger** option deselects the option for all particle objects when the level is saved.

## [2.207] Particles with long lifespans linger after a level restart if **Quick Start** is selected

Particles are not properly cleared when the level restarts if using the **Quick Start** option.

## [2.207] Uniform Color particles spawned by Spawn Particle are not uniform

A particle with the Uniform Color option that is spawned will use the color channel value at the time of spawning instead of syncing with the color channel continuously.

## [2.207] Some Particle Objects can end up having erratic spin

Particle objects can get bugged and end up having very erratic movement.
Level ID: 114681413

[Video](https://youtu.be/5zb-JCvD5JY)

## [2.207] Particle sometimes fail to spawn when near the particle limit

The first particle in a particle loop will fail to spawn if the particle limit has been hit already.

This usually happens if $Emission \cdot Lifetime = MaxParticles$

## [2.207] Spawn Particle Position Group ID is tied to game FPS

The spawn position of particles with Spawn Particle is the position of the group at the last rendered frame, instead of the current position.
This can cause particles to spawn in the wrong position when dealing with high speed or instant movement when the game runs below 240 fps.
The bug only happens while playtesting and not in the editor.

[Video: 200, 300, 60 and 120 fps](https://youtu.be/Co1UDLP2Ahk)
[Video: 120 fps vsync, mobile](https://youtu.be/wxT__dKYsr8?si=X3O1ywGwrP5fIucm)

Setup attempts to spawn a particle every tick on a moving target.
ID: 114953438

## [2.207] Spawn Particle fails to spawn on inactive targets

Spawn Particle will not spawn if the target is inactive (position is off-screen).
This only happens while playtesting and not in the editor.
If the object was active on screen at least once before, the particle will spawn at its previous on-screen position.

Link Visible can keep the target active as a potential workaround to this issue.
While this might be intentional for performance reasons, there should be an option to allow the particle to spawn regardless of whether the target is active or not.

[Video](https://youtu.be/Co1UDLP2Ahk)