# Editor

## Using editor Preview Mode hotkey at least twice while playtest is paused resets object position permanently

**Version:** 2.208
**Date:** Sat Jan 31 2026 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
Pressing the F3 Preview Mode hotkey two times or more while editor playtesting is paused moves objects permanently. The first use resets object positions to default, the second use reverts the position back to where it was in playtesting. The second move will not be undone when playtesting is stopped.

## Regrouping objects with Group Parent IDs creates phantom groups

**Version:** 2.208
**Date:** Sat Jan 31 2026 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
Groups are remapped by Regroup and Build Helper, but Group Parent IDs are not. The object remains the Group Parent ID for the old group despite said group no longer being in the group list. This can cause issues by introducing phantom groups \- the group is technically unused and not visible in the group list of the affected object, so it'll be available for Regroup and Build Helper, but the object is still the Group Parent ID for said group, so if a trigger relies on Group Parent IDs like Area or Advanced Follow, then said object will be used as the center, causing issues.

## IDs that are not affected by Build Helper or Regroup

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
This is a list of all IDs that are not affected by Build Helper or Regroup. While i do not know which ones are on purpose, i'll highlight the ones that cause issues or look like oversights: - _**Group Parent ID**_ - Enter Channel ID - _**Control ID**_ - Material ID - Enter Channel - CH - Target Channel (Start Position) - Color ID (Color trigger, Pulse trigger) - _**Rotate Target ID (Rotate)**_ - Animation ID (Animate) - _**Animation Group ID (Animate Keyframe)**_ - _**Reference IDs (Advanced Follow, Edit Advanced Follow)**_ - _**Effect ID (Area triggers)**_ - _**Group ID (Sequence)**_ - Target Channel (Rotate Gameplay) - Channel (Song) - _**Unique ID, SFXGroup (SFX)**_ - _**Group ID, Unique ID, SFXGroup (SFX)**_ - Extra ID, Extra ID2 (Event) - _**Item ID (Counter Label)**_ - Color Channel (Area Tint, Enter Tint Effect) - Enter Channel (Legacy Enter Effect) - Enter Channel, EffectID (Enter Effect triggers, Stop Enter Effect) - _**RespawnID (Checkpoint)**_

## Cannot create new Group Parent IDs if the trigger has 10 groups already

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
Group Parent IDs cannot be applied to an object with 10 existing groups, even if the object has that group already.

## Hitbox does not update properly after rotating a slope object

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
Rotating a slope object does not update its orientation in the editor unless you move the object or quit the editor. Autobuild is affected by this.

## Incorrect trigger duration line length when teleporting

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
The length of the duration line is double what it should be if the trigger is placed in a part of the level skipped by a teleport trigger.

## On-load triggers have effect lines

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
On-load triggers like Link Visible and UI have effect lines when placed on the timeline, despite having an effect only when the level loads. These triggers do still count as if they were placed on the timeline however even if they do nothing when reached.

## Triggers that do not display their target ID

**Version:** 2.207
**Date:** Sun Feb 01 2026 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
The following triggers, mostly added in 2.2, do not display any target IDs even though they should: - Re-Target Advanced Follow - Area (Move, Scale, Rotate, Tint, Fade) - Edit Area (Move, Scale, Rotate, Tint, Fade) - Area Stop - Item Compare - Time - Time Event - Time Control - Item Edit - Item Persist - Static Camera - Event - Toggle Block - Enter Effect (Move, Scale, Rotate, Tint, Fade) - Enter Stop - Link Visible - UI The following triggers which spawn on either true or false only display one / no target ID, when they should display both true / false: - Item Compare - Instant Collision

## **Disable Paste State Groups** prevents **Paste** from pasting groups

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
![image](https://github.com/user-attachments/assets/db5a88af-c6a6-4a71-992b-38364ee565a8) **Disable Paste State Groups** affects both **Paste State** and the **Paste** button from the **Edit Groups** menu, despite being noted otherwise.

## Lighter on Base Color or an object with only Base or Detail Color crashes the game

**Version:** 2.208
**Date:** Sat Jan 31 2026 00:00:00 GMT+0200 (Eastern European Standard Time)
**Level ID:** 132526309

### Description
Using the Lighter option on the Base Color of an object or on an object with only Base or Detail Color will either crash the game when the object becomes visible or kick you out of the level on load. This bug does not occur inside the editor.

## Paste + Color does not remap Pulse's Channel ID

**Version:** 2.207
**Date:** Thu Dec 18 2025 00:00:00 GMT+0200 (Eastern European Standard Time)

### Description
The Channel ID of a Pulse trigger cannot be remapped to a new value using Paste + Color.
