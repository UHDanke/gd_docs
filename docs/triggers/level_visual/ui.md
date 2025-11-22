# UI

Marks objects part of **Group ID** as UI objects.

## Options

If **Group ID** has a Group ID Parent, all objects in the group will copy the parent's alignment. This effect is only noticeable when using the **Auto** or **Relative** settings, as the other settings apply the same alignment to all objects.

**UI Target** is used as a reference for the camera's center; it does not have to be a Camera Guide object, but there's little reason to use anything else.

**UI Target** must contain one valid target for UI to activate, if multiple objects are present then you have to define one as the Group ID Parent or else UI will not work.

### Alignments

UI objects can be made to keep their position relative to a reference point like the camera's center or edges using alignments. For example, if a **Left** alignment is used then the object will keep the same distance from the left edge of the screen on all aspect ratios.

By default, the default screen ratio (Camera Guide's green outline) is used as reference, NOT your aspect ratio (the orange guideline).

Alignments are split into XRef and YRef, only one alignment is applied at a time depending on your screen's aspect ratio. If your aspect ratio is wider than default (orange guideline appears on the sides of the camera guide) XRef is used and if its taller than default (guideline appears at the top and bottom) then YRef is used.

**Auto** makes UI objects align to the closest edge - **Left** or **Right** for XRef, **Top** or **Bottom** for YRef.

**Center** applies no alignment, the objects keep their positions relative to the center which is static for all aspect ratios.

**Left**, **Right**, **Top** and **Bottom** align objects to the respective edge.

**Relative** makes the objects position scale with the aspect ratio - if your object is 50% of the distance between the camera's center and the closest edge, it will be 50% of the distance on all aspect ratios. This option ignores all other alignments, it doesn't matter whether **Auto**, **Center** or any other alignment is used.

## Behavior

UI is an on-load trigger, it is activated once when the level loads and remains permanently active.

The UI layer is unaffected by ALL camera changes (ex: zoom, rotate, offset, etc).

UI effects do not stack and only one is applied per object, as a result only the first alignment on an object will be applied, and any further UI triggers will skip it. If the parent of a group ID has already been affected by an UI trigger, this group cannot be affected by another UI.

While UI objects render above every other layer, objects part of UI do perserve their layering (layer, Z-order, tileset, blending, etc). It is not possible to differentiate between these sub-layers when using shaders or gradients, as they reference the entire UI layer.

UI objects do not follow the camera's movement, their position is set on-load and will remain static unless affected by other triggers. When marked as UI, they are moved to the default camera position (the initial camera position when loading the level in classic mode) based on their position relative to **UI Target**, their alignment settings and your device's aspect ratio.

Object part of UI can only collide with other UI objects. Hitboxes will no longer collide with the player and UI collision objects will only be able to collide with other UI collision objects. The chunk optimization is skipped by UI collisions, so all UI collisions will check all other UI collisions, just like when using Extended Collision.