from Grid6x6 import *
from cars6x6 import *

#this function returns the occupied coordinates on the board
def occupiedfuntion():
    occupiedcoordinates = []
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

    return occupiedcoordinates


#this function usees the occupied coordinates to find the free coordinates
def freefunction(grid,car1ver, car2ver, car3ver,car4ver,car1hor, car2hor, car3hor,car4hor,car5hor):
    freecoordinates = []
    occupated = occupiedfuntion()
    for i in grid:
        if i not in occupated:
            freecoordinates.append(i)
    print (freecoordinates)
    return freecoordinates

#test function below
#freefunction(grid, car1ver, car2ver, car3ver,car4ver,car1hor, car2hor, car3hor,car4hor,car5hor)
