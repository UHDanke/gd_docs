### Criteria for bugs

The way i classify a certain behavior as a bug is entirely subjective, but there are two main criterias i follow:

1. Does it seem intentional?  
2. Is it detrimental and would it be more useful if it was fixed?

If i don't classify something as a bug, it is either because i find the feature useful, i consider the behavior a non-issue or it's just how it works.  
Crashes are always bugs without question.

### Last checked version

For record keeping, each bug will have the last verified version prefixed to the title (ex: \[2.207\] Crash bug).  
I will only update the version number if i encounter the bug again or retest it for a new version.

## Bug Lists

* [Area](?tab=t.0#heading=h.x7xvu6574osi)

## Misc Bugs

### \[2.207\] Enter trigger crash

If you try to call 2 different Enter triggers with the same Enter Channel and Effect IDs but different values for the same variables, the game will crash in playtesting.

### \[2.206\] Overwriting a spawn remap of ID 2 crashes the game

If you spawn remap group ID 2 to any ID, then call another spawn which remaps group ID 2 to any other non-zero ID, then call a trigger which uses group ID 2, the game will instantly crash when calling the first spawn.  
Only ID 2 is affected,  
Only Steam and Android exhibit this bug. Mac and IOS are not affected.

### \[2.207\] Regrouping objects with Group Parent IDs creates phantom groups

Groups are remapped by Regroup and Build Helper, but Group Parent IDs are not.  
The object remains the Group Parent ID for the old group despite said group no longer being in the group list.  
This can cause issues by introducing phantom groups \- the group is technically unused and not visible in the group list of the affected object, so it'll be available for Regroup and Build Helper, but the object is still the Group Parent ID for said group, so if a trigger relies on Group Parent IDs like Area or Advanced Follow, then said object will be used as the center, causing issues.

### \[2.206\] Cannot create new Group Parent IDs if the trigger has 10 groups already

Group Parent IDs cannot be applied to an object with 10 existing groups, even if the object has that group already.
