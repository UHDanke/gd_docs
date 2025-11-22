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