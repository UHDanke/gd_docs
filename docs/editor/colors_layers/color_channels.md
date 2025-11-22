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
	- If the value is between 0.00 and 0.20, the resulting color fades between the other two.
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