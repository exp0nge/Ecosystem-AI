import random
from world import World


class Organisms(object):
    def __init__(self, inst_of_world, creature_type):
        self.inst_of_world = inst_of_world
        self.health = 50
        self.state = True
        self.age = 1
        self.current_position_x = 0
        self.current_position_y = 0
        self.init_placement(creature_type)

    def move(self):
        pass

    def eat(self):
        pass

    def reproduce(self):
        pass

    def check_if_movable(self, x_coordinate, y_coordinate):
        pass

    def init_placement(self, creature_type):
        for x in range(World.get_max_x(self.inst_of_world)):
            for y in range(World.get_max_y(self.inst_of_world)):
                if World.get_xy(self.inst_of_world, x, y) is None:
                    World.set_xy(self.inst_of_world, x, y, creature_type)
                    self.current_position_x = x
                    self.current_position_y = y
                    return

    def get_x(self):
        return random.randint(0, self.inst_of_world.get_max_x())

    def get_y(self):
        return random.randint(0, self.inst_of_world.get_max_x())
