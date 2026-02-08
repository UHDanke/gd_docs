# End

Completes the level when activated.

## Options

**Spawn ID** is spawned on activation, the spawn is instant and works just like a regular spawn trigger.

**Target Pos** can be used to set an object as the level's end position. **Target Pos** must be an unique target (single object or GID Parent) otherwise it is ignored. If no valid target exists, the end trigger itself is used as the target.

**No Effects** disables the effects that play on level completion.

**Instant** skips the player's slow pull animation.

**No SFX** disables the level complete SFX.

## Notes

This trigger does not work inside the editor.

The end wall is absent in platformer mode so an End trigger is required to verify platformers.

If **No effects**, **Instant** and **No SFX** are all enabled, the level complete screen will pull down with no delay.

**Spawn ID** and  **Target Pos** can both be remapped. Triggers from **Spawn ID** inherit the end trigger's remaps.

If multiple end triggers are activated, only the first one will work and subsequent activations are ignored. The only exception are end triggers activated instantly by **Spawn ID**, you can chain as many end trigger activations as you want this way.
