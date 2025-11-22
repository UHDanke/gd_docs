# Count Desynchronization

Extending on two desynchronization bugs mentioned in the Count trigger documentation, i'll attach my test results in this file and explain a bit in how i managed to find this.

So i initially started with the misled assumption that Count has some sort of intentional, controllable "skipping" behavior that can be used to optimize Count activations by resetting the item value back to 0. And that Pause / Resume can now be used (since 2.206 i believe, it wasn't mentioned anywhere) to prevent a Count from activating and skip over values without having to stop the trigger.

The first clue that something was wrong with how i thought Count worked came from a finding by jrodo on the way Count interacts with Pause and Resume triggers. If you pause a count trigger, use a pickup to skip the count's target count, then resume the count trigger, at a first glance it seems like you've succesfully skipped past the Target Count and prevented the trigger from spawning, and this would be a good alternative for Toggle when using remaps as you cannot toggle Control IDs.
Except, if you use a Pickup trigger after resuming which doesn't cross the Target Count value, Count still activates. From further testing i've concluded that Count triggers actually store the last value of the Item ID, and everytime they activate this value gets updated. The bug in this case is that pausing stops the Count trigger from updating the item value, and once you resume the item value and the internal count value differ.

This prompted me to go back to a bug i've encountered early august, where that "skipping" behavior i thought existed seemingly broke out of nowhere. In order to figure out the reason i've created a setup able to record the activation order of Count triggers, which took about 3 days of testing.

With this i was able to map out the behavior of Count:
Count activates every time the value of the Item ID changes, even if the value remains the same.
When activating, the Count instances get ordered in a list based on their Target Count and spawn order. The game copies the item value at the time of activation and then goes through this list, checks whether the instances should spawn and updates the stored value to the copied item value.
Whether the index of the list is taken from the beginning or the end of the list depends on the last item change - If the item value decreased, then the index is taken from the end of the list. If the item value is updated during the activation of Count, then this order  can be changed despite the Count activation being unfinished.
If there is a new item change inside a Count, then the game goes through all respective Count instances before continuing with the previous Count activation.

There are two issues with this behavior:
* If you interrupt Count with another Count using the same item id, then the stored value will get updated to the new value, when continuing with the previous count the stored value gets updated to an old value, this causes the internal value to desync from the item value.
* If the first item increases the value and the second one decreases it, then the game processes the count list in descending order after the second item change. However, when continuing the first item change, the game will use descending order instead of ascending order, and because some count triggers have already been processed the list will start with an offset from the end of the list; This is the reason why some Count instances can be skipped.

Below i've added the setup used and the recorded data, as well as some suggestions i have to this.

## The Setup
There are 11 unique Count instances active, each with different Target Count values.
These instances are first activated by a Pickup of 1000 from an initial value of 0. On the instance with Target Count 2 there is an additional Item Edit trigger which changes the item value from 1000 to another, lower value.
To display the exact order, Pickup and Sequence triggers are used to record what instance activated and in what order, where the digit value represents the trigger's Target Count for values 4 to 8 (ex: value 4 represents Target Count 4). Values 1,2, and 3 all share the same Target Count of 1.

This is how the setup looks like:
![image](https://github.com/user-attachments/assets/8f2e1e11-c7e0-450e-880f-ff3d337a62dd)

I have uploaded it to the GD servers with the ID **112533336**. The uploaded test setup has some small differences from the recorded tables, but it should still showcase the same issues.

## Results
| Pickup2 | Order Results | Add \-1 | Add 0 | Add \+1 | Override 0 | Override 1000+/-1 | Spawn Branch |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| \-1 | 1265433 | 6541233 | 1233456 | 1233456 | 1233456 | 78 | 1122222 |
| 0 | 1265433 | 6541233 | 1233456 | 1233456 | 1233456 | 78 | 1122222 |
| 1 | 1233654 | 6541233 | 1233456 | 456 | 6541233 | 78 | 1111222 |
| 2 | 1233654 | 6541233 | 456 | 456 | 6541233 | 78 | 1111222 |
| 3 | 1233654 | 654 | 456 | 456 | 6541233 | 78 | 1111222 |
| 4 | 1243365 | 654 | 456 | 56 | 6541233 | 78 | 1111122 |
| 5 | 1254336 | 654 | 56 | 6 | 6541233 | 78 | 1111112 |
| 6 | 1265433 | 65 | 6 | 7 | 6541233 | 78 | 1111111 |
| 7 | 12765433 | 6 | 0 | 8 | 6541233 | 8 | 11111111 |
| 8 | 128765433 | 7 | 0 | 0 | 76541233 | 0 | 111111111 |
| 9 | 128765433 | 8 | 0 | 0 | 876541233 | 0 | 111111111 |
| 10 | 128765433 | 0 | 0 | 0 | 876541233 | 0 | 111111111 |

Order:
$Pickup1 🡒 1, 2 | Pickup2 🡒 8, 7, 6, 5, 4, 1, 2, 3, 3 |, 8, 7, 6, 5, 4, 1, 2, 3, 3$

## Suggestions
Resuming should update the item value without activating the Count trigger.
If you change an item value from inside a Count trigger with the same Item ID, the previous Count activation should be abandoned.

## Comments

While i would like to see this behavior changed, i have no way of predicting what such a change will do to existing levels. I don't think same item id changes with count are common so damage is likely to be minimal, but i have no way of knowing.
Personally, i would like to see these suggestions implemented as they would fix desync issues and add a way to skip or halt count activations early without having to use item comp to check the item value.