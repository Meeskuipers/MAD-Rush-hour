from class_auto import Auto
#from grid import Grid
from types import *

class Main():
    def __init__(self):
        self.cars = self.load_cars("autos.txt")
        #sself.grid = self.add_cars()

    def run(self, grid, ):
        print('deze ook')

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
            print(self.all_cars[0].start_position)

    # def add_cars(self):
    #     print(self.all_cars[0].id)
    #     for car in self.all_cars:
    #         Grid(car.id, car.start_position)
    #         #self.self.all_cars[id].inventory.add(one_item)


Main = Main()
