# from class_auto import Auto
# from grid import Grid
# from types import *
#
# class Main():
#     def __init__(self):
#         self.cars = self.load_cars("autos.txt")
#         self.grid = self.load_grid()
#         self.grid = self.add_cars()
#
#     def run(self, grid, ):
#         print('deze ook')
#
#     def load_grid(self):
#         gridsize = 6
#         self.grid = [[0] * gridsize for i in range(gridsize)]
#         return(self.grid)
#
#     def load_cars(self, filename):
#         with open(filename, "r") as file_cars:
#             self.all_cars = []
#             for line in file_cars:
#                 position = []
#                 line = line.strip()
#                 if line.isdigit():
#                     id = line.strip()
#                     line = file_cars.readline()
#                     direction = line.strip()
#                     line = file_cars.readline().split()
#                     for coordinate in line:
#                         xy_list = []
#                         coordinate = coordinate.split(",")
#                         for xy in coordinate:
#                             xy_list.append(xy)
#                         position.append(xy_list)
#                     position = position
#                     line = file_cars.readline()
#                     type = line.strip()
#                     auto = Auto(id, direction, position, type)
#                     self.all_cars.append(auto)
#
#     def add_cars(self):
#         for car in self.all_cars:
#             Grid(self.grid, car.id, car.position)
#         return(self.grid)
#             #self.all_cars[id].inventory.add(one_item)
#
#     def won(self):
#         if self.grid[2][5] == '6':
#             return(True)
#         else:
#             return(False)
#
#     def play(self):
#         command = [[0,3][0,4]]
#         if self.freecoordinates(command):
#             print('self.grid')
#
#     def move(self, command):
#         if len(command) != 2:
#             return(False)
#         car = int(command[0])
#         direction = command[1]
#         return(self.all_cars[car-1].move_car(direction))
#
#
#
# if __name__ == "__main__":
#     main = Main()
#     main.play()
