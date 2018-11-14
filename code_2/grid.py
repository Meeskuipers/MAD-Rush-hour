from class_auto import Auto
<<<<<<< HEAD
from main import Main

class Grid():
    def __init__(self, car_id, car_start_position):
        self.grid = self.load_grid()
        self.car = self.add_cars()

    def load_grid(self):
        gridsize = 6
        self.grid = [[0] * gridsize for i in range(gridsize)]
        return(self.grid)

    def add_cars(self, car_id, car_start_position):
        self.grid[car_start_position][car_start_position] = car_id
        print(self.grid)
=======

class Grid(object):
    def __init__(self, grid, car_id, car_start_position):
        self.grid = grid
        self.car = self.add_cars(car_start_position, car_id)
        self.car_id = car_id
        self.car_start_position = car_start_position

    def add_cars(self, car_start_position, car_id):
        for len in car_start_position:
            cor_1 = int(len[0])
            cor_2 = int(len[1])
            self.grid[cor_1][cor_2] = car_id
>>>>>>> 1c969fed1e690fac5fb9ee7f154123b517ead751

    def __str__(self):
        return(self.grid)
