# Stop

Stops, pauses or resumes a set of triggers given by Group or Control ID.

## Valid Targets
<details>
<summary>Triggers affected by Stop</summary>

- Color
- Move (if not silent)
- Pulse
- Alpha
- Spawn (if delayed)
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
</details>

### Exceptions

<details>
<summary>Triggers not affected by Stop</summary>

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
</details>

### Alternative Stops

Some of the active triggers, including ones not affected by Stop, have alternative stopping or pausing mechanisms.

#### Edit Area

Edit Area effects are done by the Area trigger, pausing or stopping the Edit Area requires respawning, stopping or pausing the target Area trigger.

#### Time

Can start paused, or be paused using a Time Control trigger.

This pause is different from the one done by Pause - it will not resume a Pause trigger and it cannot be resumed by Stop.

#### Static Camera

The follow cannot be stopped, but the target can be returned back to default by using the **Exit Static** option.

#### Camera Edge

Locked edges can be reset using ID 0 and with the **Unlock** button.

#### Song

Can be stopped by Channel ID with an Edit Song trigger.

#### SFX

Can be stopped by Unique, SFX Group or Group ID with an Edit SFX trigger.

#### Gradient

Can be stopped by using the **Disable** option. 

All active gradients can be cleared with the **Disable All** option. 

#### Shader Triggers

All shaders effects can be disabled using the Shader trigger's **Disable All** option. 

Chroma Glitch shader can be disabled using the trigger's **Disable** option.

#### Enter Triggers

Enter effects can be cleared using their Enter Channel or Effect ID from the Enter Stop trigger.

#### Item Persist

While not an active trigger, the item or timer's persistent flag can be reset using the **Reset** option, which also clears the value or **Reset All**, which affects all persistent items and timers.

## Stop Effect

The effect of a Stop, Pause or Resume trigger on other triggers varies, but can be split into three main categories:
<details>
<summary>Effect is paused or stops applying</summary>

- Color
- Move
- Alpha
- Rotate
- Scale
- Follow
- Keyframe Animation
- Follow Player Y
- Advanced Follow
- Zoom Camera
- Offset Camera
- Rotate Camera
</details>

<details>
<summary>Effect gets cleared or is undone</summary>

- Pulse
- Area Triggers
- Time (settings reset)
- SFX
- Gradient
</details>

<details>
<summary>Activation is prevented</summary>

- Spawn
- Touch
- Count
- Time
- Time Event
- Event
- Collision
- On Death
</details>

### Notes

#### Color

The last stopped Color trigger on the channel before a checkpoint gets resumed when respawning.

#### Keyframe Animation

Spawning in the same tick cannot be prevented with Stop.

#### Spawn

Stopping a Spawn trigger with delay from inside another Spawn trigger with delay causes the last scheduled Spawn delay to be checked twice in the same tick. If this delay activates, the first activation uses the Spawn's remaps, while the second uses no remaps.

If a Spawn Ordered trigger is stopped, it will stop spawning triggers. If its the last one, it will continue spawning without remaps from the stop point.

Paused Spawn delays are ignored and will not tick down until resuming.	

Delays can be resumed (or paused) and activate (or not activate) in the same tick as long as they haven't been checked yet.
