from class_auto import Auto
from grid import Grid
from types import *
from random import *


def load_cars(filename):
    ''' docstring placeholder '''
    with open(filename, "r") as file_cars:
        all_cars = []
        for line in file_cars:
            line = line.strip()
            if line.isdigit():
                id = line.strip()
                line = file_cars.readline()
                direction = line.strip()
                line = file_cars.readline().split()
                position = [[xy for xy in coordinate.split(',')] for coordinate in line]
                line = file_cars.readline()
                type = line.strip()
                auto = Auto(id, direction, position, type)
                all_cars.append(auto)
    return all_cars

load_cars('autos.txt')
