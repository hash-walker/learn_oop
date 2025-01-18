"""
Caravan
Siege weapons (battering rams, catapults, etc) are special units in Age of Dragons. Let's write the logic for how they move around the map.

Challenge
Complete the Siege, BatteringRam, and Catapult classes.

Siege Class
Constructor
Accepts two parameters (in order) and sets them as instance variables with the same name:

max_speed
efficiency
get_trip_cost()
Calculates the cost of a trip:

(distance / efficiency) * food_price

It costs food to move siege weapons, those things are heavy!

get_cargo_volume()
This method should be left empty. Use the pass keyword. Child classes will override this method.

Batteringram Class
Constructor
Calls the parent constructor, then sets the extra battering-ram-only instance variables as member variables.

get_trip_cost()
Uses the parent method to calculate the cost of food for a trip, plus the extra cost of carrying a load.

The formula for calculating the cost:

base_cost + (load_weight * 0.01)

get_cargo_volume()
Returns the cargo capacity in meters cubed. Get the volume of the battering-ram's "bed" (cargo area) by multiplying its area and depth. Every bed is 2 meters deep.

Catapult Class
Constructor
Calls the parent constructor, then sets the extra catapult-only instance variable as a member variable.

get_trip_cost()
Do not override this method.

get_cargo_volume()
Just returns the cargo capacity of the catapult. This is already set by the constructor.
"""

class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed,efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        base_cost = super().get_trip_cost(distance,food_price)
        return base_cost + (self.load_weight * 0.01)

    def get_cargo_volume(self):
        return self.bed_area * 2


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed,efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume
