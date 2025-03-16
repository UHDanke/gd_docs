# Color Assignment

Objects can be assigned a color using the Edit Object menu.

Color channels as well as HSV and layering settings can be modified per object.

## Color Layers

Objects have at least one of Base (primary) or Detail (secondary) color layers.

For objects with a single color layer, you can select whether its treated as a Base or Detail color using the options (gear) sub-menu.

## Channel Selection

A color channel for Base or Detail can be selected using this menu. The channels available are, in placement order:
* Player Color 1
* Player Color 2
* Light BG
* Default
* 1-9
* Last selected channel ID

All color channels can be viewed using the Browse option.

The Next Free option selects the lowest unused color channel.	
Unused color channels have default values, are not used by any object or referenced by any Color or Pulse triggers. 

The channel ID select box can be used to select a specific ID, including ones higher than ID 999.
 
Objects can use any color channel between 1 and 1101. Other elements such as BG (Background) and G (Ground) cannot be reassigned to another channel.

ID 0 is replaced by the Default channel.

## HSV Selectors

The object's colors can be offset from the color channel using the Hue, Saturation and Brightness (Value) sliders or by modifying the value directly.

Saturation and Brightness are multiplicative, but can be made additive using the corresponding check box.

Current HSV settings can be cleared using the trash button.



# Color Channels

Color channels store color (RGBA) values used to recolor objects and other level elements.

The color of a channel can be modified permanently by Color triggers and temporarily by Pulse triggers.

Valid channels are:
* Custom (1-999)
* BG (1000)
* G1 (1001)
* L \ Line (1002)
* 3DL (1003)
* Obj (1004)
* P1 (1005)
* P2 (1006)
* LBG (1007)
* NA (1008)
* G2 (1009)
* Black (1010)
* White (1011)
* Lighter (1012)
* MG (1013)
* MG2 (1014)
* NA (1015-1101)

IDs above 1101 can be assigned, but they are the same as 1101.

### Special Channels

#### Background (BG)
- Used by the level background.
- The background layer does not blend or use opacity.

#### Ground (G1)
- Used by the level ground.
- The ground layer does not blend or use opacity.

#### Line (L)
- Used by the ground line.

#### 3D Outline (3DL)
- Used by 3D outline objects.

#### Object (Obj)
- Used as the primary color of most collidable objects.

#### Player Color 1 (P1)
- Copies the player's main color.
- Black player colors are replaced by white.
- Blends additively.

#### Player Color 2 (P2)
- Copies the player's secondary color.
- Black player colors are replaced by white.
- Blends additively.

#### Light Background (LBG)
- Color depends on the Background's brightness:
	- If the BG's value (brightness) is more than 0.20, it copies the BG channel with +0.20 value.
	- If the BG's value is 0.00, it copies the P1 channel.
	- If the value is between 0.00 and 0.20, the resulting color is between the other two.
- Black player colors are replaced by white.
- Blends additively.

#### Ground Secondary (G2)
- Used as the secondary color for some ground options.
- The ground layer does not blend or use opacity.

#### Black
- Used by default by certain objects, like ground spikes.
- Has hex value #000000 and cannot be modified normally.

#### White
- Used by default by certain objects.
- Has hex value #FFFFFF and cannot be modified normally.

#### Lighter
- Used by default by certain objects.
- Cannot be modified normally.
- Copies the object's Base color channel (including HSV) with +0.15 value.
- WILL crash the game or kick you out of the level if used as the base color channel of an object.

#### Middle Ground (MG)
- Used as the primary color of the middle ground.
- Unlike the ground and background layers, middle ground DOES use blending and opacity.

#### Middle Ground Secondary (MG2)
- Used as the secondary color of the middle ground.
- Unlike the ground and background layers, middle ground DOES use blending and opacity.



# Select Color Menu

The color of a channel can be initialized in the level settings using the Select Color menu.

HSV values can be assigned in three ways:
- Individual RGB values
- Hex code
- Hue ring and Saturation-Value wheel

**Opacity** can only be modified with a slider.

The **Blending** option makes objects and Middle Ground blend additively with other layers.

**Player Color 1** and **Player Color 2** copy the player's colors.

## Copy Color

Color channels can copy the colors of other channels using this option.

### Behavior

Copy Color effects are not instant and count as active color changes.

As color effects are done by frame, only on the next render frame will the color be copied.

**Legacy HSV** doesn't seem to do anything at the moment and its intended behavior is undocumented.

### Channel Options

Channels that can be copied include:
* 1-999
* BG (1000)
* G1 (1001)
* G2 (1009)
* L / Line (1002)
* Obj (1004)
* 3DL (1003)
* MG (1013)
* MG2 (1014)

P1 and P2 used to be copy color options prior to 2.2 alongside the separate **Player Color 1** and **2** options, but are no longer assignable in-game.

**Player Color 1** and **2** are ignored if Copy Color is present.

Custom color channels (1-999) cannot copy themselves, but special channels (BG, G, etc) can. You need a secondary custom color in order to make them copy themselves.

### Other Properties

Blending is not copied.

Opacity is not copied unless Copy Opacity is selected.

Color changes done by Pulse triggers are not copied.

# Color Sliders

The initial RGBA values of a color channel and the HSV values of a selected object, Color trigger or Pulse trigger can be modified using sliders from the Color / HSV overlay.

This overlay pops up when clicking the HSV / Colors button found below Copy Values.

For the color sliders, the current color and the initial color are previewed next to each other.

The overlay does not get hidden during playtesting, which allows you to change values while playing the level in the editor.

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



# Other Color and Layering Options

## Color Filter

Found in the Delete menu, this option limits selection and deletion to objects that have the given color channel.

Valid channels are between 1-1101.

The following special channel can be selected using the menu:
* Obj
* Lighter
* 3DL
* P1
* P2

## Copy Values

Copies the following properties of an object:
* Color Channels
* HSV values
* Editor layers
* Z settings (Order and Layer)
* Groups
* Extra

These properties are not copied:
* Base / Detail
* Group ID Parents
* Extra2
* ORD
* CH

Properties can also be copied using the **Copy** button in the **Edit Group** menu. This feature is functionally identical to **Copy Values**.

Copied properties are not stored when exiting the editor, unlike copied objects.

### Paste State

Pastes the group properties of an object onto another object.

Groups will not be pasted if the **Disable Paste State Groups** editor option is selected. 

State can also be pasted using the **Paste** button in the **Edit Group** menu. This will also paste the copied color settings.

**Disable Paste State Groups** does prevent the **Paste** button from pasting groups, despite being noted otherwise.

### Paste Values

Pastes the color properties of an object onto another object

Color values can also be pasted using the **Paste** button in the **Edit Group** menu. This will also paste the copied object settings.

