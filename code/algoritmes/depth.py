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





def depth(size, bord):
    '''docstring placeholder '''
    grid = Grid(size,bord)
    possible_moves = []
    bool = True
    archive = {}
    archive[str(grid.grid)] = []
    currentstates = [grid.grid]
    while bool:
        checkkid = False
        grid.grid = currentstates[-1]
        grid.updatecars()
        possible_moves = possiblemoves(grid)
        path = archive[str(grid.grid)]
        for i in possible_moves:
            move(grid,i)
            grid.grid = grid.update()
            if str(grid.grid) not in archive.keys():
                print('hoi')
                currentstates.append(deepcopy(grid.grid))
                checkkid = True
                path.append(i)
                archive[str(grid.grid)] = path
                bool = win(grid,size)
                movecarback(grid,i)
                grid.update()
                break
            if checkkid == False:
                del currentstates[-1]
                bool = win(grid,size)

            movecarback(grid,i)
            grid.update()            

    print(len(archive[str(currentstates[-1])]))




def movecarback(grid,command):
    if command[1] == 'LEFT':
        move(grid,[command[0],'RIGHT',command[2]])

    if command[1] == 'RIGHT':
        move(grid,[command[0],'LEFT',command[2]])

    if command[1] == 'UP':
        move(grid,[command[0],'DOWN',command[2]])

    if command[1] == 'DOWN':
        move(grid,[command[0],'UP',command[2]])
