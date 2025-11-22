# Advanced Follow

## Advanced Follow Ignore Timewarp

Add **Ignore Timewarp** option to Advanced Follow. When used this would ensure high speed movement isn't affected while slowing down time.

## Edit AdvFollow Mod X and Mod Y reference ID

Add a reference ID besides Mod X and Mod Y, to allow the speed to be modified on the X or Y axis of a reference object. This would allow for accurate bounce physics off slopes or angled lines which is currently very difficult to do.

## Speed Multiplier

If speed not being a multiplier is intentional, a **Speed Multiplier** option should be added to allow for that behavior.
While it takes an extra workaround, this would allow the implementation of accurate collision motions between solid physics objects.
Additionally, any kind of movement could be converted to advanced follow speed values with this feature.

## Edit AdvFollow Use Dir
Add **Use Dir** option so the object's current direction is used for direction calculations.
With Speed this would allow adding speed in the direction of movement without using an individual reference ID for each target.
If Redirect Dir worked, you could use Dir to offset the direction of movement by a set amount of degrees.