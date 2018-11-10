from Grid6x6 import *
from cars6x6 import *

#this function returns the occupied coordinates on the board
def occupiedfuntion(allcars):
    occupiedcoordinates = []
    for y in allcars
        for i in grid:
            if i in y:
                occupiedcoordinates.append(i)
    return occupiedcoordinates


#this function usees the occupied coordinates to find the free coordinates
def freefunction(currentgrid,allcars):
    freecoordinates = []
    occupated = occupiedfuntion()
    for i in currentgridgrid:
        if i not in occupated:
            freecoordinates.append(i)
    return freecoordinates

#test function below
#freefunction(grid, car1ver, car2ver, car3ver,car4ver,car1hor, car2hor, car3hor,car4hor,car5hor)
