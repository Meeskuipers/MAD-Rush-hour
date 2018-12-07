from copy import deepcopy
from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import *
from code.helper.checkwin import win
from math import ceil
from code.helper.draw_2 import begin

def informedbreadth(size,bord):
    print('hoi')
#
# def breadth(size, bord):
#     grid = Grid(size, bord)
#     explored = set(str(grid.grid))
#     bool = True
#     states = [deepcopy(grid.grid)]
#     counter = 0
#
#     while bool:
#         counter += 1
#         x = states.pop(0)
#         grid.grid = deepcopy(x)
#         grid.updatecars()
#         possible_moves = possiblemoves(grid)
#         for i in range(len(possible_moves)):
#             move(grid,[possible_moves[i][0],possible_moves[i][1],
#             possible_moves[i][2]])
#             grid.update()
#
#             #if not str(grid.grid) in explored:
#             bool = win(grid, size)
#                 #explored.add(str(grid.grid))
#             states.append(deepcopy(grid.grid))
#             if not bool:
#                 break
#
#             movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])
#             grid.update()




def breadth(size,bord):
    grid = Grid(size,bord)
    possible_moves = []
    counter = 0
    bool = True
    borddict = {}
    borddict[str(grid.grid)] = grid.grid
    explored = {}

    while bool:
        parentset = ()
        counter += 1
        print(counter)
        gridlist = []
        for i in borddict.keys():
            grid.grid = borddict[i]
            grid.updatecars()
            possible_moves = possiblemoves(grid)
            for x in range(len(possible_moves)):
                move(grid,[possible_moves[x][0],possible_moves[x][1],possible_moves[x][2]])
                grid.grid = grid.update()
                gridlist.append(deepcopy(grid.grid))
                movecarback(grid,possible_moves[x][0],possible_moves[x][1],possible_moves[x][2])
                grid.update()
        bordddict = {}

        for y in gridlist:
            grid.grid = y
            grid.updatecars()
            borddict[str(y)] = y
            if not win(grid, size):
                bool = False
                begin([y])
                break



    print('it took' + " " + str(counter) + " " + "moves to win")











def movecarback(grid,car,direction,times):
    if direction == 'LEFT':
        move(grid,[car,'RIGHT',times])

    if str(direction) == 'RIGHT':
        move(grid,[car,'LEFT',times])

    if direction == 'UP':
        move(grid,[car,'DOWN',times])

    if direction == 'DOWN':
        move(grid,[car,'UP',times])
