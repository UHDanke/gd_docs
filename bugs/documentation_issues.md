# Editor Issues
## [Page 64, 65] Target Mode and Distance Mode
![image](https://github.com/user-attachments/assets/cac9de43-9551-4466-b3c2-03a56ee5894a)
![image](https://github.com/user-attachments/assets/8f69b2fe-074c-4c39-92cc-992bf7cced94)

None of the groups mentioned must contain a single object, if there are multiple objects one is picked at random for the movement. If there is a Group Parent ID it will always be used.


## [Page 66] Pausing
![image](https://github.com/user-attachments/assets/bbbf6929-b28c-431f-8e1c-a8ad8a52a0d8)

Worth mentioning not every trigger can be paused - in that case, resume does nothing and pause stops the trigger.

## [Page 70] Remapping

Things i think that need to be mentioned or added:
- Most triggers and ids can be remapped
- An example where Spawn triggers are remapped

## [Page 72] Aim and Follow Mode
![image](https://github.com/user-attachments/assets/63f04efa-b068-44d6-938d-0cd6dc998f8a)

Second page settings have no effect on follow, they are only used by aim mode to bound the position of the aim target.  
Additionally, none of the groups mentioned must contain a single object, if there are multiple objects one is picked at random for the movement unless there is a Group Parent ID.

![image](https://github.com/user-attachments/assets/8a7a126d-2753-4ba4-a50b-10de3acf9e6c)

This page should have an "Aim Boundaries" title / text to better indicate what they do.

## [Page 73] Relative Rotation
![image](https://github.com/user-attachments/assets/7d9f88c6-ae7f-4339-bea4-9e2cacb4b663)

Relative Rotation uses the center object's X/Y axis instead of the level's axis.

## [Page 73] Relative Scale
![image](https://github.com/user-attachments/assets/a3dddc09-79d7-4946-9a56-facac0659c0c)

Worth mentioning that if center object is same as the object being scaled, you can make the scaling be additive to current scale factor.
For example, with a scale of 2 on an object scaled by 3, relative will scale the object by 1.333 to a scale of 4 (or +1 from current scale).

## [Page 76] Speed

![image](https://github.com/user-attachments/assets/da0a0c29-1119-4d92-bca1-b467bba75110)

Advanced Follow Y has the same behavior as an Advanced Follow Mode 1 trigger, Speed in this case is the inverse of the easing of the movement.  
To get the equivalent easing value, use this formula:  
$Easing = 4/Speed$

## [Page 77] Max Speed

![image](https://github.com/user-attachments/assets/677a58fb-a506-41c8-821a-03ef9472f990)

Not sure where this formula is from, as with Speed, Max Speed is almost equivalent to Advanced Follow's MaxSpeed, where:
$Max Speed(AdvFollow) = MaxSpeed/4$

## [Page 89] Reverse Order

![image](https://github.com/user-attachments/assets/5bb5a16f-8e88-4fe6-bfec-6da0d59c33a8)

Reverse order doesn't invert the settings of the keyframe, it reverses the order the keyframes are processed in.

## [Page 91] ModFront / ModBack

![image](https://github.com/user-attachments/assets/b1a6c887-31f0-4604-b7b2-c0d6532176e4)

ModBack and ModFront are distance multipliers.	
ModBack is applied if the object is to the left / below of the center and ModFront is applied if the object is to the right / above the center.

## [Page 91,92] Easing

![image](https://github.com/user-attachments/assets/d84ab90a-2833-4999-8825-dd0fbcce4662)
![image](https://github.com/user-attachments/assets/b08ab3bb-4451-43b9-9bec-dd973447b45d)

"Start of movement" is not a thing for Area triggers. What Easing and Easing2 refer to instead is with Ease Out enabled, Easing is applied when ModBack is used and Easing2 is applied with ModFront.

## [Page 92] Priority

![image](https://github.com/user-attachments/assets/1055c883-2fe7-479b-868e-8b52064a8e91)

This is true only for Area Fade. For the rest, Priority sets the order in which they are applied (from highest first to lowest last)

## [Page 97] MoveAngle

![image](https://github.com/user-attachments/assets/6f6fbd41-d4e9-4252-87e2-6db2f6b8ca55)

MoveAngle is counter-clockwise instead of clockwise, 0 is down and 180 is up instead.

## [Page 97] Relative

![image](https://github.com/user-attachments/assets/6e0de744-8791-4d87-8844-d9ab5f678319)

With Relative objects move away from the center.

## [Page 97] RFade

![image](https://github.com/user-attachments/assets/352b2ed1-479c-4709-9c25-37650e4408fe)

I somewhat understand what this refers to but the explanation is lacking.	
With RFade, if the distance of the object is less than RFade (in small step units), MoveDist decreases linearly from 1 to 0 (when in the center).

## [Page 112] Sequence Unique Remap

The explanation is completely missing.	
Unique Remap makes the sequence trigger have a separate counter for each set of remaps.	
Worth mentioning that this behavior is per set of remaps, if two sets contain the same remaps they will still have separate counters.

## [Page 114] Reset

![image](https://github.com/user-attachments/assets/1db1bb3d-bc63-4dbb-b84e-5025cafb8d8e)

Also resets the electroman adventures destroyable blocks.

## [Page 119] Loop & Dont Reset

Both options aren't explained under the Song trigger section.  
Dont Reset is a recent option, but Loop isn't.

## [Page 124] FFT

![image](https://github.com/user-attachments/assets/31a05066-38b2-4640-9926-e5df2eb6f38e)

This is one of the options i'm not able to tell what is actually supposed to do.  
I notice some differences in how the sounds are pitched, but i cannot tell if this is placebo or actually real.  
My assumption is that this option changes the pitch shift algorithm to one that uses FFT, but i honestly have no idea, so i think it's a good sign that more info is needed / the option needs to be explained better.

## [Page 129] UI Settings

![image](https://github.com/user-attachments/assets/1f7d9871-edb7-4d03-b251-6a2e98b765ef)

This explanation is a complete mess.  
Auto aligns objects to the nearest screen edge. Left, Right, Top, Bottom aligns objects to the respective edge. Center has no alignment.  
What alignment means in this case is the object is moved by the distance between the green (minimal) edge## and the orange (your screen) edge.

## Camera Guide
![image](https://github.com/user-attachments/assets/6d6a213f-ace3-43f7-87c8-830b6547bfd4)

Guaranteed view is 480 by 320 units or 3:2, not 4:3.

## [Page 130] Visibility Link

![image](https://github.com/user-attachments/assets/aae6b943-009f-4a66-9cad-187f6098445c)

Worth mentioning that toggled off objects will not count as on-screen for visibility links.

## [Page 130] Collision Player

![image](https://github.com/user-attachments/assets/834c8391-2731-4045-b3f4-76f1ffd7d0ef)

Worth to add that you do not need the other collision to be dynamic if you are using P1 or P2.

## [Page 138] Teleport Target

![image](https://github.com/user-attachments/assets/114ee390-879d-404b-97cb-c83a16cb4ee5)

Can be more than one object, it picks one at random.
