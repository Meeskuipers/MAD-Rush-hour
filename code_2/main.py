from class_auto import Auto
from grid import Grid
from types import *

class Main():
    def __init__(self):
        self.cars = self.load_cars("autos.txt")
        self.grid = self.load_grid()
        self.grid = self.add_cars()

    def run(self, grid, ):
        print('deze ook')

    def load_grid(self):
        gridsize = 6
        self.grid = [[0] * gridsize for i in range(gridsize)]
        return(self.grid)

    def load_cars(self, filename):
        with open(filename, "r") as file_cars:
            self.all_cars = []
            for line in file_cars:
                start_position = []
                line = line.strip()
                if line.isdigit():
                    id = line
                    line = file_cars.readline()
                    direction = line
                    line = file_cars.readline().split()
                    for coordinate in line:
                        xy_list = []
                        coordinate = coordinate.split(",")
                        for xy in coordinate:
                            xy_list.append(xy)
                        start_position.append(xy_list)
                    start_position = start_position
                    line = file_cars.readline()
                    type = line
                    auto = Auto(id, direction, start_position, type)
                    self.all_cars.append(auto)
<<<<<<< HEAD
            print(self.all_cars)
=======
>>>>>>> 1c969fed1e690fac5fb9ee7f154123b517ead751

    def add_cars(self):
        for car in self.all_cars:
            Grid(self.grid, car.id, car.start_position)
        return(self.grid)
            #self.all_cars[id].inventory.add(one_item)

    def won(self):
        if self.grid[2][5] == '6':
            return(True)
        else:
            return(False)

    def play(self):
        print("Heee let's play!!!")
        for row in self.grid:
            for number in row:
                print("", end=" ")
                print(number, end=" ")
            print()
        while not self.won():
            command = input("> ").upper().split()
            move = self.move(command)
            if not move:
                print("Invalid move")

    def move(self, command):
        if len(command) != 2:
            return(False)
        if command[1] == 'LEFT':
            print("left")
            return True
        elif command[1] == 'RIGHT':
            print("right")
            return True
        elif command[1] == 'UP':
            print("up")
            return True
        elif command[1] == 'DOWN':
            print("DOWN")
            return True
        else:
            return False

if __name__ == "__main__":
    main = Main()
    main.play()
