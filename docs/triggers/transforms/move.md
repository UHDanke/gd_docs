# Move

Moves a group of objects from **Target Group ID** over a duration given by **Move Time** with an **Easing**.

## Options

**Small Step** increases the resolution of the movement values **Move X**/**Y** and **Distance** from 10 steps per block to 30 steps per. Toggling this option resets the current move values. This is only a visual change in the trigger's menu, moves are internally saved in units with decimal points. All triggers use and save distances in 30 units per block internally even if the display is in 10 units per, there is no visual distinction or official documentation on which one is used by an option and some triggers like Advanced Follow have a mix of both.

Normally, when a move trigger is activated, the actual movement is scheduled and executed after the trigger is activated, even if its duration is 0. **Silent** makes the movement apply instantly upon activation. For example, if you spawn multiple silent moves at once each movement is applied when the trigger is spawned, in order - without silent all movement is done after the object is spawned. **Silent** ignores **Move Time**.

Move triggers have 3 movement modes, X/Y is the default mode and the other two are enabled by selecting **Target Mode** or **Direction Mode**.

### XY Mode

Moves the group on the X/Y axis by **Move X**/**Move Y**.

The movement can be locked separately on each axis to the player or camera, which makes the group copy their movement. If multiple move locks are present on the same axis for the same group they stack additively. Selecting a move lock replaces **Move X**/**Y** with **Mod X**/**Y**.

**Lock X/Y Player** makes the group copy player 1's movement on the X/Y axis, while **Lock X/Y Camera** makes the group copy the camera's movement on the respective axis.

If the current attempt count is greater than 1, a move trigger placed before the start line with **Lock X Camera** enabled will move the group back by half the width of the screen, minus two blocks ($move_X = 60 - \frac{screen\_width}{2}$). This is done regardless of where the camera currently is or whether Static Camera is used. Since this depends on the screen width which varies between devices, using this should be avoided If the alignment of the group to the camera matters.

###  Target Mode

Moves the group to the position of an object given by **TargetPos Group ID** or towards a player with **P1**/ **P2**.
**Center Group ID** is used to define an object as the center of the group. If the center is undefined then **Target Group ID** is used as the center instead.

If there are multiple center / target objects, one will be picked at random. If the group contains a GID parent, it will always be picked as the center / target.

The target's position is calculated only when the move is activated. **Dynamic Mode** makes the move recalculate the target's position after every move step. This has no effect on a move with duration 0 as a side-effect of the calculation happening after the move. Due to a bug objects moved using **Dynamic Mode** activated before a checkpoint may reset when restarting from that checkpoint.

### Direction Mode

Moves the group towards the position of a target by a set **Distance**. 

**Direction Mode** otherwise has the same interactions as **Target Mode**.

## Behavior

Move triggers, like Scale and Rotate triggers, start their movement on their second movement step, not the first. This results in a delay of 1 to 2 ticks from the moment of activation to the start of the movement depending on whether you activated the trigger before or after movements are processed.

### Move Optimization

If an object has no collision and is not referenced by certain options inside other triggers with movement / transform effects then Move will update its position only when a new frame is rendered and not every tick.

If the object is ever referenced by the following trigger options, even if indirectly through remaps, it will lose optimization:
- Follow (Follow Group ID)
- Rotate (Target Group ID, Center Group ID, Rot Target ID)
- Area (Center Group ID)
- Move (Center Group ID, Target Pos Group ID)
- Advanced Follow (Follow GID)

If the option references only one object (Follow GID for example), only the target object loses its optimization.

If the move trigger is stopped midway through its duration and between render frames, in order to avoid optimized objects remaining offset from unoptimized ones after the move ends, the next time moves are executed all optimized objects will move by the amount they were behind, based off the elapsed tick time of the last rendered frame.

If the Move trigger is paused there is no resync and optimized objects will be offset from the rest of the group, this is corrected when movement is resumed. Because paused Move triggers are skipped, if the Move trigger is stopped while paused then the offset will not be corrected and is now permanent.

