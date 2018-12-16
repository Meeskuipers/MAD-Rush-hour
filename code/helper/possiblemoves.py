from code.classes.grid import Grid
from code.classes.class_auto import Auto


def possiblemoves(grid):
    movelist = []
    free_list = freelist(grid)
    movelist = grid.calculatemove(free_list)
    return movelist


def freelist(grid):
    freelist = []
    ycounter = 0
    for row in grid.grid:
        xcounter = 0
        for x in row:
            if x == 0:
                freelist.append([ycounter, xcounter])
            xcounter += 1
        ycounter += 1
    return freelist
