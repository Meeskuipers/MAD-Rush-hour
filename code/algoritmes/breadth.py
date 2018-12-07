from copy import deepcopy
from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import *
from code.helper.checkwin import win
from math import ceil
from code.helper.draw_2 import begin
from code.helper.play_2 import play_2

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
    startgrid = deepcopy(grid.grid)
    counter = 0
    bool = True
    borddict = {}
    borddict[str(grid.grid)] = grid.grid
    explored = {}
    explored[str(grid.grid)] = []

    while bool:
        parentset = ()
        counter += 1
        print(counter)
        gridlist = []

        for i in borddict.keys():
            grid.grid = borddict[i]
            grid.updatecars()
            possible_moves = possiblemoves(grid)
            for x in (possible_moves):
                move(grid,x)
                grid.grid = grid.update()
                if str(grid.grid) not in explored.keys():
                    gridlist.append(deepcopy(grid.grid))
                movecarback(grid,x)
                grid.update()

        for y in gridlist:
            grid.grid = y
            grid.updatecars()
            borddict[str(y)] = y
            if not win(grid, size):
                bool = False
                print(explored[str(y)])
                break



    print('it took' + " " + str(counter) + " " + "moves to win")











def movecarback(grid,command):
    if command[1] == 'LEFT':
        move(grid,[command[0],'RIGHT',command[2]])

    if command[1] == 'RIGHT':
        move(grid,[command[0],'LEFT',command[2]])

    if command[1] == 'UP':
        move(grid,[command[0],'DOWN',command[2]])

    if command[1] == 'DOWN':
        move(grid,[command[0],'UP',command[2]])
