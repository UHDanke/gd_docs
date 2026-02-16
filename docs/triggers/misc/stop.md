# Stop

Stops, pauses or resumes a set of triggers given by **Target ID**.

## Options

The behavior the trigger can be changed using the **Stop**, **Pause** and **Resume** selectors. Each option also changes the name and texture of the trigger inside the editor.

If **Use Control ID** is selected, the stop trigger will target all triggers that share a Control ID instead of a Group ID. Control IDs can be used to target a single instance of a trigger, since Group IDs cannot be remapped while Control IDs can.

**Target ID** can be remapped.

## Stop Targets

Triggers affected by Stop:
- Color
- Move (if not silent)
- Pulse
- Alpha
- Spawn (if not instant)
- Rotate
- Scale
- Follow
- Keyframe Animation
- Follow Player Y
- Advanced Follow
- Area Triggers
- Touch
- Count
- Time
- Time Event
- Zoom Camera
- Offset Camera
- Rotate Camera
- SFX
- Event
- Collision
- On Death
- Gradient

Triggers not affected by Stop:
- Shake
- Edit Area Triggers
- Spawn Particle
- Static Camera
- Gameplay Offset
- Camera Edge
- Song
- Edit Song
- Edit SFX
- UI
- Link Visible
- Shader Triggers
- Enter Triggers

## Stop Effect

The effect of stop depends on the targeted trigger.

For most triggers that implement an animation, stopping / pausing freezes the animation midway without undoing its effects. If a trigger's effect is temporary, stopping will undo its effect completely. Pausing temporary effects may freeze an animation in place or cancel the effect temporarily.

Triggers that track some kind of parameter such as an object's movement or position will have their tracking frozen if stopped or paused.

For most triggers with scheduled spawns, stopping will prevent the spawn's activation while paused triggers are skipped from their activation checks. Stopping a trigger during a spawn check (only possible with triggers that can spawn groups) tends to result in unexpected behavior (other triggers getting skipped or checked multiple times). 

Notes:
- Color: Only the animation's fade stops, copy colors remain active unless overrided by another trigger.
- Pulse: Effect is temporary, pausing freezes the pulse's animation.
- Spawn: Delay is also paused.
- Keyframe Animation: Stopping takes up to a tick to register and is only done after the next keyframe movement is executed; pausing is instant and can can freeze the animation before it can stop.
- Advanced Follow: Stopping is scheduled for the next movement step, this can prevent advanced follow from reactivating in some cases.
- Area Triggers: Pausing cancels the area effect temporarily.
- Count: Pausing prevents the count's internal item value from updating, which can cause it to desync from the target item's value.
- Time: Stopping resets all of the timer's settings and values, including remaps; the timer will not tick while paused.
- SFX: Cannot be resumed, pause behaves identical to stop.
- Gradient: Stop behaves like pause, so a gradient can be resumed after stop is used; pausing cancels the gradient temporarily.

## Alternative Stops

Some of the active triggers, including ones not affected by Stop, have alternative stopping or pausing mechanisms:
- Edit Area: Animates an Area trigger, pausing or stopping the Edit Area requires respawning, stopping or pausing the target Area trigger.
- Time: Can start paused, or be paused using a Time Control trigger. This pause is different from the one done by Stop as it will not resume a Pause trigger and it cannot be resumed by Stop.
- Static Camera: The follow cannot be stopped, but the target can be returned back to default by using the **Exit Static** option.
- Camera Edge: Locked edges can be reset using ID 0 and with the **Unlock** button.
- Song: Can be stopped by Channel ID with an Edit Song trigger.
- SFX: Can be stopped by Unique, SFX Group or Group ID with an Edit SFX trigger.
- Gradient: Can be stopped by using the **Disable** option. All active gradients can be cleared with the **Disable All** option.
- Shader Triggers: Most shaders effects can be disabled using the Shader trigger's **Disable All** option. Chroma Glitch shader can be disabled using the trigger's own **Disable** option.
- Enter Triggers: Enter effects can be cleared using their Enter Channel or Effect ID from the Enter Stop trigger.
- Item Persist: Clears target timers if **Reset** is selected.
