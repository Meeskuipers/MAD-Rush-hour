from classes.class_auto import Auto
from classes.grid import Grid
from classes.class_cache import Cache
from algoritmes.possiblemoves import possiblemoves
from random import *
from play import move
import copy


def informed(size,bord):
    grid = Grid(size, bord)
    startnode = Cache(grid.grid,[])
    cachelist = [startnode]

    while not grid.won():
        possible_moves = []
        possible_moves = possiblemoves(grid)
        shortestnode = shortpath(cachelist)
        grid.grid = shortestnode.grid
        for i in range(len(possible_moves)):
            move(grid,[possible_moves[i][0],possible_moves[i][1],possible_moves[i][2]])
            cacheentry = checkpath(grid,cachelist)
            newpath = cacheentry.path
            newpath.append(grid.grid)
            grid.grid = grid.update()
            if checkgrid(grid,cachelist):
                newnode = Cache(grid.grid,newpath)
                cachelist.append(newnode)
            movecarback(grid,possible_moves[i][0],possible_moves[i][1],possible_moves[i][2])

    shortestpath = checkpath(grid,cachelist)
    print(shortestpath)
    print(len(shortespath))


def checkgrid(grid,cachelist):
    gridlist = []
    for i in cachelist:
        gridlist.append(i.grid)
    if grid.grid in gridlist:
        return False
    else:
        return True

def checkpath(grid,cachelist):
    pathlength = 2000
    cacheentry = cachelist[0]
    for i in cachelist:
        if grid == i.grid:
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
