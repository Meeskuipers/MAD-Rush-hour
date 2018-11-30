from classes.class_auto import Auto
from classes.grid import Grid
from classes.class_cache import Cache
from algoritmes.possiblemoves import possiblemoves
from random import *
from play import move


def breadth(size,bord):
    grid = Grid(size,bord)
    gridlist = [grid]
    possible_moves = []
    counter = 0
    bool = True

    while bool:
        counter += 1
        possible_moves = possiblemoves(grid)
        print(possible_moves)
        children = []
        for x in gridlist:
            grid.id = x
            grid.updatecars()
            for i in range(len(possible_moves)):
                move(grid,[possible_moves[i][0],possible_moves[i][1],possible_moves[i][2]])
                grid.grid = grid.update()
                children.append(grid.grid)
                movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])
        gridlist = children
        for z in children:
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
