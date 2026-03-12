# Target Behavior

Triggers can target multiple objects within a Group ID but when only one object is required there are two ways this can be resolved if no unique target exists:
1. one object is picked at random
2. the group is considered null (0)

Most targets use the null behavior, some triggers will not activate if certain targets are null but this doesn't extend to all triggers.

Triggers that have random targets include Move (all), Rotate (all), Teleport (applies to all teleports), Advanced Follow (reference groups only) and Edit Advanced Follow (same as Adv Follow).

Group ID Parents can be used to enforce an unique target or center for the group which always has priority. The only triggers / objects this does not apply on is Teleport.