# Gravity

Changes the player's gravity multiplier.

The game only allows multipliers between 0.10 and 2.00, and between -2.00 and -0.10. Negative gravity accelerates away from the ground.

Gravity only affects the gravity acceleration of the player, it does not affect the player's max fall speed.

By default, it affects all active players. 

If **P1** or **P2** is selected, Gravity affects only the respective player. 

If **PT** is selected, only the player that touches the trigger changes gravity (**Touch Trigger** must also be selected, otherwise it does nothing).

If P1 enters a dual portal, P2 will not copy P1's gravity and use default (1.00) gravity.
