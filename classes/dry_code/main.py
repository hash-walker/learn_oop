"""
DRY Code
Another "rule of thumb" for writing maintainable code is "Don't Repeat Yourself" (DRY). It just means that, when possible, you should avoid writing the same code in multiple places. Repeating code can be bad because:

If you need to change it, you have to change it in multiple places
If you forget to change it in one place, you'll have a bug
It's more work to write it over and over again
Assignment
Your manager noticed that there's a lot of repetitive code in the "Age of Dragons" code base. She asked you to update the fight_soldiers function so that the DPS (damage-per-second) calculation is only written once.

Notice how these two lines are practically identical:

soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
Copy icon
Create a new function called get_soldier_dps that takes a soldier and returns its DPS using the same logic as the lines above. Then, replace the two lines above with calls to get_soldier_dps.
"""

def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]

def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"


"""
DRY Code
Take a look at the code we wrote. We started with this:

soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
Copy icon
And refactored the code to look like this:

def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]
Copy icon
soldier_one_dps = get_soldier_dps(soldier_one)
soldier_two_dps = get_soldier_dps(soldier_two)
Copy icon
Don't Repeat Yourself (DRY)
We don't want too much of our code doing the same thing. When code is duplicated, it leads to many potential problems. In our example, let's pretend the soldier dictionary changed, and now the key that stores the "damage" value is called dmg.

In the first example, we would need to update two lines of code. In the second example, we only need to make the change in one place.

It's not a big deal when two lines are the same and exist right next to each other. However, imagine if we had done this several hundred times in ten or twenty different code files! All of a sudden, it makes a lot of sense to stop repeating yourself and write more reusable functions. We call that DRY code.
"""