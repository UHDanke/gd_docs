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

**Volume Proximity** can be set per **Channel** from the options found on the 2nd page.

These settings do not reset when the song ends and remain permanently active until overriden or cleared by another Edit Song trigger.