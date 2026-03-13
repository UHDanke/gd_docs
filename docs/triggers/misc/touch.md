# Touch

Toggles and spawns a **Group ID** on and off when the player clicks.

## Behavior

Touch always spawns the target group after toggling on.

Multiple touch press / release events are individual and do not accumulate, touch will activate for every press or release separately.

Touch activates only on player jump clicks, it doesn't react to plaftormer move inputs.

Unlike other input options Touch will activate even if the player(s) have disabled controls.

## Options

By default, toggles a group on and off alternatively for every press. If **Toggle On** or **Toggle Off** are selected the trigger will exclusively toggle the group on, respectively off on press.

If **Hold Mode** is selected touch will toggle off the group on press and toggle back on release. If **Toggle On** is selected it will instead toggle the group on when holding and off on release. **Toggle Off** does not change hold behavior.

Activates on any player click by default, this can be limited to one of the player's inputs by using the **P1** or **P2 Only** options.

Disables player 2's controls when active if **Dual Mode** is selected. If multiple **Dual Mode** touch triggers are active controls are unblocked only when they are all stopped or paused. This block is similar to the options trigger's Disable Player Controls options in that it prevents all inputs except touch, but it counts as a separate block from the options one.