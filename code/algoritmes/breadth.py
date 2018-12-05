from copy import deepcopy
from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import move
from code.helper.checkwin import win

def informedbreadth(size,bord):
    ''' Informedbreadth takes two arguments: size and bord. size is an integer
        defining the gridsize. bord is a string pointing to the according bord
        in data. informedbreadth works like a breadth first search algoritm
        without exploring previously visited nodes to reduce the space complexity
        '''
    grid = Grid(size, bord)
    possible_moves = []
    counter = 0
    bool = True
    borddict = {}
    borddict[str(grid.grid)] = deepcopy(grid.grid)
    explored = {}
    key = ''

    while bool:
        counter += 1
        print(counter)
        gridlist = []

        for x in borddict.keys():
            grid.grid = borddict[x]
            grid.updatecars()
            possible_moves = possiblemoves(grid)

            for i in range(len(possible_moves)):
                move(grid,[possible_moves[i][0],possible_moves[i][1],
                possible_moves[i][2]])
                grid.grid = grid.update()

                if borddict[x] != grid.grid:
                    gridlist.append(deepcopy(grid.grid))

                    if  explored.get(x,True):
                        explored[x] = [deepcopy(grid.grid)]

                    else:
                        visited = explored[x]
                        visited.append(deepcopy(grid.grid))
                        explored[x] = visited
                movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])
                grid.grid = grid.update()

        for y in gridlist:

            if not explored.get(str(y),0):
                borddict[str(y)] = y
        borddict.pop(x, None)

        for z in borddict.keys():
            if size == 6 and borddict[z][2][5] == 6:
                bool = False
                '''dit moet het path printen uit explored, maar gooit een key errorself.
                (victory wordt nog aan gewerkt tegen deze magic nubmers)
                explored is een dict met als keys een strin van een grid zoals borddict
                de values zijn echter een lijst met grids die de path naar die node moeten voorstellen'''
                #print(explored[z])
            elif size == 9 and borddict[z][4][8] == 15:
                bool = False

    print('it took' + " " + str(counter) + " " + "moves to win")
    return counter

def movecarback(grid,car,direction,times):
    if direction == 'LEFT':
        move(grid,[car,'RIGHT',times])

    if str(direction) == 'RIGHT':
        move(grid,[car,'LEFT',times])

    if direction == 'UP':
        move(grid,[car,'DOWN',times])

    if direction == 'DOWN':
        move(grid,[car,'UP',times])
