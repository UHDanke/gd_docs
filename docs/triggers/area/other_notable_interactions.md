# Other Notable Interactions

### Stop

Stop works on Area triggers.
Paused Area triggers do not apply their effect.

Stop does not work on Edit Area.
Stopping the Area trigger will undo and stop all active Area and Edit Area effects.
Pausing the Area trigger itself pauses all of its active Edit Area effects.

### Toggle

Toggle disables Area effects on targets only in certain cases, (for example - **Length** is negative and using a Center ⟹ Edge proximity), otherwise has no effect.

### Follow

Follow does not copy Area movements.

### Gradient

Gradients are not affected by Area Tint.

Gradient Rotation is not affected by Area Rotate outside of the editor.

### Enter

Area triggers are not affected by movements caused by Enter triggers.

### Particle Objects

Particle effects are affected by Area triggers.

### Spawn Particle

Particles created using Spawn Particle ignore Area effects on the particle object.

### Advanced Follow

Advanced Follow works on objects and supports object links.
Area effects happen after Advanced Follow movements.
Advanced Follow targeting is affected by Area effects. Due to this, certain interactions can create loops or crash / freeze the game.
Using DEAP with Advanced Follow is recommended.

### Rotate

Aim and Follow modes use the object's virtual rotation instead of the real rotation, so using Area Rotate to offset these rotations will not work as they will constantly try to override the rotation made by Area Rotate.

### Scale

Relative Scale and Relative Rotation use the object's virtual scale or rotation as reference.