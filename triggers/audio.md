# FMOD
Geometry Dash uses the FMOD library as its primary audio engine, in-depth documentation for it can be found on https://www.fmod.com/docs/.

This documentation is referenced or summarized partialy in this document as a rough guideline, please reference the FMOD docs instead if you need more in-depth information.

<br>

# Game Audio Settings

Specific audio settings are found in the Options section of the Settings menu, under the Audio Category.

## Change Custom Songs Location

Saves custom songs in the ``Geometry Dash\Resources\songs`` folder instead of ``AppData\Local\GeometryDash``.

## Disable Song Alert

Removes the alert when playing a level with missing song files.

## No Song Limit

Removes the 50 song limit from the song folder. If unselected, the oldest 50th song is replaced when downloading a new song over the limit.

## Reduce Quality

Reduces the audio sample rate from 44.1 kHz to 24 kHz.

## Audio Fix 01

Increases the audio buffer size. Only use this if the audio frequently cuts while playing. Makes latency worse as a side-effect.

## Music Offset

Offsets all song playback by a value given in milliseconds.

## Debug

Displays FMOD debug stats, such as memory usage and latency.

<br>

# Pitch & Speed

FMOD uses the FFT (Fast Fourier Transform) algorithm for pitch shifting (Pitch) and time stretching (Speed). More info can be found [here](https://www.fmod.com/docs/2.03/api/effects-reference.html#fft).

Speed modifies the audio's playback speed, Pitch changes the audio's pitch without affecting its speed.
 
Pitch is measured in semi-tones, an increase by 12 semitones is an octave which is equal to a doubling (200%) of pitch, while a decrease by 12 semitones is equal to a halving (50%) of pitch.

Pitch changes are limited between -12 (50%) and 12 (200%) by the audio engine.

The exact pitch multiplier can be calculated using the formula:  
$Multiplier = \sqrt[12]{2^{Pitch}}$

Speed uses the same formula and value scaling as Pitch in order to make pitch corrections easier. Pitch of speeded audio can be corrected by giving Pitch the opposite value of Speed.

The audio engine runs separately from the main game loop and is not affected by Timewarp triggers.

<br>

# Volume Proximity

The volume of songs and SFX can be set to depend on the distance between a group of sound emitters referenced by Group ID 1 and a sound listener given by Group ID 2 or chosen between P1, P2 and Camera. This is also known as Volume Attenuation.

It can be set or modified by Edit Song, SFX or Edit SFX.

## Behavior

### Persistence

Attenuation set by Edit Song is saved per **Channel**, and by Edit SFX per **SFX Group**.

SFX triggers can set attenuation unique to the SFX. This has priority over the one set on SFX Group and cannot be edited in any way. 

### Clearing & Overriding

Attenuation remains permanently active on the song Channel or SFX Group until overriden.

Attenuation can be removed if either **GID 1** has no objects, **GID 2** is equal to 0 or does not have one object. Otherwise the current attenuation settings are overriden. If **GID 1** is equal to 0 attenuation will not be cleared nor overriden.

### Timing

Modifying the attenuation of a Song or SFX with Edit Song / Edit SFX is instant regardless of Duration.

### Emitters

If GID 1 is made up of multiple objects, then the one closest to the listener is used to determine the volume.

### Listeners

If GID 2 has more than one object, then the attenuation settings are overriden.

P1, P2 and Camera (center) override GID 2 as the listener. 

Both P1 and P2 can be selected at the same time, and this is the only way to have more than one listener per attenuation at once. In this case the closest distance between a sound emitter and one of the two players is used.

### Thresholds

The attenuated volume is calculated from the distance between listener and emitters, interpolated linearly based on three thresholds: Near, Medium and Far.

For the bounds, if Distance is less than Near then **VolNear** is used, if it's more than Far then **VolFar** is used.

Each threshold adds to the previous one, as follows:  
$Near = MinDist$  
$Medium = MinDist+Dist2$  
$Far = MinDist+Dist2+Dist3$  

All thresholds are in move units (10/block). 

If the trigger is selected, the game renders the attenuation thresholds around each emitter.

#### Distance

How distance is calculated depends on the chosen direction settings, similar to the ones found in Area triggers.

| Image | No. | Shape  | Distance |
| :---: | :---: | :---: | :---: |
| <img src="https://github.com/user-attachments/assets/8d30a8f5-7813-49c6-b008-bee239b53811" width="50%"> | 1 | Circular | $\sqrt{(Y_{l}-Y_{e})^{2}+(X_{l}-X_{e})^{2}}$ |
| <img src="https://github.com/user-attachments/assets/24f5af6d-f09b-476f-80bf-90269069104f" width="50%"> | 2 | Horizontal | $\|X_{l}-X_{e}\|$ |
| <img src="https://github.com/user-attachments/assets/2611fd55-70df-41c8-b805-255950875928" width="50%"> | 3 | Horizontal | $X_{e}-X_{l}$ |
| <img src="https://github.com/user-attachments/assets/3148644d-6f9a-4bc6-92b1-e3fb5a816ab0" width="50%"> | 4 | Horizontal | $X_{l}-X_{e}$ |
| <img src="https://github.com/user-attachments/assets/ba9d01d7-066d-414f-bd5f-62c89ac6ec94" width="50%"> | 7 | Vertical | $\|Y_{l}-Y_{e}\|$ |
| <img src="https://github.com/user-attachments/assets/d861d58b-622a-4bcf-b4c5-3fab9074c526" width="50%"> | 10 | Vertical | $Y_{l}-Y_{e}$ |
| <img src="https://github.com/user-attachments/assets/78826a65-62d5-446c-b355-6325dca8a8e3" width="50%"> | 9 | Vertical | $Y_{e}-Y_{l}$ |

<br>

# Primary Song

The default song used when playing the level, which can be changed from the level select menu. This will be displayed as the main song in any level select screen.

It is always played on **Channel** 0 and is loaded on level start.

## Song Selection

### Normal Songs

In the Normal category you can find all of the official, main-level songs for use in your custom levels.

It is not possible to use main level songs inside Song triggers (they can only be used as primary songs), but non-cut versions of some of them can be found on Newgrounds.

<details>
<summary>[2.207] All primary songs </summary>

1. Stereo Madness
2. Back On Track
3. Polargeist
4. Dry Out
5. Base After Base
6. Cant Let Go
7. Jumper
8. Time Machine
9. Cycles
10. xStep
11. Clutterfunk
12. Theory of Everything
13. Electroman Adventures
14. Clubstep
15. Electrodynamix
16. Hexagon Force
17. Blast Processing
18. Theory of Everything 2
19. Geometrical Dominator
20. Deadlocked
21. Fingerdash
22. Dash
23. Explorers (Hidden)
</details>

### Custom Songs
Custom songs can be chosen from two main sources - Newgrounds and the Audio Library.

Newgrounds is a media-hosting website for user-generated content. While possible to use your own music in-game, you first need to be scouted in order to appear in the Audio Portal and then whitelisted by RobTop.

The Audio Library hosts audio licensed for use inside Geometry Dash. This can be either on a per artist or per label basis, but not all songs from an artist or label can be featured as the usage rights can be owned by a different entity or exclusive to another game.

## Settings

The primary song settings menu can be accessed from the gear button in the Custom Song Selection menu. 

While the options can only be accessed from the custom song menu, these settings also apply to main level songs.

### Offset

Offsets the start of the song by a value given in seconds. 

This is less precise than the song trigger, as you can modify the offset only up to a tenth of a second, instead of a thousandth.

Offset is ignored if using Dont Reset.

### Fade In/Out

Applies one second of fade when starting from the beginning of the level (Fade In) and / or when completing the level (Fade Out).

Fades are not applied while playtesting in the editor

### Dont Reset

Similar to the option found in the Song trigger, songs will continue when dying or resetting the level.

Unlike the Song trigger option, it does not stop on death and will not reset when restarting from the beginning of the level.

<br>

# Song Guidelines

Song guidelines are editor-only lines used as reference for syncing triggers and gameplay to the song.

They can be toggled on or off using the Music Lines option in the editor pause screen, next to the Help button.

Guidelines are only displayed vertically, so they will not show up in vertical gameplay sections.

## Guideline Creator

Song guidelines can be created for custom levels using the Guideline Creator accessed from inside the Custom Song Selection menu.

New guidelines can be added to existing ones from the Record button. Existing ones can be cleared with the Clear button.

Custom guidelines are saved per level, not per song.

## Normal Songs 

Main level songs all have beat guidelines which cannot be edited in-game.

Audio-scaled objects do not sync to the main level song, they use the guideline beats as reference.

<br>

# BPM Guide

Displays song lines synced to a beat given in **BPM** (bars per minute) multiplied by **BPB** (beats per bar) for a **Duration** given in seconds, relative to a given gameplay Speed.

## Behavior

Bars are colored yellow, beats are orange.

Unlike song guidelines, BPM guidelines are not affected by any gameplay changes.

It is not possible to orient BPM triggers in any direction other than left to right.

## Visibility

Toggling off song guidelines does not toggle off BPM guidelines.

BPM guidelines are not toggled off if the trigger is toggled off or has its alpha set to 0. 

The only ways to hide them is either with the Disable option or with the Hide object option (if Hide Invisible is ticked on).

<br>

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

<br>

# Edit Song

Modifies the Speed and Volume of a song playing on the given Channel.

## Misc

Channel can be remapped.

Edit Song cannot be stopped or paused by a Stop trigger.

New Edit Song calls override the previous **Speed** or **Volume** transition if **Change Speed** or **Change Volume** is selected.

## Options

**Stop** instantly stops the song playing on the given **Channel**. This will not clear the channel's Prep song.

**Stop Loop** makes a looping song playing on the **Channel** no longer loop. A looping song will not stop at the End timestamp and instead continue until the end of the song.

**Duration** sets the time needed to transition **Speed** or **Volume** to their new values if **Change Speed** or **Change Volume** is selected.

## Volume Proximity

**Volume Proximity ** can be set per **Channel** from the options found on the 2nd page.

These settings do not reset when the song ends and remain permanently active until overriden or cleared by another Edit Song trigger.

<br>

# SFX

Plays the selected SFX using the given **Pitch**, **Speed** and **Volume**.

## Misc

**Unique ID**, **SFX Group** and the SFX's ID can be remapped.

Playback behavior for remapped SFX IDs has a few crucial differences compared to remapped Custom Song IDs:
- The ID must be prefixed by ``s`` and of type ``.ogg``
- The ID must be found in the SFX data library
- Remappping SFX can be done once per trigger - the first activation sets what SFX will be used by the trigger until the player quits the level, further activations will play the same SFX regardless of remaps

## Options

### Reverb

Applies a reverb effect to the played SFX. Reverbs are used primarily to simulate an acoustic space (sound reflections, decay, etc).

FMOD documentation on reverbs can be found [here](https://www.fmod.com/docs/2.03/api/effects-reference.html#sfx-reverb).

Reverb parameters cannot be modified individually in-game, instead you are allowed to pick between the 21 default presets provided by FMOD.

<details>
<summary>Reverb presets</summary>

- Off
- Generic
- Padded Cell
- Room
- Bath room
- Living room
- Stone room
- Auditorium
- Concert Hall
- Cave
- Arena
- Hangar
- Stone Corridor
- Alley
- Forest
- City
- Mountains
- Quarry
- Plain
- Parking Lot
- Sewer Pipe
- Under Water
</details>


Preset parameters can be found [here](https://www.fmod.com/docs/2.03/api/core-api-system.html#fmod_reverb_presets).

There is only one reverb channel used by all sound effects, as such there can be only one reverb preset active at a time.  

If **Enable** is selected, the SFX will replace the current reverb effect with its selected preset. If it is not selected, then the SFX uses the current active reverb preset.

### FFT

**FFT** improves the quality of the pitch effect by increasing the FFT window size. Practically, this makes the sound effects less coarse with slightly more echo at the cost of performance.

### Pre-Load

Loads the SFX in memory at the start of the level.

### Loop

Makes the SFX loop until stopped.

### Start and End

Makes the SFX **Start** and **End** at a a given time in miliseconds.

If looped, playback is looped between **Start** and **End**. However, if Stop Loop is used then **End** is ignored and the SFX continues playing to the end.

### Fade In and Out

Makes the SFX **Fade In** when starting and **Fade out** when ending. 

Like **Start** and **End*, the time is given in miliseconds.

Fades are applied only when a SFX starts or ends, not when it repeats.

### Unique

Makes the SFX unique if **Unique ID** is not 0 and **Is Unique** is selected.  
Unique SFX can be referenced by their **Unique ID** by Edit SFX triggers.

Only one SFX per unique ID can be played at a time.  
Without **Override**, the new SFX will not play if the previous SFX is still playing.  
With **Override**, the previous SFX gets replaced by the new one.

### SFX Group

Gives the SFX a **SFX Group** that can be referenced by Edit SFX triggers.

### MinInterval

Adds a cooldown to the SFX trigger and, if the SFX is unique, to the **Unique ID**. SFX will not play if activated during the cooldown.

In the case of unique SFX, the **MinInterval** of the current trigger is considered. If **Override** is selected then only the **MinInterval** cooldown is still applied.

**MinInterval** is not affected by SFX **Speed**, but is affected by timewarping.

### Ignore Volume Test

By default, the SFX will not play if it's starting volume 0.  
If **Ignore Volume Test** is selected, the SFX will play regardless of it's starting volume. 

### Volume Proximity

**Volume Proximity** can be set per SFX trigger from the 4th settings page.  
This overrides the **SFX Group**'s proximity settings and cannot be edited by other triggers.

<br>

# Edit SFX

Modifies or stops the SFX by either Group ID, SFX Group or Unique ID.

## Misc

**Group ID**, **SFX Group** and **Unique ID** can be remapped.

Edit SFX cannot be stopped or paused by a Stop trigger.

New Edit SFX calls override the previous **Speed** or **Volume** transition if **Change Speed** or **Change Volume** is selected.

The SFX's **Pitch** cannot be edited.

## Options

**Stop**, **Stop Loop**, **Change Speed** and **Change Volume** affect all SFX with the given **Group ID**, **SFX Group** or **Unique ID**.

**Stop** instantly stops all referenced SFX .

**Stop Loop** makes all referenced SFX stop looping. Looping SFX will not stop at the End timestamp and instead continue until they end.

**Duration** sets the time needed to transition **Speed** or **Volume** to their new values if **Change Speed** or **Change Volume** is selected.

**Volume Proximity** can be set per SFX Group from the 2nd settings page. These settings do not reset when the SFX ends and remain permanently active until overriden or cleared by another Edit SFX trigger.
