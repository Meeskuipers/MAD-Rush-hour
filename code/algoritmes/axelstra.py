from code.classes.class_auto import Auto
from code.classes.grid import Grid
from code.classes.class_cache import Cache
from code.helper.possiblemoves import possiblemoves
from random import *
from code.helper.play import move
import copy


def informed(size,bord):
    grid = Grid(size, bord)
    startnode = Cache(grid.grid,[])
    cachelist = [startnode]

    while not grid.won():
        shortestnode = shortpath(cachelist)
        grid.grid = shortestnode.grid
        printgrid(grid)
        input()
        grid.updatecars()
        newpath = shortestnode.path
        possible_moves = []
        possible_moves = possiblemoves(grid)
        print(possible_moves)

        for i in range(len(possible_moves)):
            move(grid,[possible_moves[i][0],possible_moves[i][1],possible_moves[i][2]])
            grid.grid = grid.update()
            printgrid(grid)
            newpath.append(grid.grid)
            if checkgrid(grid,cachelist):
                newnode = Cache(grid.grid,newpath)
                cachelist.append(newnode)
            else:
                print('doesnt update cache')

            movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])

    shortestpath = checkpath(grid,cachelist)
    print(shortestpath)
    print(len(shortespath))


def checkgrid(grid,cachelist):
    gridlist = []
    for i in cachelist:
        gridlist.append(i.grid)
    if compare(grid.grid,gridlist):
        return False
    else:
        return True

def checkpath(grid,cachelist):
    pathlength = 2000
    cacheentry = cachelist[0]
    for i in cachelist:
        if checkgrid(grid,cachelist):
            if len(i.path) < pathlength:
                cacheentry = i
    return cacheentry


def shortpath(cachelist):
    pathlength = 2000
    cacheentry = cachelist[0]
    for i in cachelist:
            if len(i.path) < pathlength:
                cacheentry = i
    return cacheentry

def movecarback(grid,car,direction,times):
    if direction == 'LEFT':
        move(grid,[car,'RIGHT',times])

    if str(direction) == 'RIGHT':
        move(grid,[car,'LEFT',times])

    if direction == 'UP':
        move(grid,[car,'DOWN',times])

    if direction == 'DOWN':
        move(grid,[car,'UP',times])

def printgrid(grid):
    for row in grid.grid:
        for number in row:
            print("", end=" ")
            print(number, end=" ")
        print()

def compare(grid,gridlist):
    bool = True
    for i in gridlist:
        for x in range(len(grid)):
            for z in range(len(grid)):
                if grid[x][z] == i[x][z]:
                    bool = True
                else:
                    bool = False
                    break
            if bool == False:
                break
    return bool
