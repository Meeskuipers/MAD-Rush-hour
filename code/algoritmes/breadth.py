from classes.class_auto import Auto
from classes.grid import Grid
from classes.class_cache import Cache
from algoritmes.possiblemoves import possiblemoves
from random import *
from play import move
from copy import deepcopy


def breadth(size,bord):
    grid = Grid(size,bord)
    gridlist = [grid.grid]
    possible_moves = []
    counter = 0
    bool = True

    while bool:
        children = []
        counter += 1
        print('1')
        for x in gridlist:
            print('2')
            print(len(gridlist))
            grid.grid = x
            grid.updatecars()
            possible_moves = possiblemoves(grid)
            for i in range(len(possible_moves)):
                print('3')
                move(grid,[possible_moves[i][0],possible_moves[i][1],possible_moves[i][2]])
                grid.grid = grid.update()
                children.append(deepcopy(grid.grid))
                movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])
                grid.grid = grid.update()
        gridlist = [a for a in children if a != x ]
        for z in children:
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
