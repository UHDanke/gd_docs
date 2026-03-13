# Event

Spawns a **Group ID** when at least one of the selected **Event IDs** is activated.

## Options

**Extra ID** makes the events require a specific Material ID to activate. If left as 0 the trigger will activate only if the event's Material ID is also 0. 

**Extra ID 2** makes the events require a specific player to trigger the event. If left as 0 the trigger will activate regardless for any Player ID.

The following table lists all events and whether they use **Extra ID** (Material) or **Extra ID 2** (Player):

| ID 	| Event 				 | Material | Player |
| :---: | :--------------------: | :--------: | :------: |
| 1  	| Tiny Landing 			 | Yes 		| Yes 	 |
| 2  	| Feather Landing 		 | Yes 		| Yes 	 |
| 3  	| Soft Landing 			 | Yes 		| Yes 	 |
| 4  	| Normal Landing 		 | Yes 		| Yes 	 |
| 5  	| Hard Landing 			 | Yes 		| Yes 	 |
| 6  	| Hit Head 				 |     		| Yes 	 |
| 7  	| Orb Touched 			 |     		|     	 |
| 8  	| Orb Activated 		 |     		| Yes 	 |
| 9  	| Pad Activated 		 |     		|     	 |
| 10 	| Gravity Inverted		 |     		| Yes 	 |
| 11 	| Gravity Restored 		 |     		| Yes 	 |
| 12 	| Normal Jump 			 |     		| Yes 	 |
| 13 	| Robot Boost Start 	 |     		| Yes 	 |
| 14 	| Robot Boost End 		 |     		| Yes 	 |
| 15 	| UFO Jump				 |     		| Yes 	 |
| 16 	| Ship Boost Start 		 |     		| Yes 	 |
| 17 	| Ship Boost End 		 |     		| Yes 	 |
| 18 	| Spider Teleport 		 |     		| Yes 	 |
| 19 	| Ball Switch 			 |     		| Yes 	 |
| 20 	| Swing Switch			 |     		| Yes 	 |
| 21 	| Wave Push 			 |     		| Yes 	 |
| 22 	| Wave Release 			 |     		| Yes 	 |
| 23 	| Dash Start 			 |     		| Yes 	 |
| 24 	| Dash Stop 			 |     		| Yes 	 |
| 25 	| Teleported 			 |     		|  	     |
| 26 	| Portal: Normal 		 |     		|  	     |
| 27 	| Portal: Ship 			 |     		|  	     |
| 28 	| Portal: Ball 			 |     		|  	     |
| 29 	| Portal: UFO 			 |     		|  	     |
| 30 	| Portal: Wave 			 |     		|  	     |
| 31 	| Portal: Robot 		 |     		|  	     |
| 32 	| Portal: Spider 		 |     		|  	     |
| 33 	| Portal: Swing 		 |     		|  	     |
| 34 	| Yellow Orb 			 |     		| Yes    |
| 35 	| Pink Orb 				 |     		| Yes    |
| 36 	| Red Orb 				 |     		| Yes    |
| 37 	| Gravity Orb 			 |     		| Yes    |
| 38 	| Green Orb 			 |     		| Yes    |
| 39 	| Drop Orb 				 |     		| Yes    |
| 40 	| Custom Orb 			 |     		| Yes    |
| 41 	| Dash Orb 				 |     		| Yes    |
| 42 	| Gravity Dash Orb 		 |     		| Yes    |
| 43 	| Spider Orb 			 |     		| Yes    |
| 44 	| Teleport Orb 			 |     		| Yes    |
| 45 	| Yellow Pad 			 |     		|  	     |
| 46 	| Pink Pad 				 |     		|  	     |
| 47 	| Red Pad 				 |     		|  	     |
| 48 	| Gravity Pad 			 |     		|  	     |
| 49 	| Spider Pad 			 |     		|  	     |
| 50 	| Portal: Gravity Flip 	 |     		|  	     |
| 51 	| Portal: Gravity Normal |     		|  	     |
| 52 	| Portal: Gravity Invert |     		|  	     |
| 53 	| Portal: Flip 			 |     		|  	     |
| 54 	| Portal: Unflip	 	 |     		|  	     |
| 55 	| Portal: Normal Scale 	 |     		|  	     |
| 56 	| Portal: Mini Scale 	 |     		|  	     |
| 57 	| Portal: Dual On 		 |     		|  	     |
| 58 	| Portal: Dual Off 		 |     		|  	     |
| 59 	| Portal: Teleport 		 |     		|  	     |
| 60 	| Checkpoint 			 |     		|  	     |
| 61 	| Destroy Block 		 |     		|  	     |
| 62 	| User Coin 			 |     		|  	     |
| 63 	| Pickup Item 			 |     		|  	     |
| 64 	| Checkpoint Respawn 	 |     		|  	     |
| 65 	| Fall Low 				 | Yes 		| Yes    |
| 66 	| Fall Med 				 | Yes 		| Yes    |
| 67 	| Fall High 			 | Yes 		| Yes    |
| 68 	| Fall VHigh 			 | Yes 		| Yes    |
| 69 	| Jump Push 			 |     		| Yes    |
| 70 	| Jump Release 			 |     		| Yes    |
| 71 	| Left Push 			 |     		| Yes    |
| 72 	| Left Release 			 |     		| Yes    |
| 73 	| Right Push 			 |     		| Yes    |
| 74 	| Right Release 		 |     		| Yes    |
| 75 	| Player Reversed 		 |     		| 	 	 |
| 76 	| Fall Speed Low 		 |     		| Yes    |
| 77 	| Fall Speed Med 		 |     		| Yes    |
| 78 	| Fall Speed High 		 |     		| Yes    |

## Event Requirements

The following events have specific thresholds to activate:
- **Tiny Landing** - player landing speed below -1 but above or equal to -4 after dropping down a block 
- **Feather Landing** - player landing speed below -1 but above or equal to -4 after jumping
- **Soft Landing** - player landing speed below -4 but above or equal to -8
- **Normal Landing** - player landing speed below -8 but above or equal to -14
- **Hard Landing** -	player landing speed strictly below -14
- **Fall Low** - fall distance higher than 11.75 and lower or equal to 154 units
- **Fall Med** - fall distance higher than 154 and lower or equal to 304 units
- **Fall High** - fall distance higher than 154 and lower or equal to 454 units
- **Fall VHigh** - fall distance higher than 454 units
- **Fall Speed Low** - player fall speed below -2 but above or equal to -7
- **Fall Speed Med** - player fall speed below -7 but above or equal to -14
- **Fall Speed High** - player fall speed strictly below -14
- **Player Reversed** - not implemented (checked in decomp)

Certain events are mutually exclusive, only one from a set of mutually exclusive event IDs will be activated at once (ex: gamemode portals, landing speed, fall distance, fall speed, etc).

Jump / Left / Right Push / Release events will not activate for players with disabled controls.

On mobile, if a direction input is held while the opposite direction input is already left (Right then Left or Left then Right), the opposite direction's event will not trigger when it's released.

## Spawn Mechanics

Events are checked in order of Event ID, active event triggers are grouped by Event ID and will spawn in the order they were activated in. If an Event trigger with multiple Event IDs has already spawned it will not spawn again in the same tick. 

**Group ID**, **Extra ID** and **Extra ID 2** can all be remapped.
