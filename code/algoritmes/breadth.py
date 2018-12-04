from copy import deepcopy
from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import move

def breadth(size,bord):
    grid = Grid(size,bord)
    possible_moves = []
    counter = 0
    bool = True
    borddict = {}
    borddict[str(grid.grid)] = grid.grid

    while bool:
        counter += 1
        gridlist = []
        for x in borddict.keys():
            grid.grid = borddict[x]
            grid.updatecars()
            possible_moves = possiblemoves(grid)
            for i in range(len(possible_moves)):
                move(grid,[possible_moves[i][0],possible_moves[i][1],possible_moves[i][2]])
                grid.grid = grid.update()
                if borddict[x] != grid.grid:
                    gridlist.append(grid.grid)
                movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])
                grid.grid = grid.update()
        for y in gridlist:
            borddict[str(y)] = y
        borddict.pop(x, None)
        for z in borddict.keys():
            if borddict[z][2][5] == 6:
                bool = False
    print('it took' + str(counter) + "moves to win")


def movecarback(grid,car,direction,times):
    if direction == 'LEFT':
        move(grid,[car,'RIGHT',times])

    if str(direction) == 'RIGHT':
        move(grid,[car,'LEFT',times])

    if direction == 'UP':
        move(grid,[car,'DOWN',times])

    if direction == 'DOWN':
        move(grid,[car,'UP',times])
