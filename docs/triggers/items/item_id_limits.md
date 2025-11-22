# Item ID Limits

## Items
Items are limited between ID 0 and 9999.

While some triggers can be assigned items outside the usual range, these items refer to either ID 0 or 9999.
ItemIDs below 0 are reserved for items like Main Time, Points and Attempts.

## Timers
Timers are not limited and can be assigned both positive IDs higher than 9999 and negative IDs lower than 0.
The only triggers able to use negative timers are Time, Time Event, Time Control and Item Persist.
Item Edit and Item Compare are not able to be used to assign or extract values from these timers, it is not possible to use these timers as a way to store numerical values. It is possible however to store remaps, which can be accessed by Time Event.