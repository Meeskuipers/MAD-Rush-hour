from code.classes.grid import Grid
from code.classes.class_auto import Auto


def possiblemoves(grid):
    moveList = []
    free_list = freelist(grid)
    for i in grid.all_cars:
        movesCar = i.calculatemove(free_list)
        for x in movesCar:
            moveList.append(x)
    return moveList

def freelist(grid):
    freelist = []
    ycounter = 0
    for row in grid.grid:
        xcounter = 0
        for x in row:
            if x == 0:
                freelist.append([ycounter,xcounter])
            xcounter += 1
        ycounter += 1
    return freelist
