from classes.class_auto import Auto
from classes.grid import Grid
from classes.class_cache import Cache
from algoritmes.possiblemoves import possiblemoves
from random import *
from play import move
from copy import deepcopy


def breadth(size,bord):
    grid = Grid(size,bord)
    possible_moves = []
    counter = 0
    bool = True
    borddict = {}
    borddict[str(grid.grid)] = grid.grid

    while bool:
        counter += 1
        print('1')
        for x in borddict.keys():
            print('2')
            print(len(borddict.keys()))
            grid.grid = borddict[x]
            grid.updatecars()
            possible_moves = possiblemoves(grid)
            for i in range(len(possible_moves)):
                print('3')
                move(grid,[possible_moves[i][0],possible_moves[i][1],possible_moves[i][2]])
                grid.grid = grid.update()
                borddict[str(grid.grid)] = grid.grid
                movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])
                grid.grid = grid.update()
        borddict.pop(x, None)
        for z in borddict.keys():
            print('4')
            if z[2][5] == 6:
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
