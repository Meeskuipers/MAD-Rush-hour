from Grid6x6 import *
from cars6x6 import *
#The main file where the code comes together

freecoordinates = []
occupiedcoordinates = []

def freecoord(grid, car1ver, car2ver, car3ver,car4ver,car1hor, car2hor, car3hor,car4hor,car5hor):
    for i in grid:
        if i in car1ver:
            occupiedcoordinates.append(i)
        elif i in car2ver:
            occupiedcoordinates.append(i)
        elif i in car3ver:
            occupiedcoordinates.append(i)
        elif i in car4ver:
            occupiedcoordinates.append(i)
        elif i in car1hor:
            occupiedcoordinates.append(i)
        elif i in car2hor:
            occupiedcoordinates.append(i)
        elif i in car3hor:
            occupiedcoordinates.append(i)
        elif i in car4hor:
            occupiedcoordinates.append(i)
        elif i in car5hor:
            occupiedcoordinates.append(i)
    freecoordinates = [x for x in grid and x not in occupiedcoordinates]
