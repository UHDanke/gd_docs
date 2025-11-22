# Rendering Order

There are 6 main factors that determine the layering order of level elements, from most to least important:
- UI
- Z Layer
- Tileset
- Blending
- Z Order
- Placement Order

Less important factors determine the rendering order only if previous ones are identical.

## UI

UI objects are rendered on top of every other layer.

UI is counted as a single layer by triggers such as Gradient.

UI objects will be ordered by Z layer settings, within the UI Layer.

## Z Layer

B5 to B1 and T1 to T4 layers can be assigned to objects.

Other layers are, from lowest to highest:
* BG (Background)
* MG (Middle Ground)
* B5
* B4
* B3
* B2
* B1
* P (Player)
* T1
* T2
* T3
* T4
* G (Ground)
* UI
* Max (Top-most layer, same as UI)

Certain objects (like gameplay portals) are made up of multiple objects with different Z settings, which cannot be changed using Z settings. Both top and bottom sides ignore Z Layers and use Placement Order, while only the bottom side uses Z Order.

## Tileset

Due to how the game renders textures, the order in which each tileset is processed in matters for the rendering order.

The tileset number can be found next to the Z Layer text. Tilesets with lower values (0 is lowest) are rendered on top, while those with higher values are rendered below.

## Blending

Objects with Blending are placed below non-blending objects.

## Z Order

Objects with a higher Z Order are rendered on top of those with lower Z Order.

## Placement Order

Objects placed last are rendered on top of those placed before.