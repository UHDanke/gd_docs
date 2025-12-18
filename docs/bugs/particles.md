# Particles

## [2.207] [18/12/25] Toggling off or unloading a Particle Object does not clear particles in normal mode

In editor, toggling off or unloading a Particle Object disables and clears all particles created by it.
In playtesting, the particles are not cleared and become separate from the particle object - any changes to the main object no longer affect the disconnected particles which continue to linger until they despawn.

## [2.207] [18/12/25] Particles with Duration -1 may lose **Animate on Trigger** randomly

Particles with infinite (-1) Duration can lose both animate settings on when loading the editor.

## [2.207] [18/12/25] Particles with long lifespans linger after a level restart if **Quick Start** is selected

Particles are not properly cleared when the level restarts if using the **Quick Start** option.

## [2.207] [18/12/25] Uniform Color particles spawned by Spawn Particle are not uniform

A particle with the Uniform Color option that is spawned will use the color channel value at the time of spawning instead of syncing with the color channel continuously.

## [2.207] [18/12/25] Weird transparency on particle objects

Particle objects calculate transparency inconsistently depending on what settings you select, as show in the following table:

| Additive | Obj Color | Uniform Color | Blending | Solid Alpha | Blending Alpha |
| :---: | :---: | :---: | :---: | :---: | :---: |
| No | No | No | Either | $(start \cdot (1-t)+end\*t) \cdot base$ | \- |
| No | No | Yes | No | $(start \cdot (1-t)+end \cdot t) \cdot base$ | \- |
| No | No | Yes | No | $(start \cdot (1-t)+end \cdot t) \cdot base$ | \- |
| No | Yes | No | No | $(base \cdot (1-t)+end \cdot t) \cdot base$ | \- |
| No | Yes | No | Yes | \- | $(base^2 \cdot (1-t)+end \cdot t) \cdot base^2$ |
| Either | No | Yes | Yes | \- | $(start \cdot (1-t)+end \cdot t) \cdot base^2$ |
| Yes | Yes | No | No | $(base \cdot (1-t)+end \cdot t) \cdot base$ | $((1-base) \cdot (1-t)+(1-end) \cdot t) \cdot base$ |
| Yes | Yes | No | Yes | \- | $(base \cdot (1-t)+end \cdot t) \cdot base^2$ |
| Yes | No | No | Either | \- | $(start \cdot (1-t)+end \cdot t) \cdot base^2$ |
| Yes | No | Yes | No | $(start \cdot (1-t)+end \cdot t) \cdot base$ | $((1-start) \cdot (1-t)+(1-end) \cdot t) \cdot base$ |

Notes:
- $start$ is the initial alpha, equal to: $Start\textunderscore A+Start\textunderscore A\textunderscore Rand$
- $end$ is the final alpha, equal to: $End\textunderscore A+End\textunderscore A\textunderscore Rand$
- $base$ is the alpha (opacity) of the base color channel.
  - The detail color channel's opacity is not used by particles.
  - **Use Obj Color** replaces $start$ with $base$ in all calculations.
  - $base$ is applied multiple times in some equations.
- For a particle to count as blending either the base or detail color must be blending.
  - If **Use Obj Color** or **Uniform Obj Color** are used with **Additive** but neither color channels blend, then the particle renders as both normal and additive.
- The resulting color for one particle is equal to: $BG\textunderscore RGB*(1-Solid\textunderscore Alpha)+Particle\textunderscore RGB*(Solid\textunderscore Alpha+Blending\textunderscore Alpha)$

## [2.207] [18/12/25] Some Particle Objects can end up having erratic spin

Particle objects can get bugged and end up having very erratic movement.
Level ID: 114681413

[Video](https://youtu.be/5zb-JCvD5JY)

## [2.207] [18/12/25] Particle sometimes fail to spawn when near the particle limit

The first particle in a particle loop will fail to spawn if the particle limit has been hit already.

This usually happens if $Emission \cdot Lifetime = MaxParticles$

## [2.207] [18/12/25] Spawn Particle Position Group ID is tied to game FPS

The spawn position of particles with Spawn Particle is the position of the group at the last rendered frame, instead of the current position.
This can cause particles to spawn in the wrong position when dealing with high speed or instant movement when the game runs below 240 fps.
The bug only happens while playtesting and not in the editor.

[Video: 200, 300, 60 and 120 fps](https://youtu.be/Co1UDLP2Ahk)
[Video: 120 fps vsync, mobile](https://youtu.be/wxT__dKYsr8?si=X3O1ywGwrP5fIucm)

Setup attempts to spawn a particle every tick on a moving target.
ID: 114953438

## [2.207] [18/12/25] Spawn Particle fails to spawn on inactive targets

Spawn Particle will not spawn if the target is inactive (position is off-screen).
This only happens while playtesting and not in the editor.
If the object was active on screen at least once before, the particle will spawn at its previous on-screen position.

Link Visible can keep the target active as a potential workaround to this issue.
While this might be intentional for performance reasons, there should be an option to allow the particle to spawn regardless of whether the target is active or not.

[Video](https://youtu.be/Co1UDLP2Ahk)
