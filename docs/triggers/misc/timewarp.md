# Timewarp

Changes the speed the game runs at using **TimeMod**.

## Notes

**TimeMod** is limited between 0.10 (10 times slower) and 2.00 (2 times faster) with 1.00 being the default.

At base speed the game simulates 240 ticks per second. Slowing down the game keeps the same effective TPS, but reduces the rate at which the game clock advances while speeding up increases the game's effective TPS up to 480 at 2.00 mod.

Time triggers have an **Ignore Timewarp** option that does not work.

The Main Time counter is not affected by timewarp.

Audio is not affected by timewarp.

Advanced Follow works with ticks and not time values, if the game is slown down then all movements done by Advanced Follow are reduced proportionally, this isn't consistent across different timewarp values which results.