"""
Classes
A class is a special type of value in an object-oriented programming language like Python. It's similar to a dictionary in that it usually stores other types inside itself.

# Defines a new class called "Soldier"
class Soldier:
    health = 5
    armor = 3
    damage = 2
Copy icon
Just like a string, integer or float, a class is a type, but instead of being a built-in type, your classes are custom types that you define.

An object is just an instance of a class type. For example:

health = 50
# health is an instance of an integer type
aragorn = Soldier()
# aragorn is an instance of the Soldier type (class)
Copy icon
"Classes" are custom new types that we define as the programmer. Each new instance of a class is an "object".

Example
class Archer:
    health = 40
    arrows = 10

# Create several instances of the Archer class
legolas = Archer()
bard = Archer()

# Print class properties
print(legolas.health) # 40
print(bard.arrows) # 10
Copy icon
Assignment
Create a class called Wall on line 1. It should have a property called armor that is initialized to 10 and a height that starts at 5.
"""

class Wall:
    armor = 10
    height = 5
