# Edit Animation Settings

Allows editing the playback settings of animated objects, accessible from the Edit Special button.

## Options

**Randomize Start** is assigned by default on some animated objects but doesn't seem to remove or add any randomness to animation frames, playback speed, or loop delay.

**Use Speed** multiplies the animation's playback by the **Speed** option and removes the random speed on selected objects if **Speed** is not 0. Negative **Speed** values will play back the animation in reverse.

**Animate on Trigger** makes the animation play from the start when activated by an Animate trigger, the animation plays once and does not loop. Animated objects start invisible if on-screen but will be visible if loaded later, they will turn invisible once the animation ends. Inactive objects (toggled off or offscreen) are ignored if **Only if Active** is selected.

**Disable Delayed Loop** removes the random delay some animations have between loops.

**Disable AnimShine** removes the glow texture from special animated objects. This property is removed by the game if used on objects this option has no effect on.

**Offset Anim** makes the animation start from **Single Frame** if enabled, otherwise the animation will be frozen in-place at the start frame. Objects animated by **Animate on Trigger** ignore **Offset Anim** and **Single Frame**.
