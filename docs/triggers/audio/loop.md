# Loop

Makes the song continue looping instead of ending.

Playing a new song or using Stop Loop are the only ways to stop the loop.

## Dont Reset

With Dont Reset, the track will not be reset and continue playing from the previous attempt when respawning from a checkpoint.

The track will pause on death and resume on respawn if the Options trigger's Audio On Death option is Off (default).

## Start and End

Makes the song Start and End at a a given time in miliseconds.

If looped, playback is looped between Start and End. However, if Stop Loop is used then End is ignored and the song continues playing past the end point.

### Milisecond Offsets

The Pause buttons next to Start and End can be used to get the milisecond offset of the song trigger's position from the start of the level.

In classic mode, all gameplay changes which affect the Music Playback line are taken into account for the offset calculation.

In platformer, all gameplay changes are ignored, including the level's default speed. The level is considered as having normal speed for the offset calculation.

## Fade In and Out

Makes the song Fade In when starting and Fade out when ending.

Like Start and End, the time is given in miliseconds.

Fade In is applied only when a loop starts, not when it repeats.