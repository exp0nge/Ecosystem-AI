import time
import random


class World(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__map = [[None for x in range(self.__x)] for y in range(self.__y)]
        self.__total_count_of_plants = 0

        # organism control numbers
        self._plant = '~'
        self.__max_plants = 600
        self._plant_consumption_value = 2

        # herbivore
        self._herbivore = '+'
        self._max_herbivore = 500

        # carnivore
        self._carnivore = '-'
        self._max_carnivore = 400

    def set_xy(self, x_coordinate, y_coordinate, type_of_organism):
        self.__map[x_coordinate][y_coordinate] = type_of_organism

    def get_xy(self, x_coordinate, y_coordinate):
        return self.__map[x_coordinate][y_coordinate]

    @property
    def get_plant_consumption_value(self):
        return self._plant_consumption_value

    def get_max_x(self):
        return self.__x - 1

    def get_max_y(self):
        return self.__y - 1

    def remove_organism(self, x_coordinate, y_coordinate):
        if self.__map[x_coordinate][y_coordinate] is not None:
            self.__map[x_coordinate][y_coordinate] = None

    # plant stuff
    def maintain_plants(self):
        for i in range(0, 3):
            if self.__total_count_of_plants < self.__max_plants:
                x = random.randint(0, 31)
                y = random.randint(0, 31)
                if self.get_xy(x, y) is not self._plant:
                    self.set_xy(x, y, self._plant)
                    self.__total_count_of_plants += 1
            else:
                for x in range(self.__x):
                    for y in range(self.__y):
                        if self.get_xy(x, y) is self._plant:
                            self.__map[x][y] = None
                            self.__total_count_of_plants -= 1
                            break
        time.sleep(1)

    def get_plant_count(self):
        return self.__total_count_of_plants

    def print_map(self):
        for x in range(self.__x):
            for y in range(self.__y):
                out = self.__map[x][y]
                if out is None:
                    out = '.'
                print out,
            print
        print "---------------------------------------------------------------"
