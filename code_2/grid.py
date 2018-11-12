#from class_auto import Auto
#from main import Main

class Grid():
    def __init__(self):
        self.grid = self.load_grid()
        self.car = self.add_cars()

    def load_grid(self):
        gridsize = 6
        grid = [[0] * gridsize for i in range(gridsize)]
        print(grid)

    def add_cars(self):
        print()

Grid()
