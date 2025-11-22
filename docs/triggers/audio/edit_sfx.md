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