# Edit Animation Settings

Allows editing the playback settings of animated objects, accessible from the Edit Special button.

## Options

**Randomize Start** is assigned by default on some animated objects, but currently does nothing.

**Use Speed** multiplies the animation's playback by the **Speed** option and removes the random start offset on selected objects if **Speed** is not 0. Negative **Speed** values can also be used.

**Animate on Trigger** makes the animation play from the start when activated by an Animate trigger, the animation plays once and does not loop. Animated objects start invisible if on-screen but will be visible if loaded later, they will turn invisible once the animation ends. Inactive objects (toggled off or offscreen) are ignored if **Only if Active** is selected.

**Disable Delayed Loop** removes the random delay some animations have between loops.

**Disable AnimShine** removes the white texture from a few animated objects. This property is removed by the game if used on objects this option has no effect on.

**Single Frame** makes the animation freeze on the selected frame. **Offset Anim** offsets the animation by the frame amount set in **Single Frame** instead. Objects animated by **Animate on Trigger** will not be offset.
