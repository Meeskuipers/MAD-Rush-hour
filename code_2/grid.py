from class_auto import Auto
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

Grid()
