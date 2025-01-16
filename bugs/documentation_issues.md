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
