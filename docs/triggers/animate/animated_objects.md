# Animated Objects

Monsters and animated ground spikes do not have an animation menu and cannot have these properties applied to them through save file editing.

Checkpoint objects have their elements move overtime, but this does not count as an animation and like monsters they are not affected by animation settings.

The coin and user coin collectible objects can be edited, but the menu is overriden by the Edit Pickup Settings menu and it is only accessible if you also select an animated object.

Scale circles do not have animation frames and instead scale and fade overtime. **Use Speed** is force selected by the game and frame options like **Single Frame** and **Offset Anim** have no effect.

Similarly, some gameplay elements (orbs) and decorations scale in sync with the music. They do not count as animated objects and thus are not affected by animation settings.

The lava bubble objects ignore all animation settings except **Animate on Trigger** and **Only if Active**. Additionally, one of them is randomized between 3 possible animations on level load.

The laser wall object has some of its frames randomized regardless of any settings used.

Objects animated using scale, rotate, move or fade effects animate smoothly every frame. Monster animation transitions are also done smoothly. Most other animated objects are made up of multiple sequential frames with a set frame delay between each frame.

Properties by object can be found in the following table:
<!-- @csv: .data/tables/animate.csv -->
<!-- @end -->
