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

Reverb presets

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