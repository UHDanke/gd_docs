# Pitch & Speed

FMOD uses the FFT (Fast Fourier Transform) algorithm for pitch shifting (Pitch) and time stretching (Speed). More info can be found [here](https://www.fmod.com/docs/2.03/api/effects-reference.html#fft).

Speed modifies the audio's playback speed, Pitch changes the audio's pitch without affecting its speed.

Pitch is measured in semi-tones, an increase by 12 semitones is an octave which is equal to a doubling (200%) of pitch, while a decrease by 12 semitones is equal to a halving (50%) of pitch.

Pitch changes are limited between -12 (50%) and 12 (200%) by the audio engine.

The exact pitch multiplier can be calculated using the formula:
$Multiplier = \sqrt[12]{2^{Pitch}}$

Speed uses the same formula and value scaling as Pitch in order to make pitch corrections easier. Pitch of speeded audio can be corrected by giving Pitch the opposite value of Speed.

The audio engine runs separately from the main game loop and is not affected by Timewarp triggers.