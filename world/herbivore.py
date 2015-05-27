import time
from organisms import Organisms
import random


class Herbivore(Organisms):
    def __init__(self, inst_of_world):
        self.inst_of_world = inst_of_world
        super(Herbivore, self).__init__(self.inst_of_world, self.inst_of_world._herbivore)

    def move(self):
        x = super(Herbivore, self).get_x()
        y = super(Herbivore, self).get_y()
        if self.check_if_movable(x, y) is True:
            self.inst_of_world.remove_organism(self.current_position_x, self.current_position_y)
            self.inst_of_world.set_xy(x, y, self.inst_of_world._herbivore)
            self.current_position_x = x
            self.current_position_y = y

    def check_if_movable(self, x_coordinate, y_coordinate):
        new_area = self.inst_of_world.get_xy(x_coordinate, y_coordinate)
        if new_area is None:
            if new_area is self.inst_of_world._plant:
                self.eat()
                return True
            return True
        return False

    def eat(self):
        self.health += self.inst_of_world._plant_consumption_value

    def reproduce(self):
        pass
