# Song Trigger

Starts a specific custom song with a given **Volume** and **Speed** in the selected **Channel**.

## Channels

Only one song can be played in a channel at a time. Audio will not cut when a song is replaced, as the track is replaced only when the new track finishes loading.

There are in total 5 playback channels, between ID 0 and 4.

Channel ID can be remapped.

## Custom Song ID

Up to 21 unique Song IDs can be used per level, levels with more IDs will fail to upload unless whitelisted by RobTop.

Surprisingly, Custom Song ID can be remapped. Custom Song ID will not remap if activated when loading the level, and it uses ID 0 if no custom song is selected.

Remapped Song IDs are not displayed in the level's Songs & SFX list and do not count towards the level's song ID limit.

Custom Song ID can be remapped to any integer ID. Any .mp3 file in your songs folder with said ID as its name will be played, including negative IDs which are normally unused - this makes this feature ideal for NONGS.

## Prep

Songs need to be loaded into memory first before playing, this can take a variable amount of time depending on your system performance and file sizes which can result in playback being noticeably delayed. Prep and Prep Load can be used to load the song early and play it when needed without delay.

Prep loads the track into the channel's memory without playing it, only one Prep can be active per channel, new activations replace previous ones. Playing a new track without Prep removes any active Preps for that channel. The track loaded by Prep will not stop or interrupt the channel's current playback.

If Prep Load is activated while the Prep track is still loading, the track will play as soon as it is fully loaded. Prep Load does nothing if activated with no Prep track, or after a non-Prep song activation.

Preps are not cleared upon level restart, preps from a previous attempt can be played in the current one if the level was not restarted from a checkpoint or from the end screen, otherwise the prep only stops the current track without playing a new one.