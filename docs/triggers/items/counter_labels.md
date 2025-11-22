# Counter Labels

Displays the value of a given **ItemID** using a text label.
Displays the value of a timer instead if **Time Counter** is selected.

Special items like Main Time, Points and Attempts can be displayed if the respective option is selected. As these are items, they will not be displayed if **Time Counter** is selected.
Items -1, -2 and -3 can also be used to display the three special items Main Time, Points and Attempts.
By default the text of the label is aligned to center, **Left Align** and **Right Align** aligns the text to the left and right respectively.

If by any reason the label is not updated properly and displays the wrong value, a Pickup with the same ItemID will update the label even if it doesn't change the value of the item.
Points will not be displayed by a counter label until the first point is obtained.

Item labels will only be updated by a Pickup with the same ID, even if its outside the normal ID range.
ItemIDs outside the 0-9999 range refer to ID 0 or 9999 for both items and timers.