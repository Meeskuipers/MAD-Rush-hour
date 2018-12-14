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


def breadth(size, bord):
    grid = Grid(size, bord)
    possible_moves = []
    startgrid = deepcopy(grid.grid)
    counter = 0
    bool = True
    borddict = {}
    borddict[str(grid.grid)] = grid.grid
    explored = {}
    explored[str(grid.grid)] = []

    while bool:
        counter += 1
        print(counter)
        gridlist = []

        for i in borddict.keys():
            grid.grid = borddict[i]
            grid.updatecars()
            possible_moves = possiblemoves(grid)
            for x in (possible_moves):
                move(grid, x)
                grid.grid = grid.update()
                if str(grid.grid) not in explored.keys():
                    gridlist.append(deepcopy(grid.grid))
                    path = []
                    path = deepcopy(explored[i])
                    path.append(deepcopy(x))
                    explored[str(grid.grid)] = deepcopy(path)
                movecarback(grid, x)
                grid.update()

        for y in gridlist:
            grid.grid = y
            grid.updatecars()
            borddict[str(y)] = y
            if not win(grid, size):
                bool = False
                print(explored[str(y)])
                input('awaiting orders sir')
                play_2(size, bord, explored[str(y)])
                break

    print('it took' + " " + str(counter) + " " + "moves to win")


def movecarback(grid, command):
    if command[1] == 'LEFT':
        move(grid, [command[0], 'RIGHT', command[2]])

    if command[1] == 'RIGHT':
        move(grid, [command[0], 'LEFT', command[2]])

    if command[1] == 'UP':
        move(grid, [command[0], 'DOWN', command[2]])

    if command[1] == 'DOWN':
        move(grid, [command[0], 'UP', command[2]])
