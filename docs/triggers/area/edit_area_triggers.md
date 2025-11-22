# Edit Area Triggers

Edits the parameters of an active Area Trigger.

## Area Options

Common

- **Duration**
- **Easing**
- **GroupID**
- **EffectID**
- **Use EffectID**
- **Offset**
- **OffsetY**
- **ModFront**
- **ModBack (BK)**
- **Deadzone**

Area Move

- **MoveDist**
- **MoveAngle**
- **RFade**
- **XY Mode**
- **MoveX**
- **MoveY**

Area Rotate

- **Rotation**

Area Scale

- **ScaleX**
- **ScaleY**

Area Fade

- **(To) Opacity**

Area Tint

- **Tint %**
- **Edit HSV**
- **Use HSV**

## Behavior

Settings are independent of each other. The values of different settings can be changed by different triggers independently of one another with their own **Duration** and **Easing**.
Settings with value *NaN* are not affected.
Spawning an Area trigger again will stop and undo active Edit Area effects.

### Multiple Instances

There can be only one Edit Area effect active for each setting of an Area trigger.
New effects override previous ones. When overriding, the new Edit Area effect will start from where the previous effect stopped.
When calling multiple Edit Area triggers that edit the same settings, the last one will override all previous ones.
Edit Area will override other active Edit Areas only if **Duration** is bigger than 0\. This is likely a bug.

### Settings

**EffectID** and **GroupID** can both be remapped.
**EffectID** 0 will edit all Area triggers without an **EffectID**.
**Duration** is the time it takes to transition between the old and new set of values, this is affected by the **Easing** option.
**Easing** does not change the Area trigger's easings.
**XY Mode** only changes which settings are displayed, an Edit Area Move trigger can affect both Angle and XY Mode Area triggers at the same time.
**Tint %** and **Set HSV** can be edited at the same time by one Edit Area Tint trigger.
There is no option to change the **From Opacity** setting of an Area Fade trigger.