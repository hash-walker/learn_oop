"""
Wizard Duel
Let's have ourselves a Wizard's duel.

Assignment
Add the following methods to the Wizard class.

get_fireballed()
This method operates on the instance of the class. It takes no inputs and returns no values explicitly, but it should remove 500 health from the wizard.

drink_mana_potion()
This method operates on the instance of the class. It takes no inputs and returns no values explicitly, but it should add 100 mana to the wizard's reserves.
"""
fireball_damage = 500
potion_mana = 100
fireball_cost = 50

fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target):
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")

        if self.mana >= fireball_cost:
            self.mana -= fireball_cost
            target.get_fireballed()
        

    def is_alive(self):
        if self.health > 0:
            return True

        return False

    def get_fireballed(self):
        self.health -= fireball_damage

    def drink_mana_potion(self):
        self.mana += potion_mana
