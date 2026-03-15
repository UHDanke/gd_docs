# Animated Objects

Monsters and animated ground spikes do not have an animation menu and cannot have these properties applied to them through save file editing.

Checkpoint objects have their elements move overtime, but this does not count as an animation and like monsters they are not affected by animation settings.

The coin and user coin collectible objects can be edited, but the menu is overriden by the Edit Pickup Settings menu and it is only accessible if you also select an animated object.

Scale circles do not have animation frames and instead scale and fade overtime. **Use Speed** is force selected by the game and frame options like **Single Frame** and **Offset Anim** have no effect.

Similarly, some gameplay elements (orbs) and decorations scale in sync with the music. They do not count as animated objects and thus are not affected by animation settings.

The lava bubble objects ignore all animation settings except **Animate on Trigger** and **Only if Active**. Additionally, one of them is randomized between 3 possible animations on level load.

The laser wall object has some of its frames randomized regardless of any settings used.

Objects animated using scale, rotate, move or fade effects animate smoothly every frame. Monster animation transitions are also done smoothly. Most other animated objects are made up of multiple sequential frames with a set frame delay between each frame.

Properties by object can be found in the following table:
<!-- @csv: data/tables/animate.csv -->
| **Object ID** | **Not Editable** | **Disable AnimShine** | **Smooth Animation** | **Randomize Start** | **Random Speed** | **Random Frames** | **Random Animations** | **Delayed Loop** | **Frame Delay** |
| :-----------: | :--------------: | :-------------------: | :------------------: | :-----------------: | :--------------: | :---------------: | :-------------------: | :--------------: | :-------------: |
|      918      |       Yes        |                       |                      |                     |                  |                   |                       |                  |   0.025 - 0.05  |
|      919      |       Yes        |                       |                      |                     |                  |                   |                       |                  |                 |
|      920      |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      921      |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.08      |
|      923      |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      924      |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      1050     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      1051     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      1052     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      1053     |                  |                       |                      |                     |                  |                   |                       |                  |      0.045      |
|      1054     |                  |                       |                      |                     |                  |                   |                       |                  |       0.06      |
|      1327     |       Yes        |                       |                      |                     |                  |                   |                       |                  |       0.06      |
|      1328     |       Yes        |                       |                      |                     |                  |                   |                       |                  |       0.06      |
|      1329     |                  |                       |                      |                     |                  |                   |                       |                  |      0.115      |
|      1516     |                  |                       |                      |         Yes         |                  |                   |                       |                  |       0.05      |
|      1518     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      1519     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      1583     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      1584     |       Yes        |                       |                      |                     |                  |                   |                       |                  |    0.06 - 0.1   |
|      1591     |                  |                       |                      |                     |                  |                   |          Yes          |                  |   0.12 - 0.13   |
|      1592     |                  |                       |                      |                     |                  |                   |                       |                  |      0.045      |
|      1593     |                  |                       |                      |                     |                  |                   |                       |                  |       0.13      |
|      1614     |                  |                       |                      |                     |                  |                   |                       |                  |       0.12      |
|      1618     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      1697     |                  |                       |                      |         Yes         |                  |        Yes        |                       |                  |       0.06      |
|      1698     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      1699     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      1839     |                  |                       |         Yes          |                     |                  |                   |                       |                  |                 |
|      1840     |                  |                       |         Yes          |                     |                  |                   |                       |                  |                 |
|      1841     |                  |                       |         Yes          |                     |                  |                   |                       |                  |                 |
|      1842     |                  |                       |         Yes          |                     |                  |                   |                       |                  |                 |
|      1849     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      1850     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      1851     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.07      |
|      1852     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.07      |
|      1853     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      1854     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.07      |
|      1855     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      1856     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.07      |
|      1857     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      1858     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      1860     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      1936     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      1937     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      1938     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      1939     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.07      |
|      2012     |       Yes        |                       |                      |                     |                  |                   |                       |                  |   0.04 - 0.06   |
|      2020     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2021     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2022     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2023     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2024     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2025     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2026     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2027     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2028     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2029     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2030     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2031     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2032     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2033     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2034     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
|      2035     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2036     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2037     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2038     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2039     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2040     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2041     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2042     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2043     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2044     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2045     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2046     |                  |          Yes          |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2047     |                  |          Yes          |                      |         Yes         |       Yes        |                   |                       |                  |       0.04      |
|      2048     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2049     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2050     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2051     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2052     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2053     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2054     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2055     |                  |          Yes          |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2223     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      2246     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      2605     |                  |                       |                      |                     |                  |                   |                       |                  |       0.1       |
|      2629     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      2630     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.1       |
|      2694     |                  |                       |                      |                     |                  |                   |                       |                  |       0.16      |
|      2864     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2865     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2867     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      2868     |                  |                       |                      |                     |       Yes        |                   |                       |                  |       0.06      |
|      2869     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2870     |                  |                       |                      |                     |       Yes        |                   |                       |                  |       0.05      |
|      2871     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2872     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2873     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2874     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2875     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2876     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2877     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      2878     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      2879     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2880     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2881     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2882     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2883     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2884     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2885     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2886     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.05      |
|      2887     |                  |                       |                      |         Yes         |       Yes        |                   |                       |                  |       0.06      |
|      2888     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2889     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.06      |
|      2890     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2891     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      2892     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |      0.025      |
|      2893     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |      0.0333     |
|      2894     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.05      |
|      3001     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      3002     |                  |                       |                      |                     |                  |                   |                       |                  |       0.05      |
|      3119     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.16      |
|      3120     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.16      |
|      3121     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.16      |
|      3219     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.16      |
|      3303     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3304     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3482     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3483     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3484     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3492     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      3493     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.12      |
|      4211     |                  |                       |                      |                     |                  |                   |                       |                  |       0.12      |
|      4300     |                  |                       |                      |         Yes         |       Yes        |                   |                       |       Yes        |       0.08      |
<!-- @end -->

## Frame Delays of Monsters

Big (918):
- 0: 0.0250
- 1: 0.0250
- 2: 0.0250
- 3: 0.0500

Big Spiked (1327):
- 0: 0.0600

Small Spiked (1328):
- 0: 0.0600

Bat (1584):
- 0: 0.0600
- 1: 0.0600
- 2: 0.0600
- 3: 0.0600
- 4: 0.0600
- 5: 0.0600
- 6: 0.0600
- 7: 0.1000
- 8: 0.0600
- 9: 0.0500

Spikeball (2012):
- 0: 0.0600
- 1: 0.0600
- 2: 0.0450
- 3: 0.0600
- 4: 0.0600
- 5: 0.0400
- 6: 0.0400
- 7: 0.0600
- 8: 0.0500
