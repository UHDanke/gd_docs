# FMOD
Geometry Dash uses the FMOD library as its primary audio engine, in-depth documentation for it can be found on 
https://www.fmod.com/docs/.

This documentation is referenced or summarized partialy in this document as a rough guideline, please reference the FMOD docs instead if you need more in-depth information.

## Game Audio Settings

Specific audio settings are found in the Options section of the Settings menu, under the Audio Category.

### Reduce Quality

Reduces the audio sample rate from 44.1 kHz to 24 kHz.

### Audio Fix 01

Increases the audio buffer size. Only use this if the audio frequently cuts while playing.

Makes latency worse as a side-effect.

### Music Offset

Offsets all song playback by a value given in milliseconds.

### Debug

Displays FMOD debug stats, such as memory usage and latency.

<br>

# Primary Song

The default song used when playing the level, which can be changed from the level select menu. This will be displayed as the main song in any level select screen.

It is always played on song channel 0 and is pre-loaded together with the level.

## Song Selection

### Normal Songs

In the Normal category you can find all of the official, main-level songs for use in your custom levels.

It is not possible to use main level songs inside Song triggers, they can only be used as primary songs.

A list of all current songs (v2.207) in order:
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

### Custom Songs
Custom songs can be chosen from two main sources - Newgrounds and the Audio Library.

Newgrounds is a media-hosting website for user-generated content. While possible to use your own music in-game, you first need to be scouted in order to appear in the Audio Portal AND then whitelisted by RobTop.

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

# Song

<br>

# Edit Song

<br>

# SFX

<br>

# Edit SFX


