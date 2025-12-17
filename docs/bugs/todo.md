# WIP Bugs

## [2.207] [TODO] Advanced Follow reversed spawn order

Advanced follow processing order for triggers with the same Priority is reversed on mobile.

## [2.207] [REDO] Area Memory Leak, Stop and Area Stop do not properly clear Area triggers

Area triggers are not properly cleared by Stop or Area Stop triggers and accumulate lag overtime.
The culprit seems to be the processAreaActions function but the details are not known.

The only way to properly clear an Area trigger is by replacing it with another Area trigger by using an EffectID.

Known affected levels are 3Depth and Dead of Night, both implement the EffectID workaround to fix the issue.
