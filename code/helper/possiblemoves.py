from code.classes.grid import Grid
from code.classes.class_auto import Auto


def possiblemoves(grid):
    """
    De possiblemoves functie calculeert de mogelijke moves die op de gegeven
    gridconfiguratie mogelijk zijn.

    Dit wordt gedaan aan de hand van alle vrije plekken die bepaald worden in
    de freelist functie
    """
    movelist = []
    free_list = freelist(grid)
    movelist = grid.calculatemove(free_list)
    return movelist


def freelist(grid):
    """
    Freelist berekent de vrije posities binnen een instance van de class grid.

    Freelist heeft een argument: een istance van de class grid."""
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
