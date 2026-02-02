# Spawn Particle

Spawns particles from particle objects in **Particle Group** at a target's position in **Position Group**.

Spawn Particle only works on particle objects, it cannot spawn the particles of other objects like pads or portals.

## Options

**Offset X** / **Y** offset the particle's spawn position by a set amount on the X / Y axis. **OffVar X** / **Y** further offset the spawn position randomly in a +/- range. All offsets are given in units (1/30 block).

**Rotation** offsets the rotation of spawned particles.

**Scale** multiplies the scale of spawned particle.

**Match Rot** adds the target object's rotation to the spawned particles.

**Rotation** and **Scale** can be randomized using the respective **+-** option.

## Group ID Parents

Group ID Parents change how **Particle Group** and **Position Group** work when they contain multiple objects.

If **Particle Group** has no GID Parent particles spawn individually at the target's position, using their own center for scale and rotation. If a GID Parent is present it becomes the center of the group - particles spawn relative to it, scale and rotation apply on the whole group.

For **Position Group** the GID Parent enforces an object as the target, without it the target is picked at random from all objects in the group.

Group Parents, Area Parents and object links have no effect on spawned particles.

## Differences from object particles

Infinite **Duration** is set to 0.00, if **Emission** is not infinite then no particles will spawn.

Spawned particle emitters do not respawn, therefore **Respawn** is ignored.

Particle emitters created by Spawn Particle are not tied to any object and cannot be repositioned after spawning, therefore **Relative** has the exact same behavior as **Grouped**. Additionally, **Free** and **Relative** emitters can be rotated or scaled which will also rotate and scale all movement, including **Free**'s camera movement.

Particle emitters created by Spawn Particle ignore most of the properties of the parent object except:
- rotation
- scale (X and Y, but not warp skew)
- position (if **Particle Group** has an ID Parent)
- Z order & layer
- if either **Use Obj Color** or **Uniform Obj Color** are used - the object's current base & detail colors (after all color changes, except Area Tint), but not alpha value (from color channel or triggers) or blending.

Particle colors do not update dynamically with **Uniform Obj Color**,
 the behavior for Spawn Particle is identical to **Use Obj Color**.

Alpha and blending behavior of emitters created by Spawn Particle is consistent between all combinations of **Additive**, **Use Obj Color** and **Uniform Obj Color**:
- base object opacity is ignored
- **Start_A** is not ignored when **Use Obj Color** is selected
- Particles will not fade between solid / blending

## Frame behavior

Spawn Particle uses the target's last active position, updated every frame (not tick) - this has two detrimental effects:
- If the target moves very fast (or instantly) and the game runs at a framerate lower than 240Hz, particles can spawn "earlier" than they should
- If the target becomes inactive by moving off screen, the particle will spawn on screen instead of at the target's current position

The second issue can be worked around by using a Link Visible trigger and keeping one object on screen at all times.
