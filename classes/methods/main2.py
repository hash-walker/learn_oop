"""
Methods Return Values
If a normal function doesn't return anything, it's typically not a very useful function. In contrast, methods often don't return anything explicitly because they can mutate the properties of the object instead. That's exactly what we did in the last assignment.

However, they can return values if you want! They're just functions with access to an object, after all.

class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(soldier_one.get_speed())
# prints "6"
Copy icon
Assignment
Add a .get_cost() method to your wall class. What do you think it should return? The cost of a wall is the product of its height and armor:

cost = armor * height
"""

class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        cost = self.armor * self.height
        return cost

    # don't touch below this line

    def fortify(self):
        self.armor *= 2
