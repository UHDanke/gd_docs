# Camera Mode

Removes borders for certain gamemodes when **Free Mode** is selected and changes how the camera behaves when the player moves up or down if **Edit Camera Settings** is used.

These settings can also be set when switching gamemode using a portal, they have the exact same behavior as the trigger version.

Gamemodes without borders like Cube and Robot are not affected by Camera Mode, not even by the camera settings.

Padding determines the Y offset, this can be calculated by the formula $OffsetY = 130-128 \cdot Padding$

Gameplay borders snapping to the Y axis grid can be disabled with **Disable Gridsnap**.